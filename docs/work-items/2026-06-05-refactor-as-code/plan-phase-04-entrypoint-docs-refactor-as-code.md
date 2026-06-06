# Phase 04: Entrypoint Docs Plan

Work ID: `2026-06-05-refactor-as-code`
Short ID: `refactor-as-code`
Status: Approved
Schema: `schema:plan.phase`
Policy references: `module:lifecycle`, `module:architecture`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:quality.phase-plan-fresh-thread`, `rule:models.strategy-required`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Objective

Update the harness public entrypoint, root repository instructions, README, and compact compatibility guidance so agents and operators route through the canonical module and rule ownership map created in Phase 02 and consumed by templates in Phase 03.

Phase 04 must preserve the existing harness lifecycle, approval freeze gates, variance rules, changelog discipline, active repository model-policy selection point in `AGENTS.md`, and the rule-versioning deferral. It must not rewrite frozen historical work-item artifacts.

## Input context

The implementing agent must read these current instructions, frozen planning artifacts, and current harness surfaces before editing:

- `AGENTS.md`
- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
- `.agents/skills/dev-doc-harness/assets/templates/`
- `README.md`
- `docs/work-items/2026-06-05-refactor-as-code/spec-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-amendment-001-architecture-guardrails-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-phase-02-canonical-modules-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-phase-03-template-slimming-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`

Preserve these prior-phase decisions:

- `AGENTS.md` bootstraps the repository-local harness and remains the single repository-local selection point for the active model policy.
- `.agents/skills/dev-doc-harness/SKILL.md` is the public harness entrypoint and should become the operation router rather than requiring every core reference for every operation.
- Canonical references own reusable policy; README and templates do not.
- Templates own artifact shape and work-specific prompts, citing schema IDs and canonical policy IDs.
- Historical work-item artifacts are immutable snapshots and are not migration targets for current policy wording.
- Rule IDs are stable retrieval and ownership anchors, not a full rule-versioning system.

## Likely files and areas

Modify during Phase 04 execution:

- `.agents/skills/dev-doc-harness/SKILL.md`
- `AGENTS.md`
- `README.md`
- `CHANGELOG.md`

Modify only if required for entrypoint or compatibility coherence discovered during execution:

- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`

Do not modify in Phase 04 unless an approved amendment changes the phase boundary:

- `.agents/skills/dev-doc-harness/assets/templates/`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- Frozen historical work-item artifacts under `docs/work-items/`, including this work item's approved spec, amendments, snapshots, and Phase 01 through Phase 03 plans
- Active repository model policy selection away from the `AGENTS.md` selector
- Any full rule-versioning system, validation script, or Phase 05 golden-scenario automation

## Model and Sub-agent Strategy

Current orchestration: Codex in this desktop thread; exact model/profile and reasoning effort are not exposed in repository artifacts.
Fit assessment: Phase 04 is architecture-sensitive documentation work with medium-to-high process blast radius. It updates the public route agents follow before planning or implementation, so omissions can weaken retrieval, freeze-gate discoverability, model-policy handling, or compatibility guidance. The repository default is the active policy selected in `AGENTS.md`, currently `economy-default`.
Recommended change: Use the active repository policy. Use stronger reasoning in the orchestration thread for the final router and documentation review because entrypoint mistakes affect future harness use.

Sub-agents: None. The expected edits are tightly coupled prose changes across entrypoint and operator-facing docs, and the current assignment is to plan only. During implementation, the orchestration thread should own integration and final architecture review unless the operator explicitly authorizes a bounded reviewer.

## Tasks

- [ ] **Step 1: Verify starting state**

  Run:

  ```powershell
  git status --short --branch
  ```

  Expected: branch is `refactor-as-code`; no unrelated staged or unstaged files are present before Phase 04 implementation edits.

- [ ] **Step 2: Re-read required inputs**

  Read every file and artifact listed in `## Input context`.

  Confirm these execution constraints before editing: no frozen historical artifact rewrite, no template changes, no active model-policy selector change away from `AGENTS.md`, no full rule-versioning system, no Phase 05 validation scripts, and no amendment need from Phase 01 through Phase 03.

- [ ] **Step 3: Inventory entrypoint and summary drift**

  Run:

  ```powershell
  rg -n "Before creating or reviewing artifacts|Core references|Workflow|Completion checklist|Planning Artifact Freeze Gate|active model policy|economy-default|enterprise-default|canonical source|router|operation|module:|rule:|Superpowers compatibility|spec-kit compatibility" AGENTS.md README.md .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/references
  ```

  Use the output to identify:

  - Places where `SKILL.md` still implies eager loading of all core references.
  - README or root instruction text that restates detailed policy instead of pointing to canonical owners.
  - Compatibility guidance that needs compact alignment with the router and ownership map.
  - Any remaining current-surface default-model wording that should instead refer to the active repository policy selected in `AGENTS.md`.

- [ ] **Step 4: Update `SKILL.md` into an operation router**

  In `.agents/skills/dev-doc-harness/SKILL.md`, add a compact operation-oriented router that cites `module:architecture` and the Phase 02 canonical owner map.

  The router must cover at least these operation families and required modules or references:

  | Operation family | Required route |
  |---|---|
  | Classify work size | `module:lifecycle`; `rule:lifecycle.work-sizing` |
  | Draft or review small/medium artifacts | `module:lifecycle`, `module:quality`, small/medium templates, and `module:models` for substantial model/sub-agent strategy |
  | Draft or review large anchor specs | `module:lifecycle`, `module:quality`, `module:models`, large/phased spec template |
  | Draft or review phase plans | Approved spec and amendments, prior phase outputs, `module:quality`, `module:lifecycle`, `module:models`, phase-plan template |
  | Freeze planning packages | `module:freeze-gate`, `module:lifecycle`; especially changelog and immutable snapshot rules |
  | Execute approved work and record variance | Approved artifacts, `module:lifecycle`, `module:execution-quality`, phase validation commands |
  | Use or review sub-agent strategy | `module:models`; `module:role-examples` only when useful |
  | Evidence-heavy review or reports | `module:evidence` only when invoked by the task, plan, or operator |
  | Update templates or router guidance | `module:architecture` plus the canonical owner for each referenced rule family |
  | Superpowers or spec-kit compatibility | `AGENTS.md`, `module:lifecycle`, `SKILL.md` compatibility notes, and the relevant external workflow instructions |

  Keep `SKILL.md` concise. It should route agents to owners and templates, not duplicate detailed freeze, variance, model, or artifact-contract prose.

- [ ] **Step 5: Preserve `SKILL.md` safety behavior while reducing eager loading**

  In `SKILL.md`, keep these outcomes discoverable:

  - Very small mechanical edits may skip durable artifacts only under the sizing rules.
  - Substantial repository development uses `docs/work-items/<work-id>/`.
  - Draft planning artifacts are staged for review before approval and not committed until explicit approval or handoff.
  - Approval freeze commits only approved planning artifacts plus `CHANGELOG.md` and stops before implementation.
  - Frozen planning artifacts are immutable snapshots.
  - Nontrivial variance uses `implementation-notes/variance-log.md`; high-impact variance uses an approved amendment.
  - `CHANGELOG.md` is updated before every commit.
  - Sub-agent strategy follows the active repository policy notation.

  Express these as route outcomes and rule IDs where practical, not copied detailed procedure.

- [ ] **Step 6: Update root `AGENTS.md` as a bootstrap and selector**

  Update `AGENTS.md` only to align with the new router and ownership map.

  Required outcomes:

  - Keep `.agents/skills/dev-doc-harness/SKILL.md` as the repository-local harness entrypoint.
  - Keep the active model-policy selection section as the single repository-local selection point, currently pointing to `economy-default` in `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
  - Point detailed lifecycle, freeze-gate, variance, changelog, documentation matrix, compatibility, and quality rules to `SKILL.md` and canonical references instead of restating them in root instructions.
  - Preserve the compatibility statement that Superpowers may own normal development methodology while this harness owns artifact location and lifecycle.

  Do not change the active repository policy away from the current `AGENTS.md` selector.

- [ ] **Step 7: Update README operator guidance**

  Update `README.md` so operator-facing guidance reflects the router and ownership map.

  Required outcomes:

  - Explain that agents discover the harness through `AGENTS.md`, then use `SKILL.md` as an operation router.
  - Summarize that canonical references own reusable policy and templates own artifact shape.
  - Make clear that README is an operator overview and not the normative source when a canonical reference differs.
  - Refresh the "What is inside" and "How to use it" sections to name `references/policy-architecture.md` and the router behavior.
  - Keep the active model-policy wording policy-relative, with `AGENTS.md` as the selection point.
  - Preserve helpful operator prompts and plan-only PR/freeze-gate outcomes without copying long canonical procedure.

- [ ] **Step 8: Compact compatibility guidance only if needed**

  If the `SKILL.md`, `AGENTS.md`, and `README.md` updates expose a gap where compatibility behavior lacks a canonical owner, make the smallest necessary clarification in one of the allowed canonical references:

  - Use `artifact-contract.md` for lifecycle compatibility between this harness, Superpowers, and spec-kit.
  - Use `policy-architecture.md` for dependency direction, content type, or router ownership clarification.
  - Use `context-and-quality-gates.md` for execution-time environment compensation.

  Do not edit canonical references just for wording preference. If the required change affects architecture, scope, acceptance criteria, model policy, or plan feasibility, stop and draft an amendment instead.

- [ ] **Step 9: Update changelog for Phase 04 execution**

  Before the Phase 04 execution commit, add a newest-first `CHANGELOG.md` entry titled:

  ```text
  2026-06-05-refactor-as-code: complete Phase 04 entrypoint docs
  ```

  The entry must mention the `SKILL.md` operation router, root instruction alignment, README ownership-map guidance, compatibility guidance updates if any, and the decision not to rewrite frozen historical artifacts or change the active repository policy selector.

- [ ] **Step 10: Run validation commands**

  Run every command in `## Tests and validation` and record the result in the Phase 04 completion handoff.

- [ ] **Step 11: Final router and documentation review**

  Review the diff against the approved spec, amendment, Phase 01 architecture snapshot, Phase 02 module map, and Phase 03 template boundaries.

  Confirm:

  - `SKILL.md` routes common operations to the minimum needed modules and templates.
  - Public entrypoints preserve discoverability of freeze gates, variance/amendment behavior, changelog-before-commit, immutable snapshots, Superpowers/spec-kit compatibility, and active model-policy notation.
  - `AGENTS.md` remains bootstrap plus repository-specific active model-policy selector.
  - README summarizes operator outcomes and links to owners without becoming competing policy.
  - Templates and frozen historical work-item artifacts were not modified.
  - Rule versioning remains deferred.

  If review finds a high-impact architecture, scope, or feasibility issue, stop and draft a plan amendment instead of committing Phase 04 implementation.

- [ ] **Step 12: Commit Phase 04 outputs**

  Review the diff to confirm Phase 04 changed only allowed files and `CHANGELOG.md`.

  Commit with message:

  ```text
  Complete Phase 04 entrypoint docs
  ```

## Tests and validation

| Command | Expected result |
|---|---|
| `git status --short --branch` | Shows branch `refactor-as-code`; before the Phase 04 execution commit, only allowed Phase 04 files are modified or staged. |
| `rg -n "module:(architecture|lifecycle|freeze-gate|models|quality|execution-quality|evidence|role-examples)" .agents/skills/dev-doc-harness/SKILL.md README.md` | Outputs matches proving the public entrypoint and README cite the canonical module map. |
| `rg -n "rule:(lifecycle\\.work-sizing|lifecycle\\.variance-policy|lifecycle\\.changelog-before-commit|freeze\\.draft-review|freeze\\.approval-freeze|freeze\\.stop-before-implementation|models\\.strategy-required|quality\\.phase-plan-fresh-thread)" .agents/skills/dev-doc-harness/SKILL.md README.md AGENTS.md` | Outputs matches or route text proving safety-critical rules remain discoverable from public entrypoints. |
| `rg -n "active repository policy|single repository-local selection point|economy-default" AGENTS.md README.md .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/assets/templates .agents/skills/dev-doc-harness/references/subagent-model-policy.md` | Shows `economy-default` only where it is the repository selector in `AGENTS.md`, a policy definition in `subagent-model-policy.md`, or historical/frozen context outside current implementation targets; current summaries and templates otherwise use active-policy wording. |
| `rg -n "Status:[ ]Draft|T[D]B|T[O]DO|R[e]place|blank[ ]unless|unresolved[ ]decision" .agents/skills/dev-doc-harness/SKILL.md AGENTS.md README.md .agents/skills/dev-doc-harness/references/artifact-contract.md .agents/skills/dev-doc-harness/references/policy-architecture.md .agents/skills/dev-doc-harness/references/context-and-quality-gates.md` | No output. Exit code may be `1` because `rg` found no matches. |
| `git diff --name-only -- .agents/skills/dev-doc-harness/assets/templates docs/work-items` | No output unless `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md` records a justified Phase 04 variance. |
| `git diff --name-only` | Before staging for the Phase 04 execution commit, includes only `CHANGELOG.md`, `.agents/skills/dev-doc-harness/SKILL.md`, `AGENTS.md`, `README.md`, and any explicitly justified allowed canonical-reference compatibility clarification. |

## Documentation tasks

- Update `CHANGELOG.md` before the Phase 04 execution commit.
- Do not update templates; Phase 03 already completed template slimming.
- Do not update `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`; it is a frozen Phase 01 snapshot.
- Update `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md` only if Phase 04 execution departs from this approved plan.
- Do not create `snapshots/test-cases.snapshot.md` or validation scripts in Phase 04. Those remain deferred to Phase 05 by the approved anchor spec unless an amendment is approved.
- Do not create `deltas/operator-manual.delta.md` or `deltas/architecture-summary.delta.md` in Phase 04 unless the implementation thread determines a durable delta is needed before Phase 05 to preserve a non-obvious operator or architecture documentation decision. If created, force-add the file because this work item is an approved tracked exception under `docs/work-items/`.

## Variance rules

Before approval, operator feedback edits this draft directly and does not require an amendment. After the approval commit or explicit handoff snapshot, this phase plan is immutable.

During Phase 04 implementation, record nontrivial local technical variance in `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`. Create a plan amendment named `plan-amendment-NNN-short-title-refactor-as-code.md` and request operator approval before proceeding when post-freeze variance affects architecture, public interfaces, data, security, privacy, compliance, scope, acceptance criteria, active model-policy selection, compatibility authority, rule-versioning scope, or plan feasibility.

## Planning artifact freeze gate

For draft review, stage only this phase plan with:

```powershell
git add -f docs/work-items/2026-06-05-refactor-as-code/plan-phase-04-entrypoint-docs-refactor-as-code.md
```

Then ask the operator to approve the staged draft or provide feedback. Do not commit before explicit approval.

After explicit approval, update `CHANGELOG.md`, verify the approved plan has no unresolved required items, stage only this phase plan and `CHANGELOG.md`, commit the approved planning package, and stop before implementation. Report the commit hash and approved artifact path, remind the operator they may push and create a draft plan-only PR, and ask the operator to confirm model, reasoning-effort, and sub-agent policy choices plus whether Phase 04 implementation should begin.

## Handoff output

At Phase 04 completion, the implementing agent must report:

- Assigned scope.
- Files inspected.
- Files changed.
- Commands and validation results.
- Router entries added or changed in `SKILL.md`.
- Root instruction changes and confirmation that `AGENTS.md` remains the active model-policy selector.
- README operator-summary changes and confirmation that README does not own normative policy.
- Compatibility guidance changes, or a statement that no canonical-reference compatibility edits were needed.
- Confirmation that templates and frozen historical work-item artifacts were not modified, or an approved amendment reference if any were modified.
- Any variance entries or a statement that no variance occurred.
- Sub-agent use, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.
- Residual risks and recommended Phase 05 action.

## Completion criteria

- Phase objective is met.
- `SKILL.md` acts as an operation router to canonical modules, supplemental references, templates, and current work-item artifacts.
- `AGENTS.md` remains a concise bootstrap and the single repository-local active model-policy selection point.
- README explains the router and ownership map as operator-facing guidance without becoming a competing normative source.
- Compatibility guidance for Superpowers and spec-kit remains discoverable and aligned with `module:lifecycle` and `module:architecture`.
- Freeze gate, variance/amendment, changelog-before-commit, immutable snapshot, work sizing, durable quality, and model/sub-agent strategy rules remain discoverable from entrypoints.
- Rule versioning remains deferred; Phase 04 introduces no full versioning system.
- No templates or frozen historical work-item artifacts are rewritten.
- Validation commands have been run and recorded.
- `CHANGELOG.md` has a newest-first entry for Phase 04 before the execution commit.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable.
