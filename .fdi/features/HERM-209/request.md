# HERM-209 authenticated request

<a id="artifact-identity"></a>
## Artifact identity

- Feature key: HERM-209
- Logical artifact: Intention (supporting authenticated-input member)
- Artifact revision: request-v1
- Producer: Intention agent
- Profile starting revision: 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Issue ID/revision: 01a04e70-c387-72a2-bf4e-f97db187c8db/5
- Trigger ID/revision: 01a04eca-8fc6-722b-a903-1934b48a1897/1

<a id="inputs"></a>
## Inputs

- Authenticated issue safe canonical payload@sha256:4d8f386bf55b1d9f0a0d7490643eba5e6b7b79f0f117a7f3daac9fa3eda937a7
- Authenticated trigger safe canonical payload@sha256:122cfeb48812a58aed3118bc4a68568c6b067f2f9cf68fe6c77ed4d35f8f7ee6
- Received: 2026-08-29T18:31:33Z
- Assurance: workspace-scoped authenticated Multica CLI/API response; immutable ID+revision capture

<a id="context-consulted"></a>
## Context consulted

- .fdi/README.md@sha256:fadbd405a33b7d440df9b60f27647614bbb2c2c9eb5b852499c04d8037db727a for adoption/start revision.
- .fdi/context/contract.md@sha256:b9089be300bbff8932c5c1e1ac98a54505e9b623cd48f8d597d4968cfea9b000 for capture schema/authority.
- .fdi/context/steering/product.md@sha256:c0c8bcc3d1c6f33e53263184ea5d569495475f627264ed471f961fad255cb97f for product outcome.
- .fdi/context/steering/agent-policy.md@sha256:27c84ed4e418f92bf7d2ff65d22bbf327da01be4c384a3a97159e8538dc33c85 for safe redaction.
- .fdi/skills/human-to-intention/SKILL.md@sha256:079f0e209b4787b3bc21f83fd4f94de5a9775326c6f560c6be118588d1ca3b47 for procedure.
- Full literal/registry proof is recorded in intention.md#context-consulted.

<a id="human-signal"></a>
## Human signal

Authenticated desired-behavior source: current HERM-209 issue revision 5 and explicit start trigger revision 1, received 2026-08-29T18:31:33Z. Raw payload is not copied.

<a id="requester"></a>
## Requester

Workspace-authorized product intent represented by the authenticated Multica issue workflow. Initiating actor type: agent acting within workspace authority. No personal identity or email is persisted or inferred.

<a id="capture-authentication"></a>
## Capture authentication

- Method: authenticated multica issue/comment reads.
- Assurance: workspace-scoped access, stable IDs, explicit revisions, provider timestamps.
- Issue digest field set: id, revision, title, description, updated_at -> sha256:4d8f386bf55b1d9f0a0d7490643eba5e6b7b79f0f117a7f3daac9fa3eda937a7.
- Trigger digest field set: id, revision, content, created_at, author_id, author_type -> sha256:122cfeb48812a58aed3118bc4a68568c6b067f2f9cf68fe6c77ed4d35f8f7ee6.
- Redaction: credentials, email, transport/auth material, and unsafe raw payload excluded.

<a id="requested-change"></a>
## Requested change

Adopt the approved coordination profile, materialize the exact mandatory .fdi core and honest Baseline, execute the four HERM-209 transitions, create a repository-root README contributor entry point, produce adjacent candidate commits and PR, and obtain an independent evidence-backed V&V verdict.

<a id="constraints"></a>
## Constraints

Preserve taxonomy, authority, provenance, registry-first selection, Skill/Tool boundaries, literal paths, B3a/B3b separation, and multi-repository ownership. Use immutable source SHA 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482. Do not execute B1/B2/B3, fabricate evidence, read mutable source, create placeholders, or self-award Execution-verified.

<a id="source-references"></a>
## Source references

- Issue 01a04e70-c387-72a2-bf4e-f97db187c8db revision 5@sha256:4d8f386bf55b1d9f0a0d7490643eba5e6b7b79f0f117a7f3daac9fa3eda937a7
- Trigger 01a04eca-8fc6-722b-a903-1934b48a1897 revision 1@sha256:122cfeb48812a58aed3118bc4a68568c6b067f2f9cf68fe6c77ed4d35f8f7ee6
- Profile start 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Authorization evidence .fdi/features/HERM-209/evidence/intention-authorization.md@sha256:c0fa7d1627a72fd41b6f3e1ba48f7c376c8b6a5142a56381e4cb4cee38e8921e

<a id="ambiguities"></a>
## Ambiguities

None blocking. The same repository has coordination and source roles in this one-repository pilot, while authority remains explicitly separate. Final execution-verification status is reserved to the independent evidence gate.

<a id="traceability"></a>
## Traceability

| Request fragment | Intention criterion | Captured obligation |
| --- | --- | --- |
| REQ-FRAG-001 | CRIT-001 | Start dependencies, immutable PR #1 merge SHA, and immutable HERM-209 input revision are recorded at required destinations. |
| REQ-FRAG-002 | CRIT-002 | Every mandatory core file exists and conforms without secret, local absolute path, copied source, or fabricated evidence; adoption is ADOPTED. |
| REQ-FRAG-003 | CRIT-003 | Every cross-file target uses an explicit stable lowercase kebab-case anchor and no generated/numbered authority fragment. |
| REQ-FRAG-004 | CRIT-004 | Catalog and relations are sole current-topology registries; structure is placement policy; planned relations are never current Context. |
| REQ-FRAG-005 | CRIT-005 | Every conditional selection is registry-first with lifecycle, applicability, freshness, successor, trust, path/digest, reason, and exclusions; no placeholder exists. |
| REQ-FRAG-006 | CRIT-006 | Eight core Skills are ACTIVE, versioned, current, cataloged, digest-resolvable, bound, permissioned, and provenance-complete. |
| REQ-FRAG-007 | CRIT-007 | Refresh Skill separates B3a/B3b and permits atomic adoption only after independent PASS; HERM-209 does not execute B3. |
| REQ-FRAG-008 | CRIT-008 | Baseline honestly records pinned empty/staged state; no unsupported capability or B1/B2/B3/VERIFIED-AS-IS claim exists. |
| REQ-FRAG-009 | CRIT-009 | Request and intention form one authenticated, redacted, reviewable, criterion-mapped bundle with one producer and sole gate. |
| REQ-FRAG-010 | CRIT-010 | Transition 2 writes/passes preflight source scope before bounded content reads and never self-authorizes from final change surface. |
| REQ-FRAG-011 | CRIT-011 | All four canonical transitions execute in order with literal/selected reads, writes, Context revisions, exclusions, mappings, evidence, and gate reviews. |
| REQ-FRAG-012 | CRIT-012 | Completed profile/Intention/Spec is candidate base and its immediate child changes exactly repository-root README.md. |
| REQ-FRAG-013 | CRIT-013 | Every Change Set deviation has disposition and proposed blocking state before V&V; PASS has no unresolved blocker. |
| REQ-FRAG-014 | CRIT-014 | Repository-root README satisfies its contract and all fresh local validation checks pass. |
| REQ-FRAG-015 | CRIT-015 | Bidirectional traceability is explicit from authenticated fragment through criterion/Spec/candidate/evidence/verdict. |
| REQ-FRAG-016 | CRIT-016 | Independent V&V records separate verification/validation, per-criterion/overall verdict, earliest re-entry, and truthful execution claim. |

<a id="open-gaps-and-deviations"></a>
## Open gaps and deviations

No capture gap. Downstream implementation/V&V state is not inferred by this member.

<a id="capture-validity-and-supersession"></a>
## Capture validity and supersession

VALID for issue revision 5 and trigger revision 1; received 2026-08-29T18:31:33Z. A material revision, revocation, or replacement invalidates downstream artifacts and re-enters Human -> Intention. Successor: none.

<a id="intention-gate"></a>
## Intention gate

Sole gate: .fdi/features/HERM-209/intention.md#gate-record. This section is a backlink only and owns no second gate.
