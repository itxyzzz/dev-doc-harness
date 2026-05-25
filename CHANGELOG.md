# Changelog

All notable changes to this repository are documented here.

Entries are newest-first and grouped by change type.

## 2026-05-25-durable-planning-quality: strengthen planning and model policy

### Added

- Added `durable-planning-quality.md` as the canonical quality bar for durable specs, phase plans, and handoff preservation.
- Added model and sub-agent strategy requirements that account for orchestration fit, risk, ambiguity, blast radius, budget, and latency.
- Added sub-agent report and final integration ownership requirements.

### Changed

- Strengthened large feature templates to require fresh-thread executable phase plans and explicit model/reasoning fit assessment.

## 2026-05-25-freeze-gate-reference: consolidate freeze-gate rules

### Added

- Added `planning-freeze-gates.md` as the canonical reference for commit-and-pause gates.

### Changed

- Replaced repeated freeze-gate explanations in the skill, artifact contract, and templates with short references to the canonical freeze-gate document.

## 2026-05-25-planning-freeze-gates: commit-and-pause planning workflow

### Added

- Added mandatory Planning Artifact Freeze Gates for finalized specs, plans, phase plans, and plan amendments.
- Added draft plan-only PR reminders and model or reasoning confirmation requirements at each freeze gate.
- Added support for multiple freeze gates across anchor specs, phase-plan batches, and high-impact amendments for very large features.

## 2026-05-25-harness-review-updates: tighten artifact workflow

### Added

- Added root changelog requirements to the harness workflow and artifact contract.
- Added issue-tracker-aware feature ID guidance for specs, plans, amendments, and variance logs.
- Added large-feature spec handoff requirements so phase plans preserve initial planning decisions.

### Changed

- Simplified harness invocation guidance to use it for all development work except very small mechanical edits.
- Clarified that sub-agent notation and large-feature spec rows are examples to replace, not required phase or agent choices.
- Flattened large-feature phase plans and amendments into `specs/<feature-id>/` as `plan-phase-NN-*.md` and `plan-amendment-NNN-*.md`.

### Removed

- Removed person-oriented approval fields from spec and plan templates; superseded artifacts now reference the artifact that replaces them.
