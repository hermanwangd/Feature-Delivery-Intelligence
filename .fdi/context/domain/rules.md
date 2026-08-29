# FDI domain rules

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Feature delivery
- Owner: Domain, product, and governance owners
- Approver: Domain, product, and governance owners
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Superseded by: none

<a id="purpose"></a>
## Purpose

Defines durable workflow invariants and validation implications.

<a id="invariants"></a>
## Invariants

Exactly four canonical feature transitions; one Intention bundle/producer/gate; immutable source evidence; registry-first conditional selection; explicit bidirectional traceability; independent verdict authority.

<a id="decision-rules"></a>
## Decision rules

Contract-ready is pre-execution only. Execution-verified requires all declared executions and independent evidence. PASS requires every blocking deviation resolved.

<a id="regulatory-obligations"></a>
## Regulatory obligations

No additional regulatory obligation is asserted by available evidence. Security/redaction and source-authority controls remain mandatory.

<a id="exceptions"></a>
## Exceptions

No active domain exception.

<a id="validation-implications"></a>
## Validation implications

Reject mutable evidence, missing stable anchors, implicit paths, stale/superseded selection, unsupported current topology, fabricated historical intent, and self-awarded independence.

<a id="provenance"></a>
## Provenance

- Profile starting revision: 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed profile candidate: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Authoritative inputs:
  - feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
  - feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Producer: HERM-209 profile bootstrap
- Produced: 2026-08-30
- Validation method: approved-profile schema projection with stable-anchor review

<a id="freshness-and-supersession"></a>
## Freshness and supersession

- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Refresh triggers: governing contract, ownership, repository, topology, or policy change
- Lifecycle: ACTIVE
- Superseded by: none
- Conflict behavior: block dependent claims and route to the named owner; never silently choose a convenient source.
