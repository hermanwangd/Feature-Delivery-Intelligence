# FDI MVP v0.4.7.2 — Live Grafel Snapshot Binding Implementation

**Status:** implementation overlay; live provider execution pending
**Inherits:** v0.4.7.1 Structural Intelligence contracts and frozen F001/DEV-204 evaluation semantics

## Goal

Implement the provider-specific `SnapshotBindingAttestor` seam required before FDI may consume a Grafel structural graph as source-bound runtime intelligence.

## Implementation

```text
StructuralSnapshotRef
        ↓
StaticGrafelSnapshotRouteResolver
        ↓
GrafelSnapshotBindingAttestor
        ├── grafel_orient(view=me, group, ref)
        └── Grafel dashboard GET /api/v2/groups/{group}
                    ↓
          per-repo indexed_ref / indexed_sha
                    ↓
       exact canonical revision comparison
                    ↓
       provider-independent binding state
                    ↓
       SnapshotBindingAttestation
                    ↓
              GrafelAdapter
```

The implementation is in `runtime/grafel_binding_attestor.py`.

## Exact source rule

For every repository in `StructuralSnapshotRef`:

1. the FDI repository identity MUST map explicitly to one Grafel repository slug;
2. the Grafel group metadata MUST report the attested `provider_ref` as `indexed_ref`;
3. the Grafel `indexed_sha` MUST be hexadecimal Git-SHA prefix-equivalent to the canonical pinned revision;
4. the explicit `group/ref` route MUST be queryable and not warming/indexing;
5. the attested repository set MUST exactly equal the snapshot repository set.
6. every repository-aware provider request MUST use the attested Grafel slug, while normalized FDI outputs retain the FDI repository identity.

`grafel_orient` must explicitly return the exact requested scope/ref, `queryable = true`, `warming = false`, and completed indexing state. Group metadata must explicitly identify the requested scope. Missing fields, empty responses, ambiguous mappings, or extra/missing repositories fail closed.

A metadata declaration without these checks does not establish source binding.

## Replay rule

For F001 or other temporal replay, `FROZEN_INDEXED` is valid. If one natural Grafel ref cannot represent the exact multi-repository cutoff vector, materialize a dedicated replay group/ref over worktrees or branches fixed at those commits and bind that group through the same attestor.

The example route shape is `03-structural-intelligence/examples/grafel-snapshot-routes.example.json`.

## No experiment refreeze

v0.4.7.2 does not alter the v0.4.7.1 H01–H05 freeze, F001 four-arm ablation, PA-03 CB-01 identity-only shared substrate, or DEV-204 scenarios. It only implements the live Grafel source-binding seam required by those experiments.

## Claim boundary

Local tests may establish that the attestor implementation is fail-closed and composes with `GrafelAdapter`. They do not establish:

- live Grafel connectivity;
- a real Product/repository snapshot;
- DEV-204 fresh-context behavior;
- F001 uplift;
- current Feature truth;
- a canonical FDI release.

This execution environment has no Grafel daemon/CLI/MCP endpoint, so the live provider gate remains unexecuted.
