# Orchestration and Model Policy Spec

Work ID: `2026-08-02_task-orchestration-model-policy`
Short ID: `task-orchestration-model-policy`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_task-orchestration-model-policy.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:artifact-style`, `module:models`, `module:architecture`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.work-item-architecture-decisions`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Reorganize the current model and sub-agent policy around an actionable upcoming-stage selection, adopt portable orchestration-session terminology, distinguish planning-stage and execution-stage methods and review, and remove duplicated notation without losing existing model, delegation, authorization, review, reporting, or integration rules.

## Source and Intent

Source input:

1. The operator's inline review of `.agents/skills/dev-doc-harness/references/artifact-contract.md` asks for the lifecycle-stage-boundary section to own a named rule that the model/orchestration policy can cite.
2. The operator's inline review of `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` observes that the module now governs task or session orchestration and model selection, not only sub-agent models.
3. The operator's seven-point review asks for a title that matches the broadened scope, primary emphasis on the draft or approved next-stage selection, an unambiguous stage method, continuity that covers planning or execution, explicit stage applicability, and a nonduplicative required-notation section.
4. The operator approved the proposed reorganization, clarified that model selection has three independent dimensions—generation, capability tier, and reasoning effort—and required all important existing rules to survive relocation.
5. The operator approved replacing platform-specific `Codex task` terminology in the current scope and requested an isolated worktree for the planning package.
6. The operator noted that initial spec drafting also deserves deliberate model and reviewer selection, while preferring not to add a new pre-spec mechanism in this revision.
7. The operator's uncommitted draft in the original checkout moves capability-tier material into a dedicated model section and begins reducing current-task emphasis; it is design input, not an implementation target to copy without reconciling the approved package.

Desired operator/user outcome:

1. A maintainer can read the canonical module from top to bottom and understand what lifecycle determines, what the orchestration policy selects, which rules apply to planning versus execution, and how those decisions are rendered.
2. New planning artifacts emphasize one actionable next-stage recommendation or approved selection; optional current-session facts no longer dominate the decision.
3. Current reusable harness surfaces use portable, nonoverlapping vocabulary for top-level orchestration sessions, Plan Tasks, bounded agent runs, and external method sessions.
4. Existing sub-agent safeguards and reviewer obligations remain intact and validator-backed after the reorganization.

Success summary:

1. `module:lifecycle` owns a named stage-boundary rule and `module:models` cites it rather than restating lifecycle transitions.
2. `subagent-model-policy.md` keeps its stable path and `module:models` ID but presents a broader title, scope, section order, and next-stage selection contract.
3. Current policy, template sources, generated templates, operator guidance, and validation agree on orchestration-session terminology, stage-sensitive method/review, and generation/tier/reasoning dimensions.

## Scope Boundary

### In scope

1. Rename the document title and scope to describe task or session orchestration and model policy while retaining the stable filename and `module:models` ID.
2. Add `rule:lifecycle.stage-boundaries` to `module:lifecycle` and make the upcoming-stage selection cite it as the sole owner of the documented next lifecycle stage.
3. Replace current reusable uses of `Codex task` and equivalent `orchestration thread` terminology with the defined term **orchestration session** where they mean the top-level operator-facing conversation or controller context.
4. Define **current orchestration session**, **next-stage orchestration session**, **Plan Task**, **agent run/sub-agent run**, and **external method session** so their meanings do not overlap.
5. Rename execution continuity to next-stage continuity, use `same orchestration session` and `new orchestration session` as the `Run in` values, and replace `rule:models.execution-continuity` with `rule:models.next-stage-continuity` in current consumers.
6. Make the documented next-stage selection primary and current-session runtime facts optional, compact diagnostic metadata.
7. Define `Method` as the workflow for the documented next lifecycle stage: planning method and planning review for plan-drafting stages, execution method and Plan Task/final review for execution stages.
8. Define model selection through three independent dimensions: model generation, capability tier, and reasoning effort. Concrete resolved profiles remain runtime mappings rather than a fourth durable selection dimension.
9. Reorganize the catch-all common rules into named sub-agent strategy subsections while preserving assessment, authorization, context, role fields, fit, concurrency, fallback, reporting, escalation, reviewer, and final-integration requirements.
10. Reduce `Required notation` to a rendering and placement contract, with normative meanings owned by preceding sections and optional role examples kept in `module:role-examples`.
11. Update direct current consumers: lifecycle and maintenance references, freeze and startup guidance, the router, role examples, root operator guidance, template source blocks, generated templates, and focused policy validation.
12. Preserve the existing obligation to assess model and reviewer/sub-agent fit before initial spec drafting.

### Non-scope

1. Create a durable pre-spec selection artifact, a new lifecycle gate before spec drafting, or a new operator interaction protocol for the first planning stage.
2. Rename the `subagent-model-policy.md` file, `module:models`, schema IDs, or unrelated stable rule IDs.
3. Rename historical frozen work-item artifacts or rewrite quoted historical terminology.
4. Replace every generic use of `task`, `thread`, or `session` in the repository when it does not denote the top-level orchestration-session concept governed here.
5. Change the lifecycle stage set, planning shapes, execution-method cascade, active `economy-default` repository policy, capability-tier meanings, current GPT-5.6 mappings, concurrency cap, authorization boundary, or final-integration owner.
6. Add provider discovery, model availability probing, runtime session control, task creation, or sub-agent tooling.
7. Require a reviewer sub-agent for all spec drafting; the missing pre-spec selection surface remains a deliberate follow-up topic.

### Assumptions

1. **Orchestration session** is the most precise portable term for the top-level operator-facing conversation or controller context; bare **session** and **agent session** would overlap more easily with sub-agent runs and external method sessions.
2. Current nonhistorical consumers can migrate together in one cohesive implementation without a compatibility alias for the retired `rule:models.execution-continuity` ID.
3. Model generation normally resolves to `latest available` in Codex unless a provider or compatibility constraint requires a concrete generation; it must still remain explicit and independent from tier and effort.
4. The current template assembler remains the only supported way to update generated templates.
5. The original checkout's uncommitted policy draft remains operator-owned and untouched; the approved durable package preserves its material intent for implementation in the isolated worktree.

### Open questions

1. None. The operator can revise terminology, rule-ID migration, or the bounded pre-spec non-scope during draft review before freeze.

## Repository Context

### Current state

1. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` owns `module:models`, but its title and introduction describe only sub-agent model selection while its body also governs orchestration mode, continuity, execution method, reviewer contracts, fallbacks, reporting, and final integration.
2. `## Selection dimensions` mixes optional current-planning-task facts with the critical next-stage selection and folds permanent model-tier definitions into the same section.
3. `Method` and `Plan Task reviewers` are presented as universal next-stage fields even though `plan drafting` and `phase-plan drafting` are valid next lifecycle stages without implementation Plan Tasks.
4. `## Execution continuity`, `Planning Codex task`, and `execution Codex task` incorrectly imply that every post-freeze stage is implementation.
5. `## Common rules` contains distinct normative areas whose current placement makes loss or duplication likely during edits.
6. `## Required notation` repeats selection semantics and embeds four example role rows even though `.agents/skills/dev-doc-harness/references/subagent-role-examples.md` already owns advisory examples.
7. `.agents/skills/dev-doc-harness/references/artifact-contract.md` has a `## Lifecycle stage boundaries` section but no matching owned rule ID.
8. Template source blocks under `.agents/skills/dev-doc-harness/assets/templates/blocks/` feed four generated primary templates; generated files must not be edited directly.
9. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` hardcodes current titles, rule IDs, field labels, and `same/new Codex task` values across several focused checks and fixtures.
10. The active repository policy is `economy-default`, and the isolated worktree baseline passes every harness policy check.

### Evidence read

1. The operator's two inline review comments, seven-point review, approved responses, terminology question, and isolated-worktree instruction in the current conversation.
2. The operator's working diff for `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` in the original checkout.
3. `.agents/skills/dev-doc-harness/SKILL.md`.
4. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
5. `.agents/skills/dev-doc-harness/references/naming-conventions.md`.
6. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`.
7. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
8. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`.
9. `.agents/skills/dev-doc-harness/references/maintenance-architecture.md`.
10. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.
11. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`.
12. `.agents/skills/dev-doc-harness/references/implementation-changelog.md`.
13. Small/medium templates, relevant template source blocks, assembly script references, current validator checks, `README.md`, `AGENTS.md`, and the prior model-selection work item at `docs/work-items/2026-07-11_model-selection-dimensions/`.

### Constraints and compatibility

1. Canonical references own reusable policy; templates and summaries must consume rule IDs and compact prompts without becoming second owners.
2. The rule graph must retain one owner per current rule and all current references must resolve after the continuity-rule migration.
3. Historical work items are immutable evidence and remain excluded from terminology cleanup.
4. Generated templates change only through `assemble_templates.py --write` after their source blocks are updated.
5. The policy reorganization must preserve every material rule listed in the current owner table and every distinct obligation presently located under `Common rules`, method/reviewer, reporting, escalation, final review, and final integration.
6. Planning artifacts and the required architecture snapshot are the only repository files changed before the Planning Artifact Freeze Gate.

## Commitments and verification

### `SPEC-001` Broaden the canonical scope without moving the module

Statement:

1. The canonical policy must use a broad orchestration and model title and scope while retaining `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`, `module:models`, current repository policy names, and unrelated stable schema/rule IDs.

#### `VER-001` Scope and stable identity

Covers: `SPEC-001`.

Criterion: Current canonical and routing surfaces identify `module:models` as the owner of upcoming-stage orchestration, model selection, sub-agent strategy, review, and integration without changing its path or module ID.

Expected evidence: Focused validator assertions plus diff inspection of the canonical module, maintenance catalog, and router.

### `SPEC-002` Separate lifecycle stage ownership from runtime selection

Statement:

1. `module:lifecycle` must own `rule:lifecycle.stage-boundaries`, which determines the documented next lifecycle stage; `module:models` must consume that value and own how the stage runs without restating the lifecycle transition table.

#### `VER-002` Single stage owner

Covers: `SPEC-002`.

Criterion: The rule graph has one owner for `rule:lifecycle.stage-boundaries`, and the upcoming-stage selection cites it while containing no duplicate lifecycle-stage mapping.

Expected evidence: Rule-graph validation, focused text assertions, and canonical-reference diff review.

### `SPEC-003` Adopt portable orchestration-session continuity

Statement:

1. Current reusable policy and direct consumers must define and consistently use orchestration-session terminology, `same orchestration session` and `new orchestration session` continuity values, and `rule:models.next-stage-continuity` for planning-stage or execution-stage transitions.
2. Current-session runtime facts must be optional compact diagnostic metadata and must not replace actionable upcoming-stage generation, tier, effort, method, review, or continuity values.

#### `VER-003` Session terminology and continuity

Covers: `SPEC-003`.

Criterion: Current nonhistorical surfaces distinguish orchestration sessions, Plan Tasks, agent runs, and external method sessions; stale `Codex task`, `orchestration thread`, and current `rule:models.execution-continuity` terminology is absent except where a platform-specific product name or immutable history requires it.

Expected evidence: Focused validator fixtures, scoped repository search, generated-template inspection, and historical-path diff check.

### `SPEC-004` Make method and review stage-sensitive

Statement:

1. `Method` must identify the workflow for the documented next lifecycle stage.
2. For `plan drafting` and `phase-plan drafting`, the selection must record a planning method and planning-review arrangement without applying the execution-method cascade or Plan Task reviewer contract.
3. For `plan execution` and `phase execution`, the selection must record the execution method and apply the existing cascade and route-specific Plan Task/final-review contract.

#### `VER-004` Stage applicability

Covers: `SPEC-004`.

Criterion: Canonical policy and current templates use a general `Review` field and state the planning-versus-execution applicability boundary without changing the existing execution cascade or review obligations.

Expected evidence: Policy inspection, template-source/generated parity, and validator fixtures for both a planning-stage and an execution-stage selection.

### `SPEC-005` Preserve three independent model dimensions

Statement:

1. Every actionable upcoming-stage allocation must select model generation, capability tier, and reasoning effort independently.
2. `latest available` is a valid actionable generation instruction; `not exposed` is valid only for optional observed current-session facts or runtime mappings, not for required upcoming-stage generation, tier, or effort.
3. Resolved profile and availability remain runtime mapping/fallback information rather than additional durable model-selection dimensions.

#### `VER-005` Generation, tier, and effort

Covers: `SPEC-005`.

Criterion: Canonical policy, required notation, template prompts, and validator fixtures expose generation, tier, and effort separately while preserving vendor-neutral tiers and the current GPT-5.6 mapping.

Expected evidence: Focused semantic validation and template inspection.

### `SPEC-006` Preserve and clarify sub-agent strategy rules

Statement:

1. The reorganization must preserve the current requirements for upcoming-stage assessment, bounded authorization, context strategies, role fields, planning-stage phase-drafter guidance, model/effort selection, fit, concurrency, fallbacks, escalation, independent review, reports, and final integration ownership.
2. The catch-all `Common rules` section must be replaced by named strategy subsections with one clear local owner for each existing `rule:models.*` entry.

#### `VER-006` Rule-preservation inventory

Covers: `SPEC-006`.

Criterion: Every current owned rule and material obligation maps to exactly one destination section and remains protected by an owner, focused validator assertion, or explicit review checklist.

Expected evidence: Before/after rule inventory in the implementation diff, owner-heading validation, focused policy assertions, and independent or fallback final review.

### `SPEC-007` Make required notation a thin rendering contract

Statement:

1. `Required notation` must specify placement and compact rendering only, refer to the normative sections for meanings, render current-session facts only when exposed or material to continuity, and avoid repeating selection, authorization, or lifecycle semantics.
2. Optional role examples must remain advisory under `module:role-examples`; the four-row example table must not remain embedded in the normative notation section.

#### `VER-007` Nonduplicative notation

Covers: `SPEC-007`.

Criterion: The canonical notation section contains one skeletal upcoming-stage rendering and one sub-agent assessment/role rendering reference without duplicating the preceding rules or example catalog.

Expected evidence: Duplicate-policy validation, manual section comparison, and advisory-example reference inspection.

### `SPEC-008` Propagate and validate current consumers

Statement:

1. All direct current policy, operator, template-source, generated-template, and validator consumers must migrate together, while frozen historical work items remain unchanged.
2. The implementation must update template source blocks first, regenerate all affected primary templates through the assembler, and leave no source/generated divergence.

#### `VER-008` Consumer parity and historical integrity

Covers: `SPEC-008`.

Criterion: Template assembly and the full harness validator pass; scoped searches show only intentional old terminology; the final diff contains no modification to pre-existing work-item artifacts.

Expected evidence: Assembler check, full validator output, scoped `rg` output, `git diff --check`, and path-limited diff inspection.

### `SPEC-009` Preserve the pre-spec assessment boundary without expanding it

Statement:

1. The canonical strategy must continue to require deliberate model and reviewer/sub-agent assessment before initial spec drafting, but this work item must not add a pre-spec artifact, lifecycle stage, or freeze gate.

#### `VER-009` Deliberate deferral

Covers: `SPEC-009`.

Criterion: The reorganized policy still names spec drafting in the required upcoming-stage assessment and records the missing durable pre-spec selection surface as future work rather than silently treating it as solved.

Expected evidence: Canonical-policy inspection and final diff review against the explicit non-scope.

## Architecture Decisions

Architecture snapshot status: `Required` at `snapshots/architecture.snapshot.md` because this work changes rule ownership, stage/method boundaries, stable terminology interfaces, and generated-template consumers used by future planning sessions.

Decision summary:

1. Drivers: platform portability, stage-correct selection, minimal duplication, stable rule ownership, preservation of sub-agent safeguards, and fresh-session handoff clarity.
2. Constraints: retain the module path and ID; preserve current lifecycle shapes, execution cascade, model policies, authorization, and historical artifacts; edit generated templates only through source assembly.
3. Selected approach: make lifecycle the sole owner of the next-stage value and organize `module:models` around how that stage runs, using orchestration-session terminology and three model dimensions.
4. Affected boundaries: lifecycle and models canonical references, freeze/startup consumers, current templates and generated outputs, validator fixtures, router/catalog summaries, root operator guidance, and advisory role examples.
5. Rejected alternatives: defer the terminology migration and immediately revisit all revised sections; perform a repository-wide unqualified session rewrite; add a pre-spec lifecycle gate; rename the stable module path or ID.
6. Validation cues: `VER-001` through `VER-009`, rule-graph validation, template parity, stale-term searches, and independent or fallback policy review.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Rule interface added: `rule:lifecycle.stage-boundaries`.
2. Rule interface replaced in current consumers: `rule:models.execution-continuity` becomes `rule:models.next-stage-continuity`.
3. Terminology interface: orchestration session, current orchestration session, next-stage orchestration session, Plan Task, agent/sub-agent run, and external method session.
4. Selection interface: Next lifecycle stage; Orchestration with Method, Run in, and Review; Model with Generation, Capability tier, and Reasoning; applicable Fallbacks and limits.
5. Template prompt and validator fixture interfaces change to match the selection interface.
6. Stable interfaces retained: `module:models`, policy filename, planning schemas, orchestration-mode values, capability-tier values, context strategies, policy names, and final integration ownership.

### Data, config, and persistence

1. No runtime data, persistence, migration, or application configuration changes.
2. Markdown policy, template sources, generated Markdown, Python validation fixtures, and one implementation changelog fragment change during implementation.

### State and control flow

1. Lifecycle selects the documented next stage from the frozen package and planning shape.
2. `module:models` selects the stage method, review arrangement, session continuity, orchestration mode, generation, tier, effort, and bounded fallbacks for that stage.
3. A planning-stage method uses planning review; an execution-stage method uses the existing execution cascade and route-specific reviewer contract.
4. The selected same/new orchestration-session route then hands the frozen package to the applicable startup or transition consumer.
5. Current-session facts inform continuity when exposed but are not a required decision group.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, compliance, destructive-operation, or user-data impact is expected.
2. Migration is limited to current reusable harness surfaces; historical artifacts remain immutable.
3. Rollback is one cohesive implementation commit because canonical policy, consumers, generated outputs, and validator assertions must remain synchronized.
4. The original checkout's uncommitted draft must not be overwritten, staged, or removed.

## Risks and Rejected Alternatives

### `RISK-001` A rule is lost during section moves

Decision or mitigation:

1. Build the implementation around the current owner table and a paragraph-level obligation inventory; move content by responsibility, then validate every destination and use an independent or focused fallback final review.

Notes:

1. Severity is high because silent policy loss affects future work items and review authorization.

### `RISK-002` Session terminology expands beyond the governed concept

Decision or mitigation:

1. Define **orchestration session** narrowly and migrate only current reusable occurrences that denote that concept; retain product names such as Codex and method-specific external sessions where accurate.

### `RISK-003` Planning-stage method remains underspecified

Decision or mitigation:

1. Require the Method and Review fields for both planning and execution while limiting this revision to applicability semantics; do not invent a new enumerated planning-method cascade.

### `RISK-004` Stable rule-ID migration breaks consumers

Decision or mitigation:

1. Update all current references and validator ownership checks in one cohesive change; frozen historical artifacts remain valid snapshots and are not migrated.

### `RISK-005` The pre-spec concern is accidentally erased

Decision or mitigation:

1. Preserve the explicit spec-drafting assessment obligation and name the missing durable pre-spec mechanism as a future-work boundary in canonical guidance, the architecture snapshot, and `SPEC-009`.

### `RISK-006` Required notation continues to duplicate policy

Decision or mitigation:

1. Make the section a skeletal placement/rendering contract, keep semantic definitions above it, and refer optional examples to `module:role-examples`.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: task-orchestration-model-policy -- approve session-oriented selection contract` |
| Implementation | `docs: task-orchestration-model-policy -- clarify session and stage selection` |

One cohesive implementation commit is required because canonical policy, rule references, template sources, generated templates, summaries, validation, and the implementation changelog fragment form one compatibility boundary.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Implementation changelog source | Living | Yes | During implementation | `docs/work-items/2026-08-02_task-orchestration-model-policy/changelog/implementation-fragment.md` | Create before the implementation commit using the matching implementation subject |
| Root changelog consolidation | Living | As needed | Operator-owned implementation or release checkpoint | `CHANGELOG.md` | Do not update during planning; consolidation remains a separate operator-owned checkpoint |
| Test cases | Snapshot | No | Before implementation | Not created | `SPEC-001` through `SPEC-009`, local Verification Criteria, and validator fixtures preserve the expected behavior without a separate snapshot |
| Testing guide delta | Living delta | No | During or after implementation | Not created | No operator test flow changes |
| Operator manual delta | Living delta | No | After implementation | Not created | README and root instructions are direct current consumers, not a separate manual delta |
| API reference delta | Living delta | No | During or after API work | Not created | No application or public API change |
| Architecture snapshot | Snapshot | Yes | Before implementation | `docs/work-items/2026-08-02_task-orchestration-model-policy/snapshots/architecture.snapshot.md` | Freezes rule ownership, terminology, stage-method applicability, and pre-spec boundary decisions |
| Architecture summary delta | Living delta | No | After review | Not created | No repository-level architecture manual exists or is required for this bounded harness change |
| Current harness policy and templates | Normative/generated | Yes | During implementation | `.agents/skills/dev-doc-harness/` | Update canonical owners and direct consumers; regenerate outputs from source blocks |
| Root operator guidance | Living documentation | Yes | During implementation | `README.md`, `AGENTS.md` | Align compact current terminology and continuity references without duplicating canonical policy |

## Planning shape and transition ownership

Use `rule:lifecycle.planning-shape`, `rule:models.execution-continuity`, `rule:freeze.approval-freeze`, and `rule:execution-quality.execution-thread-start` as the current pre-implementation policy identifiers.

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_task-orchestration-model-policy.md` is drafted and presented with this spec.
3. Required supporting snapshot: `snapshots/architecture.snapshot.md`.
4. Transition owner: `plan_task-orchestration-model-policy.md` owns the `plan execution` transition after the combined package freezes.
5. Next lifecycle stage: `plan execution`.
6. This planning artifact remains a historical snapshot after freeze; it is not rewritten merely because implementation later introduces session-oriented terminology or a replacement continuity rule ID.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments are atomic, bounded, and contain every implementation obligation in their Statements.
- [x] Verification Criteria have valid Covers sets, expected evidence, deterministic placement, and no hidden procedure or scope.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned implementation commit subjects are clear; planning approval has no changelog entry.
- [x] The companion plan and required architecture snapshot are present and the plan owns the implementation handoff.
- [x] The upcoming-stage sub-agent assessment records the operator-authorized Sol/high final reviewer and the unavailability fallback.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
