import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def readiness(case):
    return (
        case["closure_status"] == "CLOSED_WITHIN_DECLARED_SCOPE"
        and case["review_verdict"] == "PASS"
        and case["proposal_revision"] == case["reviewed_proposal_revision"]
        and case["material_unknowns"] == 0
        and case["spec_agent_decision"] == "SPEC_READY"
        and case["selector_passed"]
    )


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.text = (ROOT / "workflows/feature-closure.md").read_text(encoding="utf-8")
        self.cases = json.loads((ROOT / "tests/fixtures/workflow/cases.json").read_text(encoding="utf-8"))

    def test_only_complete_exact_chain_reaches_readiness(self):
        for case in self.cases:
            with self.subTest(case=case["name"]):
                self.assertEqual(readiness(case), case["expected_ready"])

    def test_out_of_scope_stops_before_read_and_invalidates_old_review(self):
        case = next(item for item in self.cases if item["name"] == "out-of-scope")
        self.assertFalse(case["source_read_attempted"])
        self.assertEqual(case["expected_reentry"], "SELECTOR_PREFLIGHT")
        self.assertNotEqual(case["proposal_revision"], case["reviewed_proposal_revision"])

    def test_manual_contract_has_no_runtime_or_competing_gate(self):
        self.assertIn("not an engine, orchestrator, service, scheduler, database, UI, control plane", self.text)
        self.assertIn("sole SPEC_READY decision", self.text)
        self.assertIn("No hidden runtime state", self.text)
        self.assertNotIn("Closure Engine", self.text)
        self.assertNotIn("closure-owned gate", self.text)


if __name__ == "__main__":
    unittest.main()
