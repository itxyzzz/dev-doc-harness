# Implementation Changelog

This document owns current implementation-stage changelog authoring, fragment compatibility, root consolidation, and root cleanup. Planning artifacts and freeze approvals do not create changelog entries.

Module: `module:implementation-changelog`

## Current entry schema

An implementation fragment entry has a commit-derived heading followed by exactly one compact metadata line:

```md
### 2026-08-01 refactor: example -- retain delivery records

Meta -- `unreleased` : `repository-only`

#### Changed

- Describe the delivered implementation change.
```

The release target is `unreleased`, a concrete version, or a development marker. Package impact is `distributable` or `repository-only`. Release-note selection is release-maintainer curation, not entry metadata.

## Fragment locations, names, and commit synchronization

Ordinary fragments live at `docs/work-items/<work-id>/changelog/implementation-fragment.md`. Phase-specific fragments live at `docs/work-items/<work-id>/changelog/phase-NN-fragment.md`, such as `phase-01-fragment.md`.

Each entry heading is `<date> <commit-subject>` and may use Markdown level two or three. The heading and its implementation commit use the same title or elaboration snippet. If an implementation subject changes, update the matching planned commit row and fragment heading before committing. When one entry covers multiple commits, each subject must match a listed planned commit row or a clear bullet-level title snippet under that entry.

## Fragment lifecycle

Create or update the relevant fragment before an implementation commit. Do not create planning-approval, spec, plan, amendment, or other planning-only fragments. Fragment entries stay newest-first.

## Consolidation

Run `consolidate_changelog_fragments.py --lint` before implementation commits. At an operator-owned checkpoint, run `--check` and then the default write mode to add absent eligible entries to root `CHANGELOG.md`.

Root `CHANGELOG.md` is the curated release source. Release notes are selected from its delivered implementation entries during release preparation.

## Compatibility and legacy support

Pre-0.8 fragments using the legacy three-field metadata remain frozen. The consolidator accepts them for compatibility but never rewrites them. Legacy `planning-only` entries are archival input and are never consolidated into root history.

Use `--migrate-root` only for an approved root cleanup. It removes every root planning-only entry and rewrites surviving legacy metadata to the compact tagged form. A second migration or consolidation run must make no change.
