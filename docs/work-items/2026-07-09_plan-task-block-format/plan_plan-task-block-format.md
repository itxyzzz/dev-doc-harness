# Plan Task Block Format Plan

Work ID: `2026-07-09_plan-task-block-format`
Short ID: `plan-task-block-format`
Status: Approved
Harness release: `0.5+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:artifact-style`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Input Artifacts

Read these before implementation:

1. Approved spec: `docs/work-items/2026-07-09_plan-task-block-format/spec_plan-task-block-format.md`.
2. Architecture input: None; the spec records this as a template and policy-surface change without runtime architecture impact.
3. Required snapshots or deltas: None.
4. Relevant repository files:
   1. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md`
   2. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.020.common.traceability-approach-surfaces.md`
   3. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
   4. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
   5. `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`
   6. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
   7. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
   8. `.agents/skills/dev-doc-harness/references/artifact-style.md`
   9. `CHANGELOG.md`
5. Unresolved implementation context to confirm before editing: none identified.

## Spec Traceability

| Requirement or acceptance criterion | Primary tasks | Validation |
|---|---|---|
| `REQ-001` Sectioned task-block format | `T-001`, `T-002`, `T-003` | `V-001`, `V-002`, `V-005` |
| `REQ-002` Centralized spec traceability matrix | `T-001`, `T-002`, `T-003` | `V-003`, `V-005` |
| `REQ-003` Template regeneration and consistency | `T-003`, `T-005` | `V-001`, `V-002`, `V-005` |
| `REQ-004` Regression validation | `T-004`, `T-005` | `V-004`, `V-005` |
| `AC-001` Small/medium plan template uses task blocks | `T-001`, `T-003`, `T-005` | `V-001`, `V-005` |
| `AC-002` Phase-plan template uses task blocks | `T-001`, `T-003`, `T-005` | `V-002`, `V-005` |
| `AC-003` Plan traceability is centralized | `T-002`, `T-003`, `T-005` | `V-003`, `V-005` |
| `AC-004` Harness validator protects the task-block contract | `T-004`, `T-005` | `V-004`, `V-005` |
| `AC-005` Harness policy validation passes | `T-001`, `T-002`, `T-003`, `T-004`, `T-005`, `T-006` | `V-005`, `V-006` |

## Implementation Approach

Start with the generated-template source blocks, not the generated files. Update `plan.050.common.task-plan.md` so the `## Task Plan` prompt explains sectioned task blocks and shows `T-001` and `T-002` examples with `Dependencies`, `Implementation`, `Exit criteria`, and optional `Notes`. Keep per-task traceability optional and avoid checkbox syntax in the examples.

Then update `plan.020.common.traceability-approach-surfaces.md` so `## Spec Traceability` uses one review matrix for requirements and acceptance criteria. The matrix should not include risks by default; risk-specific implementation guidance belongs in task notes, boundaries, or a plan-specific risk section when needed.

After block edits, run the template assembler so the small/medium and phase-plan generated templates stay in sync. Add a focused validator check for the explicit current-template contract: generated plan templates must contain the traceability matrix headers and task-block field labels, and must not contain checkbox task examples under `## Task Plan`.

## Change Surfaces

Expected edits:

1. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md`: replace checkbox task prompt with sectioned task-block prompt.
2. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.020.common.traceability-approach-surfaces.md`: replace list-style traceability prompt with the centralized `REQ` and `AC` matrix prompt.
3. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`: regenerated output from source blocks.
4. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`: regenerated output from source blocks.
5. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: add a focused current-template contract check.
6. `CHANGELOG.md`: add planning and implementation entries before the relevant commits.

Stable interfaces:

1. Work-item folder naming, artifact filenames, freeze gates, planned commit rules, and model/sub-agent notation remain unchanged.
2. Historical work-item artifacts remain immutable snapshots and are not retrofitted.
3. The harness validator remains a structural/current-surface validator rather than a subjective semantic plan grader.

Changed interfaces:

1. Future harness plan templates ask agents to write sectioned task blocks instead of checkbox task rows.
2. Future plan traceability prompts use a matrix for requirements and acceptance criteria.

Implementation boundaries:

1. Do not update Superpowers upstream plan templates.
2. Do not add risk rows to the default plan traceability matrix.
3. Do not broaden validation into arbitrary historical plan-quality review.
4. Do not edit unrelated templates except generated outputs from the changed blocks.

## Model and Sub-agent Strategy

Current orchestration:

1. Model/profile and reasoning effort if known: not exposed.
2. Model-policy source: active repository policy from `AGENTS.md`, using `economy-default`.
3. Override scope and expiry: none.

Fit assessment:

1. Complexity: medium, because the implementation touches source blocks, generated templates, and harness validation.
2. Risk and blast radius: medium, because a bad prompt shape affects all future harness-generated plans.
3. Ambiguity: low after operator design approval.
4. Budget and latency fit: acceptable for one orchestration thread.

Recommended orchestration change:

1. None. Use the current main-thread orchestration with careful local validation.

Sub-agents:

1. None for implementation. The changes are tightly coupled across one shared block, generated templates, and validator expectations; main-thread integration is simpler and safer.

## Task Plan

### `T-001` Replace checkbox task prompt with sectioned task blocks

Dependencies:

1. None.

Implementation:

1. Modify `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md`.
2. Replace the checkbox task-row prompt with a task-block prompt that tells agents to write one `###` section per task.
3. Make `Dependencies`, `Implementation`, and `Exit criteria` required fields in each task block.
4. Make `Notes` optional for boundaries, gotchas, or risk-specific guidance.
5. Include example blocks for `T-001` and `T-002` without checkbox syntax.

Exit criteria:

1. The source block contains no `- [ ]` task examples.
2. The source block contains the field labels `Dependencies:`, `Implementation:`, and `Exit criteria:`.
3. The source block says per-task traces are optional when the central matrix already covers review needs.

Notes:

1. Keep the examples concise enough that the generated templates remain readable.

### `T-002` Convert spec traceability prompt to a review matrix

Dependencies:

1. None.

Implementation:

1. Modify `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.020.common.traceability-approach-surfaces.md`.
2. Replace separate requirement, acceptance, and risk coverage lists with a `Spec Traceability` matrix.
3. Use the columns `Requirement or acceptance criterion`, `Primary tasks`, and `Validation`.
4. Instruct agents to include `REQ` and `AC` rows in the default matrix.
5. State that risks stay out of the default matrix and should be covered in task notes, boundaries, or a plan-specific section when needed.

Exit criteria:

1. The traceability source block contains the agreed matrix headers.
2. The source block does not instruct agents to add default risk rows to the matrix.
3. The source block still preserves architecture coverage guidance outside the matrix when architecture input exists.

Notes:

1. Keep the matrix narrow enough for Markdown review.

### `T-003` Regenerate assembled plan templates

Dependencies:

1. `T-001`
2. `T-002`

Implementation:

1. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py`.
2. Review regenerated changes in `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`.
3. Review regenerated changes in `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`.
4. Confirm the generated files include the same traceability matrix and task-block prompt from the source blocks.

Exit criteria:

1. The assembled small/medium plan template uses sectioned task blocks.
2. The assembled phase-plan template uses sectioned task blocks.
3. Generated templates contain no checkbox task examples in `## Task Plan`.

Notes:

1. Do not hand-edit generated templates except as part of normal regeneration output.

### `T-004` Add validator coverage for the new current-template contract

Dependencies:

1. `T-001`
2. `T-002`
3. `T-003`

Implementation:

1. Modify `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Add a focused check that inspects current generated plan templates.
3. Assert that each current plan template contains the traceability matrix headers.
4. Assert that each current plan template contains `Dependencies:`, `Implementation:`, and `Exit criteria:` in the task-plan section.
5. Assert that each current plan template does not contain checkbox task examples for `T-001` or `T-002`.

Exit criteria:

1. The validator fails if a generated current plan template reintroduces checkbox task examples.
2. The validator fails if the required task-block field labels are absent.
3. The validator remains scoped to current templates, not historical work-item artifacts.

Notes:

1. Place the check near existing template/schema or placeholder current-surface checks if that matches the script organization.

### `T-005` Run harness validation and inspect the diff

Dependencies:

1. `T-003`
2. `T-004`

Implementation:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Inspect the diff for the changed source blocks, generated templates, and validator.
3. Confirm no unrelated template, policy, or historical artifact changed.
4. Confirm the validator output is successful before preparing the implementation commit.

Exit criteria:

1. Harness policy validation exits successfully.
2. Diff review shows only planned files plus `CHANGELOG.md`.
3. The generated templates match the source-block intent.

Notes:

1. If validation reveals existing unrelated failures, record the exact failure and stop for operator guidance rather than hiding it with unrelated fixes.

### `T-006` Update changelog and commit implementation

Dependencies:

1. `T-005`

Implementation:

1. Add a newest-first `CHANGELOG.md` entry for `2026-07-09_plan-task-block-format -- replace checklist task rows`.
2. Stage only the implementation files and `CHANGELOG.md`.
3. Commit with `docs: plan-task-block-format -- replace checklist task rows`.

Exit criteria:

1. Changelog entry title matches the planned implementation subject snippet.
2. Implementation commit contains only planned files.
3. Final report includes validation output, commit hash, and any variance.

Notes:

1. Implementation must begin only after this plan is approved and the operator gives a fresh post-freeze start instruction.

## Planned Commits

Planning approval commit:

1. Planned subject: `plan: plan-task-block-format`.
2. Changelog title or snippet: `2026-07-09_plan-task-block-format -- plan sectioned task blocks`.
3. Notes: approval commit for this spec, plan, and changelog entry.

Implementation commit:

1. Planned subject: `docs: plan-task-block-format -- replace checklist task rows`.
2. Changelog title or snippet: `2026-07-09_plan-task-block-format -- replace checklist task rows`.
3. Notes: update source blocks, generated plan templates, validator coverage, and changelog.

## Validation Plan

| ID | Command | Expected result |
|---|---|---|
| `V-001` | Manual review of `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` | `## Task Plan` uses sectioned `T-001` and `T-002` task blocks with required fields and no checkbox task examples. |
| `V-002` | Manual review of `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md` | Phase-plan `## Task Plan` uses the same sectioned task-block format and remains fresh-thread oriented. |
| `V-003` | Manual review of `## Spec Traceability` in both generated plan templates | Each template includes a matrix with `Requirement or acceptance criterion`, `Primary tasks`, and `Validation`, and risk rows are not part of the default matrix prompt. |
| `V-004` | Intentionally inspect `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after editing | Validator contains a current-template contract check for task-block fields, traceability matrix headers, and absence of checkbox task examples. |
| `V-005` | `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exits successfully with the new task-block contract check passing. |
| `V-006` | `git diff --cached` before implementation commit | Staged diff contains only planned implementation files and `CHANGELOG.md`. |

## Plan Variance Handling

Before implementation begins, edit this draft directly if the operator changes the approved design. After freeze, record nontrivial implementation variance in `docs/work-items/2026-07-09_plan-task-block-format/implementation-notes/variance-log.md`; use a plan amendment for changes that alter acceptance criteria, validation scope, or the selected task-block format.

## Planning Artifact Freeze Gate

Draft review state: approved by operator on 2026-07-09.
Approval commit: this planning freeze gate commit.
Post-freeze implementation authorization: not yet requested.

## Plan Readiness Checklist

- [x] Input artifacts and relevant repository context have been read and listed.
- [x] Every spec requirement and acceptance criterion has at least one task and one validation path.
- [x] Risks, scope boundaries, interfaces, and documentation decisions are either covered by tasks or explicitly marked as no-op with a reason.
- [x] Task detail is sufficient for a fresh implementation agent to execute without inventing task order, file scope, validation, or documentation steps.
- [x] Validation entries have exact commands, manual checks, review findings, or operator acceptance paths with expected signals.
- [x] Planned commits and changelog title snippets are synchronized.
- [x] Variance handling is clear for likely implementation drift.
- [x] The work still fits one orchestration thread with no sub-agents.
- [x] Sub-agent strategy follows `module:models`.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Completion Criteria

1. Acceptance criteria in `spec_plan-task-block-format.md` are met.
2. Required validation commands have been run and recorded.
3. Required documentation artifacts have been created or updated.
4. The frozen plan had enough detail for implementation to proceed safely.
5. `CHANGELOG.md` has a newest-first entry before each commit.
6. Commit subjects match approved planned subjects or recorded variance.
7. Variance log is current if variance occurs.
8. De-facto sub-agent use is reported if any unplanned sub-agent is later authorized.

## Approval

- Status: Approved
- Superseded by: None
