import copy
import json
from pathlib import Path

import pytest

from scripts.governance_baseline import (
    load_baseline,
    render_governing_spec,
    verify_baseline,
)


ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = ROOT / "governance" / "baselines" / "GB-0001.yaml"


def test_candidate_baseline_verifies_and_generated_view_is_reproducible():
    baseline = load_baseline(BASELINE_PATH)

    report = verify_baseline(ROOT, baseline)

    assert report["integrity_failures"] == []
    assert report["summary"] == {
        "active_approved_baselines": 0,
        "compatibility_failures": 0,
        "competing_active_authorities": 0,
        "digest_failures": 0,
        "generated_view_failures": 0,
        "missing_approval_references": 0,
        "normative_conflicts": 0,
    }
    assert report["promotion_ready_for_independent_review"] is True
    assert report["promotion_blockers"] == [
        "INDEPENDENT_VALIDATION_REQUIRED",
        "HUMAN_APPROVAL_REQUIRED",
    ]
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


def test_approved_baseline_requires_current_pointer():
    baseline = load_baseline(BASELINE_PATH)
    broken = copy.deepcopy(baseline)
    broken["status"] = "APPROVED"

    report = verify_baseline(ROOT, broken, check_generated_view=False)

    assert any(item["code"] == "CURRENT_POINTER_MISMATCH" for item in report["integrity_failures"])


def test_baseline_file_is_json_compatible_yaml():
    parsed = json.loads(BASELINE_PATH.read_text())
    assert parsed["baseline_id"] == "GB-0001"
    assert parsed["status"] == "CANDIDATE"

