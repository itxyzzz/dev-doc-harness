# Commit Message Format Plan

Work ID: `2026-06-14-commit-message-format`
Short ID: `commit-message-format`
Status: Approved
Harness release: `unknown`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Implementation summary

Implement the second design approach: add a new lifecycle rule, `rule:lifecycle.commit-message-format`, to the existing artifact contract and route all harness commit naming requirements through that rule. Keep the policy close to the existing `CHANGELOG.md` before-commit rule because both apply at commit time.

The implementation should update freeze-gate language so plan approval commits use the subject recorded in the approved artifacts. It should update reusable work-item templates to include planned commit subjects as reviewable content. It should also make the synchronization rule explicit: planned commit subject snippets, approval or implementation commit subjects, and matching changelog headings or bullet-level title snippets must stay aligned. Commit subjects should start with the work short ID; issue keys are not duplicated as separate prefixes because issue-backed work already carries the key in the short ID.

No automated enforcement is planned. The harness currently operates as documentation, templates, and validation scripts; this change should preserve that model and rely on the review/freeze flow plus validation searches.

## Files and interfaces

Expected changes:

- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
- `README.md` only if its operator-facing flow needs commit/changelog wording.
- `CHANGELOG.md` before the planning approval commit and implementation commit.

Interfaces expected to remain stable:

- Work item folder and short ID derivation.
- Existing changelog grouping names.
- Planning freeze gate stop-before-implementation behavior.
- Sub-agent model policy notation.

## Model and Sub-agent Strategy

Current orchestration: GPT-5 Codex, reasoning effort not explicitly exposed.
Fit assessment: bounded documentation/process change with moderate policy consistency risk and low implementation blast radius. Repository policy is `economy-default`; a single orchestration-thread edit is appropriate.
Recommended change: None.

Sub-agents: None. The work is small/medium, tightly scoped to a few canonical docs and templates, and benefits more from main-thread consistency than parallel review.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `commit-message-format - Spec: commit message format` | `2026-06-14-commit-message-format: commit message format` | Commit only approved planning artifacts and `CHANGELOG.md` after operator approval. |
| Implementation | `commit-message-format docs: define harness commit message format` | `2026-06-14-commit-message-format: define harness commit message format` | Commit canonical reference, template, optional README, validation, and changelog changes. |

## Tasks

- [ ] Add `rule:lifecycle.commit-message-format` to the `artifact-contract.md` owned rule table.
- [ ] Add a canonical commit message section to `artifact-contract.md` covering all harness commits, short-ID prefixing without duplicated issue keys, planning approval subjects, typed implementation subjects, allowed types, planned-subject review, and changelog synchronization.
- [ ] Update `planning-freeze-gates.md` so approval freeze commits use the planned commit subject from the approved artifact set.
- [ ] Update small/medium spec and plan templates with a compact `Planned commits` section.
- [ ] Update large/phased spec, phase-plan, and amendment templates with planned commit subject guidance appropriate to each artifact type.
- [ ] Update `README.md` only if current operator-facing lifecycle text would otherwise omit or contradict the new commit-message policy.
- [ ] Add a newest-first `CHANGELOG.md` entry before the implementation commit with a title snippet synchronized to the planned implementation subject.
- [ ] Review canonical references and templates for stale wording that treats commit subjects as unspecified.
- [ ] Run harness validation and targeted searches.

## Validation commands

| Command | Expected result |
|---|---|
| `pwsh -NoProfile -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Harness policy validation passes. |
| `rg -n "commit-message-format|Planned commits|planned commit|commit subject|CHANGELOG.*title|rule:lifecycle.commit-message-format" .agents README.md docs/work-items/2026-06-14-commit-message-format` | Matches show the new rule, template sections, freeze-gate wording, and synchronized changelog guidance. |
| `rg -n "commit message|commit subject|planned commit|CHANGELOG" .agents/skills/dev-doc-harness/assets/templates .agents/skills/dev-doc-harness/references README.md` | No canonical template or reference leaves harness commit subjects unspecified where commit behavior is described. |

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

Changing planned commit subjects during implementation is allowed only when the matching plan row and changelog title or bullet-level snippet are updated before commit. If the changed subject reflects a scope or acceptance-criteria change, use the normal variance or amendment path first.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Draft review status: completed.
Approval commit status: approved by operator on 2026-06-14; freeze commit pending.
Post-freeze implementation authorization: pending a fresh operator instruction after approval freeze.

## Completion criteria

- Acceptance criteria in `spec-commit-message-format.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects used for this work match the approved planned subjects or recorded variance.
- Changelog heading/title snippets match the approved planned commit snippets.
- Variance log is present and current only if implementation variance occurs.
- De-facto sub-agent use is reported when applicable; expected use is none.

## Approval

- Status: Approved
- Superseded by: not applicable
