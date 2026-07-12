# User-Facing Narrative Spec

Work ID: `2026-07-12_user-facing-narrative`
Short ID: `user-facing-narrative`
Status: Approved
Harness release: `0.5+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:artifact-style`, `module:models`, `module:freeze-gate`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

Artifact style baseline: this operator-facing documentation work loads `module:artifact-style`. Final text must be concise, scannable, free of drafting scaffolds, and explicit about audience and decision boundaries.

## Goal

Make the repository's three top-level user-facing documents explain the mature harness clearly and concisely: which problems it solves, how little operators normally need to do, how its lifecycle works, and where maintainers find deeper policy and tooling.

## Source and Intent

Source input:

1. The operator requested a review of `README.md`, `.agents/skills/dev-doc-harness/docs/operator-note.md`, and root `AGENTS.md` after the post-`0.5.0` changes.
2. The review found one lifecycle-diagram error, one stale release-flow summary, delayed problem framing, a missing adoption rationale in the package-local operator note, and inefficient README audience progression.
3. The operator approved a substantial restructure targeting roughly 25% less README text while preserving the main lifecycle diagram and all mature harness capabilities.
4. The operator clarified that usage guidance must emphasize the normal experience: ask for the desired work, converse as needed, then approve planning or execution at the harness checkpoints. Command-like prompts should remain only when they express a useful exception or explicit checkpoint.

Desired operator/user outcome:

1. A prospective adopter can quickly understand why the harness exists, how to adopt it, and that normal requests require no harness-specific incantation.
2. An operator can follow the lifecycle diagram without being sent from a large/phased anchor-spec freeze directly to implementation.
3. A downstream adopter who receives only the distributable package can understand the harness's value from `docs/operator-note.md`.
4. An agent following root `AGENTS.md` receives an accurate summary of the protected post-release synchronization flow.

Success summary:

1. The README leads with problems and outcomes, preserves a corrected lifecycle diagram, presents adoption and ordinary use before maintainer internals, and removes duplicated explanations.
2. The operator note adds a compact rationale and distinguishes normal operator use from harness maintenance.
3. Root `AGENTS.md` describes the post-release protected-PR transition accurately without expanding into a duplicate runbook.

## Scope Boundary

### In scope

1. Restructure and tighten `README.md`, targeting approximately 20-30% fewer words while preserving all operator-relevant capabilities.
2. Keep and correct the main Mermaid lifecycle diagram so combined small/medium work and large/phased work reach implementation through their actual freeze boundaries.
3. Add early, explicit problem framing for lost chat context, premature execution, ambiguous conformance, silent drift, unreliable handoffs and orchestration, changelog merge contention, and duplicate compatibility artifacts.
4. Make “ask for the work normally” the primary usage guidance; keep only examples that communicate a useful exception, stop condition, or review checkpoint.
5. Add the missing adoption rationale to `.agents/skills/dev-doc-harness/docs/operator-note.md` and label maintainer-only tooling clearly.
6. Replace the stale “post-release `master` reset” wording in root `AGENTS.md` with a concise protected-PR synchronization summary.
7. Preserve canonical-owner links, distribution boundaries, Superpowers/spec-kit compatibility, and the current `SPEC` / `DEC` / `VER` / `TASK` / `CHECK` model.

### Non-scope

1. Do not change canonical lifecycle, freeze, conformance, model, release, changelog, or compatibility policy.
2. Do not change templates, assembly manifests, scripts, validator behavior, release notes, or the release runbook.
3. Do not create or seed `docs/superpowers`; this repository has no qualifying historical package continuity at that path.
4. Do not add installation automation, new operator commands, new workflow states, or new diagrams beyond the corrected main lifecycle diagram.
5. Do not rewrite historical work-item artifacts.

### Assumptions

1. The current canonical references and passing harness validator are the factual baseline.
2. A 20-30% README reduction is a target, not permission to omit a mature operator-facing capability.
3. The README may serve prospective adopters, active operators, and maintainers when those audiences are ordered through progressive disclosure.
4. Root `AGENTS.md` remains terse and agent-facing; it should not gain the problem narrative intended for human-facing orientation docs.

### Open questions

1. None identified after operator approval of the rewrite depth, retained diagram, and ordinary-use principle.

## Repository Context

### Current state

1. `README.md` contains accurate mature policy summaries but repeats its introduction, presents mechanisms before operator problems, places adoption after internal routing and maintenance details, and duplicates compatibility and policy inventories.
2. Its Mermaid diagram merges the large/phased anchor-spec route with the combined small/medium plan route and then goes directly to implementation after the first freeze.
3. The README prose below the diagram correctly says a large/phased anchor freezes before later phase-plan drafting.
4. `.agents/skills/dev-doc-harness/docs/operator-note.md` begins with package-copy instructions and has no concise statement of the problems solved for downstream adopters who do not receive the README.
5. Root `AGENTS.md` calls the protected post-release flow a `master` reset even though `docs/release-branch-process.md` requires a topic branch, protected PR, and post-merge remote verification.
6. `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` passes before this work.

### Evidence read

1. `README.md`.
2. `.agents/skills/dev-doc-harness/docs/operator-note.md`.
3. `AGENTS.md`.
4. `docs/release-branch-process.md`.
5. `.agents/skills/dev-doc-harness/SKILL.md`.
6. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
7. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`.
8. `.agents/skills/dev-doc-harness/references/artifact-style.md`.
9. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.
10. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
11. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`.
12. `.agents/skills/dev-doc-harness/references/release-policy.md`.
13. All eight specifications added after `origin/release/0.5`: Superpowers compatibility, changelog fragment consolidation, plan task blocks, commitment-verification, model-selection dimensions, protected post-release synchronization, visible new-task handoffs, and Superpowers stub continuity.

### Constraints and compatibility

1. The distributable package remains root `AGENTS.md` plus `.agents/`; the package-local operator note must stand alone without the repository README.
2. README and operator-note summaries consume canonical policy and must not become competing policy owners.
3. Superpowers compatibility permits pointer stubs only when historical packages already predate the current work; that condition is not satisfied here.
4. The active repository model policy remains `economy-default`.
5. The corrected diagram must show that the actual frozen package determines the next activity before continuity routes same-task or new-task execution.
6. Normal operator use must not be presented as a command language or require memorized harness-specific prompts.

## Specification Commitments and Local Verification Criteria

### `SPEC-001` Specification Commitment — foreground problems and ordinary use

Kind: `Outcome`

Intent: `Change`

Concerns: `Documentation`, `Adoption`, `Operator experience`

Statement:

1. `README.md` must open with one concise positioning statement followed by an early explanation of the concrete problems the harness solves and the operator outcomes it provides.
2. The primary usage instruction must say that operators ask for work normally and use ordinary conversation to refine it; the harness and agent classify, plan, and route the work without a required command vocabulary.
3. Usage examples must be retained only when they communicate a useful exception, explicit stop condition, review checkpoint, or plan-only PR request that ordinary phrasing would not make obvious.

Rationale:

1. The harness is designed to reduce process micromanagement, so its documentation should not make adoption look like learning another command interface.

#### `VER-001` Verification Criterion — value and normal use are immediately clear

Covers:

1. `SPEC-001`.

Criterion:

1. A reader can identify the harness's main problems and understand that ordinary work requests are sufficient before encountering canonical module inventories or maintainer tooling.

Expected evidence:

1. Manual review of the README opening and usage section.
2. Focused search confirming that retained prompt examples describe only exceptions or checkpoints.

### `SPEC-002` Specification Commitment — preserve and correct the lifecycle diagram

Kind: `Deliverable`

Intent: `Change`

Concerns: `Lifecycle`, `Diagram`, `Approval boundary`

Statement:

1. The main Mermaid lifecycle diagram must remain in `README.md`.
2. It must show combined small/medium spec-and-plan freeze leading to implementation, and large/phased anchor-spec freeze leading first to phase-plan drafting and a later phase-plan freeze before implementation.
3. At every frozen boundary, the diagram must preserve operator approval, pause, documented next activity, and approved continuity routing without implying automatic implementation or task creation.

Rationale:

1. The diagram is the fastest overview of the harness, but an incorrect large/phased path teaches a lifecycle violation.

#### `VER-002` Verification Criterion — diagram routes both planning shapes correctly

Covers:

1. `SPEC-002`.

Criterion:

1. The rendered diagram contains no route from a large/phased anchor-spec freeze directly to implementation and visibly includes the later phase-plan freeze.

Expected evidence:

1. Mermaid source inspection and manual path tracing for very-small, combined small/medium, and large/phased cases.

### `SPEC-003` Specification Commitment — apply progressive disclosure to the README

Kind: `Quality`

Intent: `Change`

Concerns: `Readability`, `Audience`, `Maintenance`

Statement:

1. `README.md` must present content in this order: positioning and problems, lifecycle overview, adoption and ordinary use, core operator contracts, compatibility, maintainer internals, limitations, and contributing guidance.
2. Duplicate introductions, the Scrum analogy, repeated Superpowers explanations, repeated canonical-owner inventories, and redundant override caveats must be removed or consolidated.
3. The final README should contain approximately 20-30% fewer words than the pre-edit baseline while retaining the mature operator-facing scope.
4. Canonical policy details that an operator does not need for orientation must be linked or moved to a clearly labeled maintainer section rather than repeated.

Rationale:

1. Progressive disclosure lets the README serve multiple audiences without forcing adopters through policy internals before they know how to start.

#### `VER-003` Verification Criterion — README is materially shorter and easier to navigate

Covers:

1. `SPEC-003`.

Criterion:

1. The final section order matches the stated progression, repeated explanations are absent, and the word-count reduction is within or reasonably close to the target without losing an in-scope capability.

Expected evidence:

1. Before/after word counts, heading inventory, and final diff review.

### `SPEC-004` Specification Commitment — make the package note self-explanatory

Kind: `Outcome`

Intent: `Change`

Concerns: `Distribution`, `Adoption`, `Audience`

Statement:

1. `.agents/skills/dev-doc-harness/docs/operator-note.md` must explain in a compact opening why an operator would adopt the harness before listing package-copy steps.
2. It must preserve the ordinary-use principle, combined and phased planning shapes, conformance distinction, freeze and handoff behavior, variance, changelog fragments, and compatibility.
3. Validator and template-assembly instructions must be labeled as harness-maintainer guidance rather than ordinary operator prerequisites.

Rationale:

1. The operator note travels without the repository README and must provide enough context to justify and correctly use the copied package.

#### `VER-004` Verification Criterion — downstream note works without the README

Covers:

1. `SPEC-004`.

Criterion:

1. A downstream reader can state why the harness is useful, what they copy, how they normally interact with it, and which final section is only for maintainers.

Expected evidence:

1. Manual standalone review of the operator note.

### `SPEC-005` Specification Commitment — summarize protected release synchronization accurately

Kind: `Constraint`

Intent: `Change`

Concerns: `Release`, `Safety`, `Agent instructions`

Statement:

1. Root `AGENTS.md` must replace “post-release `master` reset” with a concise summary that names the protected post-release PR synchronization and remote verification before later development branches.
2. The summary must continue routing exact commands and failure handling to `docs/release-branch-process.md` rather than duplicating the runbook.

Rationale:

1. Agent-facing bootstrap text must not suggest the obsolete direct-`master` transition.

#### `VER-005` Verification Criterion — AGENTS summary matches the runbook

Covers:

1. `SPEC-005`.

Criterion:

1. Root instructions contain no “post-release `master` reset” wording and accurately name the protected PR plus post-merge verification boundary.

Expected evidence:

1. Focused text search and comparison with `docs/release-branch-process.md`.

### `SPEC-006` Specification Commitment — preserve mature scope and policy ownership

Kind: `Constraint`

Intent: `Preserve`

Concerns: `Compatibility`, `Policy ownership`, `Regression`

Statement:

1. The rewrite must preserve discoverable operator guidance for work sizing, planning shapes, Specification Commitments and Verification Criteria, Plan Checks and evidence, architecture snapshots, freeze gates, execution continuity, model and orchestration strategy, variance and amendments, changelog fragments, package adoption, and Superpowers/spec-kit compatibility.
2. The rewrite must not introduce a rule that conflicts with a canonical owner or create a second durable source of truth.
3. `docs/superpowers` must not be created or seeded by this work.

Rationale:

1. Concision is valuable only if the README still represents the harness's mature control and evidence scope truthfully.

#### `VER-006` Verification Criterion — concise surfaces remain policy-consistent

Covers:

1. `SPEC-006`.

Criterion:

1. All listed operator capabilities remain discoverable, current compatibility restrictions remain intact, no `docs/superpowers` file exists, and the full harness validator passes.

Expected evidence:

1. Capability checklist review, focused compatibility search, worktree inspection, and validator output.

## Cross-cutting Verification Criteria

### `VER-007` Verification Criterion — the three documents tell one audience-aware story

Covers:

1. `SPEC-001`.
2. `SPEC-003`.
3. `SPEC-004`.
4. `SPEC-005`.
5. `SPEC-006`.

Criterion:

1. README serves human orientation and adoption, the package note stands alone for downstream operators, and root `AGENTS.md` remains terse executable agent guidance, with no contradiction among their shared lifecycle, compatibility, changelog, or release statements.

Expected evidence:

1. Side-by-side final review and passing structural validation.

## Architecture Decisions

Architecture snapshot status:

1. `Not applicable`: this work changes presentation and information hierarchy only. It does not change canonical policy ownership, workflow states, interfaces, data, tooling, or release architecture.

Decision summary:

1. Drivers: clearer problem framing, lower onboarding cost, correct lifecycle visualization, and reduced narrative drift.
2. Constraints: preserve the mature scope, main diagram, package boundary, canonical owners, and ordinary-use principle.
3. Selected approach: substantial restructure with progressive disclosure and approximately 20-30% README word reduction.
4. Affected boundaries: repository README, package-local operator note, and root agent bootstrap instructions.
5. Rejected alternatives: targeted line fixes would leave the narrative drift; a from-scratch rewrite risks scope loss; retaining all detail would not improve concision.
6. Validation cues: `VER-001` through `VER-007`, word count, manual diagram tracing, focused search, and full harness validation.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Human-facing repository orientation in `README.md`.
2. Package-local downstream orientation in `.agents/skills/dev-doc-harness/docs/operator-note.md`.
3. Agent-facing release-flow summary in root `AGENTS.md`.

### Data, config, and persistence

1. None. No release marker, configuration, generated artifact, schema, or persisted data changes.

### State and control flow

1. The documented lifecycle diagram changes from one incorrectly merged post-freeze path to explicit combined small/medium and large/phased paths.
2. No actual harness state transition or control-flow rule changes.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, compliance, or data migration impact.
2. The release-flow wording must preserve branch-protection safety and must not imply a direct `master` push.
3. Rollback is a normal revert of the documentation implementation commit.

## Risks and Rejected Alternatives

### `RISK-001` Concision removes an important mature capability

Decision or mitigation:

1. Use `SPEC-006` as a capability-preservation checklist and verify every listed surface before commit.

### `RISK-002` Corrected diagram becomes visually dense

Decision or mitigation:

1. Keep one main diagram, use a shared freeze/continuity subflow where readable, and test all lifecycle paths manually instead of adding secondary diagrams.

### `RISK-003` README still feels like a command interface

Decision or mitigation:

1. Lead usage guidance with ordinary conversational requests and keep examples only for non-default constraints or checkpoints.

### `RISK-004` Human summaries become new policy owners

Decision or mitigation:

1. Keep exact reusable rules in canonical references, retain one clear override statement, and link rather than duplicate internal details.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `plan: user-facing-narrative -- approve concise operator story` | `2026-07-12_user-facing-narrative -- approve concise operator story` | Approval commit for this combined spec and plan plus its changelog source fragment. |
| Implementation | `docs: user-facing-narrative -- streamline operator guidance` | `2026-07-12_user-facing-narrative -- streamline operator guidance` | README, package operator note, root AGENTS summary, and implementation changelog fragment. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `docs/work-items/2026-07-12_user-facing-narrative/changelog/*.md` | Create the matching fragment only at planning approval and implementation checkpoints. |
| Root changelog consolidation | Living | No | Operator-owned checkpoint | `CHANGELOG.md` | This work does not consolidate the root publication view. |
| Test cases | Snapshot | No | Not applicable | None | Verification Criteria and explicit Plan Checks cover the documentation behavior. |
| Testing guide delta | Living delta | No | Not applicable | None | Existing validator workflow is unchanged. |
| Operator manual delta | Living delta | No | Not applicable | None | The operator-facing documents are edited directly. |
| API reference delta | Living delta | No | Not applicable | None | No API change. |
| Architecture snapshot | Snapshot | No | Not applicable | None | No architecture decision beyond documentation presentation. |
| Architecture summary delta | Living delta | No | Not applicable | None | No repository architecture summary change. |

## Next-task handoff

1. Planning shape: `combined small/medium`.
2. Frozen package: `spec_user-facing-narrative.md` and `plan_user-facing-narrative.md`.
3. Next activity: implement the approved narrative changes beginning with `TASK-001`.
4. Execution continuity: `same task`.
5. Context visibility: `not exposed`.
6. Artifact rehydration required: `Yes; reread the frozen package and current target documents after the fresh post-freeze start instruction.`
7. Exact authoritative artifacts: this spec and `plan_user-facing-narrative.md`.
8. Approved strategy and fallback: `## Model and Sub-agent Strategy` in the plan.
9. First activity: `TASK-001`.
10. Variance stop condition: approval is required for changes to canonical policy, templates, scripts, release behavior, package boundaries, committed scope, Verification Criteria, or Plan Checks.

The combined small/medium spec does not emit an independent plan-drafting handoff. Its plan owns the post-freeze implementation transition.

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Specification Commitments are atomic, classified, bounded, and contain every implementation obligation in their Statements.
- [x] Verification Criteria have valid Covers sets, expected evidence, deterministic local/cross-cutting placement, and no hidden procedure or scope.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: None
