# System Context derived view

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Derived view of registered topology
- Owner: Architecture owner
- Approver: Architecture owner
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2026-11-28
- Superseded by: none

<a id="purpose"></a>
## Purpose

Derived, non-authoritative navigation view over the canonical entity and relation registries.

<a id="product-boundary"></a>
## Product boundary

Product ID product-feature-delivery-intelligence contains coordination System ID system-fdi-coordination through relation-product-contains-coordination.

<a id="users"></a>
## Users

Product owners, repository owners, agents, and independent verifiers interact through authenticated issue, Git, and pull-request surfaces.

<a id="systems"></a>
## Systems

Derived System ID system-fdi-coordination contains Component ID component-fdi-documentation through relation-coordination-contains-documentation.

<a id="external-systems"></a>
## External systems

GitHub and Multica are execution/evidence surfaces, not registered product topology entities in this documentation-only snapshot.

<a id="interactions"></a>
## Interactions

The documentation Component is implemented by Repository feature-delivery-intelligence through relation-documentation-implemented-by-repository.

<a id="rendered-registry-revision"></a>
## Rendered registry revision

catalog-v1 and relations-v1, rendered from released evidence revision 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482. Canonical truth remains in catalog.md#entities and relations.md#relations.

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
