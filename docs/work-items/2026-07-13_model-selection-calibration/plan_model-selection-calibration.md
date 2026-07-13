# Model-Selection Calibration Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

Work ID: `2026-07-13_model-selection-calibration`
Short ID: `model-selection-calibration`
Status: Approved
Harness release: `0.6+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.economy-default`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Input Artifacts

1. Draft spec: `spec_model-selection-calibration.md`.
2. Architecture input: `snapshots/architecture.snapshot.md` (`DEC-001`).
3. Required snapshots or deltas: `snapshots/test-cases.snapshot.md`, `deltas/testing-guide.delta.md`, and `deltas/operator-manual.delta.md`.
4. Research inputs: `evidence/model-selection-research.md`, `handoff/research-handoff.md`, and `artifact-index.md`.
5. Relevant repository files: `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`, `subagent-role-examples.md`, `assets/templates/blocks/plan.040.common.model-strategy.md`, `assets/templates/blocks/spec.060.large.phase-decomposition-model.md`, generated templates, assembly manifests, `scripts/assemble_templates.py`, and `scripts/test_harness_policy.py`.
6. Unresolved implementation context to confirm before editing: None identified; do not edit `AGENTS.md`, `README.md`, or frozen historical work items unless approved variance requires it.

## Commitment-Disposition Mapping

| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` Calibrate the bounded-work baseline | implement | `TASK-001`, `TASK-002` |
| `SPEC-002` Make escalation lifecycle-aware | implement | `TASK-001`, `TASK-002` |
| `SPEC-003` Define efficient independent review | implement | `TASK-001`, `TASK-002` |
| `SPEC-004` Keep reusable surfaces aligned without duplication | implement | `TASK-001`, `TASK-003`, `TASK-004` |

## Verification-Execution Mapping

| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` The calibrated allocation ladder is explicit and bounded | `CHECK-001`, `CHECK-004` | implementation, pre-commit |
| `VER-002` Escalation is not ceremonial or an approval substitute | `CHECK-001`, `CHECK-004` | implementation, pre-commit |
| `VER-003` Review independence and ownership remain clear | `CHECK-001`, `CHECK-003`, `CHECK-004` | implementation, review, pre-commit |
| `VER-004` Generated prompts and checks preserve canonical ownership | `CHECK-002`, `CHECK-003`, `CHECK-004` | implementation, review, pre-commit |

Architecture coverage:

1. Architecture input: `DEC-001` in `snapshots/architecture.snapshot.md`.
2. Plan usage: canonical policy owns allocation semantics; examples and source blocks prompt and illustrate; generated templates are assembly outputs; the validator protects these boundaries.
3. Drift path: update draft spec and snapshot before freeze; after freeze, use a variance record and amendment for policy ownership, allocation, authorization, or Verification Criterion changes.
4. Reinterpretation guard: do not turn examples or templates into a parallel decision tree, change permanent tiers, or treat benchmark results as a mandatory runtime configuration.

## Implementation Approach

First extend the policy validator with focused assertions that will fail until the agreed baseline, lifecycle boundary, independent-review shape, and prompt ownership are present. Then update the canonical policy and advisory reviewer examples together, preserving existing rule owners and avoiding a new review lifecycle.

Next, add only compact decision-recording prompts to the two shared source blocks, regenerate all affected templates through the repository assembler, and validate the generated result. Finish with a review that verifies every supporting edit has a distinct value and routes to the canonical policy rather than repeating it, then update work-item deltas, the implementation changelog entry, and the variance log before the implementation commit.

## Change Surfaces

Expected edits:

1. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: calibrate `economy-default`, escalation/de-escalation, and reviewer allocation semantics.
2. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`: align advisory reviewer context, lens, evidence, and integration examples.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.040.common.model-strategy.md` and `blocks/spec.060.large.phase-decomposition-model.md`: add one concise prompt addition that distinguishes baseline, effort/tier changes, and residual uncertainty.
4. `.agents/skills/dev-doc-harness/assets/templates/{small-medium-work-item-plan,large-phased-work-item-spec,large-phased-work-item-phase-plan}.md`: regenerated outputs only.
5. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: add focused model-policy and template-ownership assertions.
6. This work item’s deltas, snapshots, changelog fragments, and variance log: record delivery and execution evidence.

Stable interfaces:

1. Permanent `flagship`, `balanced`, and `fast/economy` tier names; GPT-5.6 provider mapping; authorization layers; orchestration-mode vocabulary; validator and assembler command-line arguments.

Changed interfaces:

1. Planner-facing strategy prompts: record a suggested baseline and a reasoned change classification without creating a mandatory allocation.
2. Reviewer guidance: record the independent-task and evidence-lens shape more explicitly while retaining orchestration-owned integration.

Implementation boundaries:

1. `AGENTS.md` stays unchanged because it selects, rather than defines, the active policy.
2. `README.md` stays unchanged unless a review finds a material operator-facing gap and an approved variance expands scope.
3. No current harness template outside the two shared model-strategy source blocks is edited unless assembly proves it consumes one of those blocks.
4. A supporting-surface edit is removed if it lacks a distinct canonical, illustrative, prompt, generated-output, or regression-protection purpose that the already changed surfaces cannot provide.

## Model and Sub-agent Strategy

Selection dimensions:

1. Model generation: `GPT-5.6` when available; otherwise `not exposed`.
2. Capability tier: `balanced` for implementation.
3. Reasoning effort: `medium` by default; `high` only when exact cross-surface policy reconciliation remains after the spec and plan are re-read.
4. Orchestration mode: `single-agent` with one independent review task when the changed diff is available.
5. Resolved profile: `Terra medium` preferred for execution; `Terra high` only for the documented effort escalation; `not exposed` if the runtime does not expose this mapping.
6. Availability/fallback: use the approved `balanced` configuration at the nearest available effort; if balanced is unavailable, use `fast/economy` medium for mechanical assembly or validator work and stop for confirmation before a capability-tier escalation.
7. Execution continuity: `new task with curated-artifact handoff` because planning and implementation should start from frozen artifacts with the selected runtime profile recorded afresh.
8. Context visibility: `not exposed`.
9. Artifact rehydration required: `Yes`; read `AGENTS.md`, the frozen spec, plan, architecture snapshot, test-case snapshot, research handoff, and changed canonical files before editing.
10. Model-policy source: `AGENTS.md` active `economy-default` policy, calibrated by this work item after freeze.
11. Override scope and expiry: this work item; any operator override remains authoritative and expires when the work item completes.

Fit assessment:

1. Complexity: medium; the work changes one canonical policy with tightly coupled examples, prompts, generated outputs, and structural checks.
2. Risk and blast radius: medium; ambiguous guidance can produce recurring quality, latency, and cost errors across later work items, but no runtime application interface changes.
3. Ambiguity: low after the research handoff and this combined package; a newly found policy conflict is a named escalation or variance trigger.
4. Budget and latency fit: Terra medium is the normal implementation allocation; a bounded Terra-high pass or review is cheaper than a ceremonial Sol allocation.

Recommended selection change:

1. Use Terra medium for the clear-plan executor. Escalate effort to Terra high only for named cross-surface reconciliation. Escalate tier to Sol medium only if a high-impact canonical-policy conflict remains after that bounded pass; Sol high is reserved for a separately scoped adversarial review of an unresolved foundational conflict.

Sub-agents:

1. One read-only independent reviewer is justified after implementation because the work changes the reviewer policy itself and cross-surface wording can drift. No write-capable sub-agents are planned.

Sub-agent `review-001`:

1. Purpose: independently review the implementation diff for canonical-owner duplication, escalation/variance conflation, and reviewer-integration regressions.
2. Context strategy: `curated artifacts`.
3. Input context: frozen spec, plan, architecture and test-case snapshots, changed diff, validator output, and `subagent-model-policy.md`.
4. Output artifact: `review/policy-independence-review.md` with severity, evidence, and a reproduction or validation path for each finding.
5. Model policy: active repository policy, `economy-default`.
6. Model generation: `GPT-5.6` when exposed; otherwise `not exposed`.
7. Capability tier: `balanced`.
8. Resolved profile: `Terra high` when exposed; otherwise `not exposed`.
9. Availability/fallback: orchestration-thread adversarial review using the same curated inputs.
10. Reasoning effort: `high` because the narrow lens is cross-surface policy conflation, not broad implementation discovery.
11. Selection reason: the reviewer is deliberately independent of the executor’s rationale and may use more effort than the clear-plan executor.
12. Parallel execution: `No`; it starts after the implementation diff and validator evidence exist.
13. Blast radius if wrong: `Medium`; a missed policy conflict can misdirect later planning work, but the orchestration thread retains final integration and validation.

## Implementation Tasks

### `TASK-001` Implementation Task — Add focused calibration regression checks

Dependencies:

1. Frozen `SPEC-001` through `SPEC-004` and `snapshots/test-cases.snapshot.md`.

Implementation:

1. In `scripts/test_harness_policy.py`, extend `assert_model_selection_dimensions` or a focused companion assertion with checks for the Terra-medium suggested baseline, effort-versus-tier distinction, named residual uncertainty or variance for late escalation, de-escalation when remaining work is bounded, and the missing-decision approval boundary.
2. Add checks that the canonical policy and advisory role examples retain a separate curated-artifact reviewer with a named lens, evidence-backed finding shape, and orchestration-owned integration.
3. Add compact source-block or generated-template checks that distinguish a baseline from effort/tier changes and preserve canonical-policy routing; do not test for a copied allocation ladder in templates or add a generic line-count policy.
4. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` before the policy edits and record the expected failing calibration assertion in the execution record.

Exit criteria:

1. The new assertions fail only because the pre-change policy has not yet been calibrated, and their labels identify each required semantic boundary.

Notes:

1. This task is the red phase for `VER-001` through `VER-004`; do not weaken existing permanent-tier, authorization, `ultra`, or generated-template assertions.

### `TASK-002` Implementation Task — Calibrate canonical policy and review examples

Dependencies:

1. `TASK-001`.

Implementation:

1. Update `references/subagent-model-policy.md` under `Policy: economy-default` and `Escalation rules` with the bounded Terra-medium baseline, Terra-high effort escalation, Sol-medium tier escalation, exceptional Sol-high condition, lifecycle-aware de-escalation, and variance/approval boundary specified by `SPEC-001` and `SPEC-002`.
2. Update existing review guidance in the canonical policy to require a separate task or thread, curated artifacts, one named lens, evidence-backed severity plus reproduction or validation path, and orchestration-owned final integration; retain review as a suggested allocation, not a mandatory new gate.
3. Update `references/subagent-role-examples.md` so its independent reviewer pattern illustrates the same bounded context, lens, evidence, and ownership shape without repeating the policy allocation ladder.
4. Run the policy validator and inspect only the failures attributable to unmodified template prompts; record any conflict with existing rule owners as a variance candidate rather than resolving it by expanding scope.

Exit criteria:

1. Canonical and advisory guidance meet `VER-001` through `VER-003`, preserve permanent tier and authorization language, and have no unresolved policy conflict.

### `TASK-003` Implementation Task — Regenerate compact strategy prompts

Dependencies:

1. `TASK-002`.

Implementation:

1. Update `assets/templates/blocks/plan.040.common.model-strategy.md` and `blocks/spec.060.large.phase-decomposition-model.md` with one concise recording cue for suggested baseline, effort-versus-tier change classification, and named residual uncertainty or variance for a later-stage escalation; keep detailed semantics routed to `module:models`.
2. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` to regenerate all consuming templates and execute its embedded policy validation.
3. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` to verify generated outputs are current.

Exit criteria:

1. All consuming generated templates are fresh, retain required selection fields, add only compact prompts, and satisfy `VER-004`.

### `TASK-004` Implementation Task — Review, document, and record delivery evidence

Dependencies:

1. `TASK-002` and `TASK-003`.

Implementation:

1. Create `review/policy-independence-review.md` through the approved read-only `review-001` strategy, or complete the documented fallback adversarial review if that strategy is unavailable; require the review to identify the distinct purpose of every changed supporting surface and resolve or document all findings before commit.
2. Update `deltas/testing-guide.delta.md` with validation commands and `deltas/operator-manual.delta.md` with concise baseline, escalation, de-escalation, variance, and review-lens guidance; do not change `README.md` without approved variance.
3. Create or update `implementation-notes/variance-log.md` with the actual variance result, including an explicit `None` result when no variance occurred.
4. Update `changelog/implementation.md` before the implementation commit, run the Plan Checks, review the diff for scope and duplicate-policy drift, and commit only the approved implementation surfaces.

Exit criteria:

1. `CHECK-001` through `CHECK-004` have recorded outcomes, documentation and changelog artifacts are current, review findings are resolved or accepted by the orchestration thread, and the implementation commit is ready with no unapproved scope expansion.

## Plan Checks

### `CHECK-001` Plan Check — Run calibrated policy validation

Covers:

1. `VER-001`.
2. `VER-002`.
3. `VER-003`.
4. `VER-004`.

Procedure:

1. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` from the repository root after `TASK-003`.

Expected result:

1. Exit code `0` and the validator reports the model-selection, template-assembly, duplicate-policy, and current-historical compatibility checks as passing.

Evidence record:

1. Record the command, execution instance, output summary, and pass/fail status in `implementation-notes/variance-log.md` or the implementation completion record.

Stage or environment:

1. Implementation and pre-commit.

Task/check coordination:

1. `TASK-003` must complete before this check; a failure blocks `TASK-004` commit preparation.

### `CHECK-002` Plan Check — Verify generated-template freshness

Covers:

1. `VER-004`.

Procedure:

1. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` after the assembly write step.

Expected result:

1. Exit code `0` and output includes `All assembled templates are current.`

Evidence record:

1. Record the command, execution instance, output, and pass/fail status in the implementation completion record.

Stage or environment:

1. Implementation and pre-commit.

Task/check coordination:

1. `TASK-003` enables this check; stale output returns to that task.

### `CHECK-003` Plan Check — Perform independent policy-boundary review

Covers:

1. `VER-003`.
2. `VER-004`.

Procedure:

1. Give `review-001` only the curated artifacts named in its strategy and request a review of canonical-owner duplication, effort/tier/variance conflation, and final-integration ownership.
2. Verify each reported finding includes severity, concrete evidence, and a reproduction or validation path; the orchestration thread decides integration.

Expected result:

1. The review report contains no unresolved blocking finding, and the final diff has no duplicate allocation ladder, new mandatory reviewer gate, or supporting-surface edit whose distinct purpose cannot be stated.

Evidence record:

1. `review/policy-independence-review.md` and the implementation completion record.

Stage or environment:

1. Review, after `TASK-003` and before the implementation commit.

Task/check coordination:

1. `TASK-004` cannot finish until blocking findings are resolved or the operator approves a variance amendment.

### `CHECK-004` Plan Check — Inspect scope and whitespace before commit

Covers:

1. `VER-001`.
2. `VER-002`.
3. `VER-003`.
4. `VER-004`.

Procedure:

1. Run `git diff --check` and review `git diff -- .agents/skills/dev-doc-harness/references/subagent-model-policy.md .agents/skills/dev-doc-harness/references/subagent-role-examples.md .agents/skills/dev-doc-harness/assets/templates .agents/skills/dev-doc-harness/scripts/test_harness_policy.py docs/work-items/2026-07-13_model-selection-calibration`.
2. Confirm the diff excludes `AGENTS.md`, `README.md`, frozen historical work items, and root `CHANGELOG.md` unless an approved variance explicitly adds one of them.

Expected result:

1. `git diff --check` exits `0`, and the reviewed diff is limited to the planned surfaces with no duplicated canonical decision tree.

Evidence record:

1. Record the commands, diff scope, and pass/fail status in the implementation completion record.

Stage or environment:

1. Pre-commit.

Task/check coordination:

1. `TASK-004` uses this check to gate the implementation commit.

## Planned commits

Planning approval commit:

1. Planned subject: `plan: model-selection-calibration -- approve calibrated economy guidance`.
2. Changelog title or snippet: `2026-07-13_model-selection-calibration -- approve calibrated economy guidance`.
3. Notes: approval commit for this spec, plan, architecture snapshot, test-case snapshot, and planning source fragment only.

Implementation commit:

1. Planned subject: `docs: model-selection-calibration -- calibrate economy model guidance`.
2. Changelog title or snippet: `2026-07-13_model-selection-calibration -- calibrate economy model guidance`.
3. Notes: canonical policy, advisory examples, source and generated templates, validator, deltas, review evidence, variance log, and implementation source fragment.

## Check execution and completion records

1. For each Plan Check, record its ID, unique execution instance, stage, actual result, evidence location, and `pass`, `fail`, or `blocker` status.
2. Completion reporting must distinguish executed Plan Check status from task completion, identify de-facto reviewer use and fallback if applicable, and name residual risk.

## Plan variance handling

1. Before freeze, edit this draft directly for operator feedback.
2. After freeze, record nontrivial variance in `implementation-notes/variance-log.md`; create an amendment and request approval for any changed policy owner, permanent tier, authorization boundary, scope, Specification Commitment, Verification Criterion, Plan Check, or plan feasibility.

## Planning artifact freeze gate

1. Draft review status: design approved and package approved by the operator on 2026-07-14.
2. Approval commit status: created using the planned approval subject in this package.
3. Post-freeze implementation authorization: not granted; do not execute `TASK-001` through `TASK-004` until the planning package is frozen and a fresh operator instruction authorizes implementation.

## Next-task handoff

1. Planning shape: `combined small/medium`.
2. Frozen package: `spec_model-selection-calibration.md`, this plan, `snapshots/architecture.snapshot.md`, `snapshots/test-cases.snapshot.md`, `deltas/testing-guide.delta.md`, `deltas/operator-manual.delta.md`, `evidence/model-selection-research.md`, `handoff/research-handoff.md`, `artifact-index.md`, and `changelog/planning-approval.md`.
3. Next activity: implement `TASK-001` through `TASK-004` in order, starting with the focused calibration regression checks.
4. Execution continuity: `new task with curated-artifact handoff`.
5. Context visibility: `not exposed`.
6. Artifact rehydration required: `Yes`; read the frozen package, `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, and `rule:execution-quality.execution-thread-start` before editing.
7. Exact authoritative artifacts: the frozen package listed above plus any later approved amendment.
8. Approved strategy and fallback: Terra medium is the preferred `balanced` executor allocation; Terra high is a named effort escalation; use the nearest available `balanced` configuration when exposed, permit `fast/economy` medium only for mechanical assembly or validation, and stop for confirmation before a tier escalation.
9. First activity: `TASK-001` — add focused calibration regression checks and record the expected pre-change failure.
10. Variance stop condition: stop for approval-required variance if policy ownership, permanent tiers, authorization boundaries, scope, Specification Commitments, Verification Criteria, Plan Checks, or plan feasibility must change.

## Plan readiness checklist

- [x] Input artifacts and relevant repository context are listed.
- [x] Every in-scope Specification Commitment has an authorized disposition and every applicable Verification Criterion has Plan Check coverage.
- [x] Risks, scope boundaries, interfaces, and documentation decisions are either covered by tasks or explicitly marked as no-op with a reason.
- [x] Task detail is sufficient for a fresh implementation agent or delegated reviewer to execute without inventing task order, file scope, validation, or documentation steps.
- [x] Plan Checks have complete procedure, result, evidence-record, and stage/environment fields.
- [x] Planned commits and changelog title snippets are synchronized.
- [x] Variance handling is clear for likely implementation drift.
- [x] The work fits one orchestration thread with a bounded independent-review strategy.
- [x] The sub-agent strategy follows `module:models` and has a documented fallback.
- [x] No unresolved placeholders, required decisions, sections, or ownerless deferrals remain.

## Completion criteria

1. `VER-001` through `VER-004` have evidence-backed status.
2. `CHECK-001` through `CHECK-004` have recorded results.
3. Required policy, prompt, template, validator, and work-item documentation artifacts are updated.
4. The implementation fragment and variance log exist before the implementation commit.
5. The implementation commit excludes unrelated user work and root `CHANGELOG.md` unless later explicitly owned consolidation requires it.

## Approval

- Status: Approved
- Superseded by: None
