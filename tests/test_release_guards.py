import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "OVERLAY-STATUS-v0.4.7.2.json"
ROOT_STATUS = ROOT / "OVERLAY-STATUS.json"
SUMMARY = ROOT / "VERIFICATION-SUMMARY-v0.4.7.2-overlay.json"
README = ROOT / "README.md"
BUILD = ROOT / "scripts" / "build_overlay_package.py"
PREPARED = ROOT / "06-validation" / "skill-behavior" / "prepared-v0.4.7.1"
SKILL_BEHAVIOR = ROOT / "06-validation" / "skill-behavior"
ARCHIVE = ROOT / "archive" / "superseded" / "skill-behavior"


def test_v0471_status_preserves_claim_boundary_and_refreezes_full_fdi_before_f001():
    status = json.loads(STATUS.read_text())
    assert json.loads(ROOT_STATUS.read_text()) == status
    assert status["release"] == "fdi-mvp-v0.4.7.2-live-grafel-binding-overlay"
    assert status["classification"] == "SOURCE_TREE_READY_LIVE_GRAFEL_BINDING_IMPLEMENTATION_OVERLAY"
    assert status["canonical_runtime_release"] is False
    assert status["option_b"]["H01_H05"] == "FROZEN_v0.4.7.1_BEFORE_F001"
    assert status["option_b"]["hypothesis"] == "Full FDI -> Feature Discovery"
    assert status["option_b"]["shared_repository_identity_substrate"] == "PA03_CB01_IDENTITY_ONLY_ALL_ARMS"
    assert status["external_gates"]["DEV-204"] == "EXECUTION_READY_NOT_EXECUTED"
    assert status["external_gates"]["F001"] == "NOT_EXECUTED"
    assert status["external_gates"]["live_grafel"] == "NOT_EXECUTED_RUNTIME_UNAVAILABLE"


def test_v0471_status_declares_queryable_snapshot_binding_without_claiming_live_grafel_attestor():
    status = json.loads(STATUS.read_text())
    structural = status["structural_intelligence_conformance"]
    for key in (
        "provider_independent_contracts",
        "grafel_adapter_boundary",
        "snapshot_binding_contract",
        "provider_route_enforcement",
        "dual_snapshot_diff_attestation",
        "bounded_result_postconditions",
        "pa03_grounded_feature_discovery",
        "identity_only_ablation_substrate",
        "dev204_neutral_target_semantics",
    ):
        assert structural[key] == "IMPLEMENTED_LOCAL_OVERLAY"
    assert structural["live_grafel_binding_attestor"] == "IMPLEMENTED_LOCAL_OVERLAY_NOT_EXECUTED"
    assert structural["binding_attestation_retention"] == "REQUIRED_EXECUTION_EVIDENCE"
    assert structural["current_feature_truth_authority"] == "PROHIBITED"
    assert status["external_gates"]["live_grafel_binding_attestor"] == "IMPLEMENTATION_READY_NOT_EXECUTED"


def test_readme_describes_v0471_hardening_and_apply_then_verify_boundary():
    text = README.read_text()
    assert "FDI MVP v0.4.7.2" in text
    assert "SnapshotBindingAttestation" in text
    assert "identity-only" in text.lower()
    assert "target_kind" in text and "target_loaded" in text
    assert "implementation overlay" in text.lower()
    assert "canonical v0.4.6.1 source tree" in text
    assert "Do not claim `fdi-mvp-v0.4.7.2`" in text
    assert "live Grafel" in text and "NOT" in text
    assert "binding_attestor" in text
    assert "FROZEN_INDEXED" in text
    assert "full SnapshotBindingAttestation" in text


def test_v0471_dev204_materialized_packets_are_complete_neutral_and_reviewer_separated():
    assert len(list(PREPARED.glob("*-red-packet.json"))) == 12
    assert len(list(PREPARED.glob("*-green-packet.json"))) == 12
    assert len(list(PREPARED.glob("*-reviewer-rubric.json"))) == 12
    for scenario_id in ("DEV204-OPT-B-01", "DEV204-FDI-SI-01"):
        red = json.loads((PREPARED / f"{scenario_id}-red-packet.json").read_text())
        green = json.loads((PREPARED / f"{scenario_id}-green-packet.json").read_text())
        reviewer = json.loads((PREPARED / f"{scenario_id}-reviewer-rubric.json").read_text())
        assert "rubric" not in red and "rubric" not in green
        assert red["schema_version"] == "0.2"
        assert red["target_kind"] == "SYSTEM_BEHAVIOR"
        assert red["target_loaded"] is False and green["target_loaded"] is True
        assert "target_skill_loaded" not in red and "target_skill_loaded" not in green
        assert red["scenario_sha256"] == reviewer["scenario_sha256"]
        assert red["claim_boundary"] == "EXECUTION_PACKET_ONLY_NOT_BEHAVIORAL_EVIDENCE"


def test_only_v0471_prepared_pack_is_active_and_older_packets_are_archived():
    active = sorted(p.name for p in SKILL_BEHAVIOR.glob("prepared-v*") if p.is_dir())
    assert active == ["prepared-v0.4.7.1"]
    assert (ARCHIVE / "prepared-v0.4.6.2").is_dir()
    assert (ARCHIVE / "prepared-v0.4.7.0").is_dir()


def test_current_execution_contract_refs_v02_not_legacy_generic_schema():
    status = json.loads(STATUS.read_text())
    assert status["dev204_harness"]["execution_record_schema"].endswith("execution-record-v0.2.schema.json")
    assert status["dev204_harness"]["execution_guide"].endswith("EXECUTION-GUIDE-v0.4.7.1.md")
    plan = json.loads((SKILL_BEHAVIOR / "VALIDATION-PLAN-v0.4.7.1.json").read_text())
    assert plan["execution_record_schema"] == "06-validation/skill-behavior/execution-record-v0.2.schema.json"
    assert "execution-record.schema.json" not in json.dumps(status)
    assert "execution-record.schema.json" not in json.dumps(plan)


def test_verification_summary_accounting_is_internally_consistent_and_does_not_claim_external_gates():
    summary = json.loads(SUMMARY.read_text())
    assert summary["release"] == "fdi-mvp-v0.4.7.2-live-grafel-binding-overlay"
    assert summary["classification"] == "IMPLEMENTATION_OVERLAY_NOT_CANONICAL_RELEASE"
    assert summary["total_passed"] == summary["functional_tests"]["passed"] + summary["release_guard_tests"]["passed"]
    assert summary["total_failed"] == 0
    claims = "\n".join(summary["claims_not_established"])
    for term in ("live Grafel", "DEV-204", "F001", "canonical"):
        assert term in claims


def test_active_v0471_runtime_and_docs_do_not_reintroduce_current_head_as_frozen_snapshot_authority():
    active_paths = [
        ROOT / "runtime" / "grafel_adapter.py",
        ROOT / "03-structural-intelligence" / "GRAFEL-ADAPTER-CONTRACT-v0.2.md",
        ROOT / "00-product" / "FDI-MVP-v0.4.7.1-STRUCTURAL-INTELLIGENCE-HARDENING.md",
        README,
    ]
    combined = "\n".join(path.read_text() for path in active_paths)
    assert "binding → grafel_index_status" not in combined
    assert "_verify_live_binding" not in combined
    assert "both endpoints must be current" not in combined.lower()
    assert "exact revision equivalence" in combined.lower()
    assert "provider scope" in combined.lower()
    assert "provider ref" in combined.lower()


def test_packager_is_v0471_and_excludes_compiled_cache_and_preexisting_zip_inputs():
    assert BUILD.exists()
    text = BUILD.read_text()
    assert "v0.4.7.2" in text
    assert "__pycache__" in text
    assert '".pyc"' in text
    assert '".zip"' in text


def test_deterministic_package_and_manifest_verify_v0471_identity(tmp_path):
    out1 = tmp_path / "one.zip"
    out2 = tmp_path / "two.zip"
    cmd = [sys.executable, str(BUILD), "--source", str(ROOT), "--output"]
    subprocess.run([*cmd, str(out1)], check=True, capture_output=True, text=True)
    subprocess.run([*cmd, str(out2)], check=True, capture_output=True, text=True)
    assert hashlib.sha256(out1.read_bytes()).hexdigest() == hashlib.sha256(out2.read_bytes()).hexdigest()

    with zipfile.ZipFile(out1) as zf:
        assert zf.testzip() is None
        names = zf.namelist()
        assert "MANIFEST.json" in names
        assert "06-validation/skill-behavior/prepared-v0.4.7.1/DEV204-FDI-SI-01-red-packet.json" in names
        assert not any(name.startswith("06-validation/skill-behavior/prepared-v0.4.7.0/") for name in names)
        assert not any("__pycache__" in name or name.endswith((".pyc", ".pyo")) for name in names)
        manifest = json.loads(zf.read("MANIFEST.json"))
        assert manifest["release"] == "fdi-mvp-v0.4.7.2-live-grafel-binding-overlay"
        for entry in manifest["entries"]:
            assert hashlib.sha256(zf.read(entry["path"])).hexdigest() == entry["sha256"]


def test_packager_excludes_local_virtual_environment(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    (source / "keep.txt").write_text("source\n")
    venv_file = source / ".venv" / "lib" / "installed-package.py"
    venv_file.parent.mkdir(parents=True)
    venv_file.write_text("local dependency\n")
    output = tmp_path / "package.zip"

    subprocess.run(
        [sys.executable, str(BUILD), "--source", str(source), "--output", str(output)],
        check=True,
        capture_output=True,
        text=True,
    )

    with zipfile.ZipFile(output) as zf:
        assert "keep.txt" in zf.namelist()
        assert not any(name.startswith(".venv/") for name in zf.namelist())



def test_v0472_concrete_grafel_binding_attestor_is_packaged_but_live_execution_remains_external():
    module = ROOT / "runtime" / "grafel_binding_attestor.py"
    doc = ROOT / "03-structural-intelligence" / "GRAFEL-BINDING-ATTESTOR-v0.2.md"
    assert module.exists() and doc.exists()
    text = module.read_text() + "\n" + doc.read_text()
    for term in ("GrafelSnapshotBindingAttestor", "grafel_orient", "indexed_ref", "indexed_sha", "FROZEN_INDEXED"):
        assert term in text
    status = json.loads(STATUS.read_text())
    assert status["structural_intelligence_conformance"]["live_grafel_binding_attestor"] == "IMPLEMENTED_LOCAL_OVERLAY_NOT_EXECUTED"
    assert status["external_gates"]["live_grafel"] == "NOT_EXECUTED_RUNTIME_UNAVAILABLE"

def test_package_verification_logs_do_not_mutate_release_input_tree():
    transient = sorted({
        p.relative_to(ROOT).as_posix()
        for pattern in ("final*-package-*.txt", "final*-package-sha256.txt", "v047*-package-*.txt", "v0471*-package-*.txt")
        for p in (ROOT / "evidence").glob(pattern)
        if p.is_file()
    })
    assert transient == [], (
        "package verification logs must be written outside the release input tree: " + ", ".join(transient)
    )
