# <Work Item Name> Spec

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Describe the user-visible or operator-visible outcome.

## Source and Intent

Source input:

- Summarize the operator request, issue, review comment, incident, or prior artifact that started this work.

Desired operator/user outcome:

- Name the result the operator, user, maintainer, or reviewer should see after the work.

Success summary:

- State the smallest useful outcome in one or two sentences.
- While drafting, use value and scope tradeoffs to split, defer, or re-scope candidate requirements before approval.

## Scope Boundary

### In scope

- List the behavior, files, interfaces, workflows, docs, or validation surfaces included in this change.
- Keep scope bounded enough for small/medium work: one orchestration thread with bounded delegation and a manageable context window.

### Non-scope

- List nearby work intentionally excluded, deferred, or left unchanged.
- Include any tempting follow-up that would make the work large/phased.

### Assumptions

- Record assumptions that are safe to rely on during planning.
- Use `None identified after repository-context review` only after checking the relevant local context.

### Open questions

- Record unresolved decisions, missing operator input, or repo facts that need confirmation.
- For each question, name the owner or later event needed to resolve it.
- Use `None identified after repository-context review` only when there are no known open questions.

## Repository Context

### Current state

- Summarize the relevant repository behavior, documentation, or process before implementation.

### Evidence read

- List the repository files, docs, tests, prior artifacts, logs, or review comments inspected while drafting.
- Keep this to evidence actually read, not every possible source.

### Constraints and compatibility

- Record compatibility, lifecycle, naming, release, testing, operator-workflow, or platform constraints that shape the spec.
- Include context-window or single-thread concerns if the work may exceed small/medium fit.

## Requirements

A requirement defines scope: what the work must provide, change, or preserve. Keep each requirement specific, achievable in this work item, relevant to the desired outcome, and independent enough to review or defer.

Use one block per requirement:

REQ-001: `<specific requirement>`

Rationale:

- Explain why this requirement belongs in scope and what value or risk it addresses.

Acceptance links:

- Link to acceptance criterion IDs, or write a short placeholder such as `Covered by AC-001`.

Notes:

- Add constraints, dependencies, deferrals, or implementation-neutral details when helpful.

Requirement quality prompts:

- Specific: names the concrete behavior, documentation surface, interface, or decision.
- Achievable: fits the approved small/medium boundary and one orchestration thread with bounded delegation.
- Relevant: traces back to the stated operator/user outcome.
- Bounded: has clear lifecycle timing such as before freeze, during validation, or before commit.
- Testable: can be connected to at least one acceptance criterion.

## Acceptance Criteria

An acceptance criterion defines observable verification: how a reviewer, command, manual check, test, or operator acceptance can tell that the requirement has been satisfied.

Use one block per criterion:

AC-001: `<observable outcome or scenario>`

Verifies:

- Link to requirement IDs or a named scope item.

Method:

- Name the command, manual check, review finding, or operator acceptance path.

Optional example shape:

- Given `<initial context>`, when `<event or action>`, then `<observable outcome>`.
- Use this only when it makes the outcome clearer than prose.

Acceptance quality prompts:

- Measurable: the outcome can be observed or reviewed.
- Specific: it names the expected result, not only the implementation activity.
- Time-bounded: it says when verification happens, such as before implementation, during validation, or before commit.
- Independent enough: each criterion can be checked without relying on unrelated criteria where practical.

## Interfaces, Data, and Control Flow

### Interfaces affected

- Record public APIs, internal interfaces, CLI flags, config, schemas, generated artifacts, templates, or docs affected by the change.
- State `None` when the change does not affect interfaces.

### Data, config, and persistence

- Record data model, persistence, migration, configuration, or release-identity effects.
- State `None` when the change does not affect data, config, or persistence.

### State and control flow

- Record lifecycle, routing, state-machine, validation, or process-flow changes.
- State `None` when the change does not affect state or control flow.

### Safety, security, privacy, migration, and rollback

- Record any safety, security, privacy, compliance, migration, rollback, or operational implications.
- State `None identified after repository-context review` only after checking the relevant code and docs.

## Risks and Rejected Alternatives

Use one block per risk, mitigation, or rejected option:

RISK-001: `<risk, ambiguity, compatibility concern, or rejected alternative>`

Decision or mitigation:

- Record the mitigation, owner, reason for rejection, or follow-up boundary.

Notes:

- Include severity or likelihood only when it changes the implementation or review approach.

Risk prompts:

- Behavioral or compatibility regressions.
- Migration, security, privacy, compliance, or operational concerns.
- Over-scoping, under-specifying, or making the work too large for one orchestration thread with bounded delegation.
- Alternatives rejected because they duplicate canonical harness policy, import too much external process, or create reviewer burden.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `<planning-commit-subject>` | `<changelog-heading>` | Approval commit for this spec and related planning artifacts. |
| Implementation | `<commit-subject>` | `<changelog-heading>` | Replace with the expected implementation commit subject, or defer to the plan with a reason. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries grouped by change type; title snippets synchronized with planned commit subjects |
| Test cases | Snapshot | Yes/No | Before implementation | snapshots/test-cases.snapshot.md | Capture expected behavior before code changes |
| Testing guide delta | Living delta | Yes/No | During or after implementation | deltas/testing-guide.delta.md | Update if operator or test flow changes |
| Operator manual delta | Living delta | Yes/No | After implementation | deltas/operator-manual.delta.md | Update if runtime or operator behavior changes |
| API reference delta | Living delta | Yes/No | During or after API work | deltas/api-reference.delta.md | Required for public API changes |
| Architecture snapshot | Snapshot | Yes/No | Before or after design stabilization | snapshots/architecture.snapshot.md | Work-item-bound decision snapshot |
| Architecture summary delta | Living delta | Yes/No | After review | deltas/architecture-summary.delta.md | Update if long-lived architecture docs change |

## Spec readiness checklist

- [ ] Source input and desired outcome are captured.
- [ ] Scope, non-scope, assumptions, and open questions are explicit.
- [ ] Requirements are specific, relevant, bounded, and linked to acceptance criteria.
- [ ] Acceptance criteria are observable, testable, and tied to requirements or scope items.
- [ ] Repository evidence and compatibility constraints are recorded.
- [ ] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [ ] Risks and rejected alternatives are listed or explicitly absent after review.
- [ ] Documentation artifact matrix decisions have paths or reasons.
- [ ] Planned commit subjects and changelog title snippets are synchronized.
- [ ] No unresolved placeholders remain before approval or handoff.

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: record only when this artifact is superseded
