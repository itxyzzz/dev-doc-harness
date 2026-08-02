# Worktree Continuity Rules Spec

Work ID: `2026-07-29_worktree-continuity-rules`
Short ID: `worktree-continuity-rules`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_worktree-continuity-rules.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:freeze-gate`, `module:models`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`

## Purpose

Clarify how a post-freeze `new Codex task` continues work from a source worktree, and make the two continuity routes easy to scan without changing their authorization or execution semantics.

## Scope

Included:

1. Replace the dense `Continuity routes` bullets in `references/planning-freeze-gates.md` with short labeled subsections under `Continuity rules`.
2. Require an explicit Git starting state before creating a new Codex task.
3. Explain the source-worktree default, the carry-over effect of uncommitted changes, and the no-default-branch fallback rule.
4. Extend the harness policy test so this rule and its readable section heading remain present.

Excluded:

1. Changing the two permitted `Run in` values.
2. Changing task-creation APIs, Git operations, model policy, or task authorization.
3. Changing templates, README copy, or historical work-item artifacts.

## Repository Context

### Current state

1. `references/planning-freeze-gates.md` has a `### Continuity routes` section with one dense bullet for each of `new Codex task` and `same Codex task`.
2. The new-task bullet requires a copy-ready handoff and explicit creation approval, but does not select the Git state from which the task worktree begins.
3. The current Codex task-creation capability uses the project default branch when no starting state is supplied. A `working-tree` starting state includes the source checkout and its uncommitted changes.
4. `scripts/test_harness_policy.py` asserts the existing continuity labels but does not protect source-baseline selection.

### Evidence read

1. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.
2. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
3. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
4. Official Codex worktree guidance: <https://learn.chatgpt.com/docs/environments/git-worktrees.md>.

### Constraints and compatibility

1. A new task must remain an isolated worktree; it must not share the source task's mutable checkout or branch.
2. The source baseline is a task-creation detail at the freeze boundary, so it belongs in `module:freeze-gate`, not in frozen plan templates.
3. The two canonical continuity values remain exactly `new Codex task` and `same Codex task`.
4. Preserve the existing explicit creation approval, manual fallback, and no-silent-substitution safeguards.

## Commitments and verification

### `SPEC-001` Select a new-task source baseline

Statement:

1. The new-task continuity rule must require the source Git starting state to be selected and reported before task creation; it must state that omitting it uses the project default branch.
2. The rule must direct a detached managed-worktree source to use `working-tree`, explain that uncommitted changes are copied, and require explicit handling when those changes are unrelated or should not continue.

#### `VER-001` New task starts from the intended source state

Covers: `SPEC-001`.

Criterion: The canonical continuity rule makes source-baseline selection, dirty-worktree disclosure, and the no-default-branch fallback discoverable in one place.

Expected evidence: A focused policy-test assertion and manual inspection of the new-task subsection pass.

### `SPEC-002` Make continuity routes scannable

Statement:

1. The continuity section must use a `Continuity rules` heading and separate labeled subsections for `new Codex task` and `same Codex task`.
2. The reformat must preserve the existing authorization, operator override, and post-freeze startup semantics.

#### `VER-002` Continuity routes retain their behavior

Covers: `SPEC-002`.

Criterion: The policy test confirms the two canonical route labels and new readable heading, while review confirms the pre-existing safeguards remain.

Expected evidence: `test_harness_policy.py` passes and a diff review finds no unintended lifecycle-policy changes.

## Architecture Decisions

Architecture snapshot status: Not applicable. This is a local policy-document structure and runtime-parameter clarification; it does not introduce a work-item architecture boundary.

Decision summary:

1. Drivers: Prevent a new task from receiving the correct frozen package while starting from an unrelated default-branch checkout.
2. Constraints: Source worktrees may be detached and may contain operator-owned uncommitted files.
3. Selected approach: Add a concise starting-state decision flow within the new-task subsection and retain two top-level canonical route labels.
4. Affected boundaries: Freeze-gate policy and its deterministic validation script.
5. Rejected alternatives: A third continuity value would blur task continuity with Git baseline choice; frozen templates would record runtime-specific state too early; README changes duplicate the canonical rule.
6. Validation cues: `VER-001`, `VER-002`, and the full harness policy test.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. The operator-facing post-freeze task-creation instruction changes; public APIs and repository runtime interfaces do not.

### Data, config, and persistence

1. None.

### State and control flow

1. The existing `new Codex task` transition gains an explicit source-baseline selection before task creation. The existing `same Codex task` transition is structurally separated but behaviorally unchanged.

### Safety, security, privacy, migration, and rollback

1. The clarification reduces accidental continuation from an unrelated checkout. It must disclose copied uncommitted files before an operator approves task creation.
2. Rollback is a revert of the documentation and validator commit.

## Risks and Rejected Alternatives

### `RISK-001` Dirty source worktree is copied unintentionally

Decision or mitigation:

1. Require the new-task subsection to report uncommitted paths and state that `working-tree` copies them. Route unrelated or excluded files to an explicit source branch/ref or current-task continuation rather than an implicit default-branch task.

### `RISK-002` Readability change weakens lifecycle safeguards

Decision or mitigation:

1. Preserve the existing sentences governing explicit creation approval, manual creation, runtime overrides, and startup rehydration; validate the two canonical route labels with the policy test.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: worktree-continuity-rules -- define the documentation change` |
| Implementation | `docs: worktree-continuity-rules -- clarify new-task worktree baselines` |

One cohesive implementation commit is planned.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-29_worktree-continuity-rules/changelog/*.md` | Create planning and implementation fragments at their respective commits. |
| Root changelog consolidation | Living | No | Not applicable | `CHANGELOG.md` | Root consolidation is a later operator-owned checkpoint. |
| Test cases | Snapshot | No | Not applicable | `snapshots/test-cases.snapshot.md` | The deterministic harness policy test is the durable executable check. |
| Testing guide delta | Living delta | No | Not applicable | `deltas/testing-guide.delta.md` | No project test workflow changes. |
| Operator manual delta | Living delta | No | Not applicable | `deltas/operator-manual.delta.md` | The changed canonical policy is itself the operator-facing guidance. |
| API reference delta | Living delta | No | Not applicable | `deltas/api-reference.delta.md` | No API changes. |
| Architecture snapshot | Snapshot | No | Not applicable | `snapshots/architecture.snapshot.md` | No work-item architecture decision beyond local policy wording. |
| Architecture summary delta | Living delta | No | Not applicable | `deltas/architecture-summary.delta.md` | No repository architecture change. |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_worktree-continuity-rules.md` is drafted with this spec.
3. Transition owner: `plan_worktree-continuity-rules.md` owns the implementation handoff after the combined package freezes.
4. Next activity: Update the canonical freeze-gate section and the focused policy test, then run the harness policy test.

## Approval

- Status: Approved
- Superseded by: None
