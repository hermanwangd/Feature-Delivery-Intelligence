import copy
import pytest

from runtime.structural_intelligence import (
    StructuralIntelligenceError,
    derive_discovery_hints,
    normalize_observations,
    validate_snapshot_binding,
)


def snapshot(snapshot_id='struct:spc@r1', rev_a='aaa111', rev_b='bbb222'):
    return {
        'snapshot_id': snapshot_id,
        'provider': {'name': 'GRAFEL', 'version': '0.1.x'},
        'adapter_version': 'fdi-grafel-adapter@0.2',
        'source_snapshots': [
            {'repository': 'repo:a', 'revision': rev_a},
            {'repository': 'repo:b', 'revision': rev_b},
        ],
        'created_at': '2026-09-01T00:00:00Z',
    }


def binding_state(rev_a='aaa111', rev_b='bbb222', *, freshness='FROZEN_INDEXED'):
    return {
        'provider_scope_id': 'grafel-group:spc-test',
        'provider_ref': 'fdi/test-cutoff',
        'queryability': 'QUERYABLE',
        'freshness': freshness,
        'repositories': [
            {'repository': 'repo:a', 'indexed_revision': rev_a, 'queryable': True, 'head_revision': 'future-a'},
            {'repository': 'repo:b', 'indexed_revision': rev_b, 'queryable': True, 'head_revision': 'future-b'},
        ],
    }


def query(**overrides):
    base = {
        'query_id': 'sq:hardening',
        'snapshot_id': 'struct:spc@r1',
        'scope': {'products': ['SPC'], 'repositories': ['repo:a', 'repo:b']},
        'seed': {'type': 'COMPONENT', 'id': 'component:a'},
        'allowed_relation_types': ['HTTP_CALL'],
        'max_depth': 3,
        'max_nodes': 4,
        'max_edges': 10,
        'max_paths': 2,
        'max_result_bytes': 65536,
    }
    base.update(overrides)
    return base


def record(src, dst, *, src_repo='repo:a', dst_repo='repo:b', path_id=None):
    r = {
        'from': {'type': 'COMPONENT', 'id': src, 'repository_id': src_repo},
        'relation_type': 'HTTP_CALL',
        'to': {'type': 'COMPONENT', 'id': dst, 'repository_id': dst_repo},
        'evidence_refs': [f'{src_repo}@aaa111:{src}.py'],
    }
    if path_id is not None:
        r['path_id'] = path_id
    return r


def test_snapshot_binding_requires_exact_queryable_provider_snapshot_not_current_head():
    attestation = validate_snapshot_binding(snapshot(), binding_state())
    assert attestation['binding_state'] == 'VERIFIED'
    assert attestation['snapshot_id'] == 'struct:spc@r1'
    assert attestation['freshness'] == 'FROZEN_INDEXED'
    assert attestation['provider_route']['ref'] == 'fdi/test-cutoff'
    assert attestation['attestation_id'].startswith('sba:')

    bad_revision = binding_state(rev_a='wrong')
    missing_repo = binding_state(); missing_repo['repositories'] = missing_repo['repositories'][:1]
    not_queryable = binding_state(); not_queryable['repositories'][0]['queryable'] = False
    bad_route = binding_state(); bad_route['provider_ref'] = ''
    for bad_state in (bad_revision, missing_repo, not_queryable, bad_route):
        with pytest.raises(StructuralIntelligenceError):
            validate_snapshot_binding(snapshot(), bad_state)


def test_normalization_requires_verified_binding_attestation():
    with pytest.raises(StructuralIntelligenceError, match='binding attestation'):
        normalize_observations([record('a', 'b')], snapshot(), query())

    att = validate_snapshot_binding(snapshot(), binding_state())
    result = normalize_observations([record('a', 'b')], snapshot(), query(), binding_attestation=att)
    assert result['binding_attestation_id'] == att['attestation_id']


def test_observations_require_repository_identity_on_both_endpoints():
    att = validate_snapshot_binding(snapshot(), binding_state())
    bad = record('a', 'b')
    bad['to'].pop('repository_id')
    with pytest.raises(StructuralIntelligenceError, match='repository_id'):
        normalize_observations([bad], snapshot(), query(), binding_attestation=att)


def test_normalization_enforces_max_nodes_and_max_paths_not_only_max_edges():
    att = validate_snapshot_binding(snapshot(), binding_state())
    too_many_nodes = [
        record('a1', 'b1'),
        record('a2', 'b2'),
        record('a3', 'b3'),
    ]
    with pytest.raises(StructuralIntelligenceError, match='max_nodes'):
        normalize_observations(too_many_nodes, snapshot(), query(max_nodes=4), binding_attestation=att)

    too_many_paths = [
        record('a', 'b', path_id='p1'),
        record('a', 'c', path_id='p2'),
        record('a', 'd', path_id='p3'),
    ]
    with pytest.raises(StructuralIntelligenceError, match='max_paths'):
        normalize_observations(too_many_paths, snapshot(), query(max_nodes=10, max_paths=2), binding_attestation=att)


def test_discovery_hints_reject_authoritative_or_unmarked_observation_sets():
    att = validate_snapshot_binding(snapshot(), binding_state())
    obs = normalize_observations([record('a', 'b')], snapshot(), query(), binding_attestation=att)
    bad = copy.deepcopy(obs)
    bad['non_authoritative'] = False
    with pytest.raises(StructuralIntelligenceError, match='non_authoritative'):
        derive_discovery_hints(bad, max_hints=5)

    bad = copy.deepcopy(obs)
    bad['observations'][0]['non_authoritative'] = False
    with pytest.raises(StructuralIntelligenceError, match='non_authoritative'):
        derive_discovery_hints(bad, max_hints=5)
