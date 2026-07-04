# Small/Medium Plan Template Update Plan

Work ID: `2026-07-01_small-medium-plan-template-structure`
Short ID: `small-medium-plan-template-structure`
Status: Approved
Harness release: `0.4+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Implementation summary

Update the small/medium plan template as a follow-on to the spec-template structure work. The revised plan template should make the plan a bridge from approved spec to execution: it should identify input artifacts, map requirements and acceptance criteria to tasks and validation, describe file/interface change surfaces, preserve model/sub-agent strategy, and add readiness checks that catch missing execution detail or orchestration saturation.

Keep reusable lifecycle, freeze-gate, naming, and model-policy rules in their canonical references. The plan template should own artifact shape and prompts, not long policy restatements. The implementation should avoid changing the spec template or large/phased templates.

## Files and interfaces

Input artifacts:

- `docs/work-items/2026-07-01_small-medium-plan-template-structure/spec_small-medium-plan-template-structure.md`
- `docs/work-items/2026-07-01_small-medium-plan-template-structure/plan_small-medium-plan-template-structure.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`

Expected implementation edits:

- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `CHANGELOG.md`

Possible implementation edit only if validation requires it:

- `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`

Possible implementation edit only if implementation review shows the current model-policy wording is ambiguous for small/medium plans:

- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`

Interfaces expected to remain stable:

- Harness release identity.
- Small/medium spec template structure.
- Large/phased template structure.
- Work-item lifecycle and freeze-gate sequence.
- Naming and commit-message policy.
- Model/sub-agent policy semantics.

## Model and Sub-agent Strategy

Current orchestration: Codex desktop, model/reasoning profile not explicitly exposed.

Fit assessment:

- Complexity: low-to-medium.
- Risk: low runtime risk, moderate template-quality risk.
- Ambiguity: low after the follow-up discussion and approved spec-template baseline.
- Blast radius: limited to future small/medium plan authoring.
- Policy selection: operator selected `enterprise-default` for this template-improvement sequence; no sub-agents are needed for this narrow edit.
- Latency and budget: direct main-thread implementation is appropriate.

Recommended change:

- None.

Sub-agents:

- None. The implementation touches one template and one changelog entry, and the main thread can do final integration and validation more simply than coordinating delegation.

## Tasks

- [ ] Confirm the working tree before implementation and avoid staging unrelated changes.
- [ ] Read the approved spec, this approved plan, the current small/medium plan template, and the updated small/medium spec template before editing.
- [ ] Update `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` metadata only where needed, preserving `Work ID`, `Short ID`, `Status`, `Harness release`, `Schema`, and `Policy references`.
- [ ] Add an input-artifacts or spec-traceability section that tells authors to ground the plan in the approved spec, required snapshots/deltas, relevant repository files, and unresolved implementation context.
- [ ] Revise `Implementation summary` so it describes the implementation approach without restating the spec.
- [ ] Replace or expand `Files and interfaces` with prompts for expected edits, stable interfaces, changed interfaces, and implementation boundaries.
- [ ] Add a readable traceability prompt that maps spec requirements and acceptance criteria to implementation tasks and validation methods without using a wide long-content table.
- [ ] Revise `Tasks` guidance so tasks are SMART, dependency-aware, and executable by a fresh agent, while warning against forced vertical slicing when shared setup, tests, or refactors should happen first.
- [ ] Revise `Validation commands` so every command or manual check has an expected signal and traces to acceptance criteria or risk coverage.
- [ ] Revise `Model and Sub-agent Strategy` to reference `module:models` and preserve required policy fields in bullets or card-style blocks rather than a wide table with long cells.
- [ ] Make the `Model and Sub-agent Strategy` prompts explicitly support bounded sub-agent use for review, parallel exploration, and specialized tasks when justified by the canonical policy.
- [ ] Add a `Plan readiness checklist` before approval that checks spec coverage, sufficient execution detail, validation mapping, documentation/changelog coverage, variance handling, orchestration-thread fit, and bounded sub-agent strategy.
- [ ] Update `Completion criteria` with explicit checks that the plan had sufficient detail for each assigned execution part and did not exceed one orchestration thread; if it did, the work was split, re-scoped, or escalated before implementation.
- [ ] Preserve `Planned commits`, `Plan variance handling`, `Planning artifact freeze gate`, `Completion criteria`, and `Approval` sections.
- [ ] Avoid changing the small/medium spec template, large/phased templates, unrelated canonical references, or release marker unless validation shows a directly caused defect.
- [ ] Clarify `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` only if needed to make small/medium plan applicability clear, without changing the policy semantics or duplicating that guidance in the template.
- [ ] Update `CHANGELOG.md` before the implementation commit with the approved implementation title snippet.
- [ ] Run validation commands and inspect the diff for scope creep.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spike: small-medium-plan-template-structure -- approve plan-template update plan` | `2026-07-01_small-medium-plan-template-structure -- approve plan-template update plan` | Approval commit for this spec and plan. |
| Implementation | `docs: small-medium-plan-template-structure -- improve plan-template scaffolding` | `2026-07-01_small-medium-plan-template-structure -- improve plan-template scaffolding` | Implementation commit for the small/medium plan template update and changelog entry. |

## Validation commands

| Command | Expected result |
|---|---|
| `git status --short` | Shows only approved planning artifacts staged during freeze, then implementation edits limited to `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`, `CHANGELOG.md`, and any directly required validator or model-policy clarification. |
| `rg -n "NEEDS CLARIFICATIO[N]|TB[D]" docs/work-items/2026-07-01_small-medium-plan-template-structure` | No unresolved planning placeholders. |
| `rg -n "TO[D]O" docs/work-items/2026-07-01_small-medium-plan-template-structure/spec_small-medium-plan-template-structure.md docs/work-items/2026-07-01_small-medium-plan-template-structure/plan_small-medium-plan-template-structure.md` | No unresolved planning placeholders. |
| `rg -n "## Input Artifacts|## Spec Traceability|## Implementation Approach|## Change Surfaces|## Task Plan|## Validation Plan|## Plan readiness checklist" .agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` | Expected revised headings are present after implementation; adapt exact heading names only if the final template wording is clearer and the diff review confirms equivalent coverage. |
| `rg -n "\\|.*\\|.*\\|.*\\|" .agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` | After implementation, remaining wide tables are limited to short-cell harness metadata tables such as planned commits or validation commands; no model/sub-agent long-cell table remains. |
| `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | All checks print `PASS ...` and the process exits with status 0, or the completion report names the exact blocker. |

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Draft review status: Approved by operator on 2026-07-02.
Approval commit status: Approved for freeze; commit hash will be reported in the checkpoint output.
Post-freeze implementation authorization status: Not authorized; implementation requires a fresh explicit operator instruction after the approval commit.

## Completion criteria

- Acceptance criteria in `spec_small-medium-plan-template-structure.md` are met.
- Required validation commands have been run and recorded.
- The implementation changes only approved files, or any variance is recorded before commit.
- The revised plan template gives a fresh implementation agent or delegated sub-agent enough concrete detail to execute its assigned part without inventing missing task order, file scope, validation, or documentation steps.
- The revised plan template includes a guard that small/medium execution still fits one orchestration thread with a bounded sub-agent strategy; otherwise the plan tells agents to split, re-scope, or escalate to large/phased handling before implementation.
- `CHANGELOG.md` has a newest-first entry before the implementation commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Spec-template and large/phased template changes remain out of scope.
- De-facto sub-agent use is reported when applicable.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
