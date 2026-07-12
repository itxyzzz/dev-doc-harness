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

A Specification Commitment is an implementation-neutral normative statement whose authority follows the artifact lifecycle. It is proposed while its artifact is Draft, binds implementation after an approval commit plus normal start authorization, and is authoritative from a handoff snapshot only for that handoff's named planning or review purpose.

Use the exact heading ``### `SPEC-NNN` Specification Commitment — <short title>``. Every commitment records one `Kind`, one `Intent`, optional concise `Concerns`, a normative `Statement`, and optional non-normative rationale. Every implementation obligation belongs in a Statement; rationale, examples, notes, Architecture Decisions, and Verification Criteria must not invent delivery scope.

Keep commitments atomic: clauses that can be implemented, deferred, waived, amended, or verified separately are separate commitments. Behavior-defining scenarios stay in the Statement. Architecture Decisions realize or constrain mapped commitment scope through `Source spec sections`; every selected clause must be supported by a mapped Statement.

`Kind` is one of `Outcome`, `Behavior`, `Quality`, `Constraint`, or `Deliverable`. Choose by precedence: named output, measurable degree, conditional response, restriction/prohibition, otherwise implementation-controlled end state. `Intent` is one of `Establish`, `Change`, `Preserve`, `Maintain`, or `Prevent`. Choose by precedence: prohibition, named regression baseline, ongoing invariant, alteration, otherwise creation. Preservation names its baseline, quality names its threshold or tolerance, and maintenance names its states or time horizon.

## Verification Criteria

A Verification Criterion is a pass/fail conformance proposition, not a procedure or completed result. Use the exact full-name `VER-NNN` heading and require `Covers`, `Criterion`, and `Expected evidence`. Omitted `Applicability` means final completion of the scope or phase delivering all covered commitments. A criterion covers one or more Specification Commitments, never an Architecture Decision directly, and cannot add scope absent from their Statements.

All applicable criteria covering a commitment and all numbered Expected evidence items are conjunctive by default. Alternatives use an explicit `Any one of` group with an equivalence basis. Commands belong in Plan Checks unless a command is itself a stable contractual interface.

Define a single-commitment criterion immediately beneath its commitment with a level-four heading. Define a criterion covering two or more commitments exactly once under `## Cross-cutting Verification Criteria` with a level-three heading. Cross-phase criteria name one owning phase in Applicability; the phase delivering the final prerequisite owns the decision unless the frozen spec says otherwise. Earlier phases preserve partial evidence but cannot report the criterion passed.

## Plan Checks

A Plan Check is the concrete command, test, inspection, analysis, demonstration, or review procedure used to obtain evidence for one or more Verification Criteria. Use ``### `CHECK-NNN` Plan Check — <short title>`` and require `Covers`, `Procedure`, `Expected result`, `Evidence record`, and `Stage or environment`.

Multiple checks mapped to one criterion are conjunctive by default. Equivalent alternatives use an explicit `Any one of` group and equivalence rationale. A `CHECK` ID identifies the frozen procedure contract, not an execution event. A material procedure change follows approved variance or amendment rather than silently changing the meaning of the ID.

## Asymmetric plan coverage

Plans and phase plans keep two complete mappings. The commitment-disposition mapping assigns every in-scope Specification Commitment to one or more Implementation Tasks, verification-only treatment, or an exact frozen-spec reference authorizing a later phase. Plans cannot create deferrals. Architecture Decisions are consumed only under mapped commitments.

The verification-execution mapping assigns every applicable Verification Criterion to one or more Plan Checks and expected evidence stages. Every Plan Check covers a criterion. Every Implementation Task traces to a commitment, incorporated decision, risk mitigation, lifecycle operation, or explicit Plan Check enablement need. Coordinate both mappings through task/check dependencies and stages; neither mapping is a complete Plan alone.

## Conformance status

Executing a Plan Check creates a distinct record containing the `CHECK` ID, execution-instance identity, stage or environment, actual result, evidence location or inline evidence, and pass/fail/blocker status. Repeated executions retain separate records. Check evidence determines Verification Criterion status; applicable criterion statuses contribute to Specification Commitment conformance.

Task completion alone does not establish conformance, and passing checks alone does not complete delivery while required tasks or authorized dispositions remain unresolved. Planning approval and freeze remain lifecycle decisions; optional outcome validation or delivery acceptance is named separately when it exists.

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
