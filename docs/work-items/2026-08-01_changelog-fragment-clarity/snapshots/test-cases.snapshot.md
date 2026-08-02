# Changelog Fragment Clarity Test Cases

Work ID: `2026-08-01_changelog-fragment-clarity`
Status: Approved snapshot

## Current filename convention

1. A compact current fragment at `changelog/implementation-fragment.md` passes lint and can be consolidated.
2. A phased current fragment may use `changelog/phase-01-fragment.md` without requiring parser changes.
3. A frozen legacy fragment with an older filename still passes lint and is not renamed.

## Guidance placement

1. Routine authoring and standard consolidation are presented before `Compatibility and legacy support`.
2. Frozen legacy metadata and `--migrate-root` appear only in that final compatibility section.

## Root formatting

1. Migration inserts exactly one blank line between consecutive root entry headings.
2. Migration preserves entry body text and adjacent level-two release headings.
3. A second migration is byte-for-byte identical to the first migrated state.
4. Default consolidation after stable migration makes no change.

## Regression boundary

1. No frozen pre-0.8 release-note or changelog-fragment path changes.
2. Root cleanup does not reintroduce planning-only entries or legacy root metadata.
