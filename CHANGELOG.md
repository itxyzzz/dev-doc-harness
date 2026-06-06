# Changelog

All notable changes to this repository are documented here.

Entries are newest-first and grouped by change type.

## 2026-06-05-refactor-as-code: centralize active model policy wording

### Changed

- Clarified that `AGENTS.md` is the single repository-local selection point for the active model policy.
- Replaced repeated `economy-default` default wording in current README, template examples, and model-policy examples with active-policy wording.

## 2026-06-05-refactor-as-code: complete Phase 03 template slimming

### Added

- Added compact schema IDs and canonical policy-reference anchors to the current harness templates.

### Changed

- Reduced reusable sub-agent authorization, variance handling, and freeze-gate procedure prose in templates while preserving artifact-shape prompts and fresh-thread usability.
- Kept Phase 03 scoped to templates and `CHANGELOG.md`; `SKILL.md`, `README.md`, root `AGENTS.md`, canonical references, and historical work-item artifacts were not updated.

## 2026-06-05-refactor-as-code: approve Phase 03 template slimming plan

### Added

- Added the approved Phase 03 plan for slimming harness templates with schema IDs, canonical policy citations, reduced reusable policy prose, preserved fresh-thread usability, and an operator-selected `enterprise-default` policy for Phase 03.

## 2026-06-05-refactor-as-code: complete Phase 02 canonical modules

### Added

- Added `policy-architecture.md` as the compact canonical module catalog and rule-interface reference for the harness.
- Added stable module and rule IDs to current canonical references, including lifecycle, freeze-gate, model/sub-agent, quality, execution-quality, evidence, and role-example ownership.

### Changed

- Labeled evidence and role-example references as supplemental or advisory so examples do not become competing policy.
- Kept `artifact-contract.md` intact for Phase 02, using an ownership block instead of splitting the lifecycle reference.

## 2026-06-05-refactor-as-code: approve Phase 02 canonical modules plan

### Added

- Added the approved Phase 02 plan for creating a canonical policy architecture reference, declaring module and rule IDs in current canonical references, preserving detailed rule ownership, and deferring template, README, root instruction, and entrypoint updates to later phases.

## 2026-06-05-refactor-as-code: complete Phase 01 policy architecture

### Added

- Added the Phase 01 architecture snapshot defining precedence, dependency direction, content taxonomy, operation routing, rule-interface conventions, validation budgets, golden scenario tests, work-item artifact locality, Phase 02 inputs, and open risks.
- Added the Phase 01 variance log with no variance recorded.

### Changed

- Recorded the explicit rule-versioning deferral so later phases use stable rule IDs without introducing a full versioning system in Phase 01.

## 2026-06-05-refactor-as-code: approve Phase 01 policy architecture plan

### Added

- Added the approved Phase 01 plan for producing a policy architecture snapshot, variance log, rule-interface conventions, operation router taxonomy, validation budgets, golden scenario tests, and work-item artifact locality guidance using the selected `enterprise-default` policy.

## 2026-06-05-refactor-as-code: approve architecture guardrails amendment

### Added

- Added the approved amendment requiring Phase 01 to define precedence, dependency direction, content types, operation routing, measurable architecture checks, golden scenario tests, and work-item artifact locality while deferring full rule versioning.

## 2026-06-05-refactor-as-code: approve anchor spec

### Added

- Added the approved large/phased anchor spec for refactoring harness instructions as maintainable policy modules with stable rule interfaces, slimmer templates, retrieval routing, and validation hardening.

## 2026-06-05-subagent-context-strategy: implement context strategy field

### Changed

- Added `Context strategy` to the canonical sub-agent strategy notation, templates, and role examples.
- Documented curated prompt, curated artifacts, full-history fork, and no repo context strategies, including full-history fork inheritance trade-offs.
- Extended de-facto sub-agent reporting to include actual context strategy and observed context/model inheritance behavior.
- Updated the README operator flow to treat context strategy as part of model, reasoning-effort, and sub-agent planning.

## 2026-06-05-subagent-context-strategy: approve planning package

### Added

- Added the approved spec and plan for making sub-agent context strategy a first-class planning field, including curated context options, full-history fork guidance, and de-facto context reporting.

## 2026-06-05-subagent-autonomy-policy: implement approved sub-agent autonomy behavior

### Changed

- Updated the canonical sub-agent policy so substantial plans proactively assess justified sub-agent use instead of treating missing operator mention as a prohibition.
- Clarified that approved frozen plans authorize their listed sub-agent strategy after normal post-freeze implementation authorization, while preserving fresh confirmation for unplanned or escalated delegation.
- Reframed the normal sub-agent cap as three concurrent sub-agents, with wave-based long-running use allowed when approved.
- Added de-facto sub-agent and model/model-class reporting expectations to policy, templates, and operator-facing documentation.

## 2026-06-05-subagent-autonomy-policy: approve planning package

### Added

- Added the approved spec and plan for proactive sub-agent strategy planning, approved-strategy authorization, 3-concurrent-sub-agent limits, wave-based long-running use, and de-facto sub-agent/model reporting.

## 2026-06-01-collapse-execution-approval: clarify ambiguous confirmation follow-up

### Changed

- Clarified that agents should ask a concise follow-up when execution settings are confirmed without clear start authorization, instead of passively waiting for another implementation instruction.

## 2026-06-01-collapse-execution-approval: implement combined start confirmation

### Changed

- Updated the planning freeze gate so the post-freeze prompt combines execution-setting confirmation with whether implementation should begin now.
- Clarified that clear post-gate start responses can satisfy both confirmation and implementation authorization while ambiguous settings-only confirmations remain insufficient.
- Aligned plan templates and the README operator flow with the combined post-freeze confirmation behavior.

## 2026-06-01-collapse-execution-approval: approve planning package

### Added

- Added the approved spec and plan for combining post-freeze execution-setting confirmation with implementation authorization when the operator clearly says to begin.

## 2026-05-31-local-planning-docs-distribution: keep repo planning docs local

### Changed

- Ignored this repository's local `docs/work-items/` planning packages so they are not treated as distributable project content.
- Documented the contribution convention that harness changes, user-facing documentation, and changelog entries are tracked, while this repo's own planning packages remain local.

## 2026-05-31-work-items-artifact-root: implement work item package layout

### Changed

- Moved the canonical harness package root to `docs/work-items/<work-id>/`, added short-ID durable artifact filenames, and flattened package documentation into `snapshots/` and `deltas/`.
- Clarified Superpowers compatibility so `docs/superpowers` files may only be minimal pointer stubs to canonical `docs/work-items/<work-id>/` packages.
- Migrated existing local planning packages into the new `docs/work-items/` layout.

## 2026-05-31-work-items-artifact-root: approve planning package

### Added

- Added the approved spec and plan for moving durable harness planning packages to `docs/work-items/<work-id>/`, adding short-ID artifact filenames, flattening snapshots and deltas, and clarifying Superpowers pointer-stub compatibility.

## 2026-05-31-planning-approval-freeze-flow: implement approval-first freeze flow

### Changed

- Updated the canonical freeze-gate workflow so agents stage draft planning artifacts for approval without committing, revise drafts directly on feedback, and freeze planning packages only after explicit approval and commit.
- Aligned the skill entry point, artifact lifecycle reference, durable planning quality reference, templates, and README with the approval-first planning review loop.

## 2026-05-31-planning-approval-freeze-flow: approve planning package

### Added

- Added the approved spec and plan for changing the harness planning lifecycle so draft review stages artifacts without committing, feedback edits drafts directly, and the freeze happens only after explicit approval and commit.

## 2026-05-28-work-item-scope: broaden harness beyond features

### Changed

- Reframed the harness artifact contract around substantial work items, including features, bug fixes, prior issue investigations, refactors, migrations, and documentation/process changes.
- Updated the skill, README, templates, and references so substantial bug fixes and investigations use the same durable planning, documentation, variance, and freeze-gate quality bar as features.
- Renamed reusable template files from feature-specific names to work-item names matching the small/medium and large/phased sizing model.

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
