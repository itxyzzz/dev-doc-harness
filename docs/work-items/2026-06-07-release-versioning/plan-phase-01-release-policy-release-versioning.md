# Phase 01: Release Policy Architecture Plan

Work ID: `2026-06-07-release-versioning`
Short ID: `release-versioning`
Status: Approved
Schema: `schema:plan.phase`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:architecture`, `module:freeze-gate`, `rule:quality.phase-plan-fresh-thread`, `rule:models.strategy-required`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Objective

Define the `0.3` release policy architecture before changing current harness package files. Phase 01 produces a frozen architecture snapshot that later phases use to implement package-local release identity, release notes, changelog schema changes, validation, and minimal team adoption guidance.

## Input context

The implementing agent must read these approved artifacts first:

- `docs/work-items/2026-06-07-release-versioning/spec-release-versioning.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/SKILL.md`
- `AGENTS.md`
- `README.md`
- `CHANGELOG.md`

Then inspect these current package consumers and validation surfaces:

- `.agents/skills/dev-doc-harness/assets/templates/`
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`
- `TODO.md`
- Existing release-versioning work-item files under `docs/work-items/2026-06-07-release-versioning/`

Preserve the approved spec decisions: `0.3` uses harness-level release identity, the distributable package is root `AGENTS.md` plus `.agents/`, release notes live inside `.agents/`, root `CHANGELOG.md` is the source material, downstream project `docs/work-items/` stays project-local, no `0.1` migration is required, and full per-rule semantic versioning stays out of scope.

## Likely files and areas

Create during Phase 01 execution:

- `docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-06-07-release-versioning/implementation-notes/variance-log.md`

Modify during Phase 01 execution:

- `CHANGELOG.md`

Do not modify current distributable package files in Phase 01, including root `AGENTS.md`, `.agents/`, current templates, validation scripts, or package-local release notes. Those changes belong to Phase 02 or Phase 03 after the architecture snapshot is frozen.

## Model and Sub-agent Strategy

Current orchestration: Codex desktop thread; exact model/profile and reasoning effort are not exposed in repository artifacts. Operator authorized Phase 01 planning with `proceed` after the approved anchor-spec freeze.
Fit assessment: Medium-to-high process risk and moderate ambiguity. The phase is documentation architecture, but mistakes would affect cross-repository team adoption and future release compatibility.
Recommended change: None for the orchestration thread. Use careful main-thread review for Phase 01; reserve a stronger final review for Phase 03 release hardening if package authority or validation behavior becomes subtle.

Sub-agents: None for Phase 01. The phase has one tightly coupled architecture artifact, and coordination overhead would exceed the value. Record any uncertainty directly in the architecture snapshot's open risks.

## Tasks

- [ ] **Step 1: Verify clean starting state**

  Run `git status --short --branch`.

  Expected: current branch is `versioning`; no unrelated staged or unstaged files are present.

- [ ] **Step 2: Re-read approved planning inputs**

  Read `spec-release-versioning.md` and the current harness routing and architecture references.

  Capture these non-negotiable Phase 01 outputs before writing the snapshot: release identity, package boundary, changelog-to-release-note contract, release compatibility model, adoption flow, rollback flow, artifact release-stamping decision, validation direction, Phase 02 inputs, and open risks.

- [ ] **Step 3: Inventory current release and package surfaces**

  Run:

  ```powershell
  rg -n "release|version|0\.2|0\.3|VERSION|distributable|package|CHANGELOG|docs/work-items|module:release|rule:release" AGENTS.md README.md CHANGELOG.md TODO.md .agents docs/work-items
  rg --files AGENTS.md .agents README.md CHANGELOG.md TODO.md docs/work-items
  ```

  Use the output to confirm current release/versioning deferral, current copy/install guidance, package contents, changelog shape, and existing governance TODOs.

- [ ] **Step 4: Create the architecture snapshot skeleton**

  Create `docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md` with these headings:

  ```md
  # Release Versioning Architecture Snapshot

  Work ID: `2026-06-07-release-versioning`
  Source spec: `../spec-release-versioning.md`
  Status: In progress

  ## Goal

  ## Release Identity Model

  ## Distributable Package Boundary

  ## Changelog To Release Notes Contract

  ## Changelog Go-Forward Schema

  ## Release Notes Location And Shape

  ## Rule And Schema Compatibility Model

  ## Work-Item Artifact Release Context

  ## Team Adoption And Rollback Flow

  ## Validation Direction

  ## Phase 02 Inputs

  ## Open Risks
  ```

- [ ] **Step 5: Define release identity model**

  In `## Release Identity Model`, decide the package-local release marker path and format.

  The preferred baseline is `.agents/skills/dev-doc-harness/VERSION` with plain text `0.3.0`, unless Phase 01 discovers a concrete reason to use a tiny manifest instead.

  Record that harness release versions are the compatibility unit for team adoption; `module:*`, `rule:*`, and `schema:*` IDs remain stable unversioned anchors.

- [ ] **Step 6: Define distributable package boundary**

  In `## Distributable Package Boundary`, define the package as exactly root `AGENTS.md` plus `.agents/`.

  Explicitly list excluded repository files:

  - root `README.md`
  - root `CHANGELOG.md`
  - root `TODO.md`
  - this repository's `docs/work-items/`
  - `.git/`
  - local development files

  Record that release notes and any package-local release policy must live under `.agents/skills/dev-doc-harness/` because they must travel with the package.

- [ ] **Step 7: Define changelog-to-release-notes contract**

  In `## Changelog To Release Notes Contract`, define `CHANGELOG.md` as the repository source material for release notes.

  Require release notes to cite or summarize relevant changelog sections and prohibit independent release-note-only histories. Keep the process manual or checklist-based for `0.3` unless a tiny script is clearly lower maintenance.

  Define aggregation behavior: multiple changelog entries for the same feature or work item, such as approved spec, approved plan, and implementation entries, are release-note source evidence but should not become separate release-note bullets by default. Release notes should summarize the delivered operator-facing or package-facing change once, with planning entries referenced only when they matter for audit, migration, or compatibility.

- [ ] **Step 8: Define changelog go-forward schema**

  In `## Changelog Go-Forward Schema`, define a low-friction entry format that supports release-note assembly.

  Include at least:

  - Work ID and short title in the heading.
  - Release target when known, such as `Release target: 0.3.0`.
  - Package impact, such as `Package impact: distributable / repository-only / planning-only`.
  - Release-note relevance, such as `Release-note: include / source-only / omit`.
  - Normal Keep a Changelog subsections.
  - Concise bullets that name user/operator impact or internal maintenance impact.

  Decide how much, if any, of the existing top-of-file changelog should be normalized during Phase 02.

- [ ] **Step 9: Define release notes location and shape**

  In `## Release Notes Location And Shape`, choose the package-local path and required sections.

  Preferred path:

  ```text
  .agents/skills/dev-doc-harness/docs/releases/0.3.0.md
  ```

  Required sections should stay short and release-facing:

  - Release.
  - Package contents.
  - Added.
  - Changed.
  - Compatibility.
  - Team adoption.
  - Rollback.
  - Source changelog entries.

  Record that source changelog entries may include planning approval entries, but release notes should group them under the delivered change rather than presenting spec, plan, and implementation as separate release features.

- [ ] **Step 10: Define rule and schema compatibility model**

  In `## Rule And Schema Compatibility Model`, replace the broad rule-versioning deferral with a concrete `0.3` compatibility stance:

  - Harness release versions carry compatibility meaning.
  - Rule and schema IDs stay unversioned.
  - Compatible clarifications update the current owner and release notes.
  - Incompatible replacements use `Superseded by:` or replacement notes in the canonical owner.
  - Frozen historical artifacts are not rewritten only to update rule IDs.
  - Current safety-critical policy wins for future execution unless a frozen artifact records an explicit compatible approved exception.

- [ ] **Step 11: Decide work-item artifact release context**

  In `## Work-Item Artifact Release Context`, decide whether templates should add `Harness release` only, `Minimum harness release`, both, or neither for `0.3`.

  Prefer the smallest field set that helps future agents interpret artifacts without making every template header noisy. If release stamping is adopted, specify exact template header wording for Phase 02 or Phase 03.

- [ ] **Step 12: Define team adoption and rollback flow**

  In `## Team Adoption And Rollback Flow`, define the minimum team workflow:

  - Copy root `AGENTS.md` and `.agents/` from the release.
  - Merge repository-specific `AGENTS.md` content carefully.
  - Run the harness validation command when practical.
  - Commit or PR the harness update separately.
  - Do not copy this repository's `docs/work-items/` into a project.
  - Roll back by reverting the dedicated harness update commit or PR.

- [ ] **Step 13: Define validation direction**

  In `## Validation Direction`, define which checks Phase 03 should add or update:

  - Package-local `VERSION` exists and equals `0.3.0`.
  - Package-local release notes for `0.3.0` exist.
  - Release notes include a source-changelog section.
  - Current changelog entries for release-versioning follow the go-forward schema.
  - Package-boundary docs say downstream projects copy `AGENTS.md` and `.agents/`, not this repository's `docs/work-items/`.
  - Existing graph and golden traversal validation still pass.

  Keep release-note/changelog sync validation checklist-based if robust parsing would be excessive.

- [ ] **Step 14: Fill Phase 02 inputs and open risks**

  In `## Phase 02 Inputs`, list exact decisions Phase 02 must consume before touching package files.

  In `## Open Risks`, list remaining decisions or hazards. If any risk changes release scope, package boundary, validation feasibility, or acceptance criteria, stop and propose an amendment instead of continuing.

  When the snapshot is complete, change `Status: In progress` to `Status: Final`.

- [ ] **Step 15: Create or update the variance log**

  Create `docs/work-items/2026-06-07-release-versioning/implementation-notes/variance-log.md` with initial content:

  ```md
  # Variance Log

  Work ID: `2026-06-07-release-versioning`

  ## Entries

  No variance recorded yet.
  ```

- [ ] **Step 16: Update changelog before commit**

  Add a newest-first `CHANGELOG.md` entry for Phase 01 implementation. The entry should mention the release policy architecture snapshot, package boundary, changelog-to-release-note contract, and `0.3` compatibility model.

- [ ] **Step 17: Validate and self-review**

  Run the validation commands listed below.

  Review the architecture snapshot for missing required sections, unresolved decisions, and accidental implementation instructions for later phases.

## Tests and validation

| Command | Expected result |
|---|---|
| `git status --short --branch` | Shows branch `versioning`; before implementation commit, only Phase 01 scoped files and `CHANGELOG.md` are changed. |
| `rg -n "## (Release Identity Model|Distributable Package Boundary|Changelog To Release Notes Contract|Changelog Go-Forward Schema|Release Notes Location And Shape|Rule And Schema Compatibility Model|Work-Item Artifact Release Context|Team Adoption And Rollback Flow|Validation Direction|Phase 02 Inputs|Open Risks)" docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md` | Outputs one match for each required architecture snapshot section. |
| `rg -n "0\\.3\\.0|AGENTS.md.*\\.agents|CHANGELOG.md|docs/work-items|Superseded by|VERSION" docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md` | Outputs matches proving the snapshot records release identity, package boundary, changelog source, work-item exclusion, replacement notes, and release marker decision. |
| `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Outputs all current PASS lines. |

## Documentation tasks

- Create `snapshots/architecture.snapshot.md`.
- Create or update `implementation-notes/variance-log.md`.
- Update `CHANGELOG.md` before the Phase 01 implementation commit.
- Do not create release notes, testing-guide delta, operator-manual delta, or architecture-summary delta in Phase 01 unless an approved amendment changes scope.

## Variance reminder

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

For this work item, changes to release package boundary, release-note source-of-truth, full per-rule versioning scope, migration scope from `0.1`, validation feasibility, active model-policy selection, or planning freeze behavior are high-impact and require amendment approval.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this phase plan.

## Handoff output

At Phase 01 completion, report:

- Scope completed.
- Files created or changed.
- Commands and validation run.
- Final release policy decisions.
- Whether any variance occurred.
- Open risks for Phase 02.
- Recommended next step.

## Completion criteria

- `snapshots/architecture.snapshot.md` defines release identity, package boundary, changelog-to-release-note contract, changelog schema, release-note shape, rule/schema compatibility model, work-item release context, team adoption and rollback flow, validation direction, Phase 02 inputs, and open risks.
- `implementation-notes/variance-log.md` exists and is current.
- `CHANGELOG.md` has a newest-first Phase 01 implementation entry before commit.
- Validation commands have been run and recorded.
- No current distributable package files are changed in Phase 01.
- No full per-rule semantic versioning, package manager, installer, generated release pipeline, or `0.1` migration guidance is introduced.
