# Changelog

All notable changes to this repository are documented here.

Entries are newest-first and grouped by change type.

## 2026-05-28-template-durable-spec-hardening: complete TODO items

### Changed

- Expanded plan and large-feature spec template sub-agent strategy prompts with the required policy fields for safe delegation and operator confirmation.
- Aligned the canonical sub-agent policy notation example with the required field list.
- Clarified model-policy wording so the human operator is not described as mismatched to the work.
- Expanded the large-feature spec template with explicit durable-spec sections for behavior, interfaces, state flow, safety, validation, operations, unknowns, and rejected alternatives.
- Removed the completed template-hardening follow-ups from `TODO.md`.

## 2026-05-28-review-hardening: address review feedback

### Added

- Added TODO follow-ups for full sub-agent strategy fields in plan templates and explicit durable-spec sections in the large-feature spec template.

### Changed

- Changed copied template references to point to repository-root harness reference paths.
- Clarified freeze-gate commits must stage only finalized planning artifacts and `CHANGELOG.md`, excluding unrelated worktree changes.

## 2026-05-26-root-readme: explain operator process impact

### Added

- Added `README.md` with an operator-focused overview of how the harness changes development process, pause points, handoffs, variance handling, and outcomes.
- Added a compact styled Mermaid flow diagram to show the operator-facing harness loop.

### Changed

- Clarified the README diagram with separate small, small/medium, and large/phased paths plus an explicit normal implementation flow.

## 2026-05-26-agentic-instruction-extraction: add reusable references

### Added

- Added concise references for context loading, quality gates, sub-agent role examples, and evidence/report artifacts.
- Added TODO follow-ups using only public repository references for extracted instruction patterns.

### Changed

- Clarified when to skip loading supplemental evidence/report artifact guidance.
- Removed completed TODO items for the fake small-feature harness test and common sub-agent role examples.

## 2026-05-26-agentic-instruction-research: track cross-repo review

### Added

- Added a TODO item to review public repositories, including `https://github.com/itxyzzz/gen-ai-se-hw`, for reusable agentic instruction patterns.

## 2026-05-25-root-todo: collect future harness work

### Added

- Added `TODO.md` with remaining future work from the original handoff and follow-up design discussion.
- Grouped future work from near-term validation through riskier adapter, governance, and process-maturity additions.

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
