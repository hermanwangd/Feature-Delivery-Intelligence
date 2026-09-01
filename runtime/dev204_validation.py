from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


class ValidationError(ValueError):
    pass


_ORIGINAL_TARGETS = [
    'PA-Codebase-Inventory',
    'PA-Historical-Delivery',
    'feature-intent-analysis',
    'repo-discovery',
    'changesurface-investigation',
    'dependency-closure',
    'closure-review',
    'ft-t1-intention',
    'ft-t2-delivery-spec',
    'product-team-onboarding-leader',
]
_OPTION_B_SYSTEM_BEHAVIOR = 'product-knowledge-feature-discovery-closed-loop'
_STRUCTURAL_SYSTEM_BEHAVIOR = 'structural-intelligence-feature-discovery-integration'
_SCORE_VALUES = {'PASS', 'FAIL', 'N/A'}


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def _expected_targets(release: str | None) -> list[str]:
    targets = _ORIGINAL_TARGETS + [_OPTION_B_SYSTEM_BEHAVIOR]
    if release in {'fdi-mvp-v0.4.7.0', 'fdi-mvp-v0.4.7.1'}:
        targets.append(_STRUCTURAL_SYSTEM_BEHAVIOR)
    return targets


def validate_plan(plan: dict[str, Any]) -> None:
    if plan.get('validation_mode') != 'FRESH_CONTEXT_RED_GREEN':
        raise ValidationError('DEV-204 validation_mode must be FRESH_CONTEXT_RED_GREEN')
    if plan.get('claim_boundary') != 'EXECUTION_READY_NOT_BEHAVIORALLY_VALIDATED':
        raise ValidationError('DEV-204 plan must not pre-claim behavioral validation')
    req = plan.get('execution_requirements') or {}
    for key in ('independent_fresh_contexts', 'same_frozen_scenario_per_red_green_pair', 'independent_review_required'):
        if req.get(key) is not True:
            raise ValidationError(f'missing DEV-204 execution requirement: {key}')
    scenarios = plan.get('scenarios') or []
    targets = [item.get('skill_or_behavior') for item in scenarios]
    if targets[:10] != _ORIGINAL_TARGETS:
        raise ValidationError('original DEV-204 priority targets changed')
    expected_targets = _expected_targets(plan.get('release'))
    if targets != expected_targets:
        raise ValidationError('DEV-204 target order does not match the release validation contract')
    for index, item in enumerate(scenarios, start=1):
        if item.get('priority') != index:
            raise ValidationError('DEV-204 priorities must be deterministic and contiguous')
        if item.get('red_requires_fresh_context') is not True or item.get('green_requires_fresh_context') is not True:
            raise ValidationError('each DEV-204 target requires fresh RED and GREEN contexts')
        if item.get('status') not in {'NOT_EXECUTED', 'RED_EXECUTED', 'GREEN_EXECUTED', 'VALIDATED', 'RED_NO_SKILL_GAP_OBSERVED', 'RED_NO_TARGET_GAP_OBSERVED'}:
            raise ValidationError('invalid DEV-204 scenario status')


def build_execution_packet(*, release: str, scenario_id: str, target: str, arm: str, prompt: str, output_dir: str | Path, target_kind: str = 'SKILL') -> dict[str, Any]:
    if arm not in {'RED', 'GREEN'}:
        raise ValidationError('arm must be RED or GREEN')
    if not prompt.strip():
        raise ValidationError('scenario prompt must be non-empty')
    if target_kind not in {'SKILL', 'SYSTEM_BEHAVIOR'}:
        raise ValidationError('target_kind must be SKILL or SYSTEM_BEHAVIOR')
    modern = release == 'fdi-mvp-v0.4.7.1'
    packet = {
        'schema_version': '0.2' if modern else '0.1',
        'release': release,
        'scenario_id': scenario_id,
        'target': target,
        'arm': arm,
        'scenario_sha256': _sha256_text(prompt),
        'prompt': prompt,
        'fresh_context_required': True,
        'independent_review_required': True,
        'ground_truth_mounted': False,
        'claim_boundary': 'EXECUTION_PACKET_ONLY_NOT_BEHAVIORAL_EVIDENCE',
    }
    if modern:
        packet['target_kind'] = target_kind
        packet['target_loaded'] = arm == 'GREEN'
    else:
        # Legacy v0.4.6.2/v0.4.7.0 packets predate system-behavior-neutral naming.
        packet['target_skill_loaded'] = arm == 'GREEN'
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    (path / f'{scenario_id}-{arm.lower()}-packet.json').write_text(json.dumps(packet, indent=2, sort_keys=True) + '\n')
    return packet


def validate_execution_record(record: dict[str, Any]) -> None:
    if record.get('arm') not in {'RED', 'GREEN'}:
        raise ValidationError('record arm must be RED or GREEN')
    if record.get('fresh_context') is not True or not record.get('context_id'):
        raise ValidationError('fresh independent agent context evidence is required')
    if not record.get('reviewer_context_id'):
        raise ValidationError('independent reviewer context evidence is required')
    if record['reviewer_context_id'] == record['context_id']:
        raise ValidationError('reviewer context must differ from agent context')
    if record.get('ground_truth_mounted') is not False:
        raise ValidationError('GroundTruth must not be mounted in DEV-204 production execution')
    expected_loaded = record['arm'] == 'GREEN'
    schema_version = record.get('schema_version', '0.1')
    if schema_version == '0.2':
        if record.get('release') != 'fdi-mvp-v0.4.7.1':
            raise ValidationError('execution record schema v0.2 is bound to fdi-mvp-v0.4.7.1')
        if record.get('target_kind') not in {'SKILL', 'SYSTEM_BEHAVIOR'}:
            raise ValidationError('target_kind must be SKILL or SYSTEM_BEHAVIOR')
        if 'target_skill_loaded' in record:
            raise ValidationError('schema v0.2 uses target_loaded, not target_skill_loaded')
        if record.get('target_loaded') is not expected_loaded:
            raise ValidationError('RED must omit target; GREEN must load target')
    elif schema_version == '0.1':
        if record.get('target_skill_loaded') is not expected_loaded:
            raise ValidationError('RED must omit target Skill; GREEN must load target Skill')
    else:
        raise ValidationError('unsupported DEV-204 execution-record schema_version')
    sha = record.get('scenario_sha256', '')
    if len(sha) != 64 or any(c not in '0123456789abcdef' for c in sha):
        raise ValidationError('scenario_sha256 must be a lowercase SHA-256 digest')
    if not record.get('agent_output_ref') or not record.get('review_ref'):
        raise ValidationError('agent output and independent review evidence refs are required')
    scores = record.get('scores') or {}
    for dimension in ('authority', 'decision', 'physical_shape', 'provenance', 'lifecycle', 'reentry'):
        if scores.get(dimension) not in _SCORE_VALUES:
            raise ValidationError(f'invalid/missing score: {dimension}')
    if record.get('overall') not in {'PASS', 'FAIL'}:
        raise ValidationError('overall must be PASS or FAIL')


def evaluate_dev204_gate(red: dict[str, Any], green: dict[str, Any]) -> dict[str, Any]:
    validate_execution_record(red)
    validate_execution_record(green)
    if red['arm'] != 'RED' or green['arm'] != 'GREEN':
        raise ValidationError('gate requires RED then GREEN')
    for field in ('release', 'scenario_id', 'target', 'scenario_sha256'):
        if red.get('schema_version') == '0.2' and red.get('target_kind') != green.get('target_kind'):
            raise ValidationError('RED/GREEN pair mismatch: target_kind')
        if red.get(field) != green.get(field):
            raise ValidationError(f'RED/GREEN pair mismatch: {field}')
    if red['context_id'] == green['context_id']:
        raise ValidationError('RED and GREEN must use distinct fresh agent contexts')
    if red['reviewer_context_id'] == green['reviewer_context_id']:
        raise ValidationError('RED and GREEN must use distinct independent reviewer contexts')
    all_contexts = {red['context_id'], green['context_id'], red['reviewer_context_id'], green['reviewer_context_id']}
    if len(all_contexts) != 4:
        raise ValidationError('agent and reviewer contexts must be independent across the pair')
    if red['overall'] == 'PASS':
        return {
            'status': 'RED_NO_TARGET_GAP_OBSERVED' if red.get('schema_version') == '0.2' else 'RED_NO_SKILL_GAP_OBSERVED',
            'behaviorally_validated': False,
            'reason': 'No meaningful RED failure was observed without the target.' if red.get('schema_version') == '0.2' else 'No meaningful RED failure was observed without the target Skill.',
        }
    if green['overall'] != 'PASS':
        return {
            'status': 'GREEN_FAIL',
            'behaviorally_validated': False,
            'reason': 'GREEN did not correct the observed RED failure.',
        }
    return {
        'status': 'GREEN_PASS',
        'behaviorally_validated': True,
        'reason': 'Meaningful RED failure observed; same frozen scenario passed with the target loaded in independent fresh contexts.' if red.get('schema_version') == '0.2' else 'Meaningful RED failure observed; same frozen scenario passed with target Skill in independent fresh contexts.',
    }


def evaluate_closed_loop_behavior(observation: dict[str, Any]) -> dict[str, Any]:
    violations: list[str] = []
    claims = observation.get('confirmed_surface_claims') or []
    evidence = observation.get('current_feature_evidence_refs') or []
    if claims and not evidence:
        violations.append('CURRENT_EVIDENCE_REQUIRED')
    if observation.get('spec_ready') is True and claims and not evidence:
        violations.append('FALSE_SPEC_READY')
    if observation.get('spec_ready') is True and observation.get('candidate_repo_set_produced') is not True:
        violations.append('SPEC_READY_WITHOUT_CANDIDATE_INVESTIGATION')
    return {
        'status': 'PASS' if not violations else 'FAIL',
        'violations': violations,
        'product_knowledge_roles_observed': {
            'semantics': bool(observation.get('semantics_used')),
            'realization': bool(observation.get('realization_used')),
            'delivery_prior': bool(observation.get('delivery_prior_used')),
        },
    }


def load_scenario_pack(path: str | Path) -> dict[str, Any]:
    pack = json.loads(Path(path).read_text())
    scenarios = pack.get('scenarios') or []
    targets = [s.get('target') for s in scenarios]
    expected = _expected_targets(pack.get('release'))
    if targets != expected:
        raise ValidationError('scenario pack target order must match DEV-204 validation plan')
    ids = [s.get('scenario_id') for s in scenarios]
    if len(ids) != len(set(ids)) or any(not i for i in ids):
        raise ValidationError('scenario IDs must be unique and non-empty')
    for scenario in scenarios:
        prompt = scenario.get('agent_prompt', '')
        rubric = scenario.get('rubric') or {}
        if not prompt.strip():
            raise ValidationError('agent_prompt must be non-empty')
        if not rubric.get('pass_conditions') or not rubric.get('forbidden_conditions'):
            raise ValidationError('reviewer rubric requires pass and forbidden conditions')
        lowered = prompt.lower()
        for leak in ('pass_conditions', 'forbidden_conditions', 'expected:', 'forbidden:'):
            if leak in lowered:
                raise ValidationError(f'agent prompt leaks evaluator rubric marker: {leak}')
    return pack


def prepare_all_execution_packets(scenario_pack_path: str | Path, output_dir: str | Path) -> dict[str, Any]:
    pack = load_scenario_pack(scenario_pack_path)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    packet_count = 0
    for scenario in pack['scenarios']:
        for arm in ('RED', 'GREEN'):
            build_execution_packet(
                release=pack['release'],
                scenario_id=scenario['scenario_id'],
                target=scenario['target'],
                target_kind='SYSTEM_BEHAVIOR' if scenario.get('target_kind') == 'SYSTEM_BEHAVIOR' or scenario.get('source_basis', '').endswith('SYSTEM_BEHAVIOR_NOT_SKILL') else 'SKILL',
                arm=arm,
                prompt=scenario['agent_prompt'],
                output_dir=out,
            )
            packet_count += 1
        modern = pack['release'] == 'fdi-mvp-v0.4.7.1'
        target_kind = 'SYSTEM_BEHAVIOR' if scenario.get('target_kind') == 'SYSTEM_BEHAVIOR' or scenario.get('source_basis', '').endswith('SYSTEM_BEHAVIOR_NOT_SKILL') else 'SKILL'
        reviewer = {
            'schema_version': '0.2' if modern else '0.1',
            'release': pack['release'],
            'scenario_id': scenario['scenario_id'],
            'target': scenario['target'],
            **({'target_kind': target_kind} if modern else {}),
            'scenario_sha256': _sha256_text(scenario['agent_prompt']),
            'rubric': scenario['rubric'],
            'claim_boundary': 'REVIEWER_ONLY_DO_NOT_MOUNT_IN_AGENT_CONTEXT',
        }
        (out / f"{scenario['scenario_id']}-reviewer-rubric.json").write_text(
            json.dumps(reviewer, indent=2, sort_keys=True) + '\n'
        )
    return {'scenario_count': len(pack['scenarios']), 'packet_count': packet_count}
