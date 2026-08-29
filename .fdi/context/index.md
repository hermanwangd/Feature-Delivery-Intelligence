# FDI Context index

<a id="status"></a>
## Status

- State: CURRENT
- Scope: All adopted-profile Context categories
- Owner: FDI governance owner
- Approver: FDI governance owner
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2026-11-28
- Superseded by: none

<a id="purpose"></a>
## Purpose

Canonical category index and governing registry for Steering extensions, Codebase views, Domain areas, and Operations runbooks.

<a id="category-catalog"></a>
## Category catalog

| Category | Authority | Load policy |
| --- | --- | --- |
| Steering | Durable normative constraints | seven core files always load |
| Domain | Vocabulary and invariants | core on Intention and V&V |
| Codebase | Canonical current topology plus derived views | catalog/relations always; views by impact |
| Knowledge | Explanatory only | registry-first retrieval |
| Operations | Environment/release/observability boundaries | transition-specific |
| External | Reviewed third-party interpretation | registry-first retrieval |
| Skills | Executable Context governing capabilities | transition Skill plus context-selection |

<a id="mandatory-core"></a>
## Mandatory core

- .fdi/context/contract.md
- .fdi/context/index.md
- .fdi/context/steering/product.md
- .fdi/context/steering/tech.md
- .fdi/context/steering/structure.md
- .fdi/context/steering/architecture.md
- .fdi/context/steering/agent-policy.md
- .fdi/context/steering/delivery.md
- .fdi/context/steering/governance.md
- .fdi/context/codebase/catalog.md
- .fdi/context/codebase/relations.md
- .fdi/context/codebase/system-context.md
- .fdi/context/codebase/integrations.md
- .fdi/context/codebase/data.md
- .fdi/context/codebase/repositories/feature-delivery-intelligence.md
- .fdi/context/domain/glossary.md
- .fdi/context/domain/rules.md
- .fdi/context/knowledge/index.md
- .fdi/context/operations/environments.md
- .fdi/context/operations/release.md
- .fdi/context/operations/observability.md
- .fdi/context/external/references.md

<a id="conditional-registry"></a>
## Conditional registry

| Stable ID | Kind | Exact path/digest | Lifecycle | applies_to | Owner | Trust | Last review | Next review/expiry | superseded_by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

No Steering extension, Codebase view, Domain area, or runbook is registered for this pilot.

<a id="governed-extensions"></a>
## Governed extensions

No governed extension entry exists. Disk inventory must therefore contain no extension/view/area/runbook leaf.

<a id="selection-rules"></a>
## Selection rules

Read this registry literally before a governed extension. Require ACTIVE lifecycle, applies_to intersection, current review/expiry, empty superseded_by, owner, trust, exact path/digest, and a recorded reason. Exclude absent, inactive, stale, superseded, unsafe, mutable, unrelated, and planned-as-current material.

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
