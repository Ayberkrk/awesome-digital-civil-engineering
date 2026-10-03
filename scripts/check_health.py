#!/usr/bin/env python3
"""Check the health of the GitHub projects linked from README.md.

Reports entries that are archived, have moved to a new address, have no
detectable license, or have not been pushed to for STALE_YEARS years. Also
reports entries whose "Language, License." tag does not match the repository,
and entries that differ between README.md and its translation.
Prints a Markdown report and, when running in GitHub Actions, sets the
`findings` output to the number of problems found.

Usage: GITHUB_TOKEN=... python3 scripts/check_health.py [report.md]
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
TRANSLATION = ROOT / "README.tr.md"
IGNORE_FILE = ROOT / ".github" / "health-ignore.txt"
OVERRIDES_FILE = ROOT / ".github" / "tag-overrides.txt"

STALE_YEARS = 2
# Datasets are published once and rarely change, so a quiet repository is
# not a sign of abandonment there.
STALE_EXEMPT_SECTIONS = {"Open Datasets"}
# Other lists are linked for scope, not vetted against the inclusion criteria.
LICENSE_EXEMPT_SECTIONS = {"Related Awesome Lists"}

# Language says little about a dataset or a course, so these carry the license only.
LICENSE_ONLY_SECTIONS = {"Open Datasets", "Learning Resources"}
UNTAGGED_SECTIONS = {"Related Awesome Lists"}

CHECKS = ("archived", "moved", "license", "stale", "tag")
LICENSE_TAG = re.compile(r"MIT|Unlicense|Custom|[A-Za-z0-9]+(-[A-Za-z0-9.]+)+")
LANGUAGE_TAG = re.compile(r"[A-Za-z+#]+")
LINK = re.compile(r"^- \[[^\]]+\]\((?P<url>[^)#][^)]*)\)", re.M)
ENTRY = re.compile(r"^- \[(?P<name>[^\]]+)\]\(https://github\.com/(?P<repo>[\w.-]+/[\w.-]+?)(?:#[^)]*)?\)")


def read_entries():
    """Return (section, name, owner/repo) for every GitHub entry in the list."""
    entries, section = [], None
    for line in README.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        match = ENTRY.match(line)
        if match and section not in (None, "Contents"):
            entries.append((section, match["name"], match["repo"]))
    return entries


def read_tags(path=None):
    """Return the text of the tag sentence for every GitHub entry, by owner/repo."""
    tags = {}
    for line in (path or README).read_text(encoding="utf-8").splitlines():
        match = ENTRY.match(line)
        if match:
            tags[match["repo"]] = current_tag(line)
    return tags


def current_tag(line):
    """Return the trailing "Language, License" sentence of an entry, or None."""
    sentence = line.rstrip().rstrip(".").rsplit(". ", 1)[-1]
    parts = sentence.split(", ")
    if len(parts) > 2 or not LICENSE_TAG.fullmatch(parts[-1]):
        return None
    if len(parts) == 2 and not LANGUAGE_TAG.fullmatch(parts[0]):
        return None
    return sentence


def read_overrides():
    """Return {(owner/repo, field): value} from the tag overrides file."""
    overrides = {}
    if not OVERRIDES_FILE.exists():
        return overrides
    for number, raw in enumerate(OVERRIDES_FILE.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 3 or parts[1] not in ("language", "license"):
            sys.exit(f"{OVERRIDES_FILE.name}:{number}: expected 'owner/repo field value'")
        overrides[(parts[0].lower(), parts[1])] = parts[2]
    return overrides


def expected_tag(section, repo, data, overrides):
    """Return the tag an entry should carry, "" if none, or None if the license is unknown."""
    if section in UNTAGGED_SECTIONS:
        return ""
    detected = (data["license"] or {}).get("spdx_id")
    if detected == "NOASSERTION":
        detected = None
    license_name = overrides.get((repo.lower(), "license")) or detected
    if license_name is None:
        return None
    language = overrides.get((repo.lower(), "language")) or data["language"]
    if section in LICENSE_ONLY_SECTIONS or language in (None, "none"):
        return license_name
    return f"{language}, {license_name}"


def read_ignores():
    """Return the set of (owner/repo, check) pairs accepted in the ignore file."""
    ignores = set()
    if not IGNORE_FILE.exists():
        return ignores
    for number, raw in enumerate(IGNORE_FILE.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split(None, 2)
        if len(parts) < 3 or parts[1] not in CHECKS:
            sys.exit(f"{IGNORE_FILE.name}:{number}: expected 'owner/repo check reason'")
        ignores.add((parts[0].lower(), parts[1]))
    return ignores


def translation_drift(source, translation):
    """Return messages for entry links present in only one of the two texts."""
    original = [match["url"] for match in LINK.finditer(source)]
    translated = [match["url"] for match in LINK.finditer(translation)]
    drift = [f"missing from `{TRANSLATION.name}`: {url}" for url in original if url not in translated]
    drift += [f"only in `{TRANSLATION.name}`: {url}" for url in translated if url not in original]
    return drift


def fetch(repo):
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "list-health-check"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def problems_for(section, repo, data, now, tags=None, overrides=None):
    """Yield (check, message) for every problem found on one repository."""
    if data["archived"]:
        yield "archived", "repository is archived"
    if data["full_name"].lower() != repo.lower():
        yield "moved", f"now lives at `{data['full_name']}`"
    if data["license"] is None and section not in LICENSE_EXEMPT_SECTIONS:
        yield "license", "no license detected in the repository root"
    if tags is not None:
        wanted = expected_tag(section, repo, data, overrides or {})
        if wanted is None:
            yield "tag", "license cannot be read from GitHub, add it to `.github/tag-overrides.txt`"
        elif wanted and tags.get(repo) != wanted:
            yield "tag", f"tag should be `{wanted}.`"
    pushed = datetime.fromisoformat(data["pushed_at"].replace("Z", "+00:00"))
    if section not in STALE_EXEMPT_SECTIONS and (now - pushed).days > STALE_YEARS * 365:
        yield "stale", f"last push on {pushed:%Y-%m-%d}"


def main():
    now = datetime.now(timezone.utc)
    ignores = read_ignores()
    entries = read_entries()
    tags = read_tags()
    overrides = read_overrides()
    findings, errors = [], []

    for section, name, repo in entries:
        try:
            data = fetch(repo)
        except urllib.error.HTTPError as error:
            if error.code == 404:
                findings.append((section, name, repo, "repository not found"))
            else:
                errors.append(f"{repo}: HTTP {error.code}")
            continue
        except urllib.error.URLError as error:
            errors.append(f"{repo}: {error.reason}")
            continue
        for check, message in problems_for(section, repo, data, now, tags, overrides):
            if (repo.lower(), check) not in ignores:
                findings.append((section, name, repo, message))

    drift = []
    if TRANSLATION.exists():
        drift = translation_drift(
            README.read_text(encoding="utf-8"), TRANSLATION.read_text(encoding="utf-8")
        )

    lines = [f"Checked {len(entries)} GitHub entries on {now:%Y-%m-%d}.", ""]
    if findings:
        lines += ["| Section | Entry | Problem |", "|---|---|---|"]
        lines += [f"| {s} | [{n}](https://github.com/{r}) | {m} |" for s, n, r, m in findings]
        lines += [
            "",
            "Fix or remove each entry, or accept it by adding a line with a reason to "
            "`.github/health-ignore.txt`.",
        ]
    if drift:
        lines += [""] if findings else []
        lines += ["The translation is out of sync:", ""] + [f"- {d}" for d in drift]
    if not findings and not drift:
        lines.append("No problems found.")
    if errors:
        lines += ["", "Could not check:", ""] + [f"- {e}" for e in errors]
    report = "\n".join(lines) + "\n"

    print(report, end="")
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(report, encoding="utf-8")
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
            output.write(f"findings={len(findings) + len(drift)}\n")
    # Fail only when the check itself could not run, so API hiccups are visible.
    return 1 if errors and len(errors) == len(entries) else 0


if __name__ == "__main__":
    sys.exit(main())
