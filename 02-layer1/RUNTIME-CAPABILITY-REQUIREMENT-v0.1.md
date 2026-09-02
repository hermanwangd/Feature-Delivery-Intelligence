# RuntimeCapabilityRequirement v0.1

**FDI release:** v0.4.7.0<br>
**Purpose:** bind optional/on-demand FDI runtime capabilities without changing Layer 2 ContextRequirement authority.

## Separation

```text
ContextRequirement
  -> governed Layer 2 Product Assets

RuntimeCapabilityRequirement
  -> bounded execution-time capability such as STRUCTURAL_INTELLIGENCE_QUERY
```

A FeatureKnowledgePlan may instantiate only a runtime template already declared by the root canonical Skill. It cannot:

- invent a new runtime capability or template;
- promote an OPTIONAL/ON_DEMAND capability to REQUIRED unless the root Skill explicitly allows that transition;
- exceed the root Skill's operation or traversal budgets;
- carry `ProductAssetRef`, knowledge-role, authority-dimension, or Context-selector fields;
- use Structural Intelligence availability as a shortcut to current Feature truth.

This keeps the v0.4.6.2 FeatureKnowledgePlan delegation rule intact while allowing FDI Skills to declare bounded shared runtime dependencies.
