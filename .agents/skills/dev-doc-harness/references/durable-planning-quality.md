# Durable Planning Quality

This document is the canonical quality bar for durable specs and phase plans.

## When it applies

Apply this quality bar to all harness-managed specs and plans except very small mechanical edits that do not invoke the harness.

Durable planning is especially important when the work mentions layered plans, future threads, phase plans, preserving a handoff, or work that must be more than a task list.

## Spec quality bar

A durable `spec.md` must preserve the handoff in repository terms. Include the applicable details from the planning discussion:

- Goals and user or operator outcomes.
- Scope, non-scope, and boundaries.
- Domain and data model.
- Public APIs, internal interfaces, config, schemas, and persistence.
- State flow, lifecycle, or control flow.
- Safety, security, privacy, compliance, migration, and rollback rules.
- Tests, validation strategy, and acceptance criteria.
- Triage, debugging, and operational notes.
- Important assumptions, risks, known unknowns, and rejected alternatives.

A chat summary, outline, or heading-only checklist is not a durable spec.

## Phase plan quality bar

Each `plan-phase-*.md` must be executable by a fresh agent or thread. Include:

- Exact input artifacts and context to read.
- Files, directories, modules, interfaces, schemas, APIs, config, or docs likely to change.
- Sequenced tasks with clear ownership and boundaries.
- Test cases and validation commands with expected results.
- Acceptance criteria for the phase.
- Documentation tasks and required changelog update.
- Handoff output expected from the implementing agent.

If a phase plan cannot be executed independently by a fresh thread, split or rewrite it before implementation.

## Handoff preservation check

Before implementation begins, compare the finalized docs against the original handoff and planning discussion:

- No placeholders or unresolved decisions.
- No vague instructions such as "implement the work item" without concrete tasks.
- No important detail lost between `spec.md` and phase plans.
- Every major handoff detail is preserved, adapted, or explicitly deferred with a reason.

If important context is missing before approval, update the draft. If it is discovered after approval, use the variance and amendment process from `artifact-contract.md`.
