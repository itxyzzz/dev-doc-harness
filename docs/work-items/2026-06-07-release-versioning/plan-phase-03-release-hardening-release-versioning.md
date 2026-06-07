# Phase 03: Release Hardening Plan

> For agentic workers: use `dev-doc-harness` for repository artifact lifecycle and use `superpowers:executing-plans` or equivalent stepwise execution to implement this approved phase plan task-by-task. Steps use checkbox syntax for tracking.

Work ID: `2026-06-07-release-versioning`
Short ID: `release-versioning`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:plan.phase`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:release`, `module:freeze-gate`, `rule:quality.phase-plan-fresh-thread`, `rule:models.strategy-required`, `rule:lifecycle.variance-policy`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Objective

Harden the `0.3.0` release contract by adding lightweight validation for release identity, release notes, changelog schema, package boundary, template release context, and release routing; then update release-facing notes and documentation deltas for the final `0.3.0` checkpoint.

Phase 03 must keep the release system simple. It adds validation and final release documentation only. It must not add a package manager, installer, generated release-note pipeline, package manifest, per-rule semantic versioning, or migration guidance from `0.1`.

## Input context

The implementing agent must read these approved artifacts first:

- `docs/work-items/2026-06-07-release-versioning/spec-release-versioning.md`
- `docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md`
- `docs/work-items/2026-06-07-release-versioning/implementation-notes/variance-log.md`
- `docs/work-items/2026-06-07-release-versioning/plan-phase-03-release-hardening-release-versioning.md`

Then read the current package and validation surfaces:

- `AGENTS.md`
- `README.md`
- `CHANGELOG.md`
- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/VERSION`
- `.agents/skills/dev-doc-harness/references/release-policy.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
- `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
- `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`
- `docs/work-items/2026-06-07-release-versioning/deltas/operator-manual.delta.md`
- `docs/work-items/2026-06-07-release-versioning/deltas/architecture-summary.delta.md`

Preserve these decisions from Phases 01 and 02:

- `.agents/skills/dev-doc-harness/VERSION` is the package-local release marker and contains `0.3.0`.
- `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` is the package-local release-note file.
- Root `CHANGELOG.md` is source material for release notes.
- Release notes summarize delivered package-facing change once; planning entries are source evidence, not separate feature bullets.
- The distributable package is exactly root `AGENTS.md` plus `.agents/`.
- Downstream projects must not copy this repository's `docs/work-items/`.
- Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned retrieval and ownership anchors.
- Work-item templates use exactly one release-context field: `Harness release: <version or unknown>`.
- Existing historical work-item artifacts without a harness release field remain pre-stamp artifacts and are not rewritten.

## Likely files and areas

Modify:

- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`
- `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`
- `README.md`
- `CHANGELOG.md`
- `docs/work-items/2026-06-07-release-versioning/deltas/architecture-summary.delta.md`

Create:

- `docs/work-items/2026-06-07-release-versioning/deltas/testing-guide.delta.md`

Do not modify in Phase 03 unless an approved amendment changes scope:

- `AGENTS.md`
- `.agents/skills/dev-doc-harness/VERSION`
- `.agents/skills/dev-doc-harness/references/release-policy.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/SKILL.md`
- current work-item templates
- frozen approved specs, phase plans, or architecture snapshots
- historical work-item artifacts outside `docs/work-items/2026-06-07-release-versioning/`

If validation reveals one of the protected current package files is wrong, stop and record the issue. Use a plan amendment before changing release identity, package boundary, compatibility model, template schema, or router ownership semantics.

## Model and Sub-agent Strategy

Current orchestration: Codex desktop thread; exact model/profile is not exposed in repository artifacts. Operator approved Phase 03 with `enterprise-default` for this phase, overriding the repository-local `economy-default` selection for this scoped release-hardening work.
Fit assessment: Moderate process risk and low runtime risk. The phase changes a validation script and release-facing docs; mistakes could let teams adopt a package with drift between `VERSION`, release notes, changelog, and package-boundary guidance.
Recommended change: Use current orchestration for implementation under `enterprise-default`. A final read-only review is useful after validation passes because the release checkpoint affects team adoption across repositories.

| Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|
| Final release validation review | curated artifacts | Phase 03 diff, `VERSION`, release notes, changelog entries, validation output, README, release policy, and variance log | Review findings or no-issue note in completion report | `enterprise-default` for this phase | latest strongest or strongest available review profile | high | Final release checkpoint should catch subtle source-of-truth and adoption drift | No | Medium-high: bad validation or release notes can spread confusing policy to team repositories |

Fresh confirmation is required before using a sub-agent if the environment restricts sub-agent spawning or model selection, or if the implementation agent wants more than this single read-only final review.

## Tasks

- [ ] **Step 1: Verify clean starting state**

  Run:

  ```powershell
  git status --short --branch
  git log --oneline --decorate --max-count=5
  ```

  Expected: branch is `versioning`; worktree is clean; recent history includes `b2068f3 Implement release versioning package identity` and the Phase 03 planning approval commit after this plan is approved.

- [ ] **Step 2: Re-read approved Phase 03 inputs**

  Read the input context files listed above. Confirm:

  - The anchor spec is `Status: Approved`.
  - The architecture snapshot is `Status: Final`.
  - The Phase 03 test-case snapshot is `Status: Final` after the planning approval commit.
  - The variance log contains only approved or no-approval-required entries.
  - The package marker still contains exactly `0.3.0`.
  - This Phase 03 plan is approved before any implementation files are edited.

- [ ] **Step 3: Run current validation as a baseline**

  Run:

  ```powershell
  powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
  ```

  Expected: all existing checks print `PASS` and the command exits `0`.

- [ ] **Step 4: Add release check identifiers and required package paths**

  Modify `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`.

  Add these pass markers to `$Script:KnownPassMarkers`:

  ```powershell
  "PASS release.identity",
  "PASS release.notes",
  "PASS release.changelog-schema",
  "PASS release.package-boundary",
  "PASS release.template-context",
  "PASS release.route"
  ```

  Add these paths to `$requiredFiles`:

  ```powershell
  ".agents/skills/dev-doc-harness/VERSION",
  ".agents/skills/dev-doc-harness/docs/releases/0.3.0.md",
  "docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md"
  ```

  Add `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` to the current-surface read set only if the implementation uses graph or placeholder checks against release notes. Prefer targeted release-note checks over broad duplicate-policy scanning of release notes.

- [ ] **Step 5: Add release identity validation**

  Add a release identity check that:

  - Reads `.agents/skills/dev-doc-harness/VERSION`.
  - Accepts exactly `0.3.0` plus an optional trailing newline.
  - Fails if the file is missing, empty, has surrounding spaces, contains another version, or contains extra non-newline text.
  - Confirms `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` exists for that version.

  Use check ID `release.identity`.

- [ ] **Step 6: Add release notes validation**

  Add a release notes check that verifies `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` contains these headings:

  ```text
  # Dev Doc Harness 0.3.0
  ## Release
  ## Package Contents
  ## Added
  ## Changed
  ## Compatibility
  ## Team Adoption
  ## Rollback
  ## Source Changelog Entries
  ```

  The check must also verify every backticked `2026-06-07-release-versioning: ...` entry listed under `## Source Changelog Entries` appears as a `##` heading in `CHANGELOG.md`.

  Use check ID `release.notes`.

- [ ] **Step 7: Add current-release changelog schema validation**

  Add a changelog check that inspects only `CHANGELOG.md` entries whose heading starts with:

  ```text
  ## 2026-06-07-release-versioning:
  ```

  For each current-release entry, require exactly one line matching each field:

  ```text
  Release target: `0.3.0`
  Package impact: `distributable` / `repository-only` / `planning-only`
  Release-note: `include` / `source-only` / `omit`
  ```

  Valid values are:

  - `Package impact`: `distributable`, `repository-only`, `planning-only`
  - `Release-note`: `include`, `source-only`, `omit`

  Fail with the changelog heading and missing or invalid field when an entry does not comply. Do not parse or rewrite older non-release-versioning history.

  Use check ID `release.changelog-schema`.

- [ ] **Step 8: Add package-boundary validation**

  Add a package-boundary check that verifies release policy, release notes, and README all contain discoverable package guidance:

  - `.agents/skills/dev-doc-harness/references/release-policy.md` says the distributable package is root `AGENTS.md` plus `.agents/`.
  - `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` says the distributable package is root `AGENTS.md` plus `.agents/`.
  - `README.md` says the copyable distributable package is root `AGENTS.md` plus `.agents/`.
  - At least release policy and README say downstream projects must not copy this repository's `docs/work-items/`.
  - At least release policy, release notes, and README contain rollback guidance using revert/reverting.

  Use check ID `release.package-boundary`.

- [ ] **Step 9: Add template release-context validation**

  Add a template check that verifies each file in `$Script:TemplateFiles` contains exactly one literal line:

  ```md
  Harness release: `<version or unknown>`
  ```

  Fail with the template path and count when the line is missing or duplicated.

  Use check ID `release.template-context`.

- [ ] **Step 10: Add release route validation**

  Extend route validation in `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`:

  - Add `Assert-RouteContains "Release, package, or team adoption work" @("module:release")`.
  - Add route-budget coverage for `Release, package, or team adoption work` with budget `1`.

  Use a separate check ID `release.route` for the release route assertion if the script shape stays simple. If the implementation keeps route validation under `router.required-routes` and `router.route-budget`, it must still print `PASS release.route` after confirming the release row exists and routes to `module:release`.

- [ ] **Step 11: Add release golden scenario evidence**

  Add assertions that read `docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md` and verify it contains these scenario IDs:

  - `scenario:release.package-identity`
  - `scenario:release.release-notes-source`
  - `scenario:release.changelog-schema`
  - `scenario:release.package-boundary`
  - `scenario:release.template-context`
  - `scenario:release.team-adoption-rollback`

  The implementation may attach these assertions to `release.notes`, `release.package-boundary`, or `scenarios.golden-traversal` as long as failures identify the missing scenario ID and file path. Keep the existing historical golden traversal scenarios intact.

- [ ] **Step 12: Update release notes for Phase 03**

  Modify `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`:

  - Add one release-facing bullet under `## Added` for lightweight release validation covering `VERSION`, release notes, changelog schema, package boundary, template release context, and release route checks.
  - Do not split Phase 03 planning approval and implementation into separate release-note features.
  - Add these source entries under `## Source Changelog Entries` after the Phase 02 entries:

    ```md
    - `2026-06-07-release-versioning: approve Phase 03 release hardening plan`
    - `2026-06-07-release-versioning: complete Phase 03 release hardening`
    ```

  These headings must match the actual `CHANGELOG.md` headings before the implementation commit.

- [ ] **Step 13: Update repository README validation summary**

  Modify the README validation paragraph so it remains concise and says the command checks current harness surfaces, golden traversal evidence, and release package consistency. Do not duplicate the detailed release validation policy from `release-policy.md` or the script.

- [ ] **Step 14: Create Phase 03 testing guide delta**

  Create `docs/work-items/2026-06-07-release-versioning/deltas/testing-guide.delta.md` with:

  - The validation command.
  - The expected `PASS` check IDs, including the existing checks and the new `release.*` checks.
  - A short note that strict changelog schema validation is scoped to current `2026-06-07-release-versioning` entries.
  - A short note that release-note generation remains manual, with validation limited to source heading traceability.

- [ ] **Step 15: Update architecture delta for completed validation hardening**

  Modify `docs/work-items/2026-06-07-release-versioning/deltas/architecture-summary.delta.md`:

  - Keep the Phase 02 release identity, ownership, compatibility, and artifact-context summaries.
  - Change the Phase 03 follow-up wording to a Phase 03 validation-hardening summary.
  - Mention that validation now checks release identity, release-note headings and source changelog traceability, current release-versioning changelog metadata, package boundary, template release context, and release routing.

- [ ] **Step 16: Add Phase 03 implementation changelog entry before commit**

  Add a newest-first `CHANGELOG.md` entry before the Phase 03 implementation commit:

  ```md
  ## 2026-06-07-release-versioning: complete Phase 03 release hardening

  Release target: `0.3.0`
  Package impact: `distributable`
  Release-note: `include`

  ### Added

  - Added release validation checks for package identity, release notes, current release-versioning changelog schema, package boundary, template release context, and release routing.
  - Added the Phase 03 testing-guide delta and final release validation scenarios for the `0.3.0` checkpoint.

  ### Changed

  - Updated `0.3.0` release notes and repository validation guidance to include release package consistency checks without adding generated release-note machinery.
  ```

- [ ] **Step 17: Run focused release validation checks**

  Run:

  ```powershell
  rg -n "PASS release\\.(identity|notes|changelog-schema|package-boundary|template-context|route)" .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
  rg -n "scenario:release\\.(package-identity|release-notes-source|changelog-schema|package-boundary|template-context|team-adoption-rollback)" docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md
  rg -n "approve Phase 03 release hardening plan|complete Phase 03 release hardening" CHANGELOG.md .agents/skills/dev-doc-harness/docs/releases/0.3.0.md
  rg -n "Release target: `0\\.3\\.0`|Package impact: `(distributable|repository-only|planning-only)`|Release-note: `(include|source-only|omit)`" CHANGELOG.md
  ```

  Expected:

  - The script contains all new release pass markers.
  - The release test-case snapshot contains all Phase 03 release scenario IDs.
  - The Phase 03 release-note source entries match current changelog headings.
  - Current release-versioning changelog entries contain valid schema fields.

- [ ] **Step 18: Run full harness validation**

  Run:

  ```powershell
  powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
  ```

  Expected: the command exits `0` and prints `PASS` for every existing check plus:

  ```text
  PASS release.identity
  PASS release.notes
  PASS release.changelog-schema
  PASS release.package-boundary
  PASS release.template-context
  PASS release.route
  ```

- [ ] **Step 19: Scope and placeholder review**

  Run:

  ```powershell
  git diff --name-only
  rg -n "T[B]D|T[O]DO|unresolved|placeholder|R[e]place" .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1 .agents/skills/dev-doc-harness/docs/releases/0.3.0.md README.md CHANGELOG.md docs/work-items/2026-06-07-release-versioning/deltas
  git diff --name-only -- AGENTS.md .agents/skills/dev-doc-harness/VERSION .agents/skills/dev-doc-harness/references/release-policy.md .agents/skills/dev-doc-harness/references/policy-architecture.md .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/assets/templates docs/work-items/2026-06-07-release-versioning/spec-release-versioning.md docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md docs/work-items/2026-06-07-release-versioning/plan-phase-01-release-policy-release-versioning.md docs/work-items/2026-06-07-release-versioning/plan-phase-02-release-package-release-versioning.md docs/work-items/2026-06-07-release-versioning/plan-phase-03-release-hardening-release-versioning.md docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md
  ```

  Expected:

  - `git diff --name-only` includes only Phase 03 scoped implementation files, release notes, README, `CHANGELOG.md`, and Phase 03 deltas.
  - Placeholder scan has no unexpected matches in changed implementation surfaces.
  - Protected package policy, template, frozen planning, and snapshot artifacts are not modified during implementation.

- [ ] **Step 20: Commit Phase 03 implementation**

  Stage only Phase 03 scoped files and `CHANGELOG.md`.

  Run:

  ```powershell
  git status --short --branch
  git diff --cached --name-only
  git diff --cached --check
  git commit -m "Harden release versioning validation"
  git status --short --branch
  ```

  Expected: commit succeeds; final worktree is clean.

## Tests and validation

| Command | Expected result |
|---|---|
| `git status --short --branch` | Starts clean on branch `versioning`; before the implementation commit, only Phase 03 scoped files are changed. |
| `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` before edits | Existing validation passes before Phase 03 changes. |
| `rg -n "PASS release\\.(identity|notes|changelog-schema|package-boundary|template-context|route)" .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Outputs one marker for each new release validation check. |
| `rg -n "scenario:release\\.(package-identity|release-notes-source|changelog-schema|package-boundary|template-context|team-adoption-rollback)" docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md` | Outputs all Phase 03 release scenario IDs. |
| `rg -n "approve Phase 03 release hardening plan|complete Phase 03 release hardening" CHANGELOG.md .agents/skills/dev-doc-harness/docs/releases/0.3.0.md` | Outputs matching Phase 03 changelog headings and release-note source entries after implementation. |
| `rg -n "Release target: `0\\.3\\.0`|Package impact: `(distributable|repository-only|planning-only)`|Release-note: `(include|source-only|omit)`" CHANGELOG.md` | Outputs valid schema metadata for current release-versioning changelog entries. |
| `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` after edits | Outputs all current `PASS` lines, including new `release.*` checks, and exits `0`. |
| `git diff --name-only -- AGENTS.md .agents/skills/dev-doc-harness/VERSION .agents/skills/dev-doc-harness/references/release-policy.md .agents/skills/dev-doc-harness/references/policy-architecture.md .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/assets/templates docs/work-items/2026-06-07-release-versioning/spec-release-versioning.md docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md docs/work-items/2026-06-07-release-versioning/plan-phase-01-release-policy-release-versioning.md docs/work-items/2026-06-07-release-versioning/plan-phase-02-release-package-release-versioning.md docs/work-items/2026-06-07-release-versioning/plan-phase-03-release-hardening-release-versioning.md docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md` | No output during implementation unless an approved amendment permits changing a protected path. |
| `git diff --cached --check` | No whitespace errors before commit. |

## Documentation tasks

- Use `docs/work-items/2026-06-07-release-versioning/snapshots/test-cases.snapshot.md` as the approved release-validation scenario snapshot.
- Create `docs/work-items/2026-06-07-release-versioning/deltas/testing-guide.delta.md`.
- Update `docs/work-items/2026-06-07-release-versioning/deltas/architecture-summary.delta.md` to record completed validation hardening.
- Update `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` so release notes include Phase 03 validation hardening and source changelog entries.
- Update `README.md` only to keep the validation-command summary accurate and concise.
- Update `CHANGELOG.md` before the implementation commit.
- Do not update `operator-manual.delta.md` unless implementation discovers a concrete operator-flow change beyond validation wording.

## Variance reminder

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, package-boundary, release-identity, compatibility-model, or feasibility changes.

For this phase, changes to release marker path or value, release-note location, package boundary, changelog-as-source policy, per-rule versioning scope, migration scope from `0.1`, active model-policy selection, router ownership semantics, or planning freeze behavior are high-impact and require amendment approval.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

For draft review, stage this Phase 03 plan and the Phase 03 test-case snapshot only, then request operator approval. After explicit approval, update `CHANGELOG.md` with a newest-first planning approval entry, verify the approved artifacts have no unresolved required items, stage only this phase plan, the test-case snapshot, and `CHANGELOG.md`, commit the approved planning package, and stop before implementation. Implementation must begin only after a fresh operator instruction after the freeze gate.

Use this planning approval changelog entry:

```md
## 2026-06-07-release-versioning: approve Phase 03 release hardening plan

Release target: `0.3.0`
Package impact: `planning-only`
Release-note: `source-only`

### Added

- Added the approved Phase 03 plan and release-validation test-case snapshot for hardening `0.3.0` package identity, release notes, changelog schema, package boundary, template release context, release routing, and final release checkpoint documentation.
```

## Handoff output

At Phase 03 completion, report:

- Scope completed.
- Files created or changed.
- Validation commands and results.
- Whether `Test-HarnessPolicy.ps1` passed and which new `release.*` checks were added.
- Whether release notes still trace to changelog entries.
- Whether release-note generation remains manual and intentionally not automated.
- Whether variance occurred.
- Whether final review used a sub-agent; include count, role, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.
- Recommended next step for cutting or updating the `release/0.3` branch after the implementation commit.

## Completion criteria

- `Test-HarnessPolicy.ps1` validates package-local `VERSION` equals `0.3.0`.
- `Test-HarnessPolicy.ps1` validates `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` exists and includes required release-note sections.
- `Test-HarnessPolicy.ps1` validates release-note source changelog entries exist as changelog headings.
- `Test-HarnessPolicy.ps1` validates current `2026-06-07-release-versioning` changelog entries use the go-forward schema and valid values.
- `Test-HarnessPolicy.ps1` validates package-boundary and rollback guidance are discoverable in the expected package and README surfaces.
- `Test-HarnessPolicy.ps1` validates every current template has exactly one `Harness release: <version or unknown>` field.
- `Test-HarnessPolicy.ps1` validates the release/package/adoption router row.
- Existing graph, route, duplicate-policy, placeholder, tracked work-item, and golden traversal checks still pass.
- Phase 03 testing-guide and architecture-summary deltas are complete.
- `0.3.0` release notes and `CHANGELOG.md` remain synchronized by source-heading traceability.
- No package manager, installer, generated release-note pipeline, package manifest, per-rule semantic versioning, or `0.1` migration guidance is introduced.
