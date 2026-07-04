# Small/Medium Spec Template Update Plan

Work ID: `2026-07-01_small-medium-template-structure`
Short ID: `small-medium-template-structure`
Status: Approved
Harness release: `0.4+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:evidence`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Implementation summary

Update the small/medium spec template as a focused documentation-template change. Keep the lifecycle, naming, model/sub-agent, and freeze-gate policies in their canonical references; the template should own artifact shape and prompts only.

The implementation should use the research report as evidence, then rewrite only the small/medium spec template body so future filled specs capture source intent, scope boundaries, repository evidence, requirements, acceptance criteria, interfaces/data/control flow, risks, rejected alternatives, and readiness checks. Plan-template changes remain deferred.

## Files and interfaces

Input artifacts:

- `docs/work-items/2026-07-01_small-medium-template-structure/spec_small-medium-template-structure.md`
- `docs/work-items/2026-07-01_small-medium-template-structure/plan_small-medium-template-structure.md`
- `docs/work-items/2026-07-01_small-medium-template-structure/handoff/research-verification.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`

Expected implementation edits:

- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `CHANGELOG.md`

Possible implementation edit only if validation requires it:

- `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`

Interfaces expected to remain stable:

- Harness release identity.
- Work-item lifecycle and freeze-gate sequence.
- Model/sub-agent policy notation.
- Small/medium plan template structure.
- Large/phased template structure.

## Model and Sub-agent Strategy

Current orchestration: Codex desktop, model/reasoning profile not explicitly exposed.
Fit assessment: Low-to-medium complexity, low runtime risk, moderate template-quality risk, low blast radius, and active repository policy `economy-default`.
Recommended change: None.

Sub-agents: None. The implementation touches one template and one changelog entry; main-thread integration is simpler than parallel delegation.

## Tasks

- [ ] Confirm the working tree before implementation and avoid staging unrelated existing harness-policy edits.
- [ ] Read `docs/work-items/2026-07-01_small-medium-template-structure/handoff/research-verification.md` and the approved spec before editing the template.
- [ ] Update `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md` metadata only where needed, preserving `Work ID`, `Short ID`, `Status`, `Harness release`, `Schema`, and `Policy references`.
- [ ] Replace the existing `Goal`, `Scope`, `Non-scope`, `Current state`, `Proposed behavior`, `Interfaces and data`, `Risks`, and `Acceptance criteria` prompts with a spec-first structure:
  - `Source and Intent`
  - `Scope Boundary`
  - `Repository Context`
  - `Requirements`
  - `Acceptance Criteria`
  - `Interfaces, Data, and Control Flow`
  - `Risks and Rejected Alternatives`
- [ ] Use card-style blocks and bullets for `Requirements`, `Acceptance Criteria`, and `Risks and Rejected Alternatives`; do not add wide tables with long cells to those new sections.
- [ ] Add prompt text explaining that requirements define scope while acceptance criteria define observable verification.
- [ ] Include SMART-oriented prompts for requirement and acceptance-criteria quality.
- [ ] Include compact INVEST adaptation prompts: use negotiable/value tradeoffs while drafting scope, use boundedness for context-window and single-thread fit, and preserve independence/testability for approved requirements.
- [ ] Include optional Given/When/Then example guidance only as a clarity aid, not as a mandatory format.
- [ ] Avoid EARS notation and avoid the word `shall` in the template.
- [ ] Preserve `Planned commits`, `Documentation artifact matrix`, and `Approval` sections with the current naming-policy placeholders.
- [ ] Add a `Spec readiness checklist` section before approval.
- [ ] Update `CHANGELOG.md` before the implementation commit with the approved implementation title snippet.
- [ ] Run the validation commands and inspect the template diff for scope creep into plan or large/phased templates.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spike: small-medium-template-structure -- approve spec-template update plan` | `2026-07-01_small-medium-template-structure -- approve spec-template update plan` | Approval commit for this spec, plan, and research report. |
| Implementation | `docs: small-medium-template-structure -- improve spec-template scaffolding` | `2026-07-01_small-medium-template-structure -- improve spec-template scaffolding` | Implementation commit for the small/medium spec template update and changelog entry. |

## Validation commands

| Command | Expected result |
|---|---|
| `git status --short` | Shows only approved planning artifacts staged during freeze, then implementation edits limited to `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`, `CHANGELOG.md`, and any directly required validator update. |
| `rg -n "TODO|NEEDS CLARIFICATION|TBD" docs/work-items/2026-07-01_small-medium-template-structure` | No unresolved planning placeholders. |
| `rg -n "\\bshall\\b|EARS" .agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md` | No matches after implementation. |
| `rg -n "## Source and Intent|## Scope Boundary|## Repository Context|## Requirements|## Acceptance Criteria|## Interfaces, Data, and Control Flow|## Risks and Rejected Alternatives|## Spec readiness checklist" .agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md` | Each expected section heading is present. |
| `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | All checks print `PASS ...` and the process exits with status 0, or the completion report names the exact blocker. |

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation` only if the operator wants this research package frozen.

Draft review status: Approved by operator on 2026-07-01.
Approval commit status: Approved for freeze; commit hash will be reported in the checkpoint output.
Post-freeze implementation authorization status: Paused; template implementation requires a fresh explicit operator instruction after the approval commit.

## Completion criteria

- Acceptance criteria in `spec_small-medium-template-structure.md` are met.
- Required validation commands have been run and recorded.
- The implementation changes only approved files, or any variance is recorded before commit.
- `CHANGELOG.md` has a newest-first entry before the implementation commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Plan-template and large/phased template changes remain deferred.
- De-facto sub-agent use is reported when applicable.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
