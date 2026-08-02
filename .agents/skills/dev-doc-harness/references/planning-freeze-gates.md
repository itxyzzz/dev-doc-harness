# Planning Freeze Gates

This document is the canonical source for approval-first planning gates between durable planning and implementation.

Module: `module:freeze-gate`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:freeze.draft-review` | `## Draft review checkpoint` |
| `rule:freeze.approval-freeze` | `## Approval freeze checkpoint` |
| `rule:freeze.stop-before-implementation` | `## Approval freeze checkpoint` |
| `rule:freeze.multi-gate-flow` | `## Multiple gates for very large or phased work items` |
| `rule:freeze.compatibility` | `## Compatibility` |

## When to use this workflow

Use this workflow whenever one of these durable planning artifacts is ready for operator review or approval:

- `<spec-filename>`
- `<plan-filename>`
- `<phase-plan-filename>`
- `<amendment-filename>`

Use `rule:naming.derived-patterns` for the current filename expansions.

Draft artifacts may be edited until the operator explicitly approves them and the approval commit is created. After that approval commit, the artifacts are frozen and follow the immutable snapshot rules in `artifact-contract.md`.

## Draft review checkpoint

Before committing any planning artifacts for approval:

1. Draft or update the required planning artifacts.
2. Verify package completeness before draft review: a normal combined small/medium package contains both `<spec-filename>` and `<plan-filename>`. A small/medium spec-only package is reviewable only when it records the operator-requested or operator-approved staged reason, identifies the spec-only frozen package, and names `plan drafting` as its next lifecycle stage. A large/phased anchor remains a valid anchor-spec-only package.
3. Verify that the drafts contain no placeholders, undecided required items, or missing required sections unless the undecided item is explicitly marked as deferred with a reason and owner.
4. Verify the worktree status, stage only the draft planning artifacts being reviewed, and do not commit them.
5. Present the staged package in chat with a **Next-stage recommendation** projected from `rule:models.selection-dimensions`: **Next lifecycle stage** renders `Stage: <documented lifecycle stage>` from `rule:lifecycle.stage-boundaries`; **Orchestration** gives Method, Orchestration mode, `Run in`, and Review; **Model** gives Generation, Capability tier, and Reasoning; **Fallbacks and limits** includes only applicable limits. Mirror the stage-appropriate values already resolved in the draft rather than redefining their applicability here. Confirm the upcoming-stage sub-agent assessment and authorization state; record `Sub-agents: None` with a stage-specific fit reason when no delegation is useful.
6. Ask the operator to approve the staged planning package or provide feedback.
7. If the operator provides feedback, edit the draft artifacts directly, refresh the staged planning package, and ask for approval again.

Do not create a plan amendment for feedback received before the planning package is frozen.

## Approval freeze checkpoint

After the operator explicitly approves the staged planning package:

1. Update every approved artifact's status fields from draft or proposed state to approved state before staging. This includes the top-level `Status:` line and any status line in an `Approval` section.
2. Recheck the draft-review package-completeness and artifact-completeness requirements before approval freeze.
3. Verify again that the approved artifacts contain no placeholders, undecided required items, or missing required sections unless the undecided item is explicitly marked as deferred with a reason and owner.
4. Verify the approved artifacts include a planned approval commit subject following `rule:lifecycle.commit-message-format`.
5. Verify the worktree status, stage only the approved planning artifacts, and commit only those staged paths together using the planned approval commit subject. Do not stage or commit unrelated pre-existing operator work, root `CHANGELOG.md`, or implementation edits during a plan-only checkpoint.
7. Treat the package as frozen only after the approval commit. From that point onward, high-impact changes use the amendment process from `artifact-contract.md`.
8. Stop before implementation, task execution, or the next planning stage. Implementation must not begin in the same agent turn as the approval freeze checkpoint.
9. Report the commit hash and approved artifact paths.
10. Remind the operator that they may push and create a draft plan-only PR. If context visibility is exposed, report the available signal; otherwise do not infer an exact compaction threshold. Operator-requested compaction remains optional and runtime-managed compaction remains platform-owned.
11. Confirm that the frozen package distinguishes optional current-session diagnostics from **Next-stage recommendation** defined under `## Draft review checkpoint`. In chat, present these four **Next-stage recommendation** groups relabeled as **Approved next stage** and mirror the frozen artifact values. Reconfirm the upcoming-stage sub-agent assessment and authorization state, then present the corresponding route through `## Post-freeze transition routing` below. Do not use a universal current-session start question when the approved route is a new session.

## Post-freeze transition routing

### Authorization and effective selection

A fresh operator response after the freeze may authorize the action offered by the selected continuity route when the response clearly approves that action. The planned execution method starts after that fresh authorization without a second generic method question.

A fresh explicit operator start instruction may instead override the approved method, model/profile, reasoning effort, or next-stage continuity. At execution handoff, present the effective next-stage values: start with the frozen **Approved next stage** and apply any explicit operator override. Record the actual runtime selection in the completion report without rewriting the frozen artifact or requiring a plan amendment solely for that runtime choice. Use the variance log only when the override creates a noteworthy allowed variance under `rule:lifecycle.variance-policy`. Report a concrete availability or compatibility blocker, and apply variance policy when the instruction changes a material scope, commitment, Plan Task, commit boundary, mandatory review, or safety boundary.

If the selected route cannot use independent review or the operator declines it, apply `module:models` before execution: disclose the assurance gap, obtain or record the one operator decision, and preserve its completion-report evidence.

The harness transition completes before Superpowers pre-flight or execution begins. After a fresh implementation instruction, complete the approved plan without pausing between planned tasks; ask only for an external, destructive, costly, or material scope-expanding action.

### Route inputs

Before rendering a handoff or offering task creation, read these values from the approved package:

1. Planning shape: combined small/medium, explicit staged small/medium, large/phased anchor, plan, phase plan, or amendment.
2. Frozen package: the exact approved spec, applicable plan or phase plan, required snapshots, applicable amendments, required evidence, and any other current input named by the plan.
3. Next lifecycle stage: the documented planning, implementation, review, or replanning stage that follows this actual boundary.
4. Transition owner: the plan for a combined small/medium implementation handoff, the staged spec for an explicit plan-drafting exception, or the phase plan for its documented phase transition.

### Continuity rules

Then apply the approved next-stage continuity and current capability:

#### `new orchestration session`

1. Display the copy-ready handoff as a primary conversation result. Include the instructions, harness, exact frozen package, amendments or variance, approval/baseline, documented next lifecycle stage, and variance stop without restating frozen requirements. Mirror the **Approved next stage** groups in chat.
2. Before offering compatible task creation, select and report the Git starting state. Use a named branch or ref when it is the approved baseline. For a detached managed-worktree source, use `working-tree`; it copies the source checkout and its uncommitted changes. Disclose the copied uncommitted paths. When those files are unrelated or should not continue, require an explicit source branch or ref, or same-orchestration-session continuation. Omitting the starting state uses the project default branch and is prohibited for this route.
3. When compatible task creation is available, ask for explicit approval specifically to create the task; this is the default continuation action for the `new orchestration session` route. Only after that approval may the platform action create the task with the displayed handoff as its initial prompt and the exact supported recorded model and reasoning configuration. Report the created task and do not begin its activity in the source task.
4. Use manual operator creation only when task creation is unavailable or incompatible, or when the operator specifically requests it; state the limitation and display the same copy-ready handoff.
5. Do not silently substitute a model, reasoning effort, orchestration mode, or task-creation action.

#### `same orchestration session`

Keep the current-session authorization route separate and use the fresh explicit start authorization described above. A fresh operator response may both confirm execution settings and authorize implementation when it clearly says to begin, such as `Confirmed, proceed`, `Confirm and start`, or equivalent wording. If the operator only confirms settings without clear start authorization, ask a concise follow-up about whether implementation should begin now. A bare `Confirm` authorizes same-session implementation only when the post-freeze prompt explicitly states that confirming also means beginning implementation now.

Every governed planning, execution, or resumed amended stage records one canonical `Run in` value before this routing is applied.

An operator may explicitly override a recorded `new orchestration session` selection and continue in the same orchestration session. Present this only as an opt-in override, not as a question or recommended alternative.

After fresh authorization, `rule:execution-quality.execution-thread-start` is the consumer-side startup protocol. A new orchestration session loads the instructions, harness, exact frozen package, amendments or variance, approval/baseline, documented next lifecycle stage, and variance stop; a same-session route rereads the package after a model switch or recorded continuity risk.

## Multiple gates for very large or phased work items

Large or phased work items normally pass through multiple freeze gates:

- Anchor spec freeze: after `<spec-filename>` is approved. This gate pauses before implementation and before later phase-plan drafting; phase-plan drafting resumes only after fresh operator instruction.
- Phase-plan freeze: after one or more `<phase-plan-filename>` files are approved.
- Amendment freeze: after any high-impact `<amendment-filename>` is approved.

Use the same draft review and approval freeze checkpoints each time. `rule:lifecycle.large-phase-orchestration` owns the large/phased planning order, and `rule:lifecycle.planning-shape` distinguishes combined and explicitly staged small/medium packages; this freeze-gate rule owns the approval mechanics and continuity-selected conversation result at each actual stop.

## Compatibility

This gate layers on top of Codex plan mode, Superpowers, and spec-kit. Those tools may produce or refine the artifacts, but the harness owns the approval, commit, and pause transition before implementation.

If another workflow would normally continue directly from approved planning into execution, pause and run this gate instead. The next operator response may authorize implementation and select any execution methodology or tool, including Superpowers.
