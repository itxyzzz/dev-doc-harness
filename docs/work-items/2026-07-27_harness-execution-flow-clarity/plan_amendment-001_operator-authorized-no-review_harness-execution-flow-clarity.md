# Plan Amendment 001: Operator-Authorized No-Review Execution

Work ID: `2026-07-27_harness-execution-flow-clarity`
Short ID: `harness-execution-flow-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.amendment`
Policy references: `module:lifecycle`, `module:models`, `module:freeze-gate`, `module:execution-quality`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.strategy-required`, `rule:models.final-review`, `rule:naming.derived-patterns`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-001`
- Frozen package: `spec_harness-execution-flow-clarity.md`, `plan_harness-execution-flow-clarity.md`, `snapshots/architecture.snapshot.md`, and `snapshots/test-cases.snapshot.md`
- Approval commit: `219258cfc5a3b79c19175121ed8076976d440701`
- Affected decisions: `SPEC-002`, `DEC-001`, `TC-010`, `TC-011`, plan Global constraint 6, and the native-execution fallback in Approved next stage
- Original instruction: Native execution requires an independent reviewer sub-agent. When reviewer tooling is unavailable, execution stops and reports the unavailable-review blocker; `Sub-agents: None` is not a successful native route.

## Discovered issue

The frozen rule treats unavailable reviewer tooling as an absolute execution blocker. The approved replacement keeps independent review as the agent's default obligation when it can run, while returning the final decision to the operator when independent review is unavailable or explicitly declined.

This is a material safety-boundary change because it replaces the native no-review stop in `SPEC-002`, `DEC-001`, `TC-011`, and the approved implementation plan. Frozen artifacts remain unchanged; this amendment supersedes only the affected instructions named above.

## Proposed change

Replace the native no-review blocker with this operator-decision route:

1. Use an independent reviewer sub-agent whenever the selected route requires review and reviewer tooling is available. Do not present no-review execution as the normal equivalent.
2. When reviewer tooling is unavailable, or when the operator explicitly declines sub-agent review, clearly disclose and record the missing independent review, its reason, the resulting assurance gap, and the focused self-review and validation that will be used instead.
3. If the operator has not already decided, ask once whether to proceed without independent review. No response does not authorize execution; the agent pauses for the decision.
4. An explicit operator instruction to proceed authorizes execution without the reviewer. Record the decision and continue without debating it or requesting repeated confirmation.
5. `Sub-agents: None` is valid for native execution only when the reason and operator authorization are recorded. It is not a silent default when the review requirement is omitted.
6. The completion report states whether independent review ran. If it did not, report the operator decision, the recorded limitation, and the compensating self-review and validation evidence.

The ordered execution-method cascade, independent method and Codex-task-continuity selection, Superpowers checkpoints, execution-controller integration ownership, and all other frozen decisions remain unchanged.

## Implementation tasks

### `AMD-001-TASK-001` Replace the no-review blocker with an operator decision

1. Add focused failing fixtures in `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` for: independently reviewed native execution; unavailable reviewer awaiting an operator decision; operator-authorized no-review execution; operator-declined review with recorded authorization; and invalid silent no-review execution.
2. Update `.agents/skills/dev-doc-harness/references/artifact-contract.md` and `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` with the replacement route and completion-report evidence.
3. Align `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`, `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`, `.agents/skills/dev-doc-harness/SKILL.md`, and `AGENTS.md` with the same disclosure-and-decision boundary.
4. Update `.agents/skills/dev-doc-harness/docs/operator-note.md` only with the concise operational rule. Do not add the operator's rationale or argument to harness guidance.
5. Update `docs/work-items/2026-07-27_harness-execution-flow-clarity/deltas/testing-guide.delta.md`, `deltas/operator-manual.delta.md`, and `changelog/implementation.md` before the implementation commit. Do not rewrite the frozen spec, plan, architecture snapshot, or test-case snapshot.
6. Run the full harness validator, template assembly check, changelog lint, targeted no-review route searches, and `git diff --check`.
7. Commit the amended implementation with the planned subject below.

## Impact assessment

- Outcome: native execution may continue without independent review only after the limitation is disclosed and the operator explicitly authorizes it.
- Evidence: focused fixtures distinguish reviewed, awaiting-decision, authorized-no-review, and silent-no-review states. Full existing validation remains required.
- Interfaces: canonical lifecycle, model/reviewer, execution-start, freeze, router, bootstrap, operator-note, validator, and work-item delta/changelog surfaces change. README wording is not prescribed by this amendment.
- Data, API, infrastructure, security, privacy, and compliance: no runtime or external interface changes.
- Risk: an agent could interpret operator freedom as permission to skip review silently. The explicit authorization and completion-report requirements prevent that interpretation.
- Rollback: revert the amended implementation commit to restore the frozen hard-block behavior.

## Current planning Codex task

- Model/profile: GPT-5, exact resolved profile not exposed.
- Reasoning: not exposed.
- Context visibility: not exposed.

## Next-stage recommendation

### Activity

- Next activity: implement this amendment after approval freeze and fresh authorization.
- First Plan Task: `AMD-001-TASK-001`.

### Orchestration

- Method: `superpowers:executing-plans` for the single tightly coupled policy/test/documentation task.
- Run in: same Codex task after rereading the frozen package and approved amendment.
- Plan Task reviewers: one independent final reviewer is authorized because the change alters a safety boundary.

### Model

- Implementation: balanced tier, medium reasoning; Terra medium when available.
- Final review: flagship tier, medium reasoning; Sol medium when available.

### Fallbacks and limits

- Sub-agents: None for implementation because the task is tightly coupled across one canonical rule and its fixtures.
- If the proposed final reviewer cannot run before this amendment is implemented, follow the currently frozen no-review blocker and ask the operator for direction.
- Stop for a new amendment before changing the ordered method cascade, Codex-task continuity rules, operator-authorization requirement, or any unrelated frozen commitment.

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: operator approved the written amendment in the current Codex task on 2026-07-27.
- Superseded by: None

## Planned commits

| Stage | Planned subject |
|---|---|
| Amendment approval | `amendment 001: harness-execution-flow-clarity -- allow operator-authorized no-review execution` |
| Amended implementation | `fix: harness-execution-flow-clarity -- replace no-review blocker with operator decision` |

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until this amendment is approved and frozen in its own planning commit, followed by fresh operator authorization.
