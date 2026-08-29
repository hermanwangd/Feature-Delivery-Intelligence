# Observability Context

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

Defines available signals and evidence-capture limits for the documentation-only pilot.

<a id="signals"></a>
## Signals

Git object graph, diff output, file inventory, Markdown checks, PR provider metadata, and check-rollup snapshots.

<a id="service-entity-mapping"></a>
## Service/entity mapping

No runtime service. Git evidence maps to Repository feature-delivery-intelligence and Component component-fdi-documentation.

<a id="environment-mapping"></a>
## Environment mapping

candidate-git for local checks; github-pr for provider review/check metadata.

<a id="query-entry-points"></a>
## Query entry points

git rev-parse, git merge-base, git diff, git ls-tree, git show, gh pr view, and Multica linked-PR readback where authorized.

<a id="access-redaction"></a>
## Access/redaction

Use authenticated tools; record safe results/digests, never tokens, credentials, private payloads, or user-local paths.

<a id="retention"></a>
## Retention

Committed evidence persists with the feature. Raw provider logs remain provider-owned under its retention policy.

<a id="evidence-capture"></a>
## Evidence capture

Every captured observation includes candidate/environment, command or method, timestamp, result, integrity, limitations, validity, and successor.

<a id="known-gaps"></a>
## Known gaps

No production runtime or release signal exists before merge; vv-report release observation must remain NOT_OBSERVED.

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
