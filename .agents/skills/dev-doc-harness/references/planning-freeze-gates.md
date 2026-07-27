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

Draft artifacts may be edited until the operator explicitly approves them and the approval commit is created, or until the operator explicitly asks for a handoff snapshot. After that approval commit or explicit handoff snapshot, the artifacts are frozen and follow the immutable snapshot rules in `artifact-contract.md`.

## Draft review checkpoint

Before committing any planning artifacts for approval:

1. Draft or update the required planning artifacts.
2. Verify package completeness before draft review: a normal combined small/medium package contains both `<spec-filename>` and `<plan-filename>`. A small/medium spec-only package is reviewable only when it records the operator-requested or operator-approved staged reason, identifies the spec-only frozen package, and names `plan drafting` as its next activity. A large/phased anchor remains a valid anchor-spec-only package.
3. Verify that the drafts contain no placeholders, undecided required items, or missing required sections unless the undecided item is explicitly marked as deferred with a reason and owner.
4. Verify the worktree status, stage only the draft planning artifacts being reviewed, and do not commit them.
5. Ask the operator to approve the staged planning package or provide feedback.
6. If the operator provides feedback, edit the draft artifacts directly, refresh the staged planning package, and ask for approval again.

Do not create a plan amendment for feedback received before the planning package is frozen.

## Approval freeze checkpoint

After the operator explicitly approves the staged planning package, or explicitly asks for a handoff snapshot:

1. Update the matching changelog source fragment under `docs/work-items/<work-id>/changelog/*.md` with a newest-first entry for the approved artifact set.
2. When the operator approved the package rather than requesting only a handoff snapshot, update every approved artifact's status fields from draft or proposed state to approved state before staging. This includes the top-level `Status:` line and any status line in an `Approval` section.
3. Verify package completeness before approval freeze: a normal combined small/medium package contains both `<spec-filename>` and `<plan-filename>`. A small/medium spec-only package is valid only with its operator-requested or operator-approved staged reason and `plan drafting` next activity; a large/phased anchor remains anchor-spec-only.
4. Verify again that the approved artifacts contain no placeholders, undecided required items, or missing required sections unless the undecided item is explicitly marked as deferred with a reason and owner.
5. Verify the approved artifacts include a planned approval commit subject following `rule:lifecycle.commit-message-format`, and verify the changelog source fragment entry title snippet matches that planned subject.
6. Verify the worktree status, stage only the approved planning artifacts and their changelog source fragment, and commit only those staged paths together using the planned approval commit subject. Do not stage or commit unrelated pre-existing operator work, generated files, root `CHANGELOG.md`, or implementation edits during a plan-only checkpoint.
7. Stop before implementation, task execution, or the next planning stage.
8. Report the commit hash and approved artifact paths.
9. Remind the operator that they may push and create a draft plan-only PR. If context visibility is exposed, report the available signal; otherwise do not infer an exact compaction threshold. Operator-requested compaction remains optional and runtime-managed compaction remains platform-owned.
10. Confirm that the frozen package distinguishes the Current planning Codex task from the **Approved next stage**. In chat, mirror its four groups in order: **Activity**, **Orchestration**, **Model**, and **Fallbacks and limits**. Use Method, Run in, First Plan Task, Plan Task reviewers, Model, Reasoning, and only applicable limits. Confirm the upcoming-stage sub-agent assessment and authorization state; record `Sub-agents: None` with a stage-specific fit reason when no delegation is useful.
11. Select and present the post-freeze result through `## Post-freeze transition routing` below. Do not use a universal current-task start question when the approved route is a new task.

Stage root `CHANGELOG.md` during this checkpoint only when the operator is intentionally consolidating fragments as part of the same approved package. In normal independent worktree planning, consolidation is a later operator-owned checkpoint.

The planning package is frozen only after the approval commit or explicit handoff snapshot. From that point onward, high-impact changes use the amendment process from `artifact-contract.md`.

Implementation must not begin from a frozen durable plan in the same agent turn as the approval freeze checkpoint. A fresh operator response after this gate may authorize the action offered by the selected continuity route when the response clearly approves that action.

The planned execution method starts after that fresh authorization without a second generic method question. A fresh explicit operator start instruction may instead select another available method, model/profile, reasoning effort, or Codex-task continuity; record the actual selection and do not require or debate a plan amendment solely for that runtime choice. Report a concrete availability or compatibility blocker, and apply variance policy only when the instruction changes a material scope, commitment, Plan Task, commit boundary, mandatory review, or safety boundary.

At draft review, show a **Next-stage recommendation** in chat using those same four groups. At freeze, show the matching **Approved next stage**. At execution handoff, repeat the approved groups rather than reinterpreting them. A new Codex task loads the instructions, harness, exact frozen package, amendments or variance, approval/baseline, First Plan Task, and variance stop. A same-task route rereads the package after a model switch or recorded continuity risk.

For a `same task` route, a fresh operator response may both confirm execution settings and authorize implementation when it clearly says to begin, such as `Confirmed, proceed`, `Confirm and start`, or equivalent wording. If the operator only confirms settings without clear start authorization, ask a concise follow-up about whether implementation should begin now. A bare `Confirm` authorizes same-task implementation only when the post-freeze prompt explicitly states that confirming also means beginning implementation now.

## Post-freeze transition routing

Before rendering a handoff or offering task creation, read these values from the approved package:

1. Planning shape: combined small/medium, explicit staged small/medium, large/phased anchor, plan, phase plan, or amendment.
2. Frozen package: the exact approved spec, applicable plan or phase plan, required snapshots, applicable amendments, required evidence, and any other current input named by the plan.
3. Next activity: the documented planning, implementation, review, or replanning activity that follows this actual boundary.
4. Transition owner: the plan for a combined small/medium implementation handoff, the staged spec for an explicit plan-drafting exception, or the phase plan for its documented phase transition.

Then apply the approved execution continuity and current capability:

- `new Codex task`: display the copy-ready handoff as a primary conversation result. Include the instructions, harness, exact frozen package, amendments or variance, approval/baseline, First Plan Task, and variance stop without restating frozen requirements. Mirror the Approved next stage groups in chat.
- Compatible task creation: ask for explicit approval specifically to create the task. Only after that approval may the platform action create it with the displayed handoff as its initial prompt and the exact supported recorded model and reasoning configuration. Report the created task and do not begin its activity in the source task.
- Unavailable or incompatible task creation: state which action or recorded configuration is unavailable and display the same manual copy-ready handoff. Do not silently substitute a model, reasoning effort, orchestration mode, or task-creation action.
- `same task`: keep the current-task authorization route separate and use the fresh explicit start authorization described above.
- Justified alternative: follow only the explicit transition recorded in the approved package; do not infer task creation or same-task authorization.

An operator may explicitly direct continuation in the current task despite a recorded new-task recommendation. Present this only as an opt-in override, not as a question or recommended alternative.

## Multiple gates for very large or phased work items

Very large or phased work items may have multiple freeze gates:

- Anchor spec freeze: after `<spec-filename>` is approved or explicitly handed off for phase planning. This gate pauses before implementation and before later phase-plan drafting; phase-plan drafting resumes only after fresh operator instruction.
- Phase-plan freeze: after one or more `<phase-plan-filename>` files are approved.
- Amendment freeze: after any high-impact `<amendment-filename>` is approved.

Use the same draft review and approval freeze checkpoints each time. `rule:lifecycle.large-phase-orchestration` owns the large/phased planning order, and `rule:lifecycle.planning-shape` distinguishes combined and explicitly staged small/medium packages; this freeze-gate rule owns the approval mechanics and continuity-selected conversation result at each actual stop.

## Compatibility

This gate layers on top of Codex plan mode, Superpowers, and spec-kit. Those tools may produce or refine the artifacts, but the harness owns the approval, commit, and pause transition before implementation.

If another workflow would normally continue directly from approved planning into execution, pause and run this gate instead. The next operator response may authorize implementation and select any execution methodology or tool, including Superpowers.
