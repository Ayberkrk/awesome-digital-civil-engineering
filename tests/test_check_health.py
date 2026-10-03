import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import check_health  # noqa: E402

NOW = datetime(2026, 10, 3, tzinfo=timezone.utc)


def repo_data(**overrides):
    data = {
        "archived": False,
        "full_name": "owner/repo",
        "license": {"spdx_id": "MIT"},
        "pushed_at": "2026-09-01T00:00:00Z",
    }
    data.update(overrides)
    return data


def checks(section="Structural Analysis and FEM", **overrides):
    problems = check_health.problems_for(section, "owner/repo", repo_data(**overrides), NOW)
    return [check for check, _ in problems]


class ProblemsForTest(unittest.TestCase):
    def test_healthy_repository_has_no_problems(self):
        self.assertEqual(checks(), [])

    def test_archived(self):
        self.assertEqual(checks(archived=True), ["archived"])

    def test_moved(self):
        self.assertEqual(checks(full_name="neworg/repo"), ["moved"])

    def test_case_change_is_not_a_move(self):
        self.assertEqual(checks(full_name="Owner/Repo"), [])

    def test_missing_license(self):
        self.assertEqual(checks(license=None), ["license"])

    def test_related_lists_are_exempt_from_license_check(self):
        self.assertEqual(checks("Related Awesome Lists", license=None), [])

    def test_stale_after_two_years(self):
        self.assertEqual(checks(pushed_at="2024-09-03T00:00:00Z"), ["stale"])

    def test_not_stale_within_two_years(self):
        self.assertEqual(checks(pushed_at="2024-10-10T00:00:00Z"), [])

    def test_datasets_are_exempt_from_staleness(self):
        self.assertEqual(checks("Open Datasets", pushed_at="2021-01-01T00:00:00Z"), [])

    def test_several_problems_are_all_reported(self):
        found = checks(archived=True, license=None, pushed_at="2020-01-01T00:00:00Z")
        self.assertEqual(found, ["archived", "license", "stale"])


class TranslationDriftTest(unittest.TestCase):
    SOURCE = (
        "## Contents\n\n- [Section](#section)\n\n## Section\n\n"
        "- [One](https://example.org/one#readme) - First.\n"
        "- [Two](https://example.org/two) - Second.\n"
    )

    def test_same_links_have_no_drift(self):
        translation = (
            "## Bolum\n\n"
            "- [One](https://example.org/one#readme) - Birinci.\n"
            "- [Two](https://example.org/two) - Ikinci.\n"
        )
        self.assertEqual(check_health.translation_drift(self.SOURCE, translation), [])

    def test_missing_and_extra_entries(self):
        translation = (
            "- [One](https://example.org/one#readme) - Birinci.\n"
            "- [Three](https://example.org/three) - Ucuncu.\n"
        )
        self.assertEqual(
            check_health.translation_drift(self.SOURCE, translation),
            [
                "missing from `README.tr.md`: https://example.org/two",
                "only in `README.tr.md`: https://example.org/three",
            ],
        )

    def test_table_of_contents_links_are_ignored(self):
        self.assertEqual(check_health.translation_drift(self.SOURCE, self.SOURCE), [])
        self.assertNotIn("#section", "".join(check_health.translation_drift(self.SOURCE, "")))


class FileReadingTest(unittest.TestCase):
    def write(self, text):
        handle = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8")
        handle.write(text)
        handle.close()
        self.addCleanup(Path(handle.name).unlink)
        return Path(handle.name)

    def test_read_entries_keeps_section_and_skips_contents(self):
        readme = self.write(
            "# Title\n\n## Contents\n\n- [Tools](#tools)\n\n## Tools\n\n"
            "- [Alpha](https://github.com/org/alpha#readme) - A tool.\n"
            "- [Site](https://example.org/) - Not on GitHub.\n"
            "- [Beta.jl](https://github.com/org/Beta.jl#readme) - See [org](https://github.com/org).\n"
        )
        with mock.patch.object(check_health, "README", readme):
            self.assertEqual(
                check_health.read_entries(),
                [("Tools", "Alpha", "org/alpha"), ("Tools", "Beta.jl", "org/Beta.jl")],
            )

    def test_read_ignores_parses_entries_and_comments(self):
        ignore = self.write(
            "# comment\n\nOrg/Repo  stale  Finished project  # trailing\norg/other license In a subfolder\n"
        )
        with mock.patch.object(check_health, "IGNORE_FILE", ignore):
            self.assertEqual(
                check_health.read_ignores(), {("org/repo", "stale"), ("org/other", "license")}
            )

    def test_read_ignores_rejects_unknown_check(self):
        ignore = self.write("org/repo  outdated  Some reason\n")
        with mock.patch.object(check_health, "IGNORE_FILE", ignore):
            with self.assertRaises(SystemExit):
                check_health.read_ignores()

    def test_read_ignores_requires_a_reason(self):
        ignore = self.write("org/repo  stale\n")
        with mock.patch.object(check_health, "IGNORE_FILE", ignore):
            with self.assertRaises(SystemExit):
                check_health.read_ignores()

    def test_repository_ignore_file_is_valid(self):
        self.assertTrue(check_health.read_ignores())


if __name__ == "__main__":
    unittest.main()
