# Structural Intelligence → Feature Discovery Integration v0.1

**FDI release:** v0.4.7.0<br>
**Scope:** T2 candidate augmentation only.

## Contract

Structural Intelligence produces non-authoritative repository hints. A hinted repository may contribute to T2 repository investigation only after exact repository identity is grounded in eligible PA-03 state.

```text
StructuralDiscoveryHintSet
        ↓
PA-03 identity grounding
        ↓
repository candidate augmentation
        ↓
current feature investigation
        ↓
current feature-specific Evidence
        ↓
CONFIRMED / EXCLUDED / UNRESOLVED
```

The candidate augmentation uses the existing legal basis:

```text
basis = LAYER2_PA03
```

Structural provenance is supplementary:

```text
structural_snapshot_id
structural_observation_ids
structural_relation_types
structural_evidence_refs
```

Structural Intelligence does not define a new HERM-211 candidate basis and cannot directly establish `CONFIRMED`, `EXCLUDED`, `ChangeSurfaceSet`, or `SPEC_READY`.

Unknown, stale, superseded, out-of-product-scope, or otherwise ineligible PA-03 identities do not become candidates. They remain diagnostics/incompleteness for bounded investigation.
