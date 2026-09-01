import json
from pathlib import Path

from runtime.dev204_validation import load_scenario_pack, prepare_all_execution_packets, validate_plan

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "06-validation" / "skill-behavior" / "SCENARIOS-v0.4.7.0.json"
PLAN = ROOT / "06-validation" / "skill-behavior" / "VALIDATION-PLAN-v0.4.7.0.json"

EXPECTED_LAST = "structural-intelligence-feature-discovery-integration"


def test_v047_plan_extends_dev204_without_changing_original_targets_or_creating_a_skill():
    plan = json.loads(PLAN.read_text())
    validate_plan(plan)
    assert len(plan["scenarios"]) == 12
    last = plan["scenarios"][-1]
    assert last["skill_or_behavior"] == EXPECTED_LAST
    assert last["kind"] == "SYSTEM_BEHAVIOR_NOT_SKILL"
    assert last["status"] == "NOT_EXECUTED"
    assert plan["option_b_hypothesis_ref"] == "00-product/MVP-HYPOTHESIS-FREEZE-v0.4.7.0.md"


def test_v047_pack_adds_structural_intelligence_pressure_case_without_rubric_leakage():
    pack = load_scenario_pack(PACK)
    assert len(pack["scenarios"]) == 12
    last = pack["scenarios"][-1]
    assert last["target"] == EXPECTED_LAST
    prompt = last["agent_prompt"]
    assert "Structural Intelligence" in prompt
    assert "PA-03" in prompt
    assert "current pinned evidence" in prompt.lower()
    assert "pass_conditions" not in prompt.lower()
    assert "forbidden_conditions" not in prompt.lower()
    assert any("current truth" in item for item in last["rubric"]["forbidden_conditions"])


def test_v047_packet_preparation_produces_24_agent_packets_and_12_reviewer_rubrics(tmp_path):
    result = prepare_all_execution_packets(PACK, tmp_path)
    assert result == {"scenario_count": 12, "packet_count": 24}
    assert len(list(tmp_path.glob("*-red-packet.json"))) == 12
    assert len(list(tmp_path.glob("*-green-packet.json"))) == 12
    assert len(list(tmp_path.glob("*-reviewer-rubric.json"))) == 12
    packet = json.loads((tmp_path / "DEV204-FDI-SI-01-red-packet.json").read_text())
    reviewer = json.loads((tmp_path / "DEV204-FDI-SI-01-reviewer-rubric.json").read_text())
    assert "rubric" not in packet
    assert packet["target_skill_loaded"] is False
    assert reviewer["scenario_sha256"] == packet["scenario_sha256"]
