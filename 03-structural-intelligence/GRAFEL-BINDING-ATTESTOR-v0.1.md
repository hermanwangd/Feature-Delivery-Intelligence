# Grafel Snapshot Binding Attestor v0.1

**FDI release:** v0.4.7.2
**Classification:** provider-specific implementation support; not a governing Layer 1 or Product Asset contract.

## Purpose

`StructuralSnapshotRef` pins canonical repository revisions, while `GrafelAdapter` must query an exact Grafel `group/ref`. The concrete `GrafelSnapshotBindingAttestor` closes that execution gap without turning provider metadata into Product truth.

```text
StructuralSnapshotRef
        ↓
StaticGrafelSnapshotRouteResolver
        ↓ explicit group/ref + repository identity map
GrafelSnapshotBindingAttestor
        ├─ grafel_orient(view=me, group, ref)
        │    proves the explicit provider route is queryable and not warming/indexing
        └─ Grafel dashboard group metadata
             reads per-repo graph-header indexed_ref / indexed_sha
        ↓
provider-independent binding state
        ↓
validate_snapshot_binding
        ↓
SnapshotBindingAttestation
```

## Exact revision proof

Grafel graph metadata stores `indexed_ref` and an abbreviated `indexed_sha`. The attestor requires:

- the Grafel repo slug to be explicitly mapped from each FDI repository identity;
- `indexed_ref == provider_ref` for every repository;
- the Grafel `indexed_sha` to be a hexadecimal prefix-equivalent Git SHA of the canonical revision in `StructuralSnapshotRef`;
- the repository set to match the snapshot exactly;
- `grafel_orient` to return non-empty, exact `group` and `indexed_ref` identity;
- explicit `queryable = true`, `warming = false`, and completed `indexing` state; and
- group metadata `id` to be present and exactly match the requested scope.

The normalized provider state returns the full canonical revision as `indexed_revision` and the mapped slug as `provider_repository`. The resulting attestation ID covers both values, so a later query can prove that it used the exact mapping validated against the snapshot. Missing readiness or identity fields fail closed; absence of an error is never sufficient for `QUERYABLE`.

## Frozen replay scope

`FROZEN_INDEXED` is valid. For a multi-repository F001 cutoff, use a dedicated Grafel replay group/ref whose repositories are indexed at the exact cutoff vector. Every repository may use the same synthetic ref name (for example `fdi/f001-cutoff`) while pointing to a different commit in its own Git repository.

Do not substitute current HEAD, implicit cwd routing, or a future graph snapshot.

## Live/current scope

`LIVE_CURRENT` uses the same proof contract. Freshness is a facet; it does not weaken revision equivalence.

## Dashboard dependency

The reference `GrafelDashboardGroupMetadataClient` reads:

```text
GET /api/v2/groups/{group}
```

and expects the Grafel repository metadata fields `slug`, `indexed_ref`, and `indexed_sha`. The dashboard base URL is explicit configuration; FDI does not invent a port.

If the endpoint is unavailable, the binding attestor fails closed.

## Authority boundary

The attestor proves only that a structural query is routed to the intended indexed source snapshot. It does not establish current Feature truth, `CONFIRMED`, `EXCLUDED`, `ChangeSurfaceSet`, `SPEC_READY`, Product Asset publication, or lifecycle transitions.

## Execution status

The v0.4.7.2 implementation and local contract tests exist. This environment has no `grafel` binary/daemon/MCP endpoint, therefore the real provider call is **NOT EXECUTED** and no real Product snapshot is claimed.
