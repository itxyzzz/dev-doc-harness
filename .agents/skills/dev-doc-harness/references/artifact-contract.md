# Artifact Contract

This document is the canonical source for repository work item artifact layout, lifecycle rules, and variance handling. A work item can be a feature, bug fix, prior issue investigation, refactor, migration, documentation/process change, or other substantial body of work. Naming grammar for work IDs, short IDs, artifact filenames, commit messages, and changelog entries is owned by `module:naming` in `references/naming-conventions.md`.

Module: `module:lifecycle`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:lifecycle.work-item-folders` | `## Work item folders` |
| `rule:lifecycle.short-artifact-id` | `## Short artifact ID` |
| `rule:lifecycle.work-sizing` | `## Work sizes` |
| `rule:lifecycle.planning-shape` | `## Small/medium planning shape` |
| `rule:lifecycle.large-anchor-spec` | `## Large or phased work item spec as handoff anchor` |
| `rule:lifecycle.large-phase-orchestration` | `## Large or phased planning orchestration` |
| `rule:lifecycle.superpowers-compatibility` | `## Superpowers compatibility` |
| `rule:lifecycle.work-item-architecture-decisions` | `## Work-item architecture decisions` |
| `rule:lifecycle.immutable-snapshots` | `## Immutable snapshots` |
| `rule:lifecycle.documentation-matrix` | `## Documentation artifact matrix` |
| `rule:lifecycle.variance-policy` | `## Variance policy` and `## Variance classes` |
| `rule:lifecycle.commit-message-format` | `## Commit messages` |
| `rule:lifecycle.changelog-before-commit` | `## Changelog` |

## Work item folders

Each substantial work item uses one folder:

```text
<work-item-path>
```

Use `rule:naming.derived-patterns` and `rule:naming.work-item-paths` for `<work-item-path>` grammar, issue-key placement, separators, and collision handling. Examples:

```text
docs/work-items/2026-05-25_user-profile-import/
docs/work-items/2026-05-25_PROJ-123_user-profile-import/
```

## Short artifact ID

Durable planning artifact filenames include a short ID suffix so operators can distinguish files in chat `@` references when a repository contains many work item packages.

Use `rule:naming.fields` and `rule:naming.derived-patterns` to derive `<short-id>` and construct current durable artifact filenames. Examples:

```text
2026-05-25_user-profile-import -> user-profile-import
2026-05-25_PROJ-123_user-profile-import -> PROJ-123_user-profile-import
```

## Work sizes

Small mechanical work may skip the harness unless the operator requests durable artifacts.

Small/medium work is substantial work that one orchestration thread can safely coordinate with bounded delegation and a manageable context window. The orchestration thread owns scope, decisions, validation, variance, final integration, and the user-facing summary, while any delegated sub-agent work stays limited enough to integrate without another planning hierarchy.

Small/medium examples include one bounded feature, bug fix with nontrivial investigation, prior issue investigation that changes repository state, clear API addition, limited refactor, local persistence change, or documentation/process change with meaningful review or handoff needs.

Large or phased work needs an anchor spec and later phase plans when one orchestration thread cannot safely coordinate the whole effort with bounded delegation, when a flat plan would saturate context or reviewability, or when staged review materially reduces risk. Escalation signals include broad multi-step features, complex bug fixes, prior issue investigations with follow-up implementation, cross-service changes, multi-module refactors, migrations, security-sensitive work, sub-agent-heavy work, or work with phase boundaries that need separate approval and execution checkpoints.

`module:models` in `references/subagent-model-policy.md` owns sub-agent strategy, context strategy, concurrency, model selection, approved-strategy authorization, and final integration ownership. This lifecycle rule decides which planning shape is needed; it does not copy those orchestration mechanics.

## Small/medium planning shape

`rule:lifecycle.planning-shape` makes combined planning the small/medium default. A small/medium work item normally drafts its spec and plan together as one planning package, reviews and freezes that package together, and uses the approved plan as the transition owner for the documented implementation activity.

A small/medium spec-only freeze is an explicit staged-planning exception, not an implied intermediate gate. Before review and freeze, the spec must record the reason for staging, identify the spec as the frozen package, name plan drafting as the next activity, and provide any handoff required for that activity. A generic template heading or continuity preference cannot create this exception.

Large/phased work keeps its existing anchor sequence: the anchor spec freezes before later phase-plan drafting unless combined planning was explicitly requested. Plan, phase-plan, and amendment freezes hand off only to the implementation, replanning, or other next activity documented by their approved package.

At every freeze boundary, record the planning shape, exact frozen package, and documented next activity before applying execution-continuity routing. `module:freeze-gate` owns the operator-facing transition after those lifecycle facts are established.

## Small/medium layout

```text
<work-item-path>
  <spec-filename>
  <plan-filename>

  changelog/
    planning-approval.md
    implementation.md

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
<work-item-path>
  <spec-filename>
  <phase-plan-filename>      # one per concrete phase
  <amendment-filename>

  changelog/
    planning-approval.md
    phase-01.md

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

The normal initial planning package is anchor-spec-only: create `<spec-filename>` plus only the required supporting snapshots, deltas, or handoff files. Do not create concrete `<phase-plan-filename>` files during the anchor-spec planning package unless the operator explicitly requests combined planning.

Phase plan names are planned future outputs until phase-plan drafting begins. When created later, phase plans should be numbered in execution order and each phase must be safely executable by one orchestration thread with bounded delegation. Create handoff files when they are useful for continuity.

## Large or phased planning orchestration

`rule:lifecycle.large-phase-orchestration` owns the large/phased planning state sequence. Other modules own their local mechanics: artifact layout stays in this lifecycle reference, approval checkpoint mechanics stay in `planning-freeze-gates.md`, model and sub-agent choices stay in `subagent-model-policy.md`, and durable quality stays in `durable-planning-quality.md`.

The normal large/phased planning sequence is:

1. Draft the anchor `<spec-filename>`.
2. Stage the anchor-spec planning package for draft review.
3. Freeze the anchor spec after explicit approval or create an explicit handoff snapshot.
4. Stop before implementation and before phase-plan drafting.
5. Resume post-anchor phase-plan drafting only after fresh operator instruction.
6. Freeze one or more phase plans after explicit approval.
7. Begin implementation only after the applicable frozen phase plan and fresh post-freeze operator authorization.
8. Use an amendment gate for high-impact post-freeze changes.

Combined anchor-spec and phase-plan drafting is allowed only when the operator explicitly requests combined planning and the artifact records that exception.

## Large or phased work item spec as handoff anchor

For large or phased work items, `<spec-filename>` is the central anchor between planning sessions. The initial planning session must preserve all important decisions and context in `<spec-filename>` before later sessions produce phase plans. Follow `rule:lifecycle.large-phase-orchestration` for the sequencing of anchor-spec review, freeze, later phase-plan drafting, phase-plan freeze, and implementation authorization.

`<spec-filename>` must be detailed enough that a fresh planning thread can write `<phase-plan-filename>` without losing Specification Commitments or Architecture Decisions. Include goals, scope, non-scope, assumptions, constraints, risks, Verification Criteria, data and interface decisions, phase decomposition, documentation expectations, known unknowns, and important rejected alternatives.

Phase plans must derive from `<spec-filename>`. If a phase planner discovers missing or ambiguous context, it must update the draft spec before approval and freeze, or create a plan amendment after freeze. Do not let phase plans silently narrow, drop, or reinterpret decisions from the large/phased work item spec.

Follow `durable-planning-quality.md` for the full spec and phase-plan quality bar.

## Superpowers compatibility

When Superpowers is installed and active, use Superpowers for brainstorming, planning, TDD, execution, review, and finishing workflows. This harness only controls where approved artifacts live and what documentation lifecycle decisions must be recorded.

The full durable package must live under `<work-item-path>` before the harness freeze gate. If Superpowers produces specs or plans elsewhere, copy or convert the approved content into the harness work item folder before implementation begins.

Superpowers may guide how the planning content is explored and refined, but the canonical approval package is the harness package. After the harness freeze gate, implementation requires the normal fresh post-freeze operator authorization before any Superpowers execution flow begins.

If Superpowers creates or expects files under `docs/superpowers`, those files may exist only as minimal pointer stubs. A valid stub contains:

- A title.
- A status.
- A link to the canonical package or artifact under `<work-item-path>`.

Do not duplicate full specs or plans under `docs/superpowers`, and do not maintain a second source of truth for harness-managed artifacts.

## Work-item architecture decisions

`rule:lifecycle.work-item-architecture-decisions` owns when architectural decisions are captured for a work item. Work-item architecture means consequential boundaries or tradeoffs across repositories, components, interfaces, data models, config, infrastructure, agentic or process orchestration, security, privacy, compliance, migration, rollout, rollback, or phase ownership.

Architectural decisions belong in the draft spec and, when the decision record needs dedicated shape, in `snapshots/architecture.snapshot.md`. A spec may summarize simple architectural decisions inline. Use `snapshots/architecture.snapshot.md` when the work makes or depends on meaningful architecture decisions, when multiple boundaries or alternatives need preservation, when a future phase or fresh thread will depend on the decision, or when the operator asks for architecture to be explicit.

The documentation artifact matrix must mark the architecture snapshot as required, not applicable, or deferred. Use required when meaningful work-item architecture decisions are made or depended on. Use not applicable when the work has no architectural decision beyond local implementation mechanics, and record the reason. Use deferred only with a reason plus the owner or event that will resolve it before implementation, phase planning, or approval.

Plans and phase plans consume the approved spec and architecture snapshot as inputs. They may cite architecture to explain sequencing, dependencies, validation, and drift handling, but they must not invent or silently reinterpret architectural decisions that are absent from the approved spec or snapshot. Before freeze, missing architecture is corrected by editing the draft spec or draft architecture snapshot. After freeze, high-impact architecture drift follows `rule:lifecycle.variance-policy` and uses an amendment when the variance class requires operator approval.

`deltas/architecture-summary.delta.md` remains an optional living delta for later project documentation updates. Repository-level durable architecture documents such as `ARCHITECTURE.md` are future work for a separate lifecycle extension.

## Planning Artifact Freeze Gate

Run the workflow defined in `planning-freeze-gates.md` whenever durable planning artifacts are ready for operator review, approval, handoff, or freeze. That reference is the canonical source for triggers, required actions, operator reminders, continuation rules, and multi-gate flow for very large or phased work items.

## Immutable snapshots

Draft artifacts may be edited until explicit operator approval and the approval commit, or until explicit handoff. After the approval commit or explicit handoff snapshot, these artifacts are immutable snapshots:

```text
<spec-filename>
<plan-filename>
<phase-plan-filename>
snapshots/*.md
<amendment-filename>
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
| Changelog source | Living | Yes | Before each commit | `docs/work-items/<work-id>/changelog/*.md` | Fragment entries use the changelog heading and metadata grammar; title snippets synchronized with commit subjects |
| Root changelog consolidation | Living | As needed | After merge, before publication or release-note work, or at an operator-owned checkpoint | `CHANGELOG.md` | Consolidated curated publication view generated from reviewed fragments and manual release curation |
| Test cases | Snapshot | Yes/No | Before implementation | snapshots/test-cases.snapshot.md | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | deltas/testing-guide.delta.md | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | deltas/operator-manual.delta.md | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | deltas/api-reference.delta.md | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No/Deferred | Before implementation or phase-plan drafting | snapshots/architecture.snapshot.md | Work-item-bound frozen decision snapshot when meaningful architecture decisions are made or depended on |
| Architecture summary delta | Living delta | Yes/No/Deferred | After review | deltas/architecture-summary.delta.md | Optional future input if long-lived architecture docs change outside this work-item snapshot flow |
```

Use `No` only when the artifact is not applicable. Use `Deferred` only with a reason and a later owner or event.

The matching changelog source fragment is always required before commits. Root `CHANGELOG.md` is consolidated at operator-owned checkpoints, while changelog source fragments are required before commits.

## Commit messages

All commits made under the harness must use a planned or documented subject. Commit subjects are reviewable planning content: specs, plans, phase plans, and amendments must include the expected approval and implementation subjects that are known at that stage. Operators may request subject wording changes during normal artifact review.

Use `rule:naming.commit-messages` for the current subject grammar, action types, issue-key handling, elaboration snippets, and nonredundancy rules.

The title or elaboration snippet is the phrase shared by the durable planning artifact, planned commit row, and the matching changelog source fragment heading or bullet-level snippet. Implementation subjects should be more informative than planning approval subjects and should describe the concrete delivered change or phase output.

Commit subjects and changelog entry titles must stay synchronized:

- The changelog source fragment entry heading for a commit must follow `rule:naming.changelog-entries` and include the same title or elaboration snippet represented in the planned commit subject.
- When a commit subject changes during review or implementation, update the
  matching planned commit row and changelog heading before committing.
- When one changelog entry covers multiple commits for the same work item, each
  commit subject must match a listed planned commit row or a clear bullet-level
  title snippet under that changelog heading.

## Variance policy

Frozen specs and plans are immutable snapshots. Implementation agents must not rewrite frozen artifacts to conceal deviation.

Record nontrivial variance in:

```text
<variance-log-path>
```

Create an immutable amendment in:

```text
<amendment-filename>
```

and request operator approval before proceeding when post-freeze variance affects architecture, public APIs, data models, security, privacy, compliance, scope, Specification Commitments, Verification Criteria, Plan Checks, or plan feasibility.

## Variance classes

| Class | Example | Agent may proceed? | Required documentation |
|---|---|---:|---|
| Mechanical | File rename, equivalent helper extraction, import adjustment | Yes | Record only if non-obvious |
| Local technical | Minor implementation shape differs but behavior, scope, and tests remain the same | Usually yes | Record rationale in the variance log |
| Architectural/API/data/security | Endpoint change, schema change, auth impact, persistence change | No | Create amendment and request approval |
| Scope change | New behavior, removed Specification Commitment, or changed Verification Criterion | No | Create amendment and request approval |
| Plan invalidation | Task no longer feasible as planned | No | Stop and produce replanning note or amendment |

## Changelog

Maintain living changelog source fragments under:

```text
docs/work-items/<work-id>/changelog/*.md
```

Update the matching fragment before every commit. Use `rule:naming.changelog-entries` for entry-heading grammar. Fragment filenames should be stable and descriptive, such as `planning-approval.md`, `implementation.md`, `phase-01.md`, or `validation.md`.

Root `CHANGELOG.md` remains the consolidated publication view. Ordinary independent work-item commits do not edit the root changelog directly unless the work item is intentionally running consolidation or release preparation. Operators consolidate fragments into root `CHANGELOG.md` at project-owned checkpoints such as after merging work branches, before preparing release notes, before a product/application release, or whenever the repository's process needs a complete root changelog.

Use a Keep a Changelog style:

- Newest entries first.
- Each entry heading follows the naming reference and contains the work ID or full commit message plus a useful title or elaboration snippet.
- Entry headings or bullet-level title snippets must stay synchronized with the
  planned commit subjects for the same work.
- Group changes under these headings when applicable: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.
- Keep descriptions concise and tied to specific phases, tasks, specs, or plan decisions.
- Include exactly one `Release target`, `Package impact`, and `Release-note` metadata field in each fragment entry.

Example:

```md
### 2026-05-25 PROJ-123 docs: import-validation -- document duplicate profile checks

Release target: `unreleased`
Package impact: `repository-only`
Release-note: `source-only`

#### Added

- Added validation tasks for duplicate profile identifiers in the phase plan.

#### Changed

- Clarified API Verification Criteria in the spec.
```
