# Phase 03: Template Slimming Plan

Work ID: `2026-06-05-refactor-as-code`
Short ID: `refactor-as-code`
Status: Approved

## Objective

Slim current harness templates so they capture artifact shape, required work-specific decisions, and compact policy citations without carrying long reusable policy blocks.

Phase 03 must preserve fresh-thread usability. Templates should still tell a future agent which artifact sections to fill in, which decisions to record, and which canonical policy IDs apply. The implementation should cite the stable module and rule IDs created in Phase 02 rather than restating sub-agent authorization, variance handling, or freeze-gate procedure.

Phase 03 must not update `.agents/skills/dev-doc-harness/SKILL.md`, `README.md`, root `AGENTS.md`, or frozen historical work-item artifacts unless implementation discovers a blocker that requires an approved amendment.

## Input context

The implementing agent must read these approved artifacts and current references before editing templates:

- `AGENTS.md`
- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `docs/work-items/2026-06-05-refactor-as-code/spec-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-amendment-001-architecture-guardrails-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-phase-02-canonical-modules-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`

The Phase 02 completion handoff is the current repository state at commit `ab8ea5b10f1df428d9afc85dc07a948fa49d498f`, which added `references/policy-architecture.md` and stable module or rule IDs to canonical references. Treat the existing `Status: Draft` text inside the frozen Phase 02 plan as historical artifact state; do not edit that file during Phase 03.

## Likely files and areas

Modify during Phase 03 execution:

- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
- `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`
- `CHANGELOG.md`

Do not modify in Phase 03 unless an approved amendment changes the phase boundary:

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/*.md`
- `README.md`
- root `AGENTS.md`
- frozen historical work-item artifacts under `docs/work-items/`, including this work item's approved spec, amendments, snapshots, and Phase 01 or Phase 02 plans

## Template schema IDs and policy citations

Phase 03 should add compact schema IDs to template artifacts so later validation can cite template-owned shape without treating examples as reusable policy.

| Template | Schema ID | Required policy citations |
|---|---|---|
| `small-medium-work-item-spec.md` | `schema:spec.small-medium` | `module:lifecycle`, `module:quality`, `rule:lifecycle.documentation-matrix`, `rule:quality.spec-handoff` |
| `small-medium-work-item-plan.md` | `schema:plan.small-medium` | `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation` |
| `large-phased-work-item-spec.md` | `schema:spec.large-phased` | `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.large-anchor-spec`, `rule:quality.spec-handoff`, `rule:models.strategy-required`, `rule:freeze.multi-gate-flow` |
| `large-phased-work-item-phase-plan.md` | `schema:plan.phase` | `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:quality.phase-plan-fresh-thread`, `rule:models.strategy-required`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation` |
| `plan-amendment.md` | `schema:plan.amendment` | `module:lifecycle`, `module:freeze-gate`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation` |
| `variance-log.md` | `schema:variance-log` | `module:lifecycle`, `rule:lifecycle.variance-policy` |

Implementation may add a short `Policy references` or `Schema` line near the top of each template. Keep citations searchable and ASCII. Do not create a full rule-versioning system.

## Model and Sub-agent Strategy

Current orchestration: Codex in this desktop thread; exact model/profile and reasoning effort are not exposed in repository artifacts.
Fit assessment: Phase 03 is architecture-sensitive documentation work with medium blast radius. It changes templates that future agents will copy into durable artifacts, so the main risk is weakening safety reminders or making templates too terse for a fresh thread. The operator selected `enterprise-default` for Phase 03 despite the repository default `economy-default` policy.
Recommended change: Use `enterprise-default` for Phase 03 planning freeze and implementation unless the operator later changes this phase-specific choice. Use stronger reasoning in the orchestration thread for final template review because template wording affects future planning quality and process safety.

Sub-agents: None. The six template edits are tightly coupled around a single style and policy-citation pattern, and the platform/operator has not authorized a separate sub-agent wave for this planning turn. The orchestration thread should perform final review against the Phase 01 architecture snapshot and Phase 02 rule IDs.

## Tasks

- [ ] **Step 1: Verify starting state**

  Run `git status --short --branch`.

  Expected: current branch is `refactor-as-code`; no unrelated staged or unstaged files are present.

- [ ] **Step 2: Re-read required inputs**

  Read the artifacts and references listed in `## Input context`.

  Confirm these constraints before editing: Phase 03 is limited to templates plus `CHANGELOG.md`; templates own artifact shape, not reusable policy; stable IDs are retrieval anchors, not a versioning system; historical work-item artifacts are not migration targets; repository default model policy remains `economy-default`, with an operator-selected `enterprise-default` override for Phase 03.

- [ ] **Step 3: Inventory current template policy prose**

  Run:

  ```powershell
  rg -n "Sub-agents:|Context strategy must|After this .*approved|Fresh confirmation|Planning artifact freeze gate|variance|Variance|CHANGELOG|immutable|follow .*references|Record each command" .agents/skills/dev-doc-harness/assets/templates
  ```

  Use the output to identify long reusable policy blocks to reduce, especially sub-agent authorization, context strategy explanation, variance handling, and freeze-gate procedure.

- [ ] **Step 4: Add compact schema and policy-reference anchors**

  Add a short schema or policy-reference block near the top of each template listed in `## Template schema IDs and policy citations`.

  The block should identify the template schema ID and cite canonical modules or rules by ID. It should not copy detailed policy text from canonical references.

- [ ] **Step 5: Slim model and sub-agent prompts in plan templates**

  In `small-medium-work-item-plan.md` and `large-phased-work-item-phase-plan.md`, replace the long reusable sub-agent authorization block with compact prompts that require the work-specific fields already defined by `module:models`.

  Preserve these artifact-shape requirements:

  - Current orchestration.
  - Fit assessment.
  - Recommended change.
  - `Sub-agents: None` with rationale, or a bounded strategy table.
  - Strategy table columns for purpose, context strategy, input context, output artifact, model policy, model class/profile, reasoning effort, reason, parallelism, and blast radius.

  The local template text should cite `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation` instead of restating their full procedure.

- [ ] **Step 6: Slim model and sub-agent prompts in the large anchor spec template**

  In `large-phased-work-item-spec.md`, keep the phase-aware model/sub-agent strategy shape, but reduce reusable policy explanation to compact citations.

  Preserve the phase table because large/phased anchor specs may authorize phase-level review or implementation strategies. Cite `module:models` and the required model rule IDs rather than copying authorization and fresh-confirmation details.

- [ ] **Step 7: Slim freeze-gate reminders**

  In `small-medium-work-item-plan.md`, `large-phased-work-item-spec.md`, `large-phased-work-item-phase-plan.md`, and `plan-amendment.md`, replace long freeze-gate procedure prose with concise reminders that cite `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and when applicable `rule:freeze.stop-before-implementation` or `rule:freeze.multi-gate-flow`.

  Preserve the user-visible safety outcomes: drafts are staged for review before commit, feedback edits drafts directly before approval, approved planning packages are committed only after explicit approval, and implementation remains paused until fresh authorization after freeze.

- [ ] **Step 8: Slim variance guidance**

  In plan, phase-plan, amendment, and variance-log templates, replace repeated variance procedure with compact artifact prompts and citations to `module:lifecycle` and `rule:lifecycle.variance-policy`.

  Preserve the distinction between pre-approval feedback edits, ordinary variance-log entries, and high-impact amendments requiring operator approval before proceeding.

- [ ] **Step 9: Preserve artifact-shape and fresh-thread usability**

  Review each edited template to ensure a fresh agent can still fill it out without reading chat history. Keep section headings, required tables, documentation artifact matrices, approval sections, completion criteria, and handoff-output prompts where they carry artifact shape or work-specific decision capture.

  Remove only reusable procedure prose that now has canonical module or rule IDs.

- [ ] **Step 10: Update changelog for Phase 03 execution**

  Before the Phase 03 execution commit, add a newest-first `CHANGELOG.md` entry titled `2026-06-05-refactor-as-code: complete Phase 03 template slimming`.

  The entry must mention schema IDs or policy-reference anchors, reduced reusable policy prose in templates, preserved fresh-thread usability, and the decision not to update `SKILL.md`, `README.md`, root `AGENTS.md`, or historical work-item artifacts in Phase 03.

- [ ] **Step 11: Run validation commands**

  Run every command in `## Tests and validation` and record the result in the Phase 03 completion handoff.

- [ ] **Step 12: Final template review**

  Review the diff against the Phase 01 architecture snapshot and Phase 02 `policy-architecture.md`.

  Confirm:

  - Templates cite canonical owner IDs for reusable policy.
  - Templates do not contain long copied sub-agent authorization, variance, or freeze-gate procedure blocks.
  - Template examples remain clearly replaceable artifact-shape prompts, not competing policy.
  - Fresh-thread usability remains intact.
  - No canonical references, entrypoint, README, root instructions, or frozen work-item artifacts changed.

  If review finds a high-impact architecture, scope, or feasibility issue, stop and draft a plan amendment instead of committing Phase 03 implementation.

- [ ] **Step 13: Commit Phase 03 outputs**

  Review the diff to confirm Phase 03 changed only allowed template files and `CHANGELOG.md`.

  Commit with message:

  ```text
  Complete Phase 03 template slimming
  ```

## Tests and validation

| Command | Expected result |
|---|---|
| `git status --short --branch` | Shows branch `refactor-as-code`; before the Phase 03 execution commit, only allowed Phase 03 files are modified or staged. |
| `rg -n "schema:(spec\\.small-medium|plan\\.small-medium|spec\\.large-phased|plan\\.phase|plan\\.amendment|variance-log)" .agents/skills/dev-doc-harness/assets/templates` | Outputs matches for all six template schema IDs. |
| `rg -n "rule:(models\\.strategy-required|models\\.context-strategy|models\\.approved-strategy-authorized|models\\.fresh-confirmation|lifecycle\\.variance-policy|freeze\\.draft-review|freeze\\.approval-freeze|freeze\\.stop-before-implementation|freeze\\.multi-gate-flow|quality\\.phase-plan-fresh-thread|quality\\.spec-handoff|lifecycle\\.documentation-matrix)" .agents/skills/dev-doc-harness/assets/templates` | Outputs matches proving templates cite safety-critical canonical rule IDs. |
| `rg -n "After this .*approved, frozen, and followed|Fresh confirmation is still required|Long-running .*more than 3 total sub-agents|Context strategy must say how|Before approval, operator feedback edits this draft directly|When this .*ready for operator review, follow" .agents/skills/dev-doc-harness/assets/templates` | No output. Exit code may be `1` because `rg` found no matches. These long reusable policy phrases should be replaced by compact citations. |
| `rg -n "Status:[ ]Draft|T[D]B|T[O]DO|R[e]place|blank[ ]unless|unresolved[ ]decision" .agents/skills/dev-doc-harness/assets/templates` | Outputs only intentional template status or replacement prompts if they are retained as artifact-shape placeholders. Review each match manually and record the result in the handoff. |
| `git diff --name-only -- .agents/skills/dev-doc-harness/SKILL.md README.md AGENTS.md .agents/skills/dev-doc-harness/references docs/work-items` | No output unless an approved amendment permits changing one of these paths. |
| `git diff --name-only` | Before staging for the Phase 03 execution commit, includes only `CHANGELOG.md` and allowed files under `.agents/skills/dev-doc-harness/assets/templates/`, unless an approved amendment permits more. |

## Documentation tasks

- Update `CHANGELOG.md` before the Phase 03 execution commit.
- Do not update `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`; it is a frozen Phase 01 snapshot.
- Update `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md` only if Phase 03 execution departs from this approved plan. Because this file is under ignored `docs/work-items/`, force-add it only when a variance entry is actually required and approved by the phase scope.
- Do not create `deltas/operator-manual.delta.md`, `deltas/architecture-summary.delta.md`, or `snapshots/test-cases.snapshot.md` in Phase 03. Those remain deferred to Phase 04 or Phase 05 by the approved anchor spec.
- Do not rewrite frozen historical work-item artifacts to consume slimmed templates.

## Variance rules

Before approval, operator feedback edits this draft directly and does not require an amendment. After the approval commit or explicit handoff snapshot, this phase plan is immutable.

During Phase 03 implementation, record nontrivial local technical variance in `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`. Create a plan amendment named `plan-amendment-NNN-short-title-refactor-as-code.md` and request operator approval before proceeding when post-freeze variance affects architecture, public interfaces, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

For draft review, stage only this phase plan with `git add -f docs/work-items/2026-06-05-refactor-as-code/plan-phase-03-template-slimming-refactor-as-code.md`, then ask the operator to approve the staged draft or provide feedback. Do not commit before explicit approval.

After explicit approval, update `CHANGELOG.md`, verify the approved plan has no unresolved required items, stage only this phase plan and `CHANGELOG.md`, commit the approved planning package, and stop before implementation. Report the commit hash and approved artifact path, remind the operator they may push and create a draft plan-only PR, and ask the operator to confirm model, reasoning-effort, and sub-agent policy choices plus whether Phase 03 implementation should begin.

## Handoff output

At Phase 03 completion, the implementing agent must report:

- Assigned scope.
- Files inspected.
- Files changed.
- Commands and validation results.
- Schema IDs and policy citations added to each template.
- Reusable policy blocks removed or reduced, grouped by sub-agent authorization, variance handling, and freeze-gate procedure.
- Fresh-thread usability review result.
- Confirmation that `SKILL.md`, `README.md`, root `AGENTS.md`, canonical references, and frozen historical work-item artifacts were not modified, or an approved amendment reference if any were modified.
- Any variance entries or a statement that no variance occurred.
- Sub-agent use, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.
- Residual risks and recommended Phase 04 action.

## Completion criteria

- Phase objective is met.
- All six current templates declare compact schema IDs or equivalent policy-reference anchors.
- Templates cite canonical module or rule IDs for reusable sub-agent, variance, freeze-gate, lifecycle, and quality policy.
- Long reusable sub-agent authorization, variance handling, and freeze-gate procedure blocks are removed or reduced to compact citations plus artifact-shape prompts.
- Fresh-thread usability remains intact for small/medium specs, small/medium plans, large/phased specs, phase plans, amendments, and variance logs.
- Validation commands have been run and recorded.
- `CHANGELOG.md` has a newest-first entry for Phase 03 before the execution commit.
- Variance log is present and current.
- No `SKILL.md`, `README.md`, root `AGENTS.md`, canonical reference, or frozen historical artifact changes occur without an approved amendment.
- De-facto sub-agent use is reported when applicable.
