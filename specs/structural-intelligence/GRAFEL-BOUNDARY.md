# NON-NORMATIVE IMPLEMENTATION BOUNDARY / LIVE PROOF NOT EXECUTED

# Grafel Boundary

Grafel is the preferred MVP implementation of `CodeIntelligenceProvider`.

It may provide bounded cross-repo topology, structural search, traces and diffs. It is not Product truth and it does not create a new Layer 2 Asset family.

## Provider-neutral path

```text
StructuralSnapshotRef
      ↓
SnapshotBindingAttestation
      ↓
StructuralQuery
      ↓
CodeIntelligenceProvider
      ↓
GrafelAdapter
      ↓
StructuralObservationSet / HintSet / Delta
```

## Exact source-binding rule

A declared snapshot is not execution evidence. Before a Grafel result can support reproducible publication/evaluation, FDI must attest the exact provider scope/ref and per-repository indexed revisions against the canonical full Git revisions.

Abbreviated Git hashes are never authority. Resolve them in the matching repository object database and require full equality.

## Bounded runtime

Every query declares repository scope, relation allowlist and finite caps such as `max_depth`, `max_nodes`, `max_edges`, `max_paths` and `max_result_bytes`.

## No Grafel basis

Do not invent a `GRAFEL` candidate basis. Structural hints augment investigation only after PA-03 repository identity grounding.
