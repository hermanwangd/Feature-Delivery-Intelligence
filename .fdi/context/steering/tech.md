# Technology steering

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Feature Delivery Intelligence product
- Owner: Architecture and security owners
- Approver: Architecture and security owners
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Superseded by: none

<a id="purpose"></a>
## Purpose

Defines authorized technology and security constraints for this documentation-only profile.

<a id="authorized-platforms"></a>
## Authorized platforms

Git, GitHub pull requests, UTF-8 Markdown, stable HTML anchors, SHA-256 digests, and authenticated Multica issue operations.

<a id="technology-constraints"></a>
## Technology constraints

Repository evidence uses immutable Git object IDs. Profile artifacts remain human-reviewable Markdown. No runtime service or dependency is introduced by HERM-209.

<a id="dependency-policy"></a>
## Dependency policy

No new software dependency is authorized. Validation may use available Git, shell, and standard-library tooling without committing tool implementations.

<a id="security-and-compliance"></a>
## Security and compliance

Persist no credentials, tokens, email addresses, unsafe raw payloads, local absolute paths, or unredacted sensitive evidence.

<a id="exceptions"></a>
## Exceptions

No active exception. Any future exception needs owner, scope, expiry, evidence, and a governed successor.

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
