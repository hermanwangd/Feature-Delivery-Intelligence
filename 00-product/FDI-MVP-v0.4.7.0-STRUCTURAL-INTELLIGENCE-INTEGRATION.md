# FDI MVP v0.4.7.0 — Structural Intelligence Integration

**Status:** APPROVED DESIGN / IMPLEMENTATION TARGET  
**Supersedes for MVP experiment semantics:** `MVP-HYPOTHESIS-FREEZE-v0.4.6.2.md`  
**Does not modify:** Layer 1 T1–T4 governing transitions, HERM-211 six helper contracts, or the sole T2 `SPEC_READY | BLOCKED` gate.

## 1. Decision

FDI integrates a provider-independent **Structural Intelligence Runtime** as a shared runtime capability used by both `Maintain Product` and `Develop Feature`.

```text
Durable Product Intelligence     Live Structural Intelligence
Semantics / Realization /        bounded current code graph /
Delivery Intelligence            traces / topology / diff
            \                     /
             \                   /
              ---- Feature Intelligence ----
                         |
                bounded investigation
                         |
           current feature-specific Evidence
                         |
                 current Change Surface
```

Grafel is the preferred MVP implementation of `CodeIntelligenceProvider`, but Grafel graph state, schema, tool names, and provider confidence are not governing FDI semantics.

## 2. Authority boundary

Structural Intelligence MAY:
- discover and rank structural investigation seeds;
- expose bounded cross-repository topology and traces;
- produce `StructuralObservationSet` and `StructuralDiscoveryHintSet` runtime artifacts;
- identify realization-maintenance invalidation candidates;
- support T3 implementation navigation and T4 impact hypotheses.

Structural Intelligence MUST NOT directly establish:
- `CONFIRMED` or `EXCLUDED` current repository/surface status;
- `ChangeSurfaceSet` truth;
- `SPEC_READY`;
- semantic Product Asset publication;
- a new HERM-211 helper-contract status or basis vocabulary.

Current feature-specific pinned Evidence remains the authority for current Feature truth.

## 3. Shared runtime contracts

v0.4.7.0 introduces runtime-support contracts only:

- `CodeIntelligenceProvider`
- `StructuralSnapshotRef`
- `StructuralQuery`
- `StructuralObservationSet`
- `StructuralDiscoveryHintSet`
- `StructuralDelta`
- `RuntimeCapabilityRequirement`

These are not Product Asset families and are not HERM-211 helper contracts.

## 4. Bounded query rule

Every structural query is finite and deterministic. It declares:

- source snapshot identity;
- product/repository scope;
- allowed relation types;
- `max_depth`;
- `max_nodes`;
- `max_edges`;
- `max_paths`;
- result/token budget where applicable.

Unpinned or unbounded queries are `NOT_CONTRACT_READY` for FDI runtime use.

## 5. Snapshot reproducibility

`StructuralSnapshotRef` binds provider and adapter revisions to exact repository revisions. A structural observation without a pinned source snapshot cannot support reproducible Product Intelligence publication or F001–F005 evaluation.

## 6. Develop Feature integration

T2 consumes two distinct inputs:

```text
FeatureKnowledgePlan -> ContextRequirement -> governed Product Assets
RuntimeCapabilityRequirement -> Structural Intelligence Runtime
```

`FeatureKnowledgePlan` cannot invent structural runtime authority, and `RuntimeCapabilityRequirement` cannot masquerade as a Layer 2 Product Asset requirement.

Structural hints are grounded through exact PA-03 repository identity before they can augment repository candidates. The canonical candidate basis remains `LAYER2_PA03`; structural hint ids are supplementary provenance only.

## 7. Maintain Product integration

Structural graph changes may create `MaintenanceSignal` records for affected realization knowledge. They do not silently mutate, stale, supersede, or publish a Product Asset. Existing Layer 2 governance remains authoritative for those lifecycle actions.

## 8. Grafel adapter boundary

`GrafelAdapter` implements `CodeIntelligenceProvider` behind an FDI-owned normalized API. FDI governing contracts do not reference Grafel MCP tool names or internal graph schemas. Replacing Grafel must not require Layer 1 or Product Asset contract changes.

## 9. Option B v0.4.7.0 experiment freeze

Before F001, the MVP hypothesis is revised and frozen as:

> **Does Feature Delivery Intelligence—combining governed Product Intelligence, bounded live Structural Intelligence, and current-evidence-gated investigation—improve fresh-agent Change Surface discovery quality and efficiency?**

F001 calibration uses four arms:

| Arm | Product Intelligence | Structural Intelligence |
|---|---:|---:|
| A Baseline | no | no |
| B Structural only | no | yes |
| C Product Intelligence only | yes | no |
| D Full FDI | yes | yes |

All arms share the same feature signal, pre-feature source cutoff, model/configuration, execution budget, and evaluation rubric. F002–F005 use the primary blind comparison `Baseline vs Full FDI`; ablations are optional diagnostics and do not redefine the primary proof after F001.

No target Feature implementation, target PR/commit, post-cutoff graph state, future Delivery Intelligence, future Product Asset revision, or future Registry projection may enter an arm.

## 10. DEV-204 extension

v0.4.7.0 adds one system-behavior pressure case for Structural Intelligence integration. It is `SYSTEM_BEHAVIOR_NOT_SKILL`, not a sixth FT-T2 Skill. RED/GREEN remains fresh-context and reviewer-independent.

## 11. Exit criteria

v0.4.7.0 overlay conformance requires:

1. provider-independent runtime contracts;
2. bounded/pinned query validation;
3. Grafel adapter isolation;
4. non-authoritative structural observations/hints;
5. PA-03 grounding before candidate augmentation;
6. no structural shortcut to current truth;
7. source-driven maintenance signals without silent publication;
8. v0.4.7.0 hypothesis and F001 ablation freeze before execution;
9. DEV-204 structural system-behavior packet preparation;
10. deterministic verification/package accounting.

Canonical release, live Grafel/Multica integration, DEV-204 behavioral proof, real Product binding, and F001–F005 empirical uplift remain external gates until actually executed.
