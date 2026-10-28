"""Offline contract tests for the documented skill inventory and safety rules."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
ORCHESTRATOR = (ROOT / "SKILL.md").read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
    def test_every_documented_skill_file_exists(self):
        section = README.split("## Skill files currently included", 1)[1].split(
            "## Evidence and risk standards", 1
        )[0]
        paths = re.findall(r"`((?:skills/[^`]+\\.md)|SKILL\\.md)`", section)

        self.assertEqual(paths, [
            "SKILL.md",
            "skills/market-regime/SKILL.md",
            "skills/stock-deep-dive/SKILL.md",
        ])
        for relative_path in paths:
            with self.subTest(path=relative_path):
                self.assertTrue((ROOT / relative_path).is_file())

    def test_readme_discloses_non_standalone_workflows(self):
        self.assertIn(
            "`stock-screener` and `conviction-score` are workflow sections",
            README,
        )
        self.assertIn("not separate standalone skill files yet", README)

    def test_orchestrator_requires_dated_evidence_and_uncertainty(self):
        required_phrases = (
            "explicit as-of date, time, and timezone",
            "Do not invent current prices",
            "not a probability of profit",
            "Do not place trades",
            "Do not fabricate sources",
        )
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, ORCHESTRATOR)


if __name__ == "__main__":
    unittest.main()
