import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_METADATA = {
    "name", "description", "version", "digest_algorithm", "digest", "digest_coverage", "source",
    "compatible_runtime", "owner", "authority", "status", "review_state", "reviewer", "last_reviewed",
    "next_review", "supersedes", "superseded_by",
}
REQUIRED_SECTIONS = [
    "# Purpose and applicability", "## Transition contract", "## Context selection",
    "## Capability bindings", "## Permissions and approvals", "## Procedure",
    "## Stopping conditions", "## Failure, escalation, and idempotency",
    "## Completion and evidence", "## Fixtures", "## Version and provenance",
]


def parse_skill(path):
    text = path.read_text(encoding="utf-8")
    _, frontmatter, body = text.split("---", 2)
    metadata = {}
    for line in frontmatter.strip().splitlines():
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"')
    return text, metadata, body


def covered_digest(text):
    covered = re.sub(r"(?m)^digest: [a-f0-9]{64}\n", "", text)
    return hashlib.sha256(covered.encode("utf-8")).hexdigest()


class SkillPackageTests(unittest.TestCase):
    def setUp(self):
        self.cases = json.loads((ROOT / "tests/fixtures/skills/cases.json").read_text(encoding="utf-8"))

    def test_exactly_five_complete_packages(self):
        paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual([path.parent.name for path in paths], sorted(self.cases))
        for path in paths:
            with self.subTest(skill=path.parent.name):
                text, metadata, body = parse_skill(path)
                self.assertEqual(set(metadata), REQUIRED_METADATA)
                self.assertEqual(metadata["name"], path.parent.name)
                self.assertEqual(metadata["status"], "ACTIVE")
                self.assertRegex(metadata["version"], r"^\d+\.\d+\.\d+$")
                self.assertEqual(metadata["digest_algorithm"], "SHA-256")
                self.assertEqual(metadata["digest"], covered_digest(text))
                for section in REQUIRED_SECTIONS:
                    self.assertIn(section, body)
                self.assertIn("positive", body.lower())
                self.assertIn("negative", body.lower())
                self.assertIn("trigger boundary", body.lower())
                self.assertIn("evaluator-only", body)
                self.assertNotIn("owns global workflow state", body)

    def test_positive_negative_and_trigger_boundary_contracts(self):
        for skill, case in self.cases.items():
            with self.subTest(skill=skill):
                body = (ROOT / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
                for key in ("positive", "negative", "trigger_boundary"):
                    self.assertIn(case[key], body)
                for phrase in case["must_include"]:
                    self.assertIn(phrase, body)


if __name__ == "__main__":
    unittest.main()
