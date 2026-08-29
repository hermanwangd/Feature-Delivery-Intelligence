# FDI coordination profile

<a id="status"></a>
## Status

- State: CURRENT
- Scope: Feature Delivery Intelligence product and its coordination/source authority boundary
- Owner: FDI governance owner
- Approver: FDI governance owner
- Version: 0.1.0
- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Superseded by: none

<a id="purpose"></a>
## Purpose

Entry point for the adopted Feature Delivery Intelligence coordination-repository profile.

<a id="fdi-version"></a>
## FDI version

FDI Workflow Semantics v0.1; coordination-repository profile v0.1.

<a id="repository-role"></a>
## Repository role

This repository is the coordination repository for product-wide Intention, Delivery Spec, Change Set mappings, V&V reports, curated Context, and safe evidence references. In this pilot it is also the single source repository, but source authority remains distinct.

<a id="entry-points"></a>
## Entry points

- Profile contract: context/contract.md
- Context registry: context/index.md
- Canonical topology: context/codebase/catalog.md and context/codebase/relations.md
- Skill registry: skills/catalog.md
- Baseline registry: baseline/catalog.md
- HERM-209 authenticated request: features/HERM-209/request.md

<a id="safety-boundary"></a>
## Safety boundary

The coordination profile owns cross-repository intent, aggregate mappings, and safe evidence references. Each source repository retains authority for source, local instructions, tests, configuration, schemas, review, CI, branch protection, deployment, and release. Mutable refs, credentials, raw unsafe payloads, and copied source trees are prohibited as evidence.

<a id="adoption-state"></a>
## Adoption state

ADOPTED

<a id="provenance"></a>
## Provenance

- Profile starting revision: 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed profile candidate: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Authoritative inputs:
  - feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
  - feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Producer: HERM-209 profile bootstrap
- Produced: 2026-08-30
- Validation method: approved-profile schema projection with stable-anchor review

<a id="freshness-and-supersession"></a>
## Freshness and supersession

- Last reviewed: 2026-08-30
- Next review: 2027-02-26
- Refresh triggers: governing contract, ownership, repository, topology, or policy change
- Lifecycle: ACTIVE
- Superseded by: none
- Conflict behavior: block dependent claims and route to the named owner; never silently choose a convenient source.
