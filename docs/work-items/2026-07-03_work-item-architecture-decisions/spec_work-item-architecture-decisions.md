# Work-Item Architecture Decisions Spec

Work ID: `2026-07-03_work-item-architecture-decisions`
Short ID: `work-item-architecture-decisions`
Status: Approved
Harness release: `0.4+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `module:architecture`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Goal

Make work-item-bounded architectural decisions a first-class part of the harness planning flow so future specs, snapshots, and plans clearly distinguish problem constraints, deliberate architecture tradeoffs, and implementation sequencing.

## Source and Intent

Source input:

1. Operator review after completing `2026-07-02_orchestration-sizing-large-templates` and `2026-07-02_template-block-assembly`.
2. Operator concern that the current flow says spec versus plan is roughly "what" versus "how", but architectural decisions include both problem-imposed boundaries and deliberate tradeoffs.
3. Operator direction that architecture should stay out of implementation plans except as referenced input, and should belong in specs and/or dedicated files.
4. Operator clarification that this change is only about work-item-bounded architecture for now; durable repository-level documents such as `ARCHITECTURE.md` are future work.

Desired operator/user outcome:

1. Future planning packages make architectural decisions visible before implementation starts.
2. Plans consume and reference architectural decisions instead of silently making new ones.
3. Agents know when to create or mark not applicable a work-item `snapshots/architecture.snapshot.md`.
4. The harness does not yet require, create, or update long-lived repository architecture documents.

Success summary:

1. The lifecycle reference defines when work-item architecture decisions require an architecture snapshot and how those decisions relate to specs, plans, phase plans, variance, and amendments.
2. The templates prompt agents to record architectural decisions in specs or snapshots and to keep plans downstream of those decisions.
3. A dedicated architecture snapshot template exists for work-item-bounded decisions.
4. README and package-local operator guidance explain the work-item-only boundary and leave `ARCHITECTURE.md` for a later deliberate extension.

## Scope Boundary

### In scope

1. Define work-item-bounded architecture decision handling in `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
2. Update durable planning quality guidance so specs preserve architecture decisions and phase plans do not reinterpret them.
3. Add a work-item architecture snapshot template under `.agents/skills/dev-doc-harness/assets/templates/`.
4. Update generated spec template source blocks and manifests so small/medium and large/phased specs include architecture decision prompts and architecture snapshot trigger guidance.
5. Update generated plan and phase-plan template source blocks and manifests so plans cite architecture inputs and route missing or changed architecture back to draft specs, snapshots, or amendments.
6. Update the documentation artifact matrix wording for architecture snapshots and architecture summary deltas.
7. Update `SKILL.md`, README, and package-local operator note only where needed to make architecture routing discoverable without creating a durable-doc workflow.
8. Update validation so current harness surfaces include the new architecture-decision rule, snapshot template, generated-template freshness, and expected docs wording.
9. Update `CHANGELOG.md` before implementation commit.

### Non-scope

1. No repository-level `ARCHITECTURE.md` requirement, template, lifecycle, or update flow.
2. No general durable-document management system for architecture summaries, operator manuals, API references, or other long-lived docs.
3. No ADR directory, ADR numbering scheme, or cross-repository decision registry.
4. No change to the large/phased planning sequence, freeze-gate pause behavior, or post-freeze implementation authorization.
5. No rewrite of frozen historical work-item artifacts.
6. No release marker change beyond using the current `0.4+` harness release in new artifacts.

### Assumptions

1. `module:lifecycle` is the right owner for when an architecture snapshot is required because it already owns work-item layout, documentation matrix, immutable snapshots, and variance classes.
2. `module:quality` should own the quality bar for preserving architectural decisions in specs and phase-plan handoffs.
3. Templates should prompt for architectural decisions but should not copy long reusable policy.
4. A work item may contain architecture decisions even when it is not large/phased.
5. Work-item architecture snapshots are immutable planning snapshots after approval, just like other `snapshots/*.md`.
6. The active repository model policy is `economy-default` from root `AGENTS.md`; architecture-sensitive review can still escalate model strength when justified by `module:models`.

### Open questions

1. None identified after repository-context review.

## Repository Context

### Current state

1. `artifact-contract.md` defines `snapshots/architecture.snapshot.md` as an optional work-item file in both small/medium and large/phased layouts, but does not define when it is required.
2. The documentation artifact matrix currently describes the architecture snapshot as a "work-item-bound decision snapshot" but leaves the `Required?` decision entirely to the drafter.
3. Existing historical architecture snapshots show useful patterns for architecture handoff, especially:
   - `2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`
   - `2026-06-07-followup-hardening/snapshots/architecture.snapshot.md`
   - `2026-06-07-release-versioning/snapshots/architecture.snapshot.md`
   - `2026-06-27-portable-harness-validator/snapshots/architecture.snapshot.md`
4. `policy-architecture.md` currently owns harness module and rule ownership architecture, but not work-item product or process architecture decisions.
5. Generated spec templates have requirements, acceptance criteria, interfaces, data, control flow, risks, planned commits, documentation matrix, and readiness sections, but no dedicated architecture decision prompt.
6. Generated plan templates include spec traceability, change surfaces, model strategy, tasks, validation, variance, and readiness, but do not explicitly say that architecture is upstream of plans.
7. The template assembly workflow introduced by `2026-07-02_template-block-assembly` means primary template changes should be made in source blocks and regenerated into flat templates.

### Evidence read

1. Root `AGENTS.md`
2. `.agents/skills/dev-doc-harness/SKILL.md`
3. `.agents/skills/dev-doc-harness/VERSION`
4. `.agents/skills/dev-doc-harness/references/artifact-contract.md`
5. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
6. `.agents/skills/dev-doc-harness/references/naming-conventions.md`
7. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
8. `.agents/skills/dev-doc-harness/references/policy-architecture.md`
9. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
10. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
11. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
12. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
13. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
14. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.020.common.intent-scope-context.md`
15. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.requirements-acceptance.md`
16. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.040.common.interfaces-risks.md`
17. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md`
18. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.080.common.documentation-matrix.md`
19. `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`
20. `README.md`
21. `.agents/skills/dev-doc-harness/docs/operator-note.md`
22. `docs/work-items/2026-07-02_orchestration-sizing-large-templates/spec_orchestration-sizing-large-templates.md`
23. `docs/work-items/2026-07-02_orchestration-sizing-large-templates/plan_orchestration-sizing-large-templates.md`
24. `docs/work-items/2026-07-02_template-block-assembly/spec_template-block-assembly.md`
25. `docs/work-items/2026-07-02_template-block-assembly/plan_template-block-assembly.md`
26. `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`
27. `docs/work-items/2026-06-07-followup-hardening/snapshots/architecture.snapshot.md`
28. `docs/work-items/2026-06-07-release-versioning/snapshots/architecture.snapshot.md`
29. `docs/work-items/2026-06-27-portable-harness-validator/snapshots/architecture.snapshot.md`

### Constraints and compatibility

1. Current repository-local policy says this substantial documentation/process change must use the harness and stop after the planning freeze gate.
2. Current root `AGENTS.md` selects `economy-default`; do not switch to `enterprise-default` without operator instruction.
3. Template source blocks are the maintainer surface; generated flat templates are the agent-facing surface.
4. `module:architecture` is already used for policy architecture, so work-item architecture wording must avoid confusing the module with product/process architecture decisions.
5. Validator changes should remain lightweight structural checks and should not become semantic adjudication of whether a decision is "architectural enough".
6. `deltas/architecture-summary.delta.md` remains a seed for long-lived documentation updates, not a mandatory durable-doc workflow in this work item.

## Requirements

A requirement defines scope: what the work must provide, change, or preserve. Keep each requirement specific, achievable, relevant to the desired outcome, bounded by lifecycle timing, and testable through acceptance criteria.

### `REQ-001` Work-item architecture decisions are first-class planning content

Rationale:

1. The current spec-versus-plan distinction hides architecture decisions because some decisions arise from problem constraints and some from deliberate tradeoffs.

Acceptance links:

1. Covered by `AC-001`, `AC-002`, `AC-003`, and `AC-005`.

Notes:

1. Work-item architecture includes boundaries and tradeoffs across repositories, components, public or internal interfaces, data models, config, infrastructure, agentic/process orchestration, security/privacy/compliance, migration/rollback, and phase ownership.

### `REQ-002` Architecture snapshots have clear work-item-bounded trigger rules

Rationale:

1. The harness already lists `snapshots/architecture.snapshot.md`, but future agents need a rule for required, not applicable, or deferred matrix decisions.

Acceptance links:

1. Covered by `AC-001`, `AC-002`, `AC-003`, and `AC-006`.

Notes:

1. The rule must not require snapshots for every substantial work item; it should require them when meaningful architectural decisions are made or depended on.

### `REQ-003` Specs and architecture snapshots own architectural decisions before implementation

Rationale:

1. Plans should use and reference architecture decisions. They should not silently become the place where architectural tradeoffs are invented.

Acceptance links:

1. Covered by `AC-003`, `AC-004`, and `AC-005`.

Notes:

1. Before freeze, missing architecture is fixed by editing the draft spec or architecture snapshot. After freeze, high-impact architecture drift uses variance and amendment rules.

### `REQ-004` Plans and phase plans reference architecture instead of reinterpreting it

Rationale:

1. Plans are implementation sequencing artifacts. They need enough architecture context to execute safely, but architecture decisions belong upstream.

Acceptance links:

1. Covered by `AC-004`, `AC-005`, and `AC-007`.

### `REQ-005` A reusable work-item architecture snapshot template exists

Rationale:

1. Without a template, agents may continue to create inconsistent snapshots or mark architecture snapshots not applicable because the expected shape is unclear.

Acceptance links:

1. Covered by `AC-003`, `AC-006`, and `AC-008`.

### `REQ-006` Durable repository-level architecture documents remain future work

Rationale:

1. The harness is not ready to manage long-lived durable documents such as `ARCHITECTURE.md`; forcing that now would expand scope and create lifecycle gaps.

Acceptance links:

1. Covered by `AC-002`, `AC-006`, and `AC-009`.

### `REQ-007` Current harness validation and generated-template freshness continue to pass

Rationale:

1. This change touches current harness entrypoints, references, templates, docs, and validation surfaces.

Acceptance links:

1. Covered by `AC-008`, `AC-010`, and `AC-011`.

### `REQ-008` Changelog and commit planning stay synchronized

Rationale:

1. Harness planning and implementation commits must keep planned subjects and changelog snippets aligned.

Acceptance links:

1. Covered by `AC-011`.

## Acceptance Criteria

An acceptance criterion defines observable verification: how a reviewer, command, manual check, test, or operator acceptance can tell that a requirement has been satisfied.

### `AC-001` Lifecycle owns a work-item architecture decision rule

Verifies:

1. `REQ-001` and `REQ-002`.

Method:

1. Review `.agents/skills/dev-doc-harness/references/artifact-contract.md` after implementation and confirm it defines when architecture decisions belong in specs, when `snapshots/architecture.snapshot.md` is required, and how plans and amendments consume that decision record.

### `AC-002` Documentation matrix distinguishes snapshots from future durable docs

Verifies:

1. `REQ-002` and `REQ-006`.

Method:

1. Review lifecycle and template documentation-matrix rows and confirm the architecture snapshot row describes a work-item-bound frozen decision snapshot, while architecture summary deltas or `ARCHITECTURE.md` updates remain optional/future and are not required by this change.

### `AC-003` Spec templates prompt architecture decision capture

Verifies:

1. `REQ-001`, `REQ-002`, `REQ-003`, and `REQ-005`.

Method:

1. Review generated small/medium and large/phased spec templates and their source blocks for an architecture decision section that prompts agents to record drivers, constraints, chosen approach, rejected alternatives, affected boundaries, and architecture snapshot requirement status.

### `AC-004` Plan templates treat architecture as input

Verifies:

1. `REQ-003` and `REQ-004`.

Method:

1. Review generated small/medium plan and large phase-plan templates and their source blocks for architecture input/reference prompts and instructions to route missing or changed architecture back to draft specs/snapshots or post-freeze amendments.

### `AC-005` Phase planning cannot reinterpret frozen architecture silently

Verifies:

1. `REQ-003` and `REQ-004`.

Method:

1. Review lifecycle, durable-planning-quality, and phase-plan template wording to confirm phase plans derive from approved architecture decisions and must use variance/amendment handling for high-impact changes after freeze.

### `AC-006` Architecture snapshot template is work-item-bounded

Verifies:

1. `REQ-002`, `REQ-005`, and `REQ-006`.

Method:

1. Review `.agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md` and confirm it records work-item-specific decision context, drivers, constraints, selected approach, rejected alternatives, affected boundaries, validation cues, and future-durable-doc non-scope without requiring `ARCHITECTURE.md`.

### `AC-007` Router and operator guidance are discoverable

Verifies:

1. `REQ-004` and `REQ-006`.

Method:

1. Review `.agents/skills/dev-doc-harness/SKILL.md`, `README.md`, and `.agents/skills/dev-doc-harness/docs/operator-note.md` for concise guidance that work-item architecture decisions are captured in specs and snapshots, and durable repository-level architecture docs are future work.

### `AC-008` Validator covers the new current surfaces without semantic overreach

Verifies:

1. `REQ-005` and `REQ-007`.

Method:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and confirm it passes while checking for the architecture snapshot template, rule discoverability, generated-template freshness, and absence of an active `ARCHITECTURE.md` requirement.

### `AC-009` No `ARCHITECTURE.md` workflow is introduced

Verifies:

1. `REQ-006`.

Method:

1. Run targeted searches after implementation and confirm current harness guidance does not instruct agents to create or update `ARCHITECTURE.md` as part of this work-item architecture flow.

### `AC-010` Generated templates remain current

Verifies:

1. `REQ-007`.

Method:

1. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` and confirm all assembled templates are current.

### `AC-011` Changelog and commit subjects are synchronized

Verifies:

1. `REQ-007` and `REQ-008`.

Method:

1. Review `CHANGELOG.md`, planned commit rows, and git commit subjects before the planning approval and implementation commits.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: lifecycle rule for work-item architecture decisions and documentation matrix meaning.
2. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`: spec and phase-plan quality bar for preserving architecture decisions.
3. `.agents/skills/dev-doc-harness/SKILL.md`: operation router discoverability for architecture snapshots and architecture-sensitive planning.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/`: generated template source blocks for spec and plan architecture prompts.
5. `.agents/skills/dev-doc-harness/assets/templates/assemblies/`: manifests for primary generated templates if new blocks are inserted.
6. `.agents/skills/dev-doc-harness/assets/templates/*.md`: regenerated flat templates.
7. `.agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md`: new work-item snapshot template.
8. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: structural validation for new architecture-decision surfaces.
9. `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`: concise operator-facing guidance.
10. `CHANGELOG.md`: required newest-first entries before commits.

### Data, config, and persistence

1. No runtime data, persistence, or deployment configuration changes.
2. The only new static artifact template is `architecture-snapshot.md`.
3. No release identity change; use current package marker `0.4+`.

### State and control flow

1. Draft specs decide whether architecture snapshot is required, not applicable, or deferred with owner/reason.
2. If required, the architecture snapshot is drafted and frozen with the planning package before implementation.
3. Plans and phase plans reference the approved spec and architecture snapshot as inputs.
4. Missing architecture before freeze is corrected by editing drafts.
5. High-impact architecture changes after freeze require variance handling and, when applicable, an approved amendment.

### Safety, security, privacy, migration, and rollback

1. No product runtime safety, security, privacy, or migration impact.
2. Process-safety effect: architecture-sensitive work should be less likely to hide tradeoffs inside implementation plans.
3. Rollback is a normal git revert of the implementation commit; frozen historical artifacts remain unchanged.

## Risks and Rejected Alternatives

Use one block per risk, mitigation, or rejected option:

### `RISK-001` Always requiring architecture snapshots would create low-signal artifacts

Decision or mitigation:

1. Require architecture snapshots only when meaningful architectural decisions are made or depended on; otherwise the documentation matrix may mark them not applicable with a reason.

### `RISK-002` Putting architecture only in specs could bury important decisions

Decision or mitigation:

1. Specs include an architecture decision summary, while required architecture snapshots provide a dedicated decision record for work items with meaningful architecture decisions.

### `RISK-003` Plans could keep making architecture decisions implicitly

Decision or mitigation:

1. Plan templates explicitly treat architecture as input and route missing or changed architecture to draft spec/snapshot updates before freeze or amendments after freeze.

### `RISK-004` `module:architecture` naming could confuse policy architecture with work-item architecture

Decision or mitigation:

1. Keep reusable trigger rules in `module:lifecycle`, use "work-item architecture decisions" for the planning artifact concept, and keep `module:architecture` focused on policy ownership and route graph architecture.

### `RISK-005` This could accidentally introduce unsupported durable architecture docs

Decision or mitigation:

1. State in lifecycle, templates, README, and operator note that repository-level `ARCHITECTURE.md` or durable architecture docs are future work and not created by this change.

### `RISK-006` Validator checks could become too semantic

Decision or mitigation:

1. Validate discoverability, required files, generated-template freshness, and absence of active `ARCHITECTURE.md` requirements. Do not validate whether a specific future work item made the correct architectural judgment.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spike: work-item-architecture-decisions -- approve architecture-decision flow plan` | `2026-07-03_work-item-architecture-decisions -- approve architecture-decision flow plan` | Approval commit for this spec, plan, architecture snapshot, and `CHANGELOG.md`. |
| Implementation | `docs: work-item-architecture-decisions -- make architecture snapshots first-class` | `2026-07-03_work-item-architecture-decisions -- make architecture snapshots first-class` | Implementation commit for lifecycle, quality, router, template blocks, generated templates, architecture snapshot template, validator, README, operator note, and changelog updates. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required before planning approval and implementation commits; title snippets synchronized with planned subjects |
| Test cases | Snapshot | No | Not applicable | Not applicable | Targeted validation commands and harness validator cover this policy/template change |
| Testing guide delta | Living delta | No | Not applicable | Not applicable | No testing-guide workflow change expected |
| Operator manual delta | Living delta | No | Not applicable | Not applicable | README and package-local operator note are direct implementation targets |
| API reference delta | Living delta | No | Not applicable | Not applicable | No public API changes |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | This work item introduces and dogfoods work-item-bounded architecture decision capture |
| Architecture summary delta | Living delta | No | Not applicable | Not applicable | Durable repository-level architecture docs remain future work |

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Requirements are specific, relevant, bounded, and linked to acceptance criteria.
- [x] Acceptance criteria are observable, testable, and tied to requirements or scope items.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed or explicitly absent after review.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
