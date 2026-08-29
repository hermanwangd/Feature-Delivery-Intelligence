# HERM-209 source-diff evidence

<a id="evidence-identity"></a>
## Evidence identity

- Evidence ID: source-diff
- Feature: HERM-209
- Evidence revision: source-diff-v1
- Candidate base/head: 11306cacad93f3b2eb341cfd5e8eb1e78ff1638e/bf4e12d44be77063cdfa334815a1be8146b7561c
- PR: #3 https://github.com/hermanwangd/Feature-Delivery-Intelligence/pull/3

<a id="claim"></a>
## Claim

The completed profile, Intention, and Delivery Spec are committed at candidate_base_sha; candidate_head_sha is its immediate child and adds exactly repository-root README.md without changing .fdi.

<a id="method"></a>
## Method

Resolve exact commits; inspect parent and merge-base; run git diff --check; run name-only and name-status diffs; compare .fdi trees with diff --exit-code; verify README absence/presence at base/head; compute SHA-256 over README bytes and complete patch; observe PR target/head from authenticated GitHub provider.

<a id="candidate-environment"></a>
## Candidate/environment

- Repository: feature-delivery-intelligence
- branch_base_sha/main base: 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- candidate_base_sha: 11306cacad93f3b2eb341cfd5e8eb1e78ff1638e
- candidate_head_sha: bf4e12d44be77063cdfa334815a1be8146b7561c
- candidate environment: immutable local Git objects
- provider environment: GitHub PR #3, target main, head observed bf4e12d44be77063cdfa334815a1be8146b7561c

<a id="observation"></a>
## Observation

- parent line: bf4e12d44be77063cdfa334815a1be8146b7561c 11306cacad93f3b2eb341cfd5e8eb1e78ff1638e
- merge-base(candidate base, candidate head): 11306cacad93f3b2eb341cfd5e8eb1e78ff1638e
- git diff --check: exit 0, empty output
- git diff --name-only: README.md
- git diff --name-status: A	README.md
- .fdi diff exit: 0
- candidate base .fdi file count: 42
- README at candidate base: absent
- README at candidate head: present
- PR #3 creation snapshot: OPEN, target main@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482, head bf4e12d44be77063cdfa334815a1be8146b7561c, 43 changed files, mergeable/CLEAN, no provider checks

<a id="result"></a>
## Result

PASS as producer evidence for candidate adjacency, exact README-only source diff, and PR creation identity. This result does not substitute for independent V&V or final PR-head evidence.

<a id="integrity-and-access"></a>
## Integrity and access

- README SHA-256: f935717da40a3c071be468ec9ca53997b6ff022848122664cdfddfe8bfa95c83
- candidate patch SHA-256: bc38821fb59667ce6469f43c2f3bfc40c936e4558f99a78e331c2a85106db45f
- Git object IDs are immutable.
- Provider observation used authenticated gh CLI.
- Raw credentials/provider tokens and user-local paths are excluded.

<a id="producer-and-owner"></a>
## Producer and owner

Producer: implementation agent. Source/branch/PR owner: Repository owner. Evidence owner: HERM-209 Change Set. Independent reproduction owner: Transition 4 V&V agent.

<a id="limitations"></a>
## Limitations

Provider state can change after observation; the final PR head is a later coordination/V&V commit and must be recorded externally. No CI check existed at PR creation. No release/runtime/B1/B2/B3 claim.

<a id="validity-expiry-and-supersession"></a>
## Validity, expiry, and supersession

VALID only for candidate pair 11306cacad93f3b2eb341cfd5e8eb1e78ff1638e..bf4e12d44be77063cdfa334815a1be8146b7561c and exact Git objects. Invalidated by rewritten/unresolvable objects or mismatch. PR snapshot expires when provider head/state changes; successor is the final external PR-head observation. Backlinks: .fdi/features/HERM-209/spec/vv-plan.md#evidence-destinations and .fdi/features/HERM-209/change-set/index.md#gate-record.
