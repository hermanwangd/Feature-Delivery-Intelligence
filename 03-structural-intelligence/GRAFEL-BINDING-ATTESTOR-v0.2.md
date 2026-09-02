# Grafel Snapshot Binding Attestor v0.2

**FDI release:** v0.4.7.2<br>
**Provider binding:** Grafel v0.3.0 (commit `b037c3f`)<br>
**Classification:** versioned provider-contract amendment; not a governing Layer 1 or Product Asset contract.

## Amendment scope

This version amends only the `grafel_orient` queryability-evidence clause in
`GRAFEL-BINDING-ATTESTOR-v0.1.md`. Version v0.1 remains immutable provenance for
the original integration and the two recorded HERM-220 fail-closed runs. All
identity, revision, repository-set, bounded-query, freshness, normalization,
and authority requirements from v0.1 remain in force.

## Rationale

The validated Grafel v0.3.0 `grafel_orient(view="me")` response does not emit a
`queryable` field. It does emit the exact resolved `group` and `indexed_ref`
along with boolean `warming` and `indexing` state. Requiring an invented field
prevents the attestor from recognizing this provider version's affirmative
route-readiness evidence even when the provider returned the exact requested
route and explicitly reported that no warming or indexing was active.

The amendment binds the predicate to fields Grafel v0.3.0 actually emits while
preserving fail-closed-on-omission and fail-closed-on-contradiction behavior.

## Queryability evidence

For Grafel v0.3.0, the explicit route is `QUERYABLE` only when one non-empty
`grafel_orient(view="me", group, ref)` response satisfies every condition below:

- `group` is present and exactly equals the requested provider scope;
- `indexed_ref` is present and exactly equals the requested provider ref;
- `warming` is present and is the boolean `false` value (`warming = false`);
- `indexing` is present and is the boolean `false` value (`indexing = false`);
- the response contains no provider error; and
- if `queryable` is present, its value is exactly boolean `true`; an explicitly
  false or non-boolean value is contradictory evidence and fails closed.

The `queryable` field is not required because Grafel v0.3.0 omits it. Numeric
`0`, null, empty strings, missing fields, and other false-like substitutes do
not satisfy either readiness boolean. The absence of an error alone is never
sufficient for `QUERYABLE`.

## Preserved exact revision proof

After the route probe succeeds, the attestor still requires all v0.1 graph
header proof without modification:

- every FDI repository identity has one explicit, unique Grafel repo-slug map;
- group metadata `id` is present and exactly matches the requested scope;
- the metadata repository set exactly matches `StructuralSnapshotRef`;
- every repository has `indexed_ref == provider_ref`;
- every `indexed_sha` is a hexadecimal prefix-equivalent Git SHA of the
  canonical `StructuralSnapshotRef` revision, with at least 12 characters; and
- the normalized binding retains the full canonical revision and attested
  provider repository slug.

These checks occur independently of the orient readiness predicate. Exact
route readiness cannot substitute for per-repository SHA or set equivalence.

## Frozen and live/current scopes

`FROZEN_INDEXED` and `LIVE_CURRENT` retain the v0.1 meanings. A frozen replay
must still use its dedicated, exact group/ref and canonical multi-repository
revision vector. Current HEAD, implicit cwd routing, and scheduler freshness do
not replace the explicit route and graph-header proof.

## Bounded-query and authority boundary

Successful attestation permits only the existing bounded structural query
path. This amendment does not change query limits, result normalization,
non-authoritative output, or any downstream `QUERYABLE` consumer in
`runtime/structural_intelligence.py`.

The attestor continues to prove only that a structural query is routed to the
intended indexed source snapshot. It does not establish current Feature truth,
`CONFIRMED`, `EXCLUDED`, `ChangeSurfaceSet`, `SPEC_READY`, Product Asset
publication, lifecycle transitions, DEV-204, F001, empirical proof, a release
claim, or `Execution-verified` status.

## Execution status

The v0.2 contract and local regression implementation are part of the HERM-224
work package. The HERM-220 live gate is **NOT EXECUTED** under this amended
contract in this package. Its previously recorded fail-closed evidence remains
historical evidence and must not be rewritten as a successful attestation.
