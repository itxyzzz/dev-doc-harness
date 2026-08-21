# Large/Phased Lifecycle

This document owns the detailed large/phased lifecycle layout and planning sequence. It is loaded only for large/phased work.

Module: `module:lifecycle`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:lifecycle.large-anchor-spec` | `## Large or phased work item spec as handoff anchor` |
| `rule:lifecycle.large-phase-orchestration` | `## Large or phased planning orchestration` |

## Large or phased work item layout

The full lifecycle package for large or phased work may eventually contain these files:

```text
<work-item-path>
  <spec-filename>
  <phase-plan-filename>      # one per concrete phase
  <amendment-filename>

  changelog/
    <phase implementation source; see module:implementation-changelog>

  snapshots/
    test-cases.snapshot.md
    architecture.snapshot.md
    api-contract.snapshot.md

  deltas/
    testing-guide.delta.md
    operator-manual.delta.md
    api-reference.delta.md
    architecture-summary.delta.md

  handoff/
    implementation-handoff.md
    review-handoff.md

  implementation-notes/
    variance-log.md
```

The normal initial planning package is anchor-spec-only: create `<spec-filename>` plus only the required supporting snapshots, deltas, or handoff files. Do not create concrete `<phase-plan-filename>` files during the anchor-spec planning package unless the operator explicitly requests combined planning.

Phase plan names are planned future outputs until phase-plan drafting begins. When created later, phase plans should be numbered in execution order and each phase must be safely executable by one orchestration session with bounded delegation. Create handoff files when they are useful for continuity.

## Large or phased planning orchestration

`rule:lifecycle.large-phase-orchestration` owns the large/phased planning state sequence. Other modules own their local mechanics: artifact layout stays in this lifecycle reference, approval checkpoint mechanics stay in `planning-freeze-gates.md`, model and sub-agent choices stay in `subagent-model-policy.md`, and durable quality stays in `durable-planning-quality.md`.

The normal large/phased planning sequence is a rolling loop:

1. Draft the anchor `<spec-filename>`.
2. Stage the anchor-spec planning package for draft review.
3. Freeze the anchor spec after explicit approval and its planning approval commit.
4. Stop before implementation and before phase-plan drafting.
5. Resume phase-plan drafting only after fresh operator instruction, draft and freeze one phase plan, then begin that phase implementation after fresh post-freeze authorization.
6. Record the actual phase outputs, validation, variance, and commit state as inputs to the next phase plan.
7. Draft and freeze the next phase plan from the anchor, amendments, and actual prior-phase outputs; repeat until completion.
8. Batch planning or freezing multiple phases before implementation is an explicit exception only for stable, independently plannable phases.
9. Use an amendment gate for high-impact post-freeze changes.

Combined anchor-spec and phase-plan drafting is allowed only when the operator explicitly requests combined planning and the artifact records that exception.

## Large or phased work item spec as handoff anchor

For large or phased work items, `<spec-filename>` is the central anchor between planning sessions. The initial planning session must preserve all important decisions and context in `<spec-filename>` before later sessions produce phase plans. Follow `rule:lifecycle.large-phase-orchestration` for the sequencing of anchor-spec review, freeze, later phase-plan drafting, phase-plan freeze, and implementation authorization.

`<spec-filename>` must be detailed enough that a fresh planning thread can write `<phase-plan-filename>` without losing Specification Commitments or Architecture Decisions. Include goals, scope, non-scope, assumptions, constraints, risks, Verification Criteria, data and interface decisions, phase decomposition, documentation expectations, known unknowns, and important rejected alternatives.

Phase plans must derive from `<spec-filename>`. If a phase planner discovers missing or ambiguous context, it must update the draft spec before approval and freeze, or create a plan amendment after freeze. Do not let phase plans silently narrow, drop, or reinterpret decisions from the large/phased work item spec.

Follow `durable-planning-quality.md` for the full spec and phase-plan quality bar.
