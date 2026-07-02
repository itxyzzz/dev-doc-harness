# <Work Item Name> Large or Phased Work Spec

Work ID: `<work-id>`
Short ID: `<short-id>`
Status: Draft
Harness release: `<version or unknown>`
Schema: `schema:spec.large-phased`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `rule:lifecycle.large-anchor-spec`, `rule:lifecycle.large-phase-orchestration`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`, `rule:models.strategy-required`, `rule:freeze.multi-gate-flow`

## Goal

Describe the operator-visible or user-visible outcome and why the whole work item needs the large/phased path instead of a small/medium spec and plan.

## Source and Intent

Source input:

- Summarize the operator request, issue, review comments, incident, prior artifact, or external source that started this work.

Desired operator/user outcome:

- Name the end state the operator, user, maintainer, or reviewer should see after all phases are complete.

Success summary:

- State the smallest complete outcome for the full work item in one or two sentences.
- Explain why an anchor spec plus phase plans is needed: one orchestration thread cannot safely coordinate the whole effort with bounded delegation, a flat plan would saturate context or reviewability, or staged review materially reduces risk.

## Scope Boundary

### In scope

- List the behavior, systems, modules, workflows, APIs, data, docs, validation surfaces, or decisions included in the full work item.
- Group related scope into mid-level objectives when that helps later phase decomposition.

### Non-scope

- List nearby work intentionally excluded, deferred, or left unchanged.
- Include follow-ups that should not be absorbed into this large/phased package.

### Assumptions

- Record assumptions that affect phase order, interfaces, data, risk, validation, rollout, or review.
- Use `None identified after repository-context review` only after checking the relevant local context.

### Open questions and known unknowns

- Record unresolved facts or decisions that affect planning, implementation, validation, rollout, or risk.
- For each item, name the owner or later event needed to resolve it.
- Use `None identified after repository-context review` only when there are no known open questions.

## Repository Context

### Current state

- Summarize the relevant repository behavior, architecture, documentation, tests, operational behavior, or process before implementation.

### Evidence read

- List the repository files, docs, tests, prior artifacts, logs, review comments, or external references inspected while drafting.
- Keep this to evidence actually read, not every possible source.

### Constraints and compatibility

- Record compatibility, lifecycle, naming, release, testing, operator-workflow, platform, context-window, security, privacy, migration, or compliance constraints that shape the full work item.

## Requirements

A requirement defines full-work-item scope: what all phases together must provide, change, or preserve. Keep each requirement outcome-focused and independent enough to trace into one or more phase objectives.

Use one block per requirement:

REQ-001: `<specific cross-phase requirement>`

Rationale:

- Explain why this requirement belongs in scope and what value or risk it addresses.

Acceptance links:

- Link to acceptance criterion IDs, or write a short placeholder such as `Covered by AC-001`.

Notes:

- Add constraints, dependencies, deferrals, phase expectations, or implementation-neutral details when helpful.

Requirement quality prompts:

- Specific: names the concrete behavior, documentation surface, interface, or decision.
- Achievable through the planned phase structure.
- Relevant to the stated operator/user outcome.
- Bounded by lifecycle checkpoint, phase boundary, or review gate.
- Testable through at least one acceptance criterion.

## Acceptance Criteria

An acceptance criterion defines observable verification for the full work item or a cross-phase outcome.

Use one block per criterion:

AC-001: `<observable outcome or scenario>`

Verifies:

- Link to requirement IDs or a named scope item.

Method:

- Name the command, manual check, review finding, phase completion signal, or operator acceptance path.

Optional example shape:

- Given `<initial context>`, when `<event or action>`, then `<observable outcome>`.
- Use this only when it makes the outcome clearer than prose.

Acceptance quality prompts:

- Measurable: the outcome can be observed or reviewed.
- Specific: it names the expected result, not only the implementation activity.
- Phase-aware: it says whether verification happens in one phase, across phases, before final integration, or before release.
- Independent enough: each criterion can be checked without relying on unrelated criteria where practical.

## Interfaces, Data, and Control Flow

### Interfaces affected

- Record public APIs, internal interfaces, CLI flags, config, schemas, generated artifacts, templates, docs, or service contracts affected across the full work item.
- State `None` when the work does not affect interfaces.

### Data, config, and persistence

- Record data model, persistence, migration, configuration, release-identity, or rollout effects.
- State `None` when the work does not affect data, config, or persistence.

### State and control flow

- Record lifecycle, routing, state-machine, validation, request flow, jobs, concurrency, retries, or process-flow changes.
- State `None` when the work does not affect state or control flow.

### Safety, security, privacy, migration, and rollback

- Record safety, auth, data exposure, privacy, compliance, migration, rollout, rollback, destructive-operation, and operator-safety considerations.
- State `None identified after repository-context review` only after checking the relevant code and docs.

### Triage, debugging, and operations

- Record logs, metrics, diagnostics, runbooks, failure modes, recovery steps, support workflows, or operational review signals.
- State `None` when not applicable.

## Risks and Rejected Alternatives

Use one block per risk, mitigation, or rejected option:

RISK-001: `<risk, ambiguity, compatibility concern, or rejected alternative>`

Decision or mitigation:

- Record the mitigation, owner, reason for rejection, phase boundary, or follow-up condition.

Notes:

- Include severity or likelihood only when it changes the phase order, validation, rollout, or review approach.

Risk prompts:

- Behavioral or compatibility regressions.
- Migration, security, privacy, compliance, rollout, or operational concerns.
- Phase coupling that might invalidate fresh-thread execution.
- Alternatives rejected because they duplicate canonical harness policy, import too much external process, or create reviewer burden.

## Phase decomposition

Use actual phases for this work item. The output filenames below are future phase-plan outputs, not files to create during the anchor-spec planning package unless combined planning was explicitly requested.

Phase `01`: `<phase name>`

- Objective: `<mid-level objective that advances the full-work-item goal>`.
- Scope: `<included areas or decisions>`.
- Depends on: `<None, prior phase, external event, or approved amendment>`.
- Future phase-plan output: `<phase-plan-filename>`.
- Acceptance focus: `<AC ids or phase-specific review signal>`.

Phase `02`: `<phase name>`

- Objective: `<mid-level objective that advances the full-work-item goal>`.
- Scope: `<included areas or decisions>`.
- Depends on: `<phase ids, artifacts, or external events>`.
- Future phase-plan output: `<phase-plan-filename>`.
- Acceptance focus: `<AC ids or phase-specific review signal>`.

Phase decomposition prompts:

- Each phase should be safely executable by one orchestration thread with bounded delegation.
- Shared setup, discovery, migrations, hardening, and review phases are acceptable when vertical slicing would make task execution less safe.
- If phase objectives are independently plannable, later phase-plan drafting may use curated-artifact sub-agents under `module:models`.

## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this large/phased work item.

Current orchestration:

- Model/profile and reasoning effort if known: `<value or not exposed>`.

Fit assessment:

- Complexity: `<low/medium/high plus reason>`.
- Risk and blast radius: `<low/medium/high plus consequence>`.
- Ambiguity: `<low/medium/high plus reason>`.
- Budget and latency fit: `<acceptable constraints or tradeoff>`.

Recommended orchestration change:

- `<None, or concrete model/profile/reasoning change with reason>`.

Sub-agents:

- `<None with rationale, or bounded strategy below>`.

Prefer curated-artifact sub-agent phase-plan drafting after anchor-spec freeze when phases are independently plannable and platform support is available. For each proposed role, record a short block:

Sub-agent `<role or phase id>`:

- Purpose: `<bounded explorer, reviewer, phase-plan drafter, or worker task>`.
- Context strategy: `<curated prompt / curated artifacts / full-history fork / no repo context>`.
- Input context: `<approved spec, amendments, prior phase outputs, files, docs, or decisions>`.
- Output artifact: `<phase plan, notes, review findings, patch scope, test list, or other deliverable>`.
- Model policy: `<active repository policy unless changed by operator>`.
- Model class/profile: `<policy-relative class or concrete profile if required>`.
- Reasoning effort: `<low/medium/high plus reason>`.
- Selection reason: `<why this delegation is useful>`.
- Parallel execution: `<Yes/No and dependency>`.
- Blast radius if wrong: `<Low/Medium/High plus consequence>`.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and phase-plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

Anchor spec approval:

- Planned subject: `<planning-commit-subject>`.
- Changelog title or snippet: `<changelog-heading>`.
- Notes: `Approval commit for this anchor spec.`

Phase plan approval pattern:

- Planned subject: `<planning-commit-subject>`.
- Changelog title or snippet: `<changelog-heading>`.
- Notes: `Replace or refine in each concrete phase plan.`

Implementation pattern:

- Planned subject: `<commit-subject>`.
- Changelog title or snippet: `<changelog-heading>`.
- Notes: `Replace with concrete rows in phase plans.`

## Planning artifact freeze gates

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.multi-gate-flow`.

Record the draft review, approval commit or handoff snapshot, and pause before implementation, later phase-plan drafting, or later phase execution. The initial planning package is anchor-spec-only by default under `rule:lifecycle.large-phase-orchestration`; do not create concrete phase-plan files during this package unless the operator explicitly requests combined planning.

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
- [ ] Scope, non-scope, assumptions, open questions, and known unknowns are explicit.
- [ ] Requirements are specific, relevant, bounded, and linked to acceptance criteria.
- [ ] Acceptance criteria are observable, testable, and tied to requirements or scope items.
- [ ] Repository evidence and compatibility constraints are recorded.
- [ ] Interfaces, data, control flow, operations, and safety/privacy/migration impacts are checked.
- [ ] Risks and rejected alternatives are listed or explicitly absent after review.
- [ ] Phase decomposition explains why each phase belongs and what future phase-plan output will hold it.
- [ ] Each phase is expected to fit one orchestration thread with bounded delegation, or the spec explains the escalation boundary.
- [ ] Model and sub-agent strategy follows `module:models`, or `Sub-agents: None` has a brief fit rationale.
- [ ] Documentation artifact matrix decisions have paths or reasons.
- [ ] Planned commit subjects and changelog title snippets are synchronized.
- [ ] No unresolved placeholders remain before approval or handoff.

## Approval

- Status: Draft / Approved / Superseded
- Superseded by: record only when this artifact is superseded
