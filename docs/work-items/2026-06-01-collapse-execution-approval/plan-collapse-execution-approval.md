# Collapse Execution Approval Plan

Work ID: `2026-06-01-collapse-execution-approval`
Short ID: `collapse-execution-approval`
Status: Approved

## Implementation summary

Update the planning freeze gate to remove the redundant third approval in the common case. The approval commit remains the hard boundary between planning and implementation, but the post-freeze execution-setting confirmation should be able to include implementation authorization when the operator clearly says to start.

The canonical change belongs in `planning-freeze-gates.md`. After that, align the small/medium and phase-plan templates and the README if their wording would otherwise teach agents or operators that settings confirmation and start authorization must always be separate turns.

## Files and interfaces

Expected files to change:

- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `README.md`
- `CHANGELOG.md`

Interfaces expected to remain stable:

- Work item folder naming and required artifact layout.
- Draft review approval before the freeze commit.
- Approved planning package immutability after freeze.
- Active `economy-default` model/sub-agent policy.
- Amendment requirements for high-impact post-freeze variance.

## Model and Sub-agent Strategy

Current orchestration: GPT-5 Codex, reasoning effort not explicitly provided.
Fit assessment: low implementation risk and moderate process risk. The change is documentation-only, but the wording must be precise because agents will follow it literally. Budget and latency favor one orchestration-thread edit.
Recommended change: None.

Sub-agents: None. The files are tightly coupled process references; splitting the wording across agents would add coordination overhead and increase inconsistency risk.

## Tasks

- [ ] Update `planning-freeze-gates.md` so the post-freeze prompt combines execution-setting confirmation with whether implementation should begin now.
- [ ] Add explicit examples or criteria showing that clear post-gate responses such as `Confirm, proceed` satisfy both confirmation and start authorization.
- [ ] Preserve the rule that implementation cannot begin in the same turn as the freeze commit.
- [ ] Clarify how to handle ambiguous `Confirm` responses so settings-only confirmation does not accidentally start implementation unless the prompt made that meaning explicit.
- [ ] Update plan templates if their freeze-gate text needs to point at the combined post-freeze confirmation behavior.
- [ ] Update `README.md` if the operator-facing flow needs to describe the two-approval path.
- [ ] Add a newest-first `CHANGELOG.md` entry for this work before committing implementation changes.
- [ ] Review all changed docs for consistent terminology around `approval`, `confirmation`, `authorization`, `post-freeze`, and `implementation`.

## Validation commands

| Command | Expected result |
|---|---|
| `rg -n "fresh explicit|model, reasoning|reasoning-effort|begin implementation|before implementation|Confirm|proceed|third approval" .agents README.md CHANGELOG.md docs/work-items/2026-06-01-collapse-execution-approval` | Remaining matches are consistent with the combined post-freeze confirmation and implementation authorization behavior |
| `git diff --check` | No whitespace errors |
| `git status --short` | Only intended planning, harness documentation, README, and changelog files are modified or staged |

## Plan variance handling

Before approval, operator feedback edits this draft directly and does not require an amendment. After the approval commit or explicit handoff snapshot, approved plans are immutable snapshots. Record nontrivial implementation variance in `implementation-notes/variance-log.md` if implementation departs from this plan. Create a plan amendment and request operator approval before proceeding when post-freeze variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

When this plan is ready for operator review, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage the draft without committing, request approval or feedback, revise directly on feedback, and commit only after explicit approval.

## Completion criteria

- Acceptance criteria in `spec-collapse-execution-approval.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- No variance log is required unless implementation departs nontrivially from this approved plan.

## Approval

- Status: Approved
- Superseded by: None
