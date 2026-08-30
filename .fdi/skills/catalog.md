# FDI Skill catalog

<a id="skill-registry"></a>
## Skill registry

| Stable ID | Exact path | Version | SHA-256 | Lifecycle | applies_to | Owner | Authority | Trust | Last review | Next review | superseded_by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| context-selection | .fdi/skills/context-selection/SKILL.md | 0.1.1 | da661dd387f6a3232072b06f67eb1c1959b7d84773254a7a6675398a9f317dbe | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| human-to-intention | .fdi/skills/human-to-intention/SKILL.md | 0.1.1 | f48c36bfb5fcf7ca00b048d25cc4e929748a79609d337a690a9fa43b2b80e52f | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| intention-to-spec | .fdi/skills/intention-to-spec/SKILL.md | 0.1.1 | 6ff39b93bb65b750e1dacecb7e31a2dc2cc94b159cf2642943a5a14fee6effe6 | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| spec-to-implementation | .fdi/skills/spec-to-implementation/SKILL.md | 0.1.1 | 60b28e5228f2433bdae3255e706b5200613751d66ede9cd1c04108400947c87f | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| implementation-to-correctness | .fdi/skills/implementation-to-correctness/SKILL.md | 0.1.1 | 13bf34867cc3e5d606d2ed7c41e919a73137971a2a6b321ce6affaaa54066b1a | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| baseline-discovery | .fdi/skills/baseline-discovery/SKILL.md | 0.1.1 | 87ce50a23d19801f15295d4e20a1bb531e823f7730d1904d729da4ea61e4341e | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| baseline-verification | .fdi/skills/baseline-verification/SKILL.md | 0.1.1 | 9dcec7055de562c9c56fb12ba8cf250d5652a7eee64922575f3e9d1a9f83325d | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| release-to-codebase-baseline-refresh | .fdi/skills/release-to-codebase-baseline-refresh/SKILL.md | 0.1.1 | d6d182b63f902d580b896d6363192c0a86122deb5fde8b5ba6f85441c99727a8 | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |

<a id="transition-mapping"></a>
## Transition mapping

| Execution | Required Skills |
| --- | --- |
| 1 Human -> Intention | context-selection; human-to-intention |
| 2 Intention -> Delivery Spec | context-selection; intention-to-spec |
| 3 Delivery Spec -> Change Set | context-selection; spec-to-implementation |
| 4 Change Set -> V&V | context-selection; implementation-to-correctness |
| B1 Baseline discovery | context-selection; baseline-discovery |
| B2 Baseline verification | context-selection; baseline-verification |
| B3a refresh candidate | context-selection; release-to-codebase-baseline-refresh |
| B3b refresh verification/adoption | context-selection; release-to-codebase-baseline-refresh; baseline-verification |

<a id="version-and-digest"></a>
## Version and digest

All eight packages are version 0.1.1. Digests above are SHA-256 over final UTF-8 bytes. Version 0.1.1 makes each output and allowed-write surface literal and exact while preserving the approved 0.1 transition semantics. Source profile starting revision: 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482; reviewed candidate: f4561614ba1a1d0f222ef838ff6c4815c051dd01.

<a id="capability-dependencies"></a>
## Capability dependencies

Stable bindings are declared in the Capability bindings section of each exact registered Skill. Capabilities are Tools governed by Skills, not a peer Context category. No implementation or credential is stored in a Skill.

<a id="permission-classes"></a>
## Permission classes

read-bounded; write-feature-artifact; write-source-candidate; open-pr; independent-read; post-release-candidate; independent-adoption. Each Skill narrows its allowed class and names approvals/prohibitions.

<a id="status"></a>
## Status

All eight entries are ACTIVE, digest-resolvable, review-current, and have no successor. Missing or mismatched package bytes fail transition preflight.

<a id="owner-and-authority"></a>
## Owner and authority

FDI workflow owner owns procedures; capability/security owners govern runtime and permissions; product/repository/verifier/release/row owners retain decision authority.

<a id="review-freshness-and-supersession"></a>
## Review, freshness, and supersession

Last review 2026-08-30; next review 2026-11-28. Refresh on contract, capability, permission, runtime, owner, or binding change and rerun smoke tests. SUPERSEDED entries remain traceable and name a successor.
