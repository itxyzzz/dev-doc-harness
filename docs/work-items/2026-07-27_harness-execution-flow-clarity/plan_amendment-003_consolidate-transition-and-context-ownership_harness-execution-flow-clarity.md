# Plan Amendment 003: Consolidate Transition and Context Ownership

Work ID: `2026-07-27_harness-execution-flow-clarity`
Short ID: `harness-execution-flow-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.amendment`
Policy references: `module:architecture`, `module:lifecycle`, `module:naming`, `module:models`, `module:freeze-gate`, `module:execution-quality`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.selection-dimensions`, `rule:models.execution-continuity`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`, `rule:execution-quality.execution-thread-start`, `rule:naming.derived-patterns`, `rule:naming.commit-messages`

## Original plan reference

- Amendment ID: `AMD-003`
- Frozen package: `spec_harness-execution-flow-clarity.md`, `plan_harness-execution-flow-clarity.md`, `snapshots/architecture.snapshot.md`, `snapshots/test-cases.snapshot.md`, `plan_amendment-001_operator-authorized-no-review_harness-execution-flow-clarity.md`, and `plan_amendment-002_compact-bootstrap-and-add-skill-metadata_harness-execution-flow-clarity.md`
- Approval commits: `219258cfc5a3b79c19175121ed8076976d440701`, `37f2713f5d28e732b4c5493edbe1f83eaf29bd1a`, and `d886788dc05d746dfa3ae6cf162199dbfde611f0`
- Expected implementation baseline: `f6adf23c990ff167dff426de067b2c0151c94d40`
- Affected decisions and evidence: `SPEC-003` statements 3, 6, and 8; `VER-003`; `DEC-002` statements 3 through 5; `TC-016`; `TC-017`; original plan Change surfaces item 6; `TASK-002` steps 5 and 6; `CHECK-003`; validator checks `execution.thread-start` and `presentation.next-stage-summary`
- Original instruction: `module:models` defines the grouped next-stage selection, `module:freeze-gate` renders it at planning transitions, and `module:execution-quality` starts the selected execution method with deterministic frozen-package loading. The original implementation also put a short grouping cue in `module:artifact-style` and repeated selection and transition details in `module:execution-quality`.

## Discovered issue

Post-implementation review found that the intended ownership split is blurred in current guidance. `context-and-quality-gates.md` repeats the four-group next-stage schema, chat-projection timing, execution-start override behavior, and review fallback details already owned more clearly by `subagent-model-policy.md` and `planning-freeze-gates.md`. The repetition makes the advisory execution-quality module a partial second transition owner and weakens its original environment-independent context-management purpose.

The same review found one related presentation duplication in `artifact-style.md`: a next-stage grouping sentence repeated the model-policy schema without adding a general style rule. The operator has already authorized its removal and the matching self-referential validator cleanup. The operator also unwrapped inconsistent paragraph line breaks in `context-and-quality-gates.md`; those mechanical edits are preserved.

This is a material architecture-ownership correction because it changes the responsibility boundary among `module:models`, `module:freeze-gate`, and `module:execution-quality`, plus the validator evidence for that boundary. Frozen artifacts remain unchanged; this amendment supersedes only the affected ownership and validation instructions named above.

## Proposed change

1. Keep `rule:execution-quality.execution-thread-start` in `context-and-quality-gates.md`. It remains the environment-independent startup protocol for a fresh execution Codex task and for same-task rehydration after a model switch or recorded continuity risk.
2. Keep the full planning-transition flow in `planning-freeze-gates.md`: approval freeze, stop-before-implementation, fresh authorization, grouped chat presentation, runtime override handling, and continuity-selected handoff routing.
3. Keep next-stage field meaning and selection rules in `subagent-model-policy.md`, especially `rule:models.selection-dimensions` and `rule:models.execution-continuity`.
4. Narrow `rule:execution-quality.execution-thread-start` to consume those decisions rather than restate them. It must:
   1. Begin only after the transition and authorization governed by `rule:freeze.stop-before-implementation`.
   2. Consume the approved runtime selection from `rule:models.selection-dimensions` and the same-task or new-task choice from `rule:models.execution-continuity` without reconstructing either.
   3. Load system and runtime constraints, applicable repository instructions, and every frozen artifact and execution input named by the approved handoff.
   4. Verify branch, worktree, approval state, amendments, variance records, and the expected validation baseline before edits.
   5. Treat the frozen package as authoritative, avoid broad rediscovery, begin its documented next activity, and route conflicts through `rule:lifecycle.variance-policy`.
5. Remove from `context-and-quality-gates.md` the repeated four-group definition and field list, draft/freeze/execution chat-projection rule, detailed execution-start override and amendment behavior, and detailed reviewer exception mechanics. Keep only short references where runtime or environment availability makes the dependency relevant.
6. Keep environment compensation and increment quality gates in `module:execution-quality`. They remain responsible for differences among local, web, reduced-tool, and other execution environments.
7. In `planning-freeze-gates.md`, retain the coherent transition and handoff flow and identify `rule:execution-quality.execution-thread-start` as the consumer-side startup protocol. Do not duplicate task-preflight or environment-compensation mechanics there.
8. Clarify the `module:execution-quality` catalog description in `policy-architecture.md` so it owns context loading, execution-start consumption, task preflight, environment compensation, and increment quality gates, not planning-transition or model-selection semantics.
9. Preserve and include the already authorized removal of the next-stage grouping sentence from `artifact-style.md` and its self-referential assertion from `test_harness_policy.py`. General plain-language and scannable-structure guidance remains unchanged.
10. Preserve the operator's line-unwrapping changes in `context-and-quality-gates.md`. Do not rewrap paragraphs or modify unrelated prose solely for formatting.
11. Do not change the next-stage groups, their order or content, runtime override authority, execution-method cascade, review behavior, continuity criteria, freeze authorization, templates, operator-facing behavior, or frozen historical artifacts.

## Implementation tasks

### `AMD-003-TASK-001` Separate transition flow from execution context loading

**Files**

- Modify: `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
- Modify: `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- Modify: `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- Preserve authorized change: `.agents/skills/dev-doc-harness/references/artifact-style.md`
- Modify: `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
- Update: `docs/work-items/2026-07-27_harness-execution-flow-clarity/deltas/testing-guide.delta.md`
- Update: `docs/work-items/2026-07-27_harness-execution-flow-clarity/changelog/implementation.md`
- Do not modify: frozen spec, plan, snapshots, prior amendments, templates, `AGENTS.md`, `SKILL.md`, `README.md`, or `docs/operator-note.md`

**Interfaces**

- Consumes: the approved post-freeze transition from `rule:freeze.stop-before-implementation`, next-stage semantics from `rule:models.selection-dimensions`, continuity from `rule:models.execution-continuity`, the frozen handoff inputs named by the plan, the operator-authorized artifact-style cleanup, and the operator's current line-unwrapping changes.
- Produces: one transition owner, one model-selection owner, a narrower environment-independent execution-start consumer, and validator evidence aligned with those boundaries.

1. Extend `execution.thread-start` validator assertions to require `context-and-quality-gates.md` to cite `rule:freeze.stop-before-implementation`, `rule:models.selection-dimensions`, and `rule:models.execution-continuity` while retaining checks for instruction and frozen-artifact loading, branch or baseline verification, rediscovery avoidance, the named next activity, and variance routing.
2. Update `presentation.next-stage-summary` so grouped chat projection is required from `planning-freeze-gates.md`, not independently from `context-and-quality-gates.md`. Preserve behavioral fixtures and template checks for the four ordered groups, current-versus-next-stage separation, allowed continuity values, and draft/frozen labels.
3. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`. Expected RED result: `execution.thread-start` fails because the current execution-quality rule lacks the three explicit owner references; no unrelated check should fail.
4. Rewrite `## Execution thread start` in `context-and-quality-gates.md` to the narrowed five-step consumer protocol from this amendment. Replace duplicated model, freeze, and review mechanics with short rule or module references. Preserve the file's context-load order, task preflight, environment compensation, increment quality gate, and operator line-unwrapping.
5. Update `planning-freeze-gates.md` only where necessary to name `rule:execution-quality.execution-thread-start` as the protocol that consumes the approved handoff. Keep its transition flow coherent and do not copy execution-quality preflight or environment-compensation details.
6. Update the `module:execution-quality` row in `policy-architecture.md` to state the narrowed ownership boundary without changing module IDs or route budgets.
7. Preserve the already authorized `artifact-style.md` deletion and matching validator cleanup. Confirm no next-stage presentation semantics remain owned by the style module.
8. Run the focused validator again. Expected GREEN result: `PASS execution.thread-start` and `PASS presentation.next-stage-summary`, with all existing checks passing.
9. Update `deltas/testing-guide.delta.md` with the owner-reference and consumer-boundary assertions. Do not update `deltas/operator-manual.delta.md` because operator-visible behavior is unchanged.
10. Prepend a matching implementation entry to `changelog/implementation.md` before the implementation commit.
11. Run the full harness validator, `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`, changelog lint, the installed skill creator's `quick_validate.py`, targeted ownership searches, and `git diff --check`.
12. Inspect the final diff and status. Exclude `.superpowers/sdd/plan_harness-execution-flow-clarity/task-3-report.md` and every other unrelated pre-existing change from staging.
13. Dispatch one independent final reviewer with a policy-ownership and regression lens. Provide this amendment, the affected canonical modules, the changed validator assertions, RED/GREEN evidence, and full validation output. Resolve or report all findings.
14. Commit the reviewed amended implementation with the planned subject below.

## Impact assessment

- Outcome: no operator-visible execution behavior changes. The same approved next-stage selection reaches the same execution method and context; canonical ownership becomes explicit and nonduplicative.
- Evidence: focused owner-reference checks, existing next-stage behavioral fixtures, the full validator, template assembly check, changelog lint, skill validation, targeted searches, and an independent ownership review.
- Interfaces: canonical model, freeze, execution-quality, architecture-catalog, validator, testing-guide delta, and implementation-changelog surfaces. No template or external runtime interface changes.
- Data, API, infrastructure, security, privacy, and compliance: no change.
- Risk: excessive compaction could make execution startup omit a required artifact or authorization boundary. Positive startup-input checks and explicit references to the normative owners preserve those requirements without copying their prose.
- Rollback: revert the amended implementation commit to restore the duplicated execution-quality guidance and style cue.

## Current planning Codex task

- Model/profile: current Codex model; exact resolved profile is not exposed.
- Reasoning: not exposed.
- Context visibility: not exposed.

## Approved next stage

### Activity

- Next activity: implement this amendment after approval freeze and fresh authorization.
- First Plan Task: `AMD-003-TASK-001`.

### Orchestration

- Method: `superpowers:executing-plans` for one tightly coupled canonical-policy and validator task.
- Run in: same Codex task to preserve the operator's line-unwrapping and the already authorized artifact-style and validator working-tree changes.
- Plan Task reviewers: one independent final reviewer with a policy-ownership and regression lens.

### Model

- Implementation: balanced tier, medium reasoning; Terra medium when available.
- Final review: balanced tier, high reasoning; Terra high when available.

### Fallbacks and limits

- Sub-agents: None for implementation because all writable surfaces share one ownership contract and validator boundary. One independent reviewer is the bounded review use.
- If independent review cannot run or the operator declines it, use the approved disclosure and one-time operator-decision route from Amendment 001.
- Stop for another amendment before changing next-stage content, freeze authorization, runtime override authority, execution-method order, reviewer behavior, continuity criteria, module IDs, templates, or operator-visible outcomes.

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: operator approved the staged amendment in the current Codex task on 2026-07-28.
- Superseded by: None

## Planned commits

| Stage | Planned subject |
|---|---|
| Amendment approval | `amendment 003: harness-execution-flow-clarity -- consolidate transition and context ownership` |
| Amended implementation | `refactor: harness-execution-flow-clarity -- separate transition flow from context loading` |

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until this amendment is approved and frozen in its own planning commit, followed by fresh operator authorization.
