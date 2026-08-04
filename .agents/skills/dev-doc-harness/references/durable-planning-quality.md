# Durable Planning Quality

This document is the canonical quality bar for durable specs and plans, including phase plans.

Module: `module:quality`

Owned rule IDs:

| Rule ID | Local owner |
|---|---|
| `rule:quality.spec-handoff` | `## Spec quality bar` |
| `rule:quality.plan-executable` | `## Plan quality bar` |
| `rule:quality.phase-plan-fresh-thread` | `## Additional phase-plan quality bar` |
| `rule:quality.handoff-preservation` | `## Handoff preservation check` |
| `rule:quality.plain-language` | `## Baseline artifact readability` |
| `rule:quality.specification-commitments` | `### Specification Commitments` |
| `rule:quality.verification-criteria` | `### Verification Criteria` |
| `rule:quality.plan-tasks` | `### Plan Tasks` |
| `rule:quality.plan-checks` | `### Plan Checks` |
| `rule:quality.asymmetric-plan-coverage` | `## Asymmetric plan coverage` |
| `rule:quality.conformance-status` | `## Conformance` |

## When it applies

Apply this quality bar to all harness-managed durable specs and plans.

## Baseline artifact readability

Use `must` for binding obligations and `should` for guidance.

Use short, everyday words. Avoid legalistic authority language and legalistic modal phrasing, inflated status labels, and process narration that does not change a decision. Say what to do and why only when the reason helps the reader act. Prefer scannable sections, lists, and tables over dense prose.

Every durable planning artifact should read as final artifact content. Before approval or handoff, remove authoring scaffolds and resolve every question material to the artifact's documented next activity. A known unknown may remain only when reasonable checking establishes that it does not affect that activity; record why, and record an owner or resolving event when it may affect a later stage.

When a spec, plan, phase plan, snapshot, amendment, report, or handoff becomes large or hard to scan, load `module:artifact-style`. Large anchor specs always load that module.

Mutable external evidence used by an artifact is preserved through `module:evidence` and `rule:evidence.preservation`.

## Spec quality bar

A `<spec-filename>` records goals and scope, decisions and constraints needed to turn the approved scope into an implementation plan:

- Goals and user or operator outcomes.
- Scope boundaries, assumptions, risks, and known unknowns.
- Validation strategy and Verification Criteria.
- Selected architectural decisions, constraints, and any required `snapshots/architecture.snapshot.md`.

Include additional information when it materially affects scope, design, implementation, or verification:

- Relevant domain, interfaces, configuration, data, and persistence.
- Relevant state, data, lifecycle, or control flow.
- Operational or recovery details when they affect the plan.
- Safety, security, privacy, compliance, migration, or rollback behavior.

The durable `<spec-filename>`, together with any required `snapshots/architecture.snapshot.md`, must let a fresh session draft the implementation plan without reconstructing the original discussion.

A chat summary, outline, or heading-only checklist is not a durable spec.

### Specification Commitments

A Specification Commitment states an approved outcome, behavior, quality bar, constraint, or deliverable. Use a stable `SPEC-NNN` ID and a short title. Put the delivery obligation in its Statement; rationale and examples do not add scope.

Keep commitments separate when they can be implemented, changed, or verified separately. Every commitment has a Statement and a local Verification Criterion unless a genuinely cross-cutting criterion explicitly links the shared evidence.

### Verification Criteria

A Verification Criterion says what evidence proves a commitment; it is not a procedure or a result. Use a stable `VER-NNN` ID, link it to the commitments it covers, and state the criterion and expected evidence. Keep a local criterion near its commitment; put genuinely cross-cutting criteria in one shared section.

## Plan quality bar

Each `<plan-filename>` and `<phase-plan-filename>` must be executable from its declared inputs by a fresh executor without inventing scope or reconstructing hidden chat context. Include:

- Exact input artifacts and context to read.
- Files, directories, modules, interfaces, schemas, APIs, config, or docs likely to change.
- A flat list of self-contained tasks with clear ownership and boundaries; dependencies identify tasks that may run in parallel.
- Test cases and validation commands with expected results.
- Plan Tasks with executable checks that link to relevant Verification Criteria.
- Required or deferred documentation outputs assigned to Plan Tasks; before an implementation commit, use `module:implementation-changelog`.
- Handoff output expected from the implementing agent.

Plans consume the approved spec, approved amendments, and any approved architecture snapshot. They may use architecture decisions as implementation inputs, but they must not silently reinterpret frozen architecture or introduce new high-impact architecture decisions. `artifact-contract.md` owns architecture-snapshot eligibility, post-freeze variance, and amendment mechanics.

### Plan Tasks

A Plan Task is a bounded implementation, documentation, or review unit that advances one or more commitments. The executable body is a flat list of self-contained tasks. Use a stable `TASK-NNN` ID and short title. State its outcome and enough dependencies, interfaces, numbered implementation steps, observable exit criteria, and checks for a fresh executor to act without inventing scope.

### Plan Checks

A Plan Check is a command, test, inspection, analysis, demonstration, or review that obtains evidence. It is nested in exactly one Plan Task. Use a stable `CHECK-NNN` ID, name the `VER-NNN` criterion it supports, and describe the evidence purpose, method, expected result, and evidence record. Commands that gather validation evidence belong here rather than in a Verification Criterion.

`Covers` links the check to its Verification Criterion. End-to-end or multi-area verification belongs in an explicit integration or verification task with its own checks; a standalone or shared check is invalid.

The method may change through the variance process when it still proves the same thing; only a material change needs an amendment.

## Additional phase-plan quality bar

Each `<phase-plan-filename>` must also be safely executable by one orchestration session with its recorded bounded delegation. If it cannot meet that bar without hidden context, excessive coordination, or an oversized change boundary, split or rewrite it before implementation.

## Asymmetric plan coverage

Mappings are optional. Use local links between commitments, tasks, criteria, and checks when that is enough to follow the work. Add a complete mapping only when it prevents a coverage gap, supports a fresh handoff, or feeds deterministic validation; state that benefit beside the mapping.

## Conformance

A Plan Check produces evidence for the Verification Criterion it covers. A commitment conforms only when all its applicable Verification Criteria are met. Completing a task alone does not establish conformance. `module:execution-quality` owns recording implementation evidence and criterion status; planning approval and freeze remain lifecycle decisions.

## Handoff preservation check

Before approval or handoff, compare the draft artifacts with the operator-provided source materials, including relevant documents, attachments, tickets, review comments, and chat context. The spec must preserve every material detail affecting outcome, scope, constraints, decisions, risks, or verification. The plan must preserve every remaining material detail affecting its tasks, checks, and handoff.

After freeze, a fresh session must be able to use the approved artifacts as the source of truth without reconstructing the original discussion. If material context is missing before approval and freeze, update the draft. If it is discovered after freeze, use the variance and amendment process from `artifact-contract.md`.
