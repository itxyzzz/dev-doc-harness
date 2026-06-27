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

- `spec-<short-id>.md`
- `plan-<short-id>.md`
- `plan-phase-*-<short-id>.md`
- `plan-amendment-*-<short-id>.md`

Draft artifacts may be edited until the operator explicitly approves them and the approval commit is created, or until the operator explicitly asks for a handoff snapshot. After that approval commit or explicit handoff snapshot, the artifacts are frozen and follow the immutable snapshot rules in `artifact-contract.md`.

## Draft review checkpoint

Before committing any planning artifacts for approval:

1. Draft or update the required planning artifacts.
2. Verify that the drafts contain no placeholders, undecided required items, or missing required sections unless the undecided item is explicitly marked as deferred with a reason and owner.
3. Verify the worktree status, stage only the draft planning artifacts being reviewed, and do not commit them.
4. Ask the operator to approve the staged planning package or provide feedback.
5. If the operator provides feedback, edit the draft artifacts directly, refresh the staged planning package, and ask for approval again.

Do not create a plan amendment for feedback received before the planning package is frozen.

## Approval freeze checkpoint

After the operator explicitly approves the staged planning package, or explicitly asks for a handoff snapshot:

1. Update `CHANGELOG.md` with a newest-first entry for the approved artifact set.
2. When the operator approved the package rather than requesting only a handoff snapshot, update every approved artifact's status fields from draft or proposed state to approved state before staging. This includes the top-level `Status:` line and any status line in an `Approval` section.
3. Verify again that the approved artifacts contain no placeholders, undecided required items, or missing required sections unless the undecided item is explicitly marked as deferred with a reason and owner.
4. Verify the approved artifacts include a planned approval commit subject following `rule:lifecycle.commit-message-format`, and verify the `CHANGELOG.md` entry title snippet matches that planned subject.
5. Verify the worktree status, stage only the approved planning artifacts and `CHANGELOG.md`, and commit only those staged paths together using the planned approval commit subject. Do not stage or commit unrelated pre-existing operator work, generated files, or implementation edits during a plan-only checkpoint.
6. Stop before implementation, task execution, or the next planning stage.
7. Report the commit hash and approved artifact paths.
8. Remind the operator that they may push, create a draft plan-only PR, and/or compact the thread at this point.
9. Ask the operator to confirm model, reasoning-effort, and sub-agent policy choices and to say whether implementation should begin now.

The planning package is frozen only after the approval commit or explicit handoff snapshot. From that point onward, high-impact changes use the amendment process from `artifact-contract.md`.

Implementation must not begin from a frozen durable plan in the same agent turn as the approval freeze checkpoint. A fresh operator response after this gate may both confirm execution settings and authorize implementation when the response clearly says to begin, such as `Confirmed, proceed`, `Confirm and start`, or equivalent wording.

If the operator only confirms execution settings without clear start authorization, ask a concise follow-up question about whether implementation should begin now. A bare `Confirm` may authorize implementation only when the agent's combined post-freeze prompt explicitly states that confirming also means beginning implementation now; otherwise treat it as settings-only confirmation and ask whether to start.

## Multiple gates for very large or phased work items

Very large or phased work items may have multiple freeze gates:

- Anchor spec freeze: after `spec-<short-id>.md` is approved or explicitly handed off for phase planning. This gate pauses before implementation and before later phase-plan drafting; phase-plan drafting resumes only after fresh operator instruction.
- Phase-plan freeze: after one or more `plan-phase-*-<short-id>.md` files are approved.
- Amendment freeze: after any high-impact `plan-amendment-*-<short-id>.md` is approved.

Use the same draft review and approval freeze checkpoints each time. `rule:lifecycle.large-phase-orchestration` owns the large/phased planning order; this freeze-gate rule owns the approval mechanics at each stop.

## Compatibility

This gate layers on top of Codex plan mode, Superpowers, and spec-kit. Those tools may produce or refine the artifacts, but the harness owns the approval, commit, and pause transition before implementation.

If another workflow would normally ask to implement immediately after planning, pause instead and run this gate.
