# Harness Simplification Architecture Snapshot

Work ID: `2026-07-14_harness-simplification`
Short ID: `harness-simplification`
Status: Approved
Harness release: `0.6+`
Schema: `schema:snapshot.architecture`

## Purpose

Preserve the decisions that simplify the harness without discarding the useful
commitment-verification architecture.

## Decision ledger

### `DEC-001` Keep identifiers; make structure proportional

Selected approach:

1. Retain stable entity IDs and short titles.
2. Use local references by default. Add a complete mapping only when its named
   coverage, handoff, or automation benefit exceeds the reader cost.

Affected boundaries:

1. Templates, quality guidance, validator scenarios, and durable work items
   created after this implementation.

Source spec sections:

1. `SPEC-001` and `SPEC-002`.

Validation cues:

1. `VER-001`, `VER-002`, `CHECK-002`, and `CHECK-003`.

Rejected alternatives:

1. Remove the entity IDs entirely, or require complete mappings for every plan.

### `DEC-002` Centralize one approval boundary

Selected approach:

1. The freeze gate is the one ordinary pause between planning and execution.
2. A fresh start instruction authorizes the approved implementation path through
   its planned tasks. Routine confirmation is not a task boundary.

Affected boundaries:

1. README bootstrap guidance, repository lifecycle-policy consumers, handoff
   templates, and operator documentation.

Source spec sections:

1. `SPEC-003` and `SPEC-005`.

Validation cues:

1. `VER-003`, `VER-005`, `CHECK-001`, and `CHECK-004`.

Rejected alternatives:

1. Remove the freeze gate, or add task-by-task confirmation checkpoints.

### `DEC-003` Let evidence purpose determine materiality

Selected approach:

1. An equivalent method that still proves the same result is ordinary execution
   drift and may receive a variance note.
2. An amendment is reserved for changed material outcomes or evidence that no
   longer establishes the agreed result.

Affected boundaries:

1. Quality, lifecycle, variance, amendment, plan-check templates, and scenario
   validation.

Source spec sections:

1. `SPEC-004`.

Validation cues:

1. `VER-004` and `CHECK-005`.

Rejected alternatives:

1. Treat every command or procedure change as an amendment, or record no
   noteworthy allowed variance.

## Constraints

1. Frozen history is immutable and remains outside the implementation diff.
2. The source-block assembler remains authoritative for generated templates.
3. The README bootstrap is the only global-guidance surface changed; the
   operator owns any later personal global-file copy.
4. The canonical freeze-gate module and README workflow diagram remain unchanged.
5. The implementation must show a net reduction in changed active author-facing
   Markdown unless the operator approves a material exception.

## Approval

- Status: Approved
- Superseded by: None
