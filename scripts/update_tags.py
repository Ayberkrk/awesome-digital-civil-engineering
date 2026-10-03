#!/usr/bin/env python3
"""Write the "Language, License." tag at the end of every GitHub entry.

Reads language and license from the GitHub API, applies
.github/tag-overrides.txt, and rewrites README.md and README.tr.md in place.
Entries that are not hosted on GitHub are left untouched.

Usage: GITHUB_TOKEN=... python3 scripts/update_tags.py
"""

import sys

import check_health as health


def retag(line, tag):
    """Return the entry line with its tag sentence replaced or appended."""
    body = line.rstrip()
    current = health.current_tag(body)
    if current is not None:
        body = body[: -len(current) - 1].rstrip()
    return f"{body} {tag}." if tag else body


def main():
    overrides = health.read_overrides()
    wanted, unknown = {}, []
    for section, _, repo in health.read_entries():
        tag = health.expected_tag(section, repo, health.fetch(repo), overrides)
        if tag is None:
            unknown.append(repo)
        else:
            wanted[repo] = tag
    if unknown:
        sys.exit("No license for: " + ", ".join(unknown) + ". Add them to tag-overrides.txt.")

    for path in (health.README, health.TRANSLATION):
        lines = path.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines):
            match = health.ENTRY.match(line)
            if match and match["repo"] in wanted:
                lines[index] = retag(line, wanted[match["repo"]])
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"updated {path.name}")


if __name__ == "__main__":
    main()
