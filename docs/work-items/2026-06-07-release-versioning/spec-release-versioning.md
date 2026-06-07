# Harness Release Versioning Spec

Work ID: `2026-06-07-release-versioning`
Short ID: `release-versioning`
Status: Approved
Schema: `schema:spec.large-phased`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:architecture`, `module:freeze-gate`, `rule:lifecycle.large-anchor-spec`, `rule:quality.spec-handoff`, `rule:models.strategy-required`, `rule:freeze.multi-gate-flow`

## Goal

Define the release and versioning contract for Dev Doc Harness `0.3`, so a team can adopt, update, audit, and roll back the harness across multiple repositories with minimal ceremony.

The release contract must answer these questions:

- What files comprise the distributable harness package?
- How does a project know which harness release it has installed?
- How are release notes produced from the changelog?
- What changelog schema is required so release notes can be generated or assembled reliably?
- How do rule IDs, module IDs, schemas, and frozen artifacts interact with harness-level release versions?
- What is the smallest practical upgrade workflow for a team repository?

This work is release-worthy because `0.2` established the policy architecture, router, rule IDs, templates, and validation model. `0.3` should make those artifacts safe to distribute and maintain as a package.

## Planning handoff quality bar

This spec is the central handoff for the `0.3` release-versioning work. Phase plans must preserve the user constraints:

- Keep team adoption simple.
- Treat changelog entries as the source for release notes.
- Identify the distributable package clearly.
- Keep this harness repository's planning artifacts out of downstream project packages.
- Avoid migration work from `0.1` because no external users depend on it yet.
- Do not introduce heavy package-manager behavior or per-rule semantic versioning unless a later approved amendment expands scope.

Phase plans must derive from this spec. If later planning discovers missing context before this spec is frozen, update the draft spec directly. If missing context is discovered after freeze, create an amendment.

## Scope

- Add a harness-level release identity for `0.3`.
- Define the distributable package as root `AGENTS.md` plus the `.agents/` folder.
- Keep this repository's `docs/work-items/` planning artifacts out of the distributable package.
- Add release notes inside the distributable package, likely under `.agents/skills/dev-doc-harness/docs/releases/`.
- Define a release-note policy that treats `CHANGELOG.md` as the source material for release notes.
- Tighten the changelog policy and update existing current entries as needed so go-forward release notes can be assembled from changelog content.
- Define the relationship between harness release versions, stable unversioned `module:*` and `rule:*` IDs, template/schema IDs, and historical work-item artifacts.
- Update templates or artifact prompts, if needed, so newly created work-item artifacts can record the harness release that produced or froze them.
- Update validation so the harness release identity, distributable-package docs, release notes, and changelog schema remain consistent.
- Update README/operator guidance so team repositories have a minimal harness upgrade flow.

## Non-scope

- Migration guidance from `0.1`; no external users depend on that release.
- Full per-rule semantic versioning.
- A package manager, installer, publishing service, or generated release pipeline.
- Automated release-note generation unless a small script is clearly simpler than manual assembly.
- Moving project work-item artifacts into the distributable package.
- Rewriting historical frozen work-item artifacts only to stamp a harness release.
- Changing the active repository model policy from the `AGENTS.md` selection point.
- Removing or weakening planning freeze gates, variance handling, changelog-before-commit, immutable snapshots, or graph validation.

## Current state

The current `versioning` branch has completed the policy architecture refactor and follow-up hardening:

- `SKILL.md` is an operation router.
- `references/policy-architecture.md` owns `module:architecture`, rule ID conventions, dependency direction, router inputs, and the current rule-versioning deferral.
- Current canonical references declare `module:*` and `rule:*` owners.
- Templates include schema anchors and compact policy-reference lines.
- `Test-HarnessPolicy.ps1` validates current harness surfaces, graph references, route budgets, duplicated policy blocks, placeholders, tracked work-item docs, and golden traversal scenarios.
- `README.md` says users may copy `AGENTS.md` and `.agents/` into another repository, or install the skill globally.
- `CHANGELOG.md` is newest-first and grouped by change type, but it currently records work-item and phase history rather than explicit release-note source sections.
- `TODO.md` still lists in-team distribution, cross-repository update policy, and harness versioning/update policy as governance work.
- No release marker, release-note location, or distributable-package manifest currently exists in the repository state inspected for this spec.

## Proposed behavior

The harness should use harness-level release versions, not versioned rule IDs, as the primary compatibility unit.

For `0.3`:

- The distributable package is exactly:
  - `AGENTS.md`
  - `.agents/`
- The distributable package explicitly excludes:
  - root `README.md`
  - root `CHANGELOG.md`
  - root `TODO.md`
  - this repository's `docs/work-items/`
  - `.git/` and local development files
- Release notes live inside the package, for example:
  - `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`
- A small release marker lives inside the package, for example:
  - `.agents/skills/dev-doc-harness/VERSION`
- A package manifest or concise package policy may live inside the package only if it materially reduces ambiguity. If introduced, keep it human-readable and lightweight.
- `CHANGELOG.md` remains the repository-level source material for release notes. Release notes are curated from changelog entries, not a separate competing history.
- Changelog entries should follow a go-forward schema that supports release-note assembly by recording work ID, release target when known, change type, impacted package surface, and concise user/operator impact.
- Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned retrieval and ownership anchors. Compatibility is expressed at the harness release level.
- New work-item artifacts should record the harness release used to create or freeze them only when that can be done with minimal template friction.
- Existing historical work-item artifacts without a harness release stamp are treated as pre-stamp historical artifacts and are not rewritten.
- Team project upgrades happen as a dedicated harness-update commit or PR that copies the new `AGENTS.md` and `.agents/`, runs validation, and records the adopted harness release.

## Interfaces and data

Expected affected interfaces include:

- Root `CHANGELOG.md` schema and existing current entries that need normalization for go-forward release-note assembly.
- Root `AGENTS.md` if release/package identity needs a bootstrap note.
- `.agents/skills/dev-doc-harness/SKILL.md` if the router needs a release/versioning route.
- `.agents/skills/dev-doc-harness/references/policy-architecture.md` for replacing the broad rule-versioning deferral with the `0.3` release-compatibility model.
- A new canonical reference or section, likely `module:release`, if release/versioning policy is large enough to deserve a single owner.
- `.agents/skills/dev-doc-harness/VERSION` or equivalent package-local release marker.
- `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` or equivalent release-note file.
- Templates under `.agents/skills/dev-doc-harness/assets/templates/` if artifact release stamping is adopted.
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` for validation of release marker, release notes, package boundaries, and changelog schema.
- README operator guidance for minimal team adoption and update workflow.

No runtime product API, persistence schema, external service, or user-data interface is affected.

## State flow and control flow

Release flow for this repository:

1. Development happens on trunk-oriented branches.
2. Changelog entries are maintained before commits and include enough metadata to support release-note assembly.
3. A release branch such as `release/0.3` is cut when release content is ready.
4. The release marker is set to `0.3.0`.
5. Package-local release notes are created from relevant changelog entries.
6. Validation confirms the package has a version marker, release notes, package boundary documentation, and current harness graph consistency.
7. The release commit or PR finalizes the distributable package.

Adoption flow for a project repository:

1. Copy the release's `AGENTS.md` and `.agents/` into the project repository.
2. Merge `AGENTS.md` carefully if the project already has repository-specific instructions.
3. Run the harness validation command when practical.
4. Commit the harness update as a dedicated change.
5. Keep the project repository's own `docs/work-items/` for that project's work items only.

Rule compatibility flow:

1. For new work, agents follow the repo-local installed harness release.
2. Frozen project work-item artifacts preserve the policy context and decisions from when they were created.
3. Current safety-critical canonical policy wins for future execution unless an old artifact records an explicit approved exception that is still compatible with the current harness release.
4. If a future release marks a policy or schema change as migration-required, a project should create a harness-update work item or amendment before relying on older active artifacts.

## Safety, security, privacy, compliance, migration, and rollback

No privacy, compliance, or product-security behavior changes are expected. The process-safety risk is adoption drift: different repositories may silently run different harness versions while operators assume they are using the same policy.

The `0.3` release should reduce that risk by making release identity visible and package boundaries simple.

Rollback for a project should be simple:

- Revert the dedicated harness-update commit or PR.
- Restore the previous `AGENTS.md` and `.agents/` package.
- Preserve project `docs/work-items/` artifacts unless a project-specific cleanup plan says otherwise.

Migration from `0.1` is not required. Migration from `0.2` should be concise because `0.2` is the current release branch created from this repository's present state and no external team repositories depend on earlier releases yet.

## Validation strategy

Validation should stay lightweight and local.

Required validation directions:

- Existing harness policy graph validation passes.
- The package release marker exists and matches the current release notes filename.
- Package-local release notes exist for `0.3.0`.
- Release notes can be traced to relevant `CHANGELOG.md` entries.
- Changelog entries follow the go-forward schema for new `0.3` work.
- The documented distributable package excludes this repository's `docs/work-items/`.
- Templates or artifact schemas record harness release only if that requirement is adopted by the phase plan.
- README or package docs describe the minimal team update flow.

If validation cannot reasonably prove release notes are built from changelog entries, it should use a simple manual checklist rather than overfitting Markdown parsing.

## Triage, debugging, and operations

Useful checks and diagnostics:

- Search for release identity:
  - `rg -n "0\\.3\\.0|Harness release|module:release|rule:release" AGENTS.md README.md CHANGELOG.md .agents`
- Confirm package boundary:
  - `rg -n "distributable|package|docs/work-items|release notes" README.md .agents`
- Confirm no downstream package guidance tells teams to copy this repository's `docs/work-items/`.
- Confirm validation still passes:
  - `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`
- Confirm release notes are not orphaned from changelog entries by manually comparing `CHANGELOG.md` sections for release-versioning work with `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`.

## Assumptions

- `0.2` exists as a branch and represents the current policy-architecture baseline.
- `0.3` should be the first release with explicit release identity and team adoption policy.
- The team prefers repo-local pinned harness copies over relying only on a global install.
- The release package should be simple enough to copy manually.
- Changelog remains the repository history; release notes are curated release-facing summaries derived from it.
- No external repositories currently need migration from `0.1`.
- Full per-rule semantic versioning would add more maintenance than value at this stage.

## Risks

- Changelog schema tightening could create busywork if it asks for too much metadata on every commit.
- Release notes may drift from changelog if no validation or review checklist links them.
- Putting release notes under `.agents/` increases package size slightly, but keeps team adopters informed without copying repository-level docs.
- Adding harness release stamps to every artifact could create noise if templates become too header-heavy.
- A package manifest could become a mini package manager if it grows beyond package identity and boundaries.
- Excluding `docs/work-items/` from the package while tracking it in this repository may confuse contributors unless README and release policy are explicit.

## Known unknowns

- Whether the release marker should be `VERSION`, `harness-version.txt`, or a tiny JSON/Markdown manifest.
- Whether release notes should be manually curated from changelog or assembled by a small script in a later release.
- Whether artifact templates should include both `Harness release` and `Minimum harness release`, or only one field.
- Whether validation should warn or fail when release notes mention changes not found in the changelog.
- Whether the package should include a short `docs/package.md` inside `.agents/skills/dev-doc-harness/`.

## Rejected alternatives

- Per-rule semantic versioning for `0.3`: rejected as too much maintenance and too heavy for team adoption now.
- Release notes only at the repository root: rejected because the distributable package would not carry its own release information.
- Copy this repository's `docs/work-items/` into downstream projects: rejected because project work-item folders must contain that project's work, not harness development history.
- Keep changelog and release notes as independent histories: rejected because they would drift.
- Add a full installer or package manager: rejected because manual copy plus dedicated update PR is simple enough for `0.3`.
- Provide migration from `0.1`: rejected because there are no external users to migrate.

## Acceptance criteria

- The harness has a visible package-local `0.3.0` release identity.
- The distributable package is documented as root `AGENTS.md` plus `.agents/`.
- The distributable package explicitly excludes this repository's `docs/work-items/`.
- Package-local release notes for `0.3.0` exist under `.agents/skills/dev-doc-harness/`.
- Release notes are derived from `CHANGELOG.md`, and the release policy says changelog is the source material.
- Changelog policy is tightened enough to support release-note assembly without becoming onerous.
- Existing current changelog entries relevant to `0.3` are normalized if needed for the go-forward schema.
- Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned anchors; compatibility is handled at the harness release level.
- New work-item artifacts record harness release context if the approved plan chooses that template change.
- README or package docs describe a minimal project upgrade flow through a dedicated commit or PR.
- Validation covers release marker, release notes, package boundary, changelog schema expectations, and existing harness graph checks.

## Phase decomposition

| Phase | Objective | Output |
|---|---|---|
| 01 | Define the release policy, package boundary, changelog schema, and release-note derivation contract. | `plan-phase-01-release-policy-release-versioning.md` |
| 02 | Implement package-local release identity, release notes, changelog policy/schema changes, and release documentation. | `plan-phase-02-release-package-release-versioning.md` |
| 03 | Add validation and template/update-flow refinements, then prepare the `0.3.0` release checkpoint. | `plan-phase-03-release-hardening-release-versioning.md` |

Phase 01 should decide exact filenames and whether `module:release` is a new canonical reference or a section in `policy-architecture.md`. Phase 02 should keep implementation simple and package-local. Phase 03 should harden validation and avoid adding release machinery beyond the acceptance criteria.

## Planning artifact freeze gates

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.multi-gate-flow`. Record the draft review, approval commit or handoff snapshot, and pause before implementation or later phase execution.

## Model and Sub-agent Strategy

Current orchestration: Codex desktop thread; exact model/profile is not exposed in repository artifacts. The operator has indicated branch `versioning` and release target `0.3`.
Fit assessment: Medium-to-high process risk because this affects team adoption and cross-repository compatibility. Implementation is mostly documentation and validation, but architecture review should be careful.
Recommended change: Use current orchestration. Consider a stronger final review if Phase 02 or Phase 03 changes release/package authority or validation behavior in subtle ways.

| Phase | Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | Release policy architecture review | curated artifacts | This spec, `policy-architecture.md`, `README.md`, `CHANGELOG.md`, current templates, validation script | Review notes or phase-plan findings | active repository policy unless changed by operator | latest strongest or standard | high | Release governance affects team adoption and future repositories | No | High: confusing release semantics can spread across projects |
| 03 | Final package/release validation review | curated artifacts | Completed release marker, release notes, changelog policy, validation output, README/package docs | Final review findings | active repository policy unless changed by operator | latest strongest | high | Final release checkpoint should catch adoption and rollback ambiguity | No | High: a bad release contract creates team-wide drift |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Source material for release notes and commit history |
| Test cases | Snapshot | Yes | Phase 03 | `snapshots/test-cases.snapshot.md` | Capture release/version validation scenarios |
| Testing guide delta | Living delta | Yes | Phase 03 | `deltas/testing-guide.delta.md` | Update validation expectations if script checks release/version fields |
| Operator manual delta | Living delta | Yes | Phase 02 or 03 | `deltas/operator-manual.delta.md` | Explain minimal team update flow and package boundary |
| API reference delta | Living delta | No | Not applicable | `deltas/api-reference.delta.md` | No public API changes |
| Architecture snapshot | Snapshot | Yes | Phase 01 | `snapshots/architecture.snapshot.md` | Capture release policy, package boundary, and changelog/release-note contract |
| Architecture summary delta | Living delta | Yes | Phase 02 or 03 | `deltas/architecture-summary.delta.md` | Summarize release identity and compatibility model |

## Approval

- Status: Approved
- Superseded by: None
