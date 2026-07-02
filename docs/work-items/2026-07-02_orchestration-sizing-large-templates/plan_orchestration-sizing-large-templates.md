# Orchestration Sizing And Large Template Alignment Plan

Work ID: `2026-07-02_orchestration-sizing-large-templates`
Short ID: `orchestration-sizing-large-templates`
Status: Approved
Harness release: `0.4+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Input Artifacts

Read these before finalizing implementation planning:

- Approved spec: `spec_orchestration-sizing-large-templates.md`
- Required snapshots or deltas: None.
- Relevant repository files, tests, docs, logs, or review comments:
  - `.agents/skills/dev-doc-harness/references/artifact-contract.md`
  - `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
  - `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
  - `.agents/skills/dev-doc-harness/references/policy-architecture.md`
  - `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
  - `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
  - `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
  - `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
  - `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
  - `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
  - `README.md`
  - `CHANGELOG.md`
  - `docs/work-items/2026-07-01_small-medium-template-structure/handoff/research-verification.md`
  - `docs/work-items/2026-07-01_small-medium-plan-template-structure/spec_small-medium-plan-template-structure.md`
  - `https://github.com/itxyzzz/gen-ai-se-hw/blob/main/homework-3/TASKS.md`
  - `https://github.com/itxyzzz/gen-ai-se-hw/blob/main/homework-3/specification.md`
  - `https://raw.githubusercontent.com/github/spec-kit/main/spec-driven.md`
  - `https://scrumguides.org/scrum-guide.html`
- Unresolved implementation context to confirm before editing: None identified.

## Spec Traceability

Map the approved spec to execution without restating the spec.

Requirement coverage:

- `REQ-001`: implemented by `T-001`; verified by `V-001`, `V-006`, and `AC-001`.
- `REQ-002`: implemented by `T-001` and `T-002`; verified by `V-006` and `AC-002`.
- `REQ-003`: implemented by `T-003`; verified by `V-002` and `AC-003`.
- `REQ-004`: implemented by `T-004`; verified by `V-003` and `AC-004`.
- `REQ-005`: implemented by `T-005`; verified by `V-004`, `V-006`, and `AC-005`.
- `REQ-006`: implemented by `T-006`; verified by `V-004`, `V-006`, and `AC-006`.
- `REQ-007`: handled by `T-001`, `T-002`, `T-005`, `T-006`, and `T-008`; verified by `V-006` and `AC-007`.
- `REQ-008`: handled by `T-007`, `T-008`, and `T-009`; verified by `V-006`, `V-007`, and `AC-008` through `AC-009`.

Acceptance coverage:

- `AC-001`: `T-001`, `V-001`.
- `AC-002`: `T-001`, `T-002`, `V-006`.
- `AC-003`: `T-003`, `V-002`.
- `AC-004`: `T-004`, `V-003`.
- `AC-005`: `T-005`, `V-004`.
- `AC-006`: `T-006`, `V-004`.
- `AC-007`: `T-005`, `T-006`, `T-008`, `V-006`.
- `AC-008`: `T-008`, `V-006`, `V-007`.
- `AC-009`: `T-007`, `T-009`, `V-005`.

Risk and boundary coverage:

- `RISK-001`: `T-001` keeps risk/breadth escalation indicators alongside the orchestration-thread criterion.
- `RISK-002`: `T-002`, `T-005`, `T-006`, and `V-006` keep reusable policy in canonical references.
- `RISK-003`: `T-005` and `T-006` use concise prompts and readiness checks instead of long policy prose.
- `RISK-004`: `T-003` phrases Scrum as an analogy only.
- `RISK-005`: `T-005` and `T-006` borrow layered objective shape only.
- `RISK-006`: `T-008` and `V-006` cover validator evidence updates.

## Implementation Approach

Make the lifecycle sizing rule the source of truth. In `artifact-contract.md`, rewrite `## Work sizes` so small/medium work is primarily defined by safe coordination in one orchestration thread with bounded delegation. Keep examples of small/medium work and escalation signals, and explicitly route sub-agent mechanics to `subagent-model-policy.md`.

Keep `subagent-model-policy.md` focused on orchestration mechanics. If it needs a clarification, add only a compact sentence that lifecycle sizing may refer to its context strategy, concurrency, and final integration ownership rules.

Align templates in two passes. First, update small/medium wording so it no longer says one implementation thread. Second, reshape the large/phased spec and phase-plan templates to follow the improved small/medium information architecture while adding only the anchor-specific and phase-specific prompts that the complex orchestration pattern needs.

Use the requested homework examples for layered decomposition only: high-level objective, mid-level objectives, cross-cutting policy/nonfunctional expectations, implementation notes, beginning/ending context, and detailed tasks with acceptance and verification. In harness terms, those become anchor-level objectives and phase objectives, not a copied homework schema.

## Change Surfaces

Expected edits:

- `.agents/skills/dev-doc-harness/references/artifact-contract.md`: rewrite `## Work sizes` and make any necessary follow-on wording for phase-plan fit use orchestration-thread terminology.
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: optional narrow clarification that lifecycle sizing defers sub-agent strategy and final integration mechanics here.
- `README.md`: add operator-facing sizing explanation and Scrum analogy.
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`: replace one-implementation-thread prompts with one-orchestration-thread and bounded-delegation prompts.
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`: review and make only minor consistency edits if lifecycle wording changes require them.
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`: restructure as updated large anchor spec template.
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`: restructure as updated phase-plan template.
- `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: update golden traversal evidence only if existing patterns no longer match intentional wording.
- `CHANGELOG.md`: newest-first implementation entry before commit.

Stable interfaces:

- `rule:lifecycle.large-phase-orchestration`: no semantic change to the large/phased planning sequence.
- `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`: no semantic change expected.
- `schema:spec.small-medium`, `schema:plan.small-medium`, `schema:spec.large-phased`, and `schema:plan.phase`: schema IDs remain the same.

Changed interfaces:

- `rule:lifecycle.work-sizing`: clarified semantics, same rule ID.
- Large/phased template section shapes: current artifact schema prompts become more detailed and aligned with small/medium templates.

Implementation boundaries:

- Root `AGENTS.md` stays unchanged because active policy selection is not part of this work.
- `.agents/skills/dev-doc-harness/VERSION` stays unchanged because release identity is not part of this work.
- Frozen historical work-item artifacts stay unchanged because they are snapshots.
- No new docs/superpowers mirror files are created because the harness work-item folder is the canonical planning location.

## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this work item.

Current orchestration:

- Model/profile and reasoning effort if known: Codex desktop thread; exact model/profile not exposed in repository artifacts.

Fit assessment:

- Complexity: Medium. The work spans lifecycle policy, README, four templates, validation evidence, and changelog, but it is one coherent harness semantics update.
- Risk and blast radius: Medium. It changes current harness guidance and templates, but no runtime code or release identity.
- Ambiguity: Low to medium. The operator has approved the core approach; careful wording is still needed to avoid policy duplication.
- Budget and latency fit: Acceptable for one orchestration thread with one optional review sub-agent if available.

Recommended orchestration change:

- Use the operator-selected `enterprise-default` policy for this template-improvement sequence unless the operator changes it before implementation.

Sub-agents:

- Bounded strategy below. If sub-agent tooling is unavailable, the orchestration thread must perform the same review steps and report `Sub-agents: None used` with the fallback reason.

Sub-agent `template-policy-review`:

- Purpose: Read-only review of the implemented lifecycle/template diff for policy duplication, small/medium versus large/phased consistency, and missing required strategy fields.
- Context strategy: `curated prompt`.
- Input context: Approved spec and plan, changed diff, `artifact-contract.md`, `subagent-model-policy.md`, small/medium templates, large/phased templates, and validator output.
- Output artifact: Review findings summarized in the implementation completion report or variance log if material.
- Model policy: `enterprise-default` for this sequence unless changed by operator.
- Model class/profile: policy-relative standard or latest strongest if the diff creates subtle lifecycle conflicts.
- Reasoning effort: Medium; high if validator or review reveals conflicting lifecycle guidance.
- Selection reason: Independent read-only review reduces the risk of duplicated policy prose and inconsistent template semantics.
- Parallel execution: No; run after the implementation diff exists and before final commit.
- Blast radius if wrong: Medium; missed inconsistency could ship confusing harness guidance.

## Task Plan

- [ ] `T-001` Dependencies: Approved planning package; update `.agents/skills/dev-doc-harness/references/artifact-contract.md` `## Work sizes` so small/medium means one orchestration thread with bounded delegation and large/phased means anchor/phase planning is needed because that criterion fails or staged review materially reduces risk; Traces: `REQ-001`, `REQ-002`, `RISK-001`.
- [ ] `T-002` Dependencies: `T-001`; review `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` and add only a narrow deferral/clarification if lifecycle wording needs it; Traces: `REQ-002`, `REQ-007`, `RISK-002`.
- [ ] `T-003` Dependencies: `T-001`; update `README.md` operator-facing explanation of small/medium and large/phased work, including the Scrum Guide analogy as an analogy only; Traces: `REQ-003`, `RISK-004`.
- [ ] `T-004` Dependencies: `T-001`; update `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md` and review `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` for remaining one-implementation-thread wording or inconsistent small/medium fit checks; Traces: `REQ-004`.
- [ ] `T-005` Dependencies: `T-001`, `T-004`; update `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md` to align with the updated spec structure and add anchor-specific sections for why large/phased, layered objectives, phase decomposition, and anchor readiness; Traces: `REQ-005`, `REQ-007`, `RISK-003`, `RISK-005`.
- [ ] `T-006` Dependencies: `T-005`; update `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md` to align with the updated plan structure and add phase-specific sections for input artifacts, spec traceability, dependencies, validation expected signals, fresh-thread readiness, and handoff; Traces: `REQ-006`, `REQ-007`, `RISK-003`, `RISK-005`.
- [ ] `T-007` Dependencies: `T-001` through `T-006`; update `CHANGELOG.md` with `2026-07-02_orchestration-sizing-large-templates -- align sizing and phased templates`; Traces: `REQ-008`, `AC-009`.
- [ ] `T-008` Dependencies: `T-001` through `T-007`; run targeted searches and the harness validator, then update `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` only if intentional wording changes require current-surface evidence updates; Traces: `REQ-007`, `REQ-008`, `RISK-006`.
- [ ] `T-009` Dependencies: `T-008`; perform final diff review, optional `template-policy-review` sub-agent review if tooling is available, `git diff --check`, staged check, and commit with the approved implementation subject; Traces: `REQ-008`.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets. Update this table before committing if implementation changes the subject wording.

Planning approval commit:

- Planned subject: `spike: orchestration-sizing-large-templates -- approve sizing and large-template plan`
- Changelog title or snippet: `2026-07-02_orchestration-sizing-large-templates -- approve sizing and large-template plan`
- Notes: Approval commit for `spec_orchestration-sizing-large-templates.md`, `plan_orchestration-sizing-large-templates.md`, and `CHANGELOG.md`.

Implementation commit:

- Planned subject: `docs: orchestration-sizing-large-templates -- align sizing and phased templates`
- Changelog title or snippet: `2026-07-02_orchestration-sizing-large-templates -- align sizing and phased templates`
- Notes: Implementation commit for lifecycle, README, template, validator-if-needed, and changelog updates.

## Validation Plan

| Command | Expected result |
|---|---|
| `rg -n "one implementation thread" .agents/skills/dev-doc-harness/references .agents/skills/dev-doc-harness/assets/templates README.md` | No matches in current policy, README, or current templates; covers `AC-004`. |
| `rg -n "one orchestration thread|bounded delegation|large/phased" .agents/skills/dev-doc-harness/references/artifact-contract.md .agents/skills/dev-doc-harness/assets/templates README.md` | Matches show lifecycle owns core sizing and templates/README cite or apply it consistently; covers `AC-001` through `AC-004`. |
| `rg -n "Source and Intent|Requirements|Acceptance Criteria|Spec readiness checklist|Phase decomposition" .agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md` | All expected large anchor spec sections are present; covers `AC-005`. |
| `rg -n "Input Artifacts|Spec Traceability|Dependencies:|Validation Plan|Plan readiness checklist|Handoff output" .agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md` | All expected phase-plan sections or task labels are present; covers `AC-006`. |
| `rg -n "Scrum Guide|analogy" README.md` | README contains a brief analogy and does not imply Scrum is adopted as harness policy; covers `AC-003`. |
| `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | All checks print `PASS` and the command exits 0; covers `AC-002`, `AC-007`, and `AC-008`. |
| `git diff --check` | No whitespace errors; CRLF warnings are acceptable if they match current repo behavior. |
| `git status --short` | Before implementation commit, only approved implementation targets and `CHANGELOG.md` are modified. |

Every validation entry states the expected signal before implementation starts. Include command exit behavior, important output text, manual observation, review criterion, or operator acceptance condition as applicable.

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

Likely local variance that may proceed with a note in the completion report:

- Validator evidence updates are needed because intentional wording changed.
- `subagent-model-policy.md` needs no edit after lifecycle wording is clear enough.
- Minor section title changes improve readability while preserving required sections.

Variance requiring operator approval before continuing:

- Changing the large/phased lifecycle sequence.
- Changing model/sub-agent authorization semantics or concurrency caps.
- Removing required small/medium or large/phased template surfaces.
- Introducing new artifact files or schemas beyond this approved scope.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this plan.

Draft review status: Approved by operator on 2026-07-02.
Approval commit status: Approved for freeze; commit hash will be reported in the checkpoint output.
Post-freeze implementation authorization status: Not authorized; implementation requires a fresh explicit operator instruction after the approval commit.

## Plan readiness checklist

- [x] Input artifacts and relevant repository context have been read and listed.
- [x] Every spec requirement and acceptance criterion has at least one task and one validation path.
- [x] Risks, scope boundaries, interfaces, and documentation decisions are either covered by tasks or explicitly marked as no-op with a reason.
- [x] Task detail is sufficient for a fresh implementation agent or delegated sub-agent to execute its assigned part without inventing task order, file scope, validation, or documentation steps.
- [x] Validation entries have exact commands, manual checks, review findings, or operator acceptance paths with expected signals.
- [x] Planned commits and changelog title snippets are synchronized.
- [x] Variance handling is clear for likely implementation drift.
- [x] The work still fits one orchestration thread with a bounded sub-agent strategy. If it does not, split, re-scope, or escalate to large/phased handling before freeze.
- [x] Sub-agent strategy follows `module:models`, or `Sub-agents: None` has a brief fit rationale.
- [x] No unresolved placeholders remain before approval or handoff.

## Completion criteria

- Acceptance criteria in `spec_orchestration-sizing-large-templates.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- The frozen plan had enough detail for each assigned execution part or delegated sub-agent to proceed safely.
- Execution remained within one orchestration thread with a bounded sub-agent strategy; otherwise the work was split, re-scoped, or escalated before implementation.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
