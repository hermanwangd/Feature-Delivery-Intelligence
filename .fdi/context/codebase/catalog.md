# Canonical Codebase entity catalog

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Current released documentation topology at the profile starting revision
- Owner: Architecture owner with repository/entity owners
- Approver: Architecture owner with repository/entity owners
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2026-11-28
- Superseded by: none

<a id="purpose"></a>
## Purpose

Sole canonical registry for current topology entities and repository projections.

<a id="entity-model"></a>
## Entity model

Allowed types are Product, Domain, System, Component, API, Resource, and Repository. Stable IDs survive renames. Repository is an authority boundary, not a Product or Component.

<a id="entities"></a>
## Entities

| Stable ID | Type | Name | Description | Owners | Lifecycle | Product role | Repository mapping | Exact source reference | Projection path/digest | applies_to | Trust | Last verification | Next review | superseded_by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| product-feature-delivery-intelligence | Product | Feature Delivery Intelligence | AI-native correct feature-delivery capability | Product owner | ACTIVE | Profile scope | feature-delivery-intelligence | feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | none | product-feature-delivery-intelligence | reviewed pinned design | 2026-08-30@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | 2026-11-28 | none |
| system-fdi-coordination | System | FDI coordination system | Coordination boundary for Context and feature artifacts | Architecture owner | ACTIVE | Coordinates delivery | feature-delivery-intelligence | feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | none | product-feature-delivery-intelligence | reviewed pinned design | 2026-08-30@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | 2026-11-28 | none |
| component-fdi-documentation | Component | FDI documentation component | Documentation-only profile and design entry points | Repository owner | ACTIVE | Human/agent coordination documentation | feature-delivery-intelligence | feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | none | system-fdi-coordination | reviewed pinned Git content | 2026-08-30@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | 2026-11-28 | none |
| feature-delivery-intelligence | Repository | Feature-Delivery-Intelligence | GitHub authority boundary for coordination and pilot source | Repository owner | ACTIVE | Coordination and documentation source | feature-delivery-intelligence | https://github.com/hermanwangd/Feature-Delivery-Intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | .fdi/context/codebase/repositories/feature-delivery-intelligence.md@sha256:a72aec299a1517df6c08b6ff089aff9fe58f7f591ad3634e1246d3bc0de56af4 | product-feature-delivery-intelligence | owner-authenticated pinned Git | 2026-08-30@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | 2026-11-28 | none |

<a id="id-lifecycle"></a>
## ID lifecycle

IDs are immutable. Rename preserves ID. SUPERSEDED or retired rows remain traceable with a successor and are excluded from current selection.

<a id="validation"></a>
## Validation

Exactly one Product, one coordination System, one documentation Component, and Repository feature-delivery-intelligence are registered. Repository projection selection requires this catalog read, ACTIVE status, applicability, freshness, trust, empty successor, and digest match.

<a id="known-gaps"></a>
## Known gaps

No API, Resource, Domain, deployable runtime component, or additional Repository is evidenced at the starting revision.

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
