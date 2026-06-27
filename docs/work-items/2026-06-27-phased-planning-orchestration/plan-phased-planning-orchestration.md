# Phased Planning Orchestration Plan

Work ID: `2026-06-27-phased-planning-orchestration`
Short ID: `phased-planning-orchestration`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `module:architecture`, `module:execution-quality`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Implementation summary

This change tightens the harness policy path that currently leaves too much room for one-shot large/phased planning. The implementation will update canonical lifecycle and freeze-gate wording first, then align the model policy, templates, router summaries, operator-facing docs, and validation script with that canonical behavior.

The behavior to preserve is deliberately narrow: the anchor spec is still the durable handoff artifact, phase plans still derive from the approved anchor spec, and implementation still waits for post-freeze authorization. The behavior to change is the default planning orchestration: agents should not create concrete phase-plan files during the anchor-spec planning package unless the operator explicitly requests combined planning. After anchor-spec approval or handoff, curated-artifact sub-agent phase-plan drafting becomes the preferred orchestration when phases are independent enough and the platform supports it.

## Files and interfaces

Expected current harness files to modify:

- `.agents/skills/dev-doc-harness/references/artifact-contract.md`: clarify large/phased layout and anchor-spec-only initial planning.
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: clarify anchor-spec freeze as a stop before later phase-plan drafting.
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: add phase-plan drafting guidance that prefers curated-artifact sub-agents when justified and supported.
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`: mark phase-plan output filenames as future artifacts and forbid creating phase-plan files in the anchor-spec package unless explicitly requested.
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`: reinforce approved-anchor input context and context-strategy recording.
- `.agents/skills/dev-doc-harness/SKILL.md`: route large anchor spec drafting as anchor-spec-only by default and route phase-plan drafting as post-anchor work.
- `.agents/skills/dev-doc-harness/docs/operator-note.md`: summarize the clarified large/phased operator flow.
- `README.md`: update the operator overview and diagram text so the large/phased path reads as anchor spec first, then later phase plans.
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`: strengthen golden traversal evidence checks for large-anchor and phase-plan scenarios.
- `CHANGELOG.md`: add planning approval and implementation entries before the corresponding commits.

No runtime APIs or generated artifacts are expected to change.

## Model and Sub-agent Strategy

Current orchestration: Codex in the current desktop thread, exact model and reasoning controls not exposed in repo artifacts.
Fit assessment: bounded documentation/process change with high downstream process impact but tightly coupled edits across current harness surfaces; budget and latency are moderate; ambiguity is low after the operator approved the design direction.
Recommended change: None for implementation. Use the active repository policy, `economy-default`, and keep this implementation in the orchestration thread so one agent owns final wording consistency across canonical references, templates, validation, and operator docs.

Sub-agents: None for this implementation. The files are tightly coupled policy surfaces, and parallel write-capable agents would add coordination risk. The implementation itself will add guidance that future large/phased planning should prefer curated-artifact sub-agent phase-plan drafting when justified and supported.

## Tasks

- [ ] Review the current large/phased wording in `artifact-contract.md`, `planning-freeze-gates.md`, `subagent-model-policy.md`, `SKILL.md`, the large/phased templates, `README.md`, and `docs/operator-note.md` to identify the exact paragraphs that mention phase-plan sequencing and sub-agent context.
- [ ] Update `artifact-contract.md` so the large/phased layout distinguishes planned package shape from the anchor-spec-only initial planning package, and so `rule:lifecycle.large-anchor-spec` explicitly says not to create concrete phase-plan files during the anchor-spec planning package unless the operator explicitly requests combined planning.
- [ ] Update `planning-freeze-gates.md` so `rule:freeze.multi-gate-flow` states that anchor-spec freeze pauses before later phase-plan drafting and that phase-plan drafting resumes only after fresh operator instruction.
- [ ] Update `subagent-model-policy.md` so `module:models` prefers curated-artifact sub-agent phase-plan drafting after anchor-spec freeze when phases are independently plannable and platform support is available, while requiring a recorded fallback reason when sub-agents are not used.
- [ ] Update `large-phased-work-item-spec.md` so the planning handoff quality bar and phase decomposition table label phase-plan filenames as future outputs and instruct the agent to stop at the anchor-spec gate unless combined planning was explicitly requested.
- [ ] Update `large-phased-work-item-phase-plan.md` so the input context section requires the approved anchor spec or handoff snapshot, amendments, prior phase outputs, and recorded context strategy; keep the phase plan fresh-agent executable.
- [ ] Update `SKILL.md` route outcomes so large anchor spec drafting records an anchor-spec-only draft review state, while phase-plan drafting is clearly a post-anchor route using approved specs, amendments, prior phase outputs, and model/context strategy.
- [ ] Update `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md` with concise operator-facing language: large work gets anchor spec first; phase plans come later; curated-context sub-agents may replace separate operator-visible threads when justified.
- [ ] Update `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` by strengthening existing `scenario:planning.large-anchor-freeze`, `scenario:planning.phase-plan-freeze`, and `scenario:models.sub-agent-authorization` evidence checks. Use string evidence from current files; do not add a new scenario ID that would require rewriting frozen historical snapshots.
- [ ] Update `CHANGELOG.md` before the implementation commit with `Release target: unreleased`, `Package impact: distributable`, and `Release-note: include`.
- [ ] Run the validation commands in this plan and inspect failures before claiming completion.
- [ ] Review the final diff for unrelated changes, duplicated reusable policy blocks, stale placeholders, and consistency between canonical references, templates, operator docs, and validation script evidence.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets. Update this table before committing if implementation changes the subject wording.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `phased-planning-orchestration spec: clarify phased planning orchestration` | `2026-06-27-phased-planning-orchestration: clarify phased planning orchestration` | Approval commit for this spec and plan. |
| Implementation | `phased-planning-orchestration docs: enforce anchor-spec-first phase planning` | `2026-06-27-phased-planning-orchestration: enforce anchor-spec-first phase planning` | Update canonical references, templates, router, operator docs, validator, and changelog. |

## Validation commands

| Command | Expected result |
|---|---|
| `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Exit code `0`; output includes `PASS scenarios.golden-traversal` and no `FAIL` lines |
| `rg -n "anchor-spec-only|combined planning|curated-artifact sub-agent|phase-plan drafting" .agents/skills/dev-doc-harness README.md` | Outputs matches in canonical references, templates, router or operator docs, and validation script evidence |
| `git diff --check` | Exit code `0`; no whitespace errors |
| `git status --short` | Shows only the expected implementation files and `CHANGELOG.md` before the implementation commit |

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

This draft planning package is ready for operator review when the spec and plan contain no placeholders, open required decisions, or missing required sections. After operator approval, update `CHANGELOG.md`, mark approved statuses, stage only the approved planning artifacts and `CHANGELOG.md`, commit with the planned approval subject, report the commit hash and approved artifact paths, and stop before implementation.

## Completion criteria

- Acceptance criteria in `spec-phased-planning-orchestration.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Variance log is present and current if nontrivial implementation variance occurs.
- De-facto sub-agent use is reported if it changes from the approved strategy.

## Approval

- Status: Approved
- Superseded by: None
