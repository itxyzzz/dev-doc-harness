# Implementation Changelog

This document owns current implementation-stage changelog authoring, fragment compatibility, root consolidation, and root cleanup. Planning artifacts and freeze approvals do not create changelog entries.

Module: `module:implementation-changelog`

## Fragment lifecycle

Create or update the relevant fragment before an implementation commit. Do not create planning-approval, spec, plan, amendment, or other planning-only fragments. Fragment entries stay newest-first.

## Fragment locations and names

Changelog source fragments live below the work item package:

```text
docs/work-items/<work-id>/changelog/*.md
```

Implementation fragment filenames use lower-kebab-case: `implementation-fragment.md` for ordinary delivery and `phase-NN-fragment.md` for phase-specific delivery, such as `phase-01-fragment.md`.

## Current entry schema and commit synchronization

Each changelog fragment consists of the header, metadata line, and body, according to the schema

```md
### `<date> <commit-subject>`

Meta -- `<release target: unreleased, a concrete version, or a development marker>` : `<package impact: repository-only, or distributable>`

#### `<Change type: Added, Changed, Removed, Fixed, Deprecated, or Security>`

- Describe the delivered implementation change.
```

The heading must be synchronized to its implementation commit subject as defined in `rule:naming.commit-messages`.

The body format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Group together the changes of the same type.

If an implementation subject changes, update the matching planned commit row and fragment heading before committing. When one entry covers multiple commits, each subject must match a listed planned commit row or a clear bullet-level title snippet under that entry.

## Consolidation

Run `consolidate_changelog_fragments.py --lint` before implementation commits. At an operator-owned checkpoint, run `--check` and then the default write mode to add absent eligible entries to root `CHANGELOG.md`.

Root `CHANGELOG.md` is the curated release source. Release notes are selected from its delivered implementation entries during release preparation.

## Compatibility and legacy support

Pre-0.8 fragments using the legacy three-field metadata remain frozen. The consolidator accepts them for compatibility but never rewrites them. Legacy `planning-only` entries are archival input and are never consolidated into root history.

Use `--migrate-root` only for an approved root cleanup. It removes every root planning-only entry and rewrites surviving legacy metadata to the compact tagged form. A second migration or consolidation run must make no change.
