# FDI MVP Hypothesis Freeze v0.4.7.0

**Status:** Governing experiment freeze before F001.<br>
**Supersedes for future MVP execution:** `MVP-HYPOTHESIS-FREEZE-v0.4.6.2.md`<br>
**Reason for revision:** Structural Intelligence was formally integrated into FDI before F001 execution; the experiment must therefore evaluate the complete Feature Delivery Intelligence architecture rather than Product Knowledge alone.

## MVP-H01 — Core hypothesis

Status: `FROZEN`

> **Does Feature Delivery Intelligence—combining governed Product Intelligence, bounded live Structural Intelligence, and current-evidence-gated investigation—improve fresh-agent Change Surface discovery quality and efficiency?**

FDI means the combination of:

```text
Product Intelligence
  - Product Semantics
  - Product Realization
  - Delivery Intelligence

Structural Intelligence
  - source-pinned bounded code-graph queries
  - cross-repository topology / trace / structural delta

Current investigation
  - current feature-specific pinned Evidence
  - evidence-gated Change Surface truth
```

## MVP-H02 — Baseline / treatment semantics

Status: `FROZEN`

F001 calibration SHALL use four controlled arms:

```text
A Baseline                  Product Intelligence NO   Structural Intelligence NO
B Structural only           Product Intelligence NO   Structural Intelligence YES
C Product Intelligence only Product Intelligence YES  Structural Intelligence NO
D Full FDI                  Product Intelligence YES  Structural Intelligence YES
```

All arms receive the same frozen Feature signal, same exact pre-feature source cutoff, same model/configuration, same execution/tool/time budget, and same evaluation rubric.

F002–F005 primary blind proof remains `A Baseline vs D Full FDI`. B/C may be used only as diagnostic ablations and cannot redefine the primary proof after F001.

## MVP-H03 — Metrics

Status: `FROZEN`

Primary outcome dimensions:

- repository candidate recall / precision;
- Change Surface obligation recall / precision;
- false inclusion / false exclusion;
- unsupported required claims;
- false `SPEC_READY` / false closure;
- T2 gate correctness;
- investigation steps / tool calls;
- token and model cost;
- cycle time;
- retries / escalations;
- human clarification / correction / intervention.

F001 additionally measures the marginal contribution of Structural Intelligence and Product Intelligence through the four-arm ablation, but graph node count and Product Asset count are not success metrics.

## MVP-H04 — Authority boundary

Status: `FROZEN`

Product Intelligence cannot establish current `CONFIRMED` or `EXCLUDED` truth.

Structural Intelligence cannot establish current `CONFIRMED` or `EXCLUDED` truth.

Historical Delivery Intelligence cannot establish current applicability.

A Product Realization path or live structural graph relation can only guide candidate discovery and investigation.

**Current feature-specific pinned Evidence remains authoritative** for current Feature Change Surface truth and for any `SPEC_READY` decision.

No FDI runtime support contract may create a new canonical Layer 1 transition, HERM-211 helper-contract status, or Product truth source.

## MVP-H05 — Dataset / temporal isolation

Status: `FROZEN`

For Feature `Fx` with cutoff `T0`, every arm may access only information available at or before `T0` according to that arm's treatment definition.

Forbidden leakage includes:

- target Feature implementation;
- target PR/commit;
- post-cutoff Structural Intelligence / graph state;
- post-cutoff Delivery Intelligence;
- future Product Asset revision;
- future Registry projection;
- GroundTruth or evaluator artifacts.

Any leakage invalidates the replay rather than being scored as uplift.

## Execution gate

**F001 MUST NOT execute until this v0.4.7.0 H01–H05 freeze is active in the execution package.**

After F001, the allowed decision vocabulary is:

```text
CONTINUE | REVISE | STOP
```

If F001 requires `REVISE`, the revised protocol must be frozen before F002–F005 and may not retroactively reinterpret F001 evidence.
