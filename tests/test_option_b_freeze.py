from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HYPOTHESIS = ROOT / "00-product" / "MVP-HYPOTHESIS-FREEZE-v0.4.6.2.md"
PROJECT = ROOT / "00-product" / "FDI-Project-Definition-v0.3.3-OPTION-B-PATCH.md"
REPLAY = ROOT / "06-validation" / "OPTION-B-PAIRED-REPLAY-PROTOCOL-v0.1.md"


def test_h01_h05_are_frozen_before_f001():
    text = HYPOTHESIS.read_text()
    for gate in ["MVP-H01", "MVP-H02", "MVP-H03", "MVP-H04", "MVP-H05"]:
        assert gate in text
    assert text.count('Status: `FROZEN`') == 5
    assert "F001 MUST NOT execute until H01–H05 are frozen" in text


def test_option_b_names_all_three_product_knowledge_roles_and_current_evidence_boundary():
    combined = PROJECT.read_text() + "\n" + REPLAY.read_text()
    for term in ["Product Semantics", "Product Realization", "Delivery Intelligence"]:
        assert term in combined
    assert "current feature-specific Evidence" in combined or "current feature-specific pinned Evidence" in combined
    assert "current `CONFIRMED`" in combined
    assert "current `EXCLUDED`" in combined


def test_paired_replay_freezes_fair_controls_and_groundtruth_isolation():
    text = REPLAY.read_text()
    required = [
        "identical frozen Feature input",
        "identical exact pre-feature source/repository revisions",
        "identical model/configuration",
        "identical execution/tool/time budget",
        "no GroundTruth access",
        "F001 = calibration",
        "F002–F005 = blind holdout",
    ]
    assert all(item in text for item in required)


def test_baseline_does_not_receive_fdi_product_knowledge_treatment():
    text = REPLAY.read_text()
    prohibited = [
        "governed FDI Product Semantics refs",
        "FDI Product Realization view",
        "FDI Delivery Intelligence context",
        "FeatureKnowledgePlan and FDI Context resolution outputs",
    ]
    assert all(item in text for item in prohibited)


def test_f001_decision_vocabulary_is_consistent():
    project = PROJECT.read_text()
    replay = REPLAY.read_text()
    assert "CONTINUE | REVISE | STOP" in project
    assert "CONTINUE | REVISE | STOP" in replay
    assert "CONTINUE | REVISE | REJECT" not in project
