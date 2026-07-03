# Durable Planning Quality

This document is the canonical quality bar for durable specs and phase plans.

Module: `module:quality`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:quality.spec-handoff` | `## Spec quality bar` |
| `rule:quality.phase-plan-fresh-thread` | `## Phase plan quality bar` |
| `rule:quality.handoff-preservation` | `## Handoff preservation check` |

## When it applies

Apply this quality bar to all harness-managed specs and plans except very small mechanical edits that do not invoke the harness.

Durable planning is especially important when the work mentions layered plans, future threads, phase plans, preserving a handoff, or work that must be more than a task list.

## Spec quality bar

A durable `<spec-filename>` must preserve the handoff in repository terms. Include the applicable details from the planning discussion:

- Goals and user or operator outcomes.
- Scope, non-scope, and boundaries.
- Domain and data model.
- Public APIs, internal interfaces, config, schemas, and persistence.
- State flow, lifecycle, or control flow.
- Architectural decisions, including problem-imposed constraints, selected approaches, affected boundaries, rejected alternatives, and any required `snapshots/architecture.snapshot.md`.
- Safety, security, privacy, compliance, migration, and rollback rules.
- Tests, validation strategy, and acceptance criteria.
- Triage, debugging, and operational notes.
- Important assumptions, risks, known unknowns, and rejected alternatives.

A chat summary, outline, or heading-only checklist is not a durable spec.

## Phase plan quality bar

Each `<phase-plan-filename>` must be executable by a fresh agent or thread. Include:

- Exact input artifacts and context to read.
- Files, directories, modules, interfaces, schemas, APIs, config, or docs likely to change.
- Sequenced tasks with clear ownership and boundaries.
- Test cases and validation commands with expected results.
- Acceptance criteria for the phase.
- Documentation tasks and required changelog update.
- Handoff output expected from the implementing agent.

Phase plans derive from the approved spec, approved amendments, and any approved architecture snapshot. They may reference architectural decisions as implementation inputs, but they must not silently reinterpret frozen architecture or introduce new high-impact architecture decisions. Missing architecture before freeze is a draft spec or draft snapshot quality issue. Architecture drift discovered after freeze follows the variance and amendment process from `artifact-contract.md`.

If a phase plan cannot be executed independently by a fresh thread, split or rewrite it before implementation.

## Handoff preservation check

Before implementation begins, compare the frozen docs against the original handoff and planning discussion:

- No placeholders or undecided required items.
- No vague instructions such as "implement the work item" without concrete tasks.
- No important detail lost between `<spec-filename>` and phase plans.
- Architectural decisions are preserved in the spec or architecture snapshot before plans depend on them.
- Every major handoff detail is preserved, adapted, or explicitly deferred with a reason.

If important context is missing before approval and freeze, update the draft. If it is discovered after freeze, use the variance and amendment process from `artifact-contract.md`.
