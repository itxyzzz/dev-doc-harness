# Changelog Lifecycle Simplification Architecture Snapshot

Work ID: `2026-08-01_changelog-lifecycle-simplification`
Status: Approved
Harness release: `0.8+`

## Decision

Create a dedicated implementation-stage changelog module. Planning routes no longer create or load changelog source fragments. Implementation routes load the module, write compact current fragments, and use the existing consolidator at an operator-owned checkpoint.

## Entry model

Current entries retain their commit-derived heading and change body, with one metadata line:

```md
Meta -- `unreleased` : `distributable`
```

The first tagged value is the release target. The second is package impact, constrained to `distributable` or `repository-only`. Release-note relevance is no longer entry metadata.

## Compatibility boundary

| Input class | Parser behavior | Root consolidation behavior | Edit policy |
|---|---|---|---|
| Pre-0.8 legacy fragment | Accept existing three-field syntax | Do not reformat; do not require migration | Frozen |
| Post-0.8 legacy fragment | Accept for transition compatibility | Do not add planning-only entries | May migrate only when needed |
| Current compact fragment | Require `Meta --` tagged form | Eligible implementation entries insert newest-first by heading | Current authoring format |
| Root changelog | Migrate remaining entries to compact form | Remove every planning-only section | Curated in place |

## Control flow

```text
Planning package
  -> no changelog fragment
  -> freeze
  -> fresh authorization
Implementation work
  -> compact implementation fragment
  -> validate fragments
  -> operator-owned consolidation
  -> compact root changelog
```

## Invariants

1. No current policy or template requires a planning-only changelog entry.
2. Pre-0.8 release notes and fragments remain byte-for-byte unchanged.
3. Root `CHANGELOG.md` contains no planning-only entry after migration.
4. A second consolidation after a successful first consolidation changes no files.
5. Duplicate entry headings across fragments remain errors.

## Rejected options

1. Retain `Release-note`: rejected because release curation is manual and the field adds routine noise.
2. Remove all metadata: rejected because release-target and impact tags provide compact, validateable routing information.
3. Rewrite frozen fragments: rejected because frozen release evidence must remain untouched.
