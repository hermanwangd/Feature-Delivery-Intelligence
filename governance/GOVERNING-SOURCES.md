# Governing Sources — Clean Development Baseline v0.4.8.2

This project is a **normal development baseline**, not a recovery workspace.

The approved semantic sources are pinned by stable source identity in `approved-source-lock.json`.
They are external because their original approved bytes are not embedded in this package.

## Development rule

Implementation may continue against the locked conformance surfaces, but **semantic specification changes are prohibited** until the exact approved source bytes are rehydrated and digest-pinned.

## Locked architecture

- Layer 1: T1 Intention → T2 Delivery Spec → T3 Implementation → T4 Correctness.
- FT-T2 Feature Closure is subordinate to T2.
- FT-T2: exactly six helper contracts and five helper Skills.
- `SPEC_READY | BLOCKED` is the sole canonical T2 gate.
- Layer 2: durable Product Intelligence; PA-03 and PA-05 are the fully specified v0.1 profiles.
- PA-01 Product Semantics remains a proposal until separately promoted.
- Current Feature `CONFIRMED`/`EXCLUDED` and Change Surface truth require current feature-specific pinned Evidence.
- Grafel is a replaceable `CodeIntelligenceProvider`, not Product Knowledge authority.
- Product-owned Git-backed `ProductIntelligenceStore` is the MVP physical PK store candidate.
