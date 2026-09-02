# Exact Normative Source Rehydration — HERM-219

The recovery package knows the **identity and approved status** of the required modules, but does not claim byte identity for local copies because the prior project source was corrupted/lost.

Required exact source set:

1. `fdi-layer1-specification-v0.2-approved.md`
2. `fdi-layer1-markdown-io-profile-v0.1-approved.md`
3. exact HERM-211 FT-T2 six-contract/five-Skill/workflow package
4. `fdi-layer2-product-intelligence-framework-v0.1-approved.md`
5. `fdi-product-asset-profile-specification-v0.1-approved.md` (PA-03/PA-05 fully specified only)
6. `fdi-product-asset-maintenance-skill-contracts-v0.1-approved.md`

For each source:

```text
recover exact bytes
→ place under normative/<module>/
→ calculate SHA-256 (or deterministic tree digest for FT-T2)
→ record approval reference
→ compare against candidate/superseded variants
→ update GB-0001-CANDIDATE
```

Do not infer exact source text from recovery references or implementation schemas. If exact bytes cannot be recovered, baseline promotion requires an explicit new approval of a reconstructed successor; it may not inherit old approval implicitly.
