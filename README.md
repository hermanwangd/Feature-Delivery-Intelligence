# Feature Delivery Intelligence

Feature Delivery Intelligence (FDI) is an AI-native engineering capability that takes a product feature or change intent, determines the complete and evidence-backed change surface across repositories and system boundaries, converts that intent into traceable implementation work, and drives the work toward verified, production-ready changes with minimal human orchestration. It optimizes for correct feature delivery, not code-generation speed.

This repository is the FDI coordination repository. It holds the adopted coordination profile under `.fdi/` — Context, Skills, Baseline, and per-feature artifacts — and the two canonical design documents:

- [FDI workflow semantics design](docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md)
- [FDI Context taxonomy design](docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md)

## The canonical FDI workflow

Every feature delivery runs through four canonical transitions, each with its own producer, literal Context reads, registry-first selections, and gate:

```text
Human -> Intention -> Delivery Spec -> Change Set -> Verification & Validation Report
```

1. **Human -> Intention**: an authenticated Human signal is captured once at an immutable revision, safely redacted, and mapped to stable criterion identities in the two-member Intention bundle (`request.md` and `intention.md`) with one sole gate.
2. **Intention -> Delivery Spec**: a five-member Spec bundle (index, requirements, design, tasks, V&V plan) maps every criterion to requirement, design, task, and V&V IDs, and authorizes bounded source reads only through a completed preflight source scope.
3. **Delivery Spec -> Change Set**: the implementation agent writes only the exact paths authorized by the completed change-surface summary and records the candidate base/head revisions, checks, mappings, and deviations.
4. **Change Set -> Verification & Validation Report**: an independent V&V run reproduces the planned checks, maps every criterion to evidence, and records per-criterion and overall verdicts.

Profile bootstrap, Baseline reconstruction (B1/B2), and post-release Context refresh (B3a/B3b) are support workflows, not additional canonical artifacts or a fifth feature-delivery stage.

## Contract-ready versus Execution-verified

**Contract-ready** means the profile, schemas, registries, Skills, and gates exist and conform to the adopted contract. **Execution-verified** is a stronger claim: it may be asserted only for transitions whose declared reads, writes, Context selections, evidence, traceability, and gate reviews actually executed and passed for a specific feature run.

In this repository, `Contract-ready` is claimed for the adopted profile, while `Execution-verified` is claimed only within the exact recorded evidence of the HERM-209 pilot under `.fdi/features/HERM-209/`. Nothing here implies that the framework as a whole, the support workflows, or any future feature run is execution-verified.

## Starting a feature delivery

1. Open the coordination entry point: [.fdi/README.md](.fdi/README.md).
2. Register the authenticated Human signal as the feature's Intention bundle under `.fdi/features/<feature-id>/`.
3. Run the four canonical transitions in order using the eight core Skills cataloged in `.fdi/skills/catalog.md`; every governed selection loads the `context-selection` Skill plus its transition Skill.
4. Do not merge a candidate whose independent V&V verdict is not `PASS`.

## Ownership and safety boundary

This coordination repository owns the `.fdi/` profile, feature artifacts, mappings, and safe (redacted, digest-based) evidence. Source repositories own their own code, branches, pull requests, CI, review, merge, release, and rollback. A feature delivery may read source content only through bounded, preflight-authorized, immutable-revision selectors, and may write a source candidate only through the source repository's own branch/PR authority. No credentials, unsafe raw payloads, or copied source trees are ever persisted in this repository.
