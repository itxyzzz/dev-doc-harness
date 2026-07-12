## Commitment-Disposition Mapping

Map every in-scope Specification Commitment to Implementation Tasks, verification-only treatment, or an exact frozen-spec reference that already authorizes a later phase. A Plan cannot create a deferral. Preservation-only and constraint commitments may be verification-only rather than receiving artificial tasks.

| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` `<short title>` | `<implement | verification-only | frozen later-phase reference>` | `TASK-001`, `TASK-002`, or `None with reason` |

## Verification-Execution Mapping

Map every applicable Verification Criterion to one or more Plan Checks and the stage where evidence is expected. Every Plan Check covers at least one criterion.

| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` `<short title>` | `CHECK-001` | `<pre-edit | implementation | review | pre-commit | named environment>` |

Both mappings are required and coordinate through task/check dependencies and stages. Completing either mapping alone is insufficient Plan coverage.

Architecture coverage:

1. Architecture input: `<spec section, snapshots/architecture.snapshot.md, amendment, or None with reason>`.
2. Plan usage: `<how tasks consume Architecture Decisions under mapped Specification Commitments for sequencing, boundaries, checks, rollout, or review>`.
3. Drift path: `<draft spec/snapshot update before freeze, or variance/amendment after freeze>`.
4. Reinterpretation guard: plans reference approved architecture decisions and do not reinterpret missing or frozen architecture silently.

## Implementation Approach

State the implementation approach in a few concise paragraphs. Focus on sequencing, dependencies, technical shape, integration points, and review strategy. Do not repeat the spec except to record implementation tradeoffs.

## Change Surfaces

Expected edits:

1. `<file or directory>`: `<kind of change and boundary>`.

Stable interfaces:

1. `<API, schema, config, template, workflow, or None>`: `<what must remain compatible>`.

Changed interfaces:

1. `<API, schema, config, template, workflow, or None>`: `<what changes and who consumes it>`.

Implementation boundaries:

1. `<nearby file, behavior, cleanup, later phase, or follow-up>` stays out of scope because `<reason>`.
