# Integration derived view

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

Derived, non-authoritative view of current integration relations.

<a id="integration-inventory"></a>
## Integration inventory

None evidenced by current relation rows.

<a id="direction"></a>
## Direction

Not applicable.

<a id="owners"></a>
## Owners

Architecture and repository owners.

<a id="contract-locations"></a>
## Contract locations

No runtime integration contract exists.

<a id="compatibility"></a>
## Compatibility

Not applicable for the documentation-only snapshot.

<a id="failure-boundaries"></a>
## Failure boundaries

GitHub/Multica access failures block evidence operations but do not establish product topology.

<a id="rendered-registry-revision"></a>
## Rendered registry revision

`.fdi/context/codebase/catalog.md#entities` (registry revision `catalog-v1`) and `.fdi/context/codebase/relations.md#relations` (registry revision `relations-v1`); zero matching provides/consumes/depends-on integration rows.

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
