# Delivery steering

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Feature Delivery Intelligence product
- Owner: Delivery and release owners
- Approver: Delivery and release owners
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Superseded by: none

<a id="purpose"></a>
## Purpose

Defines canonical workflow, gates, evidence, release boundaries, and re-entry.

<a id="workflow-semantics"></a>
## Workflow semantics

Human -> Intention -> Delivery Spec -> Change Set -> Verification & Validation Report. Context is supporting input; Baseline and refresh are support workflows.

<a id="transition-gates"></a>
## Transition gates

The sole Intention gate is .fdi/features/{feature-id}/intention.md#gate-record; Spec gates at .fdi/features/{feature-id}/spec/index.md#gate-record; Change Set gates at .fdi/features/{feature-id}/change-set/index.md#gate-record; V&V gates at .fdi/features/{feature-id}/vv-report.md#gate-record.

<a id="evidence-policy"></a>
## Evidence policy

Every claim has immutable candidate/environment identity, method, observation, result, integrity/access, owner, limitations, validity, expiry, and successor. Raw source-owned artifacts remain at their authority.

<a id="change-and-release"></a>
## Change and release

Candidate commits and PR heads are distinct. A PASS pre-release V&V does not establish release. Refresh waits for a separately authenticated release event and independent B3 verification.

<a id="re-entry"></a>
## Re-entry

Upstream revision, failed selector, unresolved blocking deviation, stale evidence, or authority conflict re-enters the earliest invalid artifact. No deviation record authorizes a source read.

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
