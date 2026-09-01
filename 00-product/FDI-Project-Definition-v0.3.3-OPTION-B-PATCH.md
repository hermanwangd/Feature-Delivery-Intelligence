# FDI Project Definition v0.3.3 — Option B MVP Proof Patch

**Status:** APPROVED DIRECTION / PATCH CANDIDATE FOR CANONICAL PROJECT DEFINITION

This patch changes the MVP proof question only. It does not redefine Layer 1 T1–T4, HERM-211 FT-T2, the six helper contracts, the five helper Skills, or the `SPEC_READY | BLOCKED` T2 gate.

## Revised MVP scope and proof question

The MVP evaluates the complete governed Product Knowledge → Feature Discovery architecture, not only PA-03 repository indexing or PA-05 historical lookup.

### Primary hypothesis

> **Does governed Product Knowledge improve a fresh agent's ability to discover the correct current-feature Change Surface, with higher quality and lower human effort than feature investigation without FDI Product Knowledge, while preserving current feature-specific pinned Evidence as the authority for current Change Surface truth?**

### Product Knowledge treatment

For the MVP, Product Knowledge means the bounded, governed combination of:

1. **Product Semantics** — Product → Sub-product* → Capability plus applicable durable semantic/domain constraints by exact governed refs;
2. **Product Realization** — bounded typed realization/navigation relations from Capability/technical nodes to PA-03 repository grounding;
3. **Delivery Intelligence** — PA-05 historical delivery facts/patterns used only as candidate priors;
4. **FeatureKnowledgePlan** — non-canonical per-feature binding of the root Skill's already-declared Context requirement classes to exact governed ProductAssetRefs.

### Truth boundary

```text
Product Semantics
Product Realization
Delivery Intelligence
        ↓
understand / constrain / navigate / prioritize
        ↓
Candidate investigation
        ↓
current feature-specific pinned Evidence
        ↓
CONFIRMED / EXCLUDED / UNRESOLVED
        ↓
Change Surface
        ↓
SPEC_READY | BLOCKED
```

Product Knowledge MUST NOT by itself establish current `CONFIRMED`, current `EXCLUDED`, current implementation truth, or `SPEC_READY`.

## Baseline and treatment

### Baseline arm

Receives:

- the same frozen historical Feature input;
- the same pre-feature repository/source access;
- the same model family/configuration;
- the same execution/tool budget;
- ordinary bounded repository/issue/PR/commit investigation capabilities.

Does **not** receive:

- FDI governed Product Semantics;
- FDI Product Realization graph;
- FDI Delivery Intelligence context;
- FeatureKnowledgePlan;
- FDI Product Knowledge Context resolution.

The baseline may independently search/read allowed source material. It is not intentionally deprived of ordinary engineering access.

### FDI treatment arm

Receives everything available to the baseline plus:

- exact governed Product Semantics refs;
- bounded Product Realization refs;
- eligible Delivery Intelligence refs;
- FeatureKnowledgePlan instantiated from root Skill-declared requirements;
- bounded Context resolution and FDI Feature Discovery Skills.

## MVP outcome dimensions

Primary outcome dimensions:

- Change Surface repository recall/precision;
- material path/interface/schema/config/test obligation recall/precision when ground truth supports scoring;
- unsupported required claims;
- false inclusion/exclusion;
- false `SPEC_READY` / false closure;
- T2 gate correctness;
- investigation tool calls/steps;
- Context/model tokens and cost;
- cycle time;
- retries/escalations;
- human clarification/correction/intervention.

Repository discovery is a component metric, not the sole MVP success definition.

## Decision rule

The MVP produces `CONTINUE | REVISE | STOP` only from governed F001 calibration plus F002–F005 blind holdout evidence. Local deterministic tests, synthetic fixtures, DEV-204 structural/behavioral validation, or live Multica installation do not establish empirical Product Knowledge uplift.
