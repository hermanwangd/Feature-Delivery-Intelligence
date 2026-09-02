import json
from pathlib import Path

from runtime.dev204_validation import load_scenario_pack, prepare_all_execution_packets

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / '06-validation' / 'skill-behavior' / 'SCENARIOS-v0.4.6.2.json'

EXPECTED = [
    'PA-Codebase-Inventory', 'PA-Historical-Delivery', 'feature-intent-analysis',
    'repo-discovery', 'changesurface-investigation', 'dependency-closure',
    'closure-review', 'ft-t1-intention', 'ft-t2-delivery-spec',
    'product-team-onboarding-leader', 'product-knowledge-feature-discovery-closed-loop',
]


def test_scenario_pack_has_one_frozen_core_pressure_case_per_dev204_target():
    pack = load_scenario_pack(PACK)
    assert [s['target'] for s in pack['scenarios']] == EXPECTED
    assert len({s['scenario_id'] for s in pack['scenarios']}) == len(EXPECTED)
    for scenario in pack['scenarios']:
        assert scenario['agent_prompt'].strip()
        assert scenario['rubric']['pass_conditions']
        assert scenario['rubric']['forbidden_conditions']
        # Agent-facing prompt must not contain evaluator labels or reveal the answer key.
        lowered = scenario['agent_prompt'].lower()
        assert 'pass_conditions' not in lowered
        assert 'forbidden_conditions' not in lowered
        assert 'expected:' not in lowered
        assert 'forbidden:' not in lowered


def test_prepare_all_packets_keeps_rubric_outside_agent_packets(tmp_path):
    result = prepare_all_execution_packets(PACK, tmp_path)
    assert result['scenario_count'] == 11
    assert result['packet_count'] == 22
    packet = json.loads((tmp_path / 'DEV204-OPT-B-01-red-packet.json').read_text())
    assert 'rubric' not in packet
    assert packet['target_skill_loaded'] is False
    reviewer = json.loads((tmp_path / 'DEV204-OPT-B-01-reviewer-rubric.json').read_text())
    assert reviewer['rubric']['pass_conditions']
    assert reviewer['scenario_sha256'] == packet['scenario_sha256']


def test_prepare_dev204_cli_writes_execution_packets(tmp_path):
    import subprocess, sys
    script = ROOT / 'scripts' / 'prepare_dev204_execution.py'
    subprocess.run([
        sys.executable, str(script), '--scenario-pack', str(PACK), '--output-dir', str(tmp_path)
    ], check=True, capture_output=True, text=True, cwd=ROOT)
    assert (tmp_path / 'DEV204-OPT-B-01-red-packet.json').exists()
    assert (tmp_path / 'DEV204-OPT-B-01-green-packet.json').exists()
    assert (tmp_path / 'DEV204-OPT-B-01-reviewer-rubric.json').exists()
