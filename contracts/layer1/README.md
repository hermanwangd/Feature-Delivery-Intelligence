# Layer 1 Contract Binding

The governing Layer 1 semantic contract is the approved external source locked as `L1-SEM` in `governance/approved-source-lock.json`; the physical Markdown I/O contract is locked as `L1-IO`.

This clean baseline intentionally does not recreate those approved semantics from summaries. Runtime/schema work here must conform to the locked sources and MUST NOT redefine T1–T4, gates, Context/Evidence authority, lifecycle, Change Surface, or T4 independence.

Approved canonical flow:

```text
T1 Intention       -> INTENTION_READY | BLOCKED
T2 Delivery Spec   -> SPEC_READY      | BLOCKED
T3 Implementation  -> CHANGE_SET_READY| BLOCKED
T4 Correctness     -> PASS | FAIL | INCONCLUSIVE
```
