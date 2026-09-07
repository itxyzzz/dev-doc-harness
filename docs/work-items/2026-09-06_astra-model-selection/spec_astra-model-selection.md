# Astra Model Selection Spec

Work ID: `2026-09-06_astra-model-selection`
Short ID: `astra-model-selection`
Status: Approved
Harness release: `0.10+`
Schema: `schema:spec.medium`
Companion plan: `plan_astra-model-selection.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:models.selection-dimensions`, `rule:models.efficiency-first`

## Goal

Make the generation and model mapping unambiguous after GPT-6.0 Astra: GPT-5.6/Terra remains the normal bounded-work default, while Astra is latest but available only where the policy already justifies a Sol-equivalent flagship escalation.

## Source and Intent

Source input:

1. The operator reported that the current instructions could make Astra appear to be the regular-work choice after its release.

Desired operator outcome:

1. Future planning and execution agents select the GPT-5.6 Terra baseline for regular work and do not infer that Astra replaces it merely because Astra is newer.

Success summary:

1. The canonical policy, examples, templates, and validator state the GPT-5.6/Terra default, Astra's latest-but-not-default status, and the Astra/Sol escalation boundary in plain language.

## Scope Boundary

### In scope

1. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` current provider mapping, generation-selection rule, profile-local selection guidance, and escalation wording.
2. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md` reusable role examples that currently select `latest available`.
3. The model-generation placeholders in source blocks, generated templates, and amendment template.
4. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` assertions and fixtures for the required policy constraints and explicit-generation guidance.

### Non-scope

1. Changing vendor-neutral capability tiers, reasoning-effort definitions, orchestration modes, historical work items, or runtime model availability.
2. Treating Astra as a new default, a Terra replacement, or a general provider catalog.

## Repository Context

### Current state

1. The canonical policy maps GPT-5.6 Sol to `flagship`, Terra to `balanced`, and Luna to `fast/economy`; both active policy profiles already use Terra medium for normal bounded work.
2. The policy does not mention GPT-6.0 Astra, distinguish its newer generation from the retained GPT-5.6 default, or state its relationship to the Sol escalation path.
3. Reusable sub-agent examples and plan-template generation fields say `latest available`, which would make Astra look like the normal choice.
4. The policy validator checks the GPT-5.6 mapping and Terra/Sol escalation anchors but not the explicit-generation or Astra constraints.

### Evidence read

1. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
2. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.medium.handoff.md`.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.phase.handoff.md`.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md`.
6. `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`.
7. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
8. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
9. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`.
10. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.

### Constraints and compatibility

1. Preserve the durable `flagship`, `balanced`, and `fast/economy` vocabulary; concrete model names remain a current provider mapping.
2. GPT-6.0 Astra is the latest concrete model, but GPT-5.6 remains the default generation for regular bounded work.
3. The active repository policy is `efficiency-first`; its GPT-5.6 Terra-medium baseline must remain explicit.
4. Astra can be named only as a Sol-equivalent concrete alternative for a justified `flagship` escalation, never as the regular-work default.
5. Active templates and examples must require a policy-selected concrete generation and must not say or imply that newest/latest available is the default.
6. The implementation must follow the harness policy validator and keep the change limited to active model-selection guidance, its generated templates, and regression checks.

## Assumptions and Open Questions

### Assumptions

1. The operator's requested relationship applies to both `quality-first` and `efficiency-first` policy readers, so shared generation/mapping constraints are preferable to divergent profile-local rules.

### Open questions

1. None identified after repository-context review.

## Commitments and verification

### `SPEC-001` Preserve the GPT-5.6 Terra default and constrain Astra

Statement:

1. The canonical model policy must say that GPT-6.0 Astra is the latest concrete model but not the default, GPT-5.6 remains the default generation for regular bounded work, Terra remains that work's baseline, and Astra may be used only as a Sol-equivalent alternative after the existing flagship-escalation criteria are met.

#### `VER-001` Explicit policy relationship

Covers: `SPEC-001`.

Criterion: The current mapping and selection guidance make the GPT-5.6/Terra default and Astra/Sol boundary discoverable without inferring a default from model recency.

Expected evidence: Targeted policy-text assertions and manual diff review of the Model selection section.

### `SPEC-002` Remove latest-as-default guidance and guard it against regression

Statement:

1. Active role examples and model-generation templates must require the generation selected by policy or explicit operator override; they must not direct agents to choose a model because it is latest.
2. The harness policy validator must fail when the GPT-5.6 default, Terra baseline, latest-but-not-default Astra status, Astra's Sol-equivalent-only constraint, or explicit-generation guidance is removed.

#### `VER-002` Regression assertion

Covers: `SPEC-002`.

Criterion: The validator contains normalized-text assertions for the generation, baseline, and escalation constraints, rejects obsolete latest-as-default guidance in the active selection surfaces, and completes successfully after the policy update.

Expected evidence: A deliberate pre-documentation failing run followed by a passing full validator run.

## Architecture Decisions

Architecture snapshot status: Not applicable. The work changes local model-selection wording and its test only; it does not alter a repository boundary, interface, data flow, or lifecycle architecture.

Decision summary:

1. Selected approach: add shared generation and concrete-mapping constraints, replace generic latest-generation prompts with policy-selected-generation prompts, retain the existing Terra profile bullets, and test the plain-language invariants.
2. Rejected alternative: treat the newest available model as the default generation or add Astra as a regular-work profile. Either choice contradicts the operator's required GPT-5.6/Terra default.

## Impact Surfaces

### Interfaces

1. The policy text read by future harness users and agents.

### Data, config, and persistence

1. None.

### State and control flow

1. Model-selection decision flow first selects an explicit generation from policy, then applies an explicit Astra gate before a Sol-equivalent concrete profile is chosen.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, migration, or runtime rollout impact. Reverting the cohesive documentation-and-test commit restores the prior policy.

## Risks and Rejected Alternatives

### `RISK-001` Ambiguous recency wording reintroduces a new default

Decision or mitigation:

1. Use direct normative wording for the generation, Terra, and Astra constraints; replace active latest-available prompts; and regression-test the exact normalized phrases rather than relying on the historical GPT-5.6 mapping assertion.

## Documentation assessment

- `DOC-TEST-CASE`: Not required.
- `DOC-TEST-GUIDE`: Not required.
- `DOC-OPS-GUIDE`: Not required.
- `DOC-API-GUIDE`: Not required.
- `DOC-ARCH-SUMMARY`: Not required.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `docs: astra-model-selection-plan` |
| Implementation | `docs: constrain-astra-model-selection` |

## Planning shape and transition ownership

1. Planning shape: `combined medium`.
2. Companion plan: `plan_astra-model-selection.md` is drafted with this spec.
3. Transition owner: `plan_astra-model-selection.md` owns the `plan execution` transition after freeze.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Goal, scope, constraints, commitments, and verification are mutually consistent.
- [x] Operator input is preserved in this specification.
- [x] Commitments are bounded and have local verification criteria.
- [x] Architecture snapshot is correctly not applicable.
- [x] Documentation assessment is complete.
- [x] No unresolved plan-affecting decision or ownerless deferral remains.

## Approval

- Status: Approved
- Superseded by: None
