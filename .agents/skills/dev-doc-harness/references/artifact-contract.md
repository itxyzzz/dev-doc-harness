# Artifact Contract

This document is the canonical source for repository work item artifact layout, lifecycle rules, and variance handling. A work item can be a feature, bug fix, prior issue investigation, refactor, migration, documentation/process change, or other substantial body of work. Naming grammar for work IDs, short IDs, artifact filenames, commit messages, and changelog entries is owned by `module:naming` in `references/naming-conventions.md`.

Module: `module:lifecycle`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:lifecycle.work-item-folders` | `## Work item folders` |
| `rule:lifecycle.stage-boundaries` | `## Lifecycle stage boundaries` |
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

## Lifecycle stage boundaries

An explicit operator approval and its planning approval commit freeze a planning package and separate the harness's major lifecycle stages. The frozen package and planning shape determine the recorded next lifecycle stage; a Plan Task or an instruction is never a lifecycle-stage value.

The two established lifecycle shapes use these transitions:

- An explicitly staged small/medium spec freezes for `plan drafting`; a combined small/medium spec-and-plan package freezes for `plan execution`.
- A large/phased anchor spec freezes for `phase-plan drafting`; a phase plan freezes for `phase execution`. An approved amendment records the documented resumed stage from the package it changes.

Draft continuation by ordinary operator instruction and approved-package continuity in the same or a new orchestration session are operational behavior, not lifecycle stages or alternative freeze paths.

## Short artifact ID

Durable planning artifact filenames include a short ID suffix so operators can distinguish files in chat `@` references when a repository contains many work item packages.

Use `rule:naming.fields` and `rule:naming.derived-patterns` to derive `<short-id>` and construct current durable artifact filenames. Examples:

```text
2026-05-25_user-profile-import -> user-profile-import
2026-05-25_PROJ-123_user-profile-import -> PROJ-123_user-profile-import
```

## Work sizes

Small mechanical work may skip the harness unless the operator requests durable artifacts.

Small/medium work is substantial work that one orchestration session can safely coordinate with bounded delegation and a manageable context window. The orchestration session owns scope, decisions, validation, variance, final integration, and the user-facing summary, while any delegated sub-agent work stays limited enough to integrate without another planning hierarchy.

Small/medium examples include one bounded feature, bug fix with nontrivial investigation, prior issue investigation that changes repository state, clear API addition, limited refactor, local persistence change, or documentation/process change with meaningful review or handoff needs.

Large or phased work needs an anchor spec and later phase plans when one orchestration session cannot safely coordinate the whole effort with bounded delegation, when a flat plan would saturate context or reviewability, or when staged review materially reduces risk. Escalation signals include broad multi-step features, complex bug fixes, prior issue investigations with follow-up implementation, cross-service changes, multi-module refactors, migrations, security-sensitive work, sub-agent-heavy work, or work with phase boundaries that need separate approval and execution checkpoints.

Keep uncertain work small/medium until the one-session boundary demonstrably fails. Complexity alone does not make work large/phased when one orchestration session can still retain scope, decisions, validation, variance, integration, and the user-facing result with bounded delegation.

`module:models` in `references/subagent-model-policy.md` owns sub-agent strategy, context strategy, concurrency, model selection, approved-strategy authorization, and final integration ownership. This lifecycle rule decides which planning shape is needed; it does not copy those orchestration mechanics.

## Small/medium planning shape

`rule:lifecycle.planning-shape` makes combined planning the small/medium default. A small/medium work item normally drafts its spec and plan together as one planning package, reviews and freezes that package together, and uses the approved plan as the transition owner for the documented implementation activity.

A spec-only freeze is an explicit staged-planning exception, not an implied intermediate gate. It is valid only when the operator requested or approved the staging. Before review and freeze, the spec must record that operator-requested or operator-approved staging, the reason for staging, identify the spec as the frozen package, and name `plan drafting` as its next lifecycle stage. A generic template heading or continuity preference cannot create this exception.

Large/phased work keeps its existing anchor sequence: the anchor spec freezes before later phase-plan drafting unless combined planning was explicitly requested. For a combined small/medium package, the plan owns the `plan execution` transition. Plan, phase-plan, and amendment freezes use only the documented next lifecycle stage determined by their approved package.

At every freeze boundary, record the planning shape, exact frozen package, and documented next lifecycle stage before applying next-stage-continuity routing. `module:freeze-gate` owns the operator-facing transition after those lifecycle facts are established.

## Small/medium layout

```text
<work-item-path>
  <spec-filename>
  <plan-filename>

  changelog/
    implementation-fragment.md

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
    phase-01-fragment.md

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

Phase plan names are planned future outputs until phase-plan drafting begins. When created later, phase plans should be numbered in execution order and each phase must be safely executable by one orchestration session with bounded delegation. Create handoff files when they are useful for continuity.

## Large or phased planning orchestration

`rule:lifecycle.large-phase-orchestration` owns the large/phased planning state sequence. Other modules own their local mechanics: artifact layout stays in this lifecycle reference, approval checkpoint mechanics stay in `planning-freeze-gates.md`, model and sub-agent choices stay in `subagent-model-policy.md`, and durable quality stays in `durable-planning-quality.md`.

The normal large/phased planning sequence is a rolling loop:

1. Draft the anchor `<spec-filename>`.
2. Stage the anchor-spec planning package for draft review.
3. Freeze the anchor spec after explicit approval and its planning approval commit.
4. Stop before implementation and before phase-plan drafting.
5. Resume phase-plan drafting only after fresh operator instruction, draft and freeze one phase plan, then begin that phase implementation after fresh post-freeze authorization.
6. Record the actual phase outputs, validation, variance, and commit state as inputs to the next phase plan.
7. Draft and freeze the next phase plan from the anchor, amendments, and actual prior-phase outputs; repeat until completion.
8. Batch planning or freezing multiple phases before implementation is an explicit exception only for stable, independently plannable phases.
9. Use an amendment gate for high-impact post-freeze changes.

Combined anchor-spec and phase-plan drafting is allowed only when the operator explicitly requests combined planning and the artifact records that exception.

## Large or phased work item spec as handoff anchor

For large or phased work items, `<spec-filename>` is the central anchor between planning sessions. The initial planning session must preserve all important decisions and context in `<spec-filename>` before later sessions produce phase plans. Follow `rule:lifecycle.large-phase-orchestration` for the sequencing of anchor-spec review, freeze, later phase-plan drafting, phase-plan freeze, and implementation authorization.

`<spec-filename>` must be detailed enough that a fresh planning thread can write `<phase-plan-filename>` without losing Specification Commitments or Architecture Decisions. Include goals, scope, non-scope, assumptions, constraints, risks, Verification Criteria, data and interface decisions, phase decomposition, documentation expectations, known unknowns, and important rejected alternatives.

Phase plans must derive from `<spec-filename>`. If a phase planner discovers missing or ambiguous context, it must update the draft spec before approval and freeze, or create a plan amendment after freeze. Do not let phase plans silently narrow, drop, or reinterpret decisions from the large/phased work item spec.

Follow `durable-planning-quality.md` for the full spec and phase-plan quality bar.

## Superpowers compatibility

When Superpowers is installed and active, use it for brainstorming, planning, TDD, execution, review, and finishing workflows. The harness resolves only known conflicts: canonical artifact location, approved plan form and numbered tasks, approved commit boundaries, freeze and variance routing, review, finishing, and final integration. Other Superpowers methodology remains external and usable inside that envelope.

The full durable package must live under `<work-item-path>` before the harness freeze gate. Applicable project or global `AGENTS.md` guidance overrides Superpowers' default spec and plan locations for harness-managed work. Conditional conversion of Superpowers planning content into the canonical package is required whenever that content will govern the work; do not retain a second durable copy elsewhere.

Superpowers may guide how the planning content is explored and refined, but the canonical approval package is the harness package. After the harness freeze gate, implementation requires the normal fresh post-freeze operator authorization before any Superpowers pre-flight or execution flow begins. Its task briefs, review packages, progress ledgers, and similar execution aids remain ephemeral unless another harness evidence rule independently preserves them; they do not create a second approval route.

The ordered execution-method cascade is:

1. Prefer `superpowers:subagent-driven-development` when Superpowers, usable sub-agents, and the written Plan Tasks fit its execution-controller model.
2. When Superpowers is available but that preferred route is unavailable or unsuitable, use `superpowers:executing-plans`.
3. Host-native execution is the default only when Superpowers is unavailable. Independent review remains the default; `module:models` owns the disclosed, operator-authorized exception when independent review cannot run or the operator declines it.

Host-native execution is not a default while Superpowers is available. A fresh explicit operator execution-start instruction may select another available method, model/profile, reasoning effort, or next-stage continuity. Record that actual selection without a plan amendment solely for the runtime choice; use normal variance handling only when the instruction also changes a material scope, commitment, Plan Task, commit, review, or safety boundary. `module:models` owns the route-specific reviewer contract and `module:freeze-gate` owns the authorization transition.

When Superpowers is unavailable, keep each task independently executable and verifiable with its recorded checks. This fallback is a concise task-quality cue, not a second detailed task-sizing method.

Add documents under `docs/superpowers` only when that directory already exists and contains previous documentation packages from before the current work. This exception exists solely for backward compatibility and continuity. Do not create or seed the directory, an empty placeholder, or package content during the current work to satisfy this condition.

When that condition is satisfied, new files under `docs/superpowers` may exist only as minimal pointer stubs. A valid stub contains:

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

Draft artifacts may be edited until explicit operator approval and the approval commit. After that approval commit, these artifacts are immutable snapshots:

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
| Implementation changelog source | Living | Yes | Before implementation commits | `docs/work-items/<work-id>/changelog/implementation-fragment.md` | See `module:implementation-changelog`; planning artifacts do not create fragments |
| Root changelog consolidation | Living | As needed | At an operator-owned implementation or release checkpoint | `CHANGELOG.md` | See `module:implementation-changelog` |
| Test cases | Snapshot | Yes/No | Before implementation | snapshots/test-cases.snapshot.md | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | deltas/testing-guide.delta.md | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | deltas/operator-manual.delta.md | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | deltas/api-reference.delta.md | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No/Deferred | Before implementation or phase-plan drafting | snapshots/architecture.snapshot.md | Work-item-bound frozen decision snapshot when meaningful architecture decisions are made or depended on |
| Architecture summary delta | Living delta | Yes/No/Deferred | After review | deltas/architecture-summary.delta.md | Optional future input if long-lived architecture docs change outside this work-item snapshot flow |
```

Use `No` only when the artifact is not applicable. Use `Deferred` only with a reason and a later owner or event.

Implementation changelog sources are required only before implementation commits. Root `CHANGELOG.md` is consolidated at operator-owned implementation or release checkpoints; planning work does not create changelog sources.

## Commit messages

All commits made under the harness must use a planned or documented subject. Commit subjects are reviewable planning content: specs, plans, phase plans, and amendments must include the expected approval and implementation subjects that are known at that stage. Operators may request subject wording changes during normal artifact review. One cohesive implementation package is the default commit boundary. Split only at a stable, independently reviewable and revertible boundary with relevant checks passing; task count alone does not determine commit count.

Use `rule:naming.commit-messages` for the current subject grammar, action types, issue-key handling, elaboration snippets, and nonredundancy rules.

The title or elaboration snippet is shared by the durable planning artifact, planned commit row, and implementation changelog heading when an implementation commit is made. Implementation subjects should describe the concrete delivered change or phase output.

Commit subjects and changelog entry titles must stay synchronized:

- The implementation changelog entry heading must follow `rule:naming.changelog-entries` and include the same title or elaboration snippet represented in the implementation commit subject.
- When a commit subject changes during review or implementation, update the
  matching planned commit row and changelog heading before committing.
- When one changelog entry covers multiple commits for the same work item, each
  commit subject must match a listed planned commit row or a clear bullet-level
  title snippet under that changelog heading.

## Variance policy

Frozen specs and plans stay unchanged. Do not rewrite them to hide a deviation.

Record a noteworthy allowed variance in:

```text
<variance-log-path>
```

An equivalent local implementation or validation adjustment may proceed when it
preserves the approved scope, outcome, and the same evidence purpose. Record it
only when it would help a later reader understand the work.

Create an amendment in:

```text
<amendment-filename>
```

and ask the operator before proceeding when a change materially affects the
outcome, architecture, API, data, security, privacy, compliance, scope, or the
validity of required evidence. A different command alone is not material when
it proves the same thing.

## Variance classes

| Class | Example | Agent may proceed? | Required documentation |
|---|---|---:|---|
| Routine | Rename, equivalent helper, or equivalent validation | Yes | Note it only when useful |
| Material | Outcome, architecture, API, data, security, privacy, compliance, scope, or evidence no longer proves the outcome | No | Amend and ask for approval |
