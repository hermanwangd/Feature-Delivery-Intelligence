import pytest

from runtime import verification_accounting


def test_verification_accounting_exposes_required_api():
    required = {
        "VerificationAccountingError",
        "build_verification_summary",
        "validate_verification_summary",
    }
    missing = sorted(name for name in required if not hasattr(verification_accounting, name))
    assert missing == []


def valid_result(passed, failed=0, skipped=0, command="pytest -q"):
    return {
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "command": command,
    }


def test_summary_separates_functional_and_release_guard_counts():
    summary = verification_accounting.build_verification_summary(
        release="fdi-mvp-v0.4.6.2-overlay",
        functional_tests=valid_result(51, skipped=1, command="pytest -q tests/functional"),
        release_guard_tests=valid_result(4, command="pytest -q tests/release"),
        claims_not_established=["canonical source-tree release"],
    )
    assert summary["functional_tests"]["passed"] == 51
    assert summary["release_guard_tests"]["passed"] == 4
    assert summary["total_passed"] == 55
    assert summary["skipped"] == 1
    assert summary["status"] == "PASS"
    assert summary["commands"] == {
        "functional_tests": "pytest -q tests/functional",
        "release_guard_tests": "pytest -q tests/release",
    }
    verification_accounting.validate_verification_summary(summary)


def test_failed_test_makes_summary_fail():
    summary = verification_accounting.build_verification_summary(
        release="fdi-mvp-v0.4.6.2-overlay",
        functional_tests=valid_result(50, failed=1, command="pytest -q tests/functional"),
        release_guard_tests=valid_result(4, command="pytest -q tests/release"),
        claims_not_established=[],
    )
    assert summary["status"] == "FAIL"


@pytest.mark.parametrize("missing", ["functional_tests", "release_guard_tests", "total_passed", "skipped", "commands"])
def test_validator_rejects_missing_explicit_accounting_field(missing):
    summary = verification_accounting.build_verification_summary(
        release="fdi-mvp-v0.4.6.2-overlay",
        functional_tests=valid_result(51, command="pytest -q tests/functional"),
        release_guard_tests=valid_result(4, command="pytest -q tests/release"),
        claims_not_established=[],
    )
    summary.pop(missing)
    with pytest.raises(verification_accounting.VerificationAccountingError, match=missing):
        verification_accounting.validate_verification_summary(summary)


def test_validator_rejects_total_that_does_not_match_current_evidence():
    summary = verification_accounting.build_verification_summary(
        release="fdi-mvp-v0.4.6.2-overlay",
        functional_tests=valid_result(51, command="pytest -q tests/functional"),
        release_guard_tests=valid_result(4, command="pytest -q tests/release"),
        claims_not_established=[],
    )
    summary["total_passed"] = 140
    with pytest.raises(verification_accounting.VerificationAccountingError, match="total_passed"):
        verification_accounting.validate_verification_summary(summary)
