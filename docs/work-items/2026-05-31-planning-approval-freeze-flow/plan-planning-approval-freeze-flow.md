# Planning Approval Freeze Flow Plan

Work ID: `2026-05-31-planning-approval-freeze-flow`
Status: Approved

## Implementation summary

Update the harness wording so planning review is no longer conflated with freezing. The canonical `planning-freeze-gates.md` reference should become the main source for the new sequence: draft, stage, request approval, revise on feedback, commit after explicit approval, then freeze.

After the canonical reference is updated, align the entry-point skill, artifact contract, durable planning quality reference, templates, and README with that lifecycle. Keep the changes documentation-only and focused on the review/freeze boundary.

## Files and interfaces

Expected files to change:

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
- `README.md`
- `CHANGELOG.md`

Interfaces expected to remain stable:

- Work item folder naming and required artifact layout.
- Existing variance classes and amendment requirements after freeze.
- Active `economy-default` model/sub-agent policy.

## Model and Sub-agent Strategy

Current orchestration: GPT-5 Codex, reasoning effort not explicitly provided.
Fit assessment: low implementation risk, moderate process risk because stale wording across several docs could keep producing the wrong agent behavior. Budget and latency favor a single orchestration-thread edit.
Recommended change: None.

Sub-agents: None. The task is a cohesive documentation/process edit across related files; sub-agent coordination would add overhead and risk inconsistent wording.

## Tasks

- [ ] Update `planning-freeze-gates.md` to define the pre-approval draft review checkpoint and the post-approval freeze commit checkpoint.
- [ ] Update `SKILL.md` workflow language so drafts remain editable until explicit approval or explicit handoff, and approval triggers the freeze gate.
- [ ] Update `artifact-contract.md` immutable snapshot and variance language so amendments are required only after approval commit or explicit handoff.
- [ ] Update `durable-planning-quality.md` to say missing context discovered before approval edits the draft, while missing context discovered after freeze uses variance/amendment handling.
- [ ] Update small/medium, large/phased, phase-plan, and amendment templates so their freeze-gate sections point to the approval-first flow.
- [ ] Update `README.md` diagram and operator-facing explanation to show stage-for-review before commit/freeze.
- [ ] Add a newest-first `CHANGELOG.md` entry for this work before committing implementation changes.
- [ ] Review all changed docs for consistent terminology around "draft", "approval", "commit", "freeze", "handoff", and "amendment".

## Validation commands

| Command | Expected result |
|---|---|
| `rg -n "commit-and-pause|frozen|freeze|approval|approve|stage|commit|amendment|amend" .agents README.md CHANGELOG.md docs/work-items/2026-05-31-planning-approval-freeze-flow` | Remaining matches are consistent with the approval-first lifecycle |
| `git diff --check` | No whitespace errors |
| `git status --short` | Only intended planning, harness documentation, README, and changelog files are modified or staged |

## Plan variance handling

Before approval, feedback on these draft planning artifacts should be incorporated directly into `spec-planning-approval-freeze-flow.md` and `plan-planning-approval-freeze-flow.md`, followed by refreshed staging and another approval request. After the approval commit freezes this planning package, record nontrivial implementation variance in `implementation-notes/variance-log.md` if such a log becomes necessary. Create a plan amendment and request operator approval before proceeding when post-freeze variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

When this plan is approved, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md` as updated by this work item where applicable. For this planning package specifically, stage the draft artifacts without committing, request operator approval or feedback, revise on feedback, and commit only after explicit approval.

## Completion criteria

- Acceptance criteria in `spec-planning-approval-freeze-flow.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- No variance log is required unless implementation departs nontrivially from this approved plan.

## Approval

- Status: Approved
- Superseded by: None
