# FDI MVP v0.4.7.1 — Structural Intelligence Source-Binding & Evaluation Hardening

**Status:** implementation-overlay hardening increment
**Supersedes:** v0.4.7.0 source binding, StructuralDelta provenance, and F001/DEV-204 evaluation details where they conflict with this document.
**Does not modify:** Layer 1 T1–T4 governing transitions, HERM-211 six helper contracts, the canonical `SPEC_READY | BLOCKED` gate, or the rule that current feature-specific Evidence establishes current Change Surface truth.

## 1. Why this patch exists

v0.4.7.0 correctly placed Structural Intelligence inside FDI, but local review found four claims that were not yet strong enough to support replay-safe execution:

1. `StructuralSnapshotRef` declared source revisions but a live Grafel query did not prove the provider graph route matched them.
2. graph diff accepted pinned-looking refs without independently attesting both before and after provider refs.
3. some traversal budgets were contract fields rather than proven postconditions.
4. F001 Structural-only still depended on PA-03 repository grounding without separating neutral repository identity from semantic Product Intelligence.

v0.4.7.1 hardens those boundaries before DEV-204 or F001 execution.

## 2. Source binding

A snapshot declaration alone is not execution evidence. Source binding is defined as **exact revision equivalence + queryability + routed provider identity**, not “current HEAD”.

```text
StructuralSnapshotRef
        ↓
provider/version-specific binding attestor
        ↓
SnapshotBindingAttestation
  ├── provider scope
  ├── provider ref
  ├── exact repository revisions
  ├── queryability
  └── LIVE_CURRENT | FROZEN_INDEXED
        ↓
GrafelAdapter queries the same attested scope/ref
        ↓
bounded Structural query
```

Historical indexed refs are valid when exact and queryable even if HEAD has advanced. `grafel_index_status` alone is insufficient to prove this general contract, so v0.4.7.1 uses an injected `binding_attestor` seam and makes no claim that the live Grafel attestor has been executed.

## 3. Diff authority

Structural diff requires **two** independently pinned and queryable endpoints:

```text
before StructuralSnapshotRef + binding attestation
                     ↓
       before provider ref
                     ↓
                Grafel diff
                     ↑
        after provider ref
                     ↑
after StructuralSnapshotRef + binding attestation
```

Both provider refs must prove their exact canonical revisions and share the provider scope used by the diff. They do not both need to be scheduler-current. `StructuralDelta` preserves both snapshot IDs and both attestation IDs and remains non-authoritative.

## 4. Bounded runtime

FDI enforces its own finite result postconditions:

```text
max_nodes
max_edges
max_paths
max_result_bytes
relation allowlist
repository scope
```

Trace/path normalization requires path provenance sufficient to enforce `max_paths`.

## 5. F001 evaluation isolation

All four F001 arms may share a **PA-03 CB-01 identity-only repository substrate** when canonical repository normalization requires it. This substrate contains repository identity only and must not carry capability terms, Product Realization, Delivery Intelligence, semantic descriptions, inferred ownership, or ranking priors.

The experimental variables remain:

```text
A baseline:                  semantic PI NO / Structural NO
B structural only:           semantic PI NO / Structural YES
C Product Intelligence only: semantic PI YES / Structural NO
D Full FDI:                  semantic PI YES / Structural YES
```

This prevents the Structural-only arm from being mislabeled while retaining a common repository identity substrate across all four arms.

## 6. DEV-204 evidence semantics

System-behavior pressure cases are not Skills. v0.4.7.1 execution evidence therefore uses:

```text
target_kind = SKILL | SYSTEM_BEHAVIOR
target_loaded = false | true
```

rather than representing every target as `target_skill_loaded`.

No status is upgraded by packet generation. Fresh independent RED/GREEN execution and reviewer evidence remain required.

## 7. Authority invariants retained

Structural Intelligence may orient, discover, prioritize, trace, and generate maintenance review signals. It does not establish current Feature truth or silently mutate Product Assets.

```text
Product Intelligence + Structural Intelligence
                  ↓
        bounded candidate investigation
                  ↓
     current feature-specific Evidence
                  ↓
        current Change Surface truth
```

No new Layer 1 transition, Product Asset family, HERM-211 helper contract, candidate basis, or canonical gate is introduced by v0.4.7.1.
