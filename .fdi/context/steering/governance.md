# Governance steering

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Feature Delivery Intelligence product
- Owner: FDI governance owner
- Approver: FDI governance owner
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Superseded by: none

<a id="purpose"></a>
## Purpose

Defines owners, authority dimensions, review cadence, conflict resolution, extensions, and deprecation.

<a id="ownership"></a>
## Ownership

Product owner owns outcomes; architecture/security/domain/delivery/release owners own durable constraints; repository owners own source boundaries; independent verifiers own verdicts.

<a id="authority-by-dimension"></a>
## Authority by dimension

Authorized Intention/Spec govern desired behavior; Steering/Domain govern invariants; pinned source/tests/runtime observations govern current behavior; Knowledge and derived views only explain/navigate.

<a id="approval-matrix"></a>
## Approval matrix

| Decision | Required authority |
| --- | --- |
| Product outcome | Product owner |
| Source scope/candidate | Repository owner |
| Architecture/security exception | Relevant owner |
| V&V verdict | Independent verifier |
| Release | Source/release owner |
| B3 adoption | Independent B3b PASS plus row owners |

<a id="review-cadence"></a>
## Review cadence

Steering/Domain: 180 days. Codebase/Operations/Skills: 90 days. Evidence: candidate-specific validity and explicit expiry.

<a id="conflict-resolution"></a>
## Conflict resolution

Classify conflict by revision, environment, scope, authority, owner, and trust. Record the gap and block dependent claims until the governing owner authorizes a revision or exception.

<a id="extension-admission"></a>
## Extension admission

Register exact ID/path/digest, ACTIVE lifecycle, applies_to, owner, trust, review/expiry, and empty successor before creating or selecting a conditional leaf.

<a id="deprecation"></a>
## Deprecation

Mark SUPERSEDED, retain traceability, name successor, exclude by default, and preserve retired stable anchors.

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
