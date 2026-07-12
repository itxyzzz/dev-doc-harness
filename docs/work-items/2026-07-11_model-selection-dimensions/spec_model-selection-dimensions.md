# Model Selection Dimensions Spec

Work ID: `2026-07-11_model-selection-dimensions`
Short ID: `model-selection-dimensions`
Status: Approved
Harness release: `0.5+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:evidence`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.work-item-architecture-decisions`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`, `rule:evidence.preservation`

## Goal

Update the harness model-selection contract so planning agents can choose and explain model generation, capability tier, reasoning effort, orchestration mode, and execution continuity independently, including deliberate use of GPT-5.6 `ultra` and efficient document-grounded handoff to a fresh task when the main model changes.

## Source and Intent

Source input:

1. The operator asked how the existing `enterprise-default` and `economy-default` policies fare after GPT-5.6 introduced the Sol, Terra, and Luna capability tiers in addition to version and reasoning effort.
2. The operator approved an explicit multi-axis policy design, requested that `ultra` be included, and asked that planning agents have freedom to recommend it when plausible, especially under `enterprise-default`.
3. The operator identified restrictive Codex sub-agent authorization as an important compatibility limitation and required the design to avoid treating `ultra` as a complete substitute for harness-managed sub-agents.
4. The operator asked whether mid-conversation model changes make same-task continuation risky, whether agents can reliably judge compaction need, and required minimal copy-ready handoff messages plus canonical fresh-task startup guidance.

Desired operator/user outcome:

1. Plans express model and orchestration choices without conflating generation, tier, reasoning, delegation, or concrete runtime profile.
2. `enterprise-default` actively considers `ultra` and bounded sub-agents when they plausibly improve correctness, coverage, or throughput.
3. Approved orchestration strategies remain usable under restrictive runtimes through explicit freeze-gate confirmation, recorded fallbacks, and clear separation between recommendation, harness authorization, runtime permission, and platform capability.
4. When a different main model or orchestration profile should take over, the plan recommends a fresh task with a minimal artifact-grounded handoff instead of relying on invisible context-window estimates or chat rediscovery.

Success summary:

1. `module:models` remains the canonical owner and defines a vendor-neutral multi-axis selection schema with a current GPT-5.6 mapping example.
2. Current templates, examples, freeze-gate prompts, operator guidance, and validators consistently consume that schema.
3. Frozen packages contain a copy-ready next-task handoff, and `module:execution-quality` defines a fast startup protocol that treats those artifacts as authoritative.

## Scope Boundary

### In scope

1. Define independent selection dimensions for model generation, capability tier, reasoning effort, orchestration mode, resolved runtime profile, and availability/fallback.
2. Define the durable capability tiers `flagship`, `balanced`, and `fast/economy` and show GPT-5.6 Sol, Terra, and Luna only as a current provider mapping.
3. Classify `ultra` as a platform-managed multi-agent orchestration mode rather than a reasoning-effort value or capability tier.
4. Update `enterprise-default` and `economy-default` selection and escalation behavior across the new dimensions.
5. Separate policy recommendation, harness authorization, runtime permission, and platform availability.
6. Update current model-strategy template sources, regenerate their assembled templates, and align examples, freeze-gate guidance, README guidance, and validator coverage.
7. Preserve the model-release evidence used to justify the taxonomy and distinguish verified provider facts from harness design decisions.
8. Define execution-continuity choices, prefer a new task when changing the main model/profile, and require copy-ready handoffs that identify the frozen package, approved strategy, entry action, and stop condition.
9. Add canonical fresh-task startup guidance that loads instructions and planning artifacts in order without repeating discovery or reopening frozen decisions.

### Non-scope

1. Implement or emulate OpenAI `ultra` or any Codex sub-agent runtime.
2. Create a live provider registry, price catalog, entitlement matrix, availability service, or automatic model resolver.
3. Promise that `ultra` exposes task partitioning, per-agent context strategies, per-agent model choice, file ownership, independent reports, or reviewer gates.
4. Change the repository's active `economy-default` selection in `AGENTS.md`.
5. Rewrite frozen historical work-item artifacts to use the new notation.
6. Change concurrency caps or general lifecycle sizing except where wording must distinguish platform-managed multi-agent execution from harness-managed bounded sub-agents.
7. Estimate exact remaining context, prescribe compaction from an invisible token threshold, or replace runtime-managed automatic compaction.
8. Duplicate planning-package content inside generated handoff messages.

### Assumptions

1. Policy-relative dimensions are more stable than concrete provider model names.
2. A concrete runtime can expose only a subset of the planned dimensions; the strategy must record `not exposed` or use its fallback rather than invent runtime facts.
3. The freeze-gate confirmation can provide explicit operator authorization for a planned orchestration mode when the runtime requires user-requested delegation.
4. A platform-managed multi-agent mode may synthesize internally, but the harness-level orchestration thread remains responsible for validation and user-facing completion reporting.
5. Agents usually cannot see exact active-context usage, hidden prompt overhead, or the runtime's compaction threshold; context visibility must be recorded as exposed or not exposed rather than inferred as a precise value.
6. A fresh task with curated planning artifacts is a cleaner model-transition boundary than a same-task model switch, even when optional or automatic compaction is available.

### Open questions

1. None identified after repository-context review and operator design approval.

## Repository Context

### Current state

1. `references/subagent-model-policy.md` owns `module:models` and already separates policy-relative model class/profile from reasoning effort.
2. The current vocabulary uses `latest strongest`, `standard`, and `smaller/faster`; those labels cannot uniquely identify generation, durable capability tier, reasoning effort, or orchestration mode after GPT-5.6.
3. The current policy treats approved frozen sub-agent strategies as authorized after the normal post-freeze start instruction, while fresh confirmation is required for unplanned escalation.
4. Model-strategy notation is authored in template source blocks and propagated into generated small/medium and large/phased templates.
5. `references/planning-freeze-gates.md` currently asks the operator to confirm model, reasoning-effort, and sub-agent policy choices but does not name capability tier, orchestration mode, or fallback.
6. The active repository model policy remains `economy-default` through `AGENTS.md`.
7. Current runtime instructions can prohibit spawning sub-agents unless the user or applicable repository/skill instructions explicitly request delegation; harness policy cannot assume that recommendation alone grants runtime permission.
8. `module:execution-quality` already owns context load order and task preflight, but it does not yet define a planning-package-optimized fresh-task startup protocol.
9. Codex manages automatic compaction internally after a context threshold; the agent interface does not reliably expose exact remaining context or the effective threshold.

### Evidence read

1. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
2. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`.
3. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.040.common.model-strategy.md`.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md`.
6. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and the current generated template consumers found by repository search.
7. `docs/work-items/2026-07-11_model-selection-dimensions/evidence/gpt-5-6-model-taxonomy.md`.
8. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`.
9. Official OpenAI guidance on model transitions and the Codex agent loop, summarized in the evidence snapshot.

### Constraints and compatibility

1. `subagent-model-policy.md` remains the canonical owner; templates and operator docs consume rather than redefine reusable policy.
2. Template source blocks, manifests, and generated outputs must remain consistent through the repository assembler workflow.
3. The new schema must work when exact model identity, reasoning effort, runtime permission, or platform features are unavailable or not exposed.
4. The harness must not imply that its approval rules override higher-priority platform or runtime restrictions.
5. Superpowers compatibility uses the canonical harness work-item package; `docs/superpowers` contains only a pointer stub.
6. Any unrelated pre-existing operator work must not be altered, unstaged, or included in this work item's commits.
7. Fresh-task handoffs must be short enough to paste without recreating the planning documents and precise enough to avoid repository rediscovery.

## Requirements

### `REQ-001` Define a multi-axis selection contract

Rationale:

1. A single model-class/profile field no longer identifies the independent choices a planning agent must make.

Acceptance links:

1. Covered by `AC-001` and `AC-002`.

Notes:

1. The contract must independently record generation, capability tier, reasoning effort, orchestration mode, optional resolved profile, and availability/fallback.

### `REQ-002` Keep durable tiers vendor-neutral

Rationale:

1. The policy should survive later generations and providers without rewriting permanent semantics for every model release.

Acceptance links:

1. Covered by `AC-002` and `AC-003`.

Notes:

1. Permanent tiers are `flagship`, `balanced`, and `fast/economy`.
2. Sol, Terra, and Luna are a dated/current mapping example, not the policy vocabulary itself.

### `REQ-003` Model platform-managed multi-agent execution explicitly

Rationale:

1. `Ultra` changes orchestration behavior and cannot safely be represented as stronger reasoning or ordinary sub-agent delegation.

Acceptance links:

1. Covered by `AC-004` and `AC-005`.

Notes:

1. The policy must distinguish `single-agent`, `bounded delegated sub-agents`, `platform multi-agent`, and an explicitly justified hybrid when the runtime supports it.

### `REQ-004` Adapt both repository policies

Rationale:

1. The new dimensions have value only if `enterprise-default` and `economy-default` give planners actionable selection guidance.

Acceptance links:

1. Covered by `AC-006` and `AC-007`.

Notes:

1. `enterprise-default` proactively assesses platform multi-agent/`ultra` for complex decomposable work.
2. `economy-default` normally begins with fast/economy or balanced tiers and escalates when risk, uncertainty, failure, or overall cost/latency justifies it.

### `REQ-005` Preserve authorization and runtime boundaries

Rationale:

1. Planning freedom must not be confused with permission to spawn agents or invoke a broader platform mode.

Acceptance links:

1. Covered by `AC-008`, `AC-009`, and `AC-010`.

Notes:

1. The policy must distinguish recommendation, harness authorization, runtime permission, and platform availability.
2. An approved frozen strategy becomes harness-authorized after the normal fresh start instruction, but restrictive runtimes may require explicit operator confirmation or may still prevent execution.
3. Unplanned escalation to platform multi-agent/`ultra`, a higher tier, higher reasoning, broader write authority, or more concurrency requires fresh confirmation.

### `REQ-006` Update all current consumers without migrating history

Rationale:

1. Canonical policy, planning notation, examples, operator prompts, and validation must agree for future work items.

Acceptance links:

1. Covered by `AC-011` and `AC-012`.

Notes:

1. Current source blocks and assembled templates change together.
2. Frozen historical work items remain unchanged.

### `REQ-007` Validate semantics and generation parity

Rationale:

1. Future drift could again conflate reasoning with orchestration or allow generated templates to diverge from their source blocks.

Acceptance links:

1. Covered by `AC-013`, `AC-014`, and `AC-015`.

Notes:

1. Validator checks must cover the new required dimensions, `ultra` classification, authorization language, and source/generated template parity.

### `REQ-008` Make model-transition handoff explicit and efficient

Rationale:

1. Changing the main model inside a long conversation can disrupt workflow behavior and prompt caching, while agents generally cannot measure remaining context precisely enough to prescribe compaction reliably.

Acceptance links:

1. Covered by `AC-016`, `AC-017`, `AC-018`, `AC-019`, and `AC-020`.

Notes:

1. Required strategy notation records execution continuity, context visibility, and whether artifact rehydration is required.
2. A new task with curated-artifact handoff is preferred when changing the main model generation, capability tier, concrete profile, or platform-managed orchestration profile.
3. Same-task continuation remains supported, but a same-task model switch requires artifact rehydration whether or not compaction occurred.
4. Plans and applicable large-spec handoffs contain a minimal copy-ready message naming exact frozen artifacts, the canonical startup rule, approved execution strategy, first activity, and variance stop condition.
5. `module:execution-quality` owns the fresh-task startup protocol; `module:models` owns when the model strategy recommends using it.

## Acceptance Criteria

### `AC-001` Required planning notation exposes independent dimensions

Verifies:

1. `REQ-001`.

Method:

1. Review the canonical required notation and current template sources; each exposes generation, capability tier, reasoning effort, orchestration mode, resolved profile, and availability/fallback without merging them into one field.

### `AC-002` Generation and capability tier are not conflated

Verifies:

1. `REQ-001` and `REQ-002`.

Method:

1. Validator and review checks find separate generation and capability-tier terms and reject reliance on `Model class/profile` as the sole selection field.

### `AC-003` GPT-5.6 names are mappings rather than permanent tiers

Verifies:

1. `REQ-002`.

Method:

1. Review confirms the permanent tier definitions are vendor-neutral and the GPT-5.6 Sol/Terra/Luna mapping is explicitly current/provider-specific.

### `AC-004` Ultra is classified as orchestration

Verifies:

1. `REQ-003`.

Method:

1. Validator and review checks confirm `ultra` appears under platform-managed multi-agent orchestration and is not listed as a reasoning-effort value or capability tier.

### `AC-005` Ultra limitations remain explicit

Verifies:

1. `REQ-003`.

Method:

1. Canonical policy states that platform multi-agent mode does not automatically provide harness-managed task partitioning, context strategies, per-agent model selection, file ownership, independent reports, or reviewer gates.

### `AC-006` Enterprise policy proactively assesses ultra

Verifies:

1. `REQ-004`.

Method:

1. `enterprise-default` requires planners to assess platform multi-agent/`ultra` when complex decomposable work may benefit from parallelism, coverage, or throughput, while retaining a written selection reason.

### `AC-007` Economy policy has bounded escalation rules

Verifies:

1. `REQ-004`.

Method:

1. `economy-default` defines lower-cost starting tiers and explicit escalation triggers for flagship, `max`, or platform multi-agent execution.

### `AC-008` Authorization layers are explicit

Verifies:

1. `REQ-005`.

Method:

1. Canonical policy separately describes recommendation, harness authorization, runtime permission, and platform availability.

### `AC-009` Freeze confirmation names orchestration and fallback

Verifies:

1. `REQ-005`.

Method:

1. The freeze gate asks the operator to confirm capability tier, reasoning effort, orchestration mode, sub-agent policy, and fallback before implementation begins.

### `AC-010` Unplanned escalation still stops for confirmation

Verifies:

1. `REQ-005`.

Method:

1. Review and validator checks confirm unplanned `ultra`, tier escalation, reasoning escalation, write expansion, and concurrency expansion require fresh confirmation.

### `AC-011` Current template consumers use the new schema

Verifies:

1. `REQ-006`.

Method:

1. Template assembly succeeds and generated small/medium plan, large spec, and large phase-plan surfaces contain the source-block schema.

### `AC-012` Historical planning artifacts remain untouched

Verifies:

1. `REQ-006`.

Method:

1. Final diff review shows no changes under pre-existing frozen `docs/work-items/*` packages other than this new work item.

### `AC-013` Focused policy checks pass

Verifies:

1. `REQ-007`.

Method:

1. Focused tests in `test_harness_policy.py` pass for multi-axis notation, authorization layers, and `ultra` classification.

### `AC-014` Template generation checks pass

Verifies:

1. `REQ-007`.

Method:

1. The repository template assembler/check command exits successfully with generated templates matching source blocks and manifests.

### `AC-015` Full harness validation passes

Verifies:

1. `REQ-007`.

Method:

1. `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` exits `0` and reports the harness policy checks passed.

### `AC-016` Model transitions prefer a fresh task

Verifies:

1. `REQ-008`.

Method:

1. Canonical model policy recommends `new task with curated-artifact handoff` when the main model generation, capability tier, concrete profile, or platform-managed orchestration profile changes, unless an explicit continuity reason justifies same-task switching.

### `AC-017` Context visibility is not overstated

Verifies:

1. `REQ-008`.

Method:

1. Strategy notation records context visibility as `exposed` or `not exposed`, and canonical guidance prohibits precise remaining-context or compaction-necessity claims when the platform does not expose them.

### `AC-018` Fresh-task startup has a canonical owner

Verifies:

1. `REQ-008`.

Method:

1. `module:execution-quality` defines a stable fresh-task startup rule that loads applicable instructions and frozen artifacts, verifies state, avoids rediscovery, restates only immediate execution context, and uses variance handling for conflicts.

### `AC-019` Frozen packages provide minimal handoff messages

Verifies:

1. `REQ-008`.

Method:

1. Current applicable spec and plan template sources require a copy-ready handoff naming exact artifacts, `rule:execution-quality.execution-thread-start`, the approved strategy and fallback, the first activity, and the approval-required variance stop condition without duplicating planning content.

### `AC-020` Same-task switching requires rehydration

Verifies:

1. `REQ-008`.

Method:

1. Canonical guidance requires a model that takes over in the same task to re-read the frozen package and reconcile scope before edits, regardless of whether operator-requested or runtime-managed compaction occurred.

## Architecture Decisions

Architecture snapshot status:

1. `Required`: this work changes canonical policy shape, authorization flow, generated planning interfaces, and agentic orchestration semantics. Decisions are recorded in `snapshots/architecture.snapshot.md`.

Decision summary:

1. Drivers: preserve durable model-policy semantics across GPT-5.6 and later generations; give planners freedom to recommend `ultra`; retain safe authorization under restrictive runtimes.
2. Constraints: canonical policy ownership, generated-template workflow, active `economy-default`, immutable historical artifacts, runtime instructions that may restrict spawning.
3. Selected approach: explicit vendor-neutral selection dimensions with a current provider mapping and separate orchestration/authorization layers.
4. Affected boundaries: `module:models`, `module:execution-quality`, freeze-gate confirmation, template-source interfaces, assembled templates, role examples, README guidance, policy validation, fresh-task handoff, and completion reporting.
5. Rejected alternatives: minimally extending `Model class/profile` because ambiguity remains; a provider capability registry because it creates freshness and maintenance obligations outside harness scope.
6. Validation cues: `AC-001` through `AC-015`, template-generation checks, full harness validator, and final diff review.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Required Model and Sub-agent Strategy notation changes from a single model-class/profile field to independent selection fields.
2. The freeze-gate operator prompt adds explicit orchestration-mode and fallback confirmation.
3. Completion reporting adds de-facto orchestration mode and runtime-permission/fallback outcomes when relevant.
4. Applicable frozen spec and plan artifacts add a copy-ready next-task handoff interface.
5. No public software API changes.

### Data, config, and persistence

1. No runtime data model, persistence, or migration changes.
2. No repository configuration change; `AGENTS.md` continues selecting `economy-default`.

### State and control flow

1. Planning flow: assess work -> select generation/tier/effort/orchestration -> resolve profile if exposed -> record fallback and authorization needs.
2. Freeze flow: approve artifact -> confirm execution dimensions and sub-agent policy -> fresh instruction authorizes start at the harness layer.
3. Execution flow: check runtime permission and availability -> use approved mode or approved fallback -> validate and report de-facto behavior.
4. Variance flow: unplanned escalation or unavailable fallback follows fresh confirmation or the existing amendment/variance rules according to impact.
5. Continuity flow: preserve the current model for same-task continuation; prefer a fresh task with curated artifacts for a model/profile transition; if switching inside the same task, rehydrate from the frozen package before editing.
6. Compaction flow: the runtime owns mandatory automatic compaction, the operator may request compaction, and the agent records context visibility without claiming an unexposed threshold.

### Safety, security, privacy, migration, and rollback

1. The change is documentation/process policy and does not itself execute agents or expose data.
2. Explicit runtime-permission checks prevent the harness from claiming authority over higher-priority platform restrictions.
3. Explicit fallbacks prevent silent escalation into more expensive or broader execution.
4. Rollback is a normal revert of the implementation commit; no data migration is required.

## Risks and Rejected Alternatives

### `RISK-001` Concrete provider mapping becomes stale

Decision or mitigation:

1. Keep permanent semantics vendor-neutral and label GPT-5.6 as a current mapping supported by preserved evidence.

### `RISK-002` Ultra is treated as a universal replacement for controlled sub-agents

Decision or mitigation:

1. Require plans to state why platform-managed synthesis fits and what still needs harness-level validation or separately controlled agents.

### `RISK-003` Approved policy is mistaken for runtime permission

Decision or mitigation:

1. Separate the four authorization/capability layers and require freeze-gate confirmation plus runtime preflight.

### `RISK-004` The richer schema creates planning noise for simple work

Decision or mitigation:

1. Permit compact statements and `not exposed` values while retaining the independent dimensions; do not require a provider-specific catalog.

### `RISK-005` Generated templates drift from source blocks

Decision or mitigation:

1. Modify source blocks, regenerate assembled templates, and add validator coverage for parity and required terms.

### `RISK-006` Unrelated staged work is accidentally committed

Decision or mitigation:

1. Preserve any unrelated pre-existing operator work and use path-specific staging/commit checks for this work item; stop if a clean planning-only commit cannot be proven.

### `RISK-007` A model switch inherits stale conversational framing

Decision or mitigation:

1. Prefer a fresh task with curated-artifact handoff; require artifact rehydration before edits when same-task switching is explicitly chosen.

### `RISK-008` The agent guesses context pressure or compaction need

Decision or mitigation:

1. Record context visibility, leave mandatory compaction to the runtime, and make operator-requested compaction optional rather than threshold-driven when exact usage is unavailable.

### `RISK-009` Handoff messages duplicate or drift from frozen documents

Decision or mitigation:

1. Keep the message minimal, name exact authoritative paths and the startup rule, and prohibit requirements summaries that create a second source of truth.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spec: model-selection-dimensions -- define tier, orchestration, and handoff axes` | `2026-07-11_model-selection-dimensions -- define tier, orchestration, and handoff axes` | Approval commit for the spec, architecture snapshot, evidence snapshot, Superpowers pointer stub, later implementation plan, and matching changelog source fragment entry. |
| Implementation | `docs: model-selection-dimensions -- separate model tier and optimize execution handoff` | `2026-07-11_model-selection-dimensions -- separate model tier and optimize execution handoff` | Canonical policy, execution startup guidance, freeze gate, template sources and generated outputs, examples, README, validator, and implementation changelog source fragment entry. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `changelog/planning-approval.md`, then `changelog/implementation.md` | Fragment entries use newest-first headings, required release metadata, and snippets synchronized to planned subjects |
| Root changelog consolidation | Living | No | Operator-owned consolidation checkpoint | `CHANGELOG.md` | This independent work item does not consolidate the root publication view |
| Test cases | Snapshot | No | Before implementation | `snapshots/test-cases.snapshot.md` | Policy acceptance criteria and validator tasks provide sufficient test intent; no separate behavioral fixture is needed |
| Model-release evidence | Snapshot | Yes | Before spec approval | `evidence/gpt-5-6-model-taxonomy.md` | Preserves the external taxonomy claims used by the design |
| Testing guide delta | Living delta | No | During or after implementation | `deltas/testing-guide.delta.md` | Existing harness validator workflow remains unchanged |
| Operator manual delta | Living delta | No | After implementation | `deltas/operator-manual.delta.md` | README and canonical policy are the current operator surfaces |
| API reference delta | Living delta | No | During or after API work | `deltas/api-reference.delta.md` | No public software API changes |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Captures selection-schema and authorization-boundary decisions |
| Architecture summary delta | Living delta | No | After review | `deltas/architecture-summary.delta.md` | No repository-level architecture document changes are needed |
| Superpowers design pointer | Pointer stub | Yes | Before spec review | `docs/superpowers/specs/2026-07-11-model-selection-dimensions-design.md` | Points to this canonical harness spec and snapshot without duplicating content |
| Fresh-task startup guidance | Canonical policy | Yes | During implementation | `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md` | Defines efficient artifact-grounded startup without rediscovery |

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Requirements are specific, relevant, bounded, and linked to acceptance criteria.
- [x] Acceptance criteria are observable, testable, and tied to requirements or scope items.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: None
