# Durable Planning Quality

This document is the canonical quality bar for durable specs and phase plans.

Module: `module:quality`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:quality.spec-handoff` | `## Spec quality bar` |
| `rule:quality.phase-plan-fresh-thread` | `## Phase plan quality bar` |
| `rule:quality.handoff-preservation` | `## Handoff preservation check` |
| `rule:quality.specification-commitments` | `## Specification Commitments` |
| `rule:quality.verification-criteria` | `## Verification Criteria` |
| `rule:quality.plan-checks` | `## Plan Checks` |
| `rule:quality.asymmetric-plan-coverage` | `## Asymmetric plan coverage` |
| `rule:quality.conformance-status` | `## Conformance status` |

## When it applies

Apply this quality bar to all harness-managed specs and plans except very small mechanical edits that do not invoke the harness.

Durable planning is especially important when the work mentions layered plans, future threads, phase plans, preserving a handoff, or work that must be more than a task list.

## Baseline artifact readability

Every durable planning artifact should read as final artifact content. Remove
authoring scaffolds before approval or handoff, resolve required decisions and
open questions, give every deferral an owner or resolving event, and prefer
scannable sections, lists, and tables over dense prose.

When a spec, plan, phase plan, snapshot, amendment, report, or handoff becomes
large or hard to scan, load `module:artifact-style`. Large anchor specs always
load that module. Mutable external evidence used by an artifact is preserved
through `module:evidence` and `rule:evidence.preservation`.

## Spec quality bar

A durable `<spec-filename>` must preserve the handoff in repository terms. Include the applicable details from the planning discussion:

- Goals and user or operator outcomes.
- Scope, non-scope, and boundaries.
- Domain and data model.
- Public APIs, internal interfaces, config, schemas, and persistence.
- State flow, lifecycle, or control flow.
- Architectural decisions, including problem-imposed constraints, selected approaches, affected boundaries, rejected alternatives, and any required `snapshots/architecture.snapshot.md`.
- Safety, security, privacy, compliance, migration, and rollback rules.
- Tests, validation strategy, and Verification Criteria.
- Triage, debugging, and operational notes.
- Important assumptions, risks, known unknowns, and rejected alternatives.

A chat summary, outline, or heading-only checklist is not a durable spec.

## Phase plan quality bar

Each `<phase-plan-filename>` must be executable by a fresh agent or thread. Include:

- Exact input artifacts and context to read.
- Files, directories, modules, interfaces, schemas, APIs, config, or docs likely to change.
- Sequenced tasks with clear ownership and boundaries.
- Test cases and validation commands with expected results.
- Verification Criteria and Plan Checks for the phase.
- Documentation tasks and required changelog update.
- Handoff output expected from the implementing agent.

## Specification Commitments

A Specification Commitment states an approved outcome, behavior, quality bar,
constraint, or deliverable. Use a stable `SPEC-NNN` ID and a short title.
Put the delivery obligation in its Statement; rationale and examples do not add
scope.

Keep commitments separate when they can be implemented, changed, or verified
separately. Every commitment has a Statement and a local Verification Criterion
unless a genuinely cross-cutting criterion explicitly links the shared evidence.

## Verification Criteria

A Verification Criterion says what evidence proves a commitment; it is not a
procedure or a result. Use a stable `VER-NNN` ID, link it to the commitments it
covers, and state the criterion and expected evidence. Keep a local criterion
near its commitment; put genuinely cross-cutting criteria in one shared
section. Commands belong in Plan Checks unless the command itself is a stable
interface.

## Plan Checks

A Plan Check is a command, test, inspection, analysis, demonstration, or review
that obtains evidence. Use a stable `CHECK-NNN` ID, name the criterion it
supports, and describe the evidence purpose, method, and expected result. The
method may change through the variance process when it still proves the same
thing; only a material change needs an amendment.

## Asymmetric plan coverage

Mappings are optional. Use local links between commitments, tasks, criteria, and
checks when that is enough to follow the work. Add a complete mapping only when
it prevents a coverage gap, supports a fresh handoff, or feeds deterministic
validation; state that benefit beside the mapping.

## Conformance status

Record check evidence in the form that helps a later reader reproduce or trust
the result. Tasks and checks both matter: completing one does not automatically
complete the other. Planning approval and freeze remain lifecycle decisions.

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
