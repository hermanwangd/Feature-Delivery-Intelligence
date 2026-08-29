# FDI Workflow Semantics v0.1

**Status:** Approved semantic baseline · **Date:** 2026-08-29

## Purpose

Feature Delivery Intelligence (FDI) is a lightweight semantic framework for
frontier engineering teams to build their own agentic feature-delivery
workflows. It defines the minimum meaning of the workflow, its artifacts, and
its correctness loop. It does not prescribe an orchestration product, storage
layout, or universal process.

The framework optimizes for correct feature delivery: preserving the original
outcome through planning and implementation, then producing evidence that the
delivered result both conforms to the plan and works for its intended use.

In this document, **must** identifies a semantic obligation. It does not imply a
particular schema, file, tool, approval gate, or automation mechanism.

An adopted team profile may specialize these semantics with concrete storage,
schemas, selectors, Skills, and gates. The companion
[FDI Context Taxonomy and Markdown Contract v0.1](./2026-08-29-fdi-context-taxonomy-design.md)
is one such optional profile. Its concrete layout is binding only for a
repository that adopts that profile; it does not add a canonical artifact,
change the four-artifact flow, or make this semantic baseline storage-specific.
Profile-local paths, Markdown schemas, status vocabularies, authorization
roles, anchors, and gates are not additional conformance requirements of FDI
Workflow Semantics v0.1.

## Core model

The canonical forward flow is:

```text
Human --agent--> Intention --agent--> Delivery Spec --agent--> Change Set --agent--> Verification & Validation Report
             \_________________________ Team Context supports every agent execution _________________________/
```

Each arrow is an agent execution. The first execution consumes a Human signal;
each later execution consumes the completed artifact from the preceding step.
Every execution also consumes relevant current Team Context and produces or
revises exactly one logical artifact to its right. The executions may use the
same agent or different agents. FDI does not prescribe agent identities,
prompts, models, runtimes, or autonomy levels.

The four named outputs are the canonical artifacts:

1. Intention
2. Delivery Spec
3. Change Set
4. Verification & Validation Report

The human request starts the flow but is not itself a canonical artifact.
Context is cross-cutting support for every execution, not a fifth step or an
additional feature artifact.

The forward flow is not a one-way waterfall. A failed or inconclusive
correctness assessment may return work to Intention, Delivery Spec, or Change
Set. The corrected artifact and all affected downstream artifacts are then
re-evaluated.

## Team Context

### Definition

**Team Context** is a team-owned, continuously maintained asset containing the
knowledge and constraints agents need to make changes consistent with the team
and the real system. It includes, as relevant:

- team constitution, steering, product principles, and decision rules;
- architecture, interface, security, quality, and engineering rules;
- the codebase, deployed or otherwise current system state, and known system
  boundaries;
- development history, decisions, incidents, and prior delivery evidence; and
- available tools and relevant external knowledge.

Context is broader and longer-lived than any one feature. Teams improve it as
the system and their understanding evolve. Every execution uses the relevant
current Context, but v0.1 does not require all Context to be loaded at once or
stored in one place.

### Support for every transition

| Agent transition | Prior input | How Context supports the execution |
| --- | --- | --- |
| Human → Intention | Human change intent and available stakeholder information | Supplies product purpose, vocabulary, constraints, system history, and known realities so the agent can turn a request into an outcome definition rather than merely restate it. |
| Intention → Delivery Spec | Completed Intention | Supplies architecture and engineering rules, interfaces, codebase and system state, prior decisions, and relevant tools so the agent can discover the complete change surface and produce a feasible plan. |
| Delivery Spec → Change Set | Completed Delivery Spec | Supplies the current code and configuration, implementation conventions, dependency state, test practices, and development history so the agent can create a consistent product candidate. |
| Change Set → Verification & Validation Report | Intention, Delivery Spec, Change Set, planned checks, and collected evidence | Supplies expected environments, quality rules, operational knowledge, tools, and current system behavior so the agent can interpret evidence without losing either specification conformance or intended use. |

An execution may expose missing, stale, or contradictory Context. The team
should correct durable Context when that knowledge will matter again. Such a
correction does not turn Context into a workflow stage and does not replace
repairing an affected feature artifact.

## Transition semantics

The canonical arrows establish semantic handoffs, not required process gates.

1. The producing execution must make its output traceable to the prior artifact
   and must disclose unresolved gaps that affect the next execution.
2. The consuming execution must use the prior artifact as an obligation, not as
   untrusted prose to silently reinterpret. If it finds a material defect, it
   routes the work backward instead of hiding the defect in a downstream
   artifact.
3. Current Context constrains every execution. Context may clarify an artifact,
   but it must not silently override an explicit feature decision. A conflict
   must be surfaced and reconciled.
4. Artifact completion means the artifact meets its contract below. It does not
   require a particular reviewer, workflow status, or storage representation.

### Shared artifact identity and provenance

Every canonical logical artifact identifies:

- its artifact type and version or revision;
- its producer;
- the Human signal or the version of each prior artifact used as input; and
- the key Context sources that materially shaped the output.

This is a semantic provenance obligation, not a prescribed metadata envelope.
A team may satisfy it through prose, version control, issue fields, a file
header, or another reviewable representation. It does not require a Context
manifest, artifact ledger, universal identifier, or universal schema.

## Canonical artifact contracts

### 1. Intention

#### Purpose

Intention defines the change from the stakeholder and intended-use point of
view. It establishes why the change is needed, who needs it, and what outcome
must become true. It is the validation anchor for the entire delivery flow, not
a preliminary technical solution.

#### Inputs

- the Human signal: a request, problem, opportunity, feedback, or desired
  change;
- available stakeholder and user knowledge;
- known intended-use scenarios and operating conditions;
- relevant Team Context, including product principles, current behavior,
  constraints, domain rules, strategy, and prior decisions; and
- human clarification when material ambiguity cannot be resolved from the
  signal and Context.

#### Output

One logical Intention artifact, with the shared identity and provenance, that
defines the outcome contract below.

#### Minimum contents

- rationale: the problem or opportunity and why it matters;
- affected stakeholders or users;
- the outcome that must become true;
- representative intended-use scenarios and relevant operating conditions;
- in-scope and out-of-scope behavior;
- constraints and assumptions;
- explicit non-goals;
- measurable success criteria stated from the stakeholder or user point of
  view; and
- material unresolved questions, if any, with their effect on scope or
  downstream decisions.

The success criteria play the role of measures of effectiveness: they express
how stakeholders will decide whether the outcome succeeds. They should measure
the result in use, not merely whether implementation tasks were completed.

#### Completion condition

Intention is complete when:

- the intended outcome is clear enough to distinguish success from failure;
- stakeholders, intended use, scope, non-goals, constraints, assumptions, and
  measurable success criteria are explicit;
- no unresolved question would materially change the desired outcome; and
- the human or an authorized team workflow policy confirms that Delivery Spec
  work may begin.

This confirmation is a semantic authorization to proceed. v0.1 does not
prescribe who performs it or how a team records or automates it.

### 2. Delivery Spec

#### Purpose

Delivery Spec translates Intention into an actionable and reviewable delivery
contract. It defines what the system must do, how the change fits the system,
what work is required, and how conformance will be demonstrated.

Delivery Spec is **one logical artifact**. A team may represent it as one file,
a bundle of files, an issue hierarchy, or another reviewable form. v0.1 does not
standardize that physical representation.

#### Inputs

- the completed Intention;
- relevant Team Context, especially the current codebase and architecture,
  interfaces and contracts, engineering standards, ADRs and history,
  dependencies, deployment and operational constraints, and available tools;
- focused investigation needed to understand affected components, interfaces,
  dependencies, and delivery constraints.

#### Output

One logical Delivery Spec artifact, with the shared identity and provenance,
that combines the requirements, design, tasks, and correctness plan below.

#### Minimum contents

- required functional and non-functional behavior, with acceptance criteria
  traceable to the Intention;
- affected system areas, repositories, interfaces, dependencies, and other
  system boundaries;
- a technical design covering behavior, components, interfaces, data,
  configuration, infrastructure, migration needs, operational concerns, and
  cross-boundary effects as applicable;
- an ordered implementation task breakdown, including dependencies and all
  required code, configuration, infrastructure, schema, migration, test, and
  documentation work;
- a verification and validation plan mapping each in-scope requirement,
  material design obligation, and Intention success criterion to planned
  methods, execution conditions, and expected evidence; and
- identified risks, assumptions, unknowns, explicit exclusions, and
  intentionally deferred work that affect delivery correctness.

These are logical content obligations. They do not require separate
`requirements.md`, `design.md`, or `tasks.md` files, nor do they prohibit those
files.

#### Completion condition

Delivery Spec is complete when:

- every Intention success criterion maps to requirements and planned evidence;
- its requirements, design, tasks, and verification and validation plan are
  mutually consistent and traceable to the Intention;
- the implementation agent can proceed without inventing product outcomes or
  major technical decisions;
- material interfaces, dependencies, risks, and unknowns are addressed or
  explicitly declared;
- its tasks are actionable and dependency-aware; and
- no unresolved question would materially change what must be implemented.

### 3. Change Set

#### Purpose

Change Set is the buildable and reviewable product candidate that realizes the
Delivery Spec. It is the actual system change, not a description of work that
might be performed.

#### Inputs

- the completed Delivery Spec and its verification and validation plan;
- the original Intention for outcome awareness;
- relevant Team Context and the current state of every affected system or
  repository, including applicable historical patterns and target
  environment; and
- the implementation and test tools needed to produce the candidate.

#### Output

One logical Change Set, with the shared identity and provenance, containing the
product candidate and producer-side evidence below.

#### Minimum contents

- the actual code, configuration, infrastructure, schema, migration, test, and
  documentation changes required by the Delivery Spec, as applicable;
- a coherent product candidate that can be built, exercised, and reviewed;
- a mapping from implemented work to the Delivery Spec;
- producer-side build, test, and other required check results, including the
  relevant execution conditions;
- any generated or operational artifacts necessary to evaluate that candidate;
- every known deviation, unfinished item, or newly discovered constraint, with
  its reason and expected effect on the Delivery Spec, intended use,
  verification and validation, or risk; and
- for every deviation, a stable deviation ID linked to one proposed
  disposition: a corrected Change Set, an authorized Delivery Spec revision,
  an authorized waiver/risk acceptance, or a corrective action with owner and
  status. The Change Set also records a proposed blocking state for independent
  assessment.

An undeclared deviation is a defect in the Change Set's traceability. A declared
deviation is not automatically acceptable. Before independent verification and
validation begins, every known deviation must be declared and linked to its
proposed disposition. An unresolved deviation may be assessed and reported;
the V&V Report determines its blocking classification and final disposition.
An unresolved blocking deviation prevents a `PASS` verdict but does not prevent
a complete `FAIL` or `INCONCLUSIVE` report.

#### Completion condition

Change Set is complete when:

- required implementation work is complete, or every exception is declared as
  a deviation and linked to a proposed disposition;
- the candidate is buildable and reviewable in the intended environment;
- required producer-side checks have been run and their results captured;
- there are no silent or proposed-disposition-free deviations from the
  Delivery Spec; and
- the Change Set is ready for independent verification and validation.

Completion here means ready for correctness assessment, not already proven
correct.

### 4. Verification & Validation Report

#### Purpose

The Verification & Validation Report is the evidence-backed correctness
assessment for the candidate.

- **Verification** asks: *Does the Change Set conform to the Delivery Spec?*
- **Validation** asks: *Does the delivered result satisfy the original
  Intention in its intended use?*

Verification protects the integrity of the technical delivery contract.
Validation protects the integrity of the stakeholder outcome. Passing one does
not imply passing the other: a candidate can implement an incorrect spec
perfectly, or satisfy an observed scenario while violating required system
behavior.

#### Inputs

- the completed Intention, including intended-use scenarios and measurable
  success criteria;
- the completed Delivery Spec, including requirements, design obligations,
  tasks, and verification and validation plan;
- the completed, exact Change Set being assessed;
- evidence independently generated or reproduced through tests, analysis,
  inspection, demonstration, operation, or other appropriate methods; and
- relevant Team Context, including environments, tools, quality rules, and
  current system behavior.

#### Output

One logical Verification & Validation Report, with the shared identity and
provenance, containing the separate assessments, evidence record, verdict, and
disposition below.

#### Minimum contents

- identification of the Intention, Delivery Spec, and exact Change Set assessed;
- verification results mapped to applicable requirements and material design
  obligations, including method, evidence, and result;
- validation results mapped to intended-use scenarios and measurable success
  criteria, including environment, evidence, and result;
- evidence sources and the execution conditions needed to interpret them;
- known deviations, anomalies, untested conditions, missing evidence, and other
  gaps, including each deviation's confirmed disposition and blocking
  classification;
- the impact and final or required disposition of each material gap; and
- one overall verdict: `PASS`, `FAIL`, or `INCONCLUSIVE`, with a rationale and
  the required next step when the verdict is not `PASS`.

Teams may record finer-grained results, but the canonical report still carries
one overall verdict:

- `PASS`: sufficient evidence shows both Delivery Spec conformance and
  satisfaction of the Intention, with no unresolved material gap or blocking
  deviation; every remaining non-blocking deviation has an explicit final
  disposition.
- `FAIL`: sufficient evidence shows that at least one required conformance or
  Intention criterion is not met.
- `INCONCLUSIVE`: available evidence is insufficient, unavailable, invalid, or
  ambiguous, so neither `PASS` nor `FAIL` is justified.

#### Completion condition

The report is complete when all in-scope verification and validation claims
have an explicit result or are marked inconclusive with the missing evidence
stated; verification and validation results are recorded separately; evidence
is sufficient to support the verdict and is not based solely on the
implementation agent's claims; limitations and gaps are disclosed; and the
verdict and required next step follow from that record. `PASS` is permitted only
when no material failure, unresolved gap, or blocking deviation remains within
the evaluated scope. A complete report may still return `FAIL`
or `INCONCLUSIVE` while such a blocker remains.

Report completion does not mean delivery success: a complete report may
correctly conclude `FAIL` or `INCONCLUSIVE`.

## Correctness feedback and re-entry

When the report is `FAIL` or `INCONCLUSIVE`, it identifies the required next
step. Work returns to the earliest artifact whose correction can resolve the
finding, or to evidence collection when the artifacts remain sound:

| Re-entry target | Use when | Examples |
| --- | --- | --- |
| Intention | The desired outcome, stakeholder, intended-use scenario, scope, constraint, or success measure is wrong, missing, or too ambiguous to validate. | A technically correct feature solves the wrong user problem; a success criterion cannot distinguish success from failure. |
| Delivery Spec | Intention is sound, but its translation into requirements, design, tasks, or the verification and validation plan is incomplete, inconsistent, or incorrect. | A cross-repository dependency is absent; acceptance criteria do not cover an intended-use scenario. |
| Change Set | Intention and Delivery Spec are sound, but the candidate is defective, incomplete, nonconforming, or lacks required implementation evidence. | A migration is missing; behavior differs from a requirement; a test fails. |
| Evidence collection and reassessment | The artifacts are sound, but evidence is unavailable, invalid, ambiguous, or was not independently generated or reproduced. | A required environment was unavailable; a producer-reported result must be reproduced. |

After correction, all affected downstream artifacts must be regenerated,
updated, or re-assessed. A finding must not be closed by changing only the
report. Evidence collection is not another canonical artifact or workflow
stage. An `INCONCLUSIVE` result caused solely by unavailable evidence may be
re-assessed after obtaining valid evidence without changing a prior artifact;
if the missing evidence exposes a planning gap, work returns to Delivery Spec.

The correction may also reveal reusable knowledge that belongs in Team Context.
Updating Context improves future executions but does not remove the need to
correct and re-assess the current feature artifacts.

## Semantic invariants

Any team-specific workflow claiming compatibility with FDI Workflow Semantics
v0.1 preserves these invariants:

1. It produces the four canonical logical artifacts, even if their physical
   representation or names differ.
2. Each artifact identifies its version, producer, prior input, and materially
   influential Context sources without requiring a universal metadata schema.
3. Every forward transition is an agent execution informed by relevant current
   Team Context and produces one logical artifact.
4. Intention remains the validation anchor; Delivery Spec does not replace it.
5. Delivery Spec remains one logical artifact containing requirements, design,
   tasks, and the verification and validation plan.
6. Change Set is an assessable product candidate, records producer-side checks,
   and links every declared deviation to a proposed disposition and proposed
   blocking state before V&V.
7. Verification is assessed against Delivery Spec; validation is assessed
   against Intention and intended use.
8. The final report uses independently generated or reproduced evidence and
   carries `PASS`, `FAIL`, or `INCONCLUSIVE`.
9. Failed or inconclusive assessment can re-enter Intention, Delivery Spec, or
   Change Set, based on the source of the gap, or collect missing evidence when
   those artifacts remain sound.
10. Context remains a cross-cutting team asset, not a feature-workflow step.

## Reference model mapping

FDI adopts concepts selectively. The referenced products are practical models,
not required implementations.

| Adopted concept | Primary reference model | FDI v0.1 use and boundary |
| --- | --- | --- |
| Identified artifact versions, inputs, and traceable evidence | [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), §§4.1, 5.3.1.3, and 5.4.1.3 | NASA's bidirectional traceability and report-version records inform FDI's lightweight provenance rule. FDI additionally identifies the producer and materially influential Context sources without prescribing a metadata envelope. |
| Stakeholder-centered outcome, intended use, and measurable success | [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), §§4.1 and 4.2 | Intention adopts stakeholder expectations, intended-use scenarios, constraints, and measures of effectiveness as the basis for outcome definition. FDI scales the concepts to feature delivery rather than adopting NASA's full lifecycle. |
| A practical proposal that explains why a change is needed | [OpenSpec spec-driven schema](https://openspec.dev/docs/schemas/spec-driven), `proposal.md` | OpenSpec's proposal is the practical analogue for the rationale and high-level scope in Intention. FDI Intention adds explicit stakeholders, intended use, non-goals, and measurable success criteria. |
| Requirements, technical design, and executable tasks as a structured delivery specification | [Kiro Specs](https://kiro.dev/docs/specs/) | Kiro's requirements/design/tasks structure is the primary practical model for Delivery Spec contents. FDI treats them as one logical artifact and adds an explicit verification and validation plan without prescribing Kiro's three-file layout. |
| Agentic progression from what/why through design, tasks, quality checks, and implementation | [GitHub Spec Kit quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) | Spec Kit's `specify → clarify → plan → checklist → tasks → analyze → implement → converge` flow informs traceable agent handoffs, ambiguity checks, dependency-aware tasks, and consistency assessment. FDI defines semantic outputs rather than commands or gates. |
| Persistent team rules and selectively supplied project knowledge | [Kiro Steering](https://kiro.dev/docs/steering/) and [Kiro Context Management](https://kiro.dev/docs/cli/chat/context/) | Team Context adopts the idea that durable standards and relevant project knowledge inform agent work across sessions. FDI broadens Context to current system state, history, tools, and external knowledge while leaving retrieval and storage team-specific. |
| Build execution against planned tasks and convergence back to the specification | [OpenSpec spec-driven schema](https://openspec.dev/docs/schemas/spec-driven) `apply`, and [GitHub Spec Kit quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) `implement`/`converge` | These models inform the transition from Delivery Spec to Change Set and iterative closure of implementation gaps. FDI additionally requires declared deviations and permits re-entry to earlier artifacts. |
| Distinct verification and validation questions | [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), §§5.3 and 5.4 | FDI adopts verification against requirements/specification and validation against stakeholder expectations in intended use. |
| Evidence-bearing verification and validation reports with discrepancies and dispositions | [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), §§5.3.1.3 and 5.4.1.3 | FDI combines both evidence sets into one logical report. `PASS` and `FAIL` align with recorded outcome declarations; `INCONCLUSIVE` is an FDI extension that prevents an unsupported success or failure claim. |
| Reassessment when artifacts conflict or evidence exposes gaps | [GitHub Spec Kit quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) `analyze`/`converge`, together with NASA bidirectional traceability | FDI generalizes consistency and convergence into explicit re-entry to the earliest defective artifact, including Intention when validation reveals an outcome defect. |

The storage-neutral logical artifact model, lightweight shared provenance, the
four-artifact vocabulary, progression authorization, and the explicit
three-artifact re-entry rule are FDI design decisions. They are informed by the
references but are not claims that any one reference implements the FDI
workflow.

## Explicit deferrals

The storage-neutral semantic baseline in version 0.1 intentionally does **not**
universally require or define:

- a universal Context manifest, taxonomy, assembly protocol, or freshness
  algorithm;
- artifact, evidence, decision, lineage, or execution ledgers;
- a workflow engine, control plane, state machine, event model, or scheduler;
- universal artifact schemas, identifiers, file names, directory layouts, or
  serialization formats;
- a standard traceability database or graph;
- required agents, prompts, models, tools, permissions, approval roles, or gate
  implementations;
- a universal cross-repository coordination protocol;
- standardized policy enforcement, deployment, rollback, or observability
  machinery; or
- any other platform mechanism whose necessity has not been demonstrated by a
  validated team use case.

Teams may adopt optional profiles or implement local versions of these
mechanisms when useful. FDI Workflow Semantics will make one universally
normative only after concrete use cases show that a shared baseline contract is
necessary and that the contract can preserve team-specific workflows without
premature complexity.

## v0.1 boundary

This design defines what the workflow artifacts and transitions mean. It is
complete at that semantic boundary. Future work may test the semantics with a
real team workflow and propose machinery in response to observed needs; such
machinery, including machinery already defined by an optional profile, is not
implicitly part of storage-neutral v0.1 conformance.
