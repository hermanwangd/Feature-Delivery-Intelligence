import copy
import json
from pathlib import Path

import pytest

from scripts.governance_baseline import (
    baseline_digest,
    load_baseline,
    render_governing_spec,
    verify_baseline,
)


ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = ROOT / "governance" / "baselines" / "GB-0001.yaml"
PROMOTION_PATH = ROOT / "governance" / "reconciliation" / "GB-0001-PROMOTION.json"


def test_approved_baseline_verifies_and_generated_view_is_reproducible():
    baseline = load_baseline(BASELINE_PATH)

    report = verify_baseline(ROOT, baseline)

    assert baseline["status"] == "APPROVED"
    assert baseline["baseline_digest"] == (
        "96d5f43a3c50ba2697907d4170f01997ab1b21e60f01e67c27ae5ed8f9fdc48e"
    )
    assert (ROOT / "governance" / "CURRENT").read_text().strip() == "GB-0001"
    assert report["integrity_failures"] == []
    assert report["summary"] == {
        "active_approved_baselines": 1,
        "compatibility_failures": 0,
        "competing_active_authorities": 0,
        "digest_failures": 0,
        "generated_view_failures": 0,
        "missing_approval_references": 0,
        "normative_conflicts": 0,
    }
    assert report["promotion_ready_for_independent_review"] is False
    assert report["promotion_blockers"] == []
    expected = render_governing_spec(ROOT, baseline)
    actual = (ROOT / "governance" / "GOVERNING-SPEC.md").read_text()
    assert actual == expected
    assert "GENERATED — DO NOT EDIT" in actual
    assert "PA-01-MINIMAL-PRODUCT-SEMANTICS" not in actual


def test_digest_mismatch_fails_closed():
    baseline = load_baseline(BASELINE_PATH)
    broken = copy.deepcopy(baseline)
    broken["modules"][0]["files"][0]["sha256"] = "0" * 64

    report = verify_baseline(ROOT, broken, check_generated_view=False)

    assert report["summary"]["digest_failures"] == 1
    assert any(item["code"] == "DIGEST_MISMATCH" for item in report["integrity_failures"])


def test_candidate_selected_as_approved_fails_closed():
    baseline = load_baseline(BASELINE_PATH)
    broken = copy.deepcopy(baseline)
    broken["modules"][0]["status"] = "CANDIDATE"

    report = verify_baseline(ROOT, broken, check_generated_view=False)

    assert any(
        item["code"] == "CANDIDATE_SELECTED_AS_APPROVED"
        for item in report["integrity_failures"]
    )


def test_missing_approval_reference_fails_closed():
    baseline = load_baseline(BASELINE_PATH)
    broken = copy.deepcopy(baseline)
    broken["modules"][0]["approval_ref"] = ""

    report = verify_baseline(ROOT, broken, check_generated_view=False)

    assert report["summary"]["missing_approval_references"] == 1


def test_approved_baseline_requires_current_pointer(tmp_path):
    baseline = load_baseline(BASELINE_PATH)
    (tmp_path / "governance").mkdir()
    (tmp_path / "governance" / "CURRENT").write_text("UNSET\n")

    report = verify_baseline(tmp_path, baseline, check_generated_view=False)

    assert any(item["code"] == "CURRENT_POINTER_MISMATCH" for item in report["integrity_failures"])


def test_baseline_file_is_json_compatible_yaml():
    parsed = json.loads(BASELINE_PATH.read_text())
    assert parsed["baseline_id"] == "GB-0001"
    assert parsed["status"] == "APPROVED"


def test_promotion_provenance_preserves_the_approved_identity_tuple():
    baseline = load_baseline(BASELINE_PATH)
    promotion = json.loads(PROMOTION_PATH.read_text())

    assert promotion == {
        "approval": {
            "actor": "Herman Wang",
            "comment_id": "01a0619a-f3aa-748f-94c2-f298c6604994",
            "decision": "APPROVE LIFECYCLE_IN_DIGEST_NEW_REVISION_V1 AND THE EXACT TUPLE ABOVE",
            "issue": "HERM-228",
        },
        "approved_digest": "96d5f43a3c50ba2697907d4170f01997ab1b21e60f01e67c27ae5ed8f9fdc48e",
        "base_commit": "44e953c3630e8a0078000c2d00eba28f7fc03220",
        "baseline_id": "GB-0001",
        "candidate_commit": "8444d0dbbc0a93dbfe66f95c61ebfd9a2a8aacbc",
        "digest_algorithm": "sha256(canonical-json-without-baseline_digest)",
        "independent_evidence_sha256": "55b725c119a733f6dce063fe92e8a30a7f373b83cbbfb462592a6b314982b5ae",
        "pointer": "GB-0001",
        "predecessor_candidate_digest": "71a4e5ef5098ac58a2591b67894eeb0d25e4d444670e07a258228b199f49c6a5",
        "promotion_identity_mechanism": "LIFECYCLE_IN_DIGEST_NEW_REVISION_V1",
        "target_status": "APPROVED",
    }
    assert baseline_digest(baseline) == promotion["approved_digest"]
    assert baseline["baseline_digest"] == promotion["approved_digest"]
    assert baseline["status"] == promotion["target_status"]
    assert (ROOT / "governance" / "CURRENT").read_text().strip() == promotion["pointer"]
