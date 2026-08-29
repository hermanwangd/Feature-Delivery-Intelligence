# FDI Skill catalog

<a id="skill-registry"></a>
## Skill registry

| Stable ID | Exact path | Version | SHA-256 | Lifecycle | applies_to | Owner | Authority | Trust | Last review | Next review | superseded_by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| context-selection | .fdi/skills/context-selection/SKILL.md | 0.1.0 | e327dcc6ecfcdbf2085762c8b1883a59aeabdd5beac35f687c1c1eec001524b8 | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| human-to-intention | .fdi/skills/human-to-intention/SKILL.md | 0.1.0 | 079f0e209b4787b3bc21f83fd4f94de5a9775326c6f560c6be118588d1ca3b47 | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| intention-to-spec | .fdi/skills/intention-to-spec/SKILL.md | 0.1.0 | 29aa863b3a099d4274ec1c58582271f76b3eeb8d2b75f1e362f8a7d4c1af8f13 | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| spec-to-implementation | .fdi/skills/spec-to-implementation/SKILL.md | 0.1.0 | c969cf54bac4440280e501448581a0da95a2889a3957898b00c7e65c6e9ba7b9 | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| implementation-to-correctness | .fdi/skills/implementation-to-correctness/SKILL.md | 0.1.0 | d06c25a681d4efe7426d8afd988fba7b8e74ccab584743bceb55419eb15ab465 | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| baseline-discovery | .fdi/skills/baseline-discovery/SKILL.md | 0.1.0 | 7498f295f28acee6b70efa793deaeffca79e88fb58437c8b0c8bc4dfa70fbbe5 | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| baseline-verification | .fdi/skills/baseline-verification/SKILL.md | 0.1.0 | 7251353f1f585347a15aedbd452fe95074d591e9ef602d77620f38589cb52e99 | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |
| release-to-codebase-baseline-refresh | .fdi/skills/release-to-codebase-baseline-refresh/SKILL.md | 0.1.0 | 2198f9a5d512fea1d48153493912286d22dd8901e391a718d2cf44c1b830e51f | ACTIVE | product-feature-delivery-intelligence and HERM-209 where mapped | FDI workflow owner | adopted-profile procedure | reviewed pinned contract projection | 2026-08-30 | 2026-11-28 | none |

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

All eight packages are version 0.1.0. Digests above are SHA-256 over final UTF-8 bytes. Source profile starting revision: 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482; reviewed candidate: f4561614ba1a1d0f222ef838ff6c4815c051dd01.

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
