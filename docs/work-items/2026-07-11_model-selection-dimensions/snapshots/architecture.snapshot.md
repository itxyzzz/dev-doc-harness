# Model Selection Dimensions Architecture Snapshot

Work ID: `2026-07-11_model-selection-dimensions`
Short ID: `model-selection-dimensions`
Status: Approved
Harness release: `0.5+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

Preserve the work-item decisions that separate model taxonomy, orchestration choice, authorization, and runtime capability so implementation and later review do not collapse them back into a single model-profile label.

## Decision Ledger

### `DEC-001` Use explicit vendor-neutral selection dimensions

Selected approach:

1. Model strategy independently records generation, capability tier, reasoning effort, orchestration mode, optional resolved profile, and availability/fallback.
2. Permanent capability tiers are `flagship`, `balanced`, and `fast/economy`; concrete provider names are current mappings rather than canonical tier names.
3. This resolves the GPT-5.6 ambiguity while avoiding a provider catalog that the harness would need to keep current.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:models`, role examples, README model-policy guidance, template source blocks, assembled planning templates, and harness policy validation.
3. Interfaces, schemas, config, or infra: required Model and Sub-agent Strategy notation; no runtime config or infrastructure changes.
4. Agentic, process, documentation, or phase boundaries: planning selection, freeze confirmation, runtime preflight, fallback, and de-facto completion reporting.

Source spec sections:

1. `REQ-001`, `REQ-002`, `AC-001` through `AC-003`, and `Architecture Decisions` in `spec_model-selection-dimensions.md`.

Validation cues:

1. Canonical policy and template source review shows six independent dimensions.
2. Validator checks distinguish generation from capability tier.
3. GPT-5.6 Sol/Terra/Luna are labeled as a current provider mapping.

Rejected alternatives:

1. Minimal extension of `Model class/profile`: rejected because it preserves ambiguity.
2. Provider capability registry: rejected because live pricing, entitlement, availability, and freshness are outside harness scope.

### `DEC-002` Treat ultra as platform-managed orchestration

Selected approach:

1. `Ultra` maps to `platform multi-agent`, not to capability tier or reasoning effort.
2. Plans may choose single-agent execution, harness-managed bounded sub-agents, platform-managed multi-agent execution, or an explicitly justified hybrid when supported.
3. `Enterprise-default` proactively assesses platform multi-agent execution for complex decomposable work; `economy-default` uses explicit escalation triggers.
4. Platform-managed synthesis does not imply harness-managed context shaping, task ownership, model overrides, reports, or review gates.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:models`, freeze-gate prompts, template strategy notation, role examples, and completion reporting.
3. Interfaces, schemas, config, or infra: orchestration-mode field and associated selection rationale; no platform implementation changes.
4. Agentic, process, documentation, or phase boundaries: delegation planning, runtime choice, validation responsibility, and final integration reporting.

Source spec sections:

1. `REQ-003`, `REQ-004`, `AC-004` through `AC-007`, and `RISK-002`.

Validation cues:

1. Focused validator checks classify `ultra` under orchestration and exclude it from reasoning-effort and tier vocabularies.
2. Enterprise and economy policy prose contains distinct assessment and escalation behavior.
3. Completion guidance records the de-facto orchestration mode.

Rejected alternatives:

1. Treating `ultra` as `max` reasoning: rejected because multi-agent coordination changes execution shape.
2. Treating `ultra` as equivalent to ordinary bounded delegation: rejected because platform-managed internal behavior may not expose harness controls.

### `DEC-003` Separate recommendation, authorization, permission, and availability

Selected approach:

1. A planning agent may recommend an orchestration mode under the active model policy.
2. A frozen approved strategy becomes harness-authorized after the normal fresh instruction to begin implementation.
3. The freeze-gate prompt explicitly asks the operator to confirm capability tier, reasoning effort, orchestration mode, sub-agent policy, and fallback so restrictive runtimes can receive explicit user authorization.
4. Runtime permission and platform availability are checked at execution time; unavailable or prohibited choices use the approved fallback or stop for confirmation.
5. Unplanned escalation into broader or more expensive execution remains confirmation-gated.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:models`, `module:freeze-gate`, planning templates, execution preflight guidance, and completion reporting.
3. Interfaces, schemas, config, or infra: operator confirmation wording and strategy fallback field; no platform permission changes.
4. Agentic, process, documentation, or phase boundaries: plan approval, post-freeze authorization, runtime preflight, variance handling, and completion reporting.

Source spec sections:

1. `REQ-005`, `AC-008` through `AC-010`, `RISK-003`, and `State and control flow`.

Validation cues:

1. Canonical policy names all four layers.
2. Freeze-gate guidance requests explicit orchestration and fallback confirmation.
3. Fresh-confirmation language covers unplanned `ultra`, tier/effort escalation, write expansion, and concurrency expansion.

Rejected alternatives:

1. Treating plan approval as sufficient runtime permission in all environments: rejected because higher-priority runtime restrictions may still apply.
2. Requiring fresh confirmation for every previously approved use: rejected because it duplicates the normal freeze/start lifecycle and weakens durable plan authority.

### `DEC-004` Prefer curated-artifact fresh tasks for main-model transitions

Selected approach:

1. Model strategy records execution continuity, context visibility, and whether artifact rehydration is required.
2. A new task with curated-artifact handoff is preferred when changing the main model generation, capability tier, concrete profile, or platform-managed orchestration profile.
3. Same-task continuation remains normal when preserving the current model; a same-task switch must re-read the frozen package before edits regardless of compaction.
4. Runtime-managed compaction remains a platform responsibility, and agents do not claim precise remaining context unless the platform exposes it.
5. Applicable frozen specs and plans include a minimal copy-ready handoff that references canonical startup guidance in `module:execution-quality`.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:models`, `module:execution-quality`, freeze-gate guidance, current spec/plan template sources, assembled templates, README guidance, and validation.
3. Interfaces, schemas, config, or infra: execution-continuity notation, context-visibility notation, rehydration flag, and copy-ready next-task handoff; no runtime configuration change.
4. Agentic, process, documentation, or phase boundaries: model transition, post-spec phase-planning handoff, post-plan implementation handoff, same-task continuation, and task preflight.

Source spec sections:

1. `REQ-008`, `AC-016` through `AC-020`, and `RISK-007` through `RISK-009`.

Validation cues:

1. Canonical model policy gives new-task preference for main-model changes.
2. `rule:execution-quality.execution-thread-start` defines artifact-grounded startup without rediscovery.
3. Current template sources and generated outputs contain minimal handoff prompts with exact artifact references and no duplicated requirements.
4. Validator checks prohibit unsupported exact-context claims and require artifact rehydration for same-task switching.

Rejected alternatives:

1. Choosing compaction from an agent-estimated token threshold: rejected because exact active context and runtime thresholds are generally not exposed.
2. Treating compaction as equivalent to a fresh task: rejected because compacted context can preserve prior framing and does not remove model-switch cache effects.
3. Embedding a full requirements summary in each handoff: rejected because it wastes tokens and can drift from frozen artifacts.

## Decision Drivers

1. GPT-5.6 introduces durable capability tiers that can advance independently of generation.
2. Reasoning effort remains independently selectable and now includes `max` for supported profiles.
3. `Ultra` introduces platform-managed multi-agent execution and is promising enough that planners should assess it proactively under `enterprise-default`.
4. Existing Codex runtime policies can restrict manual sub-agent spawning unless explicitly requested, so planning freedom must coexist with runtime permission checks.
5. The harness must remain portable and provider-neutral.

## Constraints

1. `references/subagent-model-policy.md` remains the canonical owner.
2. Template sources, manifests, and generated outputs remain synchronized through the assembler.
3. `AGENTS.md` continues selecting `economy-default` for this repository.
4. Frozen historical work-item artifacts are not migration targets.
5. Platform-managed multi-agent details may be unavailable or not exposed.
6. Any unrelated pre-existing operator changes must remain untouched.
7. Fresh-task handoffs must remain minimal and point to authoritative artifacts instead of copying them.
8. Runtime-managed context compaction cannot be replaced by a reliable agent estimate when context telemetry is unavailable.

## Future Durable-Doc Boundary

No repository-level architecture document is required. Provider-specific mapping maintenance beyond the current example, live model discovery, and runtime feature negotiation are future work only if the harness later adopts a provider-adapter architecture.

## Approval

- Status: Approved
- Superseded by: None
