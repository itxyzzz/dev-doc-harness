# Planning Freeze Gates

This document is the canonical source for commit-and-pause gates between durable planning and implementation.

## When to run a gate

Run a Planning Artifact Freeze Gate whenever one of these durable planning artifacts is finalized:

- `spec.md`
- `plan.md`
- `plan-phase-*.md`
- `plan-amendment-*.md`

Draft artifacts may be edited before the gate. After the gate, approved artifacts follow the immutable snapshot rules in `artifact-contract.md`.

## Required gate actions

At each freeze gate:

1. Update `CHANGELOG.md` with a newest-first entry for the finalized artifact set.
2. Verify that finalized artifacts contain no placeholders, unresolved decisions, or missing required sections.
3. Verify the worktree status, stage only the finalized planning artifacts and `CHANGELOG.md`, and commit only those staged paths together. Do not stage or commit unrelated pre-existing operator work, generated files, or implementation edits during a plan-only checkpoint.
4. Stop before implementation, task execution, or the next planning stage.
5. Report the commit hash and finalized artifact paths.
6. Remind the operator that they may push and create a draft plan-only PR at this point.
7. Ask the operator to confirm model, reasoning-effort, and sub-agent policy choices before proceeding.

Implementation must not begin from a finalized durable plan in the same turn unless the operator gives a fresh explicit instruction after this gate.

## Multiple gates for very large or phased work items

Very large or phased work items may have multiple freeze gates:

- Anchor spec freeze: after `spec.md` is finalized for handoff to phase planning.
- Phase-plan freeze: after one or more `plan-phase-*.md` files are finalized.
- Amendment freeze: after any high-impact `plan-amendment-*.md` is approved.

Use the same required gate actions each time.

## Compatibility

This gate layers on top of Codex plan mode, Superpowers, and spec-kit. Those tools may produce or refine the artifacts, but the harness owns the commit-and-pause transition before implementation.

If another workflow would normally ask to implement immediately after planning, pause instead and run this gate.
