"""Exercise broken package boundaries using isolated fixtures."""

import json
import tempfile
import unittest
from pathlib import Path

from check_skills import check_repo


class CheckSkillsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.entry = self.root / "skills/use-modern-python/SKILL.md"
        self.entry.parent.mkdir(parents=True)
        self.entry.write_text(
            '---\nname: use-modern-python\ndescription: "Python code reviews."\n---\n'
            '[references/guidelines.md](references/guidelines.md)\n', encoding="utf-8"
        )
        self.reference = self.entry.parent / "references/guidelines.md"
        self.reference.parent.mkdir()
        self.reference.write_text("# Python\nhttps://docs.python.org/3/\n", encoding="utf-8")
        for host in ("codex", "cursor", "claude"):
            manifest = self.root / f".{host}-plugin/plugin.json"
            manifest.parent.mkdir()
            manifest.write_text(json.dumps({"skills": "./skills/", "version": "1.0.0"}), encoding="utf-8")
        for filename in ("README.md", "README.zh-CN.md"):
            (self.root / filename).write_text("`use-modern-python`\n", encoding="utf-8")

    def test_valid_package(self):
        self.assertEqual(check_repo(self.root), [])

    def test_missing_reference(self):
        self.reference.unlink()
        self.assertTrue(any("missing references/" in error for error in check_repo(self.root)))

    def test_unknown_dependency(self):
        with self.entry.open("a", encoding="utf-8") as stream:
            stream.write("Use use-modern-missing.\n")
        self.assertTrue(any("unknown skill" in error for error in check_repo(self.root)))

    def test_resource_outside_installed_skill(self):
        (self.root / "outside.md").write_text("outside", encoding="utf-8")
        with self.entry.open("a", encoding="utf-8") as stream:
            stream.write("[outside](../../outside.md)\n")
        self.assertTrue(any("non-local resource" in error for error in check_repo(self.root)))

    def test_invalid_frontmatter(self):
        self.entry.write_text(self.entry.read_text().replace('"Python code reviews."', r'"Python\q"'), encoding="utf-8")
        self.assertTrue(any("quoted scalar" in error for error in check_repo(self.root)))

    def test_manifest_version_drift(self):
        manifest = self.root / ".cursor-plugin/plugin.json"
        manifest.write_text(json.dumps({"skills": "./skills/", "version": "2.0.0"}), encoding="utf-8")
        self.assertIn("plugin manifests: versions disagree", check_repo(self.root))

    def test_manifest_wrong_shape(self):
        manifest = self.root / ".cursor-plugin/plugin.json"
        manifest.write_text("[]", encoding="utf-8")
        self.assertTrue(any("expected a JSON object" in error for error in check_repo(self.root)))

    def test_inventory_drift(self):
        (self.root / "README.md").write_text("`use-modern-old`", encoding="utf-8")
        self.assertTrue(any("inventory mismatch" in error for error in check_repo(self.root)))


if __name__ == "__main__":
    unittest.main()
