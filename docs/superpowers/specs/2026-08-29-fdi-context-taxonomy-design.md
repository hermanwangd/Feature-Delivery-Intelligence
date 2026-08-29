# FDI Context Taxonomy and Markdown Contract v0.1

**Status:** Approved coordination-repository profile contract (`Contract-ready: PASS`; `Execution-verified: NOT_CLAIMED`)

**Date:** 2026-08-29

**Scope:** A dedicated FDI coordination repository for one product, including products implemented across multiple source repositories.

## 1. Decision, semantic boundary, and conformance

FDI Workflow Semantics v0.1 is storage- and schema-neutral. It defines the four-artifact logical flow but does not prescribe a universal directory layout, Markdown schema, or repository topology:

```text
Human -> Intention -> Delivery Spec -> Change Set -> Verification & Validation Report
```

This document is the approved **coordination-repository profile contract** for teams that choose that operating model. It specializes the semantic baseline without redefining it. Every normative `MUST`, `MUST NOT`, and `REQUIRED` in this document applies only after a repository records the sole affirmative adoption state, `ADOPTED`, at `.fdi/README.md#adoption-state`. An absent profile or a draft outside the canonical `.fdi/` paths is not adopted and is not governed by this contract. Approval of this design does not claim that a physical profile or an execution exists. Paths, Markdown schemas, status vocabularies, authorization roles, anchors, and gates below are profile-local controls and MUST NOT be interpreted as universal requirements of FDI Workflow Semantics v0.1.

The profile uses a small mandatory core plus governed extensions. Stable core paths make workflow runs interoperable; bounded extensions avoid forcing irrelevant files on every product. The coordination repository owns durable product Context, cross-repository feature artifacts, baseline summaries, and safe evidence references. Source repositories retain authority for source, local instructions, tests, configuration, schemas, reviews, CI, branch protection, deployment, and release execution.

Baseline reconstruction is an as-is support workflow, not a fifth logical artifact or stage. Skills are executable procedural Context and declare the capabilities they use; capabilities are not a peer Context category.

## 2. Normative vocabulary and state

- **Required:** present for every conforming profile.
- **Conditional:** present only when its bounded matching rule is true; empty placeholders are prohibited.
- **Always-load:** read for every transition named by the contract.
- **Transition-load:** read only for a named transition after its scope selector matches.
- **Retrieval-only:** discovered through an index and read only after a bounded applicability match.
- **Ephemeral:** used during execution but not persisted as Context; only an authorized reference and interpretation may be recorded.
- **Current:** owner-authorized, within its review interval, resolvable at its cited revision, and unaffected by an unresolved refresh trigger.
- **Planned relation:** proposed by an authorized Delivery Spec but not yet verified in a released implementation. It MUST NOT be selected or represented as current Context.
- **Implemented candidate relation:** present at a pinned Change Set head but not yet released.
- **Current relation:** independently verified and observed in a released revision, then refreshed into Codebase.
- **Retired relation:** no longer present in the current released topology; retained only for traceability and excluded from default selection.
- **Superseded:** retained for traceability, excluded from default selection, and linked to a named successor.
- **Pinned source:** an immutable commit SHA, artifact digest, release identifier, or timestamped environment observation tied to a deployed revision.

## 3. Coordination-repository tree

```text
.fdi/
├── README.md
├── context/
│   ├── contract.md
│   ├── index.md
│   ├── steering/
│   │   ├── product.md
│   │   ├── tech.md
│   │   ├── structure.md
│   │   ├── architecture.md
│   │   ├── agent-policy.md
│   │   ├── delivery.md
│   │   ├── governance.md
│   │   └── extensions/{policy-id}.md
│   ├── codebase/
│   │   ├── catalog.md
│   │   ├── relations.md
│   │   ├── system-context.md
│   │   ├── integrations.md
│   │   ├── data.md
│   │   ├── repositories/{repo-id}.md
│   │   └── views/{view-id}.md
│   ├── domain/
│   │   ├── glossary.md
│   │   ├── rules.md
│   │   └── areas/{domain-id}.md
│   ├── knowledge/
│   │   ├── index.md
│   │   ├── decisions/{knowledge-id}.md
│   │   ├── incidents/{knowledge-id}.md
│   │   ├── learnings/{knowledge-id}.md
│   │   └── patterns/{knowledge-id}.md
│   ├── operations/
│   │   ├── environments.md
│   │   ├── release.md
│   │   ├── observability.md
│   │   └── runbooks/{runbook-id}.md
│   └── external/
│       ├── references.md
│       └── reviews/{source-id}.md
├── skills/
│   ├── catalog.md
│   ├── context-selection/SKILL.md
│   ├── human-to-intention/SKILL.md
│   ├── intention-to-spec/SKILL.md
│   ├── spec-to-implementation/SKILL.md
│   ├── implementation-to-correctness/SKILL.md
│   ├── baseline-discovery/SKILL.md
│   ├── baseline-verification/SKILL.md
│   ├── release-to-codebase-baseline-refresh/SKILL.md
│   └── {skill-id}/
│       ├── SKILL.md
│       ├── references/{reference-id}.md
│       ├── scripts/{script-id}.{sh,py,js,ts}
│       └── assets/{asset-id}.{json,yaml,yml,txt,png,svg}
├── baseline/
│   ├── snapshot.md
│   ├── catalog.md
│   └── capabilities/{capability-id}/
│       ├── capability.md
│       ├── implementation-map.md
│       └── verification.md
└── features/{feature-id}/
    ├── request.md
    ├── intention.md
    ├── spec/
    │   ├── index.md
    │   ├── requirements.md
    │   ├── design.md
    │   ├── tasks.md
    │   └── vv-plan.md
    ├── change-set/index.md
    ├── vv-report.md
    └── evidence/{evidence-id}.md
```

### 3.1 Bounded conditional patterns

All IDs except `{feature-id}` MUST match `[a-z0-9]+(?:-[a-z0-9]+)*`. `{feature-id}` is the exact case-preserving delivery key. IDs MUST NOT contain `/`, `..`, whitespace, URI schemes, or user-local paths.

| Pattern | Matching rule | Exclusions | Concrete-match record |
| --- | --- | --- | --- |
| `.fdi/context/steering/extensions/{policy-id}.md` | One authorized normative policy whose obligations do not fit a core steering file | Notes, plans, duplicate core policy | `.fdi/context/index.md#governed-extensions` and the consumer's `Context consulted` |
| `.fdi/context/codebase/repositories/{repo-id}.md` | Exactly one file for each active Repository entity in `catalog.md` | Source copies, generated trees, unregistered repositories | `catalog.md#entities` and the consumer's `Context consulted` |
| `.fdi/context/codebase/views/{view-id}.md` | A derived navigation view over IDs in `catalog.md` and current edges in `relations.md` | Independently maintained topology facts, planned edges presented as current | `.fdi/context/index.md#governed-extensions`; query and matched IDs in `Context consulted` |
| `.fdi/context/domain/areas/{domain-id}.md` | One bounded domain area with an owner listed in `glossary.md` | Implementation maps and feature-local requirements | Context index and consuming artifact |
| `.fdi/context/knowledge/{decisions,incidents,learnings,patterns}/{knowledge-id}.md` | One reviewed record admitted by `knowledge/index.md` | Feature copies, raw chat/Git history, unverified notes | `knowledge/index.md#active-catalog` and consuming artifact |
| `.fdi/context/operations/runbooks/{runbook-id}.md` | Authorized shared or cross-repository procedure | Secrets and repository-local procedures | Context index and consuming artifact |
| `.fdi/context/external/reviews/{source-id}.md` | Reviewed interpretation of one entry in `external/references.md` | Copied publications and uncited summaries | `external/references.md#source-catalog` and consuming artifact |
| `.fdi/skills/{skill-id}/SKILL.md` | Registered product-specific procedure; eight core IDs are reserved | Credentials, duplicate core procedures, vendored capability implementations | `.fdi/skills/catalog.md#skill-registry` and the gate record |
| `.fdi/skills/{skill-id}/references/{reference-id}.md` | Linked from the parent `SKILL.md` with an explicit load condition and satisfying section 9.1 | Unlinked notes and raw transcripts | Parent `SKILL.md#context-selection` and gate record |
| `.fdi/skills/{skill-id}/scripts/{script-id}.{sh,py,js,ts}` | Listed by the parent Skill with digest and invocation contract | Binaries, vendored dependencies, credentials | Parent `SKILL.md#capability-bindings` and gate record |
| `.fdi/skills/{skill-id}/assets/{asset-id}.{json,yaml,yml,txt,png,svg}` | Listed non-executable resource with digest and use condition | Executables, secrets, unlisted assets | Parent `SKILL.md#procedure` and gate record |
| `.fdi/baseline/capabilities/{capability-id}/{capability.md,implementation-map.md,verification.md}` | One staged bundle per catalog ID: `DISCOVERED`/`OWNER-CONFIRMED` requires `capability.md` plus `implementation-map.md`; `VERIFIED-AS-IS` requires all three at one bundle revision | Fabricated historical feature artifacts, a current `verification.md` for an unverified bundle revision, and extra bundle files | `.fdi/baseline/catalog.md#capability-registry` and consuming artifact |
| `.fdi/features/{feature-id}/{request.md,intention.md,vv-report.md}` | Three exact top-level members for the feature key in `request.md` | Aliases, scratch files, unrelated documents | `request.md#artifact-identity` and downstream identities |
| `.fdi/features/{feature-id}/spec/{index.md,requirements.md,design.md,tasks.md,vv-plan.md}` | Five exact Delivery Spec members | Extra spec members and generated drafts | `spec/index.md#bundle-membership` |
| `.fdi/features/{feature-id}/change-set/index.md` | One aggregate index referencing pinned source-repository candidates | Copied source and unpinned candidate descriptions | `change-set/index.md#repository-revisions-and-prs` |
| `.fdi/features/{feature-id}/evidence/{evidence-id}.md` | Safe evidence record allocated by `vv-plan.md` or a gate | Secrets, mutable unlabeled output, binary artifacts | `vv-plan.md#evidence-destinations` and `vv-report.md#evidence-inventory` |

No other path under `.fdi/` is trusted Context. A new pattern requires governance authorization and a revision to `.fdi/context/contract.md`.

A conditional Context payload is never trusted by path presence alone. In the same execution and before reading a leaf, the selector MUST literally read its governing registry: `.fdi/context/codebase/catalog.md` for repository projections; `.fdi/context/index.md` for Steering extensions, Codebase views, Domain areas, and runbooks; `.fdi/context/knowledge/index.md` for Knowledge; `.fdi/context/external/references.md` for external reviews; `.fdi/baseline/catalog.md` for Baseline bundles; and `.fdi/skills/catalog.md` plus the parent `SKILL.md` for Skill resources. Each registry entry records stable ID, path/digest, `ACTIVE` or `SUPERSEDED` lifecycle, `applies_to`, last/next review or expiry, `superseded_by`, owner, and trust/verification state. The producing gate records the registry revision, matched ID, lifecycle, applicability intersection, freshness, empty successor check, selected leaf/digest, and reason. A row that cannot make that registry read MUST NOT select the payload. Only `VERIFIED-AS-IS` Baseline claims may support a current-state conclusion; `DISCOVERED` and `OWNER-CONFIRMED` claims are selectable only as labeled hypotheses or gap inputs.

Every cross-file Markdown target MUST declare an explicit stable lowercase kebab-case ID, written immediately before its heading as `<a id="{stable-anchor}"></a>`. Every `path#fragment` reference uses that ID. Generated heading fragments are permitted only for headings that are not cross-file targets. Renaming a heading does not change its ID; retiring an ID leaves an anchor at the old target that links to its named successor.

### 3.2 Bounded source-repository selectors

Live reads use `repo:{repo-id}@{sha}:{path}`. `{repo-id}` MUST identify an active Repository entity in `catalog.md`; `{sha}` MUST be immutable; `{path}` MUST be one of:

1. an exact repository-local instruction path recorded in `repositories/{repo-id}.md#local-instructions`;
2. an exact source/test/config/schema/interface path recorded in the completed preceding artifact, an existing Baseline implementation map, or the authenticated B1 invocation named explicitly in row B1; or
3. a repository-relative glob recorded before its first use in `.fdi/features/{feature-id}/spec/index.md#preflight-source-scope` for transition 2 or `.fdi/baseline/snapshot.md#preflight-source-scope` for B1, with its repository ID, pinned SHA, root prefix, allowed extensions, maximum match count, and exclusions.

Transition 2 and B1 use a bounded draft/select/revise sequence inside one agent execution: (a) read only their literal inputs; (b) write the preflight selector section named above; (c) pass a syntax/authority gate for repository ID, immutable SHA, root, glob, extensions, exclusions, and declared maximum before repository access; (d) enumerate only candidate path names at that SHA without reading file content; (e) pass a cardinality gate, where zero or more than the declared maximum blocks; (f) read content only for the passed pinned matches; and (g) revise the bundle and record the final surface in `spec/design.md#change-surface` or `baseline/snapshot.md#source-scope`. Those final sections are outputs, never selectors for the reads that produce them. Directory-wide reads, mutable branch-only reads, dependency caches, build outputs, vendored trees, secrets, and paths outside the registered repository are excluded. Every concrete match is recorded as `repo-id:path@sha` in the producing artifact's `Context consulted`.

## 4. Common schemas and canonical topology contracts

### 4.1 Curated Context schema `C`

Every Markdown file under `.fdi/context/`, plus `.fdi/README.md`, MUST contain `# Title`, `## Status`, `## Purpose`, its section 6 headings, `## Provenance`, and `## Freshness and supersession`. Status records state, scope, owners, approvers, version, review dates, and successor links. Provenance records exact paths/anchors or immutable identifiers, producer, revision/time, and validation method.

### 4.2 Workflow artifact schema `F`

Every feature artifact except an evidence record and the supporting `request.md` member MUST contain `# Title`, `## Artifact identity`, `## Inputs`, `## Context consulted`, its section 7 headings, `## Traceability`, `## Open gaps and deviations`, `## Review, validity, and supersession`, and `## Gate record`. `request.md` contains the common headings through `## Open gaps and deviations`, plus `## Capture validity and supersession` and `## Intention gate`, which links to the sole `.fdi/features/{feature-id}/intention.md#gate-record`; it never owns a second gate. Review/validity records owner authorization, current revision, review state/time, invalidation triggers, and predecessor/successor links. The gate records the producing agent, Skill version, bound capability identifiers, preflight status/evidence, execution-review state/verdict, and exact evidence paths. For a Change Set, every known deviation MUST be declared and linked to a proposed disposition before V&V. An unresolved declared deviation does not by itself make the Change Set incomplete; the V&V Report assigns its blocking classification and disposition, and `PASS` requires every blocking deviation resolved. Before real execution, execution review MUST remain `NOT_CLAIMED`.

### 4.3 Baseline schema `B`

Every baseline file MUST contain `# Title`, `## Baseline identity`, `## Source scope`, its section 8 headings, `## Evidence and provenance`, `## Confidence and gaps`, and `## Review and freshness`; `snapshot.md` also contains `## Preflight source scope`, `## Refresh handoff`, `## Refresh candidate gate`, `## Refresh verification`, `## Refresh verification gate`, and `## Gate record`. Bundle evidence status is `DISCOVERED`, `OWNER-CONFIRMED`, or `VERIFIED-AS-IS` and never asserts unavailable historical intent. Discovery creates only `capability.md` and `implementation-map.md`; `verification.md` becomes current only when an independent verifier writes it for the same bundle revision. A prior `verification.md` may remain as superseded evidence during refresh but is excluded from the candidate bundle until B3b replaces it and the catalog returns to `VERIFIED-AS-IS`.

### 4.4 `catalog.md`: canonical entity registry

`.fdi/context/codebase/catalog.md` is the sole canonical registry for current topology entities. Its `## Entities` table MUST contain:

- stable ID and entity type: `Product`, `Domain`, `System`, `Component`, `API`, `Resource`, or `Repository`;
- name, description, owners, lifecycle status, and product role;
- Repository mapping for implementation-bearing entities;
- exact source reference as `repo-id:path@sha`, authorized registry URI, or evidence anchor;
- last verification revision/date.

Stable IDs survive renames. Each repository adopting this profile identifies exactly one Product as its scope; the profile is not a catalog entity or topology relation. Domains group Systems by business purpose; Systems group Components, APIs, and Resources into a product function; Components are deployable or executable implementation units; APIs are provided contracts; Resources are runtime or data dependencies; Repositories are source-control authority boundaries. A Repository is not a Product or Component.

### 4.5 `relations.md`: canonical relationship registry

`.fdi/context/codebase/relations.md` is the sole canonical registry for topology edges. Each row MUST contain stable relation ID, source entity ID, relation type, target entity ID, owner, exact evidence, state, and last verification revision/date.

Allowed types are `contains`, `implemented-by`, `provides`, `consumes`, `depends-on`, `stores-in`, and `deployed-as`. Source and target types MUST satisfy the validation matrix in `relations.md#allowed-relationship-types`; invalid pairs fail preflight. `current` edges require released evidence; `planned` edges remain canonical only in the Delivery Spec and MUST NOT be written to or selected from Codebase; `retired` edges remain traceable but are excluded from current queries.

`catalog.md` and `relations.md` are canonical. `system-context.md`, `integrations.md`, `data.md`, repository files, Codebase views, baseline maps, and diagrams are derived views or evidence-backed projections and MUST cite the entity/relation IDs and registry revision they render. They MUST NOT create competing topology truth.

### 4.6 Knowledge item and index schema `K`

Knowledge is explanatory and retrieval-only. It becomes normative only when an authorized workflow promotes its obligations into the applicable Steering file or an authorized feature artifact.

Every Knowledge item and every `knowledge/index.md` entry MUST record: ID/type/title/status; `applies_to` stable Product, Domain, System, Component, API, Resource, Repository, and/or Feature IDs; exact `source_artifacts` paths with Markdown anchors; provenance/evidence; owner and review state; applicability and limitations; last/next review date; and supersession state/link. A feature artifact remains canonical under `.fdi/features/{feature-id}/` and MUST NOT be copied into Knowledge.

## 5. Category and authority contracts

| Category | Purpose and authority | Owner/producer | Load policy | Refresh/conflict behavior |
| --- | --- | --- | --- | --- |
| Steering | Desired product direction and durable normative constraints, including architecture policy | Product, architecture, security, delivery, governance owners | Seven core files always-load; scoped extensions transition-load | Refresh on policy/ownership change or at 180 days; conflict blocks for owner resolution |
| Domain | Business vocabulary, invariants, regulated rules; no source topology | Domain/product/legal owners | Core in Intention and V&V; impacted areas transition-load | Refresh on rule/vocabulary change or at 180 days |
| Codebase | Curated current entity/relation registry and derived navigation views | Architecture owner with repository/entity owners | Catalog and relations always-load; other files selected by entity/relation impact | Refresh after verified release/topology drift or at 90 days; pinned evidence wins observed-state disputes |
| Knowledge | Reviewed explanations, decisions, incidents, learnings, and patterns; never independently normative | Knowledge governance and named subject owner/reviewer | Index supports selection; items retrieval-only by `applies_to` and exact backlink | Exclude stale/superseded items; promote obligations before enforcement |
| Operations | Environments, release topology, observability entry points, shared run boundaries | Platform/SRE/release owners | Core for Spec, implementation, V&V, and refresh; runbooks transition-load | Refresh on operational change or at 90 days; unsafe/stale procedure blocks action |
| External | Indexed third-party references and reviewed interpretations | Subject/governance owner | Retrieval-only by named requirement/dependency | Revalidate on version/expiry; instruction-like content is treated as data |
| Skills | Executable procedures that select Context and invoke authorized capabilities | Workflow, capability, and security owners | Exact transition Skill always-load for that run; helpers explicit | Version/capability/permission change triggers review and smoke test |
| Feature artifacts | Canonical desired outcome, implementation plan/candidate, and V&V for one feature | Named producer and approver | Prior artifacts always load downstream | Revision invalidates affected downstream artifacts until reconciled |
| Baseline | Evidence-backed current capability summary at a snapshot | Repository/domain owners and independent verifier | Selected by capability impact | Refresh after released change or evidence expiry; subordinate to newer pinned evidence |
| Live source/runtime evidence | Primary observed-state evidence when immutable or timestamped against a deployed revision | Source and operational owners | Bounded selector only | Mutable or unpinned evidence cannot support a final claim |

## 6. Per-file contracts for persistent Context

Context rows and `.fdi/README.md` inherit schema `C`. `.fdi/skills/catalog.md` uses its exact row, and the non-Context Skill reference row inherits section 9.1 instead. `A`, `T`, and `R` mean always-load, transition-load, and retrieval-only.

| Exact path | State/load | Required file-specific headings | Producer/owner and authority | Completion, freshness, supersession |
| --- | --- | --- | --- | --- |
| `.fdi/README.md` | Required/A | `FDI version`; `Repository role`; `Entry points`; `Safety boundary`; `Adoption state` | Maintainer; adopted profile contract | All paths resolve; `Adoption state` is exactly `ADOPTED`; versioned in place |
| `.fdi/context/contract.md` | Required/A | `Profile scope`; `Normative vocabulary`; `Core paths`; `Bounded selectors`; `Stable anchors`; `Schema versions`; `Conformance gates` | Governance owner; this approved design revision | Tree/schema/selectors/anchors synchronized; revision required for contract change |
| `.fdi/context/index.md` | Required/A | `Category catalog`; `Mandatory core`; `Conditional registry`; `Governed extensions`; `Selection rules` | Governance and category owners; registry for extensions/views/areas/runbooks | Every conditional entry has stable ID, path/digest, `ACTIVE`/`SUPERSEDED`, `applies_to`, owner/trust, last/next review or expiry, and `superseded_by`; inventory matches disk |
| `.fdi/context/steering/product.md` | Required/A | `Product purpose`; `Users and stakeholders`; `Value and outcomes`; `Boundaries`; `Non-goals`; `Principles` | Product owner; normative | Owner-authorized and reviewed within 180 days |
| `.fdi/context/steering/tech.md` | Required/A | `Authorized platforms`; `Technology constraints`; `Dependency policy`; `Security and compliance`; `Exceptions` | Architecture/security owners; normative | Stack/policy current; exceptions expire or renew |
| `.fdi/context/steering/structure.md` | Required/A | `Coordination-repository organization`; `Source-repository organization and placement policy`; `Naming`; `Placement`; `Instruction precedence`; `Topology references` | Architecture/repository owners; normative organization/placement policy only | It MUST NOT maintain descriptive entity, repository, or edge inventories; any illustration cites canonical IDs, current relations, and the rendered `catalog.md`/`relations.md` revision |
| `.fdi/context/steering/architecture.md` | Required/A | `Principles`; `System boundaries`; `Quality attributes`; `Authorized patterns`; `Prohibited patterns`; `Interface and data constraints`; `Exceptions` | Architecture/data/security owners; normative | Authorized obligations current; descriptive claims link to Codebase IDs |
| `.fdi/context/steering/agent-policy.md` | Required/A | `Autonomy`; `Approvals`; `Sensitive data`; `Capability boundaries`; `Escalation`; `Prohibited actions` | Governance/security owner; normative | Current permission policy; staleness blocks privileged work |
| `.fdi/context/steering/delivery.md` | Required/A | `Workflow semantics`; `Transition gates`; `Evidence policy`; `Change and release`; `Re-entry` | Delivery/release owner; normative | Matches semantic baseline and local controls |
| `.fdi/context/steering/governance.md` | Required/A | `Ownership`; `Authority by dimension`; `Approval matrix`; `Review cadence`; `Conflict resolution`; `Extension admission`; `Deprecation` | Governance owner; normative | Active owners/cadences; governed exceptions only |
| `.fdi/context/steering/extensions/{policy-id}.md` | Conditional/T | `Policy`; `Applicability`; `Obligations`; `Exceptions`; `Authorization` | Named policy owner; normative in scope | Registered/authorized/reviewed within 180 days |
| `.fdi/context/codebase/catalog.md` | Required/A | `Entity model`; `Entities`; `ID lifecycle`; `Validation`; `Known gaps` | Architecture owner plus entity/repository owners; canonical current registry | Required fields in 4.4; released evidence; refresh within 90 days |
| `.fdi/context/codebase/relations.md` | Required/A | `Relationship model`; `Allowed relationship types`; `Relations`; `State semantics`; `Validation`; `Known gaps` | Architecture owner plus edge owners; canonical current registry | Required fields in 4.5; no planned-as-current edge; refresh within 90 days |
| `.fdi/context/codebase/system-context.md` | Required/T | `Product boundary`; `Users`; `Systems`; `External systems`; `Interactions`; `Rendered registry revision` | Architecture owner; derived view | Every node/edge cites current IDs; regenerate on registry change |
| `.fdi/context/codebase/integrations.md` | Required/T | `Integration inventory`; `Direction`; `Owners`; `Contract locations`; `Compatibility`; `Failure boundaries`; `Rendered registry revision` | Integration/repository owners; derived view | Each integration cites relation IDs and pinned contracts |
| `.fdi/context/codebase/data.md` | Required/T | `Data domains`; `Owners`; `Stores and schemas`; `Flows`; `Privacy and retention`; `Migration constraints`; `Rendered registry revision` | Data/security owners; derived view | IDs and live schema refs resolve; refresh on data relation change |
| `.fdi/context/codebase/repositories/{repo-id}.md` | Conditional/T | `Repository identity`; `Product role`; `Owned entities`; `Entry points`; `Tests and checks`; `Local instructions`; `Interfaces`; `Known gaps` | Repository owner; navigation projection | One per active Repository ID; refs resolve; review within 90 days |
| `.fdi/context/codebase/views/{view-id}.md` | Conditional/R | `Question`; `Registry query`; `Included IDs`; `Exclusions`; `Rendered registry revision`; `Verification query` | Named owner; derived view | Registered query reproducible; refresh on cited registry revision |
| `.fdi/context/domain/glossary.md` | Required/T | `Terms`; `Actors`; `State vocabulary`; `Alias-to-ID mapping` | Domain owner; definitional | Every normalized alias maps deterministically to current Domain/entity IDs or a recorded ambiguity; no conflicting active definitions; review within 180 days |
| `.fdi/context/domain/rules.md` | Required/T | `Invariants`; `Decision rules`; `Regulatory obligations`; `Exceptions`; `Validation implications` | Domain/legal/product owners; normative | Every rule scoped/sourced/effective; expired rules excluded |
| `.fdi/context/domain/areas/{domain-id}.md` | Conditional/R | `Scope`; `Concepts`; `Rules`; `Scenarios`; `Boundaries`; `Validation implications` | Domain-area owner | Registered/source-backed/reviewed within 180 days |
| `.fdi/context/knowledge/index.md` | Required/T | `Admission policy`; `Active catalog`; `Superseded catalog`; `Promotion process`; `Retrieval rules` | Knowledge governance owner; retrieval index | Every entry satisfies schema `K`; catalog matches files |
| `.fdi/context/knowledge/decisions/{knowledge-id}.md` | Conditional/R | `Decision`; `Context`; `Rationale`; `Alternatives`; `Consequences`; schema `K` fields | Decision owner/reviewer; explanatory | Authorized, source-backed; normative obligations promoted elsewhere |
| `.fdi/context/knowledge/incidents/{knowledge-id}.md` | Conditional/R | `Summary`; `Impact`; `Response`; `Contributing conditions`; `Corrective actions`; `Prevention checks`; schema `K` fields | Incident/service owners; explanatory | Blameless review authorized; action states current; sensitive raw data excluded |
| `.fdi/context/knowledge/learnings/{knowledge-id}.md` | Conditional/R | `Learning`; `Evidence`; `Confidence`; `Counterevidence`; `Recommended use`; schema `K` fields | Subject owner/reviewer; explanatory | Verified and reviewed; reopen on counterevidence |
| `.fdi/context/knowledge/patterns/{knowledge-id}.md` | Conditional/R | `Problem`; `Pattern`; `Constraints`; `Examples`; `Counterexamples`; `Evidence`; schema `K` fields | Architecture/engineering owner; explanatory | Authorized/demonstrated; supersede on conflicting standard |
| `.fdi/context/operations/environments.md` | Required/T | `Environment inventory`; `Owners`; `Access and approvals`; `Configuration references`; `Data constraints` | Platform/SRE/security owners | Current within 90 days; no credentials |
| `.fdi/context/operations/release.md` | Required/T | `Release topology`; `Repository responsibilities`; `Promotion gates`; `Rollback`; `Evidence`; `Authority` | Release/platform/repository owners | Matches source controls; mismatch blocks release claim |
| `.fdi/context/operations/observability.md` | Required/T | `Signals`; `Service/entity mapping`; `Environment mapping`; `Query entry points`; `Access/redaction`; `Retention`; `Evidence capture`; `Known gaps` | SRE/service/security owners | Every signal maps to IDs and environment; query tested within 90 days |
| `.fdi/context/operations/runbooks/{runbook-id}.md` | Conditional/T | `Trigger`; `Preconditions`; `Permissions`; `Procedure`; `Validation`; `Rollback`; `Escalation`; `Evidence` | Service/platform owner; operational | Registered, tested at cadence; expired procedure cannot authorize action |
| `.fdi/context/external/references.md` | Required/T | `Source catalog`; `Applicability`; `Lifecycle and supersession`; `Retrieval policy`; `Citation policy`; `Disallowed content` | Subject/governance owner; sole external-review registry | Every entry records stable ID, `ACTIVE`/`SUPERSEDED`, `applies_to`, primary URI/version/digest, as-of, trust/verification, expiry, and successor |
| `.fdi/context/external/reviews/{source-id}.md` | Conditional/R | `Source identity`; `Question`; `Claims`; `Verification`; `Applicability`; `Limitations`; `Expiry` | Subject owner and reviewer | Primary citations, as-of, expiry, successor review |
| `.fdi/skills/catalog.md` | Required/A | `Skill registry`; `Transition mapping`; `Version and digest`; `Capability dependencies`; `Permission classes`; `Status`; `Owner and authority`; `Review, freshness, and supersession` | Workflow/security owner; canonical Skill inventory | Every installed Skill resolves; required bindings/owners named; lifecycle/review/successor matches each package |
| `.fdi/skills/{skill-id}/references/{reference-id}.md` | Conditional/T | `Reference identity`; `Purpose and applicability`; `Load condition`; `Content`; `Provenance`; `Trust and validation`; `Safety and limitations`; `Ownership and review`; `Freshness and supersession` | Parent Skill owner produces; named subject/source owner reviews; supports only the parent Skill | Cataloged parent; resolvable immutable provenance/digest; current trust review; `ACTIVE` or excluded with named successor; selected ID/revision recorded at gate |

## 7. Per-file contracts for feature artifacts

`intention.md`, all five Spec members, `change-set/index.md`, and `vv-report.md` inherit schema `F`. The supporting `request.md` member uses the exception in section 4.2; evidence records use only their exact row below.

| Exact path | Required headings | Producer/owner and source | Complete/current and mappings |
| --- | --- | --- | --- |
| `.fdi/features/{feature-id}/request.md` | `Human signal`; `Requester`; `Capture authentication`; `Requested change`; `Constraints`; `Source references`; `Ambiguities`; `Capture validity and supersession`; `Intention gate` | Intention agent; authenticated human signal | Produced in the Human-to-Intention execution; exact feature ID/source; revocation/replacement and successor are explicit; maps request fragments to Intention criteria |
| `.fdi/features/{feature-id}/intention.md` | `Rationale`; `Stakeholders`; `Outcome`; `Use scenarios`; `Scope`; `Impacted entity candidates`; `Constraints`; `Non-goals`; `Success criteria`; `Authorization` | Intention agent; product owner | Same producer and gate as request capture; recognized glossary aliases map to current catalog IDs, planned-new IDs and repository candidates are explicit, ambiguities block; criteria testable/authorized; maps request -> criteria -> Spec anchors |
| `.fdi/features/{feature-id}/spec/index.md` | `Bundle membership`; `Intention mapping`; `Revision state`; `Authorizations`; `Preflight source scope`; `Change-surface summary` | Spec agent; product/architecture/repository owners | Five members consistent; preflight selector exists before live discovery; maps every criterion to requirements/design/tasks/V&V plan |
| `.fdi/features/{feature-id}/spec/requirements.md` | `Functional requirements`; `Quality requirements`; `Constraints`; `Acceptance mapping`; `Open questions` | Spec agent; product/domain owners | Stable requirement IDs and exact criterion backlinks |
| `.fdi/features/{feature-id}/spec/design.md` | `Current state`; `Proposed design`; `Impacted entity and relation IDs`; `Planned relations`; `Change surface`; `Interfaces`; `Data`; `Operations`; `Rollout/rollback`; `Risks` | Spec agent; architecture/repository/operations owners | Planned edges remain here; every repo path/glob bounded per 3.2 |
| `.fdi/features/{feature-id}/spec/tasks.md` | `Task registry`; `Dependencies`; `Repository ownership`; `Requirement/design mapping`; `Completion evidence` | Spec agent; repo owners | Every task owned and mapped to exact obligation/evidence destination |
| `.fdi/features/{feature-id}/spec/vv-plan.md` | `Verification matrix`; `Validation scenarios`; `Independence`; `Environments`; `Capability bindings`; `Evidence destinations`; `Decision rules` | Spec agent; independent verifier/approvers | Every criterion/obligation has method, owner, destination, threshold |
| `.fdi/features/{feature-id}/change-set/index.md` | `Candidate identity`; `Repository revisions and PRs`; `Changed paths`; `Implemented relation candidates`; `Checks performed`; `Requirement/design/task mapping`; `Deviations`; `Deviation dispositions`; `Release state` | Implementation agents/repo owners; pinned commits/PRs | Every impacted repo has base/head and exact paths; candidate edges map planned relation IDs; every deviation ID links to a proposed disposition and proposed blocking state before V&V |
| `.fdi/features/{feature-id}/vv-report.md` | `Candidate assessed`; `Evidence inventory`; `Verification results`; `Validation results`; `Relation verification`; `Criterion verdicts`; `Overall verdict`; `Re-entry`; `Release observation` | Independent V&V agent and approvers | Every claim maps to evidence; `PASS`, `FAIL`, or `INCONCLUSIVE`; verified edges named; pre-release `Release observation` is `NOT_OBSERVED` and specifies the later event fields/evidence B3a must receive, but B3a never rewrites this report |
| `.fdi/features/{feature-id}/evidence/{evidence-id}.md` | `Evidence identity`; `Claim`; `Method`; `Candidate/environment`; `Observation`; `Result`; `Integrity and access`; `Producer and owner`; `Limitations`; `Validity, expiry, and supersession` | Allocated producer and named evidence owner; authority remains at cited origin | Immutable/timestamped reference and digest; exact plan/report backlinks; `VALID`, `EXPIRED`, `INVALIDATED`, or `SUPERSEDED` with review/expiry and successor; unsafe payload excluded |

Downstream placeholders MUST NOT be created before their producing transition starts. Revised upstream artifacts supersede and invalidate affected downstream revisions until re-entry completes.

## 8. Per-file contracts for baseline artifacts

Rows inherit schema `B`.

| Exact path | Required headings | Producer/owner | Complete/current |
| --- | --- | --- | --- |
| `.fdi/baseline/snapshot.md` | `Snapshot scope`; `Preflight source scope`; `Repository pins`; `Environment observations`; `Capability summary`; `Exclusions`; `Refresh handoff`; `Refresh candidate gate`; `Refresh verification`; `Refresh verification gate`; `Gate record` | Discovery/refresh agent; repository/operations owners; independent verifier owns only refresh verification and its gate | All scoped repos pinned; evidence dates/deployed revisions known; refresh candidate and verifier decisions remain distinguishable |
| `.fdi/baseline/catalog.md` | `Capability registry`; `Selection lifecycle`; `Entity/relation mappings`; `Status/confidence`; `Bundle paths`; `Review state` | Discovery/verifier; product/domain owners; sole Baseline-capability registry | Every ID has `ACTIVE`/`SUPERSEDED`, `applies_to`, freshness/expiry, successor, current registry links, and a staged bundle matching its evidence status; selection lifecycle and evidence status remain separate fields |
| `.fdi/baseline/capabilities/{capability-id}/capability.md` | `Observed behavior`; `Actors`; `Scenarios`; `Inputs/outputs`; `Rules`; `Limits` | Discovery agent; domain/product owner | Describes evidence only; unknown historical intent labeled unknown |
| `.fdi/baseline/capabilities/{capability-id}/implementation-map.md` | `Entity/relation IDs`; `Repository pins`; `Source anchors`; `Interfaces`; `Data`; `Runtime`; `Tests`; `Known gaps` | Discovery agent; repository owners | Exact `repo-id:path@sha` refs; registry revision recorded |
| `.fdi/baseline/capabilities/{capability-id}/verification.md` | `Claims`; `Methods`; `Independent evidence`; `Results`; `Owner confirmations`; `Verdict` | Independent verifier | Only supported items become `VERIFIED-AS-IS` |

## 9. Skill package contract

Every `.fdi/skills/*/SKILL.md` MUST have front matter fields `name`, `description`, `version`, `source`, compatible runtime range, `owner`, `authority`, lifecycle `status` (`ACTIVE` or `SUPERSEDED`), `last_reviewed`, `next_review`, `supersedes`, and `superseded_by`, followed by:

1. `# Purpose and applicability`;
2. `## Transition contract` with exact artifact inputs/outputs;
3. `## Context selection` with literal reads, bounded selectors, exclusions, precedence, and record destination;
4. `## Capability bindings` with stable identifiers, required/optional state, provider/runtime assumptions, input/output schemas, and availability check;
5. `## Permissions and approvals` with allowed, prohibited, destructive, external-audience, and sensitive-data boundaries;
6. `## Procedure`;
7. `## Failure, escalation, and idempotency`;
8. `## Completion and evidence`;
9. `## Version and provenance`.

Skills contain procedure and bindings, never credentials or capability implementations. A missing required binding, permission, owner/authority, current review, `ACTIVE` lifecycle, version, or digest fails transition preflight; a superseded Skill is excluded and names its successor. `.fdi/skills/catalog.md` is the only Skill registry; resources are trusted only when listed by their parent Skill and catalog entry.

The eight core Skill IDs have these exact transition contracts. Every row that performs governed selection loads `.fdi/skills/context-selection/SKILL.md` in addition to its transition Skill.

| Skill path | Exact inputs | Exact outputs/use |
| --- | --- | --- |
| `.fdi/skills/context-selection/SKILL.md` | The transition's literal reads, registry revisions, and preceding-artifact IDs | Validated bounded-match set and exclusions recorded at the transition's stated destination; it never produces a canonical artifact |
| `.fdi/skills/human-to-intention/SKILL.md` | Authenticated Human signal and transition 1 Context | The single Intention bundle: `request.md`, `intention.md`, and allocated evidence, under one producer and gate |
| `.fdi/skills/intention-to-spec/SKILL.md` | Completed Intention bundle and transition 2 Context | Five-member Delivery Spec bundle and allocated evidence using the draft/select/revise sequence |
| `.fdi/skills/spec-to-implementation/SKILL.md` | Completed Delivery Spec bundle and transition 3 Context | Source-repository candidates, `change-set/index.md`, and allocated evidence |
| `.fdi/skills/implementation-to-correctness/SKILL.md` | Intention, Delivery Spec, exact Change Set, and transition 4 Context | Independent `vv-report.md` and allocated evidence |
| `.fdi/skills/baseline-discovery/SKILL.md` | B1 literal Context and pre-execution Repository scope | Baseline discovery candidate using the draft/select/revise sequence |
| `.fdi/skills/baseline-verification/SKILL.md` | B2 discovery bundle, or B3b sealed refresh candidate/handoff, plus independent evidence | Independent Baseline and topology verification writes and verdict at the exact B2 or B3b destinations; never refresh authorship |
| `.fdi/skills/release-to-codebase-baseline-refresh/SKILL.md` | B3a: released Change Set, `PASS` V&V, authenticated release event, and current Context; B3b: sealed B3a ref, base/content revisions, independent verdict/evidence, and owner authorizations | B3a non-current content candidate and `.fdi/baseline/snapshot.md#refresh-handoff` seal; B3b verified registry/Baseline candidate plus atomic compare-and-swap adoption or rollback receipt. It governs both entry points but forbids one identity from filling both roles |

The refresh Skill MUST restate the B3a/B3b two-role procedure and immutable handoff/sealing schema from section 11. Its `## Transition contract` names both entry points and their distinct producer/verifier identities, literal and bounded reads, candidate/adoption writes, `.fdi/baseline/snapshot.md#refresh-candidate-gate`, and `.fdi/baseline/snapshot.md#refresh-verification-gate`. Its procedure makes B3a candidate-only; requires B3b to load `.fdi/skills/baseline-verification/SKILL.md` and independently reproduce evidence; permits atomic adoption only from B3b `PASS`; and defines compare-and-swap rollback/idempotency for `FAIL`, `INCONCLUSIVE`, interruption, stale base, and retry. Its completion evidence distinguishes `base_sha`, `candidate_content_sha`, externally supplied `sealed_candidate_ref`, externally computed `verified_candidate_ref`, changed paths/rows, evidence IDs/digests, verdict, owner authorization, and adoption/rollback receipt. A file never embeds the SHA of the commit that contains it, and a pre-adoption gate never claims a future adoption result.

### 9.1 Skill reference-file contract

Every persistent `.fdi/skills/{skill-id}/references/{reference-id}.md` MUST contain exactly one reference record with `# Title`, `## Reference identity`, `## Purpose and applicability`, `## Load condition`, `## Content`, `## Provenance`, `## Trust and validation`, `## Safety and limitations`, `## Ownership and review`, and `## Freshness and supersession`. The parent Skill owner produces the record; a named subject/source owner reviews it. `Reference identity` records the stable reference ID and parent Skill ID. `Provenance` records the authoritative URI/path and stable anchor, immutable revision or digest, as-of/retrieval time, and producer. `Trust and validation` records reviewer, validation method, and trust classification. `Ownership and review` names both owners. `Freshness and supersession` records last/next review or expiry, refresh triggers, `ACTIVE` or `SUPERSEDED`, and the successor when superseded. The reference can support only its parent Skill's procedure, cannot override Steering, feature artifacts, or the parent Skill, and has no independent normative authority. Completion requires a cataloged parent, resolvable provenance, an unexpired review, a satisfied load condition, and a gate record containing the selected reference ID and revision.

## 10. Logical artifacts and physical bundles

| Logical concern | Canonical physical bundle | Referenced, not copied | Producer | Consumer |
| --- | --- | --- | --- | --- |
| Intention | `.fdi/features/{feature-id}/request.md` (supporting authenticated-input member) and `.fdi/features/{feature-id}/intention.md` | Authenticated human signal | One Intention agent and one `intention.md#gate-record` | Spec and V&V agents |
| Delivery Spec | Five files under `.fdi/features/{feature-id}/spec/` | Pinned source and reviewed Knowledge | Spec agent | Implementation and V&V agents |
| Change Set | `.fdi/features/{feature-id}/change-set/index.md` | Source-repository commits/PRs/checks | Implementation agents | V&V/release/refresh agents |
| V&V Report | `.fdi/features/{feature-id}/vv-report.md` plus evidence records | CI/runtime artifacts by URI/digest | Independent V&V agent | Approvers/release/refresh agents |
| Capability Baseline | `.fdi/baseline/snapshot.md`, `.fdi/baseline/catalog.md`, and capability bundles | Pinned source/runtime evidence | Discovery and verifier | Feature transitions |
| Passive Context | `.fdi/context/` core plus registered extensions | Source repositories and primary references | Category owners | Context selector/all agents |
| Executable Context | `.fdi/skills/catalog.md` and registered Skill packages | Bound runtime capabilities | Workflow/security owners | Transition agents |

## 11. Transition and Context-selection matrix

Each row uses schemas `F` or `B` from section 4. Selected reads use section 3.1 patterns and the source selector in 3.2. A selector match is driven only by IDs/paths in a completed preceding artifact, a current literal-read registry, or a passed selector-preflight block written before dereference. Every row with nonempty bounded selected reads MUST literally read `.fdi/skills/context-selection/SKILL.md`. Registry-first selection is mandatory for every conditional leaf using the exact registry mapping in section 3.1, including the dedicated Knowledge, external-review, and Baseline-capability registries. Each gate's selection proof records registry path/revision, entry ID, `ACTIVE` lifecycle, applicability intersection, empty `superseded_by`, freshness/expiry and trust state, selected leaf/digest, and selection reason. Every concrete read is written to the output's `Context consulted` or `Source scope`. Planned edges are read only from `.fdi/features/{feature-id}/spec/design.md#planned-relations` and cannot satisfy a current-topology query. Every cross-file fragment is the explicit stable lowercase ID required by section 3.1.

| Order / producer | Literal reads | Bounded selected reads, matching, exclusions, concrete-match destination | Exact writes, schema, preceding/following mapping | Gate/evidence destination, completion, preflight/execution state |
| --- | --- | --- | --- | --- |
| 1 Human -> Intention / Intention agent | Authenticated Human signal with immutable source ID; `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/knowledge/index.md`; `.fdi/context/external/references.md`; `.fdi/baseline/catalog.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/human-to-intention/SKILL.md` | Capability bundles registered for IDs safely extracted from the signal; domain areas matched through glossary aliases; Knowledge items whose active `applies_to` intersects named feature/entity IDs; external reviews named by an explicit dependency. Exclude inactive, inapplicable, expired, superseded, unrelated, unsafe, and source-internal records. Record selection proofs and exact matches in `.fdi/features/{feature-id}/intention.md#context-consulted` | The Intention agent captures safe identity/channel, source ID, received time, authentication method/assurance, digest/redaction, and fragment mapping in `.fdi/features/{feature-id}/request.md`, then writes `.fdi/features/{feature-id}/intention.md` using `F` and allocated `.fdi/features/{feature-id}/evidence/{evidence-id}.md` records using the section 7 evidence contract. Credentials and unsafe raw payloads are never persisted. These two files are one Intention artifact with one producer. Map every recognized glossary alias deterministically to current catalog IDs in `.fdi/features/{feature-id}/intention.md#context-consulted`; record planned-new IDs/repository candidates and any unresolved ambiguity. Map request fragments to criterion IDs; following mapping targets `.fdi/features/{feature-id}/spec/index.md#intention-mapping` | Sole gate: `.fdi/features/{feature-id}/intention.md#gate-record`; `.fdi/features/{feature-id}/request.md#intention-gate` backlinks to it. Complete when capture is reviewable, scope/non-goals/scenarios/criteria/authorization resolve, and every impacted entity/repository seed is identified or blocked as an explicit ambiguity. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until reviewed |
| 2 Intention -> Delivery Spec / Spec agent | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/codebase/system-context.md`; `.fdi/context/codebase/integrations.md`; `.fdi/context/codebase/data.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/context/operations/observability.md`; `.fdi/context/knowledge/index.md`; `.fdi/context/external/references.md`; `.fdi/baseline/catalog.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/intention-to-spec/SKILL.md`; `.fdi/features/{feature-id}/request.md`; `.fdi/features/{feature-id}/intention.md` | First select repository projections for stable entity IDs already present in `.fdi/features/{feature-id}/intention.md#scope` or `.fdi/features/{feature-id}/intention.md#context-consulted`, plus applicable domain areas, views, Baseline bundles, Knowledge, reviews, and runbooks through their literal registries. Then pass selector syntax/authority preflight, enumerate only matching path names at pinned base SHAs using `.fdi/features/{feature-id}/spec/index.md#preflight-source-scope`, pass its cardinality gate, and only then read matched file content. Exclude inactive/superseded records, planned-as-current edges, unrelated trees, mutable reads, and any match outside the passed selector. Record exact matches in each Spec member's `Context consulted` and `.fdi/features/{feature-id}/spec/index.md#change-surface-summary` | Draft `.fdi/features/{feature-id}/spec/index.md#preflight-source-scope` before live reads, with selector ID, derivation anchor, `repo-id@sha`, root, exact path/glob, extensions, maximum matches, exclusions, syntax/authority verdict, enumerated count, and cardinality verdict; after selection, revise and complete `.fdi/features/{feature-id}/spec/index.md`, `.fdi/features/{feature-id}/spec/requirements.md`, `.fdi/features/{feature-id}/spec/design.md`, `.fdi/features/{feature-id}/spec/tasks.md`, and `.fdi/features/{feature-id}/spec/vv-plan.md` using `F`, plus `.fdi/features/{feature-id}/evidence/{evidence-id}.md` records whose investigation IDs are allocated by `.fdi/features/{feature-id}/spec/index.md#gate-record` and whose planned-check IDs are finalized by `.fdi/features/{feature-id}/spec/vv-plan.md#evidence-destinations`. `.fdi/features/{feature-id}/spec/design.md#change-surface` confirms results and cannot authorize its own discovery. Map criterion IDs to requirement/design/task/V&V IDs; keep planned relation IDs only in `.fdi/features/{feature-id}/spec/design.md`; following mapping targets Change Set candidate relation IDs and paths | Gate: `.fdi/features/{feature-id}/spec/index.md#gate-record`; selector evidence: `.fdi/features/{feature-id}/spec/index.md#preflight-source-scope`; planned evidence: `.fdi/features/{feature-id}/spec/vv-plan.md#evidence-destinations`. Preflight `CONTRACT_READY` only after selector syntax/authority, bounded enumeration, cardinality, and bundle-contract checks pass; invalid authority blocks before repository access, while zero/excess matches block after enumeration and before file-content reads. Complete when every criterion and change surface is mapped, owner authorizations are named, and selectors are bounded. execution `NOT_CLAIMED` until produced/reviewed |
| 3 Delivery Spec -> Change Set / implementation agents | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/context/knowledge/index.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/spec-to-implementation/SKILL.md`; `.fdi/features/{feature-id}/intention.md`; `.fdi/features/{feature-id}/spec/index.md`; `.fdi/features/{feature-id}/spec/requirements.md`; `.fdi/features/{feature-id}/spec/design.md`; `.fdi/features/{feature-id}/spec/tasks.md`; `.fdi/features/{feature-id}/spec/vv-plan.md` | Repository projections for IDs in `.fdi/features/{feature-id}/spec/index.md#change-surface-summary`; recorded local instructions; exact planned source/test/config/schema/interface paths at pinned base SHAs; applicable Knowledge/runbooks whose IDs occur in tasks/design; capability bindings from `.fdi/skills/spec-to-implementation/SKILL.md#capability-bindings`. Exclude every repository/path outside the completed Spec. If implementation discovers one, stop before reading that path and re-enter Delivery Spec; only a completed revised Spec may authorize the later read. Record every permitted match/use in the Change Set index's `Context consulted` | Write commits/PRs in each named source repository, `.fdi/features/{feature-id}/change-set/index.md` using `F`, and `.fdi/features/{feature-id}/evidence/{evidence-id}.md` records only at IDs allocated by `.fdi/features/{feature-id}/spec/vv-plan.md#evidence-destinations`. After stopping, write any discovered out-of-scope path as a blocking gap and proposed disposition in `.fdi/features/{feature-id}/change-set/index.md#deviations`; that record never authorizes a read. Map every requirement/design/task ID to `repo-id:path@head-sha` or justified no-code outcome and every planned relation ID to a candidate relation ID. No Codebase registry write occurs here | Gate: `.fdi/features/{feature-id}/change-set/index.md#gate-record`. Complete when every impacted repository has base/head/PR, changed paths/checks, and candidate relations, and every known deviation is declared and linked to a proposed disposition with owner/status/blocking proposal. Unresolved declared deviations may proceed to V&V. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until candidates/evidence exist |
| 4 Change Set -> V&V Report / independent V&V agent | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/context/operations/observability.md`; `.fdi/context/knowledge/index.md`; `.fdi/context/external/references.md`; `.fdi/baseline/catalog.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/implementation-to-correctness/SKILL.md`; `.fdi/features/{feature-id}/intention.md`; `.fdi/features/{feature-id}/spec/index.md`; `.fdi/features/{feature-id}/spec/requirements.md`; `.fdi/features/{feature-id}/spec/design.md`; `.fdi/features/{feature-id}/spec/tasks.md`; `.fdi/features/{feature-id}/spec/vv-plan.md`; `.fdi/features/{feature-id}/change-set/index.md` | `.fdi/features/{feature-id}/evidence/{evidence-id}.md` IDs named by `.fdi/features/{feature-id}/spec/vv-plan.md#evidence-destinations` or the Change Set; exact changed paths plus impacted tests/config/schemas/interfaces at pinned head SHAs; Baseline bundles named by criterion mapping; applicable Knowledge/runbooks/reviews; capability bindings from `.fdi/skills/implementation-to-correctness/SKILL.md#capability-bindings`. Exclude unreproduced assertions and evidence for another candidate/environment. Record matches in `.fdi/features/{feature-id}/vv-report.md#context-consulted` and `.fdi/features/{feature-id}/vv-report.md#evidence-inventory` | Write new `.fdi/features/{feature-id}/evidence/{evidence-id}.md` records at plan-allocated IDs, or at exception IDs allocated and justified by `.fdi/features/{feature-id}/vv-report.md#gate-record`, and `.fdi/features/{feature-id}/vv-report.md` using `F`. Map every requirement/design/task/candidate relation/criterion and every inherited/new deviation to evidence, blocking classification, disposition, and verdict; following mapping names release/refresh eligibility or earliest re-entry artifact | Gate: `.fdi/features/{feature-id}/vv-report.md#gate-record`; evidence inventory in the same file. Complete with separate verification/validation, relation verdicts, overall `PASS`/`FAIL`/`INCONCLUSIVE`, owners, and re-entry. `PASS` requires every blocking deviation resolved; complete `FAIL`/`INCONCLUSIVE` reports may retain unresolved items with an explicit next step. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until independent assessment |
| B1 Pinned source -> Baseline Discovery / discovery agent | Authenticated B1 invocation naming in-scope active Repository IDs and immutable pins; `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/codebase/system-context.md`; `.fdi/context/codebase/integrations.md`; `.fdi/context/codebase/data.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/observability.md`; `.fdi/context/knowledge/index.md`; `.fdi/context/external/references.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/baseline-discovery/SKILL.md` | First select repository projections/local instructions and applicable Knowledge/reviews/registered extensions for invocation IDs. Then pass selector syntax/authority preflight, enumerate only matching path names at the invocation's SHAs using `.fdi/baseline/snapshot.md#preflight-source-scope`, pass its cardinality gate, and only then read matched source/test/config/schema/doc content, plus observations through named query entry points. Exclude fabricated intent, uncited history/chat, caches, secrets, mutable reads, and any match outside the passed selector. Record matches in final Baseline `Source scope` and provenance | Draft `.fdi/baseline/snapshot.md#preflight-source-scope` before live reads, with selector ID, invocation anchor, `repo-id@sha`, root, exact path/glob, extensions, maximum matches, exclusions, syntax/authority verdict, enumerated count, and cardinality verdict; after selection, revise and complete `.fdi/baseline/snapshot.md`, `.fdi/baseline/catalog.md`, and each discovered `.fdi/baseline/capabilities/{capability-id}/capability.md` and `.fdi/baseline/capabilities/{capability-id}/implementation-map.md` using `B`; set each new catalog entry's evidence status to `DISCOVERED` and do not create a current `verification.md`. Final `.fdi/baseline/snapshot.md#source-scope` confirms results and cannot authorize its own discovery. Map capability IDs to exact entity/relation IDs and source anchors; following mapping targets verification claims | Gate: `.fdi/baseline/snapshot.md#gate-record`; selector evidence: `.fdi/baseline/snapshot.md#preflight-source-scope`; planned evidence paths named there. Preflight `CONTRACT_READY` only after selector syntax/authority, bounded enumeration, cardinality, and Baseline-contract checks pass; invalid authority blocks before repository access, while zero/excess matches block after enumeration and before file-content reads. Complete when all scoped repositories are pinned and each capability has concrete refs/gaps. execution `NOT_CLAIMED` until discovery review |
| B2 Baseline -> Independent As-Is Verification / baseline verifier | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/observability.md`; `.fdi/baseline/snapshot.md`; `.fdi/baseline/catalog.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/baseline-verification/SKILL.md` | For selected `ACTIVE`, applicable, fresh, non-superseded Baseline catalog IDs, read exact `.fdi/baseline/capabilities/{capability-id}/capability.md` and `.fdi/baseline/capabilities/{capability-id}/implementation-map.md`; inspect/reproduce their exact source/test/config/schema/runtime refs at the same pins and capability bindings from `.fdi/skills/baseline-verification/SKILL.md#capability-bindings`. Exclude producer claims not independently inspected/reproduced. Record selection proof, matches, and results in each `.fdi/baseline/capabilities/{capability-id}/verification.md#evidence-and-provenance` | Write each selected `.fdi/baseline/capabilities/{capability-id}/verification.md`, update `.fdi/baseline/catalog.md`, and revise `.fdi/baseline/snapshot.md#gate-record` using `B`. Map every observed-behavior claim/source anchor to method/result/owner confirmation; set the catalog evidence status to `VERIFIED-AS-IS` only for a supported same-revision three-file bundle, otherwise retain the prior staged status and record the gap | Gate: `.fdi/baseline/snapshot.md#gate-record`; evidence in each verification file. Complete when repository owners confirm maps, product/domain owners confirm descriptions, and independent verdicts exist. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until evidence exists |
| B3a Released Change Set -> refresh candidate / refresh agent | Authenticated release event with environment, deployed revision, source/event ID, observed-at time, observation method, and digest; `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/codebase/system-context.md`; `.fdi/context/codebase/integrations.md`; `.fdi/context/codebase/data.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/context/operations/observability.md`; `.fdi/baseline/snapshot.md`; `.fdi/baseline/catalog.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/release-to-codebase-baseline-refresh/SKILL.md`; `.fdi/features/{feature-id}/spec/design.md`; `.fdi/features/{feature-id}/change-set/index.md`; `.fdi/features/{feature-id}/vv-report.md` | Released `repo-id:path@sha` entries from `.fdi/features/{feature-id}/change-set/index.md`, plus source/runtime evidence named by the authenticated release event; affected Baseline bundles selected through `.fdi/baseline/catalog.md`; current Codebase rows whose IDs equal verified candidates. Exclude unreleased heads, non-`PASS` reports, unresolved blocking deviations, unrelated IDs, and mutable evidence. Record selection proof and matches in candidate files' provenance and `.fdi/baseline/snapshot.md#refresh-handoff` | Write a non-current content candidate commit limited to verified IDs in `.fdi/context/codebase/catalog.md`, `.fdi/context/codebase/relations.md`, affected `.fdi/context/codebase/system-context.md`, `.fdi/context/codebase/integrations.md`, `.fdi/context/codebase/data.md`, `.fdi/context/codebase/repositories/{repo-id}.md`, `.fdi/context/codebase/views/{view-id}.md`, `.fdi/baseline/snapshot.md`, `.fdi/baseline/catalog.md`, `.fdi/baseline/capabilities/{capability-id}/capability.md`, and `.fdi/baseline/capabilities/{capability-id}/implementation-map.md`; set affected `.fdi/baseline/catalog.md` entries to candidate evidence status `DISCOVERED`, treating any older `.fdi/baseline/capabilities/{capability-id}/verification.md` as excluded prior-revision evidence; write producer evidence only to `.fdi/features/{feature-id}/evidence/{evidence-id}.md` IDs allocated by `.fdi/baseline/snapshot.md#refresh-candidate-gate`. In a later seal-only commit, `.fdi/baseline/snapshot.md#refresh-handoff` records feature/release IDs, deployed revision, `base_sha`, the preceding `candidate_content_sha`, changed paths/row IDs, proposed registry revision, content manifest/digests, evidence IDs/digests, and planned-relation -> candidate -> V&V-verified -> released-row lineage. The seal never embeds its own SHA; after committing it, B3a returns an externally computed `sealed_candidate_ref` as `coordination-repo@seal-sha`. No `.fdi/baseline/capabilities/{capability-id}/verification.md` or current Context is written | Gate: seal `.fdi/baseline/snapshot.md#refresh-candidate-gate`; it cites the `PASS` V&V revision, authenticated release event, producer evidence, `base_sha`, and `candidate_content_sha`, but never its containing seal SHA. Complete when the candidate is internally consistent, owner authorization is recorded, every handoff field resolves, and the external `sealed_candidate_ref` is returned. The candidate is explicitly non-current until B3b `PASS`. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until a real refresh candidate exists |
| B3b Refresh candidate -> independent verification and atomic adoption / independent refresh verifier | Authenticated `sealed_candidate_ref`; base and `candidate_content_sha` revisions of every path named in `.fdi/baseline/snapshot.md#refresh-handoff`; `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/context/operations/observability.md`; base and candidate `.fdi/context/codebase/catalog.md`, `.fdi/context/codebase/relations.md`, `.fdi/baseline/snapshot.md`, and `.fdi/baseline/catalog.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/release-to-codebase-baseline-refresh/SKILL.md`; `.fdi/skills/baseline-verification/SKILL.md`; `.fdi/features/{feature-id}/spec/design.md`; `.fdi/features/{feature-id}/change-set/index.md`; `.fdi/features/{feature-id}/vv-report.md` | Independently reproduce release observation; inspect every released source/runtime evidence ref, changed entity/relation row, derived-view query, and affected Baseline claim named by the immutable handoff; select Baseline bundles only through the candidate catalog. Exclude producer-only assertions, paths/IDs outside the handoff, and mutable evidence. Record selection proof and results in affected `.fdi/baseline/capabilities/{capability-id}/verification.md#evidence-and-provenance` and `.fdi/baseline/snapshot.md#refresh-verification` | Write independent evidence only to `.fdi/features/{feature-id}/evidence/{evidence-id}.md` IDs allocated by `.fdi/baseline/snapshot.md#refresh-candidate-gate`; replace affected `.fdi/baseline/capabilities/{capability-id}/verification.md` for the candidate bundle revision; update `.fdi/baseline/catalog.md` to `VERIFIED-AS-IS` only for supported bundles; update `.fdi/context/codebase/catalog.md` and `.fdi/context/codebase/relations.md` with B3b evidence, verification date, and candidate current-state rows; regenerate affected `.fdi/context/codebase/system-context.md`, `.fdi/context/codebase/integrations.md`, `.fdi/context/codebase/data.md`, `.fdi/context/codebase/repositories/{repo-id}.md`, and `.fdi/context/codebase/views/{view-id}.md` when their rendered registry revision changes; and write candidate `.fdi/baseline/snapshot.md#refresh-verification` plus `.fdi/baseline/snapshot.md#refresh-verification-gate`. Only a `PASS` with required owner authorization may seal the resulting verified content commit as an externally computed `verified_candidate_ref` and atomically compare-and-swap the adopted Context ref from the expected base to it. `FAIL`/`INCONCLUSIVE` leaves the prior current revision unchanged and returns the handoff to B3a. No logical feature artifact or fifth stage is created | Gate: verified-content `.fdi/baseline/snapshot.md#refresh-verification-gate`; it records distinct producer/verifier identities, independence declaration, `base_sha`, `candidate_content_sha`, `sealed_candidate_ref`, reproduced evidence, verdict, expected current ref, and planned receipt destination. It never embeds its containing commit's future `verified_candidate_ref` or claims a future adoption result; after the gate commit, the repository provider returns the exact verified ref and authenticated compare-and-swap adoption/rollback receipt as external evidence. Complete when every handoff path/row/claim has an independent result and the provider returns either a successful compare-and-swap adoption receipt or an explicit non-adoption/rollback receipt; a `PASS` verdict without the receipt is verified but not adopted. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until a real independent refresh verification |

## 12. Topology refresh and Knowledge promotion lifecycle

```text
Delivery Spec planned relation
  -> Change Set implemented candidate
  -> V&V verified relation
  -> observed release
  -> B3a pinned Codebase/Baseline refresh candidate
  -> B3b independent verification
  -> atomic adoption as current Context only on PASS
  -> eligible for future separately contracted Knowledge promotion
```

Codebase is refreshed only after a `PASS` V&V Report and independently observed release. B3a authors a non-current content commit and later handoff-seal commit; the seal records the content SHA and is itself named only by the externally computed `sealed_candidate_ref`. B3b uses a distinct verifier to reproduce its evidence, writes a verified content commit without self-embedding its SHA, and then receives an external `verified_candidate_ref`. Entity/relation owners authorize their rows, every write cites the released SHA plus V&V evidence anchor, and derived views are regenerated from the same proposed registry revision. Only B3b `PASS` may atomically compare-and-swap the adopted Context ref to that verified ref; failure or a stale expected base leaves the prior current revision unchanged and returns a receipt.

After B3b `PASS`, a durable conclusion is only eligible for a future, separately contracted Knowledge-maintenance execution. This profile version does not define or authorize that execution and B3a/B3b perform no Knowledge writes. A future contract must name its exact Skill, producer, registry-first reads, writes, evidence destination, gate, and reviewer/state/backlinks. Such maintenance would be non-blocking, would not alter the B3 verdict, and would be neither a feature artifact nor a fifth workflow stage. Any promoted obligations would have no normative force until copied as obligations—not as the feature artifact itself—into Steering or an authorized future/current feature artifact.

## 13. Authority and conflict rules

### 13.1 Desired behavior

1. Latest authorized Intention owns stakeholder outcome, scope, non-goals, scenarios, and success criteria.
2. Latest authorized Delivery Spec owns technical obligations but cannot change Intention.
3. Steering owns persistent product, architecture, security, delivery, and governance constraints; Domain rules own business invariants.
4. A conflict blocks until the relevant owners authorize a revision or governed exception.
5. Knowledge explains rationale and supports retrieval. It cannot establish desired behavior until obligations are promoted into Steering or an authorized feature artifact.

### 13.2 Current behavior

1. Pinned source/config/schema/tests plus their results are primary for a named revision.
2. Timestamped telemetry is primary for a named environment only when the deployed revision is identified.
3. `catalog.md` and `relations.md` are canonical curated topology at their released evidence revision; newer pinned evidence triggers refresh rather than silent overwrite.
4. Verified Baseline summarizes evidence at its snapshot and is subordinate to newer pinned evidence.
5. Derived Codebase views, Knowledge, history, and third-party references explain or navigate; they do not outrank pinned observed-state evidence.

Conflicts are reconciled by revision, environment, scope, and authority dimension. A genuine mismatch is recorded in the relevant gap section, assigned to its owner, and blocks dependent claims.

## 14. Multi-repository ownership boundaries

| Concern | Coordination-repository authority | Source-repository authority | Required handshake |
| --- | --- | --- | --- |
| Product intent and cross-repo scope | Canonical Intention and aggregate Spec | Feasibility/current-state evidence | Product authorization plus impacted repository-owner confirmation |
| Entity/relation topology | Canonical released catalog/relations rows | Implementation and contract evidence | Entity/edge owner authorizes row citing released source/V&V |
| Source/config/schema/tests | Pinned references and mappings only | Canonical content, local controls, CI | Spec names bounded paths; local review remains required |
| Change Set | Aggregate index across commits/PRs | Candidate commits/PRs | Every impacted repo has pinned base/head/status |
| Evidence | Safe records and aggregate interpretation | Raw CI/build/test artifacts where owned | URI/digest/revision/conditions preserved; secrets not copied |
| Release | Planned gates and observed release reference | Executes/authorizes release and rollback | Refresh waits for observed release |
| Context upkeep | Product/category owners maintain shared Context | Repo owners maintain local instructions and truth | Drift triggers owner-confirmed refresh |

## 15. Failure and staleness handling

- Missing core/schema/path: preflight fails `NOT_CONTRACT_READY`.
- Zero/excess selector matches: record a Context gap and stop.
- Stale curated file: verify against its authority and refresh with owner authorization, or block.
- Planned edge selected as current: fail preflight and repair the selector/output.
- Missing Skill/capability/version/permission: fail before execution and name the missing binding.
- Unsafe evidence: retain only authorized URI/digest/redacted observation and classification.
- Upstream artifact revision: supersede affected downstream revisions and re-enter the earliest invalid transition.

## 16. Preflight review of this design

### 16.1 Mandatory contract preflight

| Check | Result | Exact evidence anchor |
| --- | --- | --- |
| Semantic baseline remains storage/schema neutral and all concrete controls are profile-local | PASS | Section 1 and the companion semantic baseline's Purpose |
| Design status is `Approved`, repository adoption has the single affirmative value `ADOPTED`, and no future-approval boundary remains | PASS | Status line; sections 1 and 6 `.fdi/README.md` row |
| Tree and bounded patterns contain every mandatory/conditional path | PASS | Sections 3, 3.1, and 3.2 |
| Transition 2 and B1 use gated draft/select/revise preflight and never select from their unproduced final surface | PASS | Sections 3.2 and 11 rows 2/B1 |
| Every Knowledge, external-review, and Baseline-bundle selection reads its registry and proves active/applicable/non-superseded state | PASS | Section 3.1 registry-first rule and section 11 opening/rows |
| Authenticated request capture is a supporting member of the one-producer, one-gate Intention artifact | PASS | Sections 4.2, 7, 10, and 11 row 1 |
| B3a refresh and B3b independent verification have immutable handoff, distinct writes/evidence/gates, and atomic adoption only on `PASS` | PASS | Sections 8, 9, 11 B3a/B3b, and 12 |
| Every governed-selection row loads `context-selection/SKILL.md`; refresh has an exact Skill contract | PASS | Sections 3, 9, and 11 all eight rows |
| Every persistent Markdown path has headings, producer/owner, authority/load, freshness, and supersession, including Skill references | PASS | Schemas in section 4; sections 6-9.1 |
| Canonical entity and relation contracts are singular; `structure.md` owns organization/placement policy only | PASS | Sections 4.4, 4.5, and 6 `structure.md` row |
| Change Set deviations link to proposed dispositions before V&V; only `PASS` requires all blockers resolved | PASS | Section 4.2; section 7 Change Set row; section 11 rows 3/4 |
| Every cross-file Markdown fragment is an explicit stable lowercase ID; generated anchors are never cross-file targets | PASS | Sections 3.1 and 11 opening rule; every path/anchor reference |
| Planned relations cannot be selected as current Context | PASS | Sections 2, 4.5, 11 opening rule, and 15 |
| Knowledge authority and fields are non-contradictory; post-B3b promotion is eligibility only, deferred to a future exact contract, and cannot add a fifth stage | PASS | Sections 4.6, 6 Knowledge rows, 12, and 13.1 |
| The four canonical artifact bundles and physical paths agree | PASS | Sections 3, 7, 8, and 10 |
| Rows 1-4, B1-B2, and B3a-B3b name producers, literal/selected reads, exact writes, mappings, gates, completion, evidence, and review state | PASS | Section 11, all eight rows |
| Desired/current authority and multi-repository ownership agree | PASS | Sections 13 and 14 |
| No disallowed category, repository registry, open-ended selector, bulk copy, secret, raw chat, or invented historical intent remains | PASS | Sections 1, 3.1, 3.2, 8, and 15 |

### 16.2 Gate result

- **Contract-ready:** `PASS`. Every mandatory preflight row above passed against its cited anchors; tree, schemas, bundle mapping, transition matrix, authority rules, ownership boundaries, and traceability lifecycle agree.
- **Execution-verified:** `NOT_CLAIMED`. No physical `.fdi/` profile, Skill package, baseline run, feature transition, release refresh, or evidence-producing execution was implemented or exercised by this design task.
- **Implementation boundary:** This approved design does not create a physical `.fdi/` profile, revise the installed workflow harness, or claim any evidence-producing execution; those remain separate implementation work.
