# FDI Layer 2 — Product Intelligence Asset Framework v0.1

> **Status:** APPROVED — Contract-ready  
> **Depends on:** FDI Layer 1 — Feature Transformation Specification v0.2 (`Contract-ready: APPROVED`)  
> **Primary actor:** Frontier Team; Agents may assist under governed maintenance contracts  
> **Scope:** Durable Product Assets that make Layer 1 agent execution more accurate, reusable, and product-aware  
> **Design only:** No crawler, graph engine, builder implementation, validator, repository mutation, or runtime execution claim  
> **Non-goal:** Turn every source into Markdown, build a complete enterprise knowledge graph, or move feature-specific execution state into Layer 2

---

## 0. Purpose

Layer 1 defines **how Agents deliver a feature**:

```text
Human Signal
    |
    v
FT-T1 Intention Skill
    |
    v
intention.md
    |
    v
FT-T2 Delivery Spec Skill
    |
    v
spec.md
    |
    v
FT-T3 Implementation Skill
    |
    v
implementation.md
    |
    v
FT-T4 Correctness Skill
    |
    v
correctness.md
```

Layer 2 defines **what durable Product Intelligence the Frontier Team maintains so those Skills can execute well**.

```text
Distributed Product Sources
        |
        v
Frontier-Team-Maintained Product Assets
        |
        | selectively resolved for one execution
        v
Execution Context
        |
        v
Layer 1 f_skill
```

The central distinction is:

> **Product Asset is durable and product-scoped. Context is an execution-specific view of Product Assets and qualified direct references.**

Layer 2 therefore does not own Layer 1 feature artifacts. It owns reusable product intelligence that persists across many features.

---

# Contract P1 — Layer Boundary

## P1.1 Layer 1 responsibility

Layer 1 owns:

- feature-specific canonical flow;
- `intention.md`, `spec.md`, `implementation.md`, `correctness.md`;
- `f_skill` transformation contracts;
- feature-specific Change Surface findings;
- execution Context requirements and resolved Context provenance;
- feature lifecycle, gates, invalidation, re-entry, traceability, and correctness.

## P1.2 Layer 2 responsibility

Layer 2 owns:

- durable product/system knowledge needed repeatedly across features;
- governed product structure and navigation assets;
- product architecture and domain assets;
- reusable delivery-history intelligence;
- operations and governance knowledge needed by delivery agents;
- provenance, ownership, lifecycle, trust, and maintenance semantics for those assets.

## P1.3 Layer 2 MUST NOT

Layer 2 MUST NOT:

- become a fifth Layer 1 transition;
- own feature-specific Intention, Spec, Implementation, or Correctness authority;
- store feature-specific temporary reasoning as durable Product Intelligence by default;
- treat an inferred or historical relationship as current product truth without qualification;
- require a complete dependency graph before Layer 1 can execute;
- require every Product Asset to be copied into an FDI-owned Markdown file;
- allow an Agent-generated summary to gain organizational authority merely because it was materialized;
- silently mutate a Layer 1 artifact when a Product Asset changes.

---

# Contract P2 — Semantic Model

## P2.1 Core entities

| Entity | Meaning |
| --- | --- |
| **Source** | Existing system of record or evidence source: repositories, service catalogs, ADRs, Feature/Backlog systems, PRs, runbooks, standards, etc. |
| **Product Asset** | Durable, governed, reusable product intelligence maintained for repeated use across features. An Asset may be materialized content or a governed registration of an authoritative external source. |
| **Product Asset Descriptor** | The uniform governed metadata envelope that gives an Asset stable identity, scope, authority, provenance, lifecycle, trust, freshness, and selection metadata independent of storage form. |
| **Product Asset Ref** | Stable reference to one exact Product Asset semantic revision and its descriptor/content or referenced source. |
| **Execution Context** | The bounded execution-specific set of Product Asset Refs and qualified direct references selected to satisfy one Layer 1 Skill's `ContextRequirement`. |
| **EvidenceRef** | Claim-specific evidence used by Layer 1 to establish a finding or verdict; it is not the same as a Product Asset Ref. |
| **Asset Maintainer** | Frontier Team role, delegated product authority, or accountable maintenance role responsible for keeping an Asset semantically useful and appropriately current. |
| **Asset Maintenance Skill** | Governed procedure that may assist creation, extraction, reconciliation, validation, or refresh of a Product Asset. |

## P2.2 Fundamental relation

```text
Product Asset
  = Product Asset Descriptor
    + materialized content OR governed source reference

Execution Context
  = Select(
      Product Asset Refs,
      qualified bounded direct references,
      Layer 1 ContextRequirement
    )
```

Layer 1 may conceptually execute:

```text
OutputBundle = f(
    CanonicalInput(s),
    FT-Skill@revision
    ; ExecutionContext
)
```

Layer 1 does not need to know how an Asset was built or where its content is stored. It depends only on the resolved Asset/reference contract: identity, exact revision/as-of state, authority dimension, provenance, applicability, trust profile, freshness, and lifecycle eligibility.

# Contract P3 — Product Asset Descriptor and Content Contract

Every durable Product Asset MUST have a stable `ProductAssetDescriptor`, regardless of whether the Asset is Markdown, another materialized representation, or a governed reference to an existing authoritative artifact.

A materialized Asset MAY embed this descriptor as frontmatter. A `REFERENCED` Asset MAY keep the descriptor only in the Product Intelligence registry while its semantics remain in the referenced source.

A descriptor MUST expose metadata equivalent to:

```yaml
fdi_asset_version: "0.1"
asset_id: "<stable-id>"
asset_family: "PRODUCT|ARCHITECTURE|CODEBASE|DOMAIN|DELIVERY_HISTORY|OPERATIONS|KNOWLEDGE|REFERENCE"
asset_type: "<specific-type>"
asset_revision: <positive-integer>
content_ref: "<materialized-content-ref-or-governed-source-ref>"

publication_state: "DRAFT|PUBLISHED|RETIRED"
validity_state: "NOT_APPLICABLE|ACTIVE|STALE|SUPERSEDED"

owner: "<frontier-team-role-or-delegated-authority>"
maintenance_mode: "CURATED|DERIVED|REFERENCED"
publication_policy: "HUMAN_APPROVAL|RULE_BASED_AUTO|SOURCE_REFERENCE"

scope:
  products: []
  systems: []
  repositories: []
  environments: []

authority_dimensions: []
trust_profile:
  provenance: "DIRECT|DERIVED|ASSERTED"
  review: "UNREVIEWED|REVIEWED"
  verification: "NOT_VERIFIED|VERIFIED"
  authorization: "NONE|SOURCE_INHERITED|EXPLICIT"

as_of: "<time-or-source-state>"
source_refs: []
dependency_refs: []

freshness_policy:
  mode: "UNTIL_SUPERSEDED|SOURCE_CHANGE|TTL|EVENT_DRIVEN|MANUAL"
  ttl: null

supersedes: null
invalidation_triggers: []
selection_metadata:
  terms: []
  applicability: []
```

## P3.1 Asset revision versus source revision

`asset_revision` identifies the semantic revision of the Product Asset descriptor/content contract. Source versions are pinned independently in `source_refs`.

For a `REFERENCED` Asset, `asset_revision` versions the FDI registration/selection metadata; it does **not** replace the referenced source's own revision/version authority.

Once an Asset revision has been `PUBLISHED`, its semantic content and provenance bindings are immutable. A semantic change creates a new `asset_revision`. Lifecycle changes such as `ACTIVE -> STALE` or `ACTIVE -> SUPERSEDED` do not by themselves create a new semantic revision.

## P3.2 Required Asset semantics

Every durable Asset MUST make reviewable, either in its content or descriptor:

1. what reusable product knowledge it provides;
2. what it explicitly does not claim;
3. source/provenance references with source revision/as-of semantics;
4. dependencies on other Product Assets where materially derived from them;
5. authority dimensions;
6. trust profile;
7. scope and applicability;
8. current Asset revision and as-of semantics;
9. known limitations or incompleteness;
10. freshness policy, invalidation, and supersession rules;
11. ownership and maintenance responsibility;
12. selection metadata sufficient for bounded Layer 1 retrieval;
13. publication state and publication policy.

## P3.3 Authority and trust invariants

> **Asset existence does not create authority.**

Authority derives from the underlying source, organizational authorization, review path, derivation method, scope, and the claim being made.

Trust is **faceted, not a single global ranking**:

- `provenance` distinguishes direct, derived, and unsupported/asserted semantics;
- `review` records whether an accountable review occurred;
- `verification` records whether the represented claim was independently checked against its declared sources/evidence;
- `authorization` records whether an accountable authority adopted the Asset for an applicable authority dimension.

A selector MUST evaluate the facets required by the Layer 1 `ContextRequirement`. These facets do not form one global ranking; for example, `EXPLICIT` authorization and `VERIFIED` source checking answer different questions.

When Layer 2 produces Layer 1 `ResolvedContextRef.trust_state`, it MAY serialize or summarize this trust profile, but the underlying facets remain reviewable.

Examples:

- an approved architecture principle may have `DIRECT + REVIEWED + NOT_VERIFIED + EXPLICIT` and be authoritative for durable architecture constraints;
- a derived repository index may have `DERIVED + UNREVIEWED + VERIFIED + NONE` and be excellent navigation intelligence while still not proving feature-specific impact;
- a historical delivery record may be authoritative about what happened historically but not about what must change now.

## P3.4 Layer 2 authority dimensions

Layer 2 Product Assets MAY declare only support/constraint authority that is compatible with the approved Layer 1 model:

| Layer 2 authority ID | Layer 1 meaning |
| --- | --- |
| `DURABLE_CONSTRAINT` | Applicable governed organizational, architecture, domain, operations, or adopted reference constraint |
| `CURRENT_BEHAVIOR_SUPPORT` | Navigation/current-state support used to guide investigation; current feature truth still requires Layer 1 pinned `EvidenceRef` when material |
| `RATIONALE_SUPPORT` | Historical rationale, patterns, learnings, and supporting knowledge |

A Product Asset MUST NOT claim Layer 1 `DESIRED_OUTCOME`, `TECHNICAL_OBLIGATION`, or `PROCEDURE` authority. Those remain owned respectively by the active Intention, active Spec, and active governed Skill/capability contract.

Asset family does not determine authority automatically; each Asset declares the dimensions justified by its sources, scope, and publication path.

# Contract P4 — Asset Maintenance Modes

Layer 2 defines three durable Asset maintenance modes.

## P4.1 `CURATED`

Used when the Product Asset itself is maintained by an accountable Frontier Team or organizational authority.

Typical examples:

- product boundaries and capability definitions;
- architecture principles;
- approved domain rules;
- technology/governance constraints.

Conceptually:

```text
Authorized product/organization knowledge
        |
        | accountable curation/review
        v
Durable Product Asset
```

Agents MAY assist drafting or diff analysis, but MUST NOT manufacture organizational authority.

## P4.2 `DERIVED`

Used when a durable Product Asset is extracted, normalized, correlated, or summarized from governed sources.

```text
ProductAsset
=
f(
  SourceInputs,
  PA-Maintenance-Skill@revision
  ; SupportingAssetRefs
)
```

Typical examples:

- repository inventory;
- historical delivery records;
- known high-value codebase relations;
- normalized operations inventory.

Derived Assets MUST preserve source backlinks and their derived status.

## P4.3 `REFERENCED`

Used when an existing governed artifact is already the correct durable source and FDI only needs to register/index it.

Examples:

- canonical OpenAPI/protobuf contracts;
- approved ADRs;
- canonical runbooks;
- external standards;
- repository-local engineering instructions.

Layer 2 SHOULD store reference metadata rather than copying the content merely to conform to an FDI directory layout.

## P4.4 `RESOLVED` is not a Product Asset maintenance mode

`RESOLVED` belongs to **Layer 1 Context consumption**, not Layer 2 durable asset maintenance.

An execution may dynamically resolve current source evidence when no durable Asset is sufficient:

```text
Layer 1 ContextRequirement
        |
        v
Product Asset selection
        +
qualified bounded direct source lookup
        |
        v
Execution Context
```

The result may later motivate a new Product Asset, but it does not automatically become one.

---

# Contract P5 — Product Asset Families

Layer 2 recommends seven core Product Intelligence families plus an optional Reference family.

```text
Product Intelligence
├── Product
├── Architecture
├── Codebase
├── Domain
├── Delivery History
├── Operations
├── Knowledge
└── Reference
```

These are semantic families, not mandatory directories or exhaustive file bundles.

---

## P5.1 Product Assets

### Purpose

Describe the product from a persistent capability and boundary perspective.

### Typical reusable knowledge

- product/platform purpose;
- capabilities;
- product/system boundaries;
- users/actors;
- stable terminology;
- product-level constraints;
- ownership at product/system level.

### Typical upstream sources

- approved product/platform definitions;
- capability maps;
- organization/product ownership sources;
- approved product documentation.

### Typical maintenance mode

Primarily `CURATED`, optionally `REFERENCED`.

### Layer 1 consumers

Primarily T1 and T2; T4 where product-level intended-use interpretation matters.

### Example logical assets

```text
product/index.md
product/capabilities.md
product/boundaries.md
```

---

## P5.2 Architecture Assets

### Purpose

Capture durable architecture rules and system-level structure that repeatedly constrain feature delivery.

### Typical reusable knowledge

- architecture principles;
- system boundaries;
- interface conventions;
- approved technology choices;
- integration patterns;
- architecture invariants;
- cross-system ownership rules.

### Typical upstream sources

- approved ADRs;
- architecture principles;
- platform standards;
- architecture review decisions.

### Typical maintenance mode

`CURATED` and `REFERENCED`.

### Layer 1 consumers

T2 and T3 primarily; T4 when architecture constraints are explicit V&V obligations.

### Important authority rule

An Agent MAY infer an architectural observation from code, but it MUST NOT turn that observation into an architecture rule without the appropriate authority/review state.

---

## P5.3 Codebase Assets

### Purpose

Make the product's code estate navigable enough for bounded feature investigation.

### Recommended minimal Asset

```text
codebase/index.md
```

### Minimum useful content

For each known repository/system/component:

```yaml
repo:
  repo_id: "..."
  canonical_ref: "..."
  product_system: []
  owner_refs: []
  languages_platforms: []
  known_entrypoints: []
  known_contract_refs: []
  source_revision_or_as_of: "..."
```

### Typical upstream sources

- repository inventory;
- ownership/CODEOWNERS;
- service catalog;
- build/package manifests;
- deployment metadata;
- repository-local descriptors.

### Typical maintenance mode

Primarily `DERIVED`, optionally augmented with `CURATED` or `REFERENCED` metadata.

### Known Relation Assets

Layer 2 MAY maintain high-value relation indexes such as:

```text
repo-A --API--> repo-B
repo-C --CONSUMES_EVENT--> repo-D
repo-E --OWNS_SCHEMA--> contract-X
```

Every materialized relation MUST preserve:

```yaml
relation:
  relation_id: "..."
  from: "..."
  to: "..."
  relation_type: "API|EVENT|SCHEMA|PACKAGE|CONFIG|DEPLOYMENT|DATA|OTHER"
  source_refs: []
  as_of: "..."
  provenance_state: "DIRECT|DERIVED"
  review_state: "UNREVIEWED|REVIEWED"
  verification_state: "NOT_VERIFIED|VERIFIED"
  completeness: "PARTIAL|BOUNDED|UNKNOWN"
```

### Critical boundary

> **Codebase Asset relations are navigation intelligence, not a promise of a complete current dependency graph.**

They may generate Layer 1 T2 candidates. Feature-specific `CONFIRMED` Change Surface findings still require current applicable evidence under Layer 1.

### Layer 1 consumers

T1 for high-level orientation; primarily T2 and T3; T4 when source ownership or candidate coverage matters.

---

## P5.4 Domain Assets

### Purpose

Represent stable business/domain semantics that should not be rediscovered for every feature.

### Typical reusable knowledge

- vocabulary;
- business rules;
- invariants;
- regulated constraints;
- canonical domain models;
- business ownership.

### Typical upstream sources

- approved domain documentation;
- business policy;
- regulatory rules;
- canonical domain definitions;
- subject-matter authority decisions.

### Typical maintenance mode

`CURATED`, `REFERENCED`, or reviewed `DERIVED`.

### Trust boundary

A derived domain summary MUST remain `DERIVED` until the appropriate authority/review process gives it stronger status.

### Layer 1 consumers

T1/T2/T4 primarily; T3 where requirements map directly to domain invariants.

---

## P5.5 Delivery History Assets

### Purpose

Turn prior product delivery experience into reusable search and change-pattern intelligence.

### Primary upstream sources

```text
Historical Feature / Epic
+ Backlog / Issues
+ PRs
+ Commits
+ Review history
+ CI/Test
+ Release/deployment evidence when available
```

These sources are **upstream of the durable Delivery History Asset**, not Layer 1 canonical inputs.

### Typical maintenance mode

`DERIVED`.

### Conceptual production

```text
HistoricalDeliveryAsset
=
f(
  Historical Feature,
  Backlog,
  PRs,
  Commits,
  Reviews,
  Delivery Evidence,
  PA-Historical-Delivery@revision
)
```

### Recommended shape

```text
delivery-history/
├── index.md
└── records/{historical-feature-id}.md
```

### Minimum historical record

```yaml
historical_delivery:
  historical_feature_id: "..."
  feature_semantics:
    product_system: []
    capability_terms: []
    requirement_terms: []
  delivery:
    repos_touched: []
    paths_touched: []
    change_types: []
    interface_impacts: []
  source_refs:
    feature: []
    backlog: []
    prs: []
    commits: []
    reviews: []
  delivered_as_of: "..."
  trust_profile:
    provenance: "DERIVED"
    review: "UNREVIEWED|REVIEWED"
    verification: "NOT_VERIFIED|VERIFIED"
    authorization: "NONE"
```

### Authority

Delivery History Assets can establish or rank **historical delivery facts/patterns**.

They MAY help T2 generate candidates:

```text
similar historical feature
        -> historically touched repo
        -> T2 candidate
```

They MUST NOT by themselves establish:

```text
historically touched repo
        -> current CONFIRMED impacted repo
```

Current feature-specific applicability remains a Layer 1 responsibility.

### Layer 1 consumers

Primarily T2 candidate discovery and investigation prioritization.

---

## P5.6 Operations Assets

### Purpose

Represent persistent operational constraints that repeatedly affect delivery.

### Typical reusable knowledge

- environments;
- deployment/release controls;
- runtime topology where governed;
- observability conventions;
- SLO/SLA;
- rollback rules;
- operational ownership;
- data/runtime constraints.

### Typical upstream sources

- canonical runbooks;
- environment definitions;
- deployment systems;
- release policy;
- observability/platform standards.

### Typical maintenance mode

Primarily `REFERENCED` and `CURATED`; indexes may be `DERIVED`.

### Boundary

Runtime observations used to establish a feature-specific correctness claim remain Layer 1 `EvidenceRef`s. Durable Operations Assets describe reusable operating constraints; they are not a substitute for execution evidence.

### Layer 1 consumers

T2, T3, T4.

---

## P5.7 Knowledge Assets

### Purpose

Retain reusable engineering rationale and learnings that help future features without redefining current product truth.

### Typical reusable knowledge

- ADR rationale;
- incident learnings;
- retrospectives;
- known failure patterns;
- reviewed engineering patterns;
- lessons from historical delivery.

### Typical upstream sources

- ADRs;
- incidents/postmortems;
- retrospectives;
- reviewed engineering notes;
- qualified historical findings.

### Typical maintenance mode

`CURATED`, `REFERENCED`, or reviewed `DERIVED`.

### Trust profile

Knowledge MUST make provenance, review, verification, and authorization explicit using the common `trust_profile`; these dimensions MUST NOT be collapsed into one implied ranking.

Raw chat, transient scratchpads, and unreviewed agent memory do not automatically become Knowledge Assets. They may remain `ASSERTED + UNREVIEWED + NOT_VERIFIED + NONE` investigative inputs until a governed maintenance path creates a durable Asset revision.

### Scope control

Layer 2 v0.1 defines the Asset contract only. A full knowledge-promotion or organizational-memory workflow is optional future work and is not a prerequisite for initial FDI operation.

---

## P5.8 Reference Assets

### Purpose

Provide a governed registry for external or internal sources that are best referenced rather than duplicated.

Examples:

- external standards;
- vendor/API documentation;
- canonical repository-local instructions;
- external policies/reference material.

### Typical maintenance mode

`REFERENCED`.

### Required metadata

At minimum:

- exact reference;
- version/as-of date;
- applicability;
- authority/trust profile;
- owner/curator;
- expiry or update trigger where applicable.

---

# Contract P6 — Frontier Team Maintenance Model

Layer 2 exists to make Product Intelligence **maintainable by the Frontier Team**, not merely discoverable by an Agent.

## P6.1 Maintenance responsibility

Every durable Asset MUST have an accountable owner or maintenance role.

Ownership means responsibility for:

- semantic usefulness;
- scope correctness;
- source/provenance quality;
- trust profile;
- invalidation and supersession;
- deciding whether an Agent-proposed update should become durable product intelligence.

## P6.2 Agent-assisted maintenance

Agents MAY:

- detect changed sources;
- propose diffs;
- extract structured data;
- correlate Feature/Backlog/PR history;
- identify likely stale Assets;
- draft updates;
- validate backlinks;
- propose new high-value relation Assets.

Agents MUST NOT automatically grant stronger authority than their source/review path supports.

## P6.3 Publication boundary

Producing or editing an Asset revision is not the same as making it available to Layer 1.

Layer 2 separates:

```text
Asset authoring / derivation
        |
        v
DRAFT revision
        |
        | publication policy / review
        v
PUBLISHED revision
        |
        v
eligible for Layer 1 selection when validity_state = ACTIVE
```

A Product Asset MUST NOT satisfy a normal Layer 1 Context requirement unless:

```text
publication_state = PUBLISHED
AND
validity_state = ACTIVE
```

unless the Layer 1 requirement explicitly permits draft/asserted investigative material.

Publication policy is Asset-specific:

| Policy | Meaning | Typical use |
| --- | --- | --- |
| `HUMAN_APPROVAL` | An accountable Human/team must approve the Asset revision before publication | Product, Architecture, authoritative Domain/Governance assets |
| `RULE_BASED_AUTO` | A governed deterministic/derived maintenance process may publish when all declared quality gates pass and authority is not elevated | Repository inventory, some delivery-history/index assets |
| `SOURCE_REFERENCE` | Publication registers a governed reference to an existing authoritative source; the FDI Asset does not re-author its semantics | ADRs, runbooks, standards, canonical interface definitions |

An Agent-proposed change defaults to `DRAFT` unless its Asset contract explicitly allows `RULE_BASED_AUTO`.

`RULE_BASED_AUTO` is permitted only when the Asset contract has fail-closed quality gates, complete required provenance, and no semantic authority elevation. AI-assisted extraction MAY participate, but semantic policy interpretation, unresolved conflict, or organizational adoption that requires judgment MUST fall back to `HUMAN_APPROVAL`.

A derived or automatically published Asset MUST NOT gain stronger review, verification, or authorization claims than its sources, checks, and maintenance policy justify.

## P6.4 Product Asset publication gate

Before a revision becomes `PUBLISHED`, the maintenance contract MUST establish at least:

1. stable Asset identity and scope;
2. valid source/provenance backlinks;
3. authority dimension consistent with the sources and owner;
4. trust profile consistent with the provenance/review/verification/authorization path;
5. known limitations/incompleteness;
6. freshness/as-of semantics;
7. invalidation triggers;
8. selection metadata sufficient for bounded use;
9. dependency backlinks for materially upstream Product Assets;
10. no silent authority, review, verification, or authorization escalation;
11. no unresolved overlapping conflict with another `PUBLISHED + ACTIVE` Asset of the same authority/scope unless the conflict is explicitly represented for Layer 1 resolution;
12. valid supersession linkage when replacing an existing revision.

A failed publication gate leaves the candidate revision `DRAFT`; it does not alter the currently published revision.

## P6.5 Generic Frontier Team maintenance loop

Layer 2 has a durable maintenance loop separate from Layer 1 feature execution:

```text
Source change / Team decision / Repeated Layer 1 miss
        |
        v
Detect maintenance need
        |
        v
Human or PA-* Skill proposes Asset revision
        |
        v
DRAFT
        |
        v
Validate provenance / authority / scope / freshness
        |
        v
Publish according to Asset policy
        |
        v
PUBLISHED + ACTIVE
        |
        +--> supersede prior revision when applicable
        |
        +--> expose updated selection/index metadata
        `--> signal possible downstream dependency impact
```

This is a Product Asset maintenance loop, not a Layer 1 canonical transition and not a feature delivery gate.

## P6.6 Maintenance Skill namespace

Layer 2 MAY use Product Asset maintenance Skills, distinct from Layer 1 Feature Transformation Skills:

```text
FT-*  Feature Transformation Skills — execute Layer 1
PA-*  Product Asset Maintenance Skills — maintain Layer 2
```

A `PA-*` Skill MAY define:

```text
PA-Skill
├── identity / revision
├── Asset family/type
├── accepted source types
├── source selectors
├── transformation/reconciliation procedure
├── authority-preservation rules
├── allowed capabilities
├── output/update contract
├── trust-profile assignment rules
├── source backlink requirements
├── incompleteness rules
├── invalidation detection
└── prohibitions
```

`PA-*` Skills are not T0 and do not enter the Layer 1 canonical feature chain.

---

# Contract P7 — Asset Lifecycle

Layer 2 Assets have a durable lifecycle independent from Layer 1 feature lifecycle.

## P7.1 Publication state and validity state

Publication state and validity state are separate dimensions, but only the following combinations are legal:

| Publication state | Legal validity state | Meaning |
| --- | --- | --- |
| `DRAFT` | `NOT_APPLICABLE` | Candidate revision; not normally selectable |
| `PUBLISHED` | `ACTIVE` | Eligible for normal bounded Layer 1 selection |
| `PUBLISHED` | `STALE` | Retained for provenance; normally fails a fresh/current requirement |
| `PUBLISHED` | `SUPERSEDED` | Historical published revision replaced by a successor |
| `RETIRED` | `NOT_APPLICABLE` | Asset lineage intentionally withdrawn from active selection; successor not required |

Any other combination is invalid.

At most one revision of the same `asset_id` may be `PUBLISHED + ACTIVE` for the same declared scope partition. Publishing an active successor moves the prior active revision to `SUPERSEDED`.

`SUPERSEDED` means "replaced but retained". `RETIRED` means "withdrawn from active use" and does not imply a successor exists.

## P7.2 Published revision immutability

A `PUBLISHED` semantic revision is immutable. Content/provenance changes create a new `asset_revision`; publication and validity transitions are lifecycle metadata and do not rewrite historical semantic content.

A failed proposed revision never mutates the currently active published revision.

## P7.3 Freshness is Asset-specific

Layer 2 MUST NOT impose one universal TTL. Every Asset declares a `freshness_policy` appropriate to its semantics.

Examples:

- an architecture principle may use `UNTIL_SUPERSEDED`;
- a repository index may use `SOURCE_CHANGE`;
- a relation record may use `SOURCE_CHANGE` against its exact supporting sources;
- a closed historical delivery fact generally uses `MANUAL` or event-driven correction;
- an external standard may use `EVENT_DRIVEN`, `TTL`, or explicit supersession.

## P7.4 Invalidation triggers and dependencies

A durable Asset MUST declare the classes of source/dependency change that can invalidate it or require re-review.

```yaml
invalidation_triggers:
  - trigger_type: "SOURCE_CHANGED|DEPENDENCY_CHANGED|POLICY_SUPERSEDED|SCOPE_CHANGED|EXPIRY|MANUAL_REVIEW"
    source_scope: "..."
    effect: "WHOLE_ASSET|SCOPED_RECORD|RECHECK_REQUIRED"
```

`dependency_refs` provide the minimum dependency graph needed for maintenance. Layer 2 does not require a complete organization-wide graph.

An upstream source or Asset change does not silently rewrite dependent Assets. The maintenance policy marks or rechecks affected Assets according to their declared triggers.

## P7.5 Supersession and Layer 1 history

A newer Asset revision may supersede an earlier revision without deleting historical provenance.

Layer 1 artifacts that previously referenced the older Asset remain historical records. Layer 1 decides whether an active feature claim becomes `STALE` according to its own material dependency semantics; Layer 2 MUST NOT silently mutate Layer 1 lifecycle state.

# Contract P8 — Asset Selection into Execution Context

Layer 2 Product Assets become useful to Layer 1 only through bounded, progressive selection.

```text
Layer 1 ContextRequirement
        |
        v
Product Intelligence Index / Registry
        |
        v
Select bounded eligible Product Asset Refs
        |
        + optional bounded direct reference resolution
        |
        v
Execution Context
        |
        v
ResolvedContextRef(s)
```

## P8.1 ProductAssetRef

A selected durable Asset is represented to the resolver with metadata equivalent to:

```yaml
product_asset_ref:
  asset_id: "..."
  asset_revision: 12
  descriptor_ref: "..."
  content_ref: "..."
  publication_state: "PUBLISHED"
  validity_state: "ACTIVE"
  as_of: "..."
  authority_dimensions: []
  trust_profile: {}
  scope_match: "..."
```

The Layer 1 resolver maps the selected Asset/reference into its approved `ResolvedContextRef` contract. Layer 2 does not change Layer 1's canonical Context interface.

## P8.2 Selection eligibility

Normal selection MUST evaluate:

1. Asset family/type compatibility;
2. authority dimension;
3. scope/applicability;
4. required trust-profile facets;
5. revision/as-of/freshness;
6. publication/validity eligibility;
7. selector bounds;
8. known supersession/conflicts.

The default eligible state is:

```text
publication_state = PUBLISHED
AND validity_state = ACTIVE
```

A `DRAFT` Asset may be selected only when the Layer 1 requirement/selector explicitly permits unpublished or asserted investigative material. It MUST NOT satisfy a requirement that demands published/authorized Context.

## P8.3 Progressive resolution

Selection SHOULD return a bounded, low-redundancy initial set sufficient to begin the Skill's declared task. It MAY expand on demand under the same `ContextRequirement` and selector bounds as new findings require.

Layer 2 MUST NOT require exhaustive preloading or claim that a globally smallest sufficient set can always be known before execution.

Selection MUST NOT silently weaken a Layer 1 Context requirement.

## P8.4 Conflicts and outcomes

A selector MUST NOT silently choose a convenient Asset when materially applicable eligible Assets conflict. It returns the conflict and the relevant refs so Layer 1 can apply its approved conflict/gap semantics.

Possible resolution outcomes:

```text
RESOLVED
NOT_FOUND
STALE_ONLY
INSUFFICIENT_TRUST
CONFLICTING
NOT_APPLICABLE
```

The Layer 1 Skill then applies claim-local blocking, investigation, or gap semantics.

# Contract P9 — Product Intelligence Index

Layer 2 SHOULD expose a compact navigation registry. The recommended logical root is:

```text
fdi/product-intelligence/index.md
```

The index is a navigation and selection surface, not a product knowledge dump.

Example registry entry:

```yaml
assets:
  - asset_id: "codebase-index"
    asset_family: "CODEBASE"
    asset_type: "REPOSITORY_INDEX"
    ref: "..."
    asset_revision: 12
    scope:
      products: ["..."]
    authority_dimensions: ["CURRENT_BEHAVIOR_SUPPORT"]
    trust_profile:
      provenance: "DERIVED"
      review: "UNREVIEWED"
      verification: "VERIFIED"
      authorization: "NONE"
    publication_state: "PUBLISHED"
    validity_state: "ACTIVE"
    as_of: "..."
    selection_metadata:
      terms: []
      applicability: []
```

The index MAY be split by Asset family when scale requires it.

The index is a navigation/selection projection, not an independent authority for the underlying product claim. Index entries MUST backlink to their Asset descriptors. The index itself MAY be maintained as a derived Asset and may use `RULE_BASED_AUTO` when its registry integrity checks pass.

---

# Contract P10 — Product Intelligence vs Evidence

Layer 2 Product Assets and Layer 1 Evidence MUST remain distinct.

```text
Product Asset
= reusable product intelligence

EvidenceRef
= evidence establishing a specific feature claim
```

Examples:

### Codebase relation Asset

```text
"repo A commonly calls service B"
```

can help T2 investigate.

### T2 EvidenceRef

```text
repo-A@sha:path
+ repo-B@sha:contract
```

establishes that the relation is currently relevant to the feature-specific finding.

Likewise:

```text
Delivery History Asset
→ suggests repo-C

Current feature-specific EvidenceRef
→ CONFIRMS or EXCLUDES repo-C
```

This boundary prevents Product Intelligence from becoming stale hidden truth.

---

# Contract P11 — Recommended Product Intelligence Structure

The following logical structure is recommended, not mandatory as a fixed exhaustive bundle:

```text
fdi/product-intelligence/
├── index.md
│
├── product/
│   ├── index.md
│   ├── capabilities.md
│   └── boundaries.md
│
├── architecture/
│   ├── index.md
│   └── principles.md
│
├── codebase/
│   ├── index.md
│   ├── repos/
│   └── relations/
│
├── domain/
│   └── index.md
│
├── delivery-history/
│   ├── index.md
│   └── records/
│
├── operations/
│   └── index.md
│
├── knowledge/
│   └── index.md
│
└── references/
    └── index.md
```

Only useful Assets SHOULD be materialized. Empty placeholder files are not required.

---

# Contract P12 — Layer 1 Consumption Map

| Product Asset family | T1 Intention | T2 Delivery Spec | T3 Implementation | T4 Correctness |
| --- | --- | --- | --- | --- |
| Product | Primary | Primary | Occasional | Applicable validation |
| Architecture | Occasional | Primary | Primary | Applicable verification |
| Codebase | Orientation | **Primary** | **Primary** | Candidate/source coverage |
| Domain | Primary when applicable | Primary | Mapped constraints | **Primary validation when applicable** |
| Delivery History | Rare | **Candidate discovery / prioritization** | Rare | Rare |
| Operations | Rare | Primary when applicable | Primary | Primary when applicable |
| Knowledge | On demand | On demand | On demand | On demand |
| Reference | On demand | On demand | On demand | On demand |

This table is a default consumption profile, not a rule to preload every family.

---

# Contract P13 — Bootstrap Principle

Layer 2 MUST grow according to demonstrated Layer 1 reuse value.

It MUST NOT begin by building a complete enterprise graph or full organizational memory system.

Recommended bootstrap order:

```text
P0  Product / architecture curated core already available to the team
P0  Minimal Codebase Index
P0  Delivery History Assets from Feature + Backlog + PR/Commit
P1  High-value Codebase relation Assets discovered as repeated T2 needs
P1  Operations Assets required by pilot product
P1  Domain Assets required by pilot product
P2  Additional Product Intelligence driven by repeated Layer 1 misses
P3  Broader Knowledge lifecycle / promotion only when justified
```

The governing rule is:

> **Materialize an Asset when maintaining it once is cheaper and more reliable than repeatedly rediscovering the same product knowledge during Layer 1 execution.**

---

# Contract P14 — Layer 2 Success Criteria

Layer 2 is successful only if maintained Product Assets measurably improve Layer 1 delivery.

Recommended evaluation dimensions:

| Dimension | Example measure |
| --- | --- |
| Reuse | How often an Asset is materially reused across features |
| Discovery quality | Improvement in T2 candidate/critical repo recall |
| Context efficiency | Reduction in unnecessary repository/context loading |
| Freshness | Rate of materially stale Asset use |
| Human maintenance burden | Time required to keep high-value Assets useful |
| Agent correction rate | How often Agents require Human correction because Product Intelligence was missing/wrong |
| Traceability | % of materially used Assets with valid source/provenance backlinks |
| Asset ROI | Maintenance cost versus repeated investigation effort avoided |

Layer 2 SHOULD remove or demote Assets that are expensive to maintain and rarely improve Layer 1 outcomes.

---

# Contract P15 — Contract Review Invariants

Before Layer 2 can be implemented, the following invariants are normative:

1. **Descriptor is universal; storage is not.** Every Product Asset has a governed descriptor, but Asset content may be Markdown, another materialized representation, or a registered authoritative reference.
2. **Published semantic revisions are immutable.** Lifecycle state may change without rewriting historical Asset content.
3. **Trust is faceted.** Provenance, review, verification, and authorization are evaluated separately; no global trust ranking is implied.
4. **One active lineage.** One `asset_id` has at most one `PUBLISHED + ACTIVE` revision per scope partition.
5. **Derived intelligence does not create current feature truth.** Historical/indexed relations may guide discovery; Layer 1 current `EvidenceRef`s establish feature-specific findings.
6. **No silent publication.** Agent-generated semantic changes default to `DRAFT`; auto-publication is fail-closed and cannot elevate authority.
7. **No silent conflict resolution.** Materially conflicting eligible Assets are surfaced to Layer 1.
8. **No complete graph prerequisite.** Only useful dependency/backlink metadata is maintained; feature execution may resolve bounded current evidence directly.
9. **Layer 2 never mutates Layer 1 authority.** Asset updates may trigger re-evaluation signals, but Layer 1 owns feature validity/invalidation.
10. **Maintenance is ROI-driven.** Frontier Teams materialize and maintain Assets when reuse value exceeds repeated rediscovery cost.

# Layer 2 Design Review Checklist

Layer 2 v0.1 design approval is complete:

- [x] Layer 2 purpose: Frontier-Team-maintained durable Product Intelligence, not execution workflow
- [x] Product Asset vs Execution Context distinction
- [x] Source vs Product Asset vs Evidence boundary
- [x] Product Asset Descriptor/content contract and semantic revision rules
- [x] `CURATED`, `DERIVED`, `REFERENCED` maintenance modes
- [x] `RESOLVED` moved to Layer 1 Context consumption rather than durable Asset maintenance
- [x] Product / Architecture / Codebase / Domain / Delivery History / Operations / Knowledge / Reference families
- [x] Frontier Team ownership and Agent-assisted maintenance boundary
- [x] Faceted trust profile: provenance / review / verification / authorization
- [x] Draft/publication boundary and Asset-specific publication policies
- [x] Product Asset publication gate and generic maintenance loop
- [x] `PA-*` Product Asset Maintenance Skill namespace separated from `FT-*`
- [x] Asset lifecycle legal states, published revision immutability, freshness, dependencies, invalidation, supersession
- [x] Product Intelligence Index / ProductAssetRef / bounded progressive selection contract
- [x] Product Asset vs feature-specific EvidenceRef boundary
- [x] Layer 1 consumption map
- [x] Incremental bootstrap principle based on reuse/ROI
- [x] Layer 2 success metrics tied to Layer 1 quality and maintenance cost

Current state:

```text
Layer 1 Contract-ready: APPROVED
Layer 2 Product Intelligence Contract-ready: APPROVED
Layer 2 Execution-verified: NOT_CLAIMED
Product Asset maintenance implementation: NOT_AUTHORIZED_BY_THIS_DESIGN
```

Approval of this framework authorizes the Product Asset **contract model** only. It does not by itself authorize creation, refresh, publication, or migration of Product Assets in any repository or source system.
