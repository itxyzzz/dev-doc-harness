# Harness Follow-up Hardening Plan

Work ID: `2026-06-07-followup-hardening`
Short ID: `followup-hardening`
Status: Approved
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Implementation summary

Implement the follow-up hardening in one controlled pass after this plan is approved and frozen. Start with the lowest-risk authority cleanup: remove the nested `docs/work-items/AGENTS.md`, stop ignoring `docs/work-items/`, and stage all currently present historical work-item Markdown artifacts. Then update the router so substantial small/medium planning requires `module:models`.

After the policy surfaces are aligned, strengthen `Test-HarnessPolicy.ps1` so it validates the policy graph structurally. The script should derive declared owners and references from current harness files, fail dangling IDs, fail duplicate current owners, verify owner-table headings, verify template policy references against router-required modules, and report precise file/ID failures. Add route-budget and duplicate-block checks without scanning historical work-item artifacts for policy cleanup.

Finally, update README and the work-item documentation artifacts to describe tracked work-item docs, graph validation, route-budget checks, and the lifecycle split recommendation. Do not split `artifact-contract.md` during this work item; record the recommended decomposition path now that graph validation will protect future changes.

## Files and interfaces

Expected implementation targets:

- Delete `docs/work-items/AGENTS.md`.
- Update `.gitignore` to stop ignoring `docs/work-items/`.
- Track all existing Markdown artifacts under `docs/work-items/`.
- Update `.agents/skills/dev-doc-harness/SKILL.md` so substantial small/medium planning requires `module:models`.
- Update `.agents/skills/dev-doc-harness/references/policy-architecture.md` with graph-validation, route-budget, duplicate-block, and lifecycle decomposition guidance.
- Update `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`.
- Update `README.md`.
- Add or update `docs/work-items/2026-06-07-followup-hardening/snapshots/test-cases.snapshot.md`.
- Add or update `docs/work-items/2026-06-07-followup-hardening/snapshots/architecture.snapshot.md`.
- Add `docs/work-items/2026-06-07-followup-hardening/implementation-notes/variance-log.md`.
- Add implementation deltas under `docs/work-items/2026-06-07-followup-hardening/deltas/` when docs are updated.
- Update `CHANGELOG.md` before implementation commits.

Interfaces expected to remain stable:

- Harness entrypoint remains `.agents/skills/dev-doc-harness/SKILL.md`.
- Validation command remains `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`.
- Full rule versioning remains deferred.
- Active repository model policy remains `economy-default` except this approved work item uses the operator-selected `enterprise-default` execution policy.

## Model and Sub-agent Strategy

Current orchestration: Codex in this desktop thread; exact model/profile is not exposed in repository artifacts. Operator selected `enterprise-default` for this planning stage and requested continuation to plan.
Fit assessment: Medium complexity, moderate process risk, low runtime blast radius, high future-maintenance leverage. The main risk is weakening validation or authority rules through a brittle script or ambiguous docs.
Recommended change: Use `enterprise-default` for implementation and final review of this work item. No separate sub-agents are proposed because edits are tightly coupled across router, validation script, and docs, and the coordination overhead would likely exceed the value.

Sub-agents: None. Rationale: bounded but cross-file consistency is central, and the orchestration thread should own graph-validation design, integration, and final review. If a future operator explicitly asks for independent review, use a read-only reviewer with curated artifacts and no write scope.

## Tasks

- [ ] Verify current tracked and untracked files under `docs/work-items/`; record which historical files are newly tracked.
- [ ] Remove `docs/work-items/AGENTS.md` and update `.gitignore` so work-item docs are not ignored.
- [ ] Force-add currently present historical work-item Markdown artifacts under `docs/work-items/`.
- [ ] Update README contributing/operator guidance to describe tracked work-item documentation and historical-artifact authority.
- [ ] Update `SKILL.md` small/medium route so `module:models` is required for substantial small/medium planning.
- [ ] Update `policy-architecture.md` with the structural graph-validation model, route-budget expectations, duplicate-block scope, and lifecycle split recommendation.
- [ ] Refactor `Test-HarnessPolicy.ps1` to collect declared owner sets for `module:*`, `rule:*`, `schema:*`, and current `scenario:*` or `metric:*` anchors.
- [ ] Refactor `Test-HarnessPolicy.ps1` to collect current references from template `Policy references:`, router rows, README route tables, validation docs, and validation script scenario/check definitions.
- [ ] Add validation failures for dangling references, duplicate current owners, missing owner-table headings, missing route targets, and template policy-reference lists that do not satisfy router requirements.
- [ ] Add route-budget or route-depth checks for common operation routes.
- [ ] Add broad duplicate reusable-policy block checks across current harness surfaces, excluding historical `docs/work-items/` artifacts from cleanup enforcement.
- [ ] Add or update `snapshots/test-cases.snapshot.md` with positive and negative graph-validation test cases.
- [ ] Add or update `snapshots/architecture.snapshot.md` with lifecycle-module decomposition recommendation and validation model.
- [ ] Add documentation deltas for testing guide, operator manual, and architecture summary.
- [ ] Update `implementation-notes/variance-log.md`; record `None` if no variance occurs.
- [ ] Update `CHANGELOG.md` before the implementation commit.
- [ ] Run validation commands and inspect the final diff for unrelated changes, historical-artifact rewrites, and broad generated noise.

## Validation commands

| Command | Expected result |
|---|---|
| `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Exits `0`; prints existing PASS lines plus new graph, route-budget, duplicate-block, and tracking checks. |
| `git ls-files docs/work-items` | Lists all current historical and follow-up work-item Markdown artifacts that should now be tracked; does not list `docs/work-items/AGENTS.md`. |
| `git check-ignore -v docs/work-items/2026-06-07-followup-hardening/spec-followup-hardening.md` | Exits nonzero with no ignore match after `.gitignore` is updated. |
| `git status --short --ignored docs/work-items` | Shows no ignored work-item artifacts that should be tracked. |
| Safe dangling-ID negative check documented in `snapshots/test-cases.snapshot.md` | Demonstrates that the graph validator reports a missing owner for an introduced temporary reference, without committing the temporary mutation. |
| `rg -n "module:models.*when model or sub-agent strategy is assessed|module:models when sub-agent strategy is assessed" .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/references/policy-architecture.md` | No matches; small/medium substantial planning no longer makes model policy conditional. |
| `rg -n "Do not stage, commit|local working notes only|not this directory's planning documents" docs/work-items README.md AGENTS.md .agents/skills/dev-doc-harness` | No current authoritative instruction blocks contradict tracked work-item docs. Historical artifacts may be reviewed separately if this check finds old frozen text. |
| `git diff --check` | No whitespace errors. |

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

Likely acceptable local technical variance:

- Keeping `.gitignore` unchanged only if deleting `docs/work-items/AGENTS.md` plus force-adding all work-item docs proves sufficient and the final docs clearly explain the remaining ignore behavior.
- Implementing duplicate-block detection with conservative thresholds if a stricter algorithm creates noisy false positives.

Amendment-required variance:

- Reintroducing local-only work-item doc rules.
- Dropping structural graph validation.
- Completing an actual lifecycle module split in this work item instead of only documenting the decomposition path.
- Changing active repository model policy defaults.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this plan.

## Completion criteria

- Acceptance criteria in `spec-followup-hardening.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable; expected value is none.

## Approval

- Status: Approved
- Superseded by: None
