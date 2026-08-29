# Environment Context

<a id="status"></a>
## Status

- State: CURRENT
- Scope: HERM-209 candidate and review environments
- Owner: Platform, release, repository, and security owners
- Approver: Platform, release, repository, and security owners
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2026-11-28
- Superseded by: none

<a id="purpose"></a>
## Purpose

Defines environments and safe access boundaries.

<a id="environment-inventory"></a>
## Environment inventory

| Environment ID | Purpose | Revision identity | Status |
| --- | --- | --- | --- |
| candidate-git | Local immutable Git object inspection and candidate construction | exact commit SHA | ACTIVE |
| github-pr | External review/check surface | PR number plus head SHA | ACTIVE |

<a id="owners"></a>
## Owners

Repository owner owns candidate-git and GitHub source controls; governance/security owners own access policy.

<a id="access-and-approvals"></a>
## Access and approvals

Authenticated local Git reads and authorized branch/PR writes are permitted for HERM-209. Deployment, secrets, permissions, and destructive actions require separate authorization.

<a id="configuration-references"></a>
## Configuration references

Repository controls and PR metadata remain at the source authority; coordination files retain safe immutable references only.

<a id="data-constraints"></a>
## Data constraints

No production data. Persist no credential, token, email, local absolute path, or unsafe raw payload.

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
- Next review: 2026-11-28
- Refresh triggers: governing contract, ownership, repository, topology, or policy change
- Lifecycle: ACTIVE
- Superseded by: none
- Conflict behavior: block dependent claims and route to the named owner; never silently choose a convenient source.
