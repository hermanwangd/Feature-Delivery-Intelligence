# FDI Product Asset Maintenance Skill Contracts v0.1

> **Status:** APPROVED — Contract-ready  
> **Depends on:** FDI Layer 1 — Feature Transformation Specification v0.2 (`Contract-ready: APPROVED`)  
> **Depends on:** FDI Layer 2 — Product Intelligence Asset Framework v0.1 (`Contract-ready: APPROVED`)  
> **Depends on:** FDI Product Asset Profile Specification v0.1 (`Contract-ready: APPROVED`)  
> **Scope:** Generic `PA-*` maintenance Skill contract plus `PA-Codebase-Inventory` and `PA-Historical-Delivery`  
> **Primary actor:** Frontier Team; Agents/Squads execute approved `PA-*` Skills under delegated capabilities  
> **Design only:** No crawler, correlator, indexer, asset migration, source-system mutation, validator, or publication execution is authorized by this specification

---

# 0. Purpose

Layer 2 defines **what durable Product Assets a Frontier Team maintains**. Product Asset Profiles define the minimum semantics of those Assets. This specification defines the next level down:

> **How an Agent may assist the Frontier Team in creating, refreshing, reconciling, and proposing revisions to those Product Assets without silently changing product authority.**

`PA-*` Skills are not Layer 1 feature transitions and are not T0.

```text
Frontier Team maintenance need
        |
        v
Approved PA-* Skill
        |
        +--> reads governed source snapshots
        +--> refers to supporting Product Assets
        +--> compares active Asset revision
        |
        v
Maintenance Bundle
        |
        +--> NO_CHANGE
        |
        +--> Asset revision proposal (DRAFT)
        |
        +--> publication recommendation
        |
        `--> gaps / conflicts / invalidation findings
```

The Frontier Team remains accountable for the Product Asset family and its publication policy. An Agent executes the Skill; it does not acquire the authority of the Asset owner merely by executing the Skill.

---

# 1. Core Maintenance Function

The common Product Asset maintenance abstraction is:

```text
MaintenanceBundle
=
f(
  MaintenanceRequest,
  SourceSnapshot(s),
  ExistingActiveAsset?,
  PA-Skill@revision
  ;
  SupportingProductAssetRefs
)
```

where:

- `MaintenanceRequest` defines why and within what scope maintenance is being performed;
- `SourceSnapshot(s)` are exact source identities plus immutable revisions or declared as-of states;
- `ExistingActiveAsset?` is the currently active Asset revision when this is a refresh/reconciliation run;
- `PA-Skill@revision` defines the governed maintenance procedure;
- `SupportingProductAssetRefs` are optional durable Assets referenced to interpret or classify source data;
- `MaintenanceBundle` contains the proposed result and provenance but does not by itself create Layer 1 feature truth.

The maintenance function is **governed and traceable**, not required to be byte-identical deterministic when semantic reasoning is involved.

---

# 2. Generic `PA-*` Skill Contract

Every `PA-*` Skill MUST define the following.

| Field | Required meaning |
| --- | --- |
| `skill_id` | Stable maintenance Skill identity |
| `skill_revision` | Exact governed Skill revision |
| `asset_profile` | Product Asset Profile the Skill is allowed to maintain |
| `asset_types` | Specific Asset types the Skill can produce or refresh |
| `maintenance_actions` | `CREATE`, `REFRESH`, `RECONCILE`, `CORRECT`, or a declared subset |
| `accepted_source_types` | Source classes the Skill may read |
| `source_selectors` | Bounded rules for selecting source records |
| `supporting_asset_requirements` | Product Assets that may/must be referenced |
| `procedure` | Required maintenance steps |
| `authority_preservation` | Rules preventing derivation from gaining unsupported authority |
| `trust_assignment` | How provenance/review/verification/authorization facets are assigned |
| `capabilities` | Permitted tools/actions |
| `side_effects` | External changes the Skill may propose or perform |
| `output_contract` | Required Maintenance Bundle structure |
| `publication_eligibility` | Rules for auto-publish eligibility vs Human approval |
| `invalidation_detection` | Source/dependency changes the Skill must identify |
| `idempotence` | Rules preventing duplicate semantic revisions for unchanged source state |
| `failure_classes` | Named blocking/gap/conflict outcomes |
| `prohibitions` | Actions the Skill may not perform |

A helper Skill may be called internally, but materially influential helper identity/revision MUST be recorded in maintenance provenance.

`trust_assignment` MUST populate the Layer 2 faceted `trust_profile` (`provenance`, `review`, `verification`, `authorization`) from observed source/review/check paths. It MUST NOT collapse them into one confidence score or infer organizational authorization from model confidence.

---

# 3. Maintenance Request Contract

A maintenance run MUST begin with a bounded `MaintenanceRequest`.

Minimum semantics:

```yaml
maintenance_request:
  request_id: "<stable-run-request-id>"
  action: "CREATE|REFRESH|RECONCILE|CORRECT"
  trigger: "HUMAN_REQUEST|SOURCE_CHANGE|SCHEDULED_REFRESH|INVALIDATION|LAYER1_FEEDBACK|MANUAL_REVIEW"
  target_profile: "PA-03|PA-05"
  target_asset_type: "<asset-type>"
  target_asset_id: "<asset-id-or-null-for-create>"
  scope:
    products: []
    systems: []
    repositories: []
    source_records: []
    time_range: null
  requested_as_of: "<time-or-source-state>"
  requested_by: "<frontier-team-role-or-system-trigger>"
```

The request scope is a **maintenance boundary**, not permission to infer completeness beyond that scope.

A Layer 1 miss may create a maintenance request or feedback record, but MUST NOT directly mutate a Product Asset.

---

# 4. Source Snapshot Contract

Every materially used source MUST be represented as a reviewable snapshot/reference:

```yaml
source_snapshot:
  source_ref: "<canonical-source-ref>"
  source_type: "<provider/work-item/pr/commit/catalog/manifest/etc>"
  revision_or_as_of: "<immutable-revision-or-as-of>"
  selected_for: "<maintenance-purpose>"
  authority_for: ["DURABLE_CONSTRAINT|CURRENT_BEHAVIOR_SUPPORT|RATIONALE_SUPPORT"]
  source_trust:
    provenance: "DIRECT|DERIVED|ASSERTED"
    review: "UNREVIEWED|REVIEWED"
    verification: "NOT_VERIFIED|VERIFIED"
    authorization: "NONE|SOURCE_INHERITED|EXPLICIT"
  retrieval_state: "AVAILABLE|PARTIAL|UNAVAILABLE|CONFLICTING"
```

Rules:

1. source identity and revision/as-of state MUST be explicit;
2. mutable "latest" references are insufficient for published derivation unless the as-of state is captured;
3. `authority_for` MUST use only approved Layer 2 authority dimensions and the Skill MUST preserve source-specific authority instead of flattening all sources into one trust level;
4. source trust facets MUST be preserved separately; a maintenance Skill MUST NOT manufacture `REVIEWED`, `VERIFIED`, or `EXPLICIT` status that the source/review path did not establish;
5. unavailable or conflicting sources create explicit gaps/conflicts rather than silent substitution;
6. source selection MUST remain bounded by the Maintenance Request and Skill selectors.

---

## 4.1 Supporting Product Asset eligibility

A supporting Product Asset reference MUST pin exact `asset_id` and `asset_revision`. Normal maintenance uses only `PUBLISHED + ACTIVE` supporting Assets. A `DRAFT` or `STALE` Asset may be used only when the specific PA-Skill declares an investigative exception, and that exception MUST be recorded as a limitation; it cannot satisfy an authoritative dependency requirement.

# 5. Maintenance Bundle Contract

Every `PA-*` Skill run returns one `MaintenanceBundle`.

```yaml
maintenance_bundle:
  request_id: "<request-id>"
  skill:
    id: "<PA-skill-id>"
    revision: "<skill-revision>"

  result: "NO_CHANGE|REVISION_PROPOSED|LIFECYCLE_UPDATE_PROPOSED|BLOCKED"

  target:
    asset_id: "<asset-id>"
    asset_profile: "<profile-id>"
    asset_type: "<asset-type>"
    prior_active_revision: "<revision-or-null>"
    prior_validity_state: "<ACTIVE|STALE|SUPERSEDED|NOT_APPLICABLE-or-null>"

  proposal:
    proposed_asset_revision: "<revision-or-null>"
    proposed_publication_state: "DRAFT|NONE"
    semantic_diff_ref: "<diff-ref-or-null>"
    proposed_validity_state: "ACTIVE|STALE|SUPERSEDED|NOT_APPLICABLE|NONE"
    lifecycle_reason: "<reason-or-null>"

  publication:
    eligibility: "RULE_BASED_AUTO_ELIGIBLE|HUMAN_APPROVAL_REQUIRED|NOT_PUBLISHABLE"
    reasons: []

  sources_used: []
  supporting_assets_used: []
  helper_skills_used: []

  findings:
    source_gaps: []
    conflicts: []
    invalidation_findings: []
    limitations: []

  maintenance_provenance:
    executor: "<agent/role>"
    execution_id: "<run-id>"
    executed_at: "<timestamp>"
```

## 5.1 Result semantics

### `NO_CHANGE`

The active Asset remains semantically correct for the evaluated maintenance scope and source state. No new semantic Asset revision is created.

### `REVISION_PROPOSED`

A semantic Asset revision is proposed. It is `DRAFT` until publication occurs according to the Asset policy.

### `LIFECYCLE_UPDATE_PROPOSED`

The semantic Asset revision remains unchanged, but lifecycle validity should change, for example `ACTIVE -> STALE`, `STALE -> ACTIVE` after successful revalidation, or `ACTIVE -> SUPERSEDED`. The Maintenance Bundle MUST state the exact prior/proposed validity states and reason. Lifecycle metadata changes do not create a new semantic `asset_revision`.

### `BLOCKED`

The Skill cannot safely determine the required Asset state because a required source, identity, authority, or conflict condition is unresolved.

`BLOCKED` MUST NOT mutate the currently active published Asset.

## 5.2 Publication eligibility is not publication

The Skill may classify a proposal as:

```text
RULE_BASED_AUTO_ELIGIBLE
HUMAN_APPROVAL_REQUIRED
NOT_PUBLISHABLE
```

This is a recommendation under the approved Asset contract. It is **not itself the publication state transition**.

Actual publication is governed by the Layer 2 Asset publication policy and accountable authority.

---

# 6. Common Maintenance Invariants

## 6.1 Published Asset immutability

A `PUBLISHED` semantic revision MUST NOT be rewritten.

Any semantic/provenance change produces a new `asset_revision`.

## 6.2 Lifecycle revalidation

Semantic revision and lifecycle validity are separate. A refresh MAY return `LIFECYCLE_UPDATE_PROPOSED` without creating a new Asset revision when the content/provenance binding is unchanged but validity changes. In particular, a previously `STALE` revision MAY return to `ACTIVE` only after the invalidation condition has been re-evaluated against qualified current sources.

## 6.3 Idempotence

For the same:

```text
MaintenanceRequest scope
+ exact SourceSnapshot set
+ exact supporting ProductAssetRefs
+ PA-Skill revision
+ existing active Asset revision
```

a repeated run SHOULD produce `NO_CHANGE` rather than an unnecessary new semantic revision when no material semantic difference exists.

## 6.4 Authority preservation

A derived output MUST NOT gain authority merely because it is normalized, summarized, indexed, or generated by a powerful model.

For example:

```text
source says "owner unknown"
        ↓
PA-Skill
        ↓
MUST NOT become "Team A owns this repo"
```

unless a qualified source supports that claim.

## 6.5 Scope-qualified completeness

Every completeness claim MUST identify the scope it covers.

```text
"complete repository inventory"
```

is invalid without a declared product/system/provider/source boundary.

## 6.6 No Layer 1 mutation

`PA-*` Skills MUST NOT:

- change an active Intention;
- change an active Delivery Spec;
- alter a Layer 1 gate or validity state;
- convert a Product Asset relation into a feature-specific `CONFIRMED` Change Surface finding;
- modify Layer 1 artifacts automatically because an Asset changed.

They MAY emit a downstream-impact signal for Layer 1 to evaluate.

## 6.6a Default side-effect boundary

Unless a specific approved PA-Skill explicitly declares otherwise, maintenance execution is read-only against upstream source systems. Permitted outputs are Maintenance Bundles, DRAFT Asset revision proposals, lifecycle-update proposals, index deltas, and review/publication recommendations. Source-system mutation and publication are separate governed actions.

## 6.7 Frontier Team accountability

The Frontier Team owns:

- Asset scope;
- publication policy;
- semantic review requirements;
- authority delegation;
- acceptable incompleteness;
- retirement/supersession decisions when not deterministic.

The Agent/Squad owns execution trace and adherence to the approved Skill contract.

---

# 7. `PA-Codebase-Inventory` Skill Contract

## 7.1 Identity

```yaml
skill_id: "PA-Codebase-Inventory"
asset_profile: "PA-03"
asset_types:
  - "CB-01_REPOSITORY_INVENTORY"
maintenance_actions:
  - "CREATE"
  - "REFRESH"
  - "RECONCILE"
  - "CORRECT"
```

## 7.2 Purpose

Maintain a bounded, stable, provenance-backed inventory of repositories relevant to declared Product/System scope so Layer 1 Agents can navigate the current product codebase without assuming a complete enterprise dependency graph.

The Skill answers:

> **What repositories currently exist in the declared scope, what stable identities/ownership/product mappings are known, and what navigation metadata can safely be reused?**

It does **not** answer:

> **Which repositories must change for a specific feature?**

That remains FT-T2 responsibility.

## 7.3 Accepted source types

The Skill MAY read, according to declared source authority:

- canonical Git/repository provider metadata;
- repository registry;
- CODEOWNERS or approved ownership system;
- product/service catalog;
- deployment/service descriptors;
- package/build manifests;
- repository-level metadata/configuration;
- approved product/system mapping assets;
- explicitly approved manual correction records.

The Skill MUST NOT treat:

- README prose alone as authoritative ownership;
- repository naming convention alone as product membership;
- semantic similarity alone as stable repository lineage;
- branch names or transient development metadata as canonical repository identity.

## 7.4 Supporting Product Assets

Optional/conditional supporting Assets may include:

```text
Product Asset
Architecture Asset
existing Codebase Asset
approved Reference Asset
```

These are used for classification/navigation only within their declared authority dimensions.

## 7.5 Required procedure

`PA-Codebase-Inventory` MUST:

1. pin the Maintenance Request scope and requested as-of state;
2. enumerate repositories from the declared canonical repository source(s);
3. establish or recover stable `repo_id`;
4. resolve canonical repository reference;
5. preserve aliases and known identity lineage;
6. classify repository lifecycle state;
7. resolve ownership from the approved ownership source, or record an ownership gap;
8. resolve product/system membership from qualified sources, or record `UNKNOWN`;
9. derive bounded technical fingerprint fields where supported:
   - language/platform;
   - build/package manifests;
   - primary entry points;
   - declared contracts;
   - deployment/service descriptors;
10. retain field-level provenance/authority;
11. compare against the active CB-01 revision;
12. detect create/archive/rename/move/replacement/split/merge signals;
13. distinguish rename/move from replacement/split/merge when evidence permits;
14. expose unresolved identity collisions rather than merging them heuristically;
15. calculate scope-qualified completeness/limitations;
16. calculate semantic diff;
17. assign publication eligibility;
18. return the Maintenance Bundle.

## 7.6 Repository identity continuity rules

Stable `repo_id` is not the repository display name.

A rename/move MAY retain the same `repo_id` when repository continuity is established.

```text
repo-old-name
      ↓ rename
repo-new-name
```

may remain one identity.

By contrast:

```text
repo-A
  ↓ split
repo-B + repo-C
```

or:

```text
repo-A + repo-B
  ↓ merge
repo-C
```

MUST be represented through lineage/replacement semantics rather than silently reusing one identity.

When continuity cannot be established confidently, the Skill MUST surface `IDENTITY_CONFLICT` or an explicit unknown lineage state.

## 7.7 Minimum CB-01 output semantics

Each repository record MUST expose the PA-03 profile fields, including semantics equivalent to:

```yaml
repo_id: "<stable-id>"
canonical_ref: "<repo-provider-ref>"
repository_state: "ACTIVE|ARCHIVED|REPLACED|UNKNOWN"
aliases: []
lineage_refs: []

product_system_refs: []
owner_refs: []

role_summary: "<bounded-reusable-description-or-unknown>"
languages_platforms: []
known_entrypoint_refs: []
known_contract_refs: []
manifest_refs: []
deployment_refs: []

source_state:
  revision_or_as_of: "<source-state>"
completeness:
  declared_scope_ref: "<coverage-boundary-ref>"
  inventory: "COMPLETE_FOR_DECLARED_SCOPE|PARTIAL|UNKNOWN"
  semantic_description: "CURATED|DERIVED|MINIMAL|UNKNOWN"
source_refs: []
limitations: []
```

Field-level provenance MAY be normalized into a supporting provenance table rather than repeated inline, provided backward traceability is preserved.

## 7.8 Publication eligibility

### `RULE_BASED_AUTO_ELIGIBLE`

Allowed only when all materially changed fields are deterministic/source-backed under an approved rule, such as:

- repository creation/archive state from canonical provider;
- exact repository reference;
- stable identity continuity established by approved deterministic identity rule;
- ownership from approved ownership source;
- manifest-derived language/platform fields;
- source/as-of metadata.

### `HUMAN_APPROVAL_REQUIRED`

Required when material publication depends on judgment, including:

- ambiguous repository identity continuity;
- conflicting ownership sources;
- ambiguous product/system membership;
- semantic `role_summary` that materially affects selection;
- split/merge/replacement interpretation not covered by approved deterministic rule.

### `NOT_PUBLISHABLE`

Required when:

- canonical repository identity cannot be established;
- required source provenance is missing;
- unresolved collision would create duplicate/incorrect repository identity;
- requested completeness claim cannot be supported.

## 7.9 Failure classes

```text
SOURCE_UNAVAILABLE
SOURCE_PARTIAL
IDENTITY_CONFLICT
OWNERSHIP_CONFLICT
PRODUCT_SCOPE_CONFLICT
LINEAGE_UNRESOLVED
COMPLETENESS_UNSUPPORTED
PUBLICATION_POLICY_BLOCK
```

Each failure is claim/scope-specific when possible; a gap in one repository record need not block unrelated valid records unless the requested publication scope requires atomic completeness.

## 7.10 Prohibitions

The Skill MUST NOT:

- create or delete source repositories;
- rewrite CODEOWNERS/service catalogs;
- invent ownership;
- infer architecture policy;
- claim a complete organization graph;
- publish a high-confidence current feature impact;
- mark an indexed repository as required for a particular feature;
- rewrite historical CB-01 revisions.

## 7.11 Quality measures

Recommended maintenance quality indicators:

```text
repository identity collision rate
ownership coverage within declared scope
product/system mapping coverage
source freshness lag
manual reconciliation rate
unnecessary revision rate
stale active Asset rate
```

These are Layer 2 maintenance measures, not Layer 1 Feature Delivery KPIs.

---

# 8. `PA-Historical-Delivery` Skill Contract

## 8.1 Identity

```yaml
skill_id: "PA-Historical-Delivery"
asset_profile: "PA-05"
asset_types:
  - "DH-01_HISTORICAL_DELIVERY_RECORD"
maintenance_actions:
  - "CREATE"
  - "REFRESH"
  - "RECONCILE"
  - "CORRECT"
```

`DH-02 Delivery History Index` is a derived navigation projection over published DH-01 records. v0.1 does not require a separate semantic correlation Skill for DH-02; the maintenance run MUST emit enough stable selection metadata for the Layer 2 index to be refreshed deterministically.

## 8.2 Purpose

Transform bounded historical delivery sources into reusable, provenance-backed records of what was requested and what was observed to change historically.

The Skill answers:

> **For this historical delivery unit, what product-change semantics, delivery sources, repositories, paths, and change types are supported by historical evidence?**

It does not answer:

> **What must change for a current feature?**

## 8.3 Accepted source types

The Skill MAY read:

- historical Feature/Epic records;
- backlog/work items/issues;
- requirement and acceptance-criteria records;
- linked design/review records;
- PRs;
- commits;
- code-review records;
- CI/build/test records;
- release/deployment evidence where relevant;
- approved manual correlation/correction records.

Every source must retain original identity and revision/as-of semantics where available.

## 8.4 Historical delivery unit identity

The Skill MUST establish:

```yaml
delivery_unit_id: "<stable-fdi-history-id>"
primary_work_item_ref: "<feature/backlog/source-ref>"
```

`delivery_unit_id` is the stable FDI Asset identity. It is not required to equal the upstream tracker ID.

Multiple historical work items may participate in one delivery unit, but the grouping rationale and source linkage MUST be explicit.

The Skill MUST NOT merge work items into one delivery unit merely because their text is semantically similar.

## 8.5 Required procedure

`PA-Historical-Delivery` MUST:

1. pin Maintenance Request scope and historical source boundary;
2. identify the primary historical work item;
3. collect declared linked backlog/issues;
4. collect PR/commit/review/CI/release sources through bounded link traversal;
5. preserve a correlation record for every materially used source;
6. classify correlation method and strength;
7. extract historical product-change semantics with provenance;
8. identify observed repositories and paths;
9. identify observed change types such as:
   - API;
   - EVENT;
   - SCHEMA;
   - CONFIG;
   - PACKAGE;
   - DEPLOYMENT;
   - DATA;
   - TEST;
   - OPERATIONS;
10. create one or more source-backed historical change facts;
11. map each fact to its supporting evidence;
12. classify delivery relevance:
   - `FEATURE_DELIVERY`;
   - `CO_DELIVERED`;
   - `INCIDENTAL`;
   - `UNKNOWN`;
13. default ambiguous relevance to `UNKNOWN`;
14. record delivery outcome where supported:
   - `EFFECTIVE`;
   - `PARTIALLY_EFFECTIVE`;
   - `REVERTED`;
   - `SUPERSEDED`;
   - `UNKNOWN`;
15. establish `delivered_as_of` plus its basis;
16. represent conflicts, reverts, replacements, missing links, and incompleteness;
17. compare against active DH-01 revision;
18. calculate semantic diff;
19. assign publication eligibility;
20. emit stable selection metadata for DH-02 navigation;
21. return the Maintenance Bundle.

## 8.6 Correlation contract

Every materially influential linked source MUST have a correlation record.

Conceptually:

```yaml
correlation:
  source_ref: "<PR/commit/work-item/etc>"
  method: "<method-id>"
  derivation: "EXPLICIT|DERIVED|MANUAL"
  strength: "STRONG|AMBIGUOUS"
  review: "UNREVIEWED|REVIEWED"
  evidence_refs: []
  limitations: []
```

Examples of strong explicit linkage:

```text
EXPLICIT_FEATURE_LINK
EXPLICIT_BACKLOG_LINK
EXPLICIT_PR_WORKITEM_LINK
EXPLICIT_COMMIT_WORKITEM_LINK
RELEASE_LINK
```

Derived methods may include:

```text
BRANCH_OR_PR_METADATA_LINK
DERIVED_SEMANTIC_LINK
DERIVED_TEMPORAL_LINK
```

A derived link MAY be useful for candidate investigation but MUST NOT be silently upgraded to explicit linkage.

## 8.7 Historical change fact contract

Each materially reusable fact MUST preserve:

```yaml
historical_change_fact:
  fact_id: "<stable-within-delivery-unit>"
  kind: "REPOSITORY|PATH|API|EVENT|SCHEMA_DATA|CONFIG|OPERATIONS|TEST_VALIDATION|OTHER"
  subject_ref: "<historical-repo-path-contract-or-other-ref>"
  current_repo_id: "<optional-current-PA-03-navigation-mapping>"
  detail: "<bounded-historical-observation>"
  evidence_refs: []
  delivery_relevance: "FEATURE_DELIVERY|CO_DELIVERED|INCIDENTAL|UNKNOWN"
  confidence_basis: "<source/correlation-basis>"
  limitations: []
```

Historical identity is preserved in `subject_ref`. `current_repo_id`, when present, is navigation support derived from PA-03 identity/lineage evidence and MUST NOT rewrite the historical identity.

The critical invariant is:

```text
historical fact
    -> historical evidence
    -> declared delivery relevance
```

A linked PR touching repo X does not by itself prove that repo X was necessary for the feature.

## 8.8 Feature semantics contract

The Skill MAY derive reusable feature terms/capability labels for retrieval, but MUST preserve derivation.

Examples:

```text
product area
capability
feature family
domain terms
change intent terms
```

Derived feature semantics support search/navigation. They do not become Product/Domain/Architecture authority.

## 8.9 Delivery outcome and temporal semantics

`delivered_as_of` MUST state both value and basis.

Examples:

```text
MERGE
RELEASE
WORK_ITEM_DONE
OTHER
UNKNOWN
```

A later correction, newly discovered PR, or newly discovered revert may require a new DH-01 semantic revision.

Historical records generally do not become stale because the current codebase changed; they become incomplete/incorrect only when the representation of what happened historically is corrected or expanded.

## 8.10 Publication eligibility

### `RULE_BASED_AUTO_ELIGIBLE`

May be used when:

- historical source correlation is based entirely on declared strong/deterministic links;
- extraction is source-backed;
- delivery relevance remains `UNKNOWN` where semantic judgment would otherwise be required;
- no material historical conflict is unresolved;
- delivered-as-of basis is mechanically supported.

### `HUMAN_APPROVAL_REQUIRED`

Required when a material reusable conclusion depends on:

- ambiguous semantic/temporal linkage;
- manual reconstruction;
- classifying a material change as `FEATURE_DELIVERY`, `CO_DELIVERED`, or `INCIDENTAL` without an approved deterministic rule;
- resolving conflicting/reverted sources;
- grouping multiple work items into one delivery unit through judgment;
- excluding a material linked change from the reusable history pattern.

### `NOT_PUBLISHABLE`

Required when:

- primary delivery-unit identity cannot be established;
- material historical evidence has no recoverable provenance;
- conflict could materially change the represented repo/change surface and cannot be exposed safely;
- correlation is too weak to support even the bounded historical claim being published.

## 8.11 DH-02 index delta

The Skill SHOULD emit selection/index metadata such as:

```text
product/system terms
capability/feature-family terms
repo IDs
change types
delivered-as-of
delivery outcome
correlation-quality indicators
```

DH-02 aggregates MUST be calculated only from eligible published DH-01 records and MUST expose:

```text
support_count
denominator
source_record_refs
aggregation_as_of
aggregation_rule_revision
```

The index is navigation intelligence, not authority.

## 8.12 Failure classes

```text
PRIMARY_WORK_ITEM_UNRESOLVED
SOURCE_LINK_CONFLICT
SOURCE_UNAVAILABLE
CORRELATION_AMBIGUOUS
DELIVERY_UNIT_GROUPING_AMBIGUOUS
HISTORICAL_FACT_UNSUPPORTED
DELIVERY_RELEVANCE_REVIEW_REQUIRED
DELIVERY_OUTCOME_UNRESOLVED
PUBLICATION_POLICY_BLOCK
```

Ambiguity MAY result in a publishable record with explicit `UNKNOWN` fields when the Asset Profile permits that bounded claim. It need not always block the entire historical record.

## 8.13 Prohibitions

The Skill MUST NOT:

- infer current repo applicability;
- label historical repo touch as a current feature requirement;
- fabricate links between Feature/Backlog/PR/Commit;
- hide a revert or conflicting delivery path when material;
- convert historical patterns into Architecture or Domain policy;
- use future historical replay truth to rewrite what sources were actually linked;
- rewrite published DH-01 revisions.

## 8.14 Quality measures

Recommended maintenance quality indicators:

```text
source-link provenance coverage
historical fact evidence coverage
explicit-vs-derived correlation mix
UNKNOWN delivery-relevance rate
manual review rate
late-discovered linked-source rate
duplicate delivery-unit rate
index support/denominator integrity
```

High `UNKNOWN` rate is not automatically poor quality; it can be preferable to false semantic certainty.

---

# 9. Frontier Team Operating Boundary

For both Skills:

```text
Frontier Team
├── owns Asset profile/policy
├── approves semantic authority delegation
├── resolves material ambiguity
└── publishes/retire/supersedes according to policy

PA-* Agent/Squad
├── executes maintenance procedure
├── preserves evidence/provenance
├── proposes semantic revision
├── identifies gaps/conflicts
└── recommends publication disposition

Layer 2 governance
├── validates legal Asset lifecycle transition
├── preserves immutable published revisions
└── exposes eligible Asset refs to Layer 1

Layer 1
└── selectively resolves Product Assets as execution Context
```

A maintenance Agent may be highly autonomous for deterministic refresh work while publication policy remains stricter for semantic judgments.

---

# 10. First Implementation Boundary

This specification deliberately stops before physical implementation.

After approval, the first implementation design SHOULD define only:

1. the physical `SKILL.md` contract for `PA-Codebase-Inventory`;
2. the physical `SKILL.md` contract for `PA-Historical-Delivery`;
3. source adapters/selectors required by a chosen pilot product;
4. Product Asset descriptor/materialization layout;
5. dry-run mode that emits Maintenance Bundles without publishing;
6. validator checks for the contracts in this specification.

It SHOULD NOT start with:

- complete enterprise repository graph extraction;
- generic knowledge graph infrastructure;
- automatic semantic publication;
- every Product Asset family;
- organization-wide historical backfill.

---

# 11. Design Approval Checklist

Approved decisions:

- [x] Generic `PA-*` maintenance function and Skill interface
- [x] Maintenance Request and Source Snapshot contracts
- [x] Maintenance Bundle result, lifecycle-update, and publication-eligibility semantics
- [x] Published-Asset immutability, lifecycle revalidation, and maintenance idempotence
- [x] Authority-preservation, faceted trust, and scope-qualified completeness invariants
- [x] No automatic Layer 1 mutation and default upstream read-only boundary
- [x] `PA-Codebase-Inventory` source classes and bounded maintenance procedure
- [x] Stable repository identity / rename / split / merge semantics
- [x] CB-01 Profile enum/schema alignment and deterministic vs Human-reviewed publication boundary
- [x] `PA-Historical-Delivery` historical source and delivery-unit identity model
- [x] Per-source correlation and historical-change-fact contracts with preserved historical identity
- [x] `UNKNOWN` as safe default for ambiguous delivery relevance
- [x] Historical delivery outcome and delivered-as-of semantics aligned to PA-05 Profile
- [x] DH-01 deterministic vs Human-reviewed publication boundary
- [x] DH-02 index delta is navigation only and exposes support/denominator
- [x] Frontier Team accountability vs Agent execution boundary
- [x] First implementation boundary and non-goals

Current state:

```text
Layer 1 Contract-ready: APPROVED
Layer 2 Product Intelligence Contract-ready: APPROVED
Product Asset Profile v0.1 Contract-ready: APPROVED

Product Asset Maintenance Skill Contracts v0.1:
Contract review: PASS
Contract-ready: APPROVED
Herman design approval: APPROVED
Execution-verified: NOT_CLAIMED
Physical SKILL.md validation: NOT_CLAIMED
Implementation/publication: NOT_AUTHORIZED_BY_THIS_DESIGN
```

---

# 12. Compact Model

```text
                  FRONTIER TEAM

         maintenance request / source change
                       |
                       v
       +----------------------------------+
       |       PA-* Maintenance Skill     |
       |                                  |
       |  sources + current Asset         |
       |  + supporting Product Assets     |
       +----------------+-----------------+
                        |
                        v
                Maintenance Bundle
              /          |          \
             /           |           \
       NO_CHANGE   REVISION/LIFECYCLE   BLOCKED
                         |
                         v
              publication eligibility
                /             \
       RULE_BASED_AUTO      HUMAN_APPROVAL
                         |
                         v
                  PUBLISHED + ACTIVE
                         |
                         v
                 Product Asset Ref
                         |
                         v
─────────────────────────┼────────────────────────
                         |
                    LAYER 1 Context
                         |
                         v
                     FT-* Skill
```

The central invariant is:

> **PA-* Skills maintain durable Product Assets for the Frontier Team; FT-* Skills consume selected Product Assets as Context to deliver a specific feature. Neither layer silently acquires the authority of the other.**
