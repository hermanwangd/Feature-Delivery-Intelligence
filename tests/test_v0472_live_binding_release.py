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


def test_v0472_binding_doc_keeps_graph_header_provenance_and_current_truth_boundaries_explicit():
    text = (ROOT / "03-structural-intelligence" / "GRAFEL-BINDING-ATTESTOR-v0.1.md").read_text()
    for term in (
        "grafel_orient",
        "indexed_ref",
        "indexed_sha",
        "StructuralSnapshotRef",
        "FROZEN_INDEXED",
        "current Feature truth",
        "NOT EXECUTED",
    ):
        assert term in text
