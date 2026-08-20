# Orchestration and Model Policy Architecture Snapshot

Work ID: `2026-08-02_task-orchestration-model-policy`
Short ID: `task-orchestration-model-policy`
Status: Approved
Harness release: `0.8+`
Schema: `schema:snapshot.architecture`
Policy references: `module:lifecycle`, `module:quality`, `module:artifact-style`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:quality.spec-handoff`

## Purpose

Preserve the ownership, terminology, stage-applicability, and compatibility decisions that the policy rewrite, its current consumers, and future review must follow.

## Decision Ledger

### `DEC-001` Architecture Decision — Separate stage ownership from stage execution shape

Selected approach:

1. `module:lifecycle` owns the documented next lifecycle stage through the new `rule:lifecycle.stage-boundaries`.
2. `module:models` consumes that stage and owns how it runs: method, review arrangement, orchestration-session continuity, orchestration mode, model generation, capability tier, reasoning effort, applicable fallbacks, sub-agent strategy, and final integration.
3. The models module must cite the lifecycle rule rather than copy its transition mapping.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:lifecycle`, `module:models`, `module:freeze-gate`, `module:execution-quality`, `module:architecture`, and their current template/validation consumers.
3. Interfaces, schemas, config, or infra: rule-owner graph and next-stage selection prompt fields; no runtime config or infrastructure.
4. Agentic, process, documentation, or phase boundaries: combined small/medium and large/phased freeze transitions, planning-stage method selection, execution-stage method/review routing, and same/new-session continuity.

Source spec sections:

1. `SPEC-002`, `SPEC-004`, and `Interfaces, Data, and Control Flow`.

Validation cues:

1. `VER-002` proves one lifecycle owner and no copied transition table.
2. `VER-004` proves planning/execution method applicability.
3. Rule-graph and owner-heading checks pass.

Rejected alternatives:

1. Keep lifecycle-stage meaning implicit in `module:models`; rejected because it creates competing ownership and the current placeholder already identifies the missing interface.
2. Move orchestration mechanics into lifecycle; rejected because lifecycle owns planning shape and stage boundaries, not model, delegation, review, or continuity mechanics.

### `DEC-002` Architecture Decision — Use orchestration session as the portable top-level term

Selected approach:

1. **Orchestration session** means the top-level operator-facing conversation or controller context that owns scope, integration, validation, and the user-facing result.
2. **Current orchestration session** produces, reviews, or freezes the current package; **next-stage orchestration session** performs its documented next lifecycle stage. They may be the same session or different sessions.
3. **Plan Task** remains a numbered unit inside an approved implementation plan. **Agent run/sub-agent run** remains a bounded delegated assignment. **External method session** identifies a separate workflow controller such as Superpowers.
4. Current reusable surfaces use `same orchestration session` and `new orchestration session`. Product-specific names such as Codex remain only where the product itself is the subject.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: current canonical references, router/catalog summaries, root operator guidance, advisory role examples, template source blocks, generated templates, and validator fixtures.
3. Interfaces, schemas, config, or infra: continuity field values and current terminology; no runtime schema or config.
4. Agentic, process, documentation, or phase boundaries: planning and execution handoffs, fresh-session rehydration, work sizing, and final integration language.

Source spec sections:

1. `SPEC-001`, `SPEC-003`, and `RISK-002`.

Validation cues:

1. `VER-003` distinguishes all defined concepts and rejects stale current terminology.
2. Template and freeze-gate fixtures accept only the new `Run in` values after implementation.

Rejected alternatives:

1. Bare **session**; rejected because it can refer to a delegated run, external controller, runtime allocation, or top-level interaction.
2. **Agent session**; rejected because it does not clearly distinguish the orchestration owner from a sub-agent session.
3. Defer the migration; rejected because the revised continuity, terminology, and notation sections would otherwise require an immediate second compatibility edit.

### `DEC-003` Architecture Decision — Make method and review conditional on lifecycle-stage kind

Selected approach:

1. `Method` always names the workflow for the documented next lifecycle stage.
2. Planning stages record a planning method and planning-review arrangement; no new enumerated planning-method cascade is introduced.
3. Execution stages retain `rule:lifecycle.superpowers-compatibility` as the execution-method cascade and retain the existing route-specific Plan Task and final-review obligations.
4. The compact selection uses the general field `Review`; its value states the planning-stage review arrangement or the execution-stage Plan Task/final-review arrangement.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:models`, freeze-gate rendering, large-anchor and plan handoffs, readiness prompts, and semantic validator fixtures.
3. Interfaces, schemas, config, or infra: `Orchestration` group field labels and stage-applicability rules.
4. Agentic, process, documentation, or phase boundaries: `plan drafting`, `phase-plan drafting`, `plan execution`, `phase execution`, and resumed amended stages.

Source spec sections:

1. `SPEC-004` and `RISK-003`.

Validation cues:

1. `VER-004` checks both a planning-stage and execution-stage selection.
2. Existing execution-cascade and reviewer-contract assertions continue to pass.

Rejected alternatives:

1. Make `Method` execution-only and omit it for planning transitions; rejected because plan and phase-plan drafting still require a deliberate orchestration choice.
2. Apply Plan Task reviewers to planning stages; rejected because those stages do not yet have approved implementation Plan Tasks.
3. Define a full planning-method cascade now; rejected as unnecessary expansion.

### `DEC-004` Architecture Decision — Select model generation, tier, and effort independently

Selected approach:

1. Actionable next-stage model selection has three dimensions: model generation, capability tier, and reasoning effort.
2. Generation normally uses `latest available` in Codex unless compatibility or provider constraints require a concrete generation.
3. Capability tiers remain `flagship`, `balanced`, and `fast/economy`; current concrete model names remain mappings.
4. Resolved profile, availability, and current-session facts remain runtime observation or fallback data, not additional durable selection dimensions.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: canonical model policy, policy profiles, required notation, template prompts, role examples, freeze-gate presentation, and validator fixtures.
3. Interfaces, schemas, config, or infra: `Model` group fields; no runtime model configuration.
4. Agentic, process, documentation, or phase boundaries: every upcoming planning, execution, amendment/replanning, or consequential review stage.

Source spec sections:

1. `SPEC-005` and `SPEC-006`.

Validation cues:

1. `VER-005` verifies distinct fields and unchanged tier semantics/mappings.
2. Existing enterprise/economy behavior and escalation assertions remain protected.

Rejected alternatives:

1. Treat resolved profile as a durable fourth dimension; rejected because it is a runtime mapping and may be unavailable.
2. Omit generation because Codex normally uses the latest model; rejected because the dimension still matters across providers, compatibility constraints, and future generations.

### `DEC-005` Architecture Decision — Preserve but do not solve pre-spec selection

Selected approach:

1. The canonical policy continues to require deliberate model and reviewer/sub-agent assessment before spec drafting.
2. This work item does not add a durable pre-spec record, stage, gate, or mandatory reviewer.
3. The lack of a durable pre-spec selection surface is stated as a future-work boundary so later lifecycle design can address it deliberately.

Affected boundaries:

1. Repositories: this repository only.
2. Components or modules: `module:models` required assessment and this work-item package.
3. Interfaces, schemas, config, or infra: none in this revision.
4. Agentic, process, documentation, or phase boundaries: initial spec drafting before a canonical work-item artifact exists.

Source spec sections:

1. `SPEC-009`, `Non-scope`, and `RISK-005`.

Validation cues:

1. `VER-009` confirms that spec drafting remains named and no new pre-spec lifecycle mechanism appears.

Rejected alternatives:

1. Remove spec drafting from the assessment rule; rejected because it is a high-value model/reviewer decision point.
2. Add a pre-spec gate now; rejected because it would expand lifecycle design beyond the policy reorganization.

## Decision Drivers

1. The canonical module already governs more than sub-agent model selection.
2. Draft/frozen next-stage choices drive future work more than mostly unexposed current-session facts.
3. Large anchor specs can hand off to planning rather than execution.
4. Platform-specific task/thread vocabulary collides with Plan Tasks and delegated runs.
5. Policy movement must not weaken authorization, concurrency, reviewer, reporting, or integration safeguards.
6. Current templates and validator fixtures make terminology and selection fields externally consumed interfaces.

## Constraints

1. Keep the stable canonical path and `module:models` ID.
2. Keep lifecycle stages, planning shapes, execution cascade, policy profiles, tier meanings, and concurrency cap unchanged.
3. Update template sources before generated outputs.
4. Preserve historical work items and the original checkout's operator-owned draft.
5. Make only current consumer changes needed for semantic consistency and validation.

## Future Durable-Doc Boundary

No repository-level architecture summary is required. A separate future work item may design a deliberate pre-spec model/reviewer selection surface if the operator chooses to expand lifecycle entry behavior.

## Approval

- Status: Approved
- Superseded by: None
