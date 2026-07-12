# Dev Doc Harness Distribution Release Policy

This document is the canonical source for Dev Doc Harness distribution release identity, package boundaries, package-local release notes, release compatibility, artifact release context, and team adoption flow. It is addressed to harness users, operators, and maintainers who need to understand the distributable harness package.

This policy does not define release processes for downstream applications, packages, or agentic systems developed with the help of the harness. Downstream projects keep their own release, deployment, publication, and release-note processes; the harness controls only its work-item artifact contract and changelog fragment consolidation points.

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

The `release/0.6` branch uses this exact marker:

```text
0.6.0
```

After that branch is cut, current development branches use the `0.6+` marker.

Use the harness release version as the compatibility unit for team adoption and rollback. The marker may include a trailing `+` on development branches to indicate changes after the latest release branch. Do not introduce per-rule semantic versions unless a later approved release expands scope.

## Distributable Package Boundary

The distributable harness package is root `AGENTS.md` plus `.agents/`.

The package excludes root `README.md`, root `CHANGELOG.md`, root `TODO.md`, this repository's `docs/work-items/`, `.git/`, and local development files.

Package-critical release policy, release notes, and release identity live under `.agents/skills/dev-doc-harness/` so they travel with the package.

## Changelog As Release Source

Root `CHANGELOG.md` is the repository source material for Dev Doc Harness package-local release notes after fragment consolidation.

Work-item-local changelog fragments under `docs/work-items/<work-id>/changelog/*.md` are pre-publication source evidence. They are consolidated into root `CHANGELOG.md` at an operator-owned checkpoint before Dev Doc Harness distribution release-note curation in this repository. Fragments are not independent Dev Doc Harness release notes, and package-local release notes must not be curated directly from unconsolidated fragments.

Release notes are curated from changelog entries in the consolidated root changelog and must not become an independent feature history. Multiple changelog entries for one delivered feature, such as spec approval, phase-plan approval, and implementation, are source evidence; release notes should summarize the delivered package-facing change once unless an approval entry matters for audit, migration, or compatibility.

## Release Notes

Release notes live under:

```text
.agents/skills/dev-doc-harness/docs/releases/
```

Release-note files use concrete released versions, not development markers. Current package-local release notes include:

```text
.agents/skills/dev-doc-harness/docs/releases/0.4.0.md
.agents/skills/dev-doc-harness/docs/releases/0.5.0.md
.agents/skills/dev-doc-harness/docs/releases/0.6.0.md
```

Do not create a `0.6+.md` release-note file for development-marker work.

Release notes should include a source changelog section so adopters can trace release-facing summaries back to consolidated repository history.

## Compatibility Model

Harness release versions carry compatibility meaning.

Stable `module:*`, `rule:*`, and `schema:*` IDs remain unversioned retrieval and ownership anchors. Compatible clarifications update the current owner and release notes when relevant. Incompatible replacements keep a discoverable replacement note such as `Superseded by:`.

Frozen historical artifacts are not rewritten only to update rule IDs, schema IDs, or release stamps. Current safety-critical canonical policy wins for future execution unless a frozen artifact records an explicit approved exception that is still compatible with the current harness release.

## Work-Item Artifact Release Context

New work-item templates include:

```md
Harness release: `<version or unknown>`
```

When a package-local `VERSION` exists, agents should use that value. Existing historical work-item artifacts without this field are pre-stamp artifacts and are not rewritten only to add it.

## Team Adoption And Rollback

Team repositories adopt the harness by copying root `AGENTS.md` and `.agents/`, merging local `AGENTS.md` instructions carefully, running validation when practical, and committing the harness update separately from product work.

Do not copy this repository's `docs/work-items/` into downstream projects. That folder is harness repository development history; each project keeps its own work-item artifacts.

Rollback is by reverting the dedicated harness update commit or PR to restore the previous root `AGENTS.md` and `.agents/` package.
