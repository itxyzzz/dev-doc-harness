# Harness Execution Flow Clarity Test Cases

Work ID: `2026-07-27_harness-execution-flow-clarity`
Short ID: `harness-execution-flow-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:snapshot.test-cases`
Policy references: `module:lifecycle`, `module:models`, `module:freeze-gate`, `module:quality`, `rule:lifecycle.planning-shape`, `rule:lifecycle.superpowers-compatibility`, `rule:models.strategy-required`, `rule:models.execution-continuity`, `rule:models.final-review`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:quality.verification-criteria`, `rule:quality.plan-checks`

## Execution-method routing

### `TC-001` Sub-agent-driven development is preferred when it fits

Given Superpowers and usable sub-agent tooling are available and a frozen implementation plan has Plan Tasks suitable for fresh sub-agent runs controlled from one execution session, when the next-stage method is selected, then the plan selects `superpowers:subagent-driven-development` and does not offer a generic execution-mode choice after freeze.

### `TC-002` Executing plans is the installed-Superpowers fallback

Given Superpowers is available but `subagent-driven-development` does not fit or cannot run, when the next-stage method is selected, then the plan selects `superpowers:executing-plans`, records the concrete reason the preferred route was unavailable or unsuitable, and runs it in a new Codex task with the frozen package.

### `TC-003` Native Codex is the default only without Superpowers

Given Superpowers is unavailable, when the default next-stage method is selected, then native or unspecified Codex execution is allowed. Given Superpowers is available and no explicit operator override exists, the same native route is rejected as the default.

### `TC-026` Explicit operator start selection overrides the planned method

Given a frozen plan records a default method and model selection, when the operator's fresh execution-start instruction explicitly selects another available method, model/profile, reasoning effort, or Codex-task continuity, then the execution controller records and uses that selection without requiring or debating a plan amendment solely for the runtime choice. Native execution still requires its independent reviewer. A concrete availability or compatibility blocker is reported, and ordinary variance rules apply only if the instruction also changes scope, Specification Commitments, Plan Tasks, commit boundaries, mandatory review, or another material safety boundary.

## Execution continuity

### `TC-004` Sub-agent-driven development can start in a new Codex task

Given `superpowers:subagent-driven-development` is selected and the harness continuity rule selects `new Codex task`, when execution starts, then the new execution Codex task loads the frozen package, invokes the skill, and remains the execution controller while dispatching fresh sub-agent runs for Plan Tasks and reviews.

### `TC-005` Same-Codex-task execution requires a recorded fit reason

Given `superpowers:subagent-driven-development` is selected, the current model/profile and context are known suitable, and a concrete continuity benefit is recorded, when continuity is selected, then `Run in: same Codex task` is valid. If those suitability facts and the continuity reason are absent, the same value is rejected for substantial work.

### `TC-006` Unknown suitability defaults substantial work to a new Codex task

Given substantial execution has `Current planning Codex task` model/profile and context suitability recorded as `not exposed`, with multiple Plan Tasks, validation cycles, reviewer/fix loops, or meaningful integration work, when continuity is selected, then the recommendation is `Run in: new Codex task` regardless of whether the execution method is sub-agent-driven development or native Codex.

### `TC-007` Continuity does not invent runtime signals

Given the runtime exposes no reliable remaining-context signal, when continuity guidance or fixtures are evaluated, then no numeric context threshold, invented remaining-context estimate, or compaction prediction is required or accepted. The planning conversation is a useful cache rather than authoritative execution input, and any essential chat-only information must be added to the durable package before freeze.

## Reviewer behavior

### `TC-008` Sub-agent-driven review satisfies the review default

Given `superpowers:subagent-driven-development` is selected, when execution and review are described, then the method's independent per-Plan-Task reviewers and final whole-branch reviewer satisfy the review requirement without a duplicate harness review workflow.

### `TC-009` Executing plans states its reviewer capability

Given `superpowers:executing-plans` is selected, when the next-stage summary is rendered, then it preserves its checkpoints and records an independent reviewer when reviewer tooling is available. If unavailable reviewer tooling caused the fallback, it states the execution controller's self-review limitation.

### `TC-010` Native execution requires an independent reviewer

Given native Codex execution is selected because Superpowers is unavailable, when the strategy is validated, then it includes an independent reviewer sub-agent with curated artifacts, a named lens, evidence-backed findings, and integration owned by the execution Codex task.

### `TC-011` Missing mandatory native review blocks execution

Given Superpowers and reviewer sub-agents are both unavailable, when native execution is considered, then the harness stops and reports the unavailable-review blocker. `Sub-agents: None` is not a successful native-execution route.

## Next-stage representation and chat projection

### `TC-012` Drafts recommend and freezes approve

Given a planning artifact is still Draft, when it describes the future stage, then the heading says `Next-stage recommendation`. Given the package is approved and frozen, the corresponding chat and handoff heading says `Approved next stage`.

### `TC-013` Next-stage groups have a fixed readable order

Given a current plan or large-spec strategy block, when the next stage is rendered, then it contains Activity, Orchestration, Model, and Fallbacks and limits in that order. Activity contains `First Plan Task` when applicable; Orchestration contains Method, `Run in`, and `Plan Task reviewers`; Model contains model and reasoning effort.

### `TC-014` Current planning Codex task facts remain separate

Given the runtime does not expose the planning Codex task's model, profile, reasoning effort, or context signal, when the artifact is rendered, then the separate `Current planning Codex task` block may say `not exposed`. The next-stage recommendation remains actionable and does not copy `not exposed` into its required model, effort, method, run location, or review fields.

### `TC-015` This work item renders the corrected recommendation

Given this work item's current model/profile and context suitability are `not exposed` and its plan contains multiple Plan Tasks, validation cycles, reviewer/fix loops, and final integration, when its next-stage card and handoff are rendered, then they say `Run in: new Codex task`, `First Plan Task: TASK-001`, one independent reviewer after each Plan Task, and one final whole-branch reviewer.

### `TC-016` Run location controls artifact loading

Given `Run in: new Codex task`, when the handoff starts, then the execution Codex task loads applicable `AGENTS.md`, the repository-local harness, frozen spec, frozen plan, required snapshots, applicable amendments and variance records, approval commit and expected baseline, first Plan Task, and variance stop condition through `rule:execution-quality.execution-thread-start`. Given `Run in: same Codex task`, it rereads the frozen package after a model switch or other recorded continuity risk before edits.

### `TC-017` Chat shows the next stage at decision boundaries

Given a package is presented for draft review, frozen after approval, or handed to execution, when the execution controller reports the boundary, then chat includes the same compact Activity, Orchestration, Model, and Fallbacks and limits values as the authoritative artifact, using the same Codex-task and Plan-Task terminology.

### `TC-018` Canonical fields distinguish the three task concepts

Given canonical policy, active templates, and operator-facing summaries describe continuity and delegation, when their focused fields are validated, then they distinguish `Codex task`, `Plan Task`, and `sub-agent run` or `sub-agent assignment`. The canonical definition states that `Codex task` is the local product label for the corresponding top-level agent conversation or thread in other tools, including tools such as Claude Code or Google Antigravity, and permits an adapted harness to use its platform-native label. Given no model override, availability problem, or exceptional authorization exists, routine output also omits model-policy source, override scope, expiry, and context-window speculation. Validation does not scan arbitrary prose for every occurrence of `task`.

## Planning-package shape

### `TC-019` Normal small/medium planning creates two artifacts

Given a normal substantial small/medium request, when planning completes, then both `spec_<short-id>.md` and `plan_<short-id>.md` exist in the work-item folder and are presented together for draft review.

### `TC-020` Unauthorized small/medium spec-only planning fails

Given a small/medium spec exists without its companion plan and no operator-requested or operator-approved staged exception is recorded, when draft review or freeze validation runs, then the package is rejected.

### `TC-021` Authorized staged planning remains available

Given the operator explicitly requests or approves staged small/medium planning and the spec records the reason and plan drafting as the next activity, when package validation runs, then the spec-only package is accepted for that boundary.

### `TC-022` Large anchor behavior is unchanged

Given work demonstrably exceeds one-thread coordination or reviewability and is classified large/phased, when the initial planning package is prepared, then anchor-spec-only remains the default and later phase-plan drafting still requires the established fresh instruction.

### `TC-023` Uncertain sizing does not imply large work

Given work is complex but still safely coordinated and reviewed by one execution Codex task with bounded delegation, when lifecycle sizing runs, then the work remains small/medium. Complexity alone does not select anchor-spec-only planning.

## Integration and regression protection

### `TC-024` Source blocks and generated templates stay synchronized

Given strategy, header, handoff, or readiness source blocks change, when the template assembler check runs, then generated small/medium and phase templates match their manifests and contain the approved grouped representation.

### `TC-025` Existing harness contracts remain green

Given implementation is complete, when the full harness validator, changelog lint, and diff checks run, then existing graph, ownership, release, assembly, compatibility, and historical-artifact checks pass without weakening their assertions.

## Approval

- Status: Approved
- Superseded by: None
