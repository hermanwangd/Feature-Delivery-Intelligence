#!/usr/bin/env python3
"""Generate and fail-closed verify an FDI governing baseline."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_baseline(path: Path) -> Dict[str, Any]:
    """Load JSON-compatible YAML without adding a YAML runtime dependency."""
    return json.loads(path.read_text(encoding="utf-8"))


def baseline_digest(baseline: Dict[str, Any]) -> str:
    payload = copy.deepcopy(baseline)
    payload.pop("baseline_digest", None)
    normalized = json.dumps(
        payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    return _sha256(normalized)


def _tree_digest(root: Path, files: Iterable[Dict[str, str]]) -> str:
    rows = []
    for item in sorted(files, key=lambda entry: entry["path"]):
        rel = item["path"]
        digest = _sha256((root / rel).read_bytes())
        rows.append(f"{digest}  {rel}\n")
    return _sha256("".join(rows).encode("utf-8"))


def render_governing_spec(root: Path, baseline: Dict[str, Any]) -> str:
    lines = [
        "# FDI Governing Specification",
        "",
        "> GENERATED — DO NOT EDIT",
        f"> baseline_id: {baseline['baseline_id']}",
        f"> baseline_status: {baseline['status']}",
        f"> baseline_digest: {baseline['baseline_digest']}",
        "",
        "This view contains only baseline-selected normative modules. The baseline",
        "selects authority; the exact modules below define semantics.",
        "",
    ]
    for module in baseline["modules"]:
        lines.extend(
            [
                f"## {module['id']} — {module['authority_domain']}",
                "",
                f"- Semantic version: `{module['semantic_version']}`",
                f"- Approval: `{module['approval_ref']}`",
                f"- Compatibility: `{module['compatibility']}`",
                "",
            ]
        )
        for item in module["files"]:
            rel = item["path"]
            content = (root / rel).read_text(encoding="utf-8").rstrip("\n")
            lines.extend(
                [
                    f"### Source: `{rel}`",
                    "",
                    f"SHA-256: `{item['sha256']}`",
                    "",
                    content,
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"


def verify_baseline(
    root: Path,
    baseline: Dict[str, Any],
    *,
    check_generated_view: bool = True,
) -> Dict[str, Any]:
    failures: List[Dict[str, str]] = []

    def fail(code: str, detail: str) -> None:
        failures.append({"code": code, "detail": detail})

    expected_baseline_digest = baseline_digest(baseline)
    if baseline.get("baseline_digest") != expected_baseline_digest:
        fail(
            "BASELINE_DIGEST_MISMATCH",
            f"expected {expected_baseline_digest}; recorded {baseline.get('baseline_digest')}",
        )

    seen_domains = set()
    digest_failure_count = 0
    missing_approval_count = 0
    competing_authority_count = 0
    for module in baseline.get("modules", []):
        module_id = module.get("id", "UNKNOWN")
        domain = module.get("authority_domain")
        if domain in seen_domains:
            competing_authority_count += 1
            fail("COMPETING_ACTIVE_AUTHORITY", f"duplicate domain {domain}")
        seen_domains.add(domain)

        if module.get("status") != "APPROVED":
            fail(
                "CANDIDATE_SELECTED_AS_APPROVED",
                f"{module_id} has status {module.get('status')}",
            )
        if not str(module.get("approval_ref", "")).strip():
            missing_approval_count += 1
            fail("MISSING_APPROVAL_REFERENCE", module_id)

        for item in module.get("files", []):
            rel = item["path"]
            source = root / rel
            if not source.is_file():
                digest_failure_count += 1
                fail("MISSING_SOURCE", rel)
                continue
            actual = _sha256(source.read_bytes())
            if actual != item.get("sha256"):
                digest_failure_count += 1
                fail(
                    "DIGEST_MISMATCH",
                    f"{rel}: expected {item.get('sha256')}; actual {actual}",
                )

        if module.get("tree_sha256"):
            try:
                actual_tree = _tree_digest(root, module.get("files", []))
            except FileNotFoundError:
                actual_tree = "MISSING_SOURCE"
            if actual_tree != module["tree_sha256"]:
                digest_failure_count += 1
                fail(
                    "TREE_DIGEST_MISMATCH",
                    f"{module_id}: expected {module['tree_sha256']}; actual {actual_tree}",
                )

    compatibility_failure_count = 0
    for check in baseline.get("compatibility_checks", []):
        if check.get("result") != "PASS":
            compatibility_failure_count += 1
            fail(
                "COMPATIBILITY_FAILURE",
                f"{check.get('id')}: {check.get('result')}",
            )

    recorded_counts = baseline.get("promotion", {}).get("observed_counts", {})
    normative_conflicts = int(recorded_counts.get("normative_conflicts", 0))
    if normative_conflicts:
        fail("NORMATIVE_CONFLICT", str(normative_conflicts))
    digest_failure_count += int(recorded_counts.get("digest_failures", 0))
    compatibility_failure_count += int(
        recorded_counts.get("compatibility_failures", 0)
    )
    competing_authority_count += int(
        recorded_counts.get("competing_active_authorities", 0)
    )

    current = (root / "governance" / "CURRENT").read_text(encoding="utf-8").strip()
    active_approved_baselines = 1 if baseline.get("status") == "APPROVED" else 0
    expected_current = baseline["baseline_id"] if active_approved_baselines else "UNSET"
    if current != expected_current:
        fail(
            "CURRENT_POINTER_MISMATCH",
            f"expected {expected_current}; actual {current}",
        )

    generated_view_failure_count = 0
    if check_generated_view:
        generated_path = root / "governance" / "GOVERNING-SPEC.md"
        expected_view = render_governing_spec(root, baseline)
        if not generated_path.is_file() or generated_path.read_text(
            encoding="utf-8"
        ) != expected_view:
            generated_view_failure_count = 1
            fail("GENERATED_VIEW_DRIFT", str(generated_path.relative_to(root)))

    summary = {
        "active_approved_baselines": active_approved_baselines,
        "compatibility_failures": compatibility_failure_count,
        "competing_active_authorities": competing_authority_count,
        "digest_failures": digest_failure_count,
        "generated_view_failures": generated_view_failure_count,
        "missing_approval_references": missing_approval_count,
        "normative_conflicts": normative_conflicts,
    }
    clean = not failures
    blockers = []
    if clean and baseline.get("status") == "CANDIDATE":
        blockers = ["INDEPENDENT_VALIDATION_REQUIRED", "HUMAN_APPROVAL_REQUIRED"]
    return {
        "baseline_id": baseline.get("baseline_id"),
        "baseline_status": baseline.get("status"),
        "baseline_digest": expected_baseline_digest,
        "source_revision": baseline.get("source_revision"),
        "summary": summary,
        "integrity_failures": failures,
        "promotion_ready_for_independent_review": clean
        and baseline.get("status") == "CANDIDATE",
        "promotion_blockers": blockers,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--baseline", default="governance/baselines/GB-0001.yaml", type=Path
    )
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    baseline_path = args.baseline if args.baseline.is_absolute() else root / args.baseline
    baseline = load_baseline(baseline_path)
    if args.generate:
        output = root / "governance" / "GOVERNING-SPEC.md"
        output.write_text(render_governing_spec(root, baseline), encoding="utf-8")
    report = verify_baseline(root, baseline)
    rendered_report = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        report_path = args.report if args.report.is_absolute() else root / args.report
        report_path.write_text(rendered_report, encoding="utf-8")
    print(rendered_report, end="")
    return 0 if not report["integrity_failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
