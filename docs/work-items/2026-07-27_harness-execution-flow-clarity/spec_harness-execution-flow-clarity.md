# Harness Execution Flow Clarity Spec

Work ID: `2026-07-27_harness-execution-flow-clarity`
Short ID: `harness-execution-flow-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Policy references: `module:architecture`, `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:artifact-style`, `module:freeze-gate`, `module:execution-quality`, `rule:lifecycle.planning-shape`, `rule:lifecycle.superpowers-compatibility`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:models.strategy-required`, `rule:models.execution-continuity`, `rule:models.final-review`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make the normal post-planning flow predictable and readable: select the appropriate Superpowers execution skill when available, preserve independent review, present the next stage clearly in both durable artifacts and chat, and make combined small/medium planning the unmistakable default.

## Source and intent

Source input:

1. The operator reported six regressions or friction points observed with harness version 0.8: reviewer sub-agents were rarely used, `superpowers:subagent-driven-development` was not selected by default, execution-continuity text became confused, current model facts were mixed with future recommendations, small/medium work often stopped after the spec, and planning language became too jargon-heavy.
2. A read-only review compared the 0.7 and 0.8 release snapshots, current policy and template sources, the installed Superpowers 6.2.0 skills, recent work-item history, and the harness validator.
3. The operator approved three focused change groups and added these decisions:
   1. Prefer `superpowers:subagent-driven-development` when its conditions hold.
   2. When Superpowers is installed but that workflow does not fit or cannot run, use `superpowers:executing-plans`.
   3. Use native or unspecified Codex execution by default only when Superpowers is unavailable; native execution must include an independent reviewer sub-agent even when explicitly selected by the operator.
   4. Group the next-stage summary by activity, orchestration, model, and remaining limits or fallbacks.
   5. Show that next-stage summary in chat instead of leaving it only in a spec or plan.
   6. Retain the proposed combined-planning and validation changes.
   7. Allow an explicit operator instruction at execution start to override the planned execution method, just as the operator may override the planned model selection, without requiring a plan amendment solely for that runtime choice.
4. Side-chat review identified one error in the first draft: it treated the Superpowers execution method as if it mechanically selected the Codex-task location. The correction keeps execution method, Codex-task continuity, and numbered Plan Tasks as separate concepts.

Desired operator outcome:

1. A normal substantial plan tells the operator what happens next without requiring them to choose among execution frameworks or decode model-policy terminology.
2. The planned method starts after the existing freeze and authorization boundary without a second generic question, while an explicit operator start instruction may override that method without an amendment.
3. Independent review is actually used according to the chosen execution route.
4. A normal small/medium request produces a spec and plan together.
5. The planning package and chat use `Codex task`, `Plan Task`, and `sub-agent run` consistently where bare `task` would be ambiguous. `Codex task` is the local product label for the equivalent top-level agent conversation or thread in other tools.

Success summary:

1. The harness keeps its existing modules, freeze gates, artifact locations, model policy, and template assembly while replacing ambiguous defaults with a small deterministic routing contract.
2. Focused validator scenarios protect the routing order, reviewer obligations, readable next-stage presentation, and combined-planning default.

## Scope boundary

### In scope

1. Define the default execution-method order across `superpowers:subagent-driven-development`, `superpowers:executing-plans`, and native Codex execution, plus the operator's explicit execution-start override.
2. Define how independent review is satisfied or required for each route, including the native-execution blocker when no reviewer sub-agent can run.
3. Replace the current dense model-and-sub-agent form with a readable current-planning-Codex-task block and grouped next-stage summary.
4. Keep execution-method selection independent from a plain `same Codex task` or `new Codex task` continuity choice, with deterministic artifact-loading behavior.
5. Require the same grouped next-stage summary in operator-facing chat at draft review, approval freeze, and execution handoff boundaries.
6. Make combined small/medium spec-and-plan drafting operationally dominant and restrict spec-only planning to an explicit operator-requested or operator-approved exception.
7. Add a compact execution terminology section to `module:models`, then use its unambiguous labels in active templates and operator-facing summaries without repeating the full definitions everywhere.
8. Update canonical policy, router guidance, template source blocks, generated templates, operator documentation, and focused validator scenarios needed to deliver these behaviors.

### Non-scope

1. Modify or fork the external Superpowers plugin or its skills.
2. Enumerate every Superpowers skill in harness policy.
3. Add a new policy module, standalone glossary reference, schema family, workflow engine, scheduler, Codex-task creation service, or durable execution artifact.
4. Change the `economy-default` model policy, capability-tier mapping, concurrency cap, freeze authorization boundary, or final integration owner.
5. Rewrite frozen historical work-item artifacts.
6. Change the large/phased anchor-spec-only default or rolling phase-plan lifecycle.
7. Prepare or publish a harness release.

### Assumptions

1. The installed Superpowers skills retain the observed trigger contract: `subagent-driven-development` executes an implementation plan with independent Plan Tasks in the execution controller's current session, while `executing-plans` executes a written plan with checkpoints and is the fallback when the sub-agent-driven route is not usable. The controller's current execution session may be either the planning Codex task or a newly created execution Codex task.
2. Superpowers availability and sub-agent availability are separate facts. Native Codex execution is the default only when Superpowers is unavailable, unless the operator explicitly selects it at execution start; in either case it may proceed only when an independent reviewer sub-agent is available.
3. The existing harness freeze gate remains the only planning-to-execution authorization boundary.
4. Template changes continue through source blocks and assembly manifests; generated templates are not edited as independent sources.

### Open questions

1. None. The operator resolved execution fallback, reviewer, presentation, and planning-shape choices before this combined package was drafted.

## Repository context

### Current state

1. The current repository branch is `0.9-clarifications`, and the package marker is `0.8+`.
2. `module:models` says an independent sub-agent reviewer is the default, while the router, plan template, and validator also make `Sub-agents: None` a routine successful route.
3. Current plan metadata says `Execution method` may be omitted, and the post-freeze compatibility text allows the next operator response to select any method. No active distributed harness guidance names `superpowers:subagent-driven-development` or `superpowers:executing-plans` as the normal method decision.
4. Current strategy templates separate planning observations from an approved execution selection but repeat overlapping model fields, call a future choice approved while the artifact is still a draft, and require open-ended continuity and rehydration explanations.
5. `module:lifecycle` defines combined small/medium planning as the default, but the generic freeze gate accepts a single spec as a reviewable package and the separate small-spec template carries a visible spec-only exception.
6. The current validator passes all checks while accepting the reported behavior, so the missing protection is scenario intent rather than overall validator execution.

### Evidence read

1. `.agents/skills/dev-doc-harness/SKILL.md`.
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
3. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.
4. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
5. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`.
6. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`.
7. `.agents/skills/dev-doc-harness/references/artifact-style.md`.
8. `.agents/skills/dev-doc-harness/references/policy-architecture.md`.
9. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`.
10. Current small/medium and phase template source blocks, assembly manifests, and generated templates under `.agents/skills/dev-doc-harness/assets/templates/`.
11. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
12. `AGENTS.md`, `README.md`, and `.agents/skills/dev-doc-harness/docs/operator-note.md`.
13. `.agents/skills/dev-doc-harness/docs/releases/0.8.0.md` and the 0.7-to-0.8 git history.
14. Installed Superpowers 6.2.0 `subagent-driven-development`, `executing-plans`, `writing-plans`, and `using-superpowers` skill sources.

### Constraints and compatibility

1. Canonical reusable semantics stay in their existing owners; templates show the final artifact shape and short prompts only.
2. The external Superpowers skill mechanics remain authoritative inside the harness lifecycle envelope.
3. The harness plan retains scope, numbered Plan Tasks, approved commit boundaries, variance routing, final integration, and freeze behavior when a generic Superpowers default conflicts.
4. The grouped next-stage presentation must use short everyday labels and must not lose the actionable method, Codex-task location, review, model, reasoning, fallback, or stop condition.
5. Validation remains focused and high-signal; it must not become a general natural-language parser.

## Commitments and verification

### `SPEC-001` Select execution by a fixed fallback order

Statement:

1. A substantial implementation plan must select `superpowers:subagent-driven-development` when Superpowers is available and the skill's own conditions hold: a written implementation plan, Plan Tasks suitable for fresh Plan-Task-level sub-agent runs, an execution controller that can remain in its execution session, and usable sub-agent tooling.
2. When Superpowers is available but the sub-agent-driven route does not fit or cannot run, the plan must select `superpowers:executing-plans`.
3. Absent a fresh explicit operator override, native or unspecified Codex execution is permitted only when Superpowers is unavailable.
4. Execution method and Codex-task continuity are selected independently. `subagent-driven-development` may run in the same Codex task or a new Codex task according to the harness continuity rule. `executing-plans` runs in a new Codex task with the frozen package because it is the separate-session execution route. Native Codex records and justifies `same Codex task` or `new Codex task`.
5. The approved plan owns the default method recommendation. After freeze, the harness must not ask a second generic execution-method question.
6. A fresh, explicit operator instruction at execution start may replace the planned execution method, model/profile, reasoning effort, or Codex-task continuity. The execution controller must accept and record the available operator-selected values without requiring or debating a plan amendment solely for that selection. It may report a concrete availability or compatibility blocker, and ordinary variance rules still apply if the instruction changes scope, Specification Commitments, Plan Tasks, commit boundaries, mandatory independent review, or another material safety boundary.

#### `VER-001` Execution routing is deterministic

Covers: `SPEC-001`.

Criterion: Canonical guidance, current plan templates, and focused scenarios express and preserve the default ordered route `subagent-driven-development` -> `executing-plans` -> native Codex, with native Codex reached by default only when Superpowers is unavailable, while a fresh explicit operator start instruction can select another available method without an amendment.

Expected evidence: Validator fixtures for each branch, active-guidance searches, generated-template inspection, and a clean full harness validation run.

### `SPEC-002` Preserve independent review across routes

Statement:

1. `superpowers:subagent-driven-development` satisfies independent review through its per-Plan-Task reviewers and final whole-branch reviewer.
2. `superpowers:executing-plans` must preserve its own review checkpoints and the harness's independent-review default when reviewer tooling is available; when its fallback reason is unavailable sub-agent tooling, the plan must state the orchestration-thread review limitation instead of pretending an independent reviewer ran.
3. Native Codex execution must use an independent reviewer sub-agent with curated artifacts, a named review lens, evidence-backed findings, and final integration retained by the execution Codex task.
4. If Superpowers and independent reviewer sub-agents are both unavailable, native execution must stop and surface the unavailable-review blocker instead of silently proceeding without the mandatory review.

#### `VER-002` Review behavior follows the selected method

Covers: `SPEC-002`.

Criterion: Each execution route has an explicit review outcome, native Codex cannot pass its scenario without an independent reviewer, and unavailability produces a visible stop rather than a `Sub-agents: None` success route.

Expected evidence: Focused reviewer-routing fixtures, plan-template inspection, operator-facing guidance review, and full harness validation.

### `SPEC-003` Present a readable next-stage summary

Statement:

1. Durable planning artifacts must separate current planning Codex task observations from the recommendation for the next stage.
2. A draft artifact must label the future choice as a recommendation; it becomes an approved next stage only after the planning package freezes.
3. The next-stage summary must use these groups in this order:
   1. Activity: the named next activity and first Plan Task when applicable.
   2. Orchestration: execution method, `same Codex task` or `new Codex task`, and reviewer arrangement.
   3. Model: policy-relative model or target profile and reasoning effort.
   4. Fallbacks and limits: availability fallback, required artifact loading, authorization state, and material-variance stop condition only when applicable.
4. Routine artifacts must not require model-policy source, override scope, expiry, context speculation, or similar administrative fields when no override or availability issue exists.
5. `Run in` must accept only `same Codex task` or `new Codex task`. For substantial work, prefer a new Codex task with curated-artifact handoff when current context or model/profile suitability is not exposed or cannot be verified, when the approved profile cannot be reconciled with the current profile, or when multiple Plan Tasks, validation cycles, reviewer/fix loops, or integration work make a clean context safer. Use the same Codex task only when the current model/profile is known suitable, available context is known suitable or context risk is immaterial for the work, and a concrete continuity benefit is recorded.
6. A new execution Codex task always loads the complete frozen package and its execution-start inputs. Same-Codex-task execution rereads the frozen package after a model switch and whenever continuity risk makes the planning conversation an unsafe authority. Agents must not use numeric context thresholds, invent remaining-context estimates, or predict compaction when the runtime does not expose those signals.
7. `module:models` must own a compact terminology section defining `Codex task`, `planning Codex task`, `execution Codex task`, `Plan Task`, `sub-agent run` or `sub-agent assignment`, and the external Superpowers term `execution session`. The definition must state that `Codex task` is the local label for the corresponding top-level agent conversation or thread in other tools, including tools such as Claude Code or Google Antigravity; an adapted harness may use the platform-native label while preserving the same distinction. Active templates and summaries use those terms where bare `task` could be confused; validation stays field- and fixture-focused rather than scanning arbitrary prose.
8. The execution Codex task must render the same concise next-stage groups in chat when it presents a package for draft review, reports an approval freeze, or hands off execution.

#### `VER-003` Next-stage information is readable and visible

Covers: `SPEC-003`.

Criterion: Source and generated templates show the four ordered groups with plain labels, current and future model information cannot be conflated, method does not determine Codex-task location, ambiguous task terms are replaced at behavioral decision points, and freeze/draft-review guidance requires a matching chat summary.

Expected evidence: Template assertions, allowed-value fixtures, operator-documentation inspection, synthetic chat-output checks, and full harness validation.

### `SPEC-004` Make combined small/medium planning the operational default

Statement:

1. A normal small/medium planning request must create the spec and plan in the same planning turn and present them as one draft-review package.
2. Spec-only small/medium planning is allowed only when the operator explicitly requests or approves staged planning and the spec records that decision, its reason, and plan drafting as the next activity.
3. When sizing is uncertain, the work must remain small/medium unless the one-thread coordination and reviewability boundary demonstrably fails; complexity alone must not select the large/phased route.
4. The draft-review and approval-freeze routes must reject a lone small/medium spec that lacks an authorized staged-planning exception.
5. The large/phased anchor-spec-only default remains unchanged.

#### `VER-004` Small/medium packages include both artifacts

Covers: `SPEC-004`.

Criterion: Normal small/medium scenarios require both canonical filenames, an unauthorized spec-only scenario fails, an authorized staged exception succeeds, and a large/phased anchor scenario remains valid.

Expected evidence: Lifecycle and freeze-gate fixtures, router and template inspection, and full harness validation.

### `SPEC-005` Protect behavior with focused validation

Statement:

1. The validator must add narrow scenario fixtures for the default execution fallback order, explicit operator execution-start override, route-specific reviewer obligations, independent method and Codex-task-continuity selection, the grouped next-stage representation and chat projection, current-versus-next-stage status, same-Codex-task/new-Codex-task loading behavior, execution terminology in canonical fields, and combined small/medium output shape.
2. Plain-language protection must check the expected routine labels and absence of superseded required jargon on current generated templates without scanning frozen history or implementing a general prose-quality engine.
3. Existing graph, ownership, assembly, release, and compatibility checks must continue to pass.

#### `VER-005` Regressions fail focused checks

Covers: `SPEC-005`.

Criterion: Each old ambiguous route has a synthetic failing fixture, each approved route has a passing fixture, and the complete validator remains green after implementation.

Expected evidence: Observed focused-test failure before each fix, focused passing output afterward, assembly check output, full policy-suite output, and diff inspection.

## Architecture decisions

Architecture snapshot status:

1. `Required`: this work changes agentic execution routing, review boundaries, artifact-to-chat projection, and planning-stage transitions. Decisions are recorded in `snapshots/architecture.snapshot.md`.

Decision summary:

1. Drivers: restore reviewer use, activate the correct installed Superpowers workflow, eliminate ambiguous continuity prose, separate current facts from future recommendations, restore combined planning, and reduce operator-facing jargon.
2. Constraints: retain existing modules and lifecycle, place the mini-glossary inside the existing `module:models` owner, do not modify Superpowers, keep source-block assembly, preserve operator approval and final integration ownership, and avoid a new semantic validation engine.
3. Selected approach: add a small ordered execution cascade, a grouped next-stage decision card projected into chat, and a small/medium package completeness guard.
4. Affected boundaries: canonical model/lifecycle/freeze/execution policy, router outcomes, plan/spec source blocks and generated templates, validator scenarios, README, operator note, and repository bootstrap guidance where needed.
5. Rejected alternatives: keep all execution methods optional; make Superpowers a separate lifecycle; add a workflow engine; create a new policy module; or use a broad jargon linter.
6. Validation cues: `VER-001` through `VER-005` and their plan checks.

## Interfaces, data, and control flow

### Interfaces affected

1. Current harness policy and template interfaces for execution method, next-stage presentation, reviewer selection, and planning-package shape.
2. Operator-facing chat output at draft review, approval freeze, and implementation handoff boundaries.
3. Focused validator fixture interfaces in `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
4. No public runtime API, CLI flag, or external plugin interface changes.

### Data, config, and persistence

1. No runtime data, persistence, migration, infrastructure, or application configuration changes.
2. The root repository continues to select `economy-default`; no model-policy configuration changes.

### State and control flow

1. Planning still proceeds through draft review, explicit approval, approval commit, and a fresh post-freeze start instruction.
2. Before freeze, the plan recommends the next stage using the fixed execution cascade.
3. At draft review and freeze, chat shows the same grouped next-stage values.
4. After authorization, the selected execution Codex task starts the planned method or a fresh operator-selected override; it does not generically reopen method selection, derive continuity from the method name, or demand an amendment solely because the operator changed execution method or model at start.
5. Small/medium draft review checks package completeness before accepting the spec and plan as ready.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, personal-data, compliance, or destructive-operation changes are introduced.
2. The mandatory native reviewer prevents silent quality-control degradation when Superpowers is unavailable.
3. If mandatory review cannot run, the safe behavior is to stop and report the unavailable capability.
4. Rollback is a focused revert of the implementation commits; existing stable module and rule IDs remain available.

## Risks and rejected alternatives

### `RISK-001` Superpowers availability is mistaken for sub-agent availability

Decision or mitigation:

1. Record the two facts separately. Installed Superpowers with no usable sub-agents selects `executing-plans`; native execution is reserved for unavailable Superpowers and separately requires a reviewer sub-agent.

### `RISK-002` Native execution becomes impossible in a reduced-tool environment

Decision or mitigation:

1. This is intentional when both Superpowers and reviewer sub-agents are unavailable. The harness must report the blocker rather than weaken a mandatory review silently.

### `RISK-003` Simplified labels hide required model-policy controls

Decision or mitigation:

1. Keep reusable authorization, fallback, model-tier, and final-integration rules in `module:models`; make routine artifacts show only the actionable values. Conditional details remain when an override or availability issue exists.

### `RISK-004` Combined-planning enforcement breaks large/phased anchors

Decision or mitigation:

1. Apply the package completeness guard only after lifecycle classification identifies small/medium work. Preserve the large/phased anchor route and test it explicitly.

### `RISK-005` Validation grows into a brittle prose parser

Decision or mitigation:

1. Use small branch fixtures, required label assertions, forbidden obsolete-field assertions on current template outputs, and existing assembly checks. Do not parse arbitrary artifact prose or frozen history.

### `RISK-006` Listing every Superpowers workflow creates maintenance drift

Decision or mitigation:

1. Name only the two execution skills needed for the ordered execution decision. Other Superpowers methodology remains external and is not enumerated.

### `RISK-007` A separate terminology module increases routing and duplication

Decision or mitigation:

1. Put the small execution glossary in `module:models`, which already owns execution continuity, sub-agent strategy, and context strategy. Templates and operator summaries use the canonical labels and link back rather than restating a second policy block. Reconsider a supplemental glossary or new module only if future terms gain independent behavior or exceed the existing module's scope.

### `RISK-008` A planned method is treated as immutable after freeze

Decision or mitigation:

1. Treat the plan value as the default and accept a fresh explicit operator execution-start override without an amendment when scope and material safety boundaries remain unchanged. Record the actual method and model selection; report only concrete availability or compatibility blockers.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: harness-execution-flow-clarity -- approve execution and planning defaults` |
| Implementation 1 | `feat: harness-execution-flow-clarity -- restore execution and review defaults` |
| Implementation 2 | `feat: harness-execution-flow-clarity -- simplify next-stage presentation` |
| Implementation 3 | `feat: harness-execution-flow-clarity -- enforce combined planning` |

The three implementation commits are intentional stable boundaries: execution and review routing, next-stage representation, and planning-package completeness can each be reviewed, validated, and reverted independently.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-27_harness-execution-flow-clarity/changelog/*.md` | Create `planning-approval.md` at approval and `implementation.md` before implementation commits; synchronize title snippets with planned subjects |
| Root changelog consolidation | Living | As needed | Later operator-owned checkpoint | `CHANGELOG.md` | Do not update during ordinary work-item commits |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Defines routing, review, presentation, and package-shape scenarios |
| Testing guide delta | Living delta | Yes | During implementation | `deltas/testing-guide.delta.md` | Summarize new focused validator scenarios and commands |
| Operator manual delta | Living delta | Yes | During implementation | `deltas/operator-manual.delta.md` | Summarize execution cascade, grouped next-stage chat output, and combined-planning behavior |
| API reference delta | Living delta | No | Not applicable | None | No public API changes |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Freezes the execution cascade, presentation boundary, and combined-planning guard |
| Architecture summary delta | Living delta | No | Not applicable | None | Work-item process architecture is fully captured in the snapshot and current operator docs |

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Transition owner: `plan_harness-execution-flow-clarity.md` owns the implementation handoff after this combined package freezes.
3. Next activity: implement Plan Task `TASK-001` from the approved plan using its recorded method and Codex-task continuity choice.
4. Staged spec-only exception: not requested and not applicable.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments contain the implementation obligations and local Verification Criteria.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, safety, and rollback impacts are checked.
- [x] Risks and rejected alternatives are explicit.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects are stable and suitable for matching changelog fragments.
- [x] The companion plan owns the combined package's implementation handoff.
- [x] The next-stage execution and reviewer strategy is defined in the companion plan.
- [x] No unresolved placeholders, required decisions, missing sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
