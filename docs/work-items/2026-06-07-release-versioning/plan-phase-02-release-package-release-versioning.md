# Phase 02: Release Package Implementation Plan

> For agentic workers: use `dev-doc-harness` for repository artifact lifecycle and use `superpowers:executing-plans` or equivalent stepwise execution to implement this approved phase plan task-by-task. Steps use checkbox syntax for tracking.

Work ID: `2026-06-07-release-versioning`
Short ID: `release-versioning`
Status: Approved
Schema: `schema:plan.phase`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:architecture`, `module:freeze-gate`, `rule:quality.phase-plan-fresh-thread`, `rule:models.strategy-required`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Objective

Implement the `0.3.0` package-local release identity, release policy owner, release notes, changelog schema normalization, template release stamping, and operator-facing package guidance defined by the Phase 01 architecture snapshot.

Phase 02 changes current package files and repository documentation, but it does not add the full Phase 03 validation hardening. The implementation must keep the distributable package simple: root `AGENTS.md` plus `.agents/`.

## Input context

The implementing agent must read these approved artifacts first:

- `docs/work-items/2026-06-07-release-versioning/spec-release-versioning.md`
- `docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-06-07-release-versioning/implementation-notes/variance-log.md`
- `docs/work-items/2026-06-07-release-versioning/plan-phase-02-release-package-release-versioning.md`

Then read the current harness entrypoints, canonical references, templates, release-facing docs, and validation script:

- `AGENTS.md`
- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
- `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`
- `README.md`
- `CHANGELOG.md`

Preserve these Phase 01 decisions:

- Package-local release marker is `.agents/skills/dev-doc-harness/VERSION` with plain text `0.3.0`.
- Package-local release notes are `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`.
- Root `CHANGELOG.md` is source material for release notes.
- Release notes summarize delivered package-facing changes once; spec, plan, and implementation changelog entries for the same feature are source evidence, not separate release-note features by default.
- The distributable package is exactly root `AGENTS.md` plus `.agents/`.
- This repository's `docs/work-items/` must not be copied into downstream projects.
- Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned anchors; harness release versions carry compatibility meaning.
- New templates should add only `Harness release: <version or unknown>`, not both `Harness release` and `Minimum harness release`.
- Do not introduce full per-rule semver, a package manager, an installer, a generated release pipeline, or `0.1` migration guidance.

## Likely files and areas

Create:

- `.agents/skills/dev-doc-harness/VERSION`
- `.agents/skills/dev-doc-harness/references/release-policy.md`
- `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`
- `docs/work-items/2026-06-07-release-versioning/deltas/operator-manual.delta.md`
- `docs/work-items/2026-06-07-release-versioning/deltas/architecture-summary.delta.md`

Modify:

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
- `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`
- `README.md`
- `CHANGELOG.md`

Do not modify in Phase 02 unless an approved amendment changes scope:

- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`
- `AGENTS.md`
- frozen approved specs, phase plans, snapshots, or amendments
- this repository's historical work-item artifacts outside `docs/work-items/2026-06-07-release-versioning/`

## Model and Sub-agent Strategy

Current orchestration: Codex desktop thread; exact model/profile is not exposed in repository artifacts. Operator requested Phase 02 planning after Phase 01 implementation commit `085fd15`.
Fit assessment: Moderate-to-high process risk because Phase 02 changes the distributable package and team adoption semantics. The implementation is documentation and template work with no runtime code, but subtle duplication or source-of-truth mistakes could spread across repositories.
Recommended change: Use current orchestration for implementation. Use careful main-thread validation. Reserve stronger final review for Phase 03 release hardening, unless Phase 02 implementation unexpectedly changes validation behavior or package authority.

Sub-agents: None for Phase 02. The touched files are closely coupled around one release contract, and concurrent edits would increase coordination risk. If the implementing environment provides cheap review sub-agents and the operator explicitly authorizes one, use at most one read-only reviewer after implementation with curated artifacts: the Phase 01 snapshot, the Phase 02 diff, release notes, and validation output.

## Tasks

- [ ] **Step 1: Verify clean starting state**

  Run:

  ```powershell
  git status --short --branch
  git log --oneline --decorate --max-count=3
  ```

  Expected: branch is `versioning`; worktree is clean; recent history includes `085fd15 Complete release versioning phase 01 architecture`.

- [ ] **Step 2: Re-read approved Phase 02 inputs**

  Read the input context files listed above. Confirm the Phase 01 architecture snapshot is `Status: Final`, the variance log says no variance is recorded yet, and this Phase 02 plan is the approved implementation plan.

- [ ] **Step 3: Create package-local release marker**

  Create `.agents/skills/dev-doc-harness/VERSION` with exactly:

  ```text
  0.3.0
  ```

  Keep the file plain text. Do not add a manifest in Phase 02.

- [ ] **Step 4: Create package-local release policy owner**

  Create `.agents/skills/dev-doc-harness/references/release-policy.md`.

  The file must own `module:release` and define these rule IDs in an owner table:

  - `rule:release.identity`
  - `rule:release.package-boundary`
  - `rule:release.changelog-source`
  - `rule:release.release-notes`
  - `rule:release.compatibility`
  - `rule:release.artifact-context`
  - `rule:release.team-adoption`

  Use this section shape:

  ```md
  # Release Policy

  Module: `module:release`

  Owned rule IDs:

  | Rule ID | Local owner |
  |---|---|
  | `rule:release.identity` | `## Release Identity` |
  | `rule:release.package-boundary` | `## Distributable Package Boundary` |
  | `rule:release.changelog-source` | `## Changelog As Release Source` |
  | `rule:release.release-notes` | `## Release Notes` |
  | `rule:release.compatibility` | `## Compatibility Model` |
  | `rule:release.artifact-context` | `## Work-Item Artifact Release Context` |
  | `rule:release.team-adoption` | `## Team Adoption And Rollback` |

  ## Release Identity

  The package-local release marker is `.agents/skills/dev-doc-harness/VERSION`.
  For this release it contains `0.3.0`.

  ## Distributable Package Boundary

  The distributable harness package is root `AGENTS.md` plus `.agents/`.
  It excludes root `README.md`, root `CHANGELOG.md`, root `TODO.md`, this repository's `docs/work-items/`, `.git/`, and local development files.

  ## Changelog As Release Source

  Root `CHANGELOG.md` is the repository source material for package-local release notes.
  Release notes are curated from changelog entries and must not become an independent feature history.

  ## Release Notes

  Release notes live under `.agents/skills/dev-doc-harness/docs/releases/`.
  The `0.3.0` release notes are `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`.

  ## Compatibility Model

  Harness release versions carry compatibility meaning.
  Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned retrieval and ownership anchors.
  Compatible clarifications update the current owner and release notes when relevant.
  Incompatible replacements keep a discoverable replacement note such as `Superseded by:`.
  Frozen historical artifacts are not rewritten only to update rule IDs, schema IDs, or release stamps.

  ## Work-Item Artifact Release Context

  New work-item templates include `Harness release: <version or unknown>`.
  Existing historical work-item artifacts without this field are pre-stamp artifacts and are not rewritten only to add it.

  ## Team Adoption And Rollback

  Team repositories adopt the harness by copying root `AGENTS.md` and `.agents/`, merging local `AGENTS.md` instructions carefully, running validation when practical, and committing the harness update separately from product work.
  Rollback is by reverting the dedicated harness update commit or PR.
  ```

  Keep the release policy concise. Avoid copying the full Phase 01 snapshot into this reusable package file.

- [ ] **Step 5: Route release policy through the skill entrypoint**

  Modify `.agents/skills/dev-doc-harness/SKILL.md`:

  - Add `references/release-policy.md` as the owner for release identity, package boundary, release notes, changelog source, compatibility, artifact release context, and team adoption.
  - Add one operation router row for release/package/adoption work. The required route should include `module:release`; optional route should include `module:architecture` when module ownership changes and `module:lifecycle` when changelog or work-item artifacts change.
  - Keep the existing router budget readable; do not make routine execution routes load release policy unless the operation is release/package/adoption work.

- [ ] **Step 6: Register `module:release` in policy architecture**

  Modify `.agents/skills/dev-doc-harness/references/policy-architecture.md`:

  - Add `module:release` to the canonical module catalog with owner `references/release-policy.md`.
  - Change `module:architecture` owned rule families from "rule versioning status" to "rule ID conventions and module catalog".
  - Replace `## Versioning Status` with a short `## Release Compatibility` section that points to `module:release`.
  - Preserve the current guidance that IDs are retrieval and ownership anchors, not full semantic versions.
  - Preserve the `Superseded by:` replacement-note guidance.

- [ ] **Step 7: Add package-local release notes**

  Create `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` with these sections:

  ```md
  # Dev Doc Harness 0.3.0

  ## Release

  Dev Doc Harness `0.3.0` is the first release with explicit package-local release identity and release notes.

  ## Package Contents

  The distributable package is root `AGENTS.md` plus `.agents/`.
  It does not include this repository's `docs/work-items/`, root `README.md`, root `CHANGELOG.md`, root `TODO.md`, `.git/`, or local development files.

  ## Added

  - Added package-local release identity with `.agents/skills/dev-doc-harness/VERSION`.
  - Added package-local release policy and release notes.
  - Added work-item template release context with `Harness release: <version or unknown>`.

  ## Changed

  - Changed rule and schema compatibility from a broad deferral to a release-level compatibility model.
  - Changed changelog management so current release work records release target, package impact, and release-note relevance.

  ## Compatibility

  Harness release versions carry compatibility meaning.
  Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned anchors.

  ## Team Adoption

  Copy root `AGENTS.md` and `.agents/` into the target repository, merge local `AGENTS.md` instructions carefully, run validation when practical, and commit the harness update separately from product work.

  ## Rollback

  Revert the dedicated harness update commit or PR to restore the previous root `AGENTS.md` and `.agents/` package.

  ## Source Changelog Entries

  - `2026-06-07-release-versioning: approve anchor spec`
  - `2026-06-07-release-versioning: approve Phase 01 release policy plan`
  - `2026-06-07-release-versioning: complete Phase 01 release policy architecture`
  - `2026-06-07-release-versioning: approve Phase 02 release package plan`
  - `2026-06-07-release-versioning: complete Phase 02 release package implementation`
  ```

  During implementation, adjust the source-entry list only to match the actual current changelog headings after approval and before commit. Do not split spec, plan, and implementation into separate release-note features.

- [ ] **Step 8: Add `Harness release` to templates**

  Modify each template header to include:

  ```md
  Harness release: `<version or unknown>`
  ```

  Add the field after `Status:` and before `Schema:` in:

  - `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
  - `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
  - `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
  - `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
  - `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`

  For `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`, add the field after `Work ID:` because the variance template has no `Status:` field.

  Do not add `Minimum harness release` in Phase 02.

- [ ] **Step 9: Update README operator guidance**

  Modify `README.md` as repository-level operator guidance:

  - State that the copyable distributable package is root `AGENTS.md` plus `.agents/`.
  - State that package release identity is recorded in `.agents/skills/dev-doc-harness/VERSION`.
  - State that package-local release notes live under `.agents/skills/dev-doc-harness/docs/releases/`.
  - State that this repository's `docs/work-items/` is harness development history and is not copied into downstream projects.
  - State that downstream teams should commit harness updates separately and roll back by reverting that commit or PR.

  Keep README concise and avoid duplicating long reusable policy from `release-policy.md`.

- [ ] **Step 10: Create documentation deltas for Phase 02**

  Create `docs/work-items/2026-06-07-release-versioning/deltas/operator-manual.delta.md` with:

  - Package boundary summary.
  - Team adoption flow.
  - Rollback flow.
  - Note that package-local release notes come from `CHANGELOG.md`.

  Create `docs/work-items/2026-06-07-release-versioning/deltas/architecture-summary.delta.md` with:

  - Release identity model.
  - `module:release` ownership.
  - Compatibility model summary.
  - Template `Harness release` field.
  - Phase 03 validation follow-up.

- [ ] **Step 11: Normalize current release-versioning changelog entries**

  Modify only the current `2026-06-07-release-versioning` changelog entries near the top of `CHANGELOG.md` so each includes:

  ```md
  Release target: `0.3.0`
  Package impact: `<distributable | repository-only | planning-only>`
  Release-note: `<include | source-only | omit>`
  ```

  Use these classifications unless implementation discovers a concrete reason to adjust:

  - `complete Phase 02 release package implementation`: `Package impact: distributable`, `Release-note: include`.
  - `approve Phase 02 release package plan`: `Package impact: planning-only`, `Release-note: source-only`.
  - `complete Phase 01 release policy architecture`: keep `Package impact: repository-only`, `Release-note: source-only`.
  - `approve Phase 01 release policy plan`: `Package impact: planning-only`, `Release-note: source-only`.
  - `approve anchor spec`: `Package impact: planning-only`, `Release-note: source-only`.

  Do not rewrite older non-release-versioning changelog history in Phase 02.

- [ ] **Step 12: Add Phase 02 implementation changelog entry before commit**

  Add a newest-first `CHANGELOG.md` entry before the Phase 02 implementation commit:

  ```md
  ## 2026-06-07-release-versioning: complete Phase 02 release package implementation

  Release target: `0.3.0`
  Package impact: `distributable`
  Release-note: `include`

  ### Added

  - Added package-local release identity, release policy, and `0.3.0` release notes under `.agents/skills/dev-doc-harness/`.
  - Added `Harness release: <version or unknown>` to current work-item templates.
  - Added Phase 02 operator-manual and architecture-summary deltas for package adoption, rollback, and compatibility guidance.

  ### Changed

  - Routed release/package/adoption work through `module:release` and replaced the broad rule-versioning deferral with the `0.3.0` release-level compatibility model.
  - Normalized current release-versioning changelog entries with release target, package impact, and release-note relevance.
  ```

- [ ] **Step 13: Validate release/package text and routing**

  Run:

  ```powershell
  rg -n "module:release|rule:release\.(identity|package-boundary|changelog-source|release-notes|compatibility|artifact-context|team-adoption)" .agents/skills/dev-doc-harness
  rg -n "0\.3\.0|VERSION|docs/releases/0\.3\.0\.md|Source Changelog Entries" .agents/skills/dev-doc-harness README.md CHANGELOG.md
  rg -n "Harness release: `<version or unknown>`" .agents/skills/dev-doc-harness/assets/templates
  rg -n "Release target: `0\.3\.0`|Package impact:|Release-note:" CHANGELOG.md
  rg -n "AGENTS.md.*\.agents|docs/work-items|rollback|revert" .agents/skills/dev-doc-harness/references/release-policy.md .agents/skills/dev-doc-harness/docs/releases/0.3.0.md README.md
  ```

  Expected:

  - `module:release` and all `rule:release.*` IDs are owned and routed.
  - `0.3.0`, `VERSION`, release notes path, and source changelog section are discoverable.
  - Every current template includes exactly one `Harness release: <version or unknown>` field.
  - Current release-versioning changelog entries include the new schema fields.
  - Package boundary and rollback guidance are discoverable in package-local docs and README.

- [ ] **Step 14: Run existing harness validation**

  Run:

  ```powershell
  powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
  ```

  Expected: all current checks output `PASS`.

  If validation fails because `module:release` is unowned, duplicated, or routed incorrectly, fix the owner table, module catalog, or route text. If validation would require new release-specific script checks, do not add them in Phase 02 unless the current graph cannot pass without a small local adjustment; record the reason in the variance log if that happens.

- [ ] **Step 15: Scope and placeholder review**

  Run:

  ```powershell
  git diff --name-only
  rg -n "Status:[ ]Draft|TBD|TODO|unresolved|placeholder|Replace" .agents/skills/dev-doc-harness README.md CHANGELOG.md docs/work-items/2026-06-07-release-versioning/deltas
  git diff --name-only -- .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1 AGENTS.md docs/work-items/2026-06-07-release-versioning/spec-release-versioning.md docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md docs/work-items/2026-06-07-release-versioning/plan-phase-01-release-policy-release-versioning.md docs/work-items/2026-06-07-release-versioning/plan-phase-02-release-package-release-versioning.md
  ```

  Expected:

  - `git diff --name-only` includes only Phase 02 scoped package files, README, `CHANGELOG.md`, and Phase 02 deltas.
  - Placeholder scan has no unexpected matches. Existing literal references to `TODO.md` or "Replace" inside historical changelog context may appear only outside Phase 02 changed surfaces.
  - Protected frozen artifacts and `AGENTS.md` are not modified.

- [ ] **Step 16: Commit Phase 02 implementation**

  Stage only Phase 02 scoped files and `CHANGELOG.md`.

  Run:

  ```powershell
  git status --short --branch
  git diff --cached --name-only
  git commit -m "Implement release versioning package identity"
  git status --short --branch
  ```

  Expected: commit succeeds; final worktree is clean.

## Tests and validation

| Command | Expected result |
|---|---|
| `git status --short --branch` | Starts clean on branch `versioning`; before implementation commit, only Phase 02 scoped files are changed. |
| `rg -n "module:release|rule:release\.(identity|package-boundary|changelog-source|release-notes|compatibility|artifact-context|team-adoption)" .agents/skills/dev-doc-harness` | Outputs owner and route matches for release policy. |
| `rg -n "0\.3\.0|VERSION|docs/releases/0\.3\.0\.md|Source Changelog Entries" .agents/skills/dev-doc-harness README.md CHANGELOG.md` | Outputs matches proving release marker, release notes, README guidance, and changelog source trace are discoverable. |
| `rg -n "Harness release: `<version or unknown>`" .agents/skills/dev-doc-harness/assets/templates` | Outputs one match per current template. |
| `rg -n "Release target: `0\.3\.0`|Package impact:|Release-note:" CHANGELOG.md` | Outputs schema fields for current release-versioning entries. |
| `rg -n "AGENTS.md.*\.agents|docs/work-items|rollback|revert" .agents/skills/dev-doc-harness/references/release-policy.md .agents/skills/dev-doc-harness/docs/releases/0.3.0.md README.md` | Outputs package boundary and rollback guidance in package-local docs and README. |
| `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Outputs all current `PASS` lines. |
| `git diff --name-only -- .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1 AGENTS.md docs/work-items/2026-06-07-release-versioning/spec-release-versioning.md docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md docs/work-items/2026-06-07-release-versioning/plan-phase-01-release-policy-release-versioning.md docs/work-items/2026-06-07-release-versioning/plan-phase-02-release-package-release-versioning.md` | No output unless an approved amendment permits changes to one of these protected paths. |

## Documentation tasks

- Create `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`.
- Create `.agents/skills/dev-doc-harness/references/release-policy.md`.
- Update README with concise operator-facing package, adoption, and rollback guidance.
- Create `docs/work-items/2026-06-07-release-versioning/deltas/operator-manual.delta.md`.
- Create `docs/work-items/2026-06-07-release-versioning/deltas/architecture-summary.delta.md`.
- Update `CHANGELOG.md` before the implementation commit and normalize current release-versioning entries to the go-forward schema.
- Do not create Phase 03 test-case snapshots or validation-script release checks in Phase 02.

## Variance reminder

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

For this phase, changes to the package boundary, release marker path, release-note source-of-truth, compatibility model, full per-rule versioning scope, migration scope from `0.1`, active model-policy selection, or planning freeze behavior are high-impact and require amendment approval.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

For draft review, stage this Phase 02 plan only and request operator approval. After explicit approval, update `CHANGELOG.md` with a newest-first planning approval entry, verify the approved plan has no unresolved required items, stage only this phase plan and `CHANGELOG.md`, commit the approved planning package, and stop before implementation. Implementation must begin only after a fresh operator instruction after the freeze gate.

## Handoff output

At Phase 02 completion, report:

- Scope completed.
- Files created or changed.
- Validation commands and results.
- Whether `Test-HarnessPolicy.ps1` passed.
- Final package decisions implemented.
- Changelog/release-note source relationship.
- Whether variance occurred.
- Remaining Phase 03 validation and release-checkpoint work.
- De-facto sub-agent use; expected value is none.

## Completion criteria

- `.agents/skills/dev-doc-harness/VERSION` exists and contains `0.3.0`.
- `.agents/skills/dev-doc-harness/references/release-policy.md` owns `module:release` and the listed `rule:release.*` IDs.
- `.agents/skills/dev-doc-harness/SKILL.md` routes release/package/adoption work to `module:release`.
- `.agents/skills/dev-doc-harness/references/policy-architecture.md` registers `module:release` and points compatibility semantics to release policy.
- `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` exists with required release sections and source changelog entries.
- Current templates include exactly one `Harness release: <version or unknown>` field.
- README describes package boundary, release identity, release notes, adoption, and rollback concisely.
- `CHANGELOG.md` has the Phase 02 implementation entry before commit and current release-versioning entries use the go-forward schema.
- Phase 02 deltas exist and summarize operator and architecture changes.
- Existing harness validation passes.
- No full per-rule semantic versioning, package manager, installer, generated release pipeline, or `0.1` migration guidance is introduced.
