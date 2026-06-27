# Large Phase Orchestration Owner Plan

Work ID: `2026-06-27-large-phase-orchestration-owner`
Short ID: `large-phase-orchestration-owner`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `module:architecture`, `module:execution-quality`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Implementation summary

This change will add a section-level lifecycle rule that owns the large/phased planning state machine. It keeps the modular architecture intact: lifecycle owns ordering, freeze-gate owns approval mechanics, model policy owns delegation choices, architecture names ownership, and templates/router entries point to the right owners.

The implementation should be small and documentation-only. It should not split files or add a new module. The validator will be updated first so the missing orchestration owner is visible as a failing structural check before the documentation change makes it pass.

## Files and interfaces

Expected implementation files:

- `.agents/skills/dev-doc-harness/references/artifact-contract.md`: add `rule:lifecycle.large-phase-orchestration` to the owner table and a compact section that owns the large/phased state sequence.
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`: update the lifecycle module owned rule families or lifecycle decomposition guidance to mention large/phased orchestration ownership.
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: cite the lifecycle orchestration rule for ordering while keeping freeze mechanics local.
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: cite the lifecycle orchestration rule for phase order while keeping curated-artifact sub-agent guidance local.
- `.agents/skills/dev-doc-harness/SKILL.md`: cite the new rule in large anchor and phase-plan route outcomes.
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`: add the new rule to policy references and planning handoff text.
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`: add the new rule to policy references and input-context or freeze-gate text.
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`: strengthen existing golden traversal evidence for lifecycle ownership, large anchor routing, and phase-plan routing.
- `CHANGELOG.md`: add a newest-first implementation entry before committing.

No runtime interfaces or generated artifacts are expected to change.

## Model and Sub-agent Strategy

Current orchestration: Codex in the current desktop thread; exact model and reasoning controls are not exposed in repo artifacts.
Fit assessment: bounded documentation architecture change, low runtime risk, moderate process impact, tightly coupled wording across current harness policy surfaces.
Recommended change: use the active operator choice for this thread if confirmed at execution time; otherwise use the active repository policy, `economy-default`.

Sub-agents: None. The implementation is a small, tightly coupled policy wording change where one orchestration thread should own final consistency.

## Tasks

- [ ] Review the current large/phased lifecycle wording in `artifact-contract.md`, `planning-freeze-gates.md`, `subagent-model-policy.md`, `SKILL.md`, and the large/phased templates.
- [ ] Add failing structural checks in `Test-HarnessPolicy.ps1` for `rule:lifecycle.large-phase-orchestration`, the `Large or phased planning orchestration` owner heading, and references from large anchor and phase-plan surfaces.
- [ ] Run `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` and verify it fails for the new missing orchestration-owner evidence.
- [ ] Update `artifact-contract.md` with the new rule owner row and a compact `## Large or phased planning orchestration` section that defines the canonical state sequence and points artifact layout, freeze mechanics, and model policy to their existing owners.
- [ ] Update `policy-architecture.md` so the lifecycle module description or lifecycle decomposition direction names large/phased orchestration as lifecycle-owned.
- [ ] Update `planning-freeze-gates.md` so `rule:freeze.multi-gate-flow` cites the new lifecycle orchestration rule for phase order.
- [ ] Update `subagent-model-policy.md` so curated-artifact sub-agent phase-plan guidance cites the new lifecycle orchestration rule for ordering.
- [ ] Update `SKILL.md` and large/phased templates to cite `rule:lifecycle.large-phase-orchestration` in the relevant route outcomes and policy references.
- [ ] Update `CHANGELOG.md` with the implementation entry before committing.
- [ ] Run the validation commands and inspect failures before claiming completion.
- [ ] Review the final diff for duplicate policy blocks, stale references, route-budget impact, and accidental operator-visible behavior changes.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `large-phase-orchestration-owner spec: define large phase orchestration owner` | `2026-06-27-large-phase-orchestration-owner: define large phase orchestration owner` | Approval commit for this spec and plan. |
| Implementation | `large-phase-orchestration-owner docs: add large phase orchestration owner` | `2026-06-27-large-phase-orchestration-owner: add large phase orchestration owner` | Add lifecycle rule owner, align references/templates/router, strengthen validation, and update changelog. |

## Validation commands

| Command | Expected result |
|---|---|
| `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Exit code `0`; output includes `PASS scenarios.golden-traversal` and no `FAIL` lines |
| `rg -n "rule:lifecycle.large-phase-orchestration|Large or phased planning orchestration|large/phased planning state" .agents/skills/dev-doc-harness` | Outputs matches in lifecycle owner, architecture/reference/template/router surfaces, and validator evidence |
| `git diff --check` | Exit code `0`; no whitespace errors |
| `git status --short` | Shows only expected implementation files and `CHANGELOG.md` before the implementation commit |

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

This draft planning package is ready for operator review when the spec and plan contain no placeholders, open required decisions, or missing required sections. After operator approval, update `CHANGELOG.md`, mark approved statuses, stage only the approved planning artifacts and `CHANGELOG.md`, commit with the planned approval subject, report the commit hash and approved artifact paths, and stop before implementation.

## Completion criteria

- Acceptance criteria in `spec-large-phase-orchestration-owner.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Variance log is present and current if nontrivial implementation variance occurs.
- De-facto sub-agent use is reported if it changes from the approved strategy.

## Approval

- Status: Approved
- Superseded by: None
