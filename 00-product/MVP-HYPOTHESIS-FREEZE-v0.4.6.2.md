# FDI MVP v0.4.6.2 — Pre-F001 Hypothesis Freeze

**Gate:** PRE_F001_OPTION_B_FREEZE

F001 MUST NOT execute until H01–H05 are frozen.

## MVP-H01 — Hypothesis Freeze

Frozen question:

> Does governed Product Knowledge improve fresh-agent current-feature Change Surface determination and reduce investigation effort without replacing current feature-specific Evidence as the source of truth?

Status: `FROZEN`

## MVP-H02 — Baseline / Treatment Freeze

Baseline and FDI treatment are defined in `FDI-Project-Definition-v0.3.3-OPTION-B-PATCH.md` and `06-validation/OPTION-B-PAIRED-REPLAY-PROTOCOL-v0.1.md`.

Rules:

- same Feature input;
- same pre-feature source boundary;
- same model/configuration unless the experiment explicitly declares model as a factor;
- same execution/tool budget;
- GroundTruth unavailable to both production arms;
- only the FDI arm receives governed FDI Product Knowledge and FeatureKnowledgePlan resolution.

Status: `FROZEN`

## MVP-H03 — Evaluation Metrics Freeze

Required metrics:

1. repository recall / precision;
2. Change Surface obligation recall / precision where scorable;
3. unsupported required claims;
4. false inclusion / false exclusion;
5. false `SPEC_READY` / false closure;
6. T2 gate correctness;
7. investigation steps/tool calls;
8. tokens/cost;
9. cycle time;
10. retries/escalations;
11. human clarification/correction/intervention.

Status: `FROZEN`

## MVP-H04 — Knowledge Authority Boundary Freeze

FDI Product Knowledge MAY establish or constrain:

- terminology and product identity;
- capability interpretation;
- durable business/domain constraints when the referenced Product Asset has the applicable authority;
- realization/navigation candidates;
- historical priors.

FDI Product Knowledge MUST NOT establish:

- current `CONFIRMED` Change Surface;
- current `EXCLUDED` Change Surface;
- current implementation truth;
- `SPEC_READY`;
- release/deploy authorization.

Current material Change Surface dispositions require current feature-specific pinned Evidence.

Status: `FROZEN`

## MVP-H05 — Dataset / Holdout Freeze

- F001 is calibration only.
- F002–F005 are blind holdouts after method freeze.
- each case binds exact pre-feature repository revisions and target refs;
- target/post-cutoff Feature/PR/commit information is evaluator-only and excluded from production Context;
- GroundTruth is scorer-only;
- tuning after observing F002–F005 invalidates their holdout status.

Status: `FROZEN`

## Gate result

```text
H01 FROZEN
H02 FROZEN
H03 FROZEN
H04 FROZEN
H05 FROZEN

PRE_F001_OPTION_B_FREEZE = READY_FOR_SOURCE_TREE_CONFORMANCE_IMPLEMENTATION
```

This is a design/experiment freeze, not evidence that runtime conformance has been implemented.
