# Phase 02: Canonical Modules Plan

Work ID: `2026-06-05-refactor-as-code`
Short ID: `refactor-as-code`
Status: Approved

## Objective

Make canonical policy ownership real before templates, the public entrypoint, README, or root instructions are updated. Phase 02 creates a compact canonical ownership and rule-interface reference, then annotates existing canonical references with stable module and rule IDs so later phases can cite owners instead of copying policy prose.

Phase 02 must preserve existing harness behavior. It should not slim templates, update root `AGENTS.md`, update `README.md`, or rewrite frozen historical work-item artifacts.

## Input context

The implementing agent must read these approved artifacts and references before editing:

- `docs/work-items/2026-06-05-refactor-as-code/spec-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-amendment-001-architecture-guardrails-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`
- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
- `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
- `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`
- `AGENTS.md`
- `README.md`

Preserve all approved Phase 01 architecture decisions: canonical references own reusable policy, templates and README do not; rule IDs are stable retrieval anchors rather than a complete versioning system; historical artifacts are not migration targets; and Phase 02 should favor the smallest change that makes ownership, retrieval, and later template slimming safe.

## Likely files and areas

Create:

- `.agents/skills/dev-doc-harness/references/policy-architecture.md`

Modify during Phase 02 execution:

- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
- `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
- `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`
- `CHANGELOG.md`

Do not modify in Phase 02 unless an approved amendment changes the phase boundary:

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/assets/templates/`
- `README.md`
- root `AGENTS.md`
- frozen historical work-item artifacts under `docs/work-items/`

## Model and Sub-agent Strategy

Current orchestration: Codex in this desktop thread; exact model/profile and reasoning effort are not exposed in repository artifacts.
Fit assessment: Phase 02 touches canonical policy references and creates the stable rule interface used by later template and router phases. The work is mostly textual, but mistakes have high downstream process risk because a bad ownership map can preserve duplication or weaken freeze, variance, changelog, or sub-agent rules.
Recommended change: Use the repository default `economy-default` policy unless the operator explicitly changes it. Apply strongest available reasoning in the orchestration thread for final architecture review because Phase 02 is high-blast-radius policy architecture work.

Sub-agents: None. The edits are tightly coupled across shared reference files, and this runtime may restrict spawning unless the operator explicitly requests delegation. The orchestration thread should perform the final architecture review and record any model or sub-agent limitation in the Phase 02 handoff.

## Tasks

- [ ] **Step 1: Verify clean starting state**

  Run `git status --short --branch`.

  Expected: current branch is `refactor-as-code`; no unrelated staged or unstaged files are present.

- [ ] **Step 2: Re-read approved architecture inputs**

  Read the approved spec, amendment, Phase 01 architecture snapshot, and variance log listed in `## Input context`.

  Capture these Phase 02 constraints in working notes before editing: no template slimming, no entrypoint/router update, no README/root instruction update, no frozen historical artifact rewrite, rule versioning remains deferred, and the default active model policy remains `economy-default` unless the operator changes it.

- [ ] **Step 3: Inventory current reference ownership and repeated policy prose**

  Run:

  ```powershell
  rg --files .agents/skills/dev-doc-harness AGENTS.md README.md docs/work-items/2026-06-05-refactor-as-code
  rg -n "canonical source|only source|Do not|must|Before approval|After .*approved|Context strategy must|Fresh confirmation|Planning artifact freeze gate|immutable snapshots|variance|CHANGELOG|Superpowers compatibility" .agents/skills/dev-doc-harness AGENTS.md README.md
  ```

  Use the output to confirm current policy owners and to identify copied policy blocks that Phase 03 should remove from templates after Phase 02 creates stable references.

- [ ] **Step 4: Create the canonical policy architecture reference**

  Create `.agents/skills/dev-doc-harness/references/policy-architecture.md`.

  Required sections:

  ```md
  # Policy Architecture

  ## Purpose

  ## Content Types

  ## Canonical Module Catalog

  ## Rule ID Conventions

  ## Dependency Direction

  ## Router Inputs

  ## Versioning Status
  ```

  The file must be concise and must cite `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md` as the Phase 01 design source. It must not replace the detailed canonical rule owners in existing references.

- [ ] **Step 5: Define content types in the new reference**

  In `## Content Types`, define these content types from the Phase 01 snapshot in compact canonical form:

  - Normative policy.
  - Artifact schema.
  - Example.
  - Advisory guidance.
  - Operator-facing summary.
  - Historical snapshot.

  Each definition must state whether the type can be cited as reusable policy. Keep this section short enough that templates can link to it without copying the full Phase 01 snapshot.

- [ ] **Step 6: Define the canonical module catalog**

  In `## Canonical Module Catalog`, create a table with these module IDs, owner files, content type, and owned rule families:

  - `module:architecture` owned by `references/policy-architecture.md`.
  - `module:lifecycle` owned by `references/artifact-contract.md`.
  - `module:freeze-gate` owned by `references/planning-freeze-gates.md`.
  - `module:models` owned by `references/subagent-model-policy.md`.
  - `module:quality` owned by `references/durable-planning-quality.md`.
  - `module:execution-quality` owned by `references/context-and-quality-gates.md`.
  - `module:evidence` owned by `references/evidence-and-report-artifacts.md`.
  - `module:role-examples` owned by `references/subagent-role-examples.md`.

  The catalog must state that `module:evidence` and `module:role-examples` are supplemental or advisory unless a plan explicitly invokes them.

- [ ] **Step 7: Define rule ID conventions and dependency direction**

  In `## Rule ID Conventions`, record the Phase 01 shape:

  ```text
  module:<area>
  rule:<area>.<short-name>
  schema:<artifact>.<short-name>
  scenario:<area>.<short-name>
  metric:<area>.<short-name>
  ```

  State that IDs are stable anchors, not full semantic versions.

  In `## Dependency Direction`, record the allowed reference direction from the Phase 01 snapshot. Include the explicit bans that canonical references do not depend on README summaries or templates for policy meaning, templates do not own long reusable policy, and historical artifacts are not updated to mimic current policy.

- [ ] **Step 8: Add module and rule IDs to `artifact-contract.md`**

  Add a compact ownership block near the top of `artifact-contract.md` for `module:lifecycle`.

  The block must list these rule IDs and their local section owners:

  - `rule:lifecycle.work-item-folders`
  - `rule:lifecycle.short-artifact-id`
  - `rule:lifecycle.work-sizing`
  - `rule:lifecycle.large-anchor-spec`
  - `rule:lifecycle.superpowers-compatibility`
  - `rule:lifecycle.immutable-snapshots`
  - `rule:lifecycle.documentation-matrix`
  - `rule:lifecycle.variance-policy`
  - `rule:lifecycle.changelog-before-commit`

  Keep the existing prose intact except for narrow wording needed to avoid duplicate ownership confusion.

- [ ] **Step 9: Add module and rule IDs to `planning-freeze-gates.md`**

  Add a compact ownership block near the top for `module:freeze-gate`.

  The block must list:

  - `rule:freeze.draft-review`
  - `rule:freeze.approval-freeze`
  - `rule:freeze.stop-before-implementation`
  - `rule:freeze.multi-gate-flow`
  - `rule:freeze.compatibility`

  Keep `planning-freeze-gates.md` as the only detailed owner of freeze-gate procedure.

- [ ] **Step 10: Add module and rule IDs to model and quality references**

  In `subagent-model-policy.md`, add `module:models` and these rule IDs:

  - `rule:models.strategy-required`
  - `rule:models.context-strategy`
  - `rule:models.approved-strategy-authorized`
  - `rule:models.fresh-confirmation`
  - `rule:models.concurrent-cap`
  - `rule:models.enterprise-default`
  - `rule:models.economy-default`
  - `rule:models.final-review`
  - `rule:models.final-integration-ownership`

  In `durable-planning-quality.md`, add `module:quality` and these rule IDs:

  - `rule:quality.spec-handoff`
  - `rule:quality.phase-plan-fresh-thread`
  - `rule:quality.handoff-preservation`

  Do not move model policy into templates or into `policy-architecture.md`.

- [ ] **Step 11: Add module IDs to supplemental references**

  In `context-and-quality-gates.md`, add `module:execution-quality` with rule IDs for context load order, task preflight, environment compensation, and increment quality gate.

  In `evidence-and-report-artifacts.md`, add `module:evidence` and label it supplemental. Include rule IDs for evidence preservation, report sections, and evidence stop conditions.

  In `subagent-role-examples.md`, add `module:role-examples` and label it advisory example content. Do not make role examples mandatory policy.

- [ ] **Step 12: Review whether `artifact-contract.md` should be split now**

  Compare the edited `artifact-contract.md` against the Phase 01 metrics:

  - If the ownership block makes lifecycle rule families discoverable without increasing traversal depth, keep the file intact for Phase 02.
  - If a split is still necessary for safety or clarity, stop and create an amendment because this plan chooses the lower-churn ownership-map approach.

  Record the no-split decision in the Phase 02 handoff.

- [ ] **Step 13: Update changelog for Phase 02 execution**

  Before the Phase 02 execution commit, add a newest-first `CHANGELOG.md` entry titled `2026-06-05-refactor-as-code: complete Phase 02 canonical modules`.

  The entry must mention the new policy architecture reference, canonical module catalog, stable rule IDs, supplemental/advisory labels, and the decision not to split `artifact-contract.md` in Phase 02 unless an approved amendment changes the plan.

- [ ] **Step 14: Run validation commands**

  Run every command in `## Tests and validation` and record the result in the Phase 02 completion handoff.

- [ ] **Step 15: Final architecture review**

  Perform a high-reasoning review in the orchestration thread. Check:

  - Every reusable rule family named by Phase 01 has exactly one detailed owner.
  - New module and rule IDs match the Phase 01 naming conventions.
  - Supplemental and advisory references are labeled so examples do not become competing policy.
  - No templates, README, root `AGENTS.md`, or frozen historical work-item artifacts changed.
  - Freeze gate, variance, changelog, immutable snapshot, Superpowers compatibility, and model/sub-agent policy remain discoverable.

  If review finds a high-impact architecture or scope issue, stop and draft an amendment instead of committing Phase 02 implementation.

- [ ] **Step 16: Commit Phase 02 outputs**

  Review the diff to confirm Phase 02 changed only the allowed canonical references and `CHANGELOG.md`.

  Commit with message:

  ```text
  Complete Phase 02 canonical modules
  ```

## Tests and validation

| Command | Expected result |
|---|---|
| `git status --short --branch` | Shows branch `refactor-as-code`; before the Phase 02 execution commit, only allowed Phase 02 files are modified or staged. |
| `Test-Path .agents/skills/dev-doc-harness/references/policy-architecture.md` | Outputs `True`. |
| `rg -n "module:(architecture|lifecycle|freeze-gate|models|quality|execution-quality|evidence|role-examples)" .agents/skills/dev-doc-harness/references/policy-architecture.md` | Outputs matches for every listed module ID. |
| `rg -n "rule:(lifecycle\\.immutable-snapshots|lifecycle\\.variance-policy|lifecycle\\.changelog-before-commit|freeze\\.stop-before-implementation|models\\.approved-strategy-authorized|models\\.fresh-confirmation|quality\\.phase-plan-fresh-thread)" .agents/skills/dev-doc-harness/references` | Outputs matches proving safety-critical rule IDs exist in canonical references. |
| `rg -n "module:(lifecycle|freeze-gate|models|quality|execution-quality|evidence|role-examples)" .agents/skills/dev-doc-harness/references` | Outputs matches proving each current reference declares its module. |
| `rg -n "Status:[ ]Draft|T[D]B|T[O]DO|R[e]place|blank[ ]unless|unresolved[ ]decision" .agents/skills/dev-doc-harness/references/policy-architecture.md .agents/skills/dev-doc-harness/references/artifact-contract.md .agents/skills/dev-doc-harness/references/planning-freeze-gates.md .agents/skills/dev-doc-harness/references/subagent-model-policy.md .agents/skills/dev-doc-harness/references/durable-planning-quality.md .agents/skills/dev-doc-harness/references/context-and-quality-gates.md .agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md .agents/skills/dev-doc-harness/references/subagent-role-examples.md` | No output. Exit code may be `1` because `rg` found no matches. |
| `git diff --name-only -- .agents/skills/dev-doc-harness/assets/templates README.md AGENTS.md docs/work-items` | No output unless `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md` records a justified Phase 02 variance. |
| `git diff --name-only` | Before staging, includes only `CHANGELOG.md` and allowed files under `.agents/skills/dev-doc-harness/references/`, unless an approved amendment permits more. |

## Documentation tasks

- Update `CHANGELOG.md` before the Phase 02 execution commit.
- Do not update `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`; it is a frozen Phase 01 snapshot.
- Update `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md` only if Phase 02 execution departs from this approved plan.
- Do not create `deltas/operator-manual.delta.md`, `deltas/architecture-summary.delta.md`, or `snapshots/test-cases.snapshot.md` in Phase 02. Those remain deferred to later phases in the approved anchor spec.

## Variance reminder

Before approval, operator feedback edits this draft directly and does not require an amendment. After the approval commit or explicit handoff snapshot, approved phase plans are immutable snapshots. Record nontrivial variance in `implementation-notes/variance-log.md`. Create a plan amendment named `plan-amendment-NNN-short-title-refactor-as-code.md` and request operator approval before proceeding when post-freeze variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

When this phase plan is ready for operator review, follow `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage the draft without committing, request approval or feedback, revise directly on feedback, and commit only after explicit approval.

After the approval commit, use the canonical post-freeze prompt to confirm model, reasoning-effort, and sub-agent policy choices and ask whether Phase 02 execution should begin now.

## Handoff output

At Phase 02 completion, the implementing agent must report:

- Assigned scope.
- Files inspected.
- Files changed.
- Commands and validation results.
- Final module catalog and rule-owner decisions.
- Whether `artifact-contract.md` was kept intact or split, with rationale.
- Any variance entries or a statement that no variance occurred.
- Sub-agent use, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.
- Residual risks and recommended next phase action.

## Completion criteria

- Phase objective is met.
- `references/policy-architecture.md` exists and defines content types, module catalog, rule ID conventions, dependency direction, router inputs, and versioning status.
- Current canonical references declare their module IDs and safety-critical rule IDs.
- Detailed rule ownership remains in canonical references rather than templates, README, or work-item artifacts.
- Validation commands have been run and recorded.
- `CHANGELOG.md` has a newest-first entry for Phase 02 before the execution commit.
- Variance log is present and current.
- No templates, README, root `AGENTS.md`, or frozen historical work-item artifacts are modified.
- De-facto sub-agent use is reported when applicable.
