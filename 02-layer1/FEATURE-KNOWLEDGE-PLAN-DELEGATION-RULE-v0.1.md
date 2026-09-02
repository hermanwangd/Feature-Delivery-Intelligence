# FeatureKnowledgePlan Delegation Rule v0.1

**Status:** CONFORMANCE RULE FOR v0.4.6.2 SOURCE-TREE IMPLEMENTATION

## Principle

The canonical root Skill owns Context requirement semantics. `FeatureKnowledgePlan` is non-canonical and may only instantiate/specialize requirement classes already permitted by the active root Skill contract.

```text
Root canonical Skill@revision
    ↓ declares allowed Context requirement classes
FeatureKnowledgePlan
    ↓ binds/specializes for this Feature
ContextRequirement
    ↓
Context Bridge
```

It is invalid to reverse this authority relationship.

## MAY

`FeatureKnowledgePlan` MAY:

- bind an allowed requirement to an exact governed ProductAssetRef;
- parameterize an already-permitted bounded selector;
- evaluate a declared `CONDITIONAL` applicability predicate;
- specialize freshness/trust/authorization thresholds within the root Skill's allowed range;
- bind dependent criterion/requirement/finding IDs;
- select `ON_DEMAND` resolution timing already permitted by the root Skill;
- record why a permitted requirement is not applicable.

## MUST NOT

`FeatureKnowledgePlan` MUST NOT:

- invent a new authority dimension;
- introduce a new Context role/class not declared by the root Skill;
- upgrade `ON_DEMAND` or `CONDITIONAL` to a new global `REQUIRED` class unless the root Skill explicitly authorizes that transformation;
- create a new `NOT_CONTRACT_READY` cause outside root Skill preflight semantics;
- weaken root Skill trust/freshness/authorization requirements;
- change canonical artifact authority or gates.

## Fail-closed compilation

Compilation fails with `INVALID_FEATURE_KNOWLEDGE_PLAN` when any requested item cannot map to a root Skill-declared requirement template.

Missing resolution of a valid `REQUIRED` instantiated requirement may cause root Skill `NOT_CONTRACT_READY` exactly as already defined by the root Skill/Layer 1 Context contract.

## Required provenance

Every compiled ContextRequirement records:

- root_skill_id;
- root_skill_revision;
- root_requirement_template_id;
- feature_knowledge_plan_id/revision;
- exact ProductAssetRef when pre-bound;
- selector bounds;
- mode and applicability result;
- dependent claims.

## Revision discipline

If the current T1/T2 Skill packages do not declare the requirement classes needed by Option B, the Skill revision must be explicitly bumped and reviewed. A package/runtime patch MUST NOT silently expand canonical Skill semantics.
