# Non-proactive Delegation Spec

Work ID: `2026-08-26_non-proactive-delegation`
Short ID: `non-proactive-delegation`
Status: Approved
Harness release: `unknown`
Schema: `schema:spec.medium`
Companion plan: `plan_non-proactive-delegation.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `rule:lifecycle.documentation-assessment`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make the harness unambiguous that a platform rule against proactive sub-agent spawning is an authorization gate, not a rationale to omit the required delegation assessment or operator-approval request.

## Source and Intent

Source input:

1. The operator requested a stronger, reusable definition of the environment's sub-agent restriction and identified the harness router, canonical sub-agent policy, and medium/large strategy template as the intended surfaces.

Desired operator/user outcome:

1. Future agents assess potentially useful delegation and request authorization instead of silently choosing single-agent execution by citing the non-proactive restriction.

Success summary:

1. The canonical policy defines the restriction, and `SKILL.md` gives every route a compact reminder while leaving the small planning route free of the full sub-agent policy and strategy notation.

## Scope Boundary

### In scope

1. Add `rule:models.non-proactive-delegation` and its canonical meaning to the sub-agent policy.
2. Add a compact dispatch-gate reminder, strengthen the router outcome and completion checklist in `SKILL.md`, and explicitly preserve the small planning route's exclusion of `module:models`.
3. Strengthen the medium/large model-strategy source block and regenerate its assembled medium plan template.
4. Run the template assembler and harness policy validator.

### Non-scope

1. Change the platform-level delegation restriction or its enforcement.
2. Change model tiers, concurrency limits, or the independent-review contract.
3. Update historical work items or duplicate the canonical policy in unrelated templates.

## Repository Context

### Current state

1. `references/subagent-model-policy.md` requires assessment and operator approval for useful delegation, but does not name the non-proactive spawning restriction as a distinct dispatch-only rule.
2. `SKILL.md` routes sub-agent strategy work and has a completion checkbox, but its current wording can be read as permitting a silent `Sub-agents: None` decision. Its small planning route deliberately excludes `module:models` and must retain that lightweight boundary.
3. `assets/templates/blocks/plan.055.medium-and-large.model-strategy.md` prompts for authorization but does not explicitly reject that misreading. The assembled `medium-work-item-plan.md` is generated from this block.

### Evidence read

1. `.agents/skills/dev-doc-harness/SKILL.md`.
2. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
4. `.agents/skills/dev-doc-harness/references/maintenance-architecture.md`.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.055.medium-and-large.model-strategy.md`.
6. `.agents/skills/dev-doc-harness/assets/templates/medium-work-item-plan.md`.

### Constraints and compatibility

1. `module:models` remains the sole owner of reusable sub-agent authorization policy.
2. `SKILL.md` remains an operational router and checklist, while templates remain compact prompts rather than duplicated policy owners.
3. Generated templates must be changed through their source blocks and kept synchronized by the assembler.
4. The small planning route must not load `references/subagent-model-policy.md`, require a Model and Sub-agent Strategy, or record a sub-agent assessment merely because the compact reminder is present.

## Assumptions and Open Questions

### Assumptions

1. The current environment's non-proactive delegation restriction remains applicable when an agent considers dispatch.
2. The documented `economy-default` repository policy remains active.

### Open questions

1. None identified after repository-context review.

## Commitments and verification

### `SPEC-001` Define the dispatch gate

Statement:

1. `module:models` must define the non-proactive delegation constraint as preventing unapproved dispatch only, and must require assessment plus an operator-approval request when delegation could plausibly help.

#### `VER-001` Canonical policy is explicit

Covers: `SPEC-001`.

Criterion: The policy names `rule:models.non-proactive-delegation` and explicitly prohibits citing the constraint to silently select single-agent execution.

Expected evidence: Focused source inspection and a passing harness policy validator.

### `SPEC-002` Enforce the interpretation at operational use sites

Statement:

1. The router and medium/large strategy template must prompt agents to treat the constraint as a dispatch gate rather than as an exemption from assessment or an operator-approval request; the router must make the same compact reminder available to small planning without loading `module:models`.

#### `VER-002` Router and template prompt agree

Covers: `SPEC-002`.

Criterion: `SKILL.md` gives every route the compact dispatch-gate reminder, explicitly preserves the small route's `module:models` exclusion, and the model-strategy block contains wording consistent with `SPEC-001` without copying its full policy.

Expected evidence: Focused inspection and a passing harness policy validator.

### `SPEC-003` Preserve generated-template integrity

Statement:

1. The assembled medium plan template must reflect the changed strategy source block.

#### `VER-003` Generated template is synchronized

Covers: `SPEC-003`.

Criterion: The template assembler reports no stale generated output and the harness policy validator passes.

Expected evidence: Output from `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` and `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

## Architecture Decisions

Architecture snapshot status: Not applicable.

Decision summary:

1. Drivers: Prevent a policy loophole in future orchestration decisions.
2. Constraints: Preserve existing module ownership and generated-template assembly.
3. Selected approach: Put the full reusable rule in `module:models` and use short enforcement prompts in the router and template.
4. Affected boundaries: The canonical sub-agent policy, operational router, small planning route boundary, strategy template source, and generated medium plan template.
5. Rejected alternatives: Loading `module:models` for small planning would erase its intentionally compact route; duplicating full policy prose in the router/template would violate the ownership boundary; relying only on the canonical policy would leave a common checklist/template misreading unaddressed.
6. Validation cues: Template assembly and the policy validator confirm synchronization and structural policy consistency.

## Impact Surfaces

### Interfaces

1. The reusable rule identifier and strategy-template instructions consumed by harness users and planning artifacts.

### Data, config, and persistence

1. None.

### State and control flow

1. Planning-stage delegation flow becomes explicit: assess usefulness, request operator approval when useful, then dispatch only after approval.

### Safety, security, privacy, migration, and rollback

1. The change reduces process risk by preserving operator authority; rollback is a normal documentation revert if the rule needs revision.

## Risks and Rejected Alternatives

### `RISK-001` Duplicate-policy drift

Decision or mitigation:

1. Keep normative meaning in `module:models`; use only concise, linked enforcement language in `SKILL.md` and the template block.

Notes:

1. The harness validator is the structural regression check.

## Documentation assessment

- `DOC-TEST-CASE`: Not required — this is documentation policy, validated by the existing harness policy test.
- `DOC-TEST-GUIDE`: Not required — contributor test instructions do not change.
- `DOC-OPS-GUIDE`: Not required — the operator-facing behavior is specified directly in the maintained harness policy.
- `DOC-API-GUIDE`: Not required — no API changes.
- `DOC-ARCH-SUMMARY`: Not required — no repository-level architecture summary changes.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `spec: non-proactive-delegation` |
| Implementation | `docs: non-proactive-delegation -- enforce delegation approval gate` |

One cohesive documentation commit is planned after validation.

## Planning shape and transition ownership

1. Planning shape: `combined medium`.
2. Companion plan: `plan_non-proactive-delegation.md` is drafted and presented with this specification.
3. Transition owner: `plan_non-proactive-delegation.md` owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Goal, source and intent, scope, constraints, architecture decisions, commitment statements, and verifications are mutually consistent.
- [x] All relevant operator input is preserved in this specification.
- [x] Commitment statements are atomic, bounded, and cover the full scope.
- [x] Verification criteria cover all commitments without adding hidden scope.
- [x] This specification is self-contained for a fresh execution session.
- [x] Documentation assessment covers every required decision.
- [x] No unresolved placeholders, plan-affecting decisions, missing sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
