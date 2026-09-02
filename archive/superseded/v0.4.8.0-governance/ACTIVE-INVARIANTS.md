# FDI Active Invariants

## Layer 1

```text
T1 Intention
    ↓
T2 Delivery Spec
    ↓
T3 Implementation
    ↓
T4 Correctness
```

HERM-211 Feature Closure is an FT-T2 capability inside T2.

Exact helper contract names:

- `IntentSpec`
- `CandidateRepoSet`
- `ChangeSurfaceSet`
- `EvidenceRecord`
- `ClosurePackage`
- `ClosureReview`

Exact helper Skill names:

- `feature-intent-analysis`
- `repo-discovery`
- `changesurface-investigation`
- `dependency-closure`
- `closure-review`

Closure status:

```text
OPEN
PARTIAL
CLOSED_WITHIN_DECLARED_SCOPE
```

Sole canonical T2 gate:

```text
SPEC_READY | BLOCKED
```

## Layer 2

Layer 2 is durable Product Intelligence. It may provide semantics, realization knowledge, delivery priors and candidate seeds.

It must not directly establish current-feature `CONFIRMED` / `EXCLUDED` Change Surface truth.

## Structural Intelligence

Structural Intelligence is a shared runtime capability. It may discover, trace, orient and prioritize. It is not a Product Asset family and not a new HERM-211 contract.

## Current truth

```text
Product Intelligence
+ Structural Intelligence
        ↓
bounded candidate investigation
        ↓
current feature-specific pinned Evidence
        ↓
current Change Surface truth
```
