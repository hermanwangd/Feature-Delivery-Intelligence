# Continue Development in Multica — Recovery Sequence v0.4.8.1

## Hard sequencing rule

`REC-000` is mandatory. While `governance/CURRENT = NONE`, implementation/proof work beyond recovery tooling remains paused.

### REC-000 — HERM-219 canonical baseline recovery
- recover exact approved normative source bytes;
- inventory id/path/version/status/approval/digest;
- reconcile Layer 1 v0.2 vs any v0.3 candidate; default to no promotion without explicit semantic approval;
- verify Layer 1 Markdown I/O compatibility;
- verify exact FT-T2 six contracts / five Skills / helper vocabularies / sole T2 gate;
- verify Layer 2 v0.1 exact framework/profile/maintenance bytes and preserve PA-03/PA-05-only fully-specified scope;
- keep PA-01 candidate unless separately promoted;
- generate exact digests and generated governing view;
- obtain explicit approval;
- create immutable `governance/baselines/GB-0001.yaml` and set `governance/CURRENT` to `GB-0001`.

**Stop:** if any exact approved source byte set is unavailable, conflicting, or unverifiable.

### REC-001 — Recovery integrity and exact normative binding
- run bundle/schema/unit validation;
- verify `GB-0001` digests and generated view;
- bind runtime/package to baseline ID + digest without changing semantics.

### REC-002 — Layer 2 exact contract runtime
- validate implementation schemas/runtime against approved Layer 2 descriptor/ref/lifecycle/selection semantics;
- preserve PA-03/PA-05 exact profile contracts;
- do not promote PA-01 as part of this issue.

### REC-003 — Product Intelligence Store
- complete Git-backed store beyond scaffold;
- immutable published semantic revisions;
- legal lifecycle transitions and one-active-lineage enforcement;
- governed supersession/stale/retire handling;
- deterministic/atomic Registry rebuild;
- publication authorization remains separate from Git merge mechanics.

### REC-004 — Azure Repos acquisition
- configure repository inventory with external credentials;
- clone/fetch into local workspace;
- freeze exact full Git revisions/worktrees;
- record reproducible SourceSnapshotSet.

### REC-005 — Grafel live exact binding
- index only frozen worktrees;
- execute real metadata/route/runtime version checks;
- require per-repository full revision equality;
- enforce repository scope, relation allowlist, depth and result bounds;
- persist strict GrafelBindingEvidenceRecord and revalidate it before use.

### REC-006 — PA-03 bootstrap
- create CB-01 inventory and ROI-qualified CB-02 relation proposals;
- use field-specific source authority;
- never copy the entire Grafel graph;
- Structural Intelligence is observation/evidence, not Product Asset truth.

### REC-007 — Product Semantics / Realization candidate synthesis
- generate Product/SubProduct/Capability/realization/domain-rule **candidates** from code + docs + history;
- keep PA-01 non-governing unless a separate approved promotion occurs;
- semantic proposals default to human review.

### REC-008 — Publication + Registry
- publish only eligible governed Product Assets;
- rebuild Registry from exact active ProductAssetRefs;
- test trust/authority/scope/freshness/supersession/conflict fail-closed resolution;
- validate Layer 1 `ResolvedContextRef` boundary.

### REC-009 — DEV-204
- fresh independent RED/GREEN only after active baseline and live binding evidence exist;
- record baseline ID/digest and runtime/provider versions;
- deterministic tests do not substitute for behavioral proof.

### REC-010 — F001
- freeze historical feature, source cutoff, evidence boundary, ground truth isolation and method;
- run four-arm calibration under the same active baseline;
- no empirical uplift claim before scoring is complete.

## Do not do

- do not add TerminusDB/Graphiti/Neo4j/GitNexus now;
- do not reconstruct approved specs from recovery summaries;
- do not redefine Layer 1/HERM-211 contracts;
- do not promote PA-01 silently;
- do not use branch names/short SHAs as evidence authority;
- do not allow Product/Structural priors to establish current Change Surface truth.
