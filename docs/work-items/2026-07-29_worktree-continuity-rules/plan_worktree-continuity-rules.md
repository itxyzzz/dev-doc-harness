# Worktree Continuity Rules Plan

Work ID: `2026-07-29_worktree-continuity-rules`
Short ID: `worktree-continuity-rules`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`
Execution method: `superpowers:executing-plans`
Current planning Codex task: Model/profile, reasoning, and context visibility: not exposed.

## Input Artifacts

1. Draft spec: `spec_worktree-continuity-rules.md`.
2. Architecture input: None; the spec records why an architecture snapshot is not applicable.
3. Required snapshots or deltas: None.
4. Relevant repository files: `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`, `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, and `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
5. Unresolved implementation context to confirm before editing: None. The user approved the explicit-starting-state approach and requested readability improvements.

## Change Surfaces

1. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: Rename and restructure the continuity section; add the Git starting-state decision flow to the new-task route.
2. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: Make the lifecycle transition policy test require the readable section and source-baseline safeguards.
3. `docs/work-items/2026-07-29_worktree-continuity-rules/changelog/implementation.md`: Record the implementation commit before it is created.

## Implementation Approach

1. Add the policy-test expectation first and run it to demonstrate that the current guidance lacks the new structure and starting-state rule.
2. Replace the two dense route bullets with a `Continuity rules` heading, two labeled route subsections, and short ordered steps.
3. Keep the existing post-freeze behavior intact; add only the Git-baseline selection and dirty-worktree disclosure before compatible new-task creation.
4. Run the focused and full harness checks, then review the diff for preservation of the two canonical route labels and no unrelated changes.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: None.
2. Fit reason: The policy wording and its single deterministic validator are tightly coupled; independent delegation would add coordination cost without improving isolation or review quality.
3. Authorization state: Not needed.

## Implementation Tasks

### `TASK-001` Add and prove the continuity policy rule

Dependencies: Approved combined planning package and fresh operator start authorization.

Interfaces:

1. Consumes: `SPEC-001`, `SPEC-002`, the existing post-freeze route text, and the current lifecycle transition policy test.
2. Produces: A readable canonical continuity section and a validator that detects regression of the starting-state rule.

Implementation:

1. In `scripts/test_harness_policy.py`, extend `assert_lifecycle_transition_targets()` to require the `Continuity rules` heading plus language for explicit Git starting-state selection, `working-tree` behavior, disclosure of uncommitted files, and the no-default-branch fallback.
2. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and confirm it fails because the current continuity section has the old heading and no starting-state rule.
3. In `references/planning-freeze-gates.md`, replace the two dense bullets with a `### Continuity rules` section containing `#### New Codex task` and `#### Same Codex task` subsections. Preserve the two route labels as the canonical `Run in` values.
4. In the new-task subsection, add a short ordered Git-baseline rule: select and report the starting state; use a named branch/ref when it is the approved baseline; use `working-tree` for a detached managed-worktree source; disclose copied uncommitted paths; and require an explicit source branch/ref or current-task continuation when those files should not continue. State that omitting starting state uses the project default branch and is prohibited for this route.
5. Retain the existing explicit creation approval, exact supported model/reasoning configuration, manual fallback, no-silent-substitution, operator override, and startup rehydration requirements in their appropriate route or surrounding prose.

Exit criteria: The text is scannable, captures every `SPEC-*` statement, and the policy test passes after the documentation change.

## Plan Checks

### `CHECK-001` Harness policy continuity regression test

Covers: `VER-001`, `VER-002`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after the test-first change and again after the canonical policy update.

Expected result: The first run fails specifically on the newly required continuity heading or source-baseline language; the final run reports all checks passed.

### `CHECK-002` Focused policy diff review

Covers: `VER-002`.

Method: Review `git diff --check` and `git diff -- .agents/skills/dev-doc-harness/references/planning-freeze-gates.md .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: No whitespace errors, unrelated edits, missing canonical route labels, or loss of existing authorization and fallback requirements.

## Planned Commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: worktree-continuity-rules -- define the documentation change` |
| Implementation | `docs: worktree-continuity-rules -- clarify new-task worktree baselines` |

One cohesive implementation commit is planned.

## Validation and Variance

`CHECK-001` is the required automated evidence. `CHECK-002` is the required policy-preservation review. Any change to the two canonical continuity values, task-creation authorization, or the scope beyond these two files is a material variance and requires operator direction before implementation proceeds.

## Implementation Handoff

### Next-stage recommendation

#### Activity

Next activity: Update the canonical continuity rules and regression test; First Plan Task: `TASK-001`.

#### Orchestration

Method: `superpowers:executing-plans`; Run in: `new Codex task`; Plan Task reviewers: route-specific reviewer capability disclosure, followed by focused self-review if an independent reviewer is unavailable.

#### Model

Model: active `economy-default` balanced tier; Reasoning: medium.

#### Fallbacks and limits

Load the frozen spec and plan before editing. Sub-agents are not needed. Stop for any material variance to the canonical continuity values, authorization behavior, or file scope.

1. Frozen package: `spec_worktree-continuity-rules.md` and `plan_worktree-continuity-rules.md`.
2. Artifact rehydration: Read the frozen package, `planning-freeze-gates.md`, and the lifecycle transition policy test before `TASK-001`.
3. Variance stop condition: Obtain operator direction before altering route semantics, task-creation authorization, or files outside the documented scope.

## Approval

- Status: Approved
- Superseded by: None
