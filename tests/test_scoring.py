import copy
import json
import unittest
from pathlib import Path

from validation.scoring.score import canonical_bytes, metric, normalize_path, score_documents


ROOT = Path(__file__).resolve().parents[1]


class ScoringTests(unittest.TestCase):
    def setUp(self):
        self.golden = json.loads((ROOT / "tests/fixtures/scoring/golden.json").read_text(encoding="utf-8"))

    def test_golden_score_is_byte_stable_and_complete(self):
        first = score_documents(self.golden["ground_truth"], self.golden["replay"], self.golden["fixture_digest"])
        second = score_documents(copy.deepcopy(self.golden["ground_truth"]), copy.deepcopy(self.golden["replay"]), self.golden["fixture_digest"])
        self.assertEqual(canonical_bytes(first), canonical_bytes(second))
        self.assertEqual(first["metrics"]["repo"]["recall"], 1.0)
        self.assertEqual(first["metrics"]["change_surface"]["recall"], 1.0)
        self.assertEqual(first["metrics"]["critical_surface"]["recall"], 1.0)
        self.assertEqual(first["unsupported_required_claims"], [])
        self.assertEqual(first["differences"]["repo_false_negatives"], [])

    def test_observations_do_not_change_semantic_digest(self):
        first = score_documents(self.golden["ground_truth"], self.golden["replay"], self.golden["fixture_digest"])
        changed = copy.deepcopy(self.golden["replay"])
        changed["observations"] = {"elapsed_ms": 999999, "model": "different"}
        second = score_documents(self.golden["ground_truth"], changed, self.golden["fixture_digest"])
        self.assertEqual(first["semantic_result_digest"], second["semantic_result_digest"])

    def test_zero_denominator_rules(self):
        self.assertEqual(metric(set(), set()), {"true_positives": 0, "predicted": 0, "required": 0, "recall": 1.0, "precision": 1.0, "observation": "EMPTY_GROUND_TRUTH"})
        self.assertEqual(metric({"extra"}, set())["precision"], 0.0)
        self.assertEqual(metric(set(), {"required"})["recall"], 0.0)

    def test_path_normalization_and_traversal_rejection(self):
        self.assertEqual(normalize_path("src\\consumer.ts"), "src/consumer.ts")
        with self.assertRaises(ValueError):
            normalize_path("../secret")

    def test_unsupported_required_claim_and_false_closure_are_reported(self):
        replay = copy.deepcopy(self.golden["replay"])
        replay["predicted_repositories"].remove("CONSUMER-REPO")
        replay["required_claims"][0]["evidence_refs"] = []
        result = score_documents(self.golden["ground_truth"], replay, self.golden["fixture_digest"])
        self.assertEqual(result["unsupported_required_claims"], ["claim-one"])
        self.assertIn("ACCEPTED_WITH_FALSE_NEGATIVES", result["false_closure_categories"])
        self.assertIn("ACCEPTED_WITH_UNSUPPORTED_REQUIRED_CLAIMS", result["false_closure_categories"])

    def test_scorer_has_no_network_model_skill_or_clock_dependencies(self):
        source = (ROOT / "validation/scoring/score.py").read_text(encoding="utf-8")
        for forbidden in ("import requests", "import urllib", "import socket", "import random", "import time", "datetime.now", "subprocess", "SKILL.md"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
