# Architecture steering

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Feature Delivery Intelligence product
- Owner: Architecture owner
- Approver: Architecture owner
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Superseded by: none

<a id="purpose"></a>
## Purpose

Defines normative architecture and authority boundaries.

<a id="principles"></a>
## Principles

Separate logical artifacts from physical bundles; separate desired-behavior authority from observed-state evidence; select Context minimally and explicitly.

<a id="system-boundaries"></a>
## System boundaries

The coordination boundary owns aggregate feature artifacts and curated Context. Each source-repository boundary owns source, tests, configuration, interfaces, CI, review, and release.

<a id="quality-attributes"></a>
## Quality attributes

Traceability, auditability, safety, deterministic selection, freshness, idempotency, and multi-repository extensibility.

<a id="authorized-patterns"></a>
## Authorized patterns

Registry-first selection, immutable revision pins, staged selectors, explicit stable anchors, independent V&V, compare-and-swap adoption after B3b PASS.

<a id="prohibited-patterns"></a>
## Prohibited patterns

Mutable branch evidence, self-authorizing output selectors, planned-as-current topology, collapsed B3 roles, source copies, implicit fixed-read bundles, or self-awarded verification.

<a id="interface-and-data-constraints"></a>
## Interface and data constraints

References preserve repo ID, path, revision, authority, integrity, access, and redaction. No API/data interface is introduced by the documentation-only pilot.

<a id="exceptions"></a>
## Exceptions

No active architecture exception.

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
