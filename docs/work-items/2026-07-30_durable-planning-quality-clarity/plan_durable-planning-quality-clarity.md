# Durable Planning Quality Clarity Plan

Work ID: `2026-07-30_durable-planning-quality-clarity`
Short ID: `durable-planning-quality-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`
Execution method: `superpowers:executing-plans`
Current planning Codex task: Model/profile, reasoning, and context visibility: `not exposed`.

## Input artifacts

1. Draft spec: `spec_durable-planning-quality-clarity.md`.
2. Target policy: `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`.
3. Lifecycle boundary: `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
4. Module ownership catalog: `.agents/skills/dev-doc-harness/references/policy-architecture.md`.
5. Source blocks and generated plan/spec templates under `.agents/skills/dev-doc-harness/assets/templates/`.
6. Validation entry point: `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
7. Template assembler: `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`.
8. Unresolved implementation context: None. The implementation must preserve the user's existing line-break cleanup in the target reference.

## Traceability approach

Local links are sufficient because four commitments map to four ordered tasks and four focused checks. No mapping table is needed; this is a routine, single-package policy change.

Related links:

1. `SPEC-001` → `TASK-001`, `TASK-002`, `CHECK-001`.
2. `SPEC-002` → `TASK-001`, `CHECK-002`.
3. `SPEC-003` → `TASK-002`, `TASK-003`, `CHECK-003`.
4. `SPEC-004` → `TASK-001`, `CHECK-004`.

## Change surfaces

1. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`: canonical quality policy.
2. `.agents/skills/dev-doc-harness/references/policy-architecture.md`: module catalog wording if its quality summary remains phase-only.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md`: concise commitment/criterion prompt if needed to reflect the approved evidence chain.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md`: ordinary-plan input and architecture-consumption cue.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.phase.header-objective-inputs.md` and `plan.030.phase.fresh-thread-readiness.md`: phase-only input and one-orchestration-thread quality cue.
6. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.020.common.traceability-approach-surfaces.md` and `plan.050.common.task-plan.md`: local-link and Plan Check evidence-record prompts.
7. Generated templates assembled from those blocks: small/medium spec and plan, large/phased spec and phase plan as affected by the changed manifests.
8. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: focused policy assertions and legacy fixture behavior.
9. `docs/work-items/2026-07-30_durable-planning-quality-clarity/deltas/testing-guide.delta.md`: implementation-time validation guidance.

## Implementation approach

First make the canonical quality owner internally coherent. Then update only the reusable source blocks that render affected policy into durable artifacts; regenerate instead of hand-editing outputs. Finally, replace stale mandatory-mapping fixture expectations with narrow structural checks for the approved evidence chain, and validate the complete current harness surface.

## Model and sub-agent strategy

Model policy: active repository `economy-default`.

Upcoming-stage assessment:

1. Execution method: `superpowers:executing-plans`; the target policy, shared source blocks, generated outputs, and validator need ordered integration rather than parallel write ownership.
2. Sub-agents: no delegated writer. A delegated writer would overlap the same policy and shared template blocks; the coordination cost exceeds the value.
3. Reviewer capability: the operator approved one read-only independent reviewer after deterministic validation. It must use the curated artifacts and requirements-traceability/policy-ownership lens recorded below.
4. Baseline execution selection: balanced capability tier, medium reasoning effort, model generation and resolved profile `not exposed`; use the nearest available policy-compliant profile.
5. Continuity: `same Codex task`, selected by the operator at approval. Rehydrate the frozen package and current sources before `TASK-001`; the active discussion and staged baseline provide the concrete continuity benefit.
6. Fallback: if the documented Superpowers method is unavailable, use the native execution flow with the same task order and every Plan Check. If the approved reviewer allocation is unavailable, do not silently downgrade it; report the availability blocker and request operator direction.
7. Final integration: the execution Codex task owns all writes, validation, variance judgment, and the user-facing completion report.

Sub-agent `review-001`:

1. Purpose: independently review the completed policy/template/validator diff for requirements traceability, ownership leakage into lifecycle, accidental mandatory-mapping restoration, and loss of the approved open-question or handoff rules.
2. Context strategy: `curated artifacts`.
3. Input context: frozen spec and plan, changed diff, completed validation output, revised quality reference, relevant lifecycle and policy-architecture references, changed source blocks, and generated templates.
4. Output artifact: evidence-backed review findings with severity, inspected paths, validation/reproduction path, residual risk, and recommended next step.
5. Model policy: operator override within the active `economy-default` policy; the operator explicitly requires Sol High for this reviewer.
6. Model generation: `GPT-5.6`; capability tier: `Sol`; resolved profile: `gpt-5.6-sol` when exposed; reasoning effort: `high`.
7. Selection reason: the reviewer judges cross-document policy ownership and evidence semantics after implementation; a high-reasoning independent read avoids an author reviewing its own interpretation as the only authority.
8. Write authority: none. Parallel execution: no; it runs after `TASK-004` validation and before the implementation commit.
9. Blast radius if wrong: medium; faulty advice can preserve ambiguous harness policy, while the execution Codex task retains final integration ownership.

## Implementation tasks

### `TASK-001` Clarify the canonical quality policy

Dependencies: approved frozen package and rehydrated target/lifecycle/module-ownership references.

Interfaces:

1. Consumes: `SPEC-001`, `SPEC-002`, `SPEC-004`, the operator's review decisions, and existing user line-break cleanup.
2. Produces: a quality reference with a consistent applicability statement, general plan quality bar, additional phase-plan boundary, precise plain-language/open-question wording, economical handoff rule, and lifecycle links for non-quality mechanics.

Implementation:

1. Replace the tautological applicability exception and non-actionable durable-planning motivation with direct artifact scope.
2. Correct the modal-language sentence to prohibit legalistic authority language and legalistic modal phrasing, not ordinary normative language.
3. Rephrase final-artifact/open-question guidance around questions material to the documented next activity, reasonable checking, and recorded later-stage ownership.
4. Remove the unqualified duplicate rejected-alternatives phrase from the spec-quality list.
5. Add a general plan-quality section and narrow the phase section to its additional independent-phase requirement.
6. Move or rewrite architecture-consumption and post-freeze references so quality states the plan constraint while lifecycle remains the owner of snapshot, variance, and amendment mechanics.
7. Rewrite handoff preservation to compare drafts against material operator-provided sources and establish the approved artifacts as the future source of truth.

Exit criteria: the reference has one clear owner per concern, does not require hidden chat context after freeze, and preserves the user's approved policy decisions.

### `TASK-002` Align reusable authoring templates

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: approved canonical quality wording, source-block manifests, and the assembler contract.
2. Produces: source blocks and regenerated templates that prompt for the same general-plan, phase-plan, local-link, and evidence-record model as the canonical reference.

Implementation:

1. Update source blocks rather than generated files directly.
2. Keep the ordinary plan self-contained for its declared inputs; keep the phase template's stronger one-orchestration-thread, bounded-delegation requirement.
3. Add or clarify the concise `CHECK` evidence-record prompt without recreating mandatory mapping tables or a separate approval gate.
4. Regenerate all affected templates with `assemble_templates.py --write` only after source-block edits are complete.
5. Update the module-catalog quality summary if it still incorrectly implies that only phase plans have a quality bar.

Exit criteria: source blocks, assembly manifests, and generated templates present a consistent minimal evidence chain and `assemble_templates.py --check` reports current outputs.

### `TASK-003` Replace stale validator expectations with focused coverage

Dependencies: `TASK-001`, `TASK-002`.

Interfaces:

1. Consumes: revised canonical wording and generated-template shapes.
2. Produces: deterministic regression coverage for scope, legalistic modal wording, general-versus-phase plan quality, local evidence links, evidence records, and the absence of mandatory mapping tables.

Implementation:

1. Identify fixtures or assertions left from the former mandatory commitment-verification model, especially requirements for complete mapping tables or obsolete Plan Check fields.
2. Retain checks that validate stable IDs, criterion coverage, expected evidence, source-block generation, and phase-plan routing.
3. Add narrow positive and negative fixtures for the approved local-link model: a criterion linked to a check with a method, expected result, and evidence record passes; missing criterion coverage or evidence record fails; a full mapping table is not required.
4. Avoid semantic parsing of policy prose beyond high-signal structural assertions.

Exit criteria: the validator protects the approved model without enforcing discarded matrix mechanics.

### `TASK-004` Validate, review, and record implementation guidance

Dependencies: `TASK-001`, `TASK-002`, `TASK-003`.

Interfaces:

1. Consumes: completed policy, source blocks, generated templates, validator changes, and the frozen package.
2. Produces: validation evidence, testing-guide delta, implementation changelog fragment, and a self-review or authorized independent-review result.

Implementation:

1. Run the Plan Checks below and inspect the full diff for unrelated paths, duplicate ownership, stale mandatory-mapping requirements, and overwritten user changes.
2. Create `deltas/testing-guide.delta.md` with the supported assembler and validator commands plus the evidence-record expectation.
3. Create the implementation changelog fragment before the implementation commit, with a heading synchronized to the planned subject.
4. Perform focused self-review on requirements traceability and policy ownership. If the operator authorizes the proposed reviewer at execution start, supply that reviewer the frozen package, changed diff, validation output, and this exact lens instead.

Exit criteria: every check passes, only intended current policy/template/validator/work-item paths change, and the final evidence says whether independent review ran.

## Plan checks

### `CHECK-001` Verify planning-shape coverage

Covers: `VER-001`.

Method: Inspect `durable-planning-quality.md`, `policy-architecture.md`, both plan source blocks, and generated plan templates for general plan coverage and the phase-only one-orchestration-thread boundary.

Expected result: Ordinary plans and phase plans each have clear, compatible quality requirements; no phase-specific statement is incorrectly presented as the entire plan quality bar.

Evidence record: Full-diff review notes and relevant focused validator assertions.

### `CHECK-002` Verify plain-language and open-question rules

Covers: `VER-002`.

Method: Search the quality reference for the modal convention, legalistic-language prohibition, material-next-activity resolution threshold, and rejected-alternatives ownership.

Expected result: The policy permits `must` and `should`, prohibits only legalistic phrasing, preserves material question resolution, and has no unqualified duplicate alternative requirement.

Evidence record: Focused textual assertion output and self-review notes.

### `CHECK-003` Verify evidence-chain schema and validator behavior

Covers: `VER-003`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` and `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`; inspect their affected fixtures.

Expected result: Generated templates are current, the full harness validator exits `0`, local criterion-to-check links and evidence records are protected, and mandatory mapping tables are not required.

Evidence record: Command output in the completion report and any focused test additions.

### `CHECK-004` Verify durable handoff preservation

Covers: `VER-004`.

Method: Review the final quality reference and templates against the frozen spec, operator decisions, and relevant lifecycle rules.

Expected result: Material initial source details are incorporated into the durable artifacts; fresh executors are not asked to reconstruct chat context; lifecycle remains the owner of freeze, variance, and snapshots.

Evidence record: Requirements-traceability self-review or authorized reviewer findings.

### `CHECK-005` Verify repository hygiene

Covers: `VER-001`, `VER-002`, `VER-003`, `VER-004`.

Method: Run `git diff --check`, inspect `git diff --stat` and `git diff --name-only`, and review the complete diff before commit.

Expected result: No whitespace errors, unrelated paths, accidental frozen-history edits, or loss of the user's pre-existing line-break cleanup.

Evidence record: Final validation summary.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: durable-planning-quality-clarity -- approve clearer plan quality` |
| Implementation | `docs: durable-planning-quality-clarity -- clarify plans and conformance` |

## Validation and variance

Use `rule:lifecycle.variance-policy` for noteworthy allowed drift. Stop for approval before changing entity semantics beyond this spec, reintroducing mandatory mappings, changing lifecycle/freeze/model ownership, changing generated-template assembly architecture, or broadening the work beyond current policy/templates/validator/documentation.

## Implementation handoff

### Approved next stage

#### Activity

Next activity: implement the approved quality-policy clarification; First Plan Task: `TASK-001`.

#### Orchestration

Method: `superpowers:executing-plans`; Run in: `same Codex task`; Plan Task reviewers: `review-001` runs after deterministic validation with the approved curated-artifact requirements-traceability and policy-ownership lens.

#### Model

Model: active repository `economy-default`, nearest available balanced profile for execution; reviewer `review-001`: `gpt-5.6-sol` at `high` reasoning by explicit operator direction.

#### Fallbacks and limits

1. Frozen package: this plan and `spec_durable-planning-quality-clarity.md`; no supporting snapshots are required.
2. Artifact rehydration: in this same task, reread the frozen package, target policy, lifecycle and ownership references, relevant source blocks, generated templates, and validator before editing.
3. Variance stop condition: stop for a material change to evidence semantics, lifecycle ownership, freeze behavior, template assembly, or package scope.

## Readiness

- [x] Inputs, scope, tasks, checks, documentation, and changelog ownership are clear.
- [x] The plan applies the approved economical evidence model without mandatory matrices.
- [x] The operator-selected same-task route, Sol High independent reviewer, fallback, and final integration owner are explicit.
- [x] No required decision or ownerless deferral remains.

## Approval

- Status: Approved
- Superseded by: None
