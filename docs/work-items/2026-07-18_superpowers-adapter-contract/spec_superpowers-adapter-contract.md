# Superpowers Adapter Contract Spec

Work ID: `2026-07-18_superpowers-adapter-contract`
Short ID: `superpowers-adapter-contract`
Status: Approved
Harness release: `0.7+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:artifact-style`, `module:models`, `module:execution-quality`, `rule:lifecycle.superpowers-compatibility`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.work-item-architecture-decisions`, `rule:models.strategy-required`, `rule:models.selection-dimensions`, `rule:models.approved-strategy-authorized`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

Artifact style: final-content draft. The harness owns durable artifact location and lifecycle; Superpowers remains an execution method inside the approved boundary.

## Goal

Define a compact adapter contract that lets the Dev Doc Harness and Superpowers coexist without duplicate durable artifacts, competing approval paths, redundant plan content, or accidental model inheritance.

## Source and Intent

Source input:

1. The operator requested an investigation of Superpowers compatibility, plan structure, model selection, and task-handoff behavior.
2. The investigation compared the repository's July 2026 compatibility guidance with local Superpowers `5.0.7`, installed Superpowers `6.1.1`, and the Superpowers `v6.0.0` release notes.
3. The operator selected an implementation-ready contract on 2026-07-18 and resolved the principal coexistence decisions in this work item's planning discussion.

Desired operator outcome:

1. A planner and executor can use Superpowers where it improves planning and execution quality while the harness remains the only durable repository record and approval authority.

Success summary:

1. Current harness guidance, templates, and validation will state one coherent boundary for artifact placement, executable plan form, task context, execution artifacts, and model selection.
2. The resulting policy will support both Superpowers-enabled and Superpowers-unavailable environments without duplicating their task or lifecycle models.

## Scope Boundary

### In scope

1. Define the repository's Superpowers adapter contract for canonical artifact placement, plan conversion, executable-plan metadata, task content, post-freeze execution, ephemeral Superpowers artifacts, and model-selection boundaries.
2. Update the active repository guidance and canonical harness owners needed to make the contract discoverable and non-contradictory.
3. Update current plan-template sources and generated outputs only where they need to support the selected contract.
4. Add focused structural validation for active policy, template, and generated-template behavior. Validation must exclude frozen historical work items and legal text from style or conversion scans.
5. Document the fallback behavior for a planning or execution environment where Superpowers is unavailable.

### Non-scope

1. Modify, fork, pin, or otherwise change the external Superpowers plugin.
2. Rewrite frozen historical specs, plans, or prior Superpowers-derived headers.
3. Create a second durable `docs/superpowers` artifact tree, a Superpowers-specific task runner, or a new repository-wide worktree lifecycle.
4. Make the Codex runtime reveal a root model or reasoning effort when the platform does not expose it.
5. Replace the active `economy-default` policy, redefine vendor-neutral capability tiers, or require a named concrete model when none is exposed.
6. Add durable storage or cleanup requirements for ephemeral Superpowers task briefs, review packages, progress ledgers, or similar execution aids.

### Assumptions

1. Repository and global `AGENTS.md` guidance is an appropriate durable location for a project-specific override of Superpowers' default spec and plan paths.
2. The currently installed Superpowers workflow continues to permit user or project preferences to override its default plan placement.
3. Superpowers task sizing, pre-flight review, and per-task execution artifacts are useful when they do not supersede the harness lifecycle or create competing durable records.
4. Codex may not expose the root task's concrete model or reasoning effort to the agent; `not exposed` is accurate unless the operator or platform supplies the value.

### Open questions

1. None identified for the adapter contract. The later plan must identify the exact generated template sources and validator assertions after inspecting their current ownership boundaries.

## Repository Context

### Current state

1. `AGENTS.md`, the harness router, lifecycle reference, operator note, and README already make the harness work-item package canonical and prohibit creating `docs/superpowers` merely for compatibility.
2. The current small/medium plan template uses stable `TASK-*` and `CHECK-*` sections, but several historical plans include a Superpowers-derived mandatory-execution header and checkbox wording.
3. Superpowers `5.0.7` already used its own default `docs/superpowers` locations, plan header, and checkbox-driven step format. Superpowers `v6.0.0` added task right-sizing, global constraints, task interfaces, explicit per-dispatch model selection, pre-flight review, and changed execution packaging.
4. The current model policy records policy-relative recommendations and correctly permits `not exposed` runtime fields, but it does not yet define how Superpowers' explicit small-task dispatch choices consume the approved policy envelope.

### Evidence read

1. `AGENTS.md`.
2. `.agents/skills/dev-doc-harness/SKILL.md`.
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
4. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.
5. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
6. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`.
7. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md` and `small-medium-work-item-plan.md`, their source blocks, assembly manifests, and `scripts/test_harness_policy.py`.
8. `docs/work-items/2026-07-07_superpowers-compat-guidance/` and selected July 2026 work items that show later plan-shape and model-policy evolution.
9. Local Superpowers `5.0.7` at `C:\\Work\\Codex\\superpowers\\` and installed Superpowers `6.1.1` skill sources.
10. Superpowers `v6.0.0` release notes and the cited `writing-plans` source revision. These external sources inform compatibility targets; the implementation plan must preserve a compact local evidence record if it relies on mutable external claims.

### Constraints and compatibility

1. Durable harness artifacts must remain under `docs/work-items/<work-id>/`; a Superpowers default path is overridden by applicable project or global guidance.
2. The harness freeze gate remains the only approval, commit, pause, and continuity-routing authority before implementation.
3. Superpowers may shape task sizing, pre-flight review, and execution mechanics only after the approved harness route authorizes execution.
4. Current policy must remain useful without Superpowers. It must provide a small fallback task-sizing cue rather than duplicate the full Superpowers methodology.
5. Policy wording must distinguish dependencies from interfaces, policy recommendations from observed runtime configuration, and durable records from ephemeral execution aids.

## Commitments and verification

### `SPEC-001` Canonical placement and preference override

`Constraint · Preserve`

Statement:

1. The repository must name `AGENTS.md` as the project-level preference that overrides Superpowers' default spec and plan locations for harness-managed work.
2. New durable specs, plans, snapshots, handoffs, and changelog sources must remain in the canonical harness work-item package.
3. `docs/superpowers` may not be created or populated for current work except for the existing historical-continuity pointer-stub exception.

#### `VER-001` Placement guidance is unambiguous

Covers: `SPEC-001`.

Criterion: An agent reading the active guidance can determine both that Superpowers defaults are overridable and that the repository's canonical work-item path is the selected override.

Expected evidence: Focused policy validation and review of the active guidance; no new duplicate durable artifact path is introduced.

### `SPEC-002` Executable plan form without checklist ambiguity

Statement:

1. A canonical plan may include one merged Superpowers execution meta-header only when the plan is intended to be executed through the approved Superpowers workflow after the harness freeze and continuity route.
2. The meta-header must preserve harness authority for scope, model-policy bounds, variance, and final integration.
3. Canonical plan steps must use stable task IDs and numbered steps, not checkbox task lists.
4. A plan that declares Superpowers execution must provide task detail sufficient for Superpowers to execute and review the work effectively, including appropriately sized steps and clear task boundaries.

#### `VER-002` Meta-header and enumerated execution steps cohere

Covers: `SPEC-002`.

Criterion: Current plan-template guidance makes the meta-header conditional, links execution to the post-freeze route, and excludes checkbox task syntax from the canonical plan form.

Expected evidence: Generated-template inspection and focused validator fixtures that distinguish allowed numbered steps from forbidden canonical checkbox lists.

### `SPEC-003` Proportional task context and interfaces

Statement:

1. A Superpowers-oriented plan must include a Global Constraints section or equivalent task-local context only when a reference or concise summary is necessary for the plan or task to be self-contained and clear to an executor.
2. Constraints and risks already reliably expressed through approved spec commitments, architecture decisions, task instructions, or Plan Checks must not be repeated merely to fill a Global Constraints section.
3. Task interfaces must describe inputs consumed and outputs produced when those contracts matter to neighboring tasks or a fresh executor.
4. Task dependencies must remain separate from interfaces: dependencies describe readiness or ordering, while interfaces describe task-boundary inputs and outputs.
5. When Superpowers is unavailable, harness guidance should offer a concise fallback: make a task independently executable and verifiable, but do not impose a competing detailed task-sizing model.

#### `VER-003` Task context is sufficient without duplication

Covers: `SPEC-003`.

Criterion: Template and policy guidance explain the self-containment test, the conditional use of global constraints, the interface/dependency distinction, and the non-Superpowers fallback.

Expected evidence: Structural checks plus review of a representative generated plan shape.

### `SPEC-004` One lifecycle with ephemeral execution aids

Statement:

1. The harness freeze gate, approved strategy, and continuity choice must complete before a Superpowers execution flow starts.
2. Superpowers pre-flight reviews, task briefs, review packages, progress ledgers, and similar execution aids are allowed when they remain ephemeral and do not become canonical planning artifacts or a second approval route.
3. The approved harness plan must not prompt for a second generic choice between Superpowers execution modes after the freeze gate; any execution method must remain compatible with the recorded strategy and fallback.

#### `VER-004` Lifecycle authority remains singular

Covers: `SPEC-004`.

Criterion: Active guidance presents one durable approval and handoff route, while allowing the selected Superpowers method to operate inside the authorized execution boundary.

Expected evidence: Scenario-based validator coverage and a focused policy-boundary review.

### `SPEC-005` Deliberate model selection without false runtime claims

Statement:

1. The harness must recommend the minimum suitable policy-relative model allocation for planning, the main execution task, and consequential or high-risk sub-agent roles.
2. The harness must record model generation, resolved profile, and reasoning effort as `not exposed` unless the platform exposes them or the operator explicitly provides an override.
3. Superpowers may dispatch small, task-specific executors and reviewers within the approved harness policy and availability/fallback range, but each Superpowers dispatch must deliberately name its model allocation rather than silently inherit an unknown session model.
4. Completion reporting must distinguish the approved recommendation from the actual allocation when the platform exposes it, and otherwise state that the resolved runtime allocation was not exposed.
5. A Superpowers per-task allocation outside the approved policy envelope, fallback, concurrency guardrail, write authority, or review boundary requires the existing approval path.

#### `VER-005` Model envelope and dispatch behavior are explicit

Covers: `SPEC-005`.

Criterion: Model-policy guidance and templates preserve `not exposed`, define the harness recommendation envelope, permit Superpowers small-task delegation within it, and prohibit silent inheritance as an execution practice.

Expected evidence: Policy and generated-template checks plus review fixtures for exposed, not-exposed, operator-override, in-envelope, and out-of-envelope cases.

### `SPEC-006` Narrow, durable enforcement

Statement:

1. Implementation must update only canonical owners, their necessary routers or operator-facing summaries, source templates, generated templates, and focused validation artifacts.
2. Structural validation must inspect current active policy and template surfaces without rewriting or treating frozen historical artifacts as non-conforming.
3. The implementation plan must preserve mutable Superpowers-version evidence only when a validation rule or compatibility claim depends on it; it must not turn transient execution packages into durable harness artifacts.

#### `VER-006` Enforcement is targeted and history-safe

Covers: `SPEC-006`.

Criterion: Validation proves the adapter contract on active surfaces and fixtures while historical work-item artifacts remain untouched.

Expected evidence: Full harness policy validation, template assembly freshness check, targeted negative fixtures, and diff inspection.

## Architecture Decisions

Architecture snapshot status:

1. Required before the combined spec-and-plan package freezes. The decision has multiple durable process boundaries and later execution depends on them.

Decision summary:

1. Drivers: preserve one canonical durable record; keep Superpowers execution quality; prevent duplicate plan content and opaque model inheritance; retain a usable non-Superpowers fallback.
2. Constraints: repository `AGENTS.md` is the preference source; the harness owns approvals, continuity, variance, changelog discipline, and final integration; external Superpowers files remain out of scope.
3. Selected approach: use a brief adapter contract that maps ownership at the boundary rather than copying Superpowers' schema into harness templates or suppressing Superpowers execution features.
4. Affected boundaries: root repository instructions; harness lifecycle, model, execution-quality, and operator guidance; plan-template sources and generated templates; policy validator; future Superpowers-enabled execution tasks.
5. Rejected alternatives: ban Superpowers-specific plan metadata entirely; copy Superpowers files into `docs/superpowers`; make every Superpowers execution artifact durable; make harness task sizing compete with Superpowers; require a concrete runtime model that Codex does not expose.
6. Validation cues: `VER-001` through `VER-006`, focused generated-template fixtures, and a policy-boundary review.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Repository guidance to Superpowers: path override, plan form, lifecycle boundary, and permitted execution behavior.
2. Harness plan templates: optional merged execution meta-header, numbered steps, conditional global constraints, task interfaces, dependency distinction, and model-policy references.
3. Harness model policy: main-task and consequential-role recommendation envelope plus permitted Superpowers small-task dispatch behavior.
4. Harness validator: active-surface and fixture checks for the adapter contract.

### Data, config, and persistence

1. No product data, runtime persistence, migration, or external API configuration changes are expected.
2. Repository policy and generated templates are durable documentation/configuration inputs; Superpowers task packages remain ephemeral unless independently required as harness evidence.

### State and control flow

1. Planning begins in the harness work-item package.
2. The harness freeze gate approves and commits the durable package, then selects same-task or new-task continuity.
3. After fresh authorization, Superpowers may perform pre-flight, dispatch explicitly selected in-envelope task agents, and use ephemeral execution aids.
4. The orchestration thread retains final integration, validation, variance handling, and the user-facing result under harness policy.

### Safety, security, privacy, migration, and rollback

1. The work changes process guidance, not product runtime behavior. Its principal risk is persistent agent workflow drift.
2. No new secrets, user data, remote writes, or external plugin modifications are in scope.
3. If the adapter produces conflicting authorization, lifecycle, or model-policy instructions, stop for an amendment rather than silently selecting an interpretation.
4. Rollback consists of reverting the focused policy/template/validator implementation commit while preserving the frozen work-item record.

## Risks and Rejected Alternatives

### `RISK-001` Over-specifying the adapter

Decision or mitigation:

1. Keep canonical rules limited to durable boundaries and delegation policy. Reference Superpowers for task sizing, pre-flight, and ephemeral execution mechanics rather than reproducing them.

### `RISK-002` Under-specifying placement override

Decision or mitigation:

1. Make project or global `AGENTS.md` the explicit source of the Superpowers path preference and test the active guidance for the canonical work-item outcome.

### `RISK-003` Duplicate or conflicting model decisions

Decision or mitigation:

1. Separate the harness policy envelope from Superpowers per-dispatch selection. Preserve `not exposed` fields and require escalation only outside the approved envelope.

### `RISK-004` Historical-document churn

Decision or mitigation:

1. Validate current owners and synthetic fixtures only. Do not rewrite historical work-item artifacts to conform to the new adapter.

### `RISK-005` Superpowers unavailable or changes again

Decision or mitigation:

1. Retain a concise no-Superpowers fallback and record the compatibility target in active guidance. Treat a future material Superpowers workflow change as a review input, not as permission to create competing artifacts.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spec: superpowers-adapter-contract -- define coexistence boundaries` | `2026-07-18_superpowers-adapter-contract -- define coexistence boundaries` | Approval commit for this staged spec-only package, if the operator approves the staged-planning exception. |
| Implementation | `docs: superpowers-adapter-contract -- align durable planning and execution` | `2026-07-18_superpowers-adapter-contract -- align durable planning and execution` | Expected policy, template, documentation, and validation delivery; refine in the later plan if needed. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-18_superpowers-adapter-contract/changelog/*.md` | Create the planning approval fragment only if this draft is approved and frozen. |
| Root changelog consolidation | Living | No | Operator-owned consolidation checkpoint | `CHANGELOG.md` | Ordinary work-item commits do not edit the root changelog. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Cover active guidance, generated templates, fixture behavior, lifecycle, and model-envelope cases. |
| Testing guide delta | Living delta | Yes | During or after implementation | `deltas/testing-guide.delta.md` | Record validator and assembly commands. |
| Operator manual delta | Living delta | Yes | After implementation | `deltas/operator-manual.delta.md` | Explain the concise adapter contract and no-Superpowers fallback. |
| API reference delta | Living delta | No | Not applicable | N/A | No public runtime API changes. |
| Architecture snapshot | Snapshot | Yes | Before combined package freeze | `snapshots/architecture.snapshot.md` | Preserve the coexistence boundary and rejected alternatives. |
| Architecture summary delta | Living delta | No | Not applicable | N/A | The work-item snapshot is sufficient; no repository architecture document is in scope. |
| Compatibility evidence record | Evidence | Deferred | Before plan freeze if a mutable-version claim is enforced | `evidence/superpowers-compatibility.md` | Required only if implementation validation depends on an external version claim rather than current local behavior. |

## Next-task handoff

Planning shape:

1. Explicit staged small/medium planning. The operator requested this spec before an implementation plan so the coexistence contract can be reviewed as the decision anchor.

Current draft boundary:

1. This draft is not frozen, committed, or a task-creation boundary.
2. Before a spec-only freeze, create the required architecture snapshot, confirm the documentation-matrix decisions, and add the planning-approval changelog source fragment.
3. If the operator approves a spec-only freeze, the frozen package will be this spec, `snapshots/architecture.snapshot.md`, and the matching planning-approval fragment.
4. Next activity after that actual frozen boundary: draft `plan_superpowers-adapter-contract.md` as a fresh planning activity using the approved spec and snapshot.
5. Implementation authorization: not granted. Do not edit active policy, templates, documentation, or validation until a later combined or phase plan passes its own freeze gate and the operator gives fresh authorization.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments are bounded and every obligation is in a Statement.
- [x] Verification Criteria identify evidence without prescribing implementation procedures.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, state flow, and process-safety impacts are checked.
- [x] Risks and rejected alternatives are explicit.
- [x] Documentation artifact decisions have paths, stages, or deferral conditions.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved required decision or ownerless deferral remains for the staged spec-only package.

## Approval

- Status: Approved
- Superseded by: None
