# Layer 1 Approved Conformance View

**Source identity:** `fdi-layer1-specification-v0.2-approved.md` / `file_00000000685482118de1eec4e5a218c7`.

This is a non-authoritative local conformance view.

```text
T1 Intention      -> intention.md      -> INTENTION_READY | BLOCKED
T2 Delivery Spec  -> spec.md           -> SPEC_READY | BLOCKED
T3 Implementation -> implementation.md -> CHANGE_SET_READY | BLOCKED
T4 Correctness    -> correctness.md    -> PASS | FAIL | INCONCLUSIVE
```

Layer 1 has exactly four canonical transformations. Context is a governed execution dependency, not a fifth stage. T2 owns feature-specific Change Surface. Current `CONFIRMED`/`EXCLUDED` findings require current feature-specific pinned Evidence when material. T4 independently separates verification from validation.
