# Naming Conventions Plan

Work ID: `2026-07-01-naming-conventions`
Short ID: `naming-conventions`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Implementation summary

Create a new canonical naming reference and move naming mechanics there. Keep `artifact-contract.md` as the lifecycle owner, but replace detailed folder, filename, commit-subject, and changelog-title prose with concise references to `module:naming`.

Update current examples and template placeholders so future work-item packages, commit subjects, and changelog headings use the new underscore-separated semantic fields and lower-kebab title fields. Do not rename historical work-item artifacts or previous changelog entries.

Update the validation script so the new naming reference is part of the required policy graph. Add targeted validation coverage for discoverability and stale old-format examples on current surfaces where practical without turning the validator into a semantic parser.

## Files and interfaces

- Create: `.agents/skills/dev-doc-harness/references/naming-conventions.md`
- Modify: `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- Modify: `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- Modify: `.agents/skills/dev-doc-harness/SKILL.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
- Modify: `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`
- Modify: `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`
- Modify: `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
- Modify: `.agents/skills/dev-doc-harness/docs/operator-note.md`
- Modify: `README.md`
- Modify: `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
- Modify: `CHANGELOG.md`

No runtime interface, external API, storage schema, or command-line interface changes are expected.

## Model and Sub-agent Strategy

Current orchestration: Codex desktop, reasoning effort not explicitly selected.
Fit assessment: This is a bounded documentation-policy change with moderate searchability risk and low runtime blast radius. Correctness depends on consistent edits across current harness surfaces and validation.
Recommended change: None for planning. Use the active repository policy, `economy-default`, for any later implementation assistance.

Sub-agents: None. The work is cohesive and touches a shared set of policy files where main-thread integration judgment is more valuable than parallel write work.

## Tasks

- [ ] Create `.agents/skills/dev-doc-harness/references/naming-conventions.md` with `module:naming`, owner table entries, definitions for `<date>`, `<issue-key>`, `<short-title>`, `<phase-id>`, `<phase-title>`, `<work-id>`, and `<short-id>`, plus rules for folders, artifact filenames, commit messages, changelog entries, collision handling, and normalization.
- [ ] Update `.agents/skills/dev-doc-harness/references/policy-architecture.md` so the canonical module catalog includes `module:naming`, dependency direction permits lifecycle references to cite naming, and route guidance mentions naming only where needed.
- [ ] Update `.agents/skills/dev-doc-harness/references/artifact-contract.md` so lifecycle sections cite `module:naming` for naming mechanics while preserving lifecycle-owned behavior for work sizing, artifact layout intent, immutability, documentation matrix, variance, commit planning, and changelog-before-commit requirements.
- [ ] Update `.agents/skills/dev-doc-harness/SKILL.md` workflow and completion guidance to use the new work ID and durable artifact filename shapes through concise references to `module:naming`.
- [ ] Update all current templates listed in this plan so `Work ID`, `Short ID`, planned commit, changelog, phase-plan, amendment, variance-log, and completion examples use the new naming grammar without copying the long normalization rules.
- [ ] Update README and `.agents/skills/dev-doc-harness/docs/operator-note.md` examples so operator-facing naming examples match the new convention.
- [ ] Update `.agents/skills/dev-doc-harness/references/subagent-role-examples.md` and `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md` examples so current reusable examples no longer teach the old filename pattern.
- [ ] Update `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` to include the new canonical reference in required files, current-surface scans, graph ownership, placeholder scans, and discoverability checks.
- [ ] Update `CHANGELOG.md` before the implementation commit with a newest-first entry matching the planned implementation subject.
- [ ] Run validation commands and fix any current-surface failures in the implementation scope.
- [ ] Confirm `git status --short` contains only the intended implementation files before the implementation commit.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets. Update this table before committing if implementation changes the subject wording.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `naming-conventions spec: define naming convention policy` | `2026-07-01-naming-conventions: define naming convention policy` | Approval commit for this spec, plan, and test-case snapshot under the current harness commit policy. |
| Implementation | `naming-conventions docs: centralize naming convention rules` | `2026-07-01-naming-conventions: centralize naming convention rules` | Applies the naming policy change after a fresh post-freeze operator instruction. |

## Validation commands

| Command | Expected result |
|---|---|
| `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | All checks print `PASS ...` and the process exits with status 0. |
| `rg -n "YYYY-MM-DD-short-kebab-title|YYYY-MM-DD-ISSUE-short-kebab-title|spec-<short-id>|plan-<short-id>|plan-phase|plan-amendment-NNN-short-title" .agents/skills/dev-doc-harness README.md AGENTS.md` | No matches in current reusable surfaces except historical release notes or intentional migration notes with clear context. |
| `rg -n "module:naming|rule:naming" .agents/skills/dev-doc-harness/references .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/assets/templates README.md` | Matches show the new owner file and concise references from current reusable surfaces. |

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Draft review status: approved by operator.
Approval commit status: approved for freeze; see freeze-gate completion report for commit hash.
Post-freeze implementation authorization status: paused; implementation requires fresh operator instruction after the approval commit.

## Completion criteria

- Acceptance criteria in `spec-naming-conventions.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current if implementation drift occurs.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
