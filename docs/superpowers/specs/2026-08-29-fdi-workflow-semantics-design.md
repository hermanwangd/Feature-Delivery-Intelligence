# FDI Workflow Semantics v0.1

**Status:** Approved design baseline · **Date:** 2026-08-29

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

## Core model

The canonical forward flow is:

```text
Human --agent--> Intention --agent--> Delivery Spec --agent--> Change Set --agent--> Verification & Validation Report
             \_________________________ Team Context supports every agent execution _________________________/
```

Each arrow is an agent execution. An execution consumes the completed artifact
to its left, the team's current Context, and any explicitly named inputs; it
produces or revises the artifact to its right. The executions may use the same
agent or different agents. FDI does not prescribe agent identities, prompts,
models, runtimes, or autonomy levels.

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

## Canonical artifact contracts

### 1. Intention

#### Purpose

Intention defines the change from the stakeholder and intended-use point of
view. It establishes why the change is needed, who needs it, and what outcome
must become true. It is the validation anchor for the entire delivery flow, not
a preliminary technical solution.

#### Inputs

- the human's change request, problem statement, or desired outcome;
- available stakeholder and user knowledge;
- known intended-use scenarios and operating conditions; and
- relevant Team Context, including product principles, current behavior,
  constraints, and prior decisions.

#### Minimum contents

- rationale: the problem or opportunity and why it matters;
- affected stakeholders or users;
- the outcome that must become true;
- representative intended-use scenarios and relevant operating conditions;
- in-scope and out-of-scope behavior;
- constraints and assumptions;
- explicit non-goals; and
- measurable success criteria stated from the stakeholder or user point of
  view.

The success criteria play the role of measures of effectiveness: they express
how stakeholders will decide whether the outcome succeeds. They should measure
the result in use, not merely whether implementation tasks were completed.

#### Completion condition

Intention is complete when its stakeholders, desired outcome, intended use,
scope boundaries, constraints, non-goals, and measurable success criteria are
explicit enough to derive requirements and later judge delivered value without
inventing a new product decision. Material uncertainty is resolved or stated as
a constraint that downstream work can safely honor.

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
- relevant Team Context, especially architecture and engineering rules, system
  and repository boundaries, current state, and development history; and
- focused investigation needed to understand affected components, interfaces,
  dependencies, and delivery constraints.

#### Minimum contents

- requirements and acceptance criteria traceable to the Intention;
- a technical design covering affected behavior, components, interfaces, data,
  operational concerns, and cross-boundary effects as applicable;
- an ordered implementation task breakdown, including dependencies and all
  required code, configuration, schema, migration, test, and documentation work;
- a verification plan that maps requirements and material design obligations to
  verification methods and expected evidence; and
- identified risks, assumptions, and intentionally deferred work that affect
  delivery correctness.

These are logical content obligations. They do not require separate
`requirements.md`, `design.md`, or `tasks.md` files, nor do they prohibit those
files.

#### Completion condition

Delivery Spec is complete when:

- its requirements, design, tasks, and verification plan are mutually
  consistent and traceable to the Intention;
- it accounts for the known change surface and relevant system boundaries;
- each requirement has an objective way to determine conformance;
- its tasks are actionable and dependency-aware; and
- no unresolved material decision must be improvised during implementation.

### 3. Change Set

#### Purpose

Change Set is the buildable and reviewable product candidate that realizes the
Delivery Spec. It is the actual system change, not a description of work that
might be performed.

#### Inputs

- the completed Delivery Spec and its verification plan;
- the original Intention for outcome awareness;
- relevant Team Context and the current state of every affected system or
  repository; and
- the implementation and test tools needed to produce the candidate.

#### Minimum contents

- the actual code, configuration, schema, migration, test, and documentation
  changes required by the Delivery Spec, as applicable;
- a coherent product candidate that can be built, exercised, and reviewed;
- any generated or operational artifacts necessary to evaluate that candidate;
  and
- every known deviation from the Delivery Spec, with its reason and expected
  effect on requirements, intended use, verification, or risk.

An undeclared deviation is a defect in the Change Set's traceability. A declared
deviation is not automatically acceptable; it must be reconciled by revising
the Delivery Spec or correcting the Change Set before a `PASS` verdict.

#### Completion condition

Change Set is complete when it contains a coherent, buildable, and reviewable
candidate; covers the Delivery Spec's implementation tasks or explicitly
declares each deviation; and is ready for the planned verification and
Intention-based validation. Completion here means ready for correctness
assessment, not already proven correct.

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

- the Intention, including intended-use scenarios and measurable success
  criteria;
- the Delivery Spec, including requirements, design obligations, tasks, and
  verification plan;
- the exact Change Set being assessed;
- evidence produced by tests, analysis, inspection, demonstration, operation,
  or other appropriate methods; and
- relevant Team Context, including environments, tools, quality rules, and
  current system behavior.

#### Minimum contents

- identification of the Intention, Delivery Spec, and exact Change Set assessed;
- verification results mapped to applicable requirements and material design
  obligations, including method, evidence, and result;
- validation results mapped to intended-use scenarios and measurable success
  criteria, including environment, evidence, and result;
- known deviations, anomalies, untested conditions, missing evidence, and other
  gaps;
- the impact and recommended disposition of each material gap; and
- one overall verdict: `PASS`, `FAIL`, or `INCONCLUSIVE`, with a rationale.

Teams may record finer-grained results, but the canonical report still carries
one overall verdict:

- `PASS`: sufficient evidence shows both Delivery Spec conformance and
  satisfaction of the Intention, with no unresolved material gap.
- `FAIL`: sufficient evidence shows that at least one required conformance or
  Intention criterion is not met.
- `INCONCLUSIVE`: available evidence is insufficient, unavailable, invalid, or
  ambiguous, so neither `PASS` nor `FAIL` is justified.

#### Completion condition

The report is complete when all in-scope verification and validation claims
have an explicit result, supporting evidence is identified, limitations and
gaps are disclosed, and the verdict follows from that record. Report completion
does not mean delivery success: a complete report may correctly conclude
`FAIL` or `INCONCLUSIVE`.

## Correctness feedback and re-entry

When the report is `FAIL` or `INCONCLUSIVE`, work returns to the earliest
artifact whose correction can resolve the finding:

| Re-entry target | Use when | Examples |
| --- | --- | --- |
| Intention | The desired outcome, stakeholder, intended-use scenario, scope, constraint, or success measure is wrong, missing, or too ambiguous to validate. | A technically correct feature solves the wrong user problem; a success criterion cannot distinguish success from failure. |
| Delivery Spec | Intention is sound, but its translation into requirements, design, tasks, or the verification plan is incomplete, inconsistent, or incorrect. | A cross-repository dependency is absent; acceptance criteria do not cover an intended-use scenario. |
| Change Set | Intention and Delivery Spec are sound, but the candidate is defective, incomplete, nonconforming, or lacks required implementation evidence. | A migration is missing; behavior differs from a requirement; a test fails. |

After correction, all affected downstream artifacts must be regenerated,
updated, or re-assessed. A finding must not be closed by changing only the
report. An `INCONCLUSIVE` result caused solely by unavailable evidence may be
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
2. Every forward transition is an agent execution informed by relevant current
   Team Context.
3. Intention remains the validation anchor; Delivery Spec does not replace it.
4. Delivery Spec remains one logical artifact containing requirements, design,
   tasks, and the verification plan.
5. Change Set is an assessable product candidate and declares deviations.
6. Verification is assessed against Delivery Spec; validation is assessed
   against Intention and intended use.
7. The final report is evidence-backed and uses `PASS`, `FAIL`, or
   `INCONCLUSIVE`.
8. Failed or inconclusive assessment can re-enter Intention, Delivery Spec, or
   Change Set, based on the source of the gap.
9. Context remains a cross-cutting team asset, not a feature-workflow step.

## Reference model mapping

FDI adopts concepts selectively. The referenced products are practical models,
not required implementations.

| Adopted concept | Primary reference model | FDI v0.1 use and boundary |
| --- | --- | --- |
| Stakeholder-centered outcome, intended use, and measurable success | [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), §§4.1 and 4.2 | Intention adopts stakeholder expectations, intended-use scenarios, constraints, and measures of effectiveness as the basis for outcome definition. FDI scales the concepts to feature delivery rather than adopting NASA's full lifecycle. |
| A practical proposal that explains why a change is needed | [OpenSpec spec-driven schema](https://openspec.dev/docs/schemas/spec-driven), `proposal.md` | OpenSpec's proposal is the practical analogue for the rationale and high-level scope in Intention. FDI Intention adds explicit stakeholders, intended use, non-goals, and measurable success criteria. |
| Requirements, technical design, and executable tasks as a structured delivery specification | [Kiro Specs](https://kiro.dev/docs/specs/) | Kiro's requirements/design/tasks structure is the primary practical model for Delivery Spec contents. FDI treats them as one logical artifact and adds an explicit verification plan without prescribing Kiro's three-file layout. |
| Agentic progression from what/why through design, tasks, quality checks, and implementation | [GitHub Spec Kit quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) | Spec Kit's `specify → clarify → plan → checklist → tasks → analyze → implement → converge` flow informs traceable agent handoffs, ambiguity checks, dependency-aware tasks, and consistency assessment. FDI defines semantic outputs rather than commands or gates. |
| Persistent team rules and selectively supplied project knowledge | [Kiro Steering](https://kiro.dev/docs/steering/) and [Kiro Context Management](https://kiro.dev/docs/cli/chat/context/) | Team Context adopts the idea that durable standards and relevant project knowledge inform agent work across sessions. FDI broadens Context to current system state, history, tools, and external knowledge while leaving retrieval and storage team-specific. |
| Build execution against planned tasks and convergence back to the specification | [OpenSpec spec-driven schema](https://openspec.dev/docs/schemas/spec-driven) `apply`, and [GitHub Spec Kit quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) `implement`/`converge` | These models inform the transition from Delivery Spec to Change Set and iterative closure of implementation gaps. FDI additionally requires declared deviations and permits re-entry to earlier artifacts. |
| Distinct verification and validation questions | [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), §§5.3 and 5.4 | FDI adopts verification against requirements/specification and validation against stakeholder expectations in intended use. |
| Evidence-bearing verification and validation reports with discrepancies and dispositions | [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), §§5.3.1.3 and 5.4.1.3 | FDI combines both evidence sets into one logical report. `PASS` and `FAIL` align with recorded outcome declarations; `INCONCLUSIVE` is an FDI extension that prevents an unsupported success or failure claim. |
| Reassessment when artifacts conflict or evidence exposes gaps | [GitHub Spec Kit quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) `analyze`/`converge`, together with NASA bidirectional traceability | FDI generalizes consistency and convergence into explicit re-entry to the earliest defective artifact, including Intention when validation reveals an outcome defect. |

The storage-neutral logical artifact model, the four-artifact vocabulary, and
the explicit three-target re-entry rule are FDI design decisions. They are
informed by the references but are not claims that any one reference implements
the FDI workflow.

## Explicit deferrals

Version 0.1 intentionally does **not** define:

- a Context manifest, taxonomy, assembly protocol, or freshness algorithm;
- artifact, evidence, decision, lineage, or execution ledgers;
- a workflow engine, control plane, state machine, event model, or scheduler;
- universal artifact schemas, identifiers, file names, directory layouts, or
  serialization formats;
- a standard traceability database or graph;
- required agents, prompts, models, tools, permissions, or human approval gates;
- a cross-repository coordination protocol;
- standardized policy enforcement, deployment, rollback, or observability
  machinery; or
- any other platform mechanism whose necessity has not been demonstrated by a
  validated team use case.

Teams may implement local versions of these mechanisms when useful. FDI will
standardize one only after concrete use cases show that a shared contract is
necessary and that the contract can preserve team-specific workflows without
premature complexity.

## v0.1 boundary

This design defines what the workflow artifacts and transitions mean. It is
complete at that semantic boundary. Future work may test the semantics with a
real team workflow and propose machinery in response to observed needs; such
machinery is not implicitly part of v0.1.
