# Naming Conventions

This document is the canonical source for harness naming conventions across work-item folders, durable planning artifact filenames, commit messages, and changelog entries.

Module: `module:naming`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:naming.fields` | `## Fields` |
| `rule:naming.derived-patterns` | `## Derived patterns` |
| `rule:naming.normalization` | `## Normalization` |
| `rule:naming.work-item-paths` | `## Work item paths` |
| `rule:naming.artifact-filenames` | `## Artifact filenames` |
| `rule:naming.commit-messages` | `## Commit messages` |
| `rule:naming.changelog-entries` | `## Changelog entries` |
| `rule:naming.collision-handling` | `## Collision handling` |
| `rule:naming.redundancy-deduplication` | `## Redundancy deduplication` |

## Fields

Use these field names consistently in current harness policy, templates, and examples:

| Field | Meaning |
|---|---|
| `<date>` | Calendar date in `YYYY-MM-DD`. |
| `<issue-key>` | Tracker key such as `KEY-123`. Preserve canonical tracker casing when known; otherwise normalize to uppercase. |
| `<short-title>` | Short lower-kebab-case title. Prefer two to six words. |
| `<phase-id>` | Phase number in `phase-NN` form, such as `phase-01`. |
| `<phase-title>` | Lower-kebab-case phase title. |
| `<artifact-type>` | Planning artifact type such as `spec`, `plan`, `phase N plan`, or `amendment NNN`. |
| `<work-id>` | `<date>[_<issue-key>]_<short-title>`. |
| `<short-id>` | `[<issue-key>_]<short-title>`. |

Include the issue key whenever available. Do not duplicate the issue key in the same name.

## Derived patterns

Use these derived pattern names from other current harness references and templates instead of restating their internal grammar:

| Pattern | Expansion |
|---|---|
| `<work-item-path>` | `docs/work-items/<work-id>/` |
| `<spec-filename>` | `spec_<short-id>.md` |
| `<plan-filename>` | `plan_<short-id>.md` |
| `<phase-plan-filename>` | `plan_<phase-id>_<phase-title>_<short-id>.md` |
| `<amendment-filename>` | `plan_amendment-NNN_<amendment-title>_<short-id>.md` |
| `<variance-log-path>` | `implementation-notes/variance-log.md` |
| `<commit-subject>` | `[<issue-key> ]<type>: <title>[ -- <plain-language-elaboration>]` |
| `<planning-commit-subject>` | `[<issue-key> ]<artifact-type>: <title>[ -- <plain-language-elaboration>]` |
| `<changelog-heading>` | One of the heading forms in `rule:naming.changelog-entries`. |

Use the explicit expansions in this file when creating actual paths, examples, validation fixtures, or migration notes. Use the derived names in lifecycle, quality, freeze-gate, router, and template guidance when the exact spelling is not the point being taught.

## Normalization

Dates use calendar date in `YYYY-MM-DD`.

Titles use lower-kebab-case. Prefer stable nouns over implementation details, remove articles and filler words when possible, and avoid branch-local or temporary wording.

Use `_` between semantic fields and `-` inside kebab-case fields. Do not use spaces in paths. Do not use `_` inside title fields.

Elaboration snippets use plain language. Start lowercase unless a proper noun is needed. Omit the snippet when the kebab title is self-explanatory. Do not repeat the same words as the title unless clarity requires it.

## Work item paths

Each substantial work item uses one folder:

```text
<work-item-path>
```

Use this work ID grammar:

```text
<work-id> = <date>[_<issue-key>]_<short-title>
```

Examples:

```text
docs/work-items/2026-01-01_KEY-123_user-profile-import/
docs/work-items/2026-01-01_user-profile-import/
```

## Artifact filenames

Durable planning artifact filenames use the short ID so operators can distinguish files in chat references when a repository contains many work-item packages.

Use these derived filename patterns:

```text
<spec-filename>
<plan-filename>
<phase-plan-filename>
<amendment-filename>
```

Examples:

```text
spec_KEY-123_user-profile-import.md
plan_KEY-123_user-profile-import.md
plan_phase-01_discovery_KEY-123_user-profile-import.md
plan_amendment-001_validation-scope_KEY-123_user-profile-import.md
```

## Commit messages

Use this subject grammar:

```text
[<issue-key> ]<type>: <title>[ -- <plain-language-elaboration>]
```

Allowed action types are `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `spike`, `release`, and `security`.

Planning approval commits may use artifact types when they are more precise than action types, including `spec`, `plan`, `phase N plan`, and `amendment NNN`.

Examples:

```text
KEY-123 docs: changelog-release-sections -- group changelog by release
KEY-123 fix: profile-import-timeout -- avoid deadlock on slow identity lookup
docs: naming-conventions
release: version-0-3-0
```

## Changelog entries

Use one of these heading grammars:

```text
## <date> <full commit message>
```

```text
## <work-id>[ -- <plain-language-elaboration>]
```

When repository changelogs are grouped by release, apply the same entry grammar beneath the release heading.

## Collision handling

When a generated `<work-id>` collides with an existing folder, append a numeric suffix to the final title field:

```text
2026-01-01_KEY-123_user-profile-import
2026-01-01_KEY-123_user-profile-import-2
```

Use the lowest available positive suffix. Preserve the same suffix in the derived `<short-id>` when it is needed to keep artifact filenames distinct.

## Redundancy deduplication

The elaboration snippet must add useful plain-language context. Omit it when the short kebab title is self-explanatory.

Bad:

```text
docs: changelog-release-sections -- changelog release sections
```

Good:

```text
docs: changelog-release-sections -- group changelog by release
fix: profile-import-timeout
```
