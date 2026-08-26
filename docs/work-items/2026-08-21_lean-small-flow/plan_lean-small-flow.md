# Lean/Small Flow Plan

Work ID: `2026-08-21_lean-small-flow`
Short ID: `lean-small-flow`
Status: Approved
Harness release: `0.9+ development`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:quality.plan-executable`
Execution method: `superpowers:subagent-driven-development`

## Input artifacts

1. Draft spec: `spec_lean-small-flow.md`.
2. Architecture snapshot: `snapshots/architecture.snapshot.md`.
3. Test-case snapshot: `snapshots/test-cases.snapshot.md`.
4. Current router, lifecycle, freeze, quality, model-policy, template assembler, validator, README, and operator-note surfaces named in the tasks below.

## Change surfaces and approach

- `.agents/skills/dev-doc-harness/references/artifact-contract.md`: retain core lifecycle ownership; add lean/small sizing and planning shape; remove moved large-only detail.
- `.agents/skills/dev-doc-harness/references/large-phased-lifecycle.md`: new owner for unchanged large-only layout and rule bodies.
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md` and execution-quality routing: preserve common approval mechanics and add the lean exception that defers runtime model/orchestration choice.
- `.agents/skills/dev-doc-harness/SKILL.md`: add lean/small drafting and execution routes with a minimal reference budget.
- `.agents/skills/dev-doc-harness/assets/templates/`: add two isolated manifests, generated templates, and dedicated lean blocks.
- `.agents/skills/dev-doc-harness/scripts/assemble_templates.py` and `scripts/test_harness_policy.py`: add explicit lean entries and additive assertions.
- `README.md`, `.agents/skills/dev-doc-harness/docs/operator-note.md`, and `references/maintenance-architecture.md`: make the new route discoverable without renaming established flows.

Implement policy ownership and route selection first, then templates, then validation and operator documentation. Do not refactor current small/medium validator literals into a registry.

## Implementation tasks

### `TASK-001` Define lean/small lifecycle and isolate large policy

Dependencies: None.

Interfaces:

1. Consumes: `SPEC-001`, `SPEC-004`, `SPEC-005`; current lifecycle and maintenance-architecture references.
2. Produces: A lean/small classification and planning-shape contract plus a large-only lifecycle owner that callers can reference by the existing rule IDs.

Implementation:

1. Add a conservative `lean/small` branch to `rule:lifecycle.work-sizing`: eligible bounded work has a known local change surface, low material risk, and a safe one-session boundary; the operator can select it explicitly; material uncertainty or boundary expansion requires pre-freeze escalation to small/medium or large/phased.
2. Extend the planning-shape and layout text for a combined lean spec-and-plan package with the same `plan execution` transition as current combined small/medium work.
3. Create `references/large-phased-lifecycle.md`, move the detailed large layout and the intact bodies of `rule:lifecycle.large-phase-orchestration` and `rule:lifecycle.large-anchor-spec` to it, and preserve their IDs.
4. Replace moved lifecycle content with a concise large-flow dispatch in `artifact-contract.md`; update module ownership and large-route callers without changing large behavior.
5. Update `references/maintenance-architecture.md` to list the new large-only policy owner and lean/small route relationship.

Exit criteria: The lifecycle core can classify lean/small work without loading detailed large planning material; existing large rule IDs resolve only from the new reference.

#### `CHECK-001` Lifecycle and owner inspection

Covers: `VER-001`, `VER-004`.

Method: Search lifecycle references and router callers for `lean/small`, `rule:lifecycle.large-anchor-spec`, and `rule:lifecycle.large-phase-orchestration`; run the policy validator after the later tasks complete.

Expected result: Lean/small eligibility and escalation are explicit; each moved rule has exactly one canonical owner and all large callers point to it.

Evidence record: `snapshots/test-cases.snapshot.md`, full validator output, and implementation review notes.

### `TASK-002` Add lean freeze and execution routing without model-policy load

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: Lean planning-shape facts, shared freeze-gate mechanics, and existing fresh-authorization rules.
2. Produces: A lean/small route that retains review, approval, approval commit, immutability, and pause controls while omitting frozen model and sub-agent selection.

Implementation:

1. Restructure or supplement `planning-freeze-gates.md` so the shared draft-review and approval-freeze mechanics apply to lean/small packages without requiring `rule:models.selection-dimensions`, model fields, or a sub-agent assessment.
2. Preserve the existing model/continuity requirements exactly for small/medium and large/phased packages, whether retained in place or moved to a dedicated companion reference.
3. Define lean post-freeze routing: the frozen package records `Stage: plan execution`; the same operator manually orchestrates execution or provides explicit instructions for its runtime method, orchestration, model, and review; no new operator or session is implied. Material scope changes still follow variance/amendment rules.
4. Add a dedicated lean execution router row that does not load model policy or implementation changelog during ordinary startup. Retain the implementation-changelog reference as a just-in-time requirement immediately before an implementation commit.
5. Update the central router so the lean drafting row loads only its compact lifecycle, naming, quality, freeze, and template inputs; it must explicitly exclude model policy, role examples, artifact style, architecture snapshot by default, and changelog.

Exit criteria: Lean packages have the same approval/commit/pause gate sequence as combined small/medium packages, but no model-policy dependency before an explicit post-freeze execution instruction.

#### `CHECK-002` Lean policy exclusion inspection

Covers: `VER-002`.

Method: Add and run validator assertions for the lean route's required and forbidden references; inspect the freeze text for a lean-specific branch and the existing small/medium/large model branches.

Expected result: Lean route assertions reject model, role-example, artifact-style, and changelog inputs while existing flow assertions remain unchanged and pass.

Evidence record: `snapshots/test-cases.snapshot.md` and full validator output.

### `TASK-003` Build isolated compact lean templates

Dependencies: `TASK-001`, `TASK-002`.

Interfaces:

1. Consumes: Lean lifecycle/freeze contract and current template assembler conventions.
2. Produces: `lean-small-work-item-spec.md` and `lean-small-work-item-plan.md`, generated from new manifests and dedicated lean source blocks.

Implementation:

1. Add a lean spec manifest and four dedicated blocks covering compact metadata/goal/scope, material context/decisions/risks, stable `SPEC-*` and `VER-*` entries, and documentation/commit/readiness/approval state.
2. Add a lean plan manifest and four dedicated blocks covering compact metadata/exact inputs, change surfaces/approach, bounded `TASK-*` units with nested `CHECK-*` evidence, and validation/variance/approval state.
3. Ensure the plan and spec retain the canonical two-artifact package, stable identifiers, statuses, approval subject, documentation assessment, and no-placeholder readiness checks.
4. Do not use shared small/medium blocks. In particular, omit `spec.085.small.handoff.md`, `plan.055.common.model-strategy.md`, `plan.085.small.handoff.md`, header style cues, and `plan.060.small.planned-commits.md` changelog wording.
5. Add the two manifests to the explicit `ASSEMBLIES` list, generate outputs with `assemble_templates.py --write`, and retain all current assembly ordering and behavior.

Exit criteria: Lean templates are self-contained, compact, assembled only from lean blocks, and contain no forbidden strategy, handoff, style, or changelog prompts.

#### `CHECK-003` Template assembly and negative contract

Covers: `VER-002`, `VER-003`.

Method: Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`; add validator assertions for lean manifests, generated output, required ID/approval sections, and forbidden references.

Expected result: Both new generated templates match their manifests; required lean content is present and all excluded references are absent.

Evidence record: Assembler and validator output.

### `TASK-004` Extend additive validation and operator guidance

Dependencies: `TASK-001`, `TASK-002`, `TASK-003`.

Interfaces:

1. Consumes: Final lifecycle, router, freeze, templates, and generated outputs.
2. Produces: Lean/small regression coverage, updated user-facing route guidance, and durable test-case evidence.

Implementation:

1. Extend `test_harness_policy.py` with explicit lean template/manifests lists, route requirements, negative-reference checks, large-owner relocation checks, and a lean/small scenario. Do not rename or weaken existing small/medium or large fixtures, and do not introduce a flow registry.
2. Update `snapshots/test-cases.snapshot.md` with lean automatic/override selection, escalation, compact-template exclusions, freeze equivalence, large-policy isolation, existing-flow continuity, and historical-preservation scenarios.
3. Update `README.md` and `docs/operator-note.md` to describe lean/small as additive, state the operator override and escalation rule, and say that established names remain pending a separate terminology work item.
4. Run the full harness policy validator, template freshness check, `git diff --check`, and a name-only diff review confirming no historical work item, release note, or changelog history was modified.

Exit criteria: New coverage proves the lean contract and relocated large ownership; operator documentation is clear; existing-flow and historical-artifact preservation are evidenced.

#### `CHECK-004` Full policy regression suite

Covers: `VER-001`, `VER-002`, `VER-003`, `VER-004`, `VER-005`.

Method: Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`, and `git diff --check`; inspect `git diff --name-only`.

Expected result: Both Python commands exit 0, the diff has no whitespace errors, and changed paths exclude historical work items, release notes, and `CHANGELOG.md` history.

Evidence record: Command output and final independent-review report.

## Model and sub-agent strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: `bounded strategy`.
2. Fit reason: The plan has discrete policy, template, and review concerns, but implementation must be integrated by one orchestration session because router, validator, and reference changes are coupled.
3. Authorization state: `Approved — the operator explicitly approved sub-agent use in this task`.

Sub-agent `implementation-task executor`:

1. Purpose: Execute one approved Plan Task at a time with the task's bounded file ownership.
2. Context strategy: `curated artifacts`.
3. Input context: Approved spec, plan, required snapshot, named task files, and prior-task diff.
4. Output artifact: Focused patch, validation output, and task report.
5. Active model policy: `economy-default`.
6. Recommended sub-agent model: Generation `latest available`; Capability tier `balanced`; Reasoning effort `medium`.
7. Availability/fallback: Use the orchestration session when task-specific delegation is unavailable.
8. Parallel execution: `No — policy and validator files are shared integration surfaces`.
9. Blast radius if wrong: `Medium — could alter harness routing or leave generated assets stale`.
10. Write authority: `Only paths named by the active Plan Task`.
11. Concurrency: `single run`.

Sub-agent `independent harness reviewer`:

1. Purpose: Review task diffs and final integration for routing regressions, accidental model-policy loads, and compatibility drift.
2. Context strategy: `curated artifacts`.
3. Input context: Approved spec and plan, relevant task files, generated templates, diff, and validation evidence.
4. Output artifact: Evidence-backed findings with severity and reproduction or validation path.
5. Active model policy: `economy-default`.
6. Recommended sub-agent model: Generation `latest available`; Capability tier `balanced`; Reasoning effort `high` because it is an independent policy review.
7. Availability/fallback: Record an execution-controller self-review limitation only if independent review is unavailable.
8. Parallel execution: `No — review follows the task diff or final integrated diff`.
9. Blast radius if wrong: `Medium — missed policy regressions can affect all future work items`.
10. Write authority: `read-only`.
11. Concurrency: `single run`.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `docs: lean-small-flow-plan -- approve compact harness route` |
| Implementation | `feat: lean-small-flow -- add compact harness route` |

One cohesive implementation commit is the default because router, lifecycle, templates, and validator assertions form one compatibility unit.

## Validation and variance

The plan's checks provide the required evidence. Any later change that weakens approval/freeze mechanics, reintroduces a forbidden lean dependency, renames an established flow, or changes historical artifacts is material and requires an amendment plus operator approval.

## Implementation handoff

### Approved next stage

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

- Method: `superpowers:subagent-driven-development`.
- Orchestration mode: `bounded delegated sub-agents`.
- Run in: `new orchestration session`.
- Review: `Independent reviewer after each Plan Task and independent final whole-branch review`.

#### Model

- Generation: `latest available`.
- Capability tier: `balanced`.
- Reasoning: `medium`.

#### Execution requirements and contingencies

Start only after the planning package freezes and the operator gives fresh authorization. Load the approved spec, plan, architecture snapshot, test-case snapshot, and any approved amendment. Stop for a material variance; use the orchestration-session fallback only if approved sub-agent execution or independent review is unavailable and disclose the assurance gap.

## Readiness

- [x] Inputs, architecture decisions, change surfaces, tasks, and checks are sufficient for a fresh executor.
- [x] Each task has a bounded outcome, dependencies, concrete steps, an observable exit criterion, and nested checks.
- [x] Checks cover every verification criterion.
- [x] Required operator documentation and test-case outputs have owners.
- [x] Existing flow labels remain intact and no terminology migration is included.
- [x] No unresolved implementation decision or placeholder remains.

## Completion

- Required work and evidence are complete; any noteworthy variance is recorded.
- Planned changes are committed, or the blocker is stated.

## Approval

- Status: Approved
- Superseded by: None
