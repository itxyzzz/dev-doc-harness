# Artifact Contract

This document is the canonical source for repository feature artifact layout, lifecycle rules, and variance handling.

## Feature folders

Each substantial feature or change uses one folder:

```text
specs/<feature-id>/
```

Use this feature ID format:

```text
YYYY-MM-DD-short-kebab-title
```

Example:

```text
specs/2026-05-25-user-profile-import/
```

## Work sizes

Small mechanical work may skip the harness unless the operator requests durable artifacts.

Small/medium feature work includes one bounded feature, clear API additions, limited refactors, local persistence changes, or bug fixes with nontrivial investigation.

Large feature work includes broad multi-step features, cross-service changes, multi-module refactors, migrations, security-sensitive work, sub-agent-heavy work, or work that needs phase plans to fit in one implementation thread.

## Small/medium layout

```text
specs/<feature-id>/
  spec.md
  plan.md

  docs/
    snapshots/
      test-cases.snapshot.md
      architecture.snapshot.md
      api-contract.snapshot.md

    living/
      testing-guide.delta.md
      operator-manual.delta.md
      api-reference.delta.md
      architecture-summary.delta.md

  implementation-notes/
    variance-log.md
```

Create only the supplemental snapshot and living-delta files that are required for the work. The documentation artifact matrix in the spec or plan must mark every listed artifact as required, not applicable, or deferred with a reason.

## Large feature layout

```text
specs/<feature-id>/
  spec.md

  phases/
    01-discovery-plan.md
    02-core-implementation-plan.md
    03-hardening-plan.md

  plan-amendments/
    001-short-title.md

  docs/
    snapshots/
      test-cases.snapshot.md
      architecture.snapshot.md
      api-contract.snapshot.md

    living/
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

Phase plan names should be numbered in execution order and each phase must be implementable in one Codex thread. Create handoff files when they are useful for continuity.

## Immutable snapshots

Draft artifacts may be edited until operator approval or explicit handoff. After approval, these artifacts are immutable snapshots:

```text
spec.md
plan.md
phases/*.md
docs/snapshots/*.md
plan-amendments/*.md
```

Allowed post-approval changes are:

- Append-only errata sections.
- A superseded-by link.
- A new versioned snapshot.
- A new plan amendment.

Do not silently rewrite approved specs, plans, phase plans, snapshots, or amendments to hide implementation drift.

## Living documentation deltas

Living deltas are proposed updates to long-lived project documentation:

```text
docs/living/*.delta.md
```

Use deltas to describe changes that should later be merged into project-level documentation such as testing guides, operator manuals, API references, or architecture summaries. This harness defines where deltas live and when they are required; it does not define detailed schemas for those long-lived documents.

## Documentation artifact matrix

Every substantial spec or plan must include a compact matrix:

```md
## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Test cases | Snapshot | Yes/No | Before implementation | docs/snapshots/test-cases.snapshot.md | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | docs/living/testing-guide.delta.md | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | docs/living/operator-manual.delta.md | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | docs/living/api-reference.delta.md | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No | Before or after design stabilization | docs/snapshots/architecture.snapshot.md | Feature-bound decision snapshot |
| Architecture summary delta | Living delta | Yes/No | After review | docs/living/architecture-summary.delta.md | Update if long-lived architecture docs change |
```

Use `No` only when the artifact is not applicable. Use `Deferred` only with a reason and a later owner or event.

## Variance policy

Approved specs and plans are immutable snapshots. Implementation agents must not rewrite approved artifacts to conceal deviation.

Record nontrivial variance in:

```text
implementation-notes/variance-log.md
```

Create an immutable amendment in:

```text
plan-amendments/NNN-short-title.md
```

and request operator approval before proceeding when variance affects architecture, public APIs, data models, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Variance classes

| Class | Example | Agent may proceed? | Required documentation |
|---|---|---:|---|
| Mechanical | File rename, equivalent helper extraction, import adjustment | Yes | Record only if non-obvious |
| Local technical | Minor implementation shape differs but behavior, scope, and tests remain the same | Usually yes | Record rationale in the variance log |
| Architectural/API/data/security | Endpoint change, schema change, auth impact, persistence change | No | Create amendment and request approval |
| Scope change | New behavior, removed requirement, changed acceptance criteria | No | Create amendment and request approval |
| Plan invalidation | Task no longer feasible as planned | No | Stop and produce replanning note or amendment |
