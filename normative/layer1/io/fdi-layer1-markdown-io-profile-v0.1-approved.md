# FDI Layer 1 — Markdown I/O Profile v0.1

> **Status:** APPROVED — Contract-ready  
> **Depends on:** FDI Layer 1 — Feature Transformation Specification v0.2 (`Contract-ready: APPROVED`)  
> **Purpose:** Fix the physical Markdown I/O contract for Layer 1 so an Agent can read and produce canonical artifacts without inventing file structure  
> **Scope:** `intention.md`, `spec.md`, `implementation.md`, `correctness.md`, and three governed appendix profiles  
> **Design only:** No validator, repository layout deployment, Skill implementation, pilot, or execution claim  
> **Current state:** `Markdown-I/O Contract-ready: NOT_CLAIMED`

---

# 0. Core Rule

FDI Layer 1 already defines the semantic transformation:

```text
OutputBundle = f(
    CanonicalInput(s),
    GovernedSkill@revision
    ; ResolvedContextRefs
)
```

This profile fixes the **physical Markdown representation** of each canonical Layer 1 input/output artifact.

The goal is:

> A compliant Agent MUST NOT need to invent headings, record placement, IDs, or machine-readable structure for a canonical Layer 1 artifact.

This profile does not change Layer 1 authority, gate, lifecycle, Change Surface, or Correctness semantics.

Execution-time Evidence and tool/capability use remain governed by the Skill and are **not additional canonical function inputs**. The physical artifact records the resulting `EvidenceRef`/provenance after observation.

---

# 1. Physical Markdown Rules

## 1.1 Required file structure

Every canonical Layer 1 Markdown file MUST contain:

```text
YAML frontmatter
        +
fixed ordered H1/H2 section structure
        +
structured YAML records in declared sections
        +
bounded human-readable narrative where permitted
```

The frontmatter and structured records are the machine-interoperable contract.

Narrative text explains rationale, interpretation, and bounded detail but MUST NOT contradict structured records.

If narrative and structured content conflict, the producing transition is non-compliant and the artifact MUST NOT claim a ready/pass gate.

## 1.2 Required sections are never omitted

Every section marked `REQUIRED` MUST be present even when empty.

Use one of:

```text
NONE
```

or:

```yaml
status: "NOT_APPLICABLE"
reason: "<why this section does not apply>"
```

Do not omit the heading because an Agent thinks it is irrelevant.

## 1.3 Optional sections

A section marked `CONDITIONAL` is required when its trigger is true. When the trigger is false, it MAY be omitted unless the owning core template explicitly requires an applicability record.

## 1.4 Stable IDs

IDs MUST be stable within one feature lineage.

Recommended prefixes:

```text
Human Signal fragment HSF-001
Criterion              C-001
Requirement            R-001
Design invariant       D-001
Task                   T-001
V&V method             V-001
Change Surface         CS-001
Context reference      CTX-001
Evidence               E-001
Candidate reference    CR-001
Deviation              DEV-001
Appendix               A-001
Check                  CHK-001
Criterion verdict      uses criterion_id
```

Renumbering existing IDs solely for presentation is prohibited because it breaks traceability.

## 1.5 Structured record rule

When this profile defines a YAML record schema, the artifact MUST expose semantically equivalent machine-readable fields.

The canonical physical profile uses fenced YAML blocks.

Example:

```yaml
criteria:
  - criterion_id: "C-001"
    statement: "..."
    blocking: true
    success_measure: "..."
    threshold_or_acceptance: "..."
    human_signal_refs:
      - "signal://..."
```

Free-form prose MAY follow the structured block for explanation.

## 1.6 References

Canonical references SHOULD use stable IDs and immutable revisions/as-of states.

Do not embed raw secrets, copied source trees, or mutable-only evidence.

The following remain distinct:

```text
ResolvedContextRef
    informs/constrains transformation

EvidenceRef
    establishes a specific claim/finding/verdict
```

## 1.7 Common artifact frontmatter

All four canonical Markdown files MUST begin with:

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<stable-feature-id>"
artifact: "intention|spec|implementation|correctness"
revision: <positive-integer>

produced_by:
  skill: "<canonical-skill-id>"
  skill_revision: "<immutable-version-or-revision>"

canonical_owner: "<stable-accountable-role-or-owner-id>"

upstream: {}

gate: "<artifact-specific-gate>"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; current lineage remains authoritative
supersedes: <prior-revision-or-null>

executor:
  role_or_agent: "<stable-executor-id-or-null>"
  execution_id: "<run-id-or-null>"
---
```

Artifact-specific profiles below define the required `upstream` fields.

---

# 2. `intention.md` Physical Contract

## 2.1 Function

```text
intention.md
=
f(
  AuthenticatedHumanSignal,
  T1-Intention-Skill@revision
  ;
  ResolvedContextRefs
)
```

## 2.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "intention"
revision: <positive-integer>

produced_by:
  skill: "T1-Intention-Skill"
  skill_revision: "<revision>"

canonical_owner: "<T1-owner>"

upstream:
  human_signal_ids:
    - "<stable-signal-id>"

gate: "INTENTION_READY|BLOCKED"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; current lineage remains authoritative
supersedes: <prior-revision-or-null>

executor:
  role_or_agent: "<executor>"
  execution_id: "<run-id>"
---
```

## 2.3 Exact body structure

```markdown
# Intention

## 1. Human Signal

## 2. Stakeholders and Intended Users

## 3. Desired Outcome

## 4. Intended-Use Scenarios

## 5. Scope and Non-Goals

## 6. Constraints and Assumptions

## 7. Success Criteria

## 8. Product, System, and Repository Seeds

## 9. Context Used

## 10. Open Questions and Conflicts

## 11. Gate Record
```

All eleven H2 sections are `REQUIRED`.

## 2.4 Section contracts

### `## 1. Human Signal`

MUST contain:

```yaml
human_signals:
  - signal_id: "<stable-signal-id>"
    source_ref: "<governed-source-ref>"
    source_identity: "<requester/authority>"
    captured_at: "<timestamp>"
    authentication_state: "VERIFIED"
    authorization_state: "AUTHORIZED|NOT_AUTHORIZED|UNCLEAR"
    content_ref_or_digest: "<immutable-ref-or-digest>"
    summary: "<safe-faithful-summary>"
    fragments:
      - fragment_id: "HSF-001"
        content_locator: "<stable-location-within-signal-or-ref>"
        summary: "<faithful-fragment-summary>"
```

The summary MUST preserve the expressed need and MUST NOT introduce implementation design.

### `## 2. Stakeholders and Intended Users`

```yaml
stakeholders:
  - stakeholder_id: "<stable-local-id>"
    role: "<role>"
    relationship: "REQUESTER|APPROVER|USER|OWNER|AFFECTED|OTHER"

intended_users:
  - user_group_id: "<stable-local-id>"
    description: "<group>"
```

### `## 3. Desired Outcome`

```yaml
desired_outcome:
  statement: "<what must become true>"
  business_or_user_value: "<why it matters>"
```

### `## 4. Intended-Use Scenarios`

```yaml
intended_use_scenarios:
  - scenario_id: "S-001"
    actor: "<actor>"
    situation: "<situation>"
    expected_outcome: "<observable desired result>"
```

### `## 5. Scope and Non-Goals`

```yaml
scope:
  in_scope:
    - "<bounded item>"
  non_goals:
    - "<explicit exclusion>"
```

### `## 6. Constraints and Assumptions`

```yaml
constraints:
  - constraint_id: "CON-001"
    statement: "<constraint>"
    source: "HUMAN_SIGNAL|CONTEXT"
    ref: "<source-ref>"

assumptions:
  - assumption_id: "ASM-001"
    statement: "<assumption>"
    validation_needed: true
```

### `## 7. Success Criteria`

```yaml
criteria:
  - criterion_id: "C-001"
    statement: "<measurable desired outcome>"
    blocking: true
    success_measure: "<observable measure>"
    threshold_or_acceptance: "<pass condition>"
    human_signal_refs:
      - "HSF-001"
```

Rules:

- Every authorized requested outcome MUST map to one or more criteria.
- `blocking` defaults to `true`.
- Only T1 may set `blocking: false`, and only when Human authorization supports it.

### `## 8. Product, System, and Repository Seeds`

```yaml
impact_seeds:
  products:
    - "<product-ref>"
  systems:
    - "<system-ref>"
  repositories:
    - "<repo-ref-or-known-name>"
  completeness: "NON_EXHAUSTIVE"
```

Repository seeds MUST be explicitly marked non-exhaustive.

### `## 9. Context Used`

```yaml
resolved_context_refs:
  - context_ref_id: "CTX-001"
    requirement_id: "<T1-context-requirement-id>"
    ref: "<stable-context-ref>"
    revision_or_as_of: "<revision/time>"
    selected_for: "<purpose/claim>"
    authority_dimension: "<dimension>"
    trust_state: "<state>"
    applicability: "<scope>"
    freshness: "<state>"
    evidence_backlink: "<source/evidence-ref-or-null>"

context_exclusions:
  - requirement_id: "<context-requirement-id>"
    candidate_ref: "<context-candidate-ref>"
    reason: "<why it was not selected>"
```

If no Context was materially influential or excluded:

```yaml
resolved_context_refs: []
context_exclusions: []
```

### `## 10. Open Questions and Conflicts`

```yaml
open_items:
  - item_id: "Q-001"
    type: "QUESTION|AUTHORITY_CONFLICT|CONTEXT_GAP|AMBIGUITY"
    statement: "<issue>"
    blocking: true
    owner: "<resolution-owner>"
```

### `## 11. Gate Record`

```yaml
gate_record:
  gate: "INTENTION_READY|BLOCKED"
  evaluated_against:
    human_signal_ids:
      - "<signal-id>"
  blocking_items:
    - "<Q-id>"
  rationale: "<bounded gate rationale>"
```

---

# 3. `spec.md` Physical Contract

## 3.1 Function

```text
SpecBundle
=
f(
  intention.md@exact-active-revision,
  T2-Delivery-Spec-Skill@revision
  ;
  ResolvedContextRefs
)

core(SpecBundle) = spec.md
```

## 3.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "spec"
revision: <positive-integer>

produced_by:
  skill: "T2-Delivery-Spec-Skill"
  skill_revision: "<revision>"

canonical_owner: "<T2-owner>"

upstream:
  intention_revision: <exact-active-revision>

gate: "SPEC_READY|BLOCKED"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; current lineage remains authoritative
supersedes: <prior-revision-or-null>

executor:
  role_or_agent: "<executor>"
  execution_id: "<run-id>"
---
```

## 3.3 Exact body structure

```markdown
# Delivery Spec

## 1. Upstream Intention

## 2. Criterion-to-Requirement Mapping

## 3. Requirements

## 4. Design and Invariants

## 5. Current-State Findings

## 6. Change Surface

## 7. Interface, Data, Security, and Operational Obligations

## 8. Implementation Tasks and Ownership

## 9. Verification and Validation Plan

## 10. Appendix Registry

## 11. Context Used and Selector Proof

## 12. Risks, Gaps, and Deviations

## 13. Gate Record
```

All thirteen H2 sections are `REQUIRED`.

## 3.4 Section contracts

### `## 1. Upstream Intention`

```yaml
upstream_intention:
  feature_id: "<feature-id>"
  revision: <exact-revision>
  gate: "INTENTION_READY"
  validity_at_execution: "ACTIVE"
  criterion_ids:
    - "C-001"
```

### `## 2. Criterion-to-Requirement Mapping`

```yaml
criterion_requirement_map:
  - criterion_id: "C-001"
    requirement_ids:
      - "R-001"
    rationale: "<required when requirement_ids is empty>"
```

Every Intention criterion MUST appear exactly once in this mapping section. A non-blocking criterion may map to an empty `requirement_ids` list only when the active Intention and V&V disposition make that treatment valid; the rationale is then mandatory.

### `## 3. Requirements`

```yaml
requirements:
  - requirement_id: "R-001"
    criterion_ids:
      - "C-001"
    statement: "<technical obligation>"
    owner: "<accountable owner>"
    repo_ids:
      - "<repo-id>"
    vv_method_ids:
      - "V-001"
```

### `## 4. Design and Invariants`

```yaml
design:
  summary: "<implementation-neutral-enough technical design>"
  invariants:
    - invariant_id: "D-001"
      statement: "<must remain true>"
      requirement_ids:
        - "R-001"
```

Narrative diagrams/rationale MAY follow, but obligations MUST remain traceable through IDs.

### `## 5. Current-State Findings`

All T2 `EvidenceRef` records materially used by `spec.md`, including Change Surface confirmation/exclusion evidence, are defined in this section and referenced elsewhere by `evidence_id`.

```yaml
evidence_refs:
  - evidence_id: "E-001"
    ref: "<immutable-artifact/source/test-result-reference>"
    revision_or_as_of: "<revision/time>"
    method: "<how the observation was obtained>"
    environment: "<environment-or-N/A>"
    integrity: "<digest/signature/governed-result-ref when applicable>"
    claim_ids:
      - "STATE-001"
      - "CS-001"

current_state_findings:
  - finding_id: "STATE-001"
    statement: "<current-state claim>"
    evidence_refs:
      - "E-001"
    context_refs:
      - "CTX-001"
    limitations: []
```

Current behavior/state claims used materially by T2 MUST have an `EvidenceRef`; Context alone is insufficient when current applicability is material. Any `evidence_id` referenced in §6 or §12 MUST resolve to an `EvidenceRef` defined here or to a governed Evidence record explicitly reachable from this artifact.

### `## 6. Change Surface`

```yaml
change_surface:
  discovery_scope:
    products: []
    systems: []
    relation_types: []
    traversal_budget: "<bounded-selector-summary>"
    exclusions: []

  findings:
    - finding_id: "CS-001"
      repo_id: "<stable-repository-id>"
      status: "CANDIDATE|CONFIRMED|EXCLUDED|UNRESOLVED"
      relevance: "<why this repo may/must matter>"
      relation_types:
        - "api"
      criterion_ids:
        - "C-001"
      requirement_ids:
        - "R-001"
      context_refs:
        - "CTX-001"
      evidence_refs:
        - "E-002"
      owner: "<resolved-owner-or-null>"
      required_action: "CHANGE|VERIFY_ONLY|NO_CHANGE|NOT_APPLICABLE|UNDECIDED"
      planned_change: "<expected change/verification/no-change rationale>"
      blocking: true
```

Rules from Layer 1 L5 are normative:

- `CANDIDATE` / `UNRESOLVED` → `UNDECIDED`
- `CONFIRMED` → `CHANGE | VERIFY_ONLY | NO_CHANGE`
- `EXCLUDED` → `NOT_APPLICABLE`
- only current feature-specific `EvidenceRef` may support `CONFIRMED`

### `## 7. Interface, Data, Security, and Operational Obligations`

This section MUST contain an applicability record:

```yaml
cross_cutting_obligations:
  interfaces:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  data:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  configuration:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  schema:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  security:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  operations:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  rollout_rollback:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []
```

### `## 8. Implementation Tasks and Ownership`

```yaml
tasks:
  - task_id: "T-001"
    requirement_ids:
      - "R-001"
    repo_ids:
      - "<repo-id>"
    owner: "<accountable owner>"
    disposition: "PLANNED|NO_CHANGE|BLOCKED"
```

At `SPEC_READY`, implementation work is normally `PLANNED`; an explicit no-change obligation may use `NO_CHANGE`. `IMPLEMENTED` is not a valid T2 disposition. A `BLOCKED` task prevents `SPEC_READY` when it affects a blocking obligation.

### `## 9. Verification and Validation Plan`

```yaml
vv_dispositions:
  - criterion_id: "C-001"
    evaluation: "REQUIRED|OBSERVE_IF_AVAILABLE"
    method_id: "V-001|null"
    method: "<non-tautological-method-or-N/A>"
    evidence_expectation: "<required-evidence-or-observation-policy>"
    threshold_or_acceptance: "<pass-condition-or-N/A>"
    required_scope: "<scope-that-must-be-observed-or-N/A>"
    independence: "<required-independence-or-N/A>"
```

Every blocking criterion MUST use `REQUIRED` and define a non-tautological method, evidence expectation, threshold/acceptance, and required scope. A non-blocking criterion may use `OBSERVE_IF_AVAILABLE` only when authorized by the active Intention.

### `## 10. Appendix Registry`

```yaml
appendices:
  - appendix_id: "A-001"
    type: "SPEC"
    trigger: "<why separate detail is required>"
    status: "ACTIVE|SUPERSEDED"
    path: "appendices/spec/A-001.md"
    related_ids:
      - "R-001"
    backlink:
      owner_artifact: "spec"
      owner_revision: <this-spec-revision>
```

If no appendices:

```yaml
appendices: []
```

### `## 11. Context Used and Selector Proof`

```yaml
resolved_context_refs:
  - context_ref_id: "CTX-001"
    requirement_id: "<context-requirement-id>"
    ref: "<stable-context-ref>"
    revision_or_as_of: "<revision/time>"
    selected_for: "<purpose/claim>"
    authority_dimension: "<dimension>"
    trust_state: "<state>"
    applicability: "<scope>"
    freshness: "<state>"
    evidence_backlink: "<source/evidence-ref-or-null>"

context_exclusions:
  - requirement_id: "<context-requirement-id>"
    candidate_ref: "<context-candidate-ref>"
    reason: "<why it was excluded>"

selector_proof:
  - selector_id: "<selector-id>"
    purpose: "<purpose>"
    bounded_by: "<scope/budget/rule>"
    excluded_by_rule: []
```

### `## 12. Risks, Gaps, and Deviations`

```yaml
risks_gaps_deviations:
  - item_id: "RGD-001"
    type: "RISK|CONTEXT_GAP|EVIDENCE_GAP|DEVIATION|OWNERSHIP_GAP|DESIGN_GAP"
    statement: "<issue>"
    affected_ids:
      - "R-001"
    blocking: true
    disposition: "RESOLVED|ACCEPTED|BLOCKING|REQUIRES_AUTHORIZATION"
    owner: "<owner>"
```

### `## 13. Gate Record`

```yaml
gate_record:
  gate: "SPEC_READY|BLOCKED"
  intention_revision: <revision>
  blocking_items: []
  unresolved_change_surface_findings: []
  rationale: "<bounded gate rationale>"
```

---

# 4. `implementation.md` Physical Contract

## 4.1 Function

```text
ImplementationBundle
=
f(
  spec.md@exact-active-revision,
  T3-Implementation-Skill@revision
  ;
  ResolvedContextRefs
)
```

## 4.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "implementation"
revision: <positive-integer>

produced_by:
  skill: "T3-Implementation-Skill"
  skill_revision: "<revision>"

canonical_owner: "<T3-owner>"

upstream:
  spec_revision: <exact-active-revision>

gate: "CHANGE_SET_READY|BLOCKED"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; current lineage remains authoritative
supersedes: <prior-revision-or-null>

executor:
  role_or_agent: "<executor>"
  execution_id: "<run-id>"
---
```

## 4.3 Exact body structure

```markdown
# Implementation

## 1. Upstream Spec

## 2. Candidate Summary

## 3. Repository Implementation Dispositions

## 4. Candidate References

## 5. Changed Paths and Migrations

## 6. Requirement, Design, and Task Mapping

## 7. Checks and Observed Results

## 8. Deviations from Spec

## 9. Appendix Registry

## 10. Context Used

## 11. Execution Provenance

## 12. Known Gaps and T4 Handoff

## 13. Gate Record
```

All thirteen H2 sections are `REQUIRED`.

## 4.4 Section contracts

### `## 1. Upstream Spec`

```yaml
upstream_spec:
  feature_id: "<feature-id>"
  revision: <exact-revision>
  gate: "SPEC_READY"
  validity_at_execution: "ACTIVE"
```

### `## 2. Candidate Summary`

```yaml
candidate_summary:
  repositories_confirmed: <integer>
  repositories_change: <integer>
  repositories_verify_only: <integer>
  repositories_no_change: <integer>
  reviewable_candidate_count: <integer>
  blocking_repository_count: <integer>
  summary: "<bounded summary>"
```

### `## 3. Repository Implementation Dispositions`

```yaml
repository_dispositions:
  - repo_id: "<repo-id>"
    required_action: "CHANGE|VERIFY_ONLY|NO_CHANGE"
    disposition: "READY|BLOCKED|SUPERSEDED"
    task_ids:
      - "T-001"
    candidate_ref: "CR-001|null"
    evidence_refs:
      - "E-001"
    notes: "<bounded-disposition-summary>"
```

Every `CONFIRMED` repository from the active Spec MUST have exactly one active disposition.

### `## 4. Candidate References`

`candidate_ref_id` is the physical stable identifier used to instantiate and cross-reference the Layer 1 `candidate_ref` record.

```yaml
candidate_refs:
  - candidate_ref_id: "CR-001"
    repo_id: "<repo-id>"
    base_revision: "<immutable-base>"
    head_revision: "<immutable-head>"
    location: "<branch/PR/commit/candidate-ref>"
    status: "REVIEWABLE|NOT_READY|SUPERSEDED"
    task_ids:
      - "T-001"
```

`CHANGE` requires a candidate ref. `VERIFY_ONLY` and `NO_CHANGE` MUST NOT fabricate one.

### `## 5. Changed Paths and Migrations`

```yaml
changed_paths:
  - repo_id: "<repo-id>"
    candidate_ref_id: "CR-001"
    paths:
      - "<path>"
    change_types:
      - "CODE|CONFIG|SCHEMA|TEST|DOC|MIGRATION|OTHER"

migrations:
  - migration_id: "MIG-001"
    repo_id: "<repo-id>"
    description: "<migration>"
    rollback_ref: "<rollback-plan-ref-or-null>"
```

If no migrations:

```yaml
migrations: []
```

### `## 6. Requirement, Design, and Task Mapping`

```yaml
implementation_mappings:
  - requirement_id: "R-001"
    invariant_ids:
      - "D-001"
    task_ids:
      - "T-001"
    repo_ids:
      - "<repo-id>"
    candidate_ref_ids:
      - "CR-001"
    changed_path_refs:
      - "<repo-id>:<path>"
```

### `## 7. Checks and Observed Results`

All T3 `EvidenceRef` records referenced by repository dispositions, checks, deviations, or the T4 handoff are defined here.

```yaml
evidence_refs:
  - evidence_id: "E-001"
    ref: "<immutable-artifact/source/test-result-reference>"
    revision_or_as_of: "<revision/time>"
    method: "<how the observation was obtained>"
    environment: "<environment-or-N/A>"
    integrity: "<digest/signature/governed-result-ref when applicable>"
    claim_ids:
      - "CHK-001"

checks:
  - check_id: "CHK-001"
    type: "BUILD|TEST|STATIC|MIGRATION|CONFIG|OTHER"
    repo_id: "<repo-id>"
    candidate_ref_id: "CR-001|null"
    method: "<how check was run>"
    result: "PASS|FAIL|NOT_RUN"
    evidence_refs:
      - "E-001"
```

T3 checks are implementation observations, not T4 Correctness verdicts. Every `evidence_id` used elsewhere in `implementation.md` MUST resolve here or to a governed Evidence record explicitly reachable from this artifact.

### `## 8. Deviations from Spec`

```yaml
deviations:
  - deviation_id: "DEV-001"
    statement: "<deviation>"
    affected_ids:
      - "R-001"
    blocking: true
    classification: "IMPLEMENTATION_DEFECT|SPEC_CONFLICT|NEW_SCOPE|OTHER"
    proposed_disposition: "FIX_T3|REENTER_T2|AUTHORIZED_EXCEPTION|BLOCK"
    evidence_refs: []
```

### `## 9. Appendix Registry`

```yaml
appendices:
  - appendix_id: "A-101"
    type: "IMPLEMENTATION_REPOSITORY"
    trigger: "<why repository-local detail is separate>"
    status: "ACTIVE|SUPERSEDED"
    path: "appendices/implementation/<repo-id>.md"
    repo_id: "<repo-id>"
```

If none:

```yaml
appendices: []
```

### `## 10. Context Used`

Use the exact `resolved_context_refs` item schema from `spec.md` §11, including `requirement_id`, immutable/as-of reference, authority dimension, trust, applicability, freshness, and `evidence_backlink`. If no Context was materially influential, emit:

```yaml
resolved_context_refs: []
```

### `## 11. Execution Provenance`

```yaml
execution_provenance:
  root_skill:
    id: "T3-Implementation-Skill"
    revision: "<revision>"

  materially_influential_helpers:
    - kind: "SKILL|AGENT|REVIEWER|WORKER"
      id: "<stable-id>"
      revision: "<revision-or-model/config-ref>"
      execution_id: "<run-id>"
      contribution: "<material contribution>"

  capability_refs:
    - "<permitted-capability-ref>"
```

### `## 12. Known Gaps and T4 Handoff`

```yaml
t4_handoff:
  known_gaps:
    - gap_id: "GAP-001"
      statement: "<gap>"
      blocking_for_t4: true

  exact_candidate_refs:
    - "CR-001"

  planned_vv_method_ids:
    - "V-001"

  evidence_available:
    - "E-001"
```

### `## 13. Gate Record`

```yaml
gate_record:
  gate: "CHANGE_SET_READY|BLOCKED"
  spec_revision: <revision>
  blocking_repository_ids: []
  blocking_deviation_ids: []
  rationale: "<bounded gate rationale>"
```

---

# 5. `correctness.md` Physical Contract

## 5.1 Function

```text
CorrectnessBundle
=
f(
  intention.md@exact-active-revision,
  spec.md@exact-active-revision,
  ImplementationBundle@exact-candidate-revisions,
  T4-Correctness-Skill@revision
  ;
  ResolvedContextRefs
)
```

## 5.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "correctness"
revision: <positive-integer>

produced_by:
  skill: "T4-Correctness-Skill"
  skill_revision: "<revision>"

canonical_owner: "<T4-owner-distinct-from-T3-owner>"

upstream:
  intention_revision: <exact-active-revision>
  spec_revision: <exact-active-revision>
  implementation_revision: <exact-active-revision>
  candidate_refs:
    - "CR-001"

gate: "PASS|FAIL|INCONCLUSIVE"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; current lineage remains authoritative
supersedes: <prior-revision-or-null>

executor:
  role_or_agent: "<independent-evaluator>"
  execution_id: "<distinct-evaluation-run-id>"
---
```

## 5.3 Exact body structure

```markdown
# Correctness

## 1. Exact Inputs and Independence

## 2. Evidence Inventory and Integrity

## 3. Verification Findings

## 4. Validation Findings

## 5. Criterion Verdicts

## 6. Coverage

## 7. Deviations, Gaps, Limitations, and Unobserved Scope

## 8. Release and Production Observation

## 9. Earliest Re-entry

## 10. Context Used

## 11. Execution Provenance

## 12. Overall Verdict and Gate Record
```

All twelve H2 sections are `REQUIRED`.

## 5.4 Section contracts

### `## 1. Exact Inputs and Independence`

```yaml
exact_inputs:
  intention_revision: <revision>
  spec_revision: <revision>
  implementation_revision: <revision>
  candidate_refs:
    - candidate_ref_id: "CR-001"
      repo_id: "<repo-id>"
      head_revision: "<immutable-head>"

independence:
  t3_canonical_owner: "<T3-owner>"
  t4_canonical_owner: "<T4-owner>"
  distinct_owner: true
  t3_execution_id: "<T3-run>"
  t4_execution_id: "<T4-run>"
  distinct_evaluation_context: true
  candidate_mutation_authority_during_evaluation: false
```

### `## 2. Evidence Inventory and Integrity`

```yaml
evidence_refs:
  - evidence_id: "E-101"
    ref: "<immutable-evidence-ref>"
    revision_or_as_of: "<revision/time>"
    method: "<observation method>"
    environment: "<environment-or-N/A>"
    integrity: "<digest/signature/governed-ref when applicable>"
    claim_ids:
      - "C-001"

evidence_appendix_registry:
  - appendix_id: "A-201"
    evidence_id: "E-101"
    trigger: "<why a governed evidence file is needed>"
    status: "ACTIVE|SUPERSEDED"
    path: "appendices/evidence/E-101.md"
    backlink:
      owner_artifact: "correctness"
      owner_revision: <this-correctness-revision>
```

### `## 3. Verification Findings`

```yaml
verification_findings:
  - finding_id: "VF-001"
    requirement_id: "R-001"
    result: "PASS|FAIL|INCONCLUSIVE"
    statement: "<Spec conformance finding>"
    evidence_refs:
      - "E-101"
    limitations: []
```

### `## 4. Validation Findings`

```yaml
validation_findings:
  - finding_id: "VAL-001"
    criterion_id: "C-001"
    result: "PASS|FAIL|INCONCLUSIVE"
    intended_use_scenario_ids:
      - "S-001"
    statement: "<fitness-for-Intention finding>"
    evidence_refs:
      - "E-101"
    limitations: []
```

### `## 5. Criterion Verdicts`

```yaml
criterion_verdicts:
  - criterion_id: "C-001"
    blocking: true
    evaluation: "REQUIRED"
    verdict: "PASS|FAIL|INCONCLUSIVE"
    verification_finding: "<verification-summary-or-N/A>"
    validation_finding: "<validation-summary>"
    verification_finding_refs:
      - "VF-001"
    validation_finding_refs:
      - "VAL-001"
    evidence_refs:
      - "E-101"
    limitations: []
    earliest_reentry: "T1|T2|T3|T4|NONE"
```

### `## 6. Coverage`

```yaml
coverage:
  criteria:
    required: ["C-001"]
    observed: ["C-001"]
    missing: []

  requirements:
    required: ["R-001"]
    observed: ["R-001"]
    missing: []

  design_invariants:
    required: ["D-001"]
    observed: ["D-001"]
    missing: []

  tasks:
    required: ["T-001"]
    observed: ["T-001"]
    missing: []

  repositories:
    required: ["<repo-id>"]
    observed: ["<repo-id>"]
    missing: []

  vv_scope:
    - criterion_id: "C-001"
      required_scope: "<from Spec>"
      observed_scope: "<actual>"
      scope_satisfied: true
```

### `## 7. Deviations, Gaps, Limitations, and Unobserved Scope`

```yaml
limitations:
  - limitation_id: "LIM-001"
    type: "EVIDENCE_GAP|SCOPE_GAP|ENVIRONMENT_LIMITATION|DEVIATION|OTHER"
    statement: "<limitation>"
    affected_ids:
      - "C-001"
    blocking: true
```

If none:

```yaml
limitations: []
```

### `## 8. Release and Production Observation`

```yaml
release_observation:
  state: "OBSERVED|NOT_OBSERVED"
  details: "<bounded observation or N/A>"
  evidence_refs: []
```

`NOT_OBSERVED` does not prevent PASS unless release/production observation is an explicit blocking criterion/V&V obligation.

### `## 9. Earliest Re-entry`

```yaml
reentry:
  transition: "T1|T2|T3|T4|NONE"
  owner: "<owner-or-null>"
  cause_ids:
    - "<finding/criterion/limitation-id>"
  required_next_action: "<bounded action>"
```

### `## 10. Context Used`

Use the exact `resolved_context_refs` item schema from `spec.md` §11, including `requirement_id`, immutable/as-of reference, authority dimension, trust, applicability, freshness, and `evidence_backlink`. If no Context was materially influential, emit:

```yaml
resolved_context_refs: []
```

### `## 11. Execution Provenance`

```yaml
execution_provenance:
  root_skill:
    id: "T4-Correctness-Skill"
    revision: "<revision>"

  materially_influential_helpers:
    - kind: "SKILL|AGENT|REVIEWER"
      id: "<id>"
      revision: "<revision/config>"
      execution_id: "<run-id>"
      contribution: "<material contribution>"

  capability_refs:
    - "<capability-ref>"
```

### `## 12. Overall Verdict and Gate Record`

```yaml
overall_verdict:
  gate: "PASS|FAIL|INCONCLUSIVE"
  blocking_criteria:
    total: <integer>
    pass: <integer>
    fail: <integer>
    inconclusive: <integer>
  required_scope_satisfied: true
  rationale: "<bounded verdict rationale>"

gate_record:
  gate: "PASS|FAIL|INCONCLUSIVE"
  exact_lineage:
    intention_revision: <revision>
    spec_revision: <revision>
    implementation_revision: <revision>
    candidate_refs:
      - "CR-001"
```

---

# 6. Spec Appendix Physical Contract

## 6.1 Path pattern

```text
appendices/spec/{appendix-id}.md
```

## 6.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "spec_appendix"
appendix_id: "A-001"
appendix_type: "SPEC"

owner_artifact:
  artifact: "spec"
  revision: <exact-owning-spec-revision>

status: "ACTIVE|SUPERSEDED"
---
```

## 6.3 Exact body structure

```markdown
# Spec Appendix — {appendix-id}

## 1. Purpose and Trigger

## 2. Scope

## 3. Related Canonical IDs

## 4. Detailed Technical Content

## 5. Context and Evidence References

## 6. Risks, Gaps, and Limitations

## 7. Backlink
```

### Required records

```yaml
purpose:
  trigger: "<registry trigger>"
  statement: "<why detail is separated>"

scope:
  included: []
  excluded: []

related_ids:
  criteria: []
  requirements: []
  invariants: []
  repositories: []
  tasks: []

references:
  context_refs: []
  evidence_refs: []

backlink:
  owner_artifact: "spec"
  owner_revision: <revision>
  registry_appendix_id: "A-001"
```

The appendix MUST NOT introduce an unregistered requirement, repository, criterion, or V&V obligation.

---

# 7. Implementation Repository Appendix Physical Contract

## 7.1 Path pattern

```text
appendices/implementation/{repo-id}.md
```

## 7.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "implementation_repository_appendix"
appendix_id: "A-101"
appendix_type: "IMPLEMENTATION_REPOSITORY"

repo_id: "<confirmed-repo-id>"

owner_artifact:
  artifact: "implementation"
  revision: <exact-owning-implementation-revision>

status: "ACTIVE|SUPERSEDED"
---
```

## 7.3 Exact body structure

```markdown
# Implementation Appendix — {repo-id}

## 1. Repository Disposition

## 2. Tasks

## 3. Candidate

## 4. Changed Paths and Migrations

## 5. Checks and Evidence

## 6. Deviations and Gaps

## 7. Backlink
```

### Required records

```yaml
repository_disposition:
  repo_id: "<repo-id>"
  required_action: "CHANGE|VERIFY_ONLY|NO_CHANGE"
  disposition: "READY|BLOCKED|SUPERSEDED"
  task_ids: []
  candidate_ref: "<CR-id-or-null>"
  evidence_refs: []

tasks: []

candidate:
  applicability: "APPLICABLE|NOT_APPLICABLE"
  candidate_ref_id: "<CR-id-or-null>"

changed_paths: []
migrations: []
checks: []
deviations: []
gaps: []

backlink:
  owner_artifact: "implementation"
  owner_revision: <revision>
  registry_appendix_id: "A-101"
```

For `CHANGE`, candidate applicability MUST be `APPLICABLE` and `candidate_ref_id` MUST resolve to the owning `implementation.md`. For `VERIFY_ONLY` / `NO_CHANGE`, candidate applicability MUST be `NOT_APPLICABLE`.

---

# 8. Evidence Appendix Physical Contract

## 8.1 Path pattern

```text
appendices/evidence/{evidence-id}.md
```

## 8.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "evidence_appendix"
appendix_id: "A-201"
appendix_type: "EVIDENCE"
evidence_id: "E-101"

owner_artifact:
  artifact: "correctness"
  revision: <exact-owning-correctness-revision>

status: "ACTIVE|SUPERSEDED"
---
```

## 8.3 Exact body structure

```markdown
# Evidence Appendix — {evidence-id}

## 1. Evidence Identity

## 2. Claim Mapping

## 3. Method and Environment

## 4. Observation

## 5. Integrity and Provenance

## 6. Limitations

## 7. Backlink
```

### Required records

```yaml
evidence_identity:
  evidence_id: "E-101"
  ref: "<immutable-evidence-ref>"
  revision_or_as_of: "<revision/time>"

claim_mapping:
  criterion_ids: []
  requirement_ids: []
  finding_ids: []

method_environment:
  method: "<method>"
  environment: "<environment-or-N/A>"

observation:
  statement: "<what was observed>"
  result: "PASS|FAIL|INCONCLUSIVE|OBSERVATION_ONLY"

integrity_provenance:
  integrity: "<digest/signature/governed-ref>"
  producer: "<producer/tool/system>"
  captured_at: "<timestamp>"

limitations: []

backlink:
  owner_artifact: "correctness"
  owner_revision: <revision>
  registry_appendix_id: "A-201"
```

An Evidence appendix records evidence; it MUST be registered in the owning `correctness.md` §2 `evidence_appendix_registry`, and it MUST NOT independently calculate the overall Correctness gate.

---

# 8.4 Cross-file Record Reuse Invariant

The physical profile MUST NOT redefine a Layer 1 shared structured record incompatibly.

The following records reuse the approved Layer 1 semantics:

```text
criterion
requirement
vv_disposition
task
candidate_ref
repository_disposition
EvidenceRef
criterion_verdict
ResolvedContextRef
```

A physical-only identifier such as `candidate_ref_id` or `context_ref_id` MAY be added solely to make cross-references addressable. Such an identifier does not change the semantic authority of the underlying record.

Every referenced `evidence_id`, `candidate_ref_id`, `appendix_id`, criterion ID, requirement ID, invariant ID, and task ID MUST resolve within the active OutputBundle or through an explicitly governed immutable reference.


# 9. Skill Read/Write Contracts

This section fixes what each canonical Skill MUST read and what it MUST produce physically.

## 9.1 T1

```text
AuthenticatedHumanSignal
        +
Resolved Context
        |
        v
T1 procedure
        |
        v
intention.md
```

| T1 reads | T1 uses it for | `intention.md` output |
| --- | --- | --- |
| Human Signal envelope/content | expressed need + authorization | §1 Human Signal |
| Human content | users/stakeholders | §2 Stakeholders |
| Human content | desired result | §3 Desired Outcome |
| Human content | intended use | §4 Intended-Use Scenarios |
| Human content + applicable constraints | boundary | §5 Scope and Non-Goals |
| Human content + Context | constraints/assumptions | §6 Constraints and Assumptions |
| authorized outcomes | measurable acceptance | §7 Success Criteria |
| product/system hints + Context | navigation seeds only | §8 Seeds |
| resolved Context | provenance | §9 Context Used |
| unresolved meaning/authority | blockers | §10 Open Questions |
| all above | gate calculation | §11 Gate Record |

## 9.2 T2

```text
intention.md
        +
Resolved Context
        |
        v
T2 procedure
        |
        +--> gathers/pins current Evidence during execution
        |
        v
spec.md + Spec appendices*
```

| T2 reads | T2 procedure | `spec.md` output |
| --- | --- | --- |
| Intention §7 Criteria | create technical obligations | §2 Mapping + §3 Requirements |
| Intention §3–§6 | preserve outcome/bounds | §3–§4 |
| Intention §8 Seeds | initialize discovery only | §6 Change Surface |
| Context refs | select constraints/navigation | §5, §6, §7, §11 |
| current Evidence | establish current applicability | §5 Current-State + §6 CONFIRMED/EXCLUDED |
| criteria + requirements | create work | §8 Tasks |
| criteria | design V&V | §9 V&V Plan |
| complex bounded design detail | allocate appendix | §10 Registry |
| all unresolved findings | classify/block | §12 Risks/Gaps |
| all above | gate calculation | §13 Gate Record |

## 9.3 T3

```text
spec.md
        +
Resolved Context
        |
        v
T3 procedure
        |
        +--> uses permitted repository capabilities during execution
        |
        v
ImplementationBundle
├── implementation.md
├── repo candidates*
└── implementation appendices*
```

| T3 reads | T3 procedure | `implementation.md` output |
| --- | --- | --- |
| Spec §6 Change Surface | determine per-repo action | §3 Dispositions |
| Spec §8 Tasks | execute approved work | §3, §6 |
| Spec §3–§4 obligations/design | implement | §5–§6 |
| repository state/Context | pin bases and local constraints | §4 Candidate Refs + §10 |
| produced candidates | record exact heads/paths | §4–§5 |
| implementation checks | record observations | §7 Checks |
| mismatch/new scope | classify deviation | §8 Deviations |
| repo-local detail | appendix if triggered | §9 Registry |
| execution topology | provenance only | §11 |
| unresolved evidence/gaps | T4 handoff | §12 |
| all above | gate calculation | §13 Gate Record |

## 9.4 T4

```text
intention.md
+ spec.md
+ implementation.md
+ exact candidate refs
+ Resolved Context
        |
        v
T4 procedure
        |
        +--> gathers/references independent Evidence during execution
        |
        v
correctness.md + evidence appendices*
```

| T4 reads | T4 procedure | `correctness.md` output |
| --- | --- | --- |
| exact lineage | pin evaluation target | §1 Exact Inputs |
| Spec §9 V&V plan | select required methods/scope | §3–§6 |
| Spec requirements | verify candidate conformance | §3 Verification |
| Intention scenarios/criteria | validate outcome | §4 Validation |
| independent Evidence | evaluate claims | §2–§5 |
| requirement/repo/task mappings | calculate coverage | §6 Coverage |
| evidence/scope gaps | limitations | §7 |
| release evidence if applicable | observe, not assume | §8 |
| findings | determine earliest return | §9 |
| Context | interpretation provenance | §10 |
| independent evaluation execution | provenance | §11 |
| all blocking verdicts + scope | gate calculation | §12 |

---

# 10. Canonical End-to-End I/O Matrix

```text
AuthenticatedHumanSignal
        |
        | T1-Intention-Skill
        | ; ResolvedContextRefs
        v
intention.md
        |
        | T2-Delivery-Spec-Skill
        | ; ResolvedContextRefs
        |   (gathers current Evidence during execution)
        v
spec.md
        |
        | T3-Implementation-Skill
        | ; ResolvedContextRefs
        |   (uses permitted repository capabilities)
        v
implementation.md
+ exact repo candidates
        |
        | T4-Correctness-Skill
        | ; ResolvedContextRefs
        |   (gathers/references independent Evidence)
        v
correctness.md
```

The canonical artifact chain remains:

```text
Human Signal
→ intention.md
→ spec.md
→ implementation.md
→ correctness.md
```

Appendices and side effects are subordinate OutputBundle members and do not add stages.

---

# 11. Agent Compliance Rules

A Layer 1 Agent producing a canonical Markdown artifact MUST:

1. use the exact required top-level section order from this profile;
2. preserve exact upstream revisions in frontmatter;
3. preserve stable IDs rather than renumbering for aesthetics;
4. emit required structured records in the declared sections;
5. include empty arrays / explicit `NOT_APPLICABLE` records instead of silently omitting required structure;
6. record materially influential `ResolvedContextRef` and `EvidenceRef` separately;
7. avoid inventing authority absent from the upstream artifact/source;
8. avoid using narrative prose to bypass structured gate fields;
9. allocate appendices only through the owning core artifact registry;
10. calculate only the gate owned by the current canonical transition.

A consumer Agent MUST reject or block on a canonical input when:

- required frontmatter is missing or inconsistent;
- the artifact's upstream reference does not match the expected lineage;
- the artifact is `STALE` or `SUPERSEDED`;
- the required previous gate is not satisfied;
- required structured sections/records necessary for the current transformation are missing;
- narrative and structured records materially conflict.

---

# 12. What This Profile Does Not Define

This profile does not define:

- how Product Assets / Layer 2 Context are physically represented;
- how `ResolvedContextRef` is selected by a runtime;
- actual `SKILL.md` contents for T1–T4;
- physical FDI repository root deployment;
- a Markdown parser or validator implementation;
- raw CI/evidence storage;
- repository branching/PR conventions;
- Agent/model assignment.

Those remain separate contracts.

---

# 13. Contract Review Result

The contract-level review for this profile is complete.

Resolved in this review:

1. Human Signal fragments now have stable physical IDs so criterion traceability is resolvable.
2. T2 and T3 now define exact `EvidenceRef` inventory locations.
3. T4 now registers governed Evidence appendices in the owning `correctness.md`.
4. `ResolvedContextRef` physical records now include the approved `evidence_backlink` field and explicit exclusions where required.
5. V&V disposition fields align with the approved Layer 1 shared record, including nullable/N/A semantics for authorized non-blocking observation.
6. `spec.md` covers configuration separately from data/schema.
7. `correctness.md` coverage now includes design invariants and tasks as required by Layer 1 traceability.
8. Criterion verdict records preserve the approved shared fields while adding physical finding references.
9. Execution-time Evidence and repository capabilities are no longer depicted as additional canonical inputs.
10. Candidate-reference physical identity is explicitly defined as addressability metadata, not new authority.

```text
Contract review: PASS
Open contract blockers: NONE IDENTIFIED
Herman design approval: APPROVED
```

---

# 14. Approval Checklist

Before this profile may be called `Contract-ready`, approve:

- [x] Common physical Markdown rules
- [x] Common canonical frontmatter
- [x] Exact `intention.md` heading order and section schemas
- [x] Exact `spec.md` heading order and section schemas
- [x] Exact `implementation.md` heading order and section schemas
- [x] Exact `correctness.md` heading order and section schemas
- [x] Spec appendix physical profile
- [x] Implementation repository appendix physical profile
- [x] Evidence appendix physical profile
- [x] Stable ID conventions
- [x] Required-section non-omission rule
- [x] Structured-record-over-narrative consistency rule
- [x] T1 input-to-output mapping
- [x] T2 input-to-output mapping
- [x] T3 input-to-output mapping
- [x] T4 multi-input-to-output mapping
- [x] Consumer rejection/blocking rules

Current state:

```text
Layer 1 semantic contract: APPROVED

Layer 1 Markdown I/O Profile v0.1:
Contract-ready: APPROVED
Execution-verified: NOT_CLAIMED
Validator implementation: NOT_AUTHORIZED_BY_THIS_DESIGN
```

---

# 15. Approval Record

```text
Approved by: Herman
Decision: APPROVE
Layer 1 Markdown I/O Profile v0.1: Contract-ready
Execution-verified: NOT_CLAIMED
Implementation authorization: NOT_GRANTED_BY_THIS_APPROVAL
```

This approval freezes the physical Markdown I/O contract unless a later approved revision supersedes it.

---

# 16. Completion Definition

After approval of this profile, Layer 1 will have all three required specification levels:

```text
A. Semantic Contract
   what each artifact means
   → APPROVED

B. Structured Record Contract
   what machine-readable records exist
   → APPROVED through Layer 1 + this profile

C. Physical Markdown I/O Contract
   exact headings, ordering, placement, and required empty-state behavior
   → APPROVED
```

At that point a conforming Agent can determine, without inventing structure:

```text
what canonical input to read
which exact sections/records are authoritative
which Context/Evidence references are dependencies
what procedure the Skill must perform
what exact Markdown structure to write
what gate it may calculate
what the next Skill is allowed to consume
```
