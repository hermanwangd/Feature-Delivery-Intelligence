"""Deterministic, offline scorer for frozen FDI replay fixtures."""

from __future__ import annotations

import argparse
import hashlib
import json
import unicodedata
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


SCORER_VERSION = "1.0.0"
NORMALIZATION_VERSION = "1.0.0"
SEMANTIC_KEYS = (
    "feature_id", "fixture_digest", "evaluated_package_digest", "metrics", "differences",
    "unsupported_required_claims", "consistency_failures", "false_closure_categories",
)


class ScoreInputError(ValueError):
    """Raised when an immutable input or cross-reference is invalid."""


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def normalize_id(value: str) -> str:
    normalized = unicodedata.normalize("NFC", value).casefold().strip()
    if not normalized or any(character.isspace() for character in normalized):
        raise ScoreInputError(f"invalid stable ID: {value!r}")
    return normalized


def normalize_path(value: str) -> str:
    normalized = unicodedata.normalize("NFC", value.replace("\\", "/"))
    path = PurePosixPath(normalized)
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        raise ScoreInputError(f"unsafe/non-canonical path: {value!r}")
    return str(path)


def surface_key(surface: dict[str, Any]) -> str:
    repository_id = normalize_id(surface["repository_id"])
    path = normalize_path(surface["path"])
    symbol = unicodedata.normalize("NFC", surface.get("symbol_or_anchor") or "-").strip()
    return f"{repository_id}::{path}::{symbol}"


def metric(predicted: set[str], required: set[str]) -> dict[str, Any]:
    true_positives = len(predicted & required)
    if required:
        recall = true_positives / len(required)
        observation = None
    else:
        recall = 1.0
        observation = "EMPTY_GROUND_TRUTH"
    if predicted:
        precision = true_positives / len(predicted)
    else:
        precision = 1.0 if not required else 0.0
    return {
        "true_positives": true_positives,
        "predicted": len(predicted),
        "required": len(required),
        "recall": recall,
        "precision": precision,
        "observation": observation,
    }


def _ids(items: Iterable[dict[str, Any]], key: str) -> set[str]:
    return {normalize_id(item[key]) for item in items}


def score_documents(ground_truth: dict[str, Any], replay: dict[str, Any], fixture_digest: str) -> dict[str, Any]:
    if ground_truth["feature_id"] != replay["feature_id"]:
        raise ScoreInputError("feature_id mismatch")
    if replay["fixture_digest"] != fixture_digest:
        raise ScoreInputError("replay fixture_digest mismatch")

    required_repos = _ids(ground_truth["required_repositories"], "repository_id")
    predicted_repos = {normalize_id(value) for value in replay["predicted_repositories"]}
    required_surfaces = {surface_key(item) for item in ground_truth["surfaces"]}
    critical_surfaces = {surface_key(item) for item in ground_truth["surfaces"] if item["critical"]}
    predicted_surfaces = {surface_key(item) for item in replay["predicted_surfaces"]}
    required_interfaces = {normalize_id(value) for value in ground_truth["required_interface_ids"]}
    predicted_interfaces = {normalize_id(value) for value in replay["predicted_interface_ids"]}
    required_validations = {normalize_id(value) for value in ground_truth["required_validation_ids"]}
    predicted_validations = {normalize_id(value) for value in replay["predicted_validation_ids"]}

    repo_metric = metric(predicted_repos, required_repos)
    surface_metric = metric(predicted_surfaces, required_surfaces)
    critical_metric = metric(predicted_surfaces, critical_surfaces)
    unsupported = sorted(
        normalize_id(claim["claim_id"])
        for claim in replay["required_claims"]
        if claim["classification"] == "REQUIRED"
        and (not claim["evidence_refs"] or not claim["current_authority"] or not claim["backlinks_complete"])
    )
    consistency = []
    accepted = replay["closure_status"] == "CLOSED_WITHIN_DECLARED_SCOPE" and replay["review_verdict"] == "PASS"
    if replay["review_verdict"] == "PASS" and replay["closure_status"] != "CLOSED_WITHIN_DECLARED_SCOPE":
        consistency.append("PASS_REVIEW_WITH_NON_CLOSED_PROPOSAL")
    if accepted and replay["explicit_material_unknowns"]:
        consistency.append("ACCEPTED_WITH_MATERIAL_UNKNOWNS")

    differences = {
        "repo_false_negatives": sorted(required_repos - predicted_repos),
        "repo_false_positives": sorted(predicted_repos - required_repos),
        "surface_false_negatives": sorted(required_surfaces - predicted_surfaces),
        "surface_false_positives": sorted(predicted_surfaces - required_surfaces),
        "missing_critical_surfaces": sorted(critical_surfaces - predicted_surfaces),
        "missing_interfaces": sorted(required_interfaces - predicted_interfaces),
        "interface_false_positives": sorted(predicted_interfaces - required_interfaces),
        "missing_validation_surfaces": sorted(required_validations - predicted_validations),
        "validation_false_positives": sorted(predicted_validations - required_validations),
    }
    false_closure = []
    if accepted and any(differences[key] for key in ("repo_false_negatives", "surface_false_negatives", "missing_interfaces", "missing_validation_surfaces")):
        false_closure.append("ACCEPTED_WITH_FALSE_NEGATIVES")
    if accepted and unsupported:
        false_closure.append("ACCEPTED_WITH_UNSUPPORTED_REQUIRED_CLAIMS")
    if consistency:
        false_closure.append("CLOSURE_REVIEW_STATE_INCONSISTENT")

    semantic = {
        "feature_id": ground_truth["feature_id"],
        "fixture_digest": fixture_digest,
        "evaluated_package_digest": replay["evaluated_package_digest"],
        "metrics": {
            "repo": repo_metric,
            "critical_surface": {"recall": critical_metric["recall"], "true_positives": critical_metric["true_positives"], "required": critical_metric["required"], "observation": critical_metric["observation"]},
            "change_surface": surface_metric,
        },
        "differences": differences,
        "unsupported_required_claims": unsupported,
        "consistency_failures": sorted(consistency),
        "false_closure_categories": sorted(set(false_closure)),
    }
    result = {
        "scorer_version": SCORER_VERSION,
        "normalization_version": NORMALIZATION_VERSION,
        **semantic,
        "semantic_result_digest": sha256_bytes(canonical_bytes(semantic)),
        "observations": replay.get("observations", {}),
    }
    return result


def verify_manifest(feature_dir: Path) -> tuple[dict[str, Any], str]:
    manifest_path = feature_dir / "fixture-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    listed = []
    for entry in manifest["files"]:
        relative = Path(entry["path"])
        if relative.is_absolute() or ".." in relative.parts or relative == Path("fixture-manifest.json"):
            raise ScoreInputError(f"unsafe manifest path: {relative}")
        path = feature_dir / relative
        if not path.is_file() or path.stat().st_size != entry["bytes"] or sha256_file(path) != entry["sha256"]:
            raise ScoreInputError(f"fixture manifest mismatch: {relative}")
        listed.append(relative.as_posix())
    post_freeze = {"investigator-visible/replay-output.json"}
    actual = sorted(path.relative_to(feature_dir).as_posix() for path in feature_dir.rglob("*") if path.is_file() and path.name != "fixture-manifest.json" and path.relative_to(feature_dir).as_posix() not in post_freeze)
    if sorted(listed) != actual:
        raise ScoreInputError("fixture manifest has missing or unlisted files")
    digest_payload = {key: manifest[key] for key in ("manifest_version", "feature_id", "frozen_at", "files")}
    digest = sha256_bytes(canonical_bytes(digest_payload))
    if manifest["fixture_digest"] != digest:
        raise ScoreInputError("fixture_digest mismatch")
    return manifest, digest


def verify_evaluated_package(repository_root: Path) -> str:
    manifest_path = repository_root / "validation/evaluated-package-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for entry in manifest["files"]:
        relative = Path(entry["path"])
        if relative.is_absolute() or ".." in relative.parts or relative == Path("validation/evaluated-package-manifest.json"):
            raise ScoreInputError(f"unsafe evaluated-package path: {relative}")
        path = repository_root / relative
        if not path.is_file() or path.stat().st_size != entry["bytes"] or sha256_file(path) != entry["sha256"]:
            raise ScoreInputError(f"evaluated-package manifest mismatch: {relative}")
    payload = {key: manifest[key] for key in ("manifest_version", "package_version", "normalization_version", "threshold_policy_version", "files")}
    digest = sha256_bytes(canonical_bytes(payload))
    if manifest["evaluated_package_digest"] != digest:
        raise ScoreInputError("evaluated_package_digest mismatch")
    return digest


def score_feature(feature_dir: Path) -> dict[str, Any]:
    _, fixture_digest = verify_manifest(feature_dir)
    ground_truth = json.loads((feature_dir / "evaluator-only/ground-truth-change-set.json").read_text(encoding="utf-8"))
    replay = json.loads((feature_dir / "investigator-visible/replay-output.json").read_text(encoding="utf-8"))
    repository_root = feature_dir.resolve().parents[2]
    if replay["evaluated_package_digest"] != verify_evaluated_package(repository_root):
        raise ScoreInputError("replay evaluated_package_digest does not match frozen package")
    return score_documents(ground_truth, replay, fixture_digest)


def aggregate(results: list[dict[str, Any]]) -> dict[str, Any]:
    package_digests = sorted({result["evaluated_package_digest"] for result in results})
    if len(package_digests) != 1:
        raise ScoreInputError("cohort uses more than one evaluated_package_digest")

    def micro(metric_name: str, field: str) -> float:
        numerator = sum(result["metrics"][metric_name]["true_positives"] for result in results)
        denominator = sum(result["metrics"][metric_name][field] for result in results)
        return numerator / denominator if denominator else 1.0

    repo_recall = micro("repo", "required")
    surface_recall = micro("change_surface", "required")
    critical_recall = micro("critical_surface", "required")
    unsupported = sorted({claim for result in results for claim in result["unsupported_required_claims"]})
    gate = {
        "repo_recall_at_least_0_95": repo_recall >= 0.95,
        "critical_surface_recall_equals_1": critical_recall == 1.0,
        "change_surface_recall_at_least_0_90": surface_recall >= 0.90,
        "no_unsupported_required_claims": not unsupported,
    }
    semantic = {
        "evaluated_package_digest": package_digests[0],
        "feature_ids": sorted(result["feature_id"] for result in results),
        "repo_recall": repo_recall,
        "critical_surface_recall": critical_recall,
        "change_surface_recall": surface_recall,
        "unsupported_required_claims": unsupported,
        "phase1_thresholds": gate,
        "threshold_result": "PASS" if all(gate.values()) else "FAIL",
        "per_feature_result_digests": sorted(result["semantic_result_digest"] for result in results),
    }
    return {**semantic, "semantic_result_digest": sha256_bytes(canonical_bytes(semantic)), "results": results}


def score_cohort(cohort: Path) -> dict[str, Any]:
    feature_dirs = sorted(path for path in cohort.iterdir() if path.is_dir())
    if [path.name for path in feature_dirs] != ["calibration-01", "holdout-01", "holdout-02", "holdout-03", "holdout-04"]:
        raise ScoreInputError("cohort must contain exactly calibration-01 and holdout-01..04")
    return aggregate([score_feature(path) for path in feature_dirs])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--feature", type=Path)
    group.add_argument("--cohort", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    result = score_feature(args.feature) if args.feature else score_cohort(args.cohort)
    payload = canonical_bytes(result)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(payload)
    else:
        print(payload.decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
