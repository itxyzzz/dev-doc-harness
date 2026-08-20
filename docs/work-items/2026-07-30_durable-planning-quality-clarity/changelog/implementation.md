## 2026-07-31 docs: spec-quality-bar -- clarify planning inputs

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

#### Changed

- Clarified the concise spec inputs needed for planning and the spec-to-plan self-containedness boundary.

## 2026-07-31 docs: entity-section-ownership -- clarify spec-plan hierarchy

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

#### Changed

- Nested `SPEC`/`VER` under spec quality and `TASK`/`CHECK` under plan quality, with a concise task-to-check-to-criterion cue.

## 2026-07-31 docs: task-bound-checks -- make checks task-bound

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

#### Changed

- Made the executable plan body a flat task list and nested every check under one parent task.
- Replaced shared-check allocation with explicit integration tasks for end-to-end validation.

## 2026-07-30 docs: task-check-conformance -- clarify execution evidence

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

#### Added

- Defined `TASK` as a first-class durable-plan entity and clarified task-local versus cross-cutting Plan Check placement.
- Added execution-quality ownership for implementation evidence and `VER` conformance statuses.

#### Changed

- Kept `CHECK` → `VER` as the conformance-evidence relationship and made task links operational only.
- Regenerated plan templates and extended validator coverage for task/check placement, execution-time status recording, and the preserved readability reordering.

## 2026-07-30 docs: durable-planning-quality-clarity -- clarify plans and conformance

Release target: `unreleased`
Package impact: `distributable`
Release-note: `source-only`

#### Changed

- Applied one quality bar to all durable specs and plans, with a separate execution-size requirement only for phase plans.
- Clarified the plain-language and material-open-question rules, preserved material operator-provided source context in durable handoffs, and removed duplicate rejected-alternatives wording.
- Defined a lightweight evidence model: `SPEC` commitments are established by `VER` criteria, while `CHECK` records the method, result, and evidence without mandatory mapping tables.
- Regenerated affected plan templates and replaced the unreachable mandatory-matrix validator fixture with active local-link coverage.
