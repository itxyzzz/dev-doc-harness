# Naming Conventions Spec

Work ID: `2026-07-01-naming-conventions`
Short ID: `naming-conventions`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:quality.spec-handoff`

## Goal

Improve readability, searchability, recall, and consistency for harness work-item folder names, planning artifact filenames, commit messages, and changelog entries by centralizing the naming rules in one canonical reference.

## Scope

- Add `.agents/skills/dev-doc-harness/references/naming-conventions.md` as the canonical naming reference for current harness policy.
- Define the granular terms and conventions requested by the operator:
  - `<date>` as `YYYY-MM-DD`.
  - `<issue-key>` as an uppercase tracker key such as `KEY-123`, preserving canonical tracker casing when known.
  - `<short-title>` and `<phase-title>` as lower-kebab-case titles.
  - `<phase-id>` as `phase-NN`.
  - `<work-id>` as `<date>[_<issue-key>]_<short-title>`.
  - `<short-id>` as `[<issue-key>_]<short-title>`.
- Define work-item folder names, file names, collision handling, commit-message grammar, changelog-entry grammar, field separators, title normalization, and elaboration-snippet deduplication.
- Update current reusable harness surfaces so naming policy is referenced from the new file rather than restated in multiple places. Expected surfaces include `artifact-contract.md`, `policy-architecture.md`, `SKILL.md`, current templates, README/operator guidance, role examples, evidence/report guidance, and validation.
- Update harness validation so the new canonical reference is part of the current policy graph and required-file checks.
- Preserve historical work-item artifacts without renaming or rewriting frozen paths.

## Non-scope

- Renaming existing historical work-item folders or frozen planning artifacts under `docs/work-items/`.
- Migrating previous changelog headings or previous commit subjects to the new convention.
- Introducing repository-specific overrides for naming policy in this change.
- Changing release identity, release-note aggregation, or package-boundary policy beyond normal changelog updates for this work.
- Enforcing the new naming grammar in Git hooks or external CI beyond the current harness validation script.

## Current state

The current lifecycle reference owns work-item folder naming, short artifact IDs, commit-message format, and changelog entry guidance directly in `artifact-contract.md`. The current convention uses hyphen-separated work IDs such as `YYYY-MM-DD-short-kebab-title` and file names such as `spec-<short-id>.md`, `plan-<short-id>.md`, `plan-phase-NN-title-<short-id>.md`, and `plan-amendment-NNN-title-<short-id>.md`.

Templates, `SKILL.md`, README guidance, role examples, and validation code repeat or depend on those shapes. That makes the convention discoverable in many places but harder to update consistently.

## Proposed behavior

A new canonical reference, `.agents/skills/dev-doc-harness/references/naming-conventions.md`, owns naming policy as `module:naming`. The lifecycle reference keeps artifact lifecycle ownership but delegates naming mechanics to `module:naming`.

The new convention uses underscores between semantic fields and hyphens inside lower-kebab title fields:

```text
docs/work-items/<work-id>/
<work-id> = <date>[_<issue-key>]_<short-title>
<short-id> = [<issue-key>_]<short-title>
```

Planning artifact filenames use underscore-separated semantic fields:

```text
spec_<short-id>.md
plan_<short-id>.md
plan_<phase-id>_<phase-title>_<short-id>.md
plan_amendment-NNN_<amendment-title>_<short-id>.md
```

Commit messages use:

```text
[<issue-key> ]<type>: <title>[ -- <plain-language-elaboration>]
```

Changelog headings use:

```text
## <date> <full commit message>
```

or:

```text
## <work-id>[ -- <plain-language-elaboration>]
```

The naming reference also defines collision handling by appending a numeric suffix to the final title field, for example `2026-01-01_KEY-123_user-profile-import-2`.

## Interfaces and data

- New canonical reference: `.agents/skills/dev-doc-harness/references/naming-conventions.md`.
- Existing canonical references continue to own lifecycle, freeze, model, quality, release, execution-quality, evidence, and examples. They should reference naming rather than duplicate naming policy.
- Template placeholders and examples change to the new naming grammar.
- The validation script changes its current-surface file list and graph checks so `module:naming` and its rule IDs are recognized.
- Root `CHANGELOG.md` gets the required newest-first entry before implementation and approval commits.

No runtime APIs, schemas, persistence, security-sensitive interfaces, or external services are affected.

## Risks

- The naming convention is self-referential: the work item that introduces it uses the pre-existing harness naming format until the new policy is approved and implemented. Historical artifacts must remain valid and unchanged.
- Current validation may fail if `module:naming` is referenced before its owner file is added to the canonical reference graph.
- Over-updating historical artifacts would violate immutable snapshot expectations and create noisy churn.
- Under-updating templates or router guidance would leave stale examples that future agents may copy.
- Changelog and commit policy transitions can confuse the approval commit for this change; the approval package should use the current frozen policy, while future work follows the new naming reference after implementation.

## Acceptance criteria

- `.agents/skills/dev-doc-harness/references/naming-conventions.md` exists and defines `module:naming` plus searchable rule IDs for fields, work-item paths, artifact filenames, commit messages, changelog entries, collision handling, and normalization.
- `artifact-contract.md` delegates naming mechanics to the new naming reference while retaining lifecycle ownership for work sizing, artifact lifecycle, immutability, variance, documentation matrix, and changelog-before-commit behavior.
- Current templates use the new work ID, short ID, file-name, commit-message, and changelog-entry examples without duplicating long naming policy prose.
- `SKILL.md`, README/operator guidance, role examples, evidence/report guidance, and policy architecture route or cite `module:naming` where naming conventions are discussed.
- `test_harness_policy.py` recognizes the new canonical reference and passes after implementation.
- Historical work-item artifacts are not renamed or rewritten only to match the new convention.
- The changelog entry and planned implementation subject use nonredundant wording.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `naming-conventions spec: define naming convention policy` | `2026-07-01-naming-conventions: define naming convention policy` | Approval commit for this spec, plan, and test-case snapshot under the current harness commit policy. |
| Implementation | `naming-conventions docs: centralize naming convention rules` | `2026-07-01-naming-conventions: centralize naming convention rules` | Applies the naming policy change. The newly introduced commit grammar governs later work after this implementation lands. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries grouped by change type; title snippets synchronized with planned commit subjects |
| Test cases | Snapshot | Yes | Before implementation | `docs/work-items/2026-07-01-naming-conventions/snapshots/test-cases.snapshot.md` | Capture validation expectations for naming policy routing and stale-example prevention |
| Testing guide delta | Living delta | No | Not applicable | Not applicable | No operator test flow change beyond existing harness validator command |
| Operator manual delta | Living delta | No | Not applicable | Not applicable | README/operator guidance updates are direct current-surface implementation work |
| API reference delta | Living delta | No | Not applicable | Not applicable | No public API change |
| Architecture snapshot | Snapshot | No | Not applicable | Not applicable | The module addition is covered in this spec and `policy-architecture.md` implementation updates |
| Architecture summary delta | Living delta | No | Not applicable | Not applicable | No separate long-lived architecture summary is required |

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
