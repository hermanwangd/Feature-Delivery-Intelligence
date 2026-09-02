import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_v0472_status_distinguishes_implemented_attestor_from_unexecuted_live_grafel():
    status_path = ROOT / "OVERLAY-STATUS-v0.4.7.2.json"
    status = json.loads(status_path.read_text())
    assert status["release"] == "fdi-mvp-v0.4.7.2-live-grafel-binding-overlay"
    structural = status["structural_intelligence_conformance"]
    assert structural["live_grafel_binding_attestor"] == "IMPLEMENTED_LOCAL_OVERLAY_NOT_EXECUTED"
    assert structural["grafel_dashboard_group_metadata_client"] == "IMPLEMENTED_LOCAL_OVERLAY_NOT_EXECUTED"
    assert status["external_gates"]["live_grafel"] == "NOT_EXECUTED_RUNTIME_UNAVAILABLE"
    assert status["external_gates"]["DEV-204"] == "EXECUTION_READY_NOT_EXECUTED"
    assert status["external_gates"]["F001"] == "NOT_EXECUTED"


def test_v0472_binding_amendment_keeps_provenance_readiness_and_current_truth_boundaries_explicit():
    legacy = ROOT / "03-structural-intelligence" / "GRAFEL-BINDING-ATTESTOR-v0.1.md"
    amended = ROOT / "03-structural-intelligence" / "GRAFEL-BINDING-ATTESTOR-v0.2.md"
    assert legacy.exists()
    text = amended.read_text()
    for term in (
        "Grafel v0.3.0",
        "grafel_orient",
        "indexed_ref",
        "indexed_sha",
        "warming = false",
        "indexing = false",
        "absence of an error",
        "StructuralSnapshotRef",
        "FROZEN_INDEXED",
        "current Feature truth",
        "NOT EXECUTED",
    ):
        assert term in text
