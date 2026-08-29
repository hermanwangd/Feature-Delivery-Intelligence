# Feature Delivery Intelligence

Feature Delivery Intelligence (FDI) is an AI-native engineering approach for turning a product change intent into a complete, traceable, and evidence-backed implementation. This repository is the coordination repository for the FDI profile and, for the HERM-209 pilot, the single documentation source repository.

## Canonical workflow

    Human -> Intention -> Delivery Spec -> Change Set -> Verification & Validation Report

Context supports every agent execution; it is not a fifth artifact or workflow stage. Baseline discovery, Baseline verification, and post-release Context refresh are separate support workflows.

## Start a feature delivery

1. Capture an authenticated Human request under its exact feature key.
2. Use the adopted [FDI coordination profile](.fdi/README.md) and registry-first Context selection to produce the Intention.
3. Convert the authorized Intention into a bounded Delivery Spec with requirements, design, tasks, source selectors, and a V&V plan.
4. Implement only the authorized source-repository surface and record immutable candidate commits, checks, deviations, and evidence.
5. Have a distinct verifier independently assess Delivery Spec conformance and intended-use success before making an execution claim.

The semantic meaning of the workflow is defined in [FDI Workflow Semantics v0.1](docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md). The adopted physical Context, Skill, Baseline, artifact, selector, and gate contracts are defined in [FDI Context Taxonomy and Markdown Contract v0.1](docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md).

## Contract-ready and Execution-verified

Contract-ready means the paths, schemas, selectors, authorities, Skills, capabilities, mappings, gates, and evidence destinations are complete enough to execute safely.

Execution-verified means the declared transitions actually ran and an independent review found that their reads, writes, evidence, traceability, and acceptance criteria passed. The HERM-209 source candidate does not by itself establish that claim; at candidate creation, Execution-verified is NOT_CLAIMED. Any later claim is limited to the exact HERM-209 candidate and evidence recorded in its V&V report. It never verifies the product, support workflows, future features, or future executions by implication.

## Coordination and source ownership

The coordination repository owns cross-repository Intention, aggregate Delivery Spec, Change Set mappings, V&V reports, curated Context, and safe evidence references. Each source repository retains authority for its source, local instructions, tests, configuration, schemas, interfaces, review, CI, branch protection, deployment, release, and rollback.

This pilot uses one repository in both roles, but the boundary still applies: files under .fdi coordinate and record the delivery, while this README is source-owned. Mutable references, copied source trees, credentials, unsafe raw payloads, planned-as-current topology, and unreviewed release actions are outside the safety boundary.
