# New-Task Handoff Visibility Test Cases Snapshot

Work ID: `2026-07-12_new-task-handoff-visibility`
Status: Approved
Harness release: `0.5+`

## Representative cases

### `CASE-001` Configured new-task transition exposes the copy-ready prompt

Given:

1. A planning package is approved and frozen.
2. Its execution continuity is `new task with curated-artifact handoff`.
3. Its implementation inputs include an approved spec, approved plan, required architecture snapshot, test-cases snapshot, an amendment, and evidence.
4. The platform exposes a compatible task-creation action and the frozen strategy records a supported concrete model and reasoning effort.

When:

1. The approval freeze checkpoint produces its post-freeze result.

Then:

1. The current conversation visibly contains a copy-ready new-task handoff.
2. The handoff names every listed current input and applicable `AGENTS.md`/harness guidance.
3. The handoff cites `rule:execution-quality.execution-thread-start`, names the approved strategy/fallback and first activity, and stops for approval-required variance.
4. The handoff does not restate the frozen requirements.
5. The visible result recommends creating the configured new task and asks approval specifically to do so.

### `CASE-002` Approved creation starts the configured task

Given:

1. The conditions of `CASE-001`.
2. The operator explicitly approves creation of the recommended task.

When:

1. The agent invokes the available task-creation action.

Then:

1. The new task receives the visible handoff as its initial prompt.
2. The action uses the exact supported recorded model and reasoning effort.
3. The agent reports the created task without beginning implementation in the source task.

### `CASE-003` New-task transition does not solicit same-task implementation

Given:

1. The conditions of `CASE-001`.

When:

1. The freeze checkpoint produces its post-freeze result.

Then:

1. It does not ask whether implementation should begin in the current task.
2. It may state that continuation in the current task requires an explicit operator direction.

### `CASE-004` Unavailable creation returns the manual fallback

Given:

1. A planning package is approved and frozen with execution continuity `new task with curated-artifact handoff`.
2. The platform has no task-creation action, or its action cannot apply the recorded required model or reasoning effort.

When:

1. The freeze checkpoint produces its post-freeze result.

Then:

1. It visibly reports the unavailable capability or unsupported configuration.
2. It provides the complete copy-ready handoff without creating a task or silently substituting a configuration.

### `CASE-005` Same-task transition preserves current authorization flow

Given:

1. A planning package is approved and frozen with execution continuity `same task`.

When:

1. The freeze checkpoint produces its post-freeze result.

Then:

1. The current-task execution-confirmation/start behavior remains available.
2. Runtime permission, availability/fallback, and approval-required variance controls remain explicit.

### `CASE-006` Template and policy consumers agree

Given:

1. The canonical policy, freeze gate, reusable handoff block, assembly manifests, generated templates, README guidance, Codex adapter contract, and validator have been updated.

When:

1. Template assembly and full harness validation run.

Then:

1. Generated outputs match source blocks and manifests.
2. Validation passes and rejects a stale universal same-task prompt, hidden-only handoff contract, unapproved task creation, or unsupported setting substitution.

### `CASE-007` Combined small/medium planning does not imply a spec handoff

Given:

1. A small/medium work item is using the default combined planning shape.
2. Its draft package contains both the spec and plan, with the plan naming implementation as the next activity.

When:

1. The draft or template is reviewed before the combined approval freeze.

Then:

1. The spec does not independently present a plan-drafting handoff or task-creation offer.
2. The combined package's plan owns the implementation transition after its freeze.

### `CASE-008` Explicit staged and large anchors name planning next steps

Given:

1. One small/medium spec-only package records an explicit staging reason and names plan drafting as its next activity.
2. One large/phased anchor spec names phase-plan drafting as its next activity.
3. Each package records `new task with curated-artifact handoff` and a compatible task-creation capability.

When:

1. Each package completes its appropriate approval freeze checkpoint.

Then:

1. Each result visibly provides its current exact handoff, recommends creation with its recorded configuration, and asks approval to create the planning task it actually names.
2. No result starts the next activity in the source task before that approval.

## Approval

- Status: Approved
