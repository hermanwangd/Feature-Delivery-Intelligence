# Product steering

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Feature Delivery Intelligence product
- Owner: Product owner
- Approver: Product owner
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Superseded by: none

<a id="purpose"></a>
## Purpose

Defines desired product outcomes and boundaries.

<a id="product-purpose"></a>
## Product purpose

Build an AI-native engineering capability that determines the complete evidence-backed change surface and drives correct, traceable, production-ready feature delivery.

<a id="users-and-stakeholders"></a>
## Users and stakeholders

Product owners, engineering owners, architecture/security/release owners, repository owners, implementation agents, and independent verifiers.

<a id="value-and-outcomes"></a>
## Value and outcomes

Correct feature delivery, early dependency detection, preserved interfaces and architecture, safe execution, and verifiable evidence.

<a id="boundaries"></a>
## Boundaries

The profile coordinates intent and evidence across repositories; it does not replace source-repository authority or release controls.

<a id="non-goals"></a>
## Non-goals

No control plane, universal ledger, bulk source copy, fabricated historical feature, or fifth workflow stage.

<a id="principles"></a>
## Principles

Evidence before claims; immutable source reads; registry-first selection; least authority; bidirectional traceability; explicit re-entry on conflict.

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
