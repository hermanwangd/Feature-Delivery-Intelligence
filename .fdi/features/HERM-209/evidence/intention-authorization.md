# HERM-209 Intention authorization evidence

<a id="evidence-identity"></a>
## Evidence identity

- Evidence ID: intention-authorization
- Feature: HERM-209
- Captured: 2026-08-30
- Issue safe digest: sha256:4d8f386bf55b1d9f0a0d7490643eba5e6b7b79f0f117a7f3daac9fa3eda937a7
- Trigger safe digest: sha256:122cfeb48812a58aed3118bc4a68568c6b067f2f9cf68fe6c77ed4d35f8f7ee6

<a id="claim"></a>
## Claim

The HERM-209 desired outcome and pilot scope were supplied through the authenticated Multica issue revision and explicit start comment, with workspace-authorized product intent and sixteen stable criterion identities.

<a id="method"></a>
## Method

Authenticated Multica CLI read; resolve issue/comment IDs and revisions once; canonicalize only safe ID/revision/title/description/content/timestamp/author-type fields; SHA-256 digest; exclude credentials, email addresses, transport metadata, and unsafe raw payload.

<a id="candidate-environment"></a>
## Candidate/environment

Multica workspace issue 01a04e70-c387-72a2-bf4e-f97db187c8db revision 5; trigger 01a04eca-8fc6-722b-a903-1934b48a1897 revision 1; received 2026-08-29T18:31:33Z; profile start 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482.

<a id="observation"></a>
## Observation

The trigger authorizes immediate implementation/pilot after HERM-204/HERM-205 and PR #1 gates, requires exact merged-contract preservation, candidate branch/PR/evidence, independent V&V, and forbids inferred execution verification.

<a id="result"></a>
## Result

PASS for authenticated capture and approved pilot scope. Criterion IDs CRIT-001 through CRIT-016 are allocated; authorization does not establish current topology/source behavior or a future verdict.

<a id="integrity-and-access"></a>
## Integrity and access

Digests are over documented safe canonical field sets. Source remains in authenticated Multica authority; no credential, email, unsafe raw payload, or local absolute path is persisted.

<a id="producer-and-owner"></a>
## Producer and owner

Producer: Intention agent. Product authorization source: authenticated current issue revision and trigger. Evidence owner: product/governance owner.

<a id="limitations"></a>
## Limitations

This evidence proves capture/authenticated authorization only. It does not prove implementation, source truth, release, B1/B2/B3, or V&V.

<a id="validity-expiry-and-supersession"></a>
## Validity, expiry, and supersession

State: VALID for issue revision 5 and trigger revision 1. Invalidated by revocation/replacement or material issue revision. Review at pilot completion; successor: none.
