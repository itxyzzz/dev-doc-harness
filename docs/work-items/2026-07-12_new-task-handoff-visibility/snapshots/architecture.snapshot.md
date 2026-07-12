# New-Task Handoff Visibility Architecture Snapshot

Work ID: `2026-07-12_new-task-handoff-visibility`
Status: Approved
Harness release: `0.5+`
Policy references: `module:lifecycle`, `module:models`, `module:execution-quality`, `module:freeze-gate`, `rule:lifecycle.work-item-architecture-decisions`, `rule:models.execution-continuity`, `rule:execution-quality.execution-thread-start`, `rule:freeze.approval-freeze`

## Purpose

Preserve the post-freeze ownership and control-flow decision for visible new-task handoffs so later planning and implementation do not reintroduce a universal same-task start question.

## `DEC-001` Architecture Decision — route the post-freeze response by continuity

Status: Proposed

Source spec sections: `SPEC-001`, `SPEC-002`, `SPEC-003`.

Decision:

1. Keep execution-continuity selection in `module:models`.
2. Make `module:freeze-gate` select the post-freeze conversational result from that approved value at every freeze-to-next-work boundary: anchor spec to phase-plan drafting, plan or phase plan to implementation, and approved amendment to resumed execution or replanning.
3. For `new task with curated-artifact handoff`, display the copy-ready handoff, recommend creation of the new task with the recorded proposed model configuration, and ask approval specifically to create it.
4. After explicit approval, call the exposed platform task-creation action with the displayed handoff as its initial prompt and the exact supported recorded model/reasoning settings.
5. When task creation or the recorded settings are unavailable, display the same handoff as a manual fallback without silently substituting settings.
6. For `same task` and a justified alternative, retain the transition behavior appropriate to the selected route.

Consequences:

1. Planning approval remains a separate unchanged gate.
2. A new-task recommendation no longer creates a contradictory same-task prompt and can create a configured fresh task after approval.
3. Explicit operator direction remains the sole way to override the recommended new-task route and continue in the current task.
4. The portable manual handoff flow remains usable outside Codex or when model settings cannot be applied.

Rejected alternatives:

1. A universal post-freeze question would continue to steer new-task recommendations back into the current thread.
2. Automatic task creation without a post-freeze approval would exceed the authorization boundary.

## `DEC-002` Architecture Decision — derive handoff inputs from the frozen package

Status: Proposed

Source spec sections: `SPEC-001`, `SPEC-004`.

Decision:

1. The handoff lists the exact current frozen inputs required by the implementation plan: spec, plan or phase plan, required snapshots, applicable amendments, evidence, and other plan-named execution inputs.
2. The handoff cites canonical startup and variance rules instead of duplicating the frozen requirements.
3. The frozen package records the proposed model configuration that the creation request displays and the platform adapter attempts to apply exactly.

Consequences:

1. A new task receives sufficient pointers without repository rediscovery.
2. Templates need a clear prompt for current-package enumeration, proposed model configuration, and creation approval rather than a fixed path list.

Rejected alternatives:

1. A generic spec-and-plan-only message can omit required snapshots, amendments, or evidence.
2. Copying requirements into the handoff creates a competing, stale source of truth.

## `DEC-003` Architecture Decision — make planning shape precede continuity routing

Status: Proposed

Source spec sections: `SPEC-006`.

Decision:

1. Classify the package and its actual next activity before rendering a next-task handoff or task-creation offer.
2. Combined small/medium packages draft and freeze spec plus plan together; the plan is the implementation-transition artifact.
3. A small/medium spec-only freeze is an explicit exception that records its reason and targets plan drafting. Large/phased anchor specs target phase-plan drafting by their existing lifecycle rule.
4. Continuity and capability routing apply only after this shape/target decision.

Consequences:

1. Generic handoff prompts cannot create an implied spec-to-plan gate for a combined package.
2. A task-creation prompt always names the activity that its task will actually perform.
3. Intentional isolation remains possible and auditable instead of becoming an accidental workflow fork.

Rejected alternatives:

1. Treating every spec handoff as plan drafting would contradict the small/medium default and hide the lifecycle choice.
2. Removing spec handoffs completely would prevent explicit staged small/medium and large-anchor planning transitions.

## Boundary map

| Owner | Responsibility | Must not own |
|---|---|---|
| `module:models` | Continuity selection and new-task preference | Freeze-gate conversational wording or startup procedure |
| `module:lifecycle` | Package classification and staged-planning exception | Continuity selection or task-creation mechanics |
| `module:freeze-gate` | Post-freeze transition routing, creation approval, and operator-facing result | Changing model-selection policy or execution preflight |
| `module:execution-quality` | Fresh-task rehydration and startup | Selecting continuity or granting runtime permission |
| Handoff template source/manifests | Capture current artifact paths and compact copy-ready prompt shape | Duplicate reusable policy |
| Codex adapter when exposed | Create an approved task with exact supported prompt/model/reasoning settings | Make the portable policy depend on Codex or silently substitute settings |
| Validator | Assert current-surface parity and representative behavior | Serve as an alternate policy owner |

## Validation cues

1. `VER-001` confirms visible, complete, copy-ready new-task handoff content.
2. `VER-002` confirms creation approval and exact configuration propagation.
3. `VER-003` confirms unavailable creation preserves the manual fallback.
4. `VER-004` confirms same-task and justified alternatives preserve authorization limits.
5. `VER-005` confirms canonical consumers and generated templates agree.
6. `VER-006` confirms planning shape and handoff target agree at every freeze boundary.

## Approval

- Status: Approved
- Superseded by: None
