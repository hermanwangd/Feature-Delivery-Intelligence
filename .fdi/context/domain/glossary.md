# FDI domain glossary

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Feature Delivery Intelligence delivery semantics
- Owner: Domain and product owners
- Approver: Domain and product owners
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Superseded by: none

<a id="purpose"></a>
## Purpose

Defines stable delivery vocabulary and deterministic aliases without source topology.

<a id="terms"></a>
## Terms

| Term | Definition |
| --- | --- |
| Intention | Authorized outcome, scope, scenarios, criteria, and non-goals |
| Delivery Spec | Traceable requirements, design, tasks, selectors, and V&V plan |
| Change Set | Pinned source candidate commits/PRs plus mappings |
| V&V Report | Independent verification and validation verdict |
| Context | Governed constraints/evidence consulted by an execution |
| Baseline | Evidence-backed as-is capability summary, subordinate to newer pinned evidence |

<a id="actors"></a>
## Actors

| Actor | Responsibility |
| --- | --- |
| Human/product owner | Authorizes desired outcome |
| Intention agent | Captures authenticated request and criteria |
| Spec agent | Produces bounded technical contract |
| Implementation agent | Produces source candidate and mappings |
| Independent V&V agent | Reproduces evidence and owns verdict |

<a id="state-vocabulary"></a>
## State vocabulary

ACTIVE, SUPERSEDED, current, planned, retired, CONTRACT_READY, NOT_CONTRACT_READY, PASS, FAIL, INCONCLUSIVE, NOT_CLAIMED, NOT_INVOKED, NOT_OBSERVED.

<a id="alias-to-id-mapping"></a>
## Alias-to-ID mapping

| Alias | Canonical ID |
| --- | --- |
| Feature Delivery Intelligence | product-feature-delivery-intelligence |
| FDI coordination | system-fdi-coordination |
| FDI documentation | component-fdi-documentation |
| Feature-Delivery-Intelligence repository | feature-delivery-intelligence |

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
