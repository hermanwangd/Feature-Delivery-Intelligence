"""Verification accounting that keeps functional tests and release guards distinct."""

from __future__ import annotations

from copy import deepcopy


class VerificationAccountingError(ValueError):
    """Raised when a verification summary is incomplete or internally inconsistent."""


def _validate_result(label: str, result: dict) -> None:
    if not isinstance(result, dict):
        raise VerificationAccountingError(f"{label} must be an object")
    for key in ("passed", "failed", "skipped", "command"):
        if key not in result:
            raise VerificationAccountingError(f"{label}.{key} is required")
    for key in ("passed", "failed", "skipped"):
        value = result[key]
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise VerificationAccountingError(f"{label}.{key} must be a non-negative integer")
    if not isinstance(result["command"], str) or not result["command"].strip():
        raise VerificationAccountingError(f"{label}.command must be exact and non-empty")


def build_verification_summary(
    *,
    release: str,
    functional_tests: dict,
    release_guard_tests: dict,
    claims_not_established: list[str],
) -> dict:
    """Build an explicit summary from current command results, not inherited totals."""
    if not release:
        raise VerificationAccountingError("release is required")
    _validate_result("functional_tests", functional_tests)
    _validate_result("release_guard_tests", release_guard_tests)
    if not isinstance(claims_not_established, list):
        raise VerificationAccountingError("claims_not_established must be a list")

    functional = deepcopy(functional_tests)
    guards = deepcopy(release_guard_tests)
    total_passed = functional["passed"] + guards["passed"]
    total_failed = functional["failed"] + guards["failed"]
    total_skipped = functional["skipped"] + guards["skipped"]
    summary = {
        "release": release,
        "classification": "IMPLEMENTATION_OVERLAY_NOT_CANONICAL_RELEASE",
        "functional_tests": functional,
        "release_guard_tests": guards,
        "total_passed": total_passed,
        "total_failed": total_failed,
        "skipped": total_skipped,
        "commands": {
            "functional_tests": functional["command"],
            "release_guard_tests": guards["command"],
        },
        "status": "PASS" if total_failed == 0 else "FAIL",
        "claims_not_established": list(claims_not_established),
    }
    validate_verification_summary(summary)
    return summary


def validate_verification_summary(summary: dict) -> None:
    required = {
        "release",
        "classification",
        "functional_tests",
        "release_guard_tests",
        "total_passed",
        "total_failed",
        "skipped",
        "commands",
        "status",
        "claims_not_established",
    }
    if not isinstance(summary, dict):
        raise VerificationAccountingError("summary must be an object")
    missing = sorted(required - set(summary))
    if missing:
        raise VerificationAccountingError(f"missing explicit accounting field: {missing[0]}")

    _validate_result("functional_tests", summary["functional_tests"])
    _validate_result("release_guard_tests", summary["release_guard_tests"])

    expected_passed = summary["functional_tests"]["passed"] + summary["release_guard_tests"]["passed"]
    expected_failed = summary["functional_tests"]["failed"] + summary["release_guard_tests"]["failed"]
    expected_skipped = summary["functional_tests"]["skipped"] + summary["release_guard_tests"]["skipped"]
    if summary["total_passed"] != expected_passed:
        raise VerificationAccountingError("total_passed does not match current evidence")
    if summary["total_failed"] != expected_failed:
        raise VerificationAccountingError("total_failed does not match current evidence")
    if summary["skipped"] != expected_skipped:
        raise VerificationAccountingError("skipped does not match current evidence")

    expected_commands = {
        "functional_tests": summary["functional_tests"]["command"],
        "release_guard_tests": summary["release_guard_tests"]["command"],
    }
    if summary["commands"] != expected_commands:
        raise VerificationAccountingError("commands do not match exact current evidence commands")
    expected_status = "PASS" if expected_failed == 0 else "FAIL"
    if summary["status"] != expected_status:
        raise VerificationAccountingError("status does not match current evidence")
