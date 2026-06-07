# Release Versioning Architecture Snapshot

Work ID: `2026-06-07-release-versioning`
Source spec: `../spec-release-versioning.md`
Status: Final

## Goal

Dev Doc Harness `0.3.0` uses release-level compatibility instead of per-rule semantic versioning. The release contract must let a team identify the installed harness, review what changed, update multiple repositories with minimal ceremony, and roll back by reverting a dedicated harness update.

This snapshot is the Phase 01 architecture handoff. It records the release identity model, distributable package boundary, changelog-to-release-note contract, rule and schema compatibility stance, artifact release-context decision, team adoption flow, validation direction, Phase 02 inputs, and remaining risks.

## Release Identity Model

The package-local release marker for `0.3.0` is:

```text
.agents/skills/dev-doc-harness/VERSION
```

The file should contain exactly the plain text release version, followed by an optional trailing newline:

```text
0.3.0
```

Use a simple `VERSION` file rather than a manifest for `0.3.0`. A manifest would only be justified later if the package needs more machine-readable fields than release identity and release-note location.

Harness release versions are the compatibility unit for team adoption. Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned retrieval and ownership anchors. They tell an agent where policy lives; they do not encode compatibility by themselves.

## Distributable Package Boundary

The distributable harness package is exactly the root `AGENTS.md` file and the `.agents/` folder.

The package explicitly excludes:

- root `README.md`
- root `CHANGELOG.md`
- root `TODO.md`
- this repository's `docs/work-items/`
- `.git/`
- local development files, editor files, caches, and generated scratch files

Release identity, release notes, and any package-local release policy must live under `.agents/skills/dev-doc-harness/` because they must travel with the package when a project receives only `AGENTS.md` and `.agents/`.

This repository's `docs/work-items/` remains repository development history for the harness itself. Downstream project repositories must keep their own `docs/work-items/` folders for their own project work items.

## Changelog To Release Notes Contract

Root `CHANGELOG.md` is the repository source material for release notes. Package-local release notes are curated from changelog entries; they are not an independent history.

For `0.3.0`, release notes should be assembled manually with a checklist. A generator script is out of scope unless later phases discover that a tiny script is lower maintenance than review discipline.

Release notes must cite or summarize relevant changelog sections. They must not introduce release-note-only feature history that cannot be traced back to `CHANGELOG.md`.

Multiple changelog entries for the same feature or work item, such as approved spec, approved phase plan, and implementation entries, are source evidence but should not become separate release-note bullets by default. Release notes should summarize the delivered operator-facing or package-facing change once. Planning entries should be referenced only when they matter for audit, migration, or compatibility.

## Changelog Go-Forward Schema

Starting with `0.3.0` release-versioning work, new changelog entries should use this low-friction schema:

```md
## <work-id>: <short title>

Release target: `0.3.0`
Package impact: `distributable` / `repository-only` / `planning-only`
Release-note: `include` / `source-only` / `omit`

### Added

- Concise user, operator, package, or maintenance impact.

### Changed

- Concise user, operator, package, or maintenance impact.
```

Use normal Keep a Changelog subsections only when they apply: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`.

Field meaning:

- `Release target`: the intended harness release when known. Use `unreleased` only when a target is genuinely unknown.
- `Package impact: distributable`: the entry changes files inside root `AGENTS.md` or `.agents/`, or directly affects package behavior for downstream adopters.
- `Package impact: repository-only`: the entry changes repository docs, planning artifacts, validation evidence, or release preparation outside the distributable package.
- `Package impact: planning-only`: the entry freezes or approves specs, plans, amendments, or other planning artifacts without changing package behavior.
- `Release-note: include`: the entry should contribute to a release-note bullet or section.
- `Release-note: source-only`: the entry is source evidence for a delivered feature but should usually be grouped under a later implementation bullet.
- `Release-note: omit`: the entry is internal enough that it normally should not appear in release notes.

Phase 02 should normalize the current top-of-file `2026-06-07-release-versioning` entries to this schema. It does not need to rewrite older historical entries unless a later validation plan explicitly scopes a narrow current-release normalization.

## Release Notes Location And Shape

The `0.3.0` release notes path is:

```text
.agents/skills/dev-doc-harness/docs/releases/0.3.0.md
```

Required sections:

- `# Dev Doc Harness 0.3.0`
- `## Release`
- `## Package Contents`
- `## Added`
- `## Changed`
- `## Compatibility`
- `## Team Adoption`
- `## Rollback`
- `## Source Changelog Entries`

Release notes should be short and release-facing. They should explain what a downstream team receives, how to adopt it, what compatibility model applies, and how to trace the notes back to changelog entries.

The `Source Changelog Entries` section may list spec and plan approval entries, but the release notes must group those under the delivered change rather than presenting planning approval, phase planning, and implementation as separate release features.

## Rule And Schema Compatibility Model

Harness release versions carry compatibility meaning. `0.3.0` is the first release with explicit package identity, package-local release notes, and a concrete compatibility stance.

Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned anchors. They are optimized for search, routing, ownership, and validation. They are not semver strings and should not be renamed merely because policy text is clarified.

Compatible clarifications update the current canonical owner and are documented in `CHANGELOG.md` and release notes when operator-facing or package-facing. Incompatible replacements should keep the old anchor discoverable long enough to point readers forward with a `Superseded by:` note or an equivalent replacement note in the canonical owner.

Frozen historical artifacts are not rewritten only to update rule IDs, schema IDs, or release stamps. They preserve the policy context and approved decisions from their own review point.

For future execution, current safety-critical canonical policy wins unless a frozen artifact records an explicit approved exception and that exception is still compatible with the current harness release. If a future release marks a change as migration-required, the project should create a harness-update work item or amendment before relying on older active artifacts.

## Work-Item Artifact Release Context

For `0.3.0`, templates should add one field:

```md
Harness release: `<version or unknown>`
```

Do not add both `Harness release` and `Minimum harness release` in `0.3.0`. A single field is enough to help future agents interpret which harness produced or froze an artifact without making every template header noisy.

For newly created artifacts, agents should set `Harness release` to the repo-local `VERSION` value when it exists. If no package-local marker exists yet, use `unknown`.

Existing historical work-item artifacts without this field are pre-stamp artifacts and must not be rewritten only to add it.

## Team Adoption And Rollback Flow

Minimum team adoption flow:

1. Copy the release's root `AGENTS.md` and `.agents/` into the target project repository.
2. If the target already has an `AGENTS.md`, merge repository-specific instructions carefully instead of blindly replacing them.
3. Confirm `.agents/skills/dev-doc-harness/VERSION` records the adopted release.
4. Run the harness validation command when practical:

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
   ```

5. Commit or open a PR for the harness update separately from product work.
6. Do not copy this harness repository's `docs/work-items/` into the project.

Rollback flow:

1. Revert the dedicated harness update commit or PR.
2. Restore the previous root `AGENTS.md` and `.agents/` package.
3. Preserve the project repository's own `docs/work-items/` unless a project-specific cleanup plan says otherwise.

## Validation Direction

Phase 03 should add or update validation for these checks:

- Package-local `.agents/skills/dev-doc-harness/VERSION` exists and equals `0.3.0`.
- Package-local `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md` exists.
- Release notes include `## Source Changelog Entries`.
- Current `2026-06-07-release-versioning` changelog entries follow the go-forward schema.
- Package-boundary docs say downstream projects copy root `AGENTS.md` and `.agents/`, not this repository's `docs/work-items/`.
- Existing graph, route, duplicate-policy, placeholder, tracked work-item, and golden traversal validation still pass.

Release-note and changelog sync may remain checklist-based for `0.3.0`. Validation should not overfit Markdown parsing if that would make changelog maintenance more brittle than the drift it prevents.

## Phase 02 Inputs

Phase 02 should consume these decisions before touching package files:

- Add `.agents/skills/dev-doc-harness/VERSION` containing `0.3.0`.
- Add package-local release notes at `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`.
- Treat root `CHANGELOG.md` as source material for release notes.
- Normalize current `2026-06-07-release-versioning` changelog entries to include release target, package impact, and release-note relevance.
- Update package-local policy, likely through a concise `module:release` owner or a release section in `policy-architecture.md`, without adding heavy package-manager behavior.
- Replace the broad rule-versioning deferral in current package policy with the release-level compatibility stance from this snapshot.
- Update README/operator guidance only as repository documentation; package-critical guidance must also live under `.agents/skills/dev-doc-harness/`.
- Add `Harness release: <version or unknown>` to new artifact templates if Phase 02 handles templates; otherwise leave it for Phase 03.
- Keep downstream project `docs/work-items/` project-local and keep this repository's work-item history out of the distributable package.

## Open Risks

- `module:release` may be useful, but Phase 02 should avoid adding a new canonical file unless release policy becomes too large for `policy-architecture.md` or the router.
- Changelog schema validation can become annoying if it tries to parse all historical entries. Limit strict checks to current release work unless a later plan scopes broader cleanup.
- Release notes can drift from `CHANGELOG.md` if reviewers skip the source comparison. `0.3.0` should rely on explicit source sections and validation/checklist discipline, not a generated pipeline.
- `Harness release` in templates improves future interpretation but adds one more header field. Keep it to one field for `0.3.0`.
- Team repositories may have local `AGENTS.md` customizations. Adoption docs should stress careful merge plus dedicated harness-update PR rather than blind replacement.
