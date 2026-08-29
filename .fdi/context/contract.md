# FDI adopted-profile contract

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Feature Delivery Intelligence coordination profile
- Owner: FDI governance owner
- Approver: FDI governance owner
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Superseded by: none

<a id="purpose"></a>
## Purpose

Local conformance contract for the physical .fdi profile. The two approved design documents at the profile starting revision remain authoritative when this summary is incomplete.

<a id="profile-scope"></a>
## Profile scope

One Product may span multiple source repositories. The canonical logical flow is Human -> Intention -> Delivery Spec -> Change Set -> Verification & Validation Report. Context supports every execution; Baseline and release refresh are support workflows, not a fifth stage.

<a id="normative-vocabulary"></a>
## Normative vocabulary

- Required: present in every conforming profile.
- Conditional: present only after a bounded registry match; empty placeholders are prohibited.
- Current: owner-authorized, fresh, resolvable, ACTIVE, and not superseded.
- Pinned source: immutable commit, digest, release ID, or timestamped observation tied to a deployed revision.
- Planned relation: Delivery Spec proposal that is never selected as current Context.

<a id="core-paths"></a>
## Core paths

- .fdi/README.md
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
- .fdi/skills/catalog.md
- .fdi/skills/context-selection/SKILL.md
- .fdi/skills/human-to-intention/SKILL.md
- .fdi/skills/intention-to-spec/SKILL.md
- .fdi/skills/spec-to-implementation/SKILL.md
- .fdi/skills/implementation-to-correctness/SKILL.md
- .fdi/skills/baseline-discovery/SKILL.md
- .fdi/skills/baseline-verification/SKILL.md
- .fdi/skills/release-to-codebase-baseline-refresh/SKILL.md

<a id="bounded-selectors"></a>
## Bounded selectors

| ID | Allowed template | Governing registry | Maximum/matching rule |
| --- | --- | --- | --- |
| steering-policy | .fdi/context/steering/extensions/{policy-id}.md | .fdi/context/index.md | 0 unless an authorized scoped policy is registered |
| codebase-repository | .fdi/context/codebase/repositories/{repo-id}.md | .fdi/context/codebase/catalog.md | one per ACTIVE Repository entity |
| codebase-view | .fdi/context/codebase/views/{view-id}.md | .fdi/context/index.md | 0 unless a derived query is registered |
| domain-area | .fdi/context/domain/areas/{domain-id}.md | .fdi/context/index.md | 0 unless a bounded area is registered |
| knowledge-item | .fdi/context/knowledge/{decisions,incidents,learnings,patterns}/{knowledge-id}.md | .fdi/context/knowledge/index.md | 0 unless an ACTIVE reviewed record matches |
| operations-runbook | .fdi/context/operations/runbooks/{runbook-id}.md | .fdi/context/index.md | 0 unless an authorized runbook matches |
| external-review | .fdi/context/external/reviews/{source-id}.md | .fdi/context/external/references.md | 0 unless an ACTIVE verified source matches |
| skill-package | .fdi/skills/{skill-id}/SKILL.md | .fdi/skills/catalog.md | eight core packages plus registered extensions |
| skill-reference | .fdi/skills/{skill-id}/references/{reference-id}.md | .fdi/skills/catalog.md and parent SKILL.md | 0 unless parent load condition and digest pass |
| skill-script | .fdi/skills/{skill-id}/scripts/{script-id}.{sh,py,js,ts} | .fdi/skills/catalog.md and parent SKILL.md | 0 unless invocation contract and digest pass |
| skill-asset | .fdi/skills/{skill-id}/assets/{asset-id}.{json,yaml,yml,txt,png,svg} | .fdi/skills/catalog.md and parent SKILL.md | 0 unless use condition and digest pass |
| baseline-bundle | .fdi/baseline/capabilities/{capability-id}/{capability.md,implementation-map.md,verification.md} | .fdi/baseline/catalog.md | 0 in this pilot |
| feature-evidence | .fdi/features/{feature-id}/evidence/{evidence-id}.md | .fdi/features/{feature-id}/spec/vv-plan.md or producing gate | finite IDs allocated by the feature |

All non-feature IDs match [a-z0-9]+(?:-[a-z0-9]+)*. Feature IDs are exact case-preserving keys. Every selector validates derivation, immutable revision, root, extension, exclusions, finite maximum, zero/excess behavior, lifecycle, applicability, freshness, trust, and successor before leaf access.

<a id="stable-anchors"></a>
## Stable anchors

Every cross-file target declares an explicit lowercase kebab-case HTML anchor immediately before its heading. Every path#fragment reference uses that ID. Generated heading fragments and section/row numbers are not authority references.

<a id="schema-versions"></a>
## Schema versions

- C-0.1: curated Context and .fdi/README.md.
- F-0.1: feature artifacts; request.md uses the single-gate exception.
- B-0.1: Baseline artifacts.
- E-0.1: ten-heading evidence records.
- S-0.1: versioned Skill packages and capability bindings.

<a id="conformance-gates"></a>
## Conformance gates

CONTRACT_READY requires exact paths, schemas, fixed reads, bounded non-circular selectors, registries, authority/trust/freshness, Skills/capabilities/permissions, mappings, completion rules, and evidence destinations. Execution verification additionally requires observed reads/writes, evidence, traceability, independence, and verdicts. Missing or conflicting controls produce NOT_CONTRACT_READY; no substitute is invented.

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
