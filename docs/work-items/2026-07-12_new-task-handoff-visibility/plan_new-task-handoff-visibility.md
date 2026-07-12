# New-Task Handoff Visibility Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` task-by-task. Do not use sub-agents unless a fresh operator instruction authorizes the recorded strategy change.

Work ID: `2026-07-12_new-task-handoff-visibility`
Short ID: `new-task-handoff-visibility`
Status: Approved
Harness release: `0.5+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:execution-quality`, `module:freeze-gate`, `rule:lifecycle.work-sizing`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.execution-continuity`, `rule:execution-quality.execution-thread-start`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

**Goal:** Restore unambiguous planning-shape and handoff-target behavior, then offer approval-gated configured task creation at actual new-task transitions.

**Architecture:** `module:lifecycle` classifies the frozen package and names the next activity before `module:models` continuity and `module:freeze-gate` route the conversational result. Context-specific template blocks preserve that distinction, while `module:execution-quality` remains the canonical new-task startup owner. A Codex-capable runtime creates the approved task using the visible handoff and recorded supported configuration; all other runtimes receive the same copy-ready handoff as a manual fallback.

**Tech stack:** Markdown policy and templates, JSON template assemblies, Python 3 validator and assembler, Git, and a capability-gated Codex task-creation action.

## Global Constraints

1. Preserve `economy-default` as the active repository policy; use the recorded capability tier and reasoning effort independently from the concrete runtime profile.
2. Keep combined spec-and-plan drafting as the default for small/medium work. A small/medium spec-only freeze must be an explicit reasoned exception that names plan drafting as its next activity.
3. Preserve the existing large/phased anchor-spec sequence; its next activity is phase-plan drafting unless combined planning is explicitly recorded.
4. Render a next-task handoff only for an actual frozen package boundary and name the exact frozen inputs plus the documented next activity.
5. For a compatible new-task route, display the handoff and proposed model configuration, then ask approval before calling a task-creation action. Do not create a task or begin its activity without that approval.
6. Use the exact supported recorded model and reasoning values when task creation is available. If the action or configuration is unavailable, state the limitation and provide the manual copy-ready handoff without silent substitution.
7. Keep same-task and justified-alternative authorization, fallback, runtime-permission, platform-availability, and variance controls intact.
8. Edit source blocks and assembly manifests before generated templates; never hand-edit generated templates.
9. Do not modify frozen historical work-item artifacts, root `CHANGELOG.md`, runtime configuration, or Codex product code.

## Input Artifacts

1. Approved draft spec: `docs/work-items/2026-07-12_new-task-handoff-visibility/spec_new-task-handoff-visibility.md`.
2. Architecture input: `docs/work-items/2026-07-12_new-task-handoff-visibility/snapshots/architecture.snapshot.md`, especially `DEC-001` through `DEC-003`.
3. Test cases: `docs/work-items/2026-07-12_new-task-handoff-visibility/snapshots/test-cases.snapshot.md`.
4. Lifecycle and transition owners: `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`, `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`, and `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`.
5. Current consumers: `.agents/skills/dev-doc-harness/assets/templates/blocks/handoff.085.common.execution-thread.md`, the four primary template assemblies, generated templates, `README.md`, `.agents/skills/dev-doc-harness/docs/operator-note.md`, and `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
6. Historical comparison only: `docs/work-items/2026-07-11_model-selection-dimensions/` as a combined small/medium package and `docs/work-items/2026-07-11_commitment-verification-model/` as an explicit staged exception.
7. Unresolved implementation context: none. Runtime task-creation availability and supported model values are checked only at execution preflight; the plan supplies its fallback.

## Commitment-Disposition Mapping

| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` visible new-task handoff | implement | `TASK-002`, `TASK-003`, `TASK-004` |
| `SPEC-002` approval-gated task creation | implement | `TASK-002`, `TASK-003`, `TASK-005` |
| `SPEC-003` manual handoff fallback | implement | `TASK-002`, `TASK-003`, `TASK-005` |
| `SPEC-004` preserve alternative continuity routes | implement | `TASK-002`, `TASK-005` |
| `SPEC-005` consistent discoverable guidance | implement | `TASK-001`–`TASK-005` |
| `SPEC-006` explicit planning shape and handoff target | implement | `TASK-001`–`TASK-005` |

## Verification-Execution Mapping

| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` new-task handoff is executable from the conversation | `CHECK-002`, `CHECK-003` | implementation and final review |
| `VER-002` task creation is explicit and correctly configured | `CHECK-001`, `CHECK-002`, `CHECK-003` | RED baseline, implementation, final review |
| `VER-003` unavailable creation preserves the manual route | `CHECK-001`, `CHECK-002` | RED baseline and implementation |
| `VER-004` non-new-task flows remain authorized and bounded | `CHECK-002`, `CHECK-003` | implementation and final review |
| `VER-005` current consumers agree | `CHECK-002`, `CHECK-003`, `CHECK-004` | implementation, final review, pre-commit |
| `VER-006` handoff target matches the frozen package | `CHECK-001`, `CHECK-002`, `CHECK-003` | RED baseline, implementation, final review |

Architecture coverage:

1. Architecture input: `DEC-001` routes an actual freeze response by continuity, `DEC-002` derives exact frozen inputs, and `DEC-003` makes package shape and named next activity precede continuity routing.
2. Plan usage: `TASK-002` assigns ownership to lifecycle, freeze, models, and startup references; `TASK-003` encodes the context-specific template interfaces; `TASK-001` and `TASK-005` prevent consumer drift.
3. Drift path: before freeze, update this plan and the draft spec/snapshot directly. After freeze, use `implementation-notes/variance-log.md` and an amendment when `rule:lifecycle.variance-policy` requires approval.
4. Reinterpretation guard: no task may treat a generic `Next-task handoff` heading as a lifecycle classification; the approved package shape and named next activity are authoritative.

## Implementation Approach

Add focused failing validator assertions first, because this is a policy-contract regression that can otherwise recur through templates. Establish an explicit lifecycle rule for default combined small/medium packages and a recorded exception for staged small/medium packages; then make the freeze gate consume the resulting package shape and next activity before it assesses continuity and creation capability.

Replace the one shared handoff block with context-specific blocks selected by each of the four assembly manifests. The combined small/medium spec block describes the default package and prohibits an independent plan-drafting transition; the large-anchor block targets phase-plan drafting; the plan/phase-plan block describes an execution/replanning handoff. Regenerate all outputs, align operator guidance, and verify the validator plus assembly parity before committing.

## Change Surfaces

Expected edits:

1. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: add the owned planning-shape rule, define combined small/medium drafting and the explicit staged exception, and preserve the large/phased sequence.
2. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: route each post-freeze result from frozen package shape, named next activity, continuity, capability, and explicit creation approval.
3. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` and `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`: require continuity handoffs to refer to the actual frozen boundary and named activity; preserve startup, fallback, and variance behavior.
4. `.agents/skills/dev-doc-harness/references/policy-architecture.md` and `.agents/skills/dev-doc-harness/SKILL.md`: expose the new lifecycle/freeze ownership route without duplicating policy.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/handoff.085.common.execution-thread.md`: replace its ambiguous all-template prompt with context-specific source blocks for combined small specs, large anchors, and execution/replanning plans.
6. `.agents/skills/dev-doc-harness/assets/templates/assemblies/small-medium-work-item-spec.json`, `small-medium-work-item-plan.json`, `large-phased-work-item-spec.json`, and `large-phased-work-item-phase-plan.json`: select the correct handoff block for each artifact shape.
7. The four generated primary templates under `.agents/skills/dev-doc-harness/assets/templates/`: regenerate with `assemble_templates.py --write` only.
8. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: add focused policy and template assertions for package shape, exact transition target, creation approval, and manual fallback.
9. `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`: explain the default combined small/medium path, explicit staged exception, and transition result in compact operator language.
10. `docs/work-items/2026-07-12_new-task-handoff-visibility/deltas/operator-manual.delta.md` and `changelog/implementation.md`: record the completed operator-facing change and implementation commit source.

Stable interfaces:

1. `economy-default`, durable capability tiers, model-selection dimensions, context visibility semantics, runtime permission, platform availability, concurrency limits, variance classes, and final integration ownership remain unchanged.
2. `rule:execution-quality.execution-thread-start` remains the startup owner; task creation supplies its initial prompt but does not bypass preflight.
3. Existing large/phased anchor-spec lifecycle and frozen historical packages remain unchanged.

Changed interfaces:

1. Each freeze transition records `Planning shape`, `Frozen package`, and `Next activity` before its continuity and handoff fields.
2. A supported new-task transition presents an approval prompt that includes the proposed model generation, resolved profile when exposed, capability tier, reasoning effort, orchestration mode, and fallback.
3. Template-specific handoff prompts replace the single context-free prompt.

Implementation boundaries:

1. Codex Desktop itself, its task-creation tool schema, model availability, and non-Codex platform adapters remain out of scope; harness guidance consumes an exposed capability rather than implementing it.
2. A new automated task-creation integration test outside the Markdown/Python harness validator remains out of scope; static scenario coverage and current-session preflight are the available repository evidence.

## Model and Sub-agent Strategy

Selection dimensions:

1. Model generation: `GPT-5.6`.
2. Capability tier: `flagship`.
3. Reasoning effort: `high`.
4. Orchestration mode: `single-agent`.
5. Resolved profile: `gpt-5.6-sol` when the execution runtime exposes that profile.
6. Availability/fallback: use `gpt-5.6-sol` at `high` when exposed and permitted; otherwise use `gpt-5.6-terra` at `high` with the same single-agent review, then the current permitted main-agent profile plus deterministic validation if neither override is available.
7. Execution continuity: `new task with curated-artifact handoff` after the combined spec-and-plan approval freeze.
8. Context visibility: `not exposed`.
9. Artifact rehydration required: `Yes`; load the frozen spec, plan, architecture snapshot, test-case snapshot, applicable instructions, and any approved amendment before editing.
10. Model-policy source: repository `AGENTS.md`, active `economy-default`.
11. Override scope and expiry: implementation and final policy review for this work item only.

Fit assessment:

1. Complexity: medium; the edit set spans canonical policy, source/generated templates, validator behavior, and operator documentation.
2. Risk and blast radius: high; ambiguous lifecycle prompts affect every future substantial work item.
3. Ambiguity: low after the recorded root-cause comparison, but subtle wording can reinstate an implicit transition.
4. Budget and latency fit: a single flagship/high pass avoids integration overhead across tightly coupled policy surfaces; the balanced fallback retains deterministic validation.

Recommended selection change:

1. Escalate from the repository's normal economy starting point to `gpt-5.6-sol` at `high` for implementation and final review because the work sets a process-wide lifecycle contract.

Sub-agents:

1. None. The source blocks, manifests, canonical policies, generated templates, and validator assertions are tightly coupled; one orchestration thread should own their integration and final interpretation. The approved fallback is a second main-agent diff review after validation.

## Implementation Tasks

### `TASK-001` Implementation Task — establish failing transition-contract checks

Dependencies:

1. Frozen combined spec-and-plan package and a clean worktree preflight.

Implementation:

1. In `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, add `lifecycle.transition-targets` to `CHECK_IDS` and define `assert_lifecycle_transition_targets()` beside `assert_execution_thread_start()`.
2. Make the assertion require: the combined small/medium spec-and-plan default; the recorded small/medium staged exception; the existing large-anchor phase-plan route; shape, frozen-package, and named-next-activity fields in relevant freeze/template consumers; explicit creation approval; exact supported configuration use; and visible manual fallback with no substitution.
3. Extend `assert_execution_thread_start()` only for its existing handoff interface: require an actual frozen boundary and named next activity without making it own lifecycle classification.
4. Run the focused validator before policy/template edits and preserve the expected failing `lifecycle.transition-targets` result as the RED evidence in the implementation record.

Exit criteria:

1. The new assertion fails only because the currently released policy/templates lack the planned planning-shape and transition-target contract; unrelated existing checks remain green.

### `TASK-002` Implementation Task — define lifecycle and freeze routing ownership

Dependencies:

1. `TASK-001` RED evidence.

Implementation:

1. Update `.agents/skills/dev-doc-harness/references/artifact-contract.md` to add an owned planning-shape rule that states: small/medium packages normally draft spec and plan together; small/medium spec-only freeze is an explicit reasoned exception; large/phased anchors retain their existing post-anchor sequence.
2. Update `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md` so an approval freeze first identifies its frozen package and documented next activity, then applies continuity and capability routing. State that a compatible new-task result displays the handoff and requests creation approval; after approval it creates the configured task; unavailable creation returns the manual handoff; same-task behavior remains separate.
3. Update `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` so its minimal transition handoff is emitted only for an actual frozen boundary and starts at the package's documented next activity. Update `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md` only where needed to preserve the named activity during startup.
4. Update `.agents/skills/dev-doc-harness/references/policy-architecture.md` and `.agents/skills/dev-doc-harness/SKILL.md` with compact routing references to the lifecycle owner and freeze interaction.
5. Run the focused validator. Remaining failures must be limited to the scheduled template and operator-guidance consumers.

Exit criteria:

1. Canonical ownership follows `DEC-001` through `DEC-003`, and no canonical reference claims that every spec is a plan-drafting transition.

### `TASK-003` Implementation Task — make handoff prompts artifact-shape aware

Dependencies:

1. `TASK-002` canonical contract.

Implementation:

1. Replace `blocks/handoff.085.common.execution-thread.md` with three source blocks: a combined-small-spec block that records the default combined package and prohibits an independent plan-drafting handoff; a large-anchor block that names phase-plan drafting; and a plan/phase-plan block that captures execution or documented replanning handoffs.
2. In every applicable block, require `Planning shape`, `Frozen package`, `Next activity`, continuity, context visibility, rehydration, exact inputs, approved strategy/fallback, variance stop condition, and conditional copy-ready prompt. The plan/phase-plan block also requires the approval-gated configuration display and manual fallback route.
3. Update the four assembly manifests so the small spec uses the combined-small-spec block, the large spec uses the anchor block, and the small plan plus phase plan use the execution/replanning block.
4. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`, then `--check`; do not edit any generated template directly.

Exit criteria:

1. All four generated templates are current, and their handoff prompts cannot imply a transition inconsistent with their artifact shape.

### `TASK-004` Implementation Task — align operator-facing lifecycle guidance

Dependencies:

1. `TASK-002` and `TASK-003`.

Implementation:

1. Update `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md` to distinguish the combined small/medium default, explicit staged small/medium exception, and large/phased anchor route in compact prose.
2. Explain that a visible handoff/task-creation offer follows the real frozen package boundary, names the next activity and proposed configuration, requires approval to create a supported configured task, and falls back to manual copy-ready handoff when unavailable.
3. Create `docs/work-items/2026-07-12_new-task-handoff-visibility/deltas/operator-manual.delta.md` with the exact durable operator-facing changes to apply after implementation.
4. Run focused searches for `Next-task handoff`, `small/medium`, `phase-plan drafting`, `next activity`, and `task creation` across canonical owners and generated templates; correct contradictory wording only in its owner.

Exit criteria:

1. An operator can determine whether a proposed transition is combined planning, explicit staged planning, or a large anchor without reading implementation code or historical work items.

### `TASK-005` Implementation Task — validate, review, and commit the policy package

Dependencies:

1. `TASK-001` through `TASK-004`.

Implementation:

1. Run every Plan Check below. Record execution instances, actual outputs, and pass/fail status in the completion handoff; create `implementation-notes/variance-log.md` only if nontrivial variance occurs.
2. Review `git diff --check`, `git diff --stat`, the full diff, and path-specific historical work-item changes. Confirm no frozen historical work item or root `CHANGELOG.md` was changed.
3. Perform the approved main-agent fallback review for lifecycle-owner drift, ambiguous template context, unsupported configuration substitution, and unauthorized task creation.
4. Create `changelog/implementation.md` with heading `### 2026-07-12_new-task-handoff-visibility -- create configured continuity tasks`, `Release target: unreleased`, `Package impact: distributable`, and `Release-note: include`; add concise `Changed` bullets synchronized with the planned implementation subject.
5. Stage only implementation paths and commit `docs: new-task-handoff-visibility -- create configured continuity tasks` after all checks pass.

Exit criteria:

1. Every applicable Verification Criterion has evidence-backed status, no blocking review finding remains, generated templates match their sources, and the implementation commit contains no unrelated work.

## Plan Checks

### `CHECK-001` Plan Check — capture transition-contract RED baseline

Covers:

1. `VER-002`.
2. `VER-003`.
3. `VER-006`.

Procedure:

1. Add `assert_lifecycle_transition_targets()` and its check ID as described in `TASK-001`.
2. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` before updating canonical policy or templates.

Expected result:

1. The command exits non-zero with `lifecycle.transition-targets` as the expected new failing contract; no unrelated existing check fails.

Evidence record:

1. Completion handoff entry with command output, commit state, and the exact failed check ID.

Stage or environment:

1. Pre-edit RED baseline.

Task/check coordination:

1. Gates `TASK-002`; unexpected failure returns to repository diagnosis before policy edits.

### `CHECK-002` Plan Check — validate canonical routing and generated templates

Covers:

1. `VER-001`.
2. `VER-002`.
3. `VER-003`.
4. `VER-004`.
5. `VER-005`.
6. `VER-006`.

Procedure:

1. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` after source-block and manifest edits.
2. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.
3. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result:

1. The assembly check exits `0` and prints `All assembled templates are current.`
2. The harness validator exits `0` and reports policy checks passed, including `lifecycle.transition-targets` and existing execution-thread checks.

Evidence record:

1. Completion handoff command outputs and generated-template diff summary.

Stage or environment:

1. Implementation after `TASK-003`.

Task/check coordination:

1. Validates `TASK-002` and `TASK-003`; failure returns to the canonical owner or source block named by the failed assertion.

### `CHECK-003` Plan Check — review transition scenarios and no-substitution rule

Covers:

1. `VER-001`.
2. `VER-002`.
3. `VER-003`.
4. `VER-004`.
5. `VER-006`.

Procedure:

1. Compare the final policy and generated templates against `CASE-001` through `CASE-008` in `snapshots/test-cases.snapshot.md`.
2. Confirm the combined small/medium spec has no independent plan-drafting handoff; staged small/medium and large-anchor handoffs name planning next steps; plan/phase-plan/amendment handoffs name the actual execution or replanning step.
3. Confirm compatible task creation requires approval and exact supported settings, while an unavailable action or configuration yields only the visible manual handoff.

Expected result:

1. Every case maps to one unambiguous policy/template route; no route offers an unauthorized task, an implied transition, or a substituted configuration.

Evidence record:

1. Review checklist in the completion handoff with case IDs and pass/fail findings.

Stage or environment:

1. Final policy review before commit.

Task/check coordination:

1. Gates `TASK-005` and complements the static validator with semantic review.

### `CHECK-004` Plan Check — inspect implementation scope and commit readiness

Covers:

1. `VER-005`.

Procedure:

1. Run `git diff --check` and `git diff --name-only -- docs/work-items`.
2. Review `git diff --stat` and the full diff, verifying source-first template generation, no root `CHANGELOG.md` edit, and no historical frozen-package rewrite.
3. Run `git diff --cached --check` and `git diff --cached --name-only` immediately before committing.

Expected result:

1. No whitespace errors appear; work-item changes are limited to `2026-07-12_new-task-handoff-visibility`; the staged file list contains only the planned implementation paths and matching implementation fragment.

Evidence record:

1. Completion handoff diff-review summary and final staged path list.

Stage or environment:

1. Pre-commit.

Task/check coordination:

1. Final gate for `TASK-005`.

## Planned Commits

Planning approval commit:

1. Planned subject: `plan: new-task-handoff-visibility -- clarify transition targets`.
2. Changelog title or snippet: `2026-07-12_new-task-handoff-visibility -- clarify transition targets`.
3. Notes: one combined approval commit for the spec, plan, architecture snapshot, test-cases snapshot, Superpowers pointers, and `changelog/planning-approval.md`.

Implementation commit:

1. Planned subject: `docs: new-task-handoff-visibility -- create configured continuity tasks`.
2. Changelog title or snippet: `2026-07-12_new-task-handoff-visibility -- create configured continuity tasks`.
3. Notes: one cohesive policy, template, generated-output, documentation, validator, operator delta, and implementation-fragment commit.

## Check Execution and Completion Records

For every Plan Check execution, record the `CHECK` ID, a unique execution instance, stage or environment, actual result, evidence location or inline evidence, and `pass`, `fail`, or `blocker` status. Repeated executions of an unchanged procedure produce distinct records. A material procedure change follows approved variance or amendment rather than silently reusing the ID.

Completion reports cite executed Plan Checks, resulting Verification Criterion status, remaining task or disposition status, variance, and residual risk. Task completion alone does not establish conformance.

## Plan Variance Handling

Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, lifecycle classification, task-creation authorization, API, data, security, privacy, compliance, scope, Verification Criterion, Plan Check, or feasibility changes.

## Planning Artifact Freeze Gate

Draft review status: the operator approved the spec on 2026-07-12; this plan completes the same combined small/medium package and remains Draft pending review.

After the operator approves the combined package, update both the spec and plan status fields to `Approved`, create `changelog/planning-approval.md` with the planned title and required release metadata, stage only the approved planning package and fragment, and commit them together. Stop before implementation.

## Next-Task Handoff

Planning shape: `combined small/medium`; this plan is the transition owner after the combined package freezes.

Execution continuity: `new task with curated-artifact handoff`.

Context visibility: `not exposed`; do not infer a compaction threshold.

Artifact rehydration required: `Yes`; the new task must load the exact frozen package, applicable `AGENTS.md`, and repository harness before editing.

Proposed configured task:

1. Model generation: `GPT-5.6`.
2. Resolved profile: `gpt-5.6-sol` when exposed and supported.
3. Capability tier: `flagship`.
4. Reasoning effort: `high`.
5. Orchestration mode: `single-agent`.
6. Approved fallback: `gpt-5.6-terra` at `high`, then the current permitted main-agent profile with deterministic validators and the recorded main-agent review.

Exact authoritative artifacts after approval:

1. `docs/work-items/2026-07-12_new-task-handoff-visibility/spec_new-task-handoff-visibility.md`.
2. `docs/work-items/2026-07-12_new-task-handoff-visibility/plan_new-task-handoff-visibility.md`.
3. `docs/work-items/2026-07-12_new-task-handoff-visibility/snapshots/architecture.snapshot.md`.
4. `docs/work-items/2026-07-12_new-task-handoff-visibility/snapshots/test-cases.snapshot.md`.
5. `docs/work-items/2026-07-12_new-task-handoff-visibility/changelog/planning-approval.md`.

First activity: `TASK-001` — establish the failing transition-contract checks.

Variance stop condition: stop for an approved amendment before changing lifecycle classification, handoff target, creation authorization, model-setting semantics, scope, Verification Criteria, Plan Checks, or plan feasibility.

Copy-ready handoff:

```text
Implement `2026-07-12_new-task-handoff-visibility` from its frozen combined planning package.

Read applicable `AGENTS.md`, the repository harness, and these exact artifacts:

- `docs/work-items/2026-07-12_new-task-handoff-visibility/spec_new-task-handoff-visibility.md`
- `docs/work-items/2026-07-12_new-task-handoff-visibility/plan_new-task-handoff-visibility.md`
- `docs/work-items/2026-07-12_new-task-handoff-visibility/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-07-12_new-task-handoff-visibility/snapshots/test-cases.snapshot.md`
- `docs/work-items/2026-07-12_new-task-handoff-visibility/changelog/planning-approval.md`

Follow `rule:execution-quality.execution-thread-start`. Use the approved GPT-5.6 / gpt-5.6-sol / flagship / high / single-agent strategy and its recorded fallback only when runtime permission and platform availability allow it. Start at `TASK-001`. Treat frozen decisions as authoritative and stop for variance that requires operator approval.
```

At the freeze gate, display this handoff and the proposed configuration, then ask approval to create the task with the handoff as its initial prompt. If a compatible task-creation action or exact supported configuration is unavailable, display this same handoff as the manual fallback; do not silently substitute settings.

## Plan Readiness Checklist

- [x] Input artifacts and relevant repository context have been read and listed.
- [x] Every in-scope Specification Commitment has an authorized disposition and every applicable Verification Criterion has Plan Check coverage.
- [x] Risks, scope boundaries, interfaces, and documentation decisions are either covered by tasks or explicitly marked as no-op with a reason.
- [x] Task detail is sufficient for a fresh implementation agent to execute without inventing task order, file scope, validation, or documentation steps.
- [x] Plan Checks have complete procedure, result, evidence-record, and stage/environment fields.
- [x] Planned commits and changelog title snippets are synchronized.
- [x] Variance handling is clear for likely implementation drift.
- [x] The work fits one orchestration thread; `Sub-agents: None` has a recorded fit rationale.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Completion Criteria

1. `VER-001` through `VER-006` have evidence-backed status and `TASK-001` through `TASK-005` are complete.
2. Template assembly and full harness validation pass.
3. The completed policy, templates, generated outputs, operator guidance, validator, and deltas agree on planning shape, named next activity, creation approval, and manual fallback.
4. The implementation fragment and planned implementation commit contain no unrelated work.
5. Completion reports executed Plan Checks, de-facto model/permission/availability/fallback result, execution continuity, any task-creation result, variance, and residual risk.

## Approval

- Status: Approved
- Superseded by: None
