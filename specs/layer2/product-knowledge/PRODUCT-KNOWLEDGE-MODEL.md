# NON-NORMATIVE RECOVERY DESIGN / PA-01 CANDIDATE

# Product Knowledge Model

Layer 2 retains existing Product Asset families for governance, while exposing three Layer-1-oriented knowledge roles.

## 1. Product Semantics

```text
Product
  ↓
SubProduct*
  ↓
Capability
  ↓
Behavior / Domain Rules / Invariants
```

Answers what the Product means.

## 2. Product Realization

```text
Capability
  --REALIZED_BY--> Component/System
Component
  --PROVIDES/CONSUMES--> Interface/Data Contract
Component
  --IMPLEMENTED_IN--> Repository
Repository
  --CONTAINS--> Module/Schema/Config/Test
```

Answers where/how meaning is implemented.

`Product → SubProduct → Repo` is a derived view, not the canonical relation model.

## 3. Delivery Intelligence

```text
Historical Feature
  ↓
PR / Commit
  ↓
Changed realization nodes
  ↓
Reusable delivery priors
```

Delivery Intelligence is candidate prior only; current Feature applicability requires current evidence.

## Core boundary

> Semantics tells Layer 1 what the product means. Realization tells Layer 1 where that meaning is implemented. Delivery Intelligence tells Layer 1 where similar meanings changed before. Current Evidence tells Layer 1 what actually has to change now.


> Product Semantics/PA-01 content remains candidate until explicit HERM-219 promotion. PA-03/PA-05 approved v0.1 scope is not expanded by this document.
