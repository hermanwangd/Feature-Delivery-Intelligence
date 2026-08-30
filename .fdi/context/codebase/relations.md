# Canonical Codebase relation registry

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Current released documentation topology at the profile starting revision
- Owner: Architecture owner with relation owners
- Approver: Architecture owner with relation owners
- Version: 0.1.0
- Registry revision: relations-v1
- Last reviewed: 2026-08-30
- Next review: 2026-11-28
- Superseded by: none

<a id="purpose"></a>
## Purpose

Sole canonical registry for evidence-backed current topology relations.

`relations-v1` is the stable, resolvable registry revision identity for this rendered relation set. Cross-file consumers cite `.fdi/context/codebase/relations.md#relations`; record `Registry revision: relations-v1` separately.

<a id="relationship-model"></a>
## Relationship model

Allowed relation types are contains, implemented-by, provides, consumes, depends-on, stores-in, and deployed-as. Only released evidence can create a current relation.

<a id="allowed-relationship-types"></a>
## Allowed relationship types

| Relation type | Allowed source -> target |
| --- | --- |
| contains | Product -> Domain/System; Domain -> System; System -> Component/API/Resource |
| implemented-by | Domain/System/Component/API -> Repository |
| provides | System/Component -> API |
| consumes | System/Component/API -> API/Resource |
| depends-on | System/Component/API -> System/Component/API/Resource |
| stores-in | System/Component -> Resource |
| deployed-as | Component -> Resource |

<a id="relations"></a>
## Relations

| Stable relation ID | Source ID | Type | Target ID | Owner | Exact evidence | State | Last verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| relation-product-contains-coordination | product-feature-delivery-intelligence | contains | system-fdi-coordination | Architecture owner | feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | current | 2026-08-30@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 |
| relation-coordination-contains-documentation | system-fdi-coordination | contains | component-fdi-documentation | Repository owner | feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | current | 2026-08-30@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 |
| relation-documentation-implemented-by-repository | component-fdi-documentation | implemented-by | feature-delivery-intelligence | Repository owner | feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | current | 2026-08-30@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 |

<a id="state-semantics"></a>
## State semantics

current means independently evidenced at a released revision; planned remains only in a Delivery Spec; retired remains traceable but excluded from current queries.

<a id="validation"></a>
## Validation

All endpoints exist in `.fdi/context/codebase/catalog.md#entities` (registry revision `catalog-v1`), type pairs are allowed, evidence is immutable, and no planned relation appears as current.

<a id="known-gaps"></a>
## Known gaps

No integration, data, deployment, API, or runtime dependency relation is evidenced.

<a id="provenance"></a>
## Provenance

- Profile starting revision: 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed profile candidate: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Authoritative inputs:
  - feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
  - feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Producer: HERM-209 profile bootstrap
- Registry revision: relations-v1
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
