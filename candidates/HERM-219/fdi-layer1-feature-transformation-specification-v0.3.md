# Feature Delivery Intelligence Framework Design v0.3

## 1. Purpose and semantic model

FDI optimizes for correct feature delivery: discovering everything that must change, preserving authority and architectural consistency across repositories, producing traceable implementation work, and requiring evidence before claiming correctness.

```text
Layer 1 — Feature Execution
Human -> Intention -> Delivery Spec -> Change Set -> Verification & Validation Report
          FT-T1          FT-T2            FT-T3                    FT-T4

Layer 2 — Product Intelligence
governed Product Assets -> selective Context resolution -> FT-T1/FT-T2/FT-T3/FT-T4
```

Each Layer 1 arrow is one governed agent execution. Layer 2 maintenance workflows are separately governed; they are not a fifth Layer 1 transition and do not create feature artifacts. Context is selected for each execution and does not own a feature gate.

### Glossary

| Term | Definition | Authority boundary |
| --- | --- | --- |
| Human signal | Authenticated request, decision, correction, or approval with stable source identity | Owns expressed need and authorization, not technical feasibility |
| Intention | Authorized statement of why a change is needed, for whom, the outcome and expected behavior, scope, constraints, non-goals, and measurable criteria | Canonical desired-behavior authority |
| Context | Bounded set of governed information and executable procedure selected for one agent execution | Authority depends on source category; cannot silently replace an artifact |
| Product Asset | Durable, product-scoped, governed Layer 2 intelligence with ownership, provenance, trust, lifecycle, and publication state | Owns only its declared authority dimensions; never gains current-source authority by publication alone |
| Execution Context | Exact Product Asset leaves, source evidence, rules, Skill, and capability bindings resolved for one execution | Ephemeral selection record; not a Product Asset or feature artifact |
| Skill | Versioned executable procedure that declares inputs, outputs, Context selection, capability bindings, permissions, stopping, failure, and evidence | Procedure authority only; does not own product intent, schemas, or global workflow state |
| Tool/capability | Invoked capability bound by a Skill and execution environment | Performs an allowed operation; not a peer Context category |
| Delivery Spec | Implementable contract translating Intention into requirements, design, ChangeSurface, owners, tasks, risks, and V&V plan | Canonical technical-obligation authority, subordinate to Intention |
| Change Set | Reviewable source-repository candidates plus an aggregate mapping of exact bases/heads, paths, checks, owners, and deviations | Source repositories own candidate content; coordination repository owns aggregate traceability |
| Evidence | Claim-linked observation with method, origin, revision/environment, integrity, authority dimension, owner, limits, and lifecycle | Retains the authority of its origin; a copied reference does not transfer authority |
| Correctness | Independent verification of Spec conformance plus validation of fitness for Intention, per criterion and overall | Evidence-backed T4 verdict only; never inferred from implementation completion |

## 2. Layer 1 invariants

- The only canonical logical artifacts are Intention, Delivery Spec, Change Set, and Verification & Validation Report.
- Each logical artifact has one required Markdown core file. Governed appendices are conditional, bounded, registered by their core, and never own a gate.
- A simple feature may use only the four core files; no empty appendix placeholders are required.
- An appendix cannot introduce scope, change the owning core artifact's meaning, or authorize its own source reads.
- Every material claim records provenance, authority dimension, applicability, freshness, limitations, and exact backlinks.
- `CONTRACT_READY|NOT_CONTRACT_READY` is a preflight result, distinct from the output gate of a transition.
- `INTENTION_READY`, `SPEC_READY`, and `CHANGE_SET_READY` authorize only entry to the next transition at the exact pinned revision. They do not authorize merge, deployment, release, or publication.
- T4 `PASS` does not override source-repository review, release, deployment, or rollback policy.

## 3. Four-transition matrix

| Transition | Producer | Exact logical inputs | Exact physical inputs | Selected Context | Output bundle | Completion and existing gate | Required evidence | Failure and earliest re-entry |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FT-T1 Human -> Intention | Intention agent accountable to the authorizing Human | Authenticated Human signal and explicit authorization boundary | Stable Human-signal reference; no upstream feature file | Applicable Steering product/architecture rules, Domain vocabulary/rules, high-level Codebase index, reviewed Knowledge; exact FT-T1 Skill | `intention.md`; only triggered intention appendix registered by it | Outcome, expected behavior, scope/non-goals, constraints, criterion IDs, authorized sources, and material unknowns are reviewable; `INTENTION_READY`, else `BLOCKED` | Human-signal provenance, consulted Context selection/exclusion record, ambiguity resolutions | Ambiguous outcome, identity, authority, or material scope -> Human clarification and restart FT-T1 at affected section |
| FT-T2 Intention -> Delivery Spec | Accountable Spec agent; source-repository owners acknowledge local obligations | Exact `INTENTION_READY` revision; Feature Closure records are internal working records, not new canonical inputs | `intention.md` and registered intention appendices | Steering, Domain, Codebase registries/topology, pinned source/config/schema/tests, Operations, applicable published Product Assets, reviewed Knowledge/External, exact FT-T2 and closure Skills | `spec.md`; bounded Spec appendices including candidate repository, ChangeSurface, closure proposal/review, and safe evidence records | Every criterion maps to requirement, design obligation, owner, repository, task, and non-tautological V&V method; selectors pass; material candidates/edges have supported dispositions; independent closure review passes exact proposal; `SPEC_READY`, else `BLOCKED` | Current feature-specific pinned evidence, selector/concrete-match proof, repository-owner handshakes, closure proposal and independent review, Context/provenance records | Desired-outcome conflict -> FT-T1; stale/missing authority or selector failure -> FT-T2 preflight; missing surface/dependency -> earliest affected closure step; new material evidence -> supersede affected proposal/review and re-enter earliest affected FT-T2 step |
| FT-T3 Delivery Spec -> Change Set | Implementation agent plus accountable owners in every impacted source repository | Exact `SPEC_READY` revision and approved repository/task map | `spec.md` plus its registered appendices and exact source-repository local instructions | Exact repository projections, pinned source, tests/config/schema, Operations, active FT-T3 Skill and capability bindings | `implementation.md`, reviewable source-repository candidates, and bounded per-repository implementation appendices | Every impacted repository has a pinned reviewable candidate or evidence-backed no-change disposition; mappings/checks/deviations complete; `CHANGE_SET_READY`, else `BLOCKED` | Immutable base/head, changed paths/symbols, checks/results, PR/review refs, deviations, consulted Context/Skills | New repository/path/interface or Spec conflict -> stop before out-of-scope read/change and re-enter FT-T2; implementation defect -> FT-T3; unavailable permission/capability -> FT-T3 preflight |
| FT-T4 Change Set -> Verification & Validation Report | Verifier independent of FT-T3 implementation | Exact active Intention, Spec, Change Set, all candidate revisions, and V&V plan | `intention.md`, `spec.md`, `implementation.md`, registered appendices, pinned candidates | Pinned test/runtime evidence, Operations, applicable Steering/Domain/Product Assets, exact FT-T4 Skill; investigator identity/context independent from FT-T3 | `correctness.md` and bounded evidence appendices | Every criterion has verification and validation evidence or an explicit evidence gap; independence declared; overall `PASS|FAIL|INCONCLUSIVE` | Method, environment, revision, integrity, criterion backlinks, coverage, limitations, release observation or `NOT_OBSERVED` | Verification failure -> FT-T3; validation failure due intent/spec -> FT-T1 or FT-T2; missing/expired evidence -> FT-T4 after evidence becomes valid; changed candidate -> invalidate affected verdict and restart FT-T4 |

## 4. Logical-to-physical Markdown bundle

The framework uses abstract `{fdi-root}/features/{feature-id}`. Binding `{fdi-root}` to an exact coordination repository/ref and selecting YAML or JSON for typed appendix instances are Phase 0 deployment-profile decisions. Those choices are non-semantic and may not alter artifact ownership, fields, limits, or gates.

| Logical item and physical pattern | Trigger and finite bound | Producer / owner | Consumers | Authority | Provenance, freshness, supersession | Required mappings and completion contribution |
| --- | --- | --- | --- | --- | --- | --- |
| Intention: `{feature-root}/intention.md` | Always; exactly one active revision | FT-T1 agent / authorizing Human for desired behavior | FT-T2, FT-T4, product review | Desired behavior | Authenticated signal, artifact revision, as-of time; later authorized revision supersedes | Signal fragments -> criteria; Context consulted/excluded; owns sole `INTENTION_READY` record |
| Delivery Spec: `{feature-root}/spec.md` | Always; exactly one active revision | FT-T2 Spec agent / coordination repository with source-owner acknowledgement | FT-T3, FT-T4, repo owners | Technical obligations subordinate to Intention | Exact Intention revision; pinned evidence/Product Asset/Skill refs; newer Intention or material source change invalidates affected claims | Criterion -> requirement/design/owner/repo/task/V&V; appendix registry; owns sole `SPEC_READY` record |
| Change Set: `{feature-root}/implementation.md` | Always; exactly one aggregate record per active Spec/candidate set | FT-T3 agent / coordination repository for aggregate, source repos for changes | FT-T4, repo reviewers, delivery/release owners | Aggregate mapping only; source repos retain source/review authority | Exact Spec, base/head and observed checks; changed head/Spec/check validity supersedes affected rows | Requirement/task -> repo/path/symbol/candidate/check/deviation; owns sole `CHANGE_SET_READY` record |
| Correctness: `{feature-root}/correctness.md` | Always for FT-T4; exactly one active report per candidate set | Independent FT-T4 verifier / verifier owns verdict | Human approver, repo/release owners, audit/re-entry | Independent V&V verdict | Exact Intention/Spec/Change Set/candidates/environment/method; changed input or expired evidence invalidates affected verdict | Criterion -> verification + validation evidence + verdict; owns `PASS|FAIL|INCONCLUSIVE` |
| General Spec appendix: `{feature-root}/appendices/spec/{appendix-id}.md` | Separate owner or material interface/data/security/migration/design section cannot remain reviewable in core; IDs preallocated in `spec.md`; count <= registry maximum | FT-T2 contributor / `spec.md` owner controls registry; domain owner retains subject authority | FT-T3, FT-T4, relevant owners | Only declared technical/rationale dimension | Exact source refs, owner, review/freshness, successor; core marks supersession | Backlink both directions; cannot add scope or a gate; complete only when registry metadata and owner review satisfy trigger |
| Candidate repository appendix: `{feature-root}/appendices/spec/feature-closure/candidate-repo-set.{yaml|json}` | Closure invoked; one active `CandidateRepoSet`; candidates <= declared `max_candidate_repositories` | `repo-discovery` / Spec agent | Investigation, closure, review, Spec finalization | Discovery record, not current truth | Exact `IntentSpec`, registries/Product Assets, timestamps/pins; new intent or discovery evidence creates new revision | Candidate -> introduction source/rationale/state/evidence/limits; maps into Spec impacted-repository analysis |
| ChangeSurface appendix: `{feature-root}/appendices/spec/feature-closure/change-surface-set.{yaml|json}` | Current investigation required; one active `ChangeSurfaceSet`; surfaces <= passed selector/cap totals | `changesurface-investigation` / Spec agent plus source owners for current findings | Dependency closure, review, Spec finalization, FT-T3/T4 | Current-state mapping only when supported by current evidence | Immutable repo/path/symbol pins and evidence; changed pin or evidence invalidates affected surfaces | Surface -> criterion/obligation/owner/dependencies/evidence/disposition; maps into Spec change surface |
| Closure proposal appendix: `{feature-root}/appendices/spec/feature-closure/closure-package.{yaml|json}` | Dependency closure invoked; one immutable proposal revision per evidence set; nodes/edges/selectors within declared caps | `dependency-closure` / Spec agent owns incorporation, producer owns proposal | Independent reviewer, Spec finalizer | Bounded closure claim only | Pins, selector proofs, source/contract/Skill versions; new material evidence creates a superseding proposal, never in-place rewrite | Candidate/surface/edge/interface/validation/exclusion/unknown disposition; status `OPEN|PARTIAL|CLOSED_WITHIN_DECLARED_SCOPE`; cannot set `SPEC_READY` |
| Closure review appendix: `{feature-root}/appendices/spec/feature-closure/closure-review.{yaml|json}` | Closure workflow invoked; one review per exact proposal/draft tuple; review count <= declared retry cap | Independent `closure-review` / reviewer owns verdict | Spec finalizer, audit/re-entry | Review evidence only | Exact reviewed proposal and optional draft Spec revisions, identities, evidence; superseded when reviewed input changes | Omissions/unsupported claims/unresolved edges/selector failures -> exact re-entry; `PASS|FAIL|INCONCLUSIVE`; cannot rewrite proposal or set a gate |
| Implementation appendix: `{feature-root}/appendices/implementation/{repo-id}.md` | More than one impacted repo or independently owned local execution; at most one active appendix per approved impacted `repo-id` | Repo-local FT-T3 owner / source repository owner | Aggregate FT-T3, FT-T4, reviewers | Repository-local implementation/review evidence | Exact Spec/base/head/local instructions/checks; changed head supersedes | Local obligations -> paths/candidates/checks/deviations; backlink to `implementation.md`; no independent gate |
| Evidence appendix: `{feature-root}/appendices/evidence/{evidence-id}.md` | Claim needs governed safe evidence beyond URI/digest row; IDs preallocated by owning core; count <= declared `max_evidence_records` | Evidence producer / origin owner retains authority; coordination repo stores safe reference/interpretation | Any explicitly backlinked core/appendix | Origin authority dimension only | Method, immutable/timestamped origin, revision/environment, digest, expiry/supersession | Exact claim and consumer backlinks; no raw secrets, copied trees, unsafe local paths, or gate authority |

All appendix selectors declare allowed path template, ID derivation, producer, owner, authority, consumers, exclusions, zero-match behavior, positive finite count/byte caps, completion, and owning-core backlink before creation. Excess always blocks. An unregistered repository or mutable ref never satisfies a selector.

## 5. Core Markdown contracts

### `intention.md`

Required sections: artifact identity/version/revision; authenticated Human signal and safe provenance; feature identity; stakeholders/users; outcome and expected behavior; intended-use scenarios; scope and non-goals; constraints/assumptions; stable criterion IDs and acceptance signals; authorized sources; product/system/repository seeds explicitly marked as non-authorizing hints; Context consulted/excluded; explicit unknowns/conflicts; supersession; gate record.

Complete only when every requested outcome maps to a criterion, intended behavior is reviewable, authorization is known, non-goals and constraints are explicit, and no unresolved ambiguity materially changes the desired outcome. Inferred repository scope is prohibited.

### `spec.md`

Required sections: artifact identity and exact Intention revision; criterion mapping; functional/quality requirements; design/invariants; current-state assumptions and evidence; ChangeSurface and impacted repository map; interface/data/security/operations/deployment/rollout/rollback obligations as applicable; ownership/task plan; V&V methods/evidence destinations/thresholds/independence; appendix registry and bounds; Context/selector/concrete-match proof; exclusions/unknowns/risks/conflicts; closure proposal and independent review backlinks; source/contract/Skill versions; re-entry/invalidation; supersession; sole gate record.

Complete only when the FT-T2 row in the transition matrix is satisfied. Feature Closure contributes evidence; the accountable Spec agent alone finalizes the core. `SPEC_READY` is forbidden for `OPEN`, material `PARTIAL`, review `FAIL|INCONCLUSIVE`, invalid selectors/provenance, unresolved material edges, stale Intention, or unmapped criteria.

### `implementation.md`

Required sections: artifact identity and exact Spec revision; candidate summary; each repository's immutable base/head, branch/PR, owner, status; changed paths/symbols/migrations; requirement/design/task mappings; checks and observed results; deviations and blocking dispositions; appendix registry; Context/Skills/capabilities actually used; known gaps; independent V&V handoff; supersession; gate record.

Complete only when every impacted repository has a reviewable candidate or supported no-change rationale, mappings/checks exist, deviations are dispositioned, and exact ownership/revisions are pinned. `CHANGE_SET_READY` means ready for independent FT-T4 only.

### `correctness.md`

Required sections: artifact identity; independent verifier identity/declaration; exact Intention/Spec/Change Set/candidate inputs; evidence inventory/integrity; verification findings; validation findings; per-criterion verdicts; requirement/design/task/repository coverage; deviations/gaps/limitations; release observation or `NOT_OBSERVED`; earliest re-entry and owner; Context/Skills/capabilities used; supersession; overall verdict.

Complete only when every criterion has evidence or an explicit evidence gap and verification and validation are distinct. `PASS` requires every blocking criterion to pass; `FAIL` means at least one blocking criterion fails; `INCONCLUSIVE` means required evidence/capability is unavailable or insufficient.

## 6. Context taxonomy, authority, and loading

Layer 1 resolves Product and Architecture Product Assets through the Steering authority category. Other Product Asset families project into the matching Context category; the Layer 2 family and Layer 1 authority category remain distinct concerns.

| Context category | Owns | Must not own | Required use |
| --- | --- | --- | --- |
| Steering | Product direction, architecture constraints, technology policy, repository organization, delivery/governance rules | Current inventory or transient feature scope | Small applicable core for all transitions |
| Codebase | Curated current-system topology and navigation to pinned source | Desired behavior or planned relations | Index first; exact repo/component projections and bounded current source for FT-T2-FT-T4 |
| Domain | Vocabulary, business/regulatory rules and invariants | Implementation design | FT-T1/FT-T2 when applicable; mapped rules for FT-T3/FT-T4 |
| Operations | Environments, release controls, observability, runtime/data constraints | Product intent or source truth | Select by environment/release impact for FT-T2-FT-T4 |
| Knowledge | Reviewed decisions, incidents, patterns, history, and memory | New obligations, current topology, unreviewed chat/notes | Retrieval only after applicability/trust/freshness/successor checks |
| External | Third-party standards/vendor/reference material | Internal authority or mutable instructions | Retrieval only after trust/version/expiry checks |
| Skills | Executable procedures and capability/permission bindings | Credentials, tool implementations, product intent, schemas, global workflow state | Exact version/digest selected per execution |

Authority is dimensional:

1. Desired behavior: latest authorized Intention.
2. Technical obligations: latest approved Spec, subordinate to Intention.
3. Durable constraints: applicable Steering and Domain sources.
4. Current behavior: pinned source/config/schema/tests and revision/environment-tied observations.
5. Procedure: active Skill and permitted capability bindings.
6. Rationale/support: reviewed Knowledge and governed External references.

Every material Context selection records locator, immutable revision or as-of time, digest, claim/purpose, owner/producer, authority dimension, trust/review state, applicability/selection reason, environment, freshness/expiry, lifecycle, successor, exclusions, conflicts, and consumer backlink.

Loading sequence is mandatory: load minimal indexes/rules; select by applicable IDs; validate owner/status/freshness/successor; resolve exact leaf; then, only with a passed selector, enumerate names at an immutable repository pin before bounded content reads. Never bulk-load all repositories, all history/Knowledge, raw chat, unrelated evidence, generated/vendor/cache trees, or evaluation answers. A genuine unresolved authority conflict blocks only dependent claims and is never silently resolved for convenience.

Baseline is a trust-qualified snapshot supporting Codebase or Knowledge. Newer pinned source/config/schema/tests and environment-tied observations outrank it for current behavior. History and memory are reviewed Knowledge, never current truth by themselves.

## 7. Multi-repository ownership and handshakes

| Concern | Coordination repository | Source repository | Required handshake |
| --- | --- | --- | --- |
| Product intent | Canonical Intention and cross-product traceability | Feasibility evidence | Product authorization plus impacted owner acknowledgement |
| Cross-repository Spec | Aggregate requirements/design/sequence/ownership/V&V | Local constraints, interfaces, design review | Every impacted `repo-id`, owner, obligation, revision, and dependency registered in `spec.md` |
| Source/config/schema/tests | Pinned refs and safe summaries only | Canonical content and repository-local rules | Registry-validated repository plus immutable SHA and passed bounded selector |
| Change Set | Aggregate candidate map and ordering | Commits/branches/PRs/CI/review | One candidate/no-change disposition per approved repository; local owner accepts mappings |
| Interface/data/event changes | Cross-repo dependency and compatibility contract | Producer/consumer schemas, migrations, tests | Both producer and consumer owners acknowledge version/rollout/rollback/validation obligations |
| Evidence | Safe claim mapping, URI/digest, access conditions | Raw owned artifacts | Origin authority, revision/environment, method, integrity, and expiry preserved |
| Release/rollback | Cross-repo plan and observed state | Authorization and execution | Aggregate gate never bypasses local release/deploy/rollback controls |

A new repository or path discovered after a selector passes cannot authorize its own read. Investigation stops, records the candidate and evidence, validates registry/ownership/pin, creates a new bounded selector, and re-enters FT-T2 at selector preflight. FT-T3 makes the same stop-and-re-enter handoff before out-of-scope reading or changes.

## 8. Traceability, gates, and invalidation

Every independently verifiable criterion supports bidirectional navigation:

```text
Human signal fragment
  -> Intention criterion
  -> Spec requirement/design/owner/task/repository
  -> pinned repository:path#symbol@candidate-sha
  -> evidence claim/backlink
  -> verification and validation finding
  -> criterion verdict
```

Missing links block the affected criterion. A no-code result requires evidence and owner acknowledgement.

New material evidence reopens the earliest affected step: intent evidence -> FT-T1; discovery/selector/current-source/dependency evidence -> corresponding FT-T2 step; candidate implementation evidence -> FT-T3; V&V-only evidence -> FT-T4. Superseding a proposal invalidates its review; superseding a Spec invalidates dependent Change Sets; changing a candidate invalidates dependent correctness findings. Revalidation is dependency-scoped when materiality can be proven, otherwise the enclosing transition re-runs.

`Execution-verified: NOT_CLAIMED` remains mandatory for this design bundle because none of these transitions or gates has executed.

