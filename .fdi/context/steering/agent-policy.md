# Agent policy steering

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Feature Delivery Intelligence product
- Owner: Governance and security owners
- Approver: Governance and security owners
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Superseded by: none

<a id="purpose"></a>
## Purpose

Defines autonomy, approvals, sensitive-data, capability, and escalation controls.

<a id="autonomy"></a>
## Autonomy

Agents may perform bounded read/write, Git, validation, and PR operations expressly authorized by the issue and source-repository controls.

<a id="approvals"></a>
## Approvals

Product intent, architecture/repository scope, external publication, release, privileged access, destructive action, and B3 adoption require their named authorities.

<a id="sensitive-data"></a>
## Sensitive data

Redact unsafe payloads; persist only safe digests, immutable identifiers, methods, and authorized observations. Never store credentials or email addresses.

<a id="capability-boundaries"></a>
## Capability boundaries

Skills govern capability use. Missing registration, runtime, permission, binding, review, owner, or digest blocks execution; no substitute capability is inferred.

<a id="escalation"></a>
## Escalation

Conflicts, missing exact inputs, unbounded selectors, stale registries, or authority gaps return to the earliest owning artifact and named owner.

<a id="prohibited-actions"></a>
## Prohibited actions

No destructive repository rewrite, secret exposure, external deployment, release claim, B1/B2/B3 simulation, same-identity B3a/B3b, or product-wide inference from one pilot.

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
