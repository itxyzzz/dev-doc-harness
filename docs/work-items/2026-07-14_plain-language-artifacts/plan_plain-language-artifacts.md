# Plain-language Artifact Policy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

Work ID: `2026-07-14_plain-language-artifacts`
Short ID: `plain-language-artifacts`
Status: Approved
Harness release: `0.6+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:artifact-style`, `module:models`, `module:freeze-gate`, `rule:style.template-prompts`, `rule:models.strategy-required`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

**Goal:** Make ordinary `must` and `should` wording the enforceable authoring voice for current harness guidance and new durable artifacts without changing frozen history or the legal license.

**Architecture:** `artifact-style.md` owns one compact rule; the skill router ensures planners load it; the shared specification block makes the rule visible at the moment authors write commitment statements. The policy validator checks these layers and a narrow active-path scan while the template assembler keeps generated outputs synchronized.

**Tech stack:** Markdown policy and templates; Python standard-library validator and assembler; PowerShell and Git checks.

## Global constraints

1. Preserve frozen `docs/work-items/**` artifacts and `LICENSE` byte-for-byte.
2. Use `must` for obligations and `should` for recommendations in all newly edited authoring prose.
3. Keep `module:artifact-style` as the sole canonical owner; templates repeat only a concise operational cue.
4. Change generated templates only by editing `blocks/spec.030.common.commitments-verification.md` and running the repository assembler.
5. Record source fragments and update root `CHANGELOG.md` before every work-item commit, as required by repository agent instructions.
6. Do not begin any task until this combined package is frozen and a fresh operator instruction authorizes implementation.

## Input artifacts

1. Draft specification: `spec_plain-language-artifacts.md`.
2. Architecture input: `snapshots/architecture.snapshot.md`.
3. Test-case input: `snapshots/test-cases.snapshot.md`.
4. Repository instructions: `AGENTS.md` and `.agents/skills/dev-doc-harness/SKILL.md`.
5. Canonical owner and route: `.agents/skills/dev-doc-harness/references/artifact-style.md` and `.agents/skills/dev-doc-harness/SKILL.md`.
6. Template source, outputs, assembler, and validator: `assets/templates/blocks/spec.030.common.commitments-verification.md`, `assets/templates/{small-medium-work-item-spec,large-phased-work-item-spec}.md`, `scripts/assemble_templates.py`, and `scripts/test_harness_policy.py`.

## Commitment-Disposition Mapping

| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` Define ordinary modal language | implement | `TASK-001`, `TASK-002` |
| `SPEC-002` Prompt the intended artifact voice | implement | `TASK-001`, `TASK-003` |
| `SPEC-003` Protect the policy without rewriting history | implement | `TASK-001`, `TASK-004` |

## Verification-Execution Mapping

| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` Canonical guidance states and routes the rule | `CHECK-001`, `CHECK-003` | implementation, pre-commit |
| `VER-002` Generated specification templates preserve the prompt | `CHECK-001`, `CHECK-002`, `CHECK-003` | implementation, pre-commit |
| `VER-003` Validation distinguishes active policy from excluded material | `CHECK-001`, `CHECK-003`, `CHECK-004` | implementation, review, pre-commit |

## Change surfaces

1. `.agents/skills/dev-doc-harness/references/artifact-style.md`: add `rule:style.plain-language` and its compact canonical modal-language rule.
2. `.agents/skills/dev-doc-harness/SKILL.md`: require `module:artifact-style` for small/medium spec and plan drafting while retaining its existing large-spec route.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md`: add one concise commitment-statement prompt that names `must` and `should` and routes semantics to the canonical rule.
4. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md` and `large-phased-work-item-spec.md`: regenerated outputs only.
5. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: extend the existing artifact-style guidance assertion or add a focused companion assertion for the rule, router, prompt, generated outputs, active-path scan, and exclusions.
6. This work item: record testing guidance, review evidence, variance, implementation changelog, and required root changelog entries during execution.

Stable interfaces:

1. `module:artifact-style`, all existing style-rule identifiers, `schema:*` anchors, the assembler command-line interface, frozen artifact immutability, and the legal `LICENSE`.

Changed interfaces:

1. Small/medium planners now always load the artifact-style module.
2. Authors receive a visible modal-language cue at the Specification Commitment `Statement` field.
3. The current policy validator rejects unapproved active-surface instances of the prohibited modal.

## Model and Sub-agent Strategy

Model generation: `GPT-5.6` when exposed; otherwise `not exposed`.

Capability tier: `balanced`.

Reasoning effort: `medium`; use `high` only for the named post-diff reviewer or a documented policy-boundary conflict.

Orchestration mode: `single-agent` with one read-only post-diff reviewer.

Resolved profile: `not exposed`.

Availability/fallback: use the nearest available `balanced` configuration. If unavailable, `fast/economy` medium can perform mechanical assembly and validation; stop for confirmation before an unplanned capability-tier increase.

Execution continuity: `new task with curated-artifact handoff`.

Context visibility: `not exposed`.

Artifact rehydration required: `Yes`; read the frozen package, repository instructions, target current files, and the current validator before editing.

Fit assessment: one executor best preserves the small, coupled policy/template/validator boundary. A reviewer runs after validation to challenge scope and exception handling without concurrent file writes.

## Implementation tasks

### `TASK-001` Implementation Task — Add failing policy-boundary checks

Dependencies:

1. Frozen `SPEC-001` through `SPEC-003` and `snapshots/test-cases.snapshot.md`.

Files:

1. Modify: `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Implementation:

1. Extend `assert_artifact_style_guidance` or create a focused sibling assertion that requires `rule:style.plain-language`, the canonical `must`/`should` rule, and a mandatory `module:artifact-style` small/medium route.
2. Add a helper or focused fixture that scans only declared active authoring Markdown paths. Make the helper fail for a synthetic active-surface occurrence and pass for frozen work-item content, `LICENSE`, the canonical definition, and validator fixtures.
3. Require the shared source block and both generated specification templates to contain the compact prompt. Keep the check structural; do not infer prose quality or scan implementation evidence.
4. Run the validator before the policy and template edits and record the expected failure caused by the missing rule and route.

Exit criteria:

1. The added checks fail for the pre-change state with labels that identify missing canonical guidance, routing, prompt, or scan behavior.

### `TASK-002` Implementation Task — Add and route the canonical style rule

Dependencies:

1. `TASK-001`.

Files:

1. Modify: `.agents/skills/dev-doc-harness/references/artifact-style.md`.
2. Modify: `.agents/skills/dev-doc-harness/SKILL.md`.

Implementation:

1. Add `rule:style.plain-language` to the artifact-style owner table and a short section that defines `must` for binding obligations, `should` for guidance, and the prohibition plus its controlled definition-only exception.
2. Update the small/medium draft/review route so `module:artifact-style` is required with lifecycle, quality, and models. Do not copy the rule into lifecycle or quality guidance.
3. Preserve every existing style rule, routing outcome, and large-anchor behavior.

Exit criteria:

1. The style module is the only semantic owner, and an ordinary small/medium planner receives it as a mandatory input.

### `TASK-003` Implementation Task — Prompt authors and regenerate templates

Dependencies:

1. `TASK-002`.

Files:

1. Modify: `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md`.
2. Generated: `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`.
3. Generated: `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`.

Implementation:

1. Add one sentence immediately before the commitment examples that tells authors to use `must` for binding Statements and `should` for advisory prose, and points to `rule:style.plain-language` for the rule.
2. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` from the repository root.
3. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` to prove the two outputs are current.

Exit criteria:

1. Both generated templates mirror the source block exactly and the assembler reports no stale output.

### `TASK-004` Implementation Task — Validate, review, and record delivery evidence

Dependencies:

1. `TASK-002` and `TASK-003`.

Files:

1. Create: `docs/work-items/2026-07-14_plain-language-artifacts/deltas/testing-guide.delta.md`.
2. Create: `docs/work-items/2026-07-14_plain-language-artifacts/review/plain-language-policy-review.md`.
3. Create: `docs/work-items/2026-07-14_plain-language-artifacts/implementation-notes/variance-log.md`.
4. Create or modify: `docs/work-items/2026-07-14_plain-language-artifacts/changelog/implementation.md`.
5. Modify: `CHANGELOG.md`.

Implementation:

1. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and record the execution instance, full result, and evidence location for `CHECK-001` through `CHECK-003`.
2. Obtain the approved `review-001` review or perform the documented fallback; require severity, evidence, and a reproduction or validation path for every finding. Resolve blocking findings before commit.
3. Record the focused validator and assembler commands in the testing-guide delta, and record actual implementation variance or explicit `None` in the variance log.
4. Update the implementation source fragment and root changelog with the synchronized planned subject before committing. Confirm that excluded historical and legal files are absent from the diff.

Exit criteria:

1. All Plan Checks have evidence-backed results, no blocking review finding remains, required documentation exists, and the implementation diff is limited to the approved surfaces.

## Plan checks

### `CHECK-001` Plan Check — Run the full policy validator

Covers:

1. `VER-001`.
2. `VER-002`.
3. `VER-003`.

Procedure:

1. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after `TASK-003`.

Expected result:

1. Exit code `0`; output records passing artifact-style, template-assembly, current-policy, and historical-compatibility checks.

Evidence record:

1. `implementation-notes/variance-log.md` and the implementation completion report.

Stage or environment:

1. Implementation and pre-commit from the repository root.

### `CHECK-002` Plan Check — Verify generated-template freshness

Covers:

1. `VER-002`.

Procedure:

1. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` after the assembly write step.

Expected result:

1. Exit code `0` and output includes `All assembled templates are current.`

Evidence record:

1. `implementation-notes/variance-log.md` and the implementation completion report.

Stage or environment:

1. Implementation and pre-commit from the repository root.

### `CHECK-003` Plan Check — Inspect active-policy scope

Covers:

1. `VER-001`.
2. `VER-002`.
3. `VER-003`.

Procedure:

1. Run `rg -n -i '\\bshall\\b' AGENTS.md .agents/skills/dev-doc-harness` and compare every hit with the validator's controlled canonical-rule or fixture exception list.
2. Run `git diff --check` and inspect `git diff -- AGENTS.md LICENSE docs/work-items .agents/skills/dev-doc-harness CHANGELOG.md`.

Expected result:

1. The modal scan finds no unapproved active authoring occurrence; `git diff --check` exits `0`; and the diff leaves `LICENSE` and all pre-existing work items unchanged.

Evidence record:

1. `implementation-notes/variance-log.md`, review report, and implementation completion report.

Stage or environment:

1. Pre-commit review from the repository root.

### `CHECK-004` Plan Check — Perform independent policy-boundary review

Covers:

1. `VER-003`.

Procedure:

1. Give `review-001` the curated inputs from the spec strategy and ask it to challenge exception breadth, current-versus-historical boundaries, policy duplication, and generated-template drift.

Expected result:

1. The review report contains no unresolved blocking finding and each finding includes severity, evidence, and a reproduction or validation path.

Evidence record:

1. `review/plain-language-policy-review.md`.

Stage or environment:

1. Review after `CHECK-001` through `CHECK-003` and before the implementation commit.

## Planned commits

Planning approval commit:

1. Planned subject: `plan: plain-language-artifacts -- approve readable authoring policy`.
2. Changelog title or snippet: `2026-07-14_plain-language-artifacts -- approve readable authoring policy`.
3. Contents: this spec, this plan, both snapshots, planning source fragment, and the root changelog entry required by repository instructions.

Implementation commit:

1. Planned subject: `docs: plain-language-artifacts -- require ordinary modal wording`.
2. Changelog title or snippet: `2026-07-14_plain-language-artifacts -- require ordinary modal wording`.
3. Contents: current policy, routing, template source and regenerated outputs, validator, review and execution records, deltas, implementation fragment, and root changelog entry.

## Plan variance handling

1. Before freeze, edit this draft directly for operator feedback.
2. After freeze, record nontrivial variance in `implementation-notes/variance-log.md` and request an amendment for changed canonical ownership, validation scope, exception policy, template consumers, Specification Commitments, Verification Criteria, Plan Checks, or plan feasibility.

## Planning artifact freeze gate

1. Draft review status: operator approved the staged combined spec-and-plan package on 2026-07-14.
2. Approval commit status: created with the planned approval subject in this package.
3. Post-freeze implementation authorization: not granted; do not execute `TASK-001` through `TASK-004` until the package is approved, committed, and a fresh operator instruction authorizes implementation.

## Next-task handoff

1. Planning shape: `combined small/medium`.
2. Frozen package: `spec_plain-language-artifacts.md`, this plan, `snapshots/architecture.snapshot.md`, `snapshots/test-cases.snapshot.md`, and the approval fragment created at freeze.
3. Next activity: implement `TASK-001` through `TASK-004` in order, starting with the focused failing validator check.
4. Execution continuity: `new task with curated-artifact handoff`.
5. Approved strategy and fallback: balanced medium single-agent execution with the named post-diff reviewer and fallback in the Model and Sub-agent Strategy.
6. Variance stop condition: stop for approval-required variance if the owner, routing, validation boundary, controlled exception, changed template set, scope, Specification Commitment, Verification Criterion, Plan Check, or plan feasibility changes.

## Plan readiness checklist

- [x] Inputs, change surfaces, and stable interfaces are explicit.
- [x] Each Specification Commitment has an authorized disposition and each Verification Criterion has Plan Check coverage.
- [x] Tasks identify concrete files, dependencies, implementation boundaries, and exit criteria.
- [x] Plan Checks include procedure, result, evidence record, and stage.
- [x] Planning and implementation subjects match their changelog snippets.
- [x] The model and reviewer strategy follows the active repository policy.
- [x] Historical and legal exclusions are explicit.
- [x] No unresolved required decisions, ownerless deferrals, or authoring placeholders remain.

## Approval

- Status: Approved
- Superseded by: None
