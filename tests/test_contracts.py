import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = {
    "IntentSpec": "intent-spec.schema.json",
    "EvidenceRecord": "evidence-record.schema.json",
    "CandidateRepoSet": "candidate-repo-set.schema.json",
    "ChangeSurfaceSet": "change-surface-set.schema.json",
    "ClosurePackage": "closure-package.schema.json",
    "ClosureReview": "closure-review.schema.json",
}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chain = load_json(ROOT / "tests/fixtures/contracts/valid-chain.json")
        cls.validators = {}
        for name, filename in SCHEMAS.items():
            schema = load_json(ROOT / "contracts" / filename)
            Draft202012Validator.check_schema(schema)
            if schema["$schema"] != "https://json-schema.org/draft/2020-12/schema":
                raise AssertionError(f"{filename} is not Draft 2020-12")
            cls.validators[name] = Draft202012Validator(schema, format_checker=FormatChecker())

    def test_all_six_positive_contract_fixtures_validate(self):
        self.assertEqual(set(self.chain), set(SCHEMAS))
        for name, instance in self.chain.items():
            with self.subTest(contract=name):
                errors = list(self.validators[name].iter_errors(instance))
                self.assertEqual(errors, [], "\n".join(error.message for error in errors))

    def test_all_negative_contract_fixtures_fail(self):
        cases = load_json(ROOT / "tests/fixtures/contracts/negative-cases.json")
        for case in cases:
            with self.subTest(case=case["name"]):
                instance = copy.deepcopy(self.chain[case["contract"]])
                target = instance
                for part in case["path"][:-1]:
                    target = target[part]
                target[case["path"][-1]] = case["value"]
                self.assertTrue(list(self.validators[case["contract"]].iter_errors(instance)))

    def test_cross_contract_chain_is_exact_and_non_circular(self):
        intent = self.chain["IntentSpec"]
        candidates = self.chain["CandidateRepoSet"]
        surfaces = self.chain["ChangeSurfaceSet"]
        package = self.chain["ClosurePackage"]
        review = self.chain["ClosureReview"]
        self.assertEqual(candidates["intent_spec_ref"]["record_id"], intent["record_id"])
        self.assertEqual(surfaces["candidate_repo_set_ref"]["record_id"], candidates["record_id"])
        self.assertEqual(package["change_surface_set_ref"]["record_id"], surfaces["record_id"])
        self.assertEqual(review["reviewed_closure_package_ref"]["record_id"], package["record_id"])
        self.assertNotEqual(review["investigator_identity"]["identity_id"], review["reviewer_identity"]["identity_id"])
        self.assertNotEqual(review["investigator_identity"]["context_id"], review["reviewer_identity"]["context_id"])
        self.assertNotIn("SPEC_READY", json.dumps(package))
        self.assertNotIn("SPEC_READY", json.dumps(review))

    def test_contract_set_is_exactly_six(self):
        self.assertEqual(sorted(path.name for path in (ROOT / "contracts").glob("*.schema.json")), sorted(SCHEMAS.values()))


if __name__ == "__main__":
    unittest.main()
