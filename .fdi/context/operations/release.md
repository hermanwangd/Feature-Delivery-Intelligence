# Release Context

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

Defines source/release responsibilities, gates, rollback, evidence, and authority.

<a id="release-topology"></a>
## Release topology

HERM-209 produces a GitHub PR targeting main. A pre-release candidate is not a release or deployment.

<a id="repository-responsibilities"></a>
## Repository responsibilities

Source repository owns branch protection, review, CI, merge, release, rollback, and exact source content. Coordination profile owns aggregate mappings and safe evidence references.

<a id="promotion-gates"></a>
## Promotion gates

Candidate base/head adjacency; exact README-only source diff; independent V&V; source review/checks; merge authorization. B3 support requires a later authenticated release observation.

<a id="rollback"></a>
## Rollback

Before merge, update or close the PR. After release, source owner performs repository rollback; Context adoption remains unchanged unless B3b independently verifies and atomically adopts.

<a id="evidence"></a>
## Evidence

PR URL/number, target, immutable heads, check snapshot, review state, merge/release event ID, environment, observation time/method, and digest.

<a id="authority"></a>
## Authority

Repository/release owner authorizes merge/release. V&V agent cannot release; refresh agent cannot adopt current Context.

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
