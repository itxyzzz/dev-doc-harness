# Artifact Contract

This document is the canonical source for repository work item artifact layout, lifecycle rules, and variance handling. A work item can be a feature, bug fix, prior issue investigation, refactor, migration, documentation/process change, or other substantial body of work.

Module: `module:lifecycle`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:lifecycle.work-item-folders` | `## Work item folders` |
| `rule:lifecycle.short-artifact-id` | `## Short artifact ID` |
| `rule:lifecycle.work-sizing` | `## Work sizes` |
| `rule:lifecycle.large-anchor-spec` | `## Large or phased work item spec as handoff anchor` |
| `rule:lifecycle.superpowers-compatibility` | `## Superpowers compatibility` |
| `rule:lifecycle.immutable-snapshots` | `## Immutable snapshots` |
| `rule:lifecycle.documentation-matrix` | `## Documentation artifact matrix` |
| `rule:lifecycle.variance-policy` | `## Variance policy` and `## Variance classes` |
| `rule:lifecycle.commit-message-format` | `## Commit messages` |
| `rule:lifecycle.changelog-before-commit` | `## Changelog` |

## Work item folders

Each substantial work item uses one folder:

```text
docs/work-items/<work-id>/
```

Use this work ID format:

```text
YYYY-MM-DD-short-kebab-title
```

When a JIRA key or another issue-tracker ID is available, include it after the date:

```text
YYYY-MM-DD-ISSUE-short-kebab-title
```

Examples:

```text
docs/work-items/2026-05-25-user-profile-import/
docs/work-items/2026-05-25-fix-profile-import-timeout/
docs/work-items/2026-05-25-PROJ-123-user-profile-import/
```

## Short artifact ID

Durable planning artifact filenames include a short ID suffix so operators can distinguish files in chat `@` references when a repository contains many work item packages.

Derive `<short-id>` by removing only the leading `YYYY-MM-DD-` from `<work-id>`. Preserve issue keys.

Examples:

```text
2026-05-25-user-profile-import -> user-profile-import
2026-05-25-PROJ-123-user-profile-import -> PROJ-123-user-profile-import
```

## Work sizes

Small mechanical work may skip the harness unless the operator requests durable artifacts.

Small/medium work includes one bounded feature, bug fix with nontrivial investigation, prior issue investigation that changes repository state, clear API addition, limited refactor, local persistence change, or documentation/process change with meaningful review or handoff needs.

Large or phased work includes broad multi-step features, complex bug fixes, prior issue investigations with follow-up implementation, cross-service changes, multi-module refactors, migrations, security-sensitive work, sub-agent-heavy work, or work that needs phase plans to fit in one implementation thread.

## Small/medium layout

```text
docs/work-items/<work-id>/
  spec-<short-id>.md
  plan-<short-id>.md

  snapshots/
    test-cases.snapshot.md
    architecture.snapshot.md
    api-contract.snapshot.md

  deltas/
    testing-guide.delta.md
    operator-manual.delta.md
    api-reference.delta.md
    architecture-summary.delta.md

  implementation-notes/
    variance-log.md
```

Create only the supplemental snapshot and delta files that are required for the work. The documentation artifact matrix in the spec or plan must mark every listed artifact as required, not applicable, or deferred with a reason.

## Large or phased work item layout

The full lifecycle package for large or phased work may eventually contain these files:

```text
docs/work-items/<work-id>/
  spec-<short-id>.md
  plan-phase-01-discovery-<short-id>.md
  plan-phase-02-core-implementation-<short-id>.md
  plan-phase-03-hardening-<short-id>.md
  plan-amendment-001-short-title-<short-id>.md

  snapshots/
    test-cases.snapshot.md
    architecture.snapshot.md
    api-contract.snapshot.md

  deltas/
    testing-guide.delta.md
    operator-manual.delta.md
    api-reference.delta.md
    architecture-summary.delta.md

  handoff/
    implementation-handoff.md
    review-handoff.md

  implementation-notes/
    variance-log.md
```

The normal initial planning package is anchor-spec-only: create `spec-<short-id>.md` plus only the required supporting snapshots, deltas, or handoff files. Do not create concrete `plan-phase-*-<short-id>.md` files during the anchor-spec planning package unless the operator explicitly requests combined planning.

Phase plan names are planned future outputs until phase-plan drafting begins. When created later, phase plans should be numbered in execution order and each phase must be implementable in one Codex thread. Create handoff files when they are useful for continuity.

## Large or phased work item spec as handoff anchor

For large or phased work items, `spec-<short-id>.md` is the central anchor between planning sessions. The initial planning session must preserve all important decisions and context in `spec-<short-id>.md` before later sessions produce phase plans. The anchor-spec-only initial planning package stops at the spec freeze unless the operator explicitly requests combined planning.

`spec-<short-id>.md` must be detailed enough that a fresh planning thread can write `plan-phase-NN-title-<short-id>.md` without losing requirements or decisions that were discussed earlier. Include goals, scope, non-scope, assumptions, constraints, risks, acceptance criteria, data and interface decisions, phase decomposition, documentation expectations, known unknowns, and important rejected alternatives.

Phase plans must derive from `spec-<short-id>.md`. If a phase planner discovers missing or ambiguous context, it must update the draft spec before approval and freeze, or create a plan amendment after freeze. Do not let phase plans silently narrow, drop, or reinterpret decisions from the large/phased work item spec.

Follow `durable-planning-quality.md` for the full spec and phase-plan quality bar.

## Superpowers compatibility

When Superpowers is installed and active, use Superpowers for brainstorming, planning, TDD, execution, review, and finishing workflows. This harness only controls where approved artifacts live and what documentation lifecycle decisions must be recorded.

The full durable package must live under `docs/work-items/<work-id>/` before the harness freeze gate. If Superpowers produces specs or plans elsewhere, copy or convert the approved content into the harness work item folder before implementation begins.

If Superpowers creates or expects files under `docs/superpowers`, those files may exist only as minimal pointer stubs. A valid stub contains:

- A title.
- A status.
- A link to the canonical package or artifact under `docs/work-items/<work-id>/`.

Do not duplicate full specs or plans under `docs/superpowers`, and do not maintain a second source of truth for harness-managed artifacts.

## Planning Artifact Freeze Gate

Run the workflow defined in `planning-freeze-gates.md` whenever durable planning artifacts are ready for operator review, approval, handoff, or freeze. That reference is the canonical source for triggers, required actions, operator reminders, continuation rules, and multi-gate flow for very large or phased work items.

## Immutable snapshots

Draft artifacts may be edited until explicit operator approval and the approval commit, or until explicit handoff. After the approval commit or explicit handoff snapshot, these artifacts are immutable snapshots:

```text
spec-<short-id>.md
plan-<short-id>.md
plan-phase-*-<short-id>.md
snapshots/*.md
plan-amendment-*-<short-id>.md
```

Allowed post-freeze changes are:

- Append-only errata sections.
- A superseded-by link.
- A new versioned snapshot.
- A new plan amendment.

Do not silently rewrite frozen specs, plans, phase plans, snapshots, or amendments to hide implementation drift.

## Living documentation deltas

Living deltas are proposed updates to long-lived project documentation:

```text
deltas/*.delta.md
```

Use deltas to describe changes that should later be merged into project-level documentation such as testing guides, operator manuals, API references, or architecture summaries. This harness defines where deltas live and when they are required; it does not define detailed schemas for those long-lived documents.

## Documentation artifact matrix

Every substantial spec or plan must include a compact matrix:

```md
## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries grouped by change type; title snippets synchronized with commit subjects |
| Test cases | Snapshot | Yes/No | Before implementation | snapshots/test-cases.snapshot.md | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | deltas/testing-guide.delta.md | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | deltas/operator-manual.delta.md | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | deltas/api-reference.delta.md | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No | Before or after design stabilization | snapshots/architecture.snapshot.md | Work-item-bound decision snapshot |
| Architecture summary delta | Living delta | Yes/No | After review | deltas/architecture-summary.delta.md | Update if long-lived architecture docs change |
```

Use `No` only when the artifact is not applicable. Use `Deferred` only with a reason and a later owner or event.

`CHANGELOG.md` is always required before commits.

## Commit messages

All commits made under the harness must use a planned or documented subject.
Commit subjects are reviewable planning content: specs, plans, phase plans, and
amendments must include the expected approval and implementation subjects that
are known at that stage. Operators may request subject wording changes during
normal artifact review.

Every harness commit subject must start with the work short ID. When the work
ID includes an issue tracking key, the short ID already includes that key; do
not duplicate the issue key as a separate prefix.

Use one subject pattern for all harness commits:

```text
SHORT-ID TYPE: TITLE-SNIPPET
```

Planning approval commits use artifact types:

```text
SHORT-ID spec: TITLE-SNIPPET
SHORT-ID plan: TITLE-SNIPPET
SHORT-ID phase N plan: TITLE-SNIPPET
SHORT-ID amendment NNN: TITLE-SNIPPET
```

Implementation, validation, release, maintenance, and other non-approval commits
use action types. Allowed action types are `feat`, `fix`, `docs`, `test`,
`refactor`, `chore`, `spike`, `release`, and `security`.

Examples:

```text
PROJ-123 spec: user profile import
PROJ-123 chore: update Spring Boot to 3.4
release-versioning release: publish 0.3.0 package notes
```

The title snippet is the human-readable phrase shared by the durable planning
artifact, planned commit row, and `CHANGELOG.md` entry heading or bullet-level
snippet. Implementation snippets should be more informative than planning
approval snippets and should describe the concrete delivered change or phase
output.

Commit subjects and changelog entry titles must stay synchronized:

- The `CHANGELOG.md` entry heading for a commit must include the work ID and the
  same title snippet represented in the planned commit subject.
- When a commit subject changes during review or implementation, update the
  matching planned commit row and changelog heading before committing.
- When one changelog entry covers multiple commits for the same work item, each
  commit subject must match a listed planned commit row or a clear bullet-level
  title snippet under that changelog heading.

## Variance policy

Frozen specs and plans are immutable snapshots. Implementation agents must not rewrite frozen artifacts to conceal deviation.

Record nontrivial variance in:

```text
implementation-notes/variance-log.md
```

Create an immutable amendment in:

```text
plan-amendment-NNN-short-title-<short-id>.md
```

and request operator approval before proceeding when post-freeze variance affects architecture, public APIs, data models, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Variance classes

| Class | Example | Agent may proceed? | Required documentation |
|---|---|---:|---|
| Mechanical | File rename, equivalent helper extraction, import adjustment | Yes | Record only if non-obvious |
| Local technical | Minor implementation shape differs but behavior, scope, and tests remain the same | Usually yes | Record rationale in the variance log |
| Architectural/API/data/security | Endpoint change, schema change, auth impact, persistence change | No | Create amendment and request approval |
| Scope change | New behavior, removed requirement, changed acceptance criteria | No | Create amendment and request approval |
| Plan invalidation | Task no longer feasible as planned | No | Stop and produce replanning note or amendment |

## Changelog

Maintain a living `CHANGELOG.md` at the repository root. Update it before every commit.

Use a Keep a Changelog style:

- Newest entries first.
- Each entry heading is the work ID plus a short descriptive snippet.
- Entry headings or bullet-level title snippets must stay synchronized with the
  planned commit subjects for the same work.
- Group changes under these headings when applicable: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.
- Keep descriptions concise and tied to specific phases, tasks, specs, or plan decisions.

Example:

```md
## 2026-05-25-PROJ-123-user-profile-import: Phase 02 import validation

### Added

- Added validation tasks for duplicate profile identifiers in `plan-phase-02-core-implementation-PROJ-123-user-profile-import.md`.

### Changed

- Clarified API acceptance criteria in `spec-PROJ-123-user-profile-import.md`.
```
