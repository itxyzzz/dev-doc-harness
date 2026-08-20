# Harness Execution Flow Clarity Architecture Snapshot

Work ID: `2026-07-27_harness-execution-flow-clarity`
Short ID: `harness-execution-flow-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:snapshot.architecture`
Policy references: `module:architecture`, `module:lifecycle`, `module:models`, `module:quality`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.planning-shape`, `rule:lifecycle.superpowers-compatibility`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:models.execution-continuity`, `rule:models.final-review`, `rule:quality.spec-handoff`

## Purpose

Freeze the agentic and process decisions that implementation must preserve while clarifying the harness's execution route, reviewer behavior, next-stage presentation, and small/medium planning shape.

## Decision ledger

### `DEC-001` Use an ordered execution-method cascade

Selected approach:

1. Prefer `superpowers:subagent-driven-development` when Superpowers and usable sub-agents are available and the written plan's Plan Tasks fit that skill's execution-controller model.
2. If Superpowers is available but the preferred route does not fit or cannot run, use `superpowers:executing-plans`.
3. Use native or unspecified Codex execution by default only when Superpowers is unavailable; a fresh explicit operator start instruction may select it while Superpowers is available.
4. Native execution requires an independent reviewer sub-agent; if it cannot run, stop and report the blocker.
5. Select execution method and Codex-task continuity independently. The preferred route may run in the same Codex task or a new Codex task under the harness continuity rule; the executing-plans fallback runs in a new Codex task with the frozen package; native Codex records and justifies its Codex-task location.
6. Planning approval freezes the default method recommendation. The harness does not ask a second generic method question, but a fresh explicit operator instruction at execution start may replace the method, model/profile, reasoning effort, or Codex-task continuity without an amendment solely for that selection.
7. Interpret Superpowers' `current session` as the execution controller's session. A newly created execution Codex task can load the frozen package, invoke `subagent-driven-development`, and remain the controller while dispatching fresh sub-agent runs for Plan Tasks and reviews.
8. Record the actual execution-start selection. Report a concrete availability or compatibility blocker when necessary; use variance or amendment handling only when the instruction also changes scope, Specification Commitments, Plan Tasks, commit boundaries, mandatory independent review, or another material safety boundary.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:models`, `module:execution-quality`, `module:freeze-gate`, the harness router, and Superpowers compatibility guidance.
3. Interfaces, schemas, config, or infra: current plan execution-method and review-strategy fields; no runtime config or infrastructure.
4. Agentic, process, documentation, or phase boundaries: planning recommendation, approval freeze, post-freeze start, per-Plan-Task review, final review, and reduced-tool fallback.

Source spec sections:

1. `SPEC-001`, `SPEC-002`, `RISK-001`, `RISK-002`, and `RISK-006`.

Validation cues:

1. `VER-001`, `VER-002`, `CHECK-001`, and `CHECK-002`.

Rejected alternatives:

1. Leave the execution method optional and ask after freeze; this reproduces the current non-selection regression.
2. Make native Codex a peer fallback while Superpowers is available; this bypasses the installed workflow contract.
3. Modify Superpowers itself; the harness needs only a local selection rule.
4. Derive `same Codex task` from `subagent-driven-development`; the skill selects the execution mechanics, not whether its controller is the planning or a new Codex task.
5. Require an amendment whenever the operator explicitly changes execution method or model at start; this contradicts existing freeze-gate override authority and creates avoidable negotiation at the authorization boundary.

### `DEC-002` Use one grouped next-stage card and project it into chat

Selected approach:

1. Keep current planning Codex task observations in a separate, short block.
2. Represent the future decision as a recommendation in drafts and an approved next stage only after freeze.
3. Group next-stage values as Activity, Orchestration, Model, and Fallbacks and limits.
4. Use `Run in: same Codex task` or `Run in: new Codex task`; choose that value independently from the execution method and derive artifact loading instead of requesting open-ended continuity prose.
5. Render the same concise values in chat at draft review, approval freeze, and execution handoff boundaries.
6. Keep override, policy-source, expiry, and availability metadata conditional.
7. Add a compact `Execution terminology` section to `module:models` for `Codex task`, `planning Codex task`, `execution Codex task`, `Plan Task`, `sub-agent run` or `sub-agent assignment`, and `execution session`. Define `Codex task` as the local product label for the corresponding top-level agent conversation or thread in other tools, including tools such as Claude Code or Google Antigravity, and allow adapted distributions to use their platform-native label while preserving the distinction. Use those labels in active behavioral fields and operator-facing summaries.
8. For substantial work, default to a new Codex task with curated-artifact handoff when current context or model/profile suitability cannot be verified. Permit the same Codex task only when the current model/profile is known suitable, context is known suitable or immaterial for the work, and a concrete continuity benefit is recorded. Do not use numeric context thresholds or invented compaction claims.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:models`, `module:freeze-gate`, `module:artifact-style`, plan and large-spec strategy source blocks, handoff blocks, and operator-facing documentation.
3. Interfaces, schemas, config, or infra: `schema:plan.small-medium`, `schema:plan.phase`, and `schema:spec.large-phased` presentation fields; no runtime config or infrastructure.
4. Agentic, process, documentation, or phase boundaries: artifact authoring, draft review, freeze reporting, new-Codex-task handoff, and same-Codex-task start.

Source spec sections:

1. `SPEC-003`, `RISK-003`, and `RISK-005`.

Validation cues:

1. `VER-003`, `CHECK-003`, and `CHECK-004`.

Rejected alternatives:

1. Retain the current nine-field approved-selection list and thirteen-field role blocks for routine plans; this keeps the jargon and current-versus-future confusion.
2. Create a second chat-only schema; this would allow artifact and conversation values to drift.
3. Add a broad readability score or jargon linter; focused labels and fixtures provide safer coverage.
4. Add a separate terminology module or glossary reference; `module:models` already owns the affected continuity and sub-agent semantics, while another required route would add ownership and route-budget cost without independent behavior.

### `DEC-003` Guard combined small/medium package completeness

Selected approach:

1. Make the router and small/medium templates require spec and plan creation in the same planning turn.
2. Accept a lone small/medium spec only when an operator-requested or operator-approved staged exception is recorded.
3. Check package completeness before draft review and again before approval freeze.
4. Keep uncertain work small/medium unless the one-thread coordination boundary demonstrably fails.
5. Leave large/phased anchor-spec-only planning unchanged.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:lifecycle`, `module:freeze-gate`, the harness router, small-spec handoff/readiness blocks, and package-shape validator scenarios.
3. Interfaces, schemas, config, or infra: `schema:spec.small-medium` companion-plan and planning-shape expectations; no runtime config or infrastructure.
4. Agentic, process, documentation, or phase boundaries: work sizing, combined drafting, draft review, approval freeze, and staged-plan exception handling.

Source spec sections:

1. `SPEC-004` and `RISK-004`.

Validation cues:

1. `VER-004`, `CHECK-005`, and `CHECK-006`.

Rejected alternatives:

1. Keep the combined default only in lifecycle prose; the current more actionable single-artifact freeze route overrides it in practice.
2. Remove all spec-only planning; large/phased anchors and explicit operator-approved staged work still need that shape.

## Decision drivers

1. Restore the behavior the current default wording claims but does not operationally enforce.
2. Reuse installed Superpowers execution and review mechanics instead of reproducing them in the harness.
3. Give operators a short, actionable next-stage view in the place where they approve or start work.
4. Keep the change proportional: three existing-boundary corrections and one small glossary section in an existing owner, not a new orchestration system or policy module.

## Constraints

1. Preserve current module and rule IDs unless an independent ownership concern becomes unavoidable.
2. Preserve the harness freeze gate, immutable planning snapshots, variance routing, planned commit subjects, and orchestration-owned final integration.
3. Do not edit generated templates without updating their source blocks and running the assembler.
4. Do not infer hidden runtime model, context, plugin, sub-agent availability, remaining-context percentages, or future compaction.
5. Do not begin implementation until this combined package is approved, committed, and followed by a fresh operator start instruction.

## Future durable-doc boundary

1. No repository-level architecture document is required. Current operator documentation will be updated during implementation, and this snapshot remains the work-item decision record.

## Approval

- Status: Approved
- Superseded by: None
