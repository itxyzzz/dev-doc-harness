# Context And Quality Gates

Use this reference to keep routine harness work consistent across local, web, and reduced-tool environments.

Module: `module:execution-quality`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:execution-quality.context-load-order` | `## Context load order` |
| `rule:execution-quality.execution-thread-start` | `## Execution thread start` |
| `rule:execution-quality.task-preflight` | `## Task preflight` |
| `rule:execution-quality.environment-compensation` | `## Environment compensation` |
| `rule:execution-quality.conformance-evidence` | `## Conformance evidence` |
| `rule:execution-quality.increment-quality-gate` | `## Increment quality gate` |

## Context load order

Before planning or implementation, build context in this order:

1. System, tool, sandbox, plugin, and model constraints.
2. Repository instructions, including `AGENTS.md` and this harness.
3. Active specs, plans, amendments, variance logs, and related documentation.
4. The user's current prompt, including scope and stop conditions.
5. Discovered working state from files, tests, logs, diffs, and branch status.

If instructions conflict, preserve higher-priority system and user constraints, then apply the most specific repository or artifact rule.

## Execution thread start

Use this protocol after the transition and fresh authorization governed by `rule:freeze.stop-before-implementation`. It applies when a frozen planning package hands work to a fresh execution Codex task or when an approved same-task model switch or recorded continuity risk requires rehydration:

1. Consume the approved runtime selection from `rule:models.selection-dimensions` and the same-task or new-task choice from `rule:models.execution-continuity`; do not reconstruct either decision here.
2. Load system and runtime constraints, applicable instructions, and all frozen artifacts and execution inputs named by the approved handoff.
3. Verify branch, worktree, approval state, amendments, variance records, and the expected validation baseline before editing.
4. Treat the frozen package as authoritative, avoid broad repository rediscovery, and do not reopen settled decisions without conflicting evidence.
5. Begin the documented next activity or First Plan Task. Route conflicts through `rule:lifecycle.variance-policy`, and stop when the variance class requires operator approval.

If runtime or environment limitations affect this startup, use the approved fallback defined by the transition owners and the environment compensation below. `module:models` owns model, continuity, sub-agent, and reviewer decisions; `module:freeze-gate` owns planning-transition and authorization behavior.

## Task preflight

For non-mechanical work, confirm:

- Current branch and dirty worktree state.
- Applicable instructions and harness references.
- Relevant existing code, docs, tests, and changelog entries.
- Required planning artifacts or reason they are not applicable.
- Expected verification commands and success signals.

## Environment compensation

When local quality controls are unavailable, compensate explicitly.

| Missing control | Compensation |
|---|---|
| Superpowers unavailable | State a short plan, use focused verification, and run fresh checks before completion claims. |
| Model or reasoning controls unavailable | Record the limitation and apply the repository's policy-relative intent manually. |
| Subagents unavailable | Keep role boundaries in the plan and have the orchestration thread own integration and review. |
| Tests unavailable | Record the blocker, inspect the diff, and provide the best manual or static validation available. |
| Browser or runtime tooling unavailable | Probe first, record the unavailable tool, and avoid claiming visual or runtime verification. |

## Conformance evidence

During implementation, after a Plan Check runs, retain its result and evidence in the form that helps a later reader reproduce or trust it. Record each affected Verification Criterion as `met`, `not met`, `pending`, or `blocked`: evidence that satisfies the criterion is met; contradictory evidence is not met; absent or insufficient evidence is pending; and an unavailable evidence path with its reason is blocked.

This record is implementation evidence, not a planning-time assertion. Apply `module:quality`'s conformance definition when reporting completion: a commitment conforms only when all its applicable Verification Criteria are met. Report non-met, pending, or blocked criteria rather than treating a completed task as proof. `module:lifecycle` continues to own variance and amendment mechanics; `module:freeze-gate` owns approval, freeze, and authorization transitions.

## Increment quality gate

Before a commit, PR-ready handoff, or completion report, check:

- Plan or rationale captured.
- Existing context inspected.
- Implementation stayed within scope.
- Verification run or blocker recorded.
- Relevant docs and changelog updated.
- Diff reviewed for unrelated changes, placeholders, contradictions, and generated noise.

After the final commit, PR-ready handoff, or completion report, report the commit outcome consistently: include the commit hash and subject when a commit was created, or state that no commit was created and why.

Implementation completion with uncommitted implementation changes is not a normal completion state. Either create the planned implementation commit, or report the exact blocker or explicit no-commit instruction plus the current worktree status.

Do not use this gate to bypass the Planning Artifact Freeze Gate. Finalized specs, plans, phase plans, and amendments still follow `planning-freeze-gates.md`.
