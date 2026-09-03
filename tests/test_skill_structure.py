from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


class SkillStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SKILL.read_text(encoding="utf-8")

    def test_frontmatter_and_identity(self):
        self.assertTrue(self.text.startswith("---\n"))
        self.assertIn("name: jia-yueting-perspective", self.text)
        self.assertIn("Historical-Core Runtime", self.text)

    def test_five_era_routes_exist(self):
        required = [
            "2012–2014",
            "2015–2016 H1",
            "2016 H2–2017",
            "2017–2023",
            "2024–2026",
        ]
        for era in required:
            with self.subTest(era=era):
                self.assertIn(era, self.text)

    def test_core_models_survive(self):
        required = [
            "Future-Back",
            "Category / Boundary Redefinition",
            "Ecosystem Reaction",
            "Third-Paradigm Creation",
            "Naming Creates Strategy",
            "Numbered Architecture",
            "Founder-Led Product Definition",
            "Distributed Execution + Centralized Inflection",
            "Milestone as Proof",
            "Crisis Reframing",
        ]
        for model in required:
            with self.subTest(model=model):
                self.assertIn(model, self.text)

    def test_safety_and_falsifiability_guards_exist(self):
        required = [
            "Failure Shadow",
            "V/C/M/O",
            "终局假设本身错了",
            "99%",
            "被反对所以正确",
            "事实准确",
        ]
        for guard in required:
            with self.subTest(guard=guard):
                self.assertIn(guard, self.text)

    def test_domestic_and_modern_speech_protocols_are_distinct(self):
        self.assertIn("2015–2016 H1 国内巅峰", self.text)
        self.assertIn("2024–2026 现代 FF", self.text)
        self.assertIn("第三范式 C", self.text)
        self.assertIn("已发生结果", self.text)
        self.assertIn("下一里程碑", self.text)

    def test_referenced_repo_files_exist(self):
        # Only validate repository-relative Markdown/Python/data paths enclosed in backticks.
        refs = set(
            re.findall(
                r"`((?:references|tests|tools|data)/[^`\n]+?)`",
                self.text,
            )
        )
        self.assertTrue(refs, "SKILL.md should reference supporting repository files")

        missing = []
        for ref in sorted(refs):
            # Ignore command fragments or descriptive suffixes; references in SKILL are expected to be paths.
            if any(ch in ref for ch in ["*", " "]):
                continue
            if not (ROOT / ref).exists():
                missing.append(ref)

        self.assertEqual([], missing, f"Missing files referenced by SKILL.md: {missing}")


if __name__ == "__main__":
    unittest.main()
