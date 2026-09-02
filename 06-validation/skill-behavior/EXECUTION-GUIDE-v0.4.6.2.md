# DEV-204 Fresh-Context RED/GREEN Execution Guide — v0.4.6.2

## Status

`EXECUTION_READY_NOT_EXECUTED`

This package prepares DEV-204 evidence collection. It does not substitute deterministic tests for Agent behavior and does not upgrade any `STRUCTURAL_ONLY` Skill status by itself.

## Invariants

For every RED/GREEN pair:

1. use the exact same frozen scenario prompt and `scenario_sha256`;
2. RED runs in a fresh context without the target Skill;
3. GREEN runs in a different fresh context with the target Skill;
4. RED and GREEN use different independent reviewer contexts;
5. reviewer rubric is never mounted in the Agent context;
6. GroundTruth is never mounted;
7. capture the Agent output and independent reviewer record as immutable evidence;
8. a Skill is not behaviorally validated unless a meaningful RED failure is observed and the same frozen scenario passes GREEN;
9. if RED already passes, record `RED_NO_SKILL_GAP_OBSERVED`; do not add procedural prose merely to manufacture a Skill gap;
10. the Option B closed-loop target is a **system behavior**, not a sixth FT-T2 Skill.

## Prepare packets

```bash
python scripts/prepare_dev204_execution.py \
  --scenario-pack 06-validation/skill-behavior/SCENARIOS-v0.4.6.2.json \
  --output-dir 06-validation/skill-behavior/prepared-v0.4.6.2
```

Each scenario yields:

```text
<scenario>-red-packet.json
<scenario>-green-packet.json
<scenario>-reviewer-rubric.json
```

Only the RED/GREEN packet is sent to the Agent. The reviewer rubric is supplied only after the Agent output is frozen.

## Executor contract

The external executor may be Multica or another environment that can prove independent fresh contexts. For each arm it must preserve at least:

```text
context_id
reviewer_context_id
scenario_sha256
target_skill_loaded
ground_truth_mounted=false
agent_output_ref
review_ref
scores
overall
```

The completed record must conform to `execution-record.schema.json` and the runtime validation in `runtime/dev204_validation.py`.

## Evaluate a RED/GREEN pair

```bash
python scripts/evaluate_dev204_pair.py \
  --red <red-execution-record.json> \
  --green <green-execution-record.json>
```

Possible pair results:

```text
GREEN_PASS
GREEN_FAIL
RED_NO_SKILL_GAP_OBSERVED
```

`GREEN_PASS` is evidence for that exact scenario/target only. A full Skill validation decision must still satisfy the applicable scenario pack and any required REFACTOR/loophole tests.

## Option B system behavior

`DEV204-OPT-B-01` tests the architecture flow:

```text
Feature Intention
  ↓
Product Semantics
  ↓
Product Realization
  ↓
Delivery Intelligence
  ↓
Candidate investigation
  ↓
current feature-specific pinned Evidence
  ↓
Change Surface
```

Required authority boundary:

```text
Product Knowledge → understanding / constraints / candidates / priors
Current Evidence  → current CONFIRMED / EXCLUDED truth
T2 root Skill     → SPEC_READY | BLOCKED
```

The system behavior must fail if Product Knowledge alone is used to create current Change Surface truth or `SPEC_READY`.

## Current blocker in this runtime

This ChatGPT runtime has no callable independent fresh-agent/Multica executor and no mounted canonical v0.4.6.1 source tree. Therefore the prepared packets are ready, but all DEV-204 execution statuses remain `NOT_EXECUTED` until an external executor supplies conforming records.
