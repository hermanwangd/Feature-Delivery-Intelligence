# Repository projection: feature-delivery-intelligence

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Repository entity feature-delivery-intelligence
- Owner: Repository owner
- Approver: Repository owner
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2026-11-28
- Superseded by: none

<a id="purpose"></a>
## Purpose

Derived navigation projection for the registered source and coordination repository.

<a id="repository-identity"></a>
## Repository identity

- Repository ID: feature-delivery-intelligence
- URI: https://github.com/hermanwangd/Feature-Delivery-Intelligence
- Pinned profile source revision: 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Lifecycle: ACTIVE

<a id="product-role"></a>
## Product role

Coordination repository and, for HERM-209 only, the single documentation source repository. This dual role does not collapse the authority boundary.

<a id="owned-entities"></a>
## Owned entities

Derived ID `component-fdi-documentation` from `.fdi/context/codebase/catalog.md#entities` (registry revision `catalog-v1`). The projection does not create or own an entity definition.

<a id="entry-points"></a>
## Entry points

- docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Planned candidate output: repository-root README.md

<a id="tests-and-checks"></a>
## Tests and checks

git diff --check; exact changed-path audit; Markdown schema/anchor/link validation; registry/Skill/topology/traceability audit.

<a id="local-instructions"></a>
## Local instructions

No repository-local instruction file exists at 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482. Authenticated workspace runtime instructions apply during execution but are not copied into repository Context.

<a id="interfaces"></a>
## Interfaces

No runtime API, schema, data store, or deployment interface exists in the pinned documentation-only repository.

<a id="known-gaps"></a>
## Known gaps

No released README contributor entry point exists at the starting revision; HERM-209 plans it as a source candidate.

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
