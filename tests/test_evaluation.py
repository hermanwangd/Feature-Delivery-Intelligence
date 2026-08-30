import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from validation.scoring.score import score_cohort, verify_evaluated_package, verify_manifest


ROOT = Path(__file__).resolve().parents[1]
FEATURES = ["calibration-01", "holdout-01", "holdout-02", "holdout-03", "holdout-04"]


class EvaluationFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ground_schema = json.loads((ROOT / "validation/scoring/schemas/ground-truth-change-set.schema.json").read_text(encoding="utf-8"))
        replay_schema = json.loads((ROOT / "validation/scoring/schemas/replay-result.schema.json").read_text(encoding="utf-8"))
        cls.ground_validator = Draft202012Validator(ground_schema, format_checker=FormatChecker())
        cls.replay_validator = Draft202012Validator(replay_schema, format_checker=FormatChecker())

    def test_exact_fixture_names_and_all_manifests_verify(self):
        feature_root = ROOT / "validation/features"
        self.assertEqual(sorted(path.name for path in feature_root.iterdir() if path.is_dir()), FEATURES)
        for feature in FEATURES:
            with self.subTest(feature=feature):
                manifest, digest = verify_manifest(feature_root / feature)
                self.assertEqual(manifest["feature_id"], feature)
                self.assertEqual(manifest["fixture_digest"], digest)

    def test_evaluator_formats_validate_and_boundaries_are_disjoint(self):
        for feature in FEATURES:
            with self.subTest(feature=feature):
                feature_dir = ROOT / "validation/features" / feature
                ground = json.loads((feature_dir / "evaluator-only/ground-truth-change-set.json").read_text(encoding="utf-8"))
                replay = json.loads((feature_dir / "investigator-visible/replay-output.json").read_text(encoding="utf-8"))
                boundary = json.loads((feature_dir / "evaluator-only/evidence-boundary.json").read_text(encoding="utf-8"))
                self.assertEqual(list(self.ground_validator.iter_errors(ground)), [])
                self.assertEqual(list(self.replay_validator.iter_errors(replay)), [])
                self.assertNotEqual(replay["investigator_id"], replay["reviewer_id"])
                self.assertTrue(replay["contexts_isolated"])
                self.assertEqual(boundary["investigator_access"], "DENIED")
                self.assertEqual(boundary["reviewer_access"], "DENIED")
                self.assertTrue(all(path.startswith("evaluator-only/") for path in boundary["answer_bearing_paths"]))
                self.assertEqual(replay["observations"]["execution_class"], "CONTRACT_FIXTURE_NOT_BLIND_REPLAY")

    def test_one_unchanged_evaluated_package_is_used_for_all_runs(self):
        expected = verify_evaluated_package(ROOT)
        digests = set()
        for feature in FEATURES:
            replay = json.loads((ROOT / "validation/features" / feature / "investigator-visible/replay-output.json").read_text(encoding="utf-8"))
            digests.add(replay["evaluated_package_digest"])
        self.assertEqual(digests, {expected})

    def test_contract_fixture_cohort_is_deterministic_and_thresholds_pass(self):
        first = score_cohort(ROOT / "validation/features")
        second = score_cohort(ROOT / "validation/features")
        self.assertEqual(first, second)
        self.assertEqual(first["repo_recall"], 1.0)
        self.assertEqual(first["critical_surface_recall"], 1.0)
        self.assertEqual(first["change_surface_recall"], 0.9)
        self.assertEqual(first["unsupported_required_claims"], [])
        self.assertEqual(first["threshold_result"], "PASS")


if __name__ == "__main__":
    unittest.main()
