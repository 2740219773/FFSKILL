import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import analyze_corpus as ac  # noqa: E402


class AnalyzeCorpusTests(unittest.TestCase):
    def test_safe_harbor_tail_is_removed(self):
        text = (
            "We completed a milestone. Next week we plan another test."
            "\nABOUT FARADAY FUTURE\n"
            "This legal tail may may could could subject to funding."
        )
        row = ac.analyze_document({"id": "x", "text": text})
        self.assertEqual(row["conditionality_count"], 1)  # plan only; legal tail removed
        self.assertGreater(row["next_event_count"], 0)

    def test_numbered_architecture_and_conditionality(self):
        text = (
            "S1 User Ecosystem and S2 Product are our two key tracks. "
            "We plan to begin the next phase, subject to funding and approval."
        )
        row = ac.analyze_document({"id": "x", "text": text})
        self.assertTrue(row["has_numbered_architecture"])
        self.assertGreaterEqual(row["s_label_count"], 2)
        self.assertGreaterEqual(row["conditionality_count"], 3)

    def test_result_meaning_next_chain(self):
        text = (
            "We completed the first delivery milestone. "
            "More importantly, this marks validation of the user workflow. "
            "Next week we will begin the next phase."
        )
        row = ac.analyze_document({"id": "x", "text": text})
        self.assertGreater(row["result_to_meaning_pairs"], 0)
        self.assertGreater(row["meaning_to_next_pairs"], 0)

    def test_chinese_redefinition(self):
        text = "这不是一个按钮数量的问题，而是实验人员与整套设备关系的问题。"
        row = ac.analyze_document({"id": "x", "text": text})
        self.assertGreater(row["redefinition_hits"], 0)

    def test_war_language_is_separate_from_numbering(self):
        calm = ac.analyze_document({"id": "a", "text": "S1 Product. S2 Delivery. Next week we test again."})
        war = ac.analyze_document({"id": "b", "text": "We launch an all-out offensive and fight this key battle at full sprint."})
        self.assertTrue(calm["has_numbered_architecture"])
        self.assertEqual(calm["war_sprint_count"], 0)
        self.assertGreater(war["war_sprint_count"], 0)


if __name__ == "__main__":
    unittest.main()
