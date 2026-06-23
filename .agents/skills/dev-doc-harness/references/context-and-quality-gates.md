# Context And Quality Gates

Use this reference to keep routine harness work consistent across local, web,
and reduced-tool environments.

Module: `module:execution-quality`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:execution-quality.context-load-order` | `## Context load order` |
| `rule:execution-quality.task-preflight` | `## Task preflight` |
| `rule:execution-quality.environment-compensation` | `## Environment compensation` |
| `rule:execution-quality.increment-quality-gate` | `## Increment quality gate` |

## Context load order

Before planning or implementation, build context in this order:

1. System, tool, sandbox, plugin, and model constraints.
2. Repository instructions, including `AGENTS.md` and this harness.
3. Active specs, plans, amendments, variance logs, and related documentation.
4. The user's current prompt, including scope and stop conditions.
5. Discovered working state from files, tests, logs, diffs, and branch status.

If instructions conflict, preserve higher-priority system and user constraints,
then apply the most specific repository or artifact rule.

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

## Increment quality gate

Before a commit, PR-ready handoff, or completion report, check:

- Plan or rationale captured.
- Existing context inspected.
- Implementation stayed within scope.
- Verification run or blocker recorded.
- Relevant docs and changelog updated.
- Diff reviewed for unrelated changes, placeholders, contradictions, and generated noise.

After the final commit, PR-ready handoff, or completion report, report the
commit outcome consistently: include the commit hash and subject when a commit
was created, or state that no commit was created and why.

Do not use this gate to bypass the Planning Artifact Freeze Gate. Finalized
specs, plans, phase plans, and amendments still follow `planning-freeze-gates.md`.
