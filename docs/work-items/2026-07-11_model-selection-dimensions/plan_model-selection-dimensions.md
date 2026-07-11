# Model Selection Dimensions Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` task-by-task. Use `superpowers:subagent-driven-development` only if the operator explicitly confirms the bounded reviewer strategy below.

Work ID: `2026-07-11_model-selection-dimensions`
Short ID: `model-selection-dimensions`
Status: Approved
Harness release: `0.5+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:execution-quality`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:execution-quality.context-load-order`, `rule:execution-quality.task-preflight`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.changelog-entries`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

**Goal:** Separate model generation, capability tier, reasoning effort, orchestration mode, and execution continuity while adding safe `ultra` guidance and efficient fresh-task handoff.

**Architecture:** Keep model and orchestration decisions in `module:models`, fresh-task startup in `module:execution-quality`, and authorization in `module:freeze-gate`. Propagate the contract through reusable template source blocks and enforce it with focused validator checks.

**Tech stack:** Markdown policy and templates, JSON assembly manifests, Python 3 assembler and validator, Git.

## Global Constraints

1. Keep `economy-default` as the active repository policy.
2. Do not modify frozen historical work items, root `CHANGELOG.md`, runtime tooling, Codex configuration, automatic compaction, or provider availability.
3. Keep permanent tiers vendor-neutral; GPT-5.6 names are a current mapping only.
4. Treat `ultra` as platform-managed orchestration, never reasoning effort or capability tier.
5. Prefer a fresh task when the main model/profile changes; never claim exact remaining context when it is not exposed.
6. Keep handoff messages minimal and refer to frozen artifacts rather than duplicating requirements.
7. Edit template sources and manifests, then regenerate outputs; do not hand-edit generated templates.
8. Preserve unrelated operator changes and stop if overlapping edits cannot be integrated safely.

## Input Artifacts

1. `docs/work-items/2026-07-11_model-selection-dimensions/spec_model-selection-dimensions.md`.
2. `docs/work-items/2026-07-11_model-selection-dimensions/snapshots/architecture.snapshot.md`.
3. `docs/work-items/2026-07-11_model-selection-dimensions/evidence/gpt-5-6-model-taxonomy.md`.
4. This plan and any later `plan_amendment-*.md`.
5. Canonical targets under `Change Surfaces`.
6. Unresolved context: none; runtime availability and permission use the approved fallback.

## Spec Traceability

| Requirement or criterion | Tasks | Validation |
|---|---|---|
| `REQ-001`, `AC-001`, `AC-002` Multi-axis notation | `T-002`–`T-004` | `V-001`, `V-003` |
| `REQ-002`, `AC-003` Vendor-neutral tiers | `T-003`, `T-005` | `V-001`, `V-004` |
| `REQ-003`, `AC-004`, `AC-005` Platform orchestration | `T-002`–`T-004` | `V-001`, `V-004` |
| `REQ-004`, `AC-006`, `AC-007` Policy behavior | `T-003`, `T-005` | `V-001` |
| `REQ-005`, `AC-008`–`AC-010` Authorization | `T-002`, `T-003` | `V-001`, `V-004` |
| `REQ-006`, `AC-011`, `AC-012` Current consumers | `T-004`–`T-006` | `V-002`, `V-005` |
| `REQ-007`, `AC-013`–`AC-015` Validation | `T-002`, `T-006` | `V-001`–`V-003` |
| `REQ-008`, `AC-016`–`AC-020` Transition handoff | `T-002`–`T-005` | `V-001`, `V-003`, `V-004` |

Architecture input is `DEC-001` through `DEC-004`. `T-003` establishes ownership, `T-004` propagates interfaces, and `T-002`/`T-006` enforce them. After freeze, use an amendment for ownership, authorization, scope, or acceptance changes.

## Implementation Approach

Use test-first policy development: add validator expectations, confirm focused failures, implement canonical owners, propagate through source blocks and manifests, regenerate templates, align examples and operator guidance, then run final validation.

Create one reusable `blocks/handoff.080.common.execution-thread.md` and include it in all four primary template assemblies before their readiness/approval blocks. Keep the implementation in one cohesive commit because policy, generated outputs, and validator expectations must stay synchronized.

## Change Surfaces

Modify:

1. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` — dimensions, tiers, `ultra`, authorization, continuity, fallback, reporting.
2. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md` — own `rule:execution-quality.execution-thread-start`.
3. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md` — confirm execution dimensions and handoff.
4. `.agents/skills/dev-doc-harness/references/policy-architecture.md` and `.agents/skills/dev-doc-harness/SKILL.md` — route owners without duplicating policy.
5. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md` and `README.md` — current examples and operator guidance.
6. Template source blocks `plan.040.common.model-strategy.md` and `spec.060.large.phase-decomposition-model.md`.
7. Create `.agents/skills/dev-doc-harness/assets/templates/blocks/handoff.085.common.execution-thread.md`.
8. Assembly manifests `small-medium-work-item-spec.json`, `small-medium-work-item-plan.json`, `large-phased-work-item-spec.json`, and `large-phased-work-item-phase-plan.json` under `.agents/skills/dev-doc-harness/assets/templates/assemblies/`.
9. Generated outputs `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`, `small-medium-work-item-plan.md`, `large-phased-work-item-spec.md`, and `large-phased-work-item-phase-plan.md`, only through `assemble_templates.py`.
10. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` — focused contract checks.
11. Create `docs/work-items/2026-07-11_model-selection-dimensions/changelog/implementation.md` before implementation commit.

Stable interfaces: policy names, active `economy-default`, context strategies, concurrency cap, freeze/variance semantics, schema IDs, output paths, and final integration ownership.

Changed interfaces: explicit model dimensions, transition fields, freeze confirmation, copy-ready handoff, and de-facto continuity/runtime reporting.

## Model and Sub-agent Strategy

Current orchestration:

1. Model generation, capability tier, reasoning effort, and resolved profile: not exposed.
2. Orchestration mode: single planning task; no sub-agents used.
3. Availability/fallback: current task profile; alternatives not exposed.
4. Execution continuity: new implementation task with curated artifacts.
5. Context visibility: not exposed; do not prescribe compaction.
6. Artifact rehydration: required from the frozen package.
7. Policy source: root `AGENTS.md`, `economy-default`; no override.

Fit assessment: medium implementation complexity, high process blast radius, low post-spec ambiguity. Recommend a fresh implementation task using a `flagship` tier at `high` reasoning (`max` only when available and accepted), with single-agent implementation.

`Ultra` was assessed but is not recommended: the edit set is tightly coupled and benefits more from one integration owner plus an auditable reviewer. Fallback is a separate main-agent review pass.

Optional sub-agent `final-policy-reviewer`:

1. Purpose: review the completed policy/template/validator diff for conflation, authorization gaps, handoff duplication, and historical drift.
2. Context: curated frozen artifacts, completed diff, assembler output, validator output, and changelog fragment.
3. Output: blocking/non-blocking findings in the completion report.
4. Selection: active `economy-default` escalated to latest `flagship`, `high` reasoning for high-risk final review.
5. Timing: after validation, not parallel.
6. Authorization: use only if explicitly confirmed at the freeze gate; otherwise use the fallback.

## Task Plan

### `T-001` Rehydrate the package and protect the worktree

Dependencies: frozen package and fresh post-freeze authorization.

Implementation:

1. Read the frozen spec, architecture snapshot, evidence, plan, applicable `AGENTS.md`, and harness router.
2. Run `git status --short`, `git diff --name-only`, and path-specific diffs for every dirty implementation target.
3. Preserve unrelated changes; stop if overlapping edits cannot be integrated within frozen scope.
4. Run baseline `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` and `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Exit criteria: ownership is clear and both commands exit `0`, or a pre-existing failure is recorded and approved.

### `T-002` Add failing validator checks

Dependencies: `T-001`.

Implementation:

1. Add `models.selection-dimensions` and `execution.thread-start` to `CHECK_IDS`.
2. Add `assert_model_selection_dimensions()` asserting owned rule IDs, every explicit field label, vendor-neutral tiers/current mapping, `ultra` classification/limitations, enterprise/economy behavior, four authorization layers, fallback, and de-facto reporting.
3. Add `assert_execution_thread_start()` asserting the startup-rule owner, new-task preference, no unexposed context estimate, same-task rehydration, handoff fields in all primary templates, freeze confirmation, and router discoverability.
4. Call both from `run_checks()` and write their result IDs.
5. Run the full validator.

Exit criteria: validator exits non-zero only for the newly absent policy/template/docs contract; unexpected regressions are resolved first.

### `T-003` Implement canonical policy owners

Dependencies: `T-002` failing checks.

Implementation:

1. Add owned rules `rule:models.selection-dimensions`, `rule:models.orchestration-mode`, and `rule:models.execution-continuity` to `subagent-model-policy.md` and implement every approved semantic from `DEC-001`–`DEC-004`.
2. Add `rule:execution-quality.execution-thread-start` to `context-and-quality-gates.md`: load instructions/artifacts, verify state, avoid rediscovery, restate only immediate work, start at the named task, and route conflicts through variance.
3. Update freeze guidance to confirm tier, effort, orchestration, fallback, continuity, context visibility, rehydration, and the copy-ready next-task handoff.
4. Update policy architecture and router descriptions to expose ownership without copying rules.
5. Run the validator; remaining failures must be limited to scheduled consumers.

Exit criteria: canonical ownership matches the architecture snapshot and focused failures narrow as expected.

### `T-004` Propagate templates and handoff

Dependencies: `T-003`.

Implementation:

1. Replace ambiguous model-class prompts in both model-strategy source blocks with the approved explicit fields.
2. Create the common `## Next-task handoff` block with continuity choice, exact artifacts, strategy/fallback reference, conditional copy-ready prompt, startup-rule reference, first activity, and variance stop condition.
3. Add the common block before readiness/approval in all four manifests.
4. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`; generated files may be written even if its embedded validator still reports only `T-005` consumer gaps.
5. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` and expect `All assembled templates are current.`

Exit criteria: all four generated templates match their sources and expose consistent strategy/handoff semantics.

### `T-005` Align examples and operator guidance

Dependencies: `T-004`.

Implementation:

1. Update role examples to distinguish tier, effort, and orchestration.
2. Update README model-policy and execution-quality sections with the dimensions, `ultra` versus bounded agents, runtime permission, new-task preference, and minimal handoff/startup route.
3. Keep prose compact and refer to canonical rules.
4. Run the full validator and fix only the owning current surface for any remaining focused failure.

Exit criteria: operator guidance is discoverable, examples are unambiguous, and the full validator exits `0`.

### `T-006` Validate and review the completed change

Dependencies: `T-005`.

Implementation:

1. Run `V-001` through `V-006`.
2. Inspect `git diff --check`, `git diff --stat`, and the full diff for duplicated policy, generated noise, placeholders, historical changes, and root changelog edits.
3. If authorized, run the optional reviewer with curated inputs; otherwise perform the recorded main-agent fallback review.
4. Resolve in-scope findings, record variance, and rerun affected validation.

Exit criteria: every validation passes and review has no blocking findings.

### `T-007` Record the source fragment and commit

Dependencies: `T-006`.

Implementation:

1. Create `changelog/implementation.md` headed `### 2026-07-11_model-selection-dimensions -- separate model tier and optimize execution handoff` with `Release target: unreleased`, `Package impact: distributable`, and `Release-note: include` exactly once.
2. Add concise `Changed` bullets for policy dimensions, orchestration/authorization, fresh-task startup, handoff templates, and validation.
3. Re-run the full validator and `git diff --check`.
4. Stage only approved implementation paths and verify `git diff --cached --name-only`.
5. Commit `docs: model-selection-dimensions -- separate model tier and optimize execution handoff`.

Exit criteria: fragment validation passes, the commit contains no unrelated work, and completion reports validation, variance, de-facto strategy, continuity, and reviewer use.

## Planned Commits

Planning approval:

1. Subject: `spec: model-selection-dimensions -- define tier, orchestration, and handoff axes`.
2. Fragment: `changelog/planning-approval.md` with matching title and required release metadata.
3. Contents: spec, plan, architecture snapshot, evidence, Superpowers pointers, and planning fragment.

Implementation:

1. Subject: `docs: model-selection-dimensions -- separate model tier and optimize execution handoff`.
2. Fragment: `changelog/implementation.md` with matching title and required release metadata.
3. Contents: one cohesive policy/template/validator change.

## Validation Plan

| ID | Command | Expected result |
|---|---|---|
| `V-001` | `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exit `0`; new focused checks pass; final summary reports policy checks passed |
| `V-002` | `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` | Exit `0`; `All assembled templates are current.` |
| `V-003` | `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` | Regenerate only declared outputs, run validation, exit `0` |
| `V-004` | `rg -n "flagship|balanced|fast/economy|ultra|platform multi-agent|execution-thread-start|Execution continuity|Context visibility|Artifact rehydration required" .agents/skills/dev-doc-harness/references .agents/skills/dev-doc-harness/assets/templates README.md` | Canonical definitions in owners and compact prompts/references in consumers; `ultra` is not a tier or effort |
| `V-005` | `git diff --name-only -- docs/work-items` | Only this work item's implementation fragment; no frozen historical package changes |
| `V-006` | `git diff --check` | Exit `0` with no whitespace errors |

## Plan Variance Handling

Before freeze, edit this draft. After freeze, record nontrivial local variance in `implementation-notes/variance-log.md`; obtain amendment approval before changing ownership, tiers, authorization, continuity defaults, acceptance criteria, template-schema intent, or feasibility.

## Planning Artifact Freeze Gate

Draft review status: spec and plan approved by the operator on 2026-07-11. The approval freeze commit includes the approved planning package and `changelog/planning-approval.md`; implementation remains prohibited until a fresh post-freeze operator instruction. The post-freeze confirmation must cover flagship/high fresh-task execution, optional reviewer authorization/fallback, and whether to start in a new task.

## Next-Task Handoff

Execution continuity: `new task with curated-artifact handoff`.

Context visibility: `not exposed`; do not prescribe compaction.

Artifact rehydration required: `Yes`.

```text
Implement `2026-07-11_model-selection-dimensions` from its frozen package:

- `docs/work-items/2026-07-11_model-selection-dimensions/spec_model-selection-dimensions.md`
- `docs/work-items/2026-07-11_model-selection-dimensions/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-07-11_model-selection-dimensions/evidence/gpt-5-6-model-taxonomy.md`
- `docs/work-items/2026-07-11_model-selection-dimensions/plan_model-selection-dimensions.md`

Follow applicable `AGENTS.md`, the repository harness, and
`rule:execution-quality.execution-thread-start` (use frozen DEC-004 until that
rule is implemented). Use the approved flagship/high strategy, single-agent
implementation, and recorded fallback. Use the bounded reviewer only if
explicitly authorized. Treat frozen decisions as authoritative, run `T-001`,
and stop for variance that requires operator approval.
```

## Plan Readiness Checklist

- [x] Inputs, exact change surfaces, tasks, commands, expected signals, and ownership are recorded.
- [x] Every requirement and acceptance criterion maps to tasks and validation.
- [x] Changelog fragments and planned subjects are synchronized.
- [x] `Ultra` was assessed and rejected for this tightly coupled implementation with a reason.
- [x] Fresh-task handoff is copy-ready and does not duplicate frozen content.
- [x] No unresolved placeholders, required decisions, or ownerless deferrals remain.

## Completion Criteria

1. `AC-001` through `AC-020` and `V-001` through `V-006` pass.
2. Canonical policy, startup guidance, freeze gate, templates, examples, README, router, and validator agree.
3. The implementation fragment and commit are complete without unrelated work.
4. Completion reports de-facto model dimensions, orchestration, permission, fallback, continuity, context visibility, reviewer use, and residual risk.

## Approval

- Status: Approved
- Superseded by: None
