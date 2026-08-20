# Router and Maintenance Architecture Plan

Work ID: `2026-08-01_router-maintenance-architecture`
Short ID: `router-maintenance-architecture`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`
Execution method: `superpowers:executing-plans`
Current planning Codex task: Model/profile, reasoning, and context visibility: `not exposed`.

## Input Artifacts

1. Draft spec: `spec_router-maintenance-architecture.md`.
2. Architecture input: `snapshots/architecture.snapshot.md`.
3. Required snapshots or deltas: `snapshots/test-cases.snapshot.md`; no documentation delta is required.
4. Relevant repository files: `.agents/skills/dev-doc-harness/SKILL.md`, the former `references/policy-architecture.md`, `references/planning-freeze-gates.md`, `references/artifact-contract.md`, `references/subagent-model-policy.md`, planning-template source blocks and generated templates, `scripts/assemble_templates.py`, and `scripts/test_harness_policy.py`.
5. Unresolved implementation context to confirm before editing: None identified; the approved package must still be re-read before edits.

## Traceability approach

Local links connect `SPEC-001` to `TASK-001` and `CHECK-001`, `SPEC-002` to `TASK-002` and `CHECK-002`, `SPEC-003` to `TASK-003` and `CHECK-003`, and `SPEC-004` to `TASK-004` and `CHECK-004`. This gives deterministic coverage without a duplicated requirements matrix.

## Global Constraints

Self-containment reason: all tasks modify one coupled documentation-policy graph and must preserve these approved boundaries.

1. Keep `SKILL.md` as the only operational router; do not add a replacement route table to the maintenance reference.
2. Preserve `module:architecture` as the stable module ID while renaming its owner file to `maintenance-architecture.md`.
3. Do not load or cite `module:freeze-gate` as a required drafting input; do not weaken the distinct review/freeze route or its stop-before-implementation behavior.
4. Edit template source blocks, then regenerate generated templates with `assemble_templates.py`; do not hand-edit generated outputs.
5. Do not update historical frozen work-item artifacts solely to replace the retired filename.

## Change surfaces

1. `.agents/skills/dev-doc-harness/SKILL.md`: make lifecycle sizing and the operation router the first normal route guidance; remove the eager policy-architecture reference; make maintenance architecture reachable only from maintenance operations; clarify required versus conditional planning inputs and a separate freeze route.
2. `.agents/skills/dev-doc-harness/references/policy-architecture.md`: rename to `maintenance-architecture.md`; retain maintenance-only ownership, identifier, dependency, validation, route-budget, and lifecycle-decomposition material; remove the duplicate router and stale provenance.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/`: remove draft-time freeze-gate policy references from plan/phase-plan headers and body blocks while retaining draft artifact state fields that are owned by lifecycle and models.
4. `.agents/skills/dev-doc-harness/assets/templates/`: regenerated small/medium and phase-plan outputs from source blocks.
5. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: replace the old path, update expected canonical-file and catalog references, and add focused assertions for the single router, reduced content types, and freeze-gate deferral.
6. `docs/work-items/2026-08-01_router-maintenance-architecture/`: implementation changelog source, validation evidence, variance record only if needed, and reviewer report if an independent reviewer is authorized later.

## Implementation approach

First write failing structural assertions that express the new loading boundary. Then move and simplify the maintenance reference, update the entrypoint router and source template metadata, regenerate templates, and run focused plus full validation. Keep freeze mechanics untouched in their owner; only remove early references that cause eager loading.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: one bounded independent final reviewer after implementation validation.
2. Fit reason: the router, reference, templates, and validator assertions form one tightly coupled ownership migration, so concurrent implementation would create conflicts; an independent final review of the integrated diff is useful to catch stale route, template, or validator ownership after deterministic checks pass.
3. Authorization state: Approved by the operator on 2026-08-01 for the reviewer below.

Sub-agent `independent-final-policy-reviewer`:

1. Purpose: review the completed implementation against `SPEC-001` through `SPEC-004`, focusing on router duplication, maintenance-reference scope, freeze-gate deferral, stale old-path references, generated-template alignment, and validator weakening.
2. Context strategy: curated artifacts.
3. Input context: frozen spec and plan, architecture and test-case snapshots, changed-file diff, `CHECK-002` through `CHECK-004` results, and implementation changelog source.
4. Output artifact: evidence-backed findings with severity, validation path, residual risk, and recommendation; the execution controller records the result in `review/independent-implementation-review.md`.
5. Model policy: `economy-default` from repository `AGENTS.md`, with the operator-approved review escalation.
6. Model generation: not exposed.
7. Capability tier: flagship.
8. Resolved profile: Sol.
9. Availability/fallback: use Sol at high reasoning; if unavailable, disclose the assurance gap and obtain a fresh operator decision before substituting a different reviewer allocation.
10. Reasoning effort: high, as explicitly selected by the operator for final cross-surface review.
11. Selection reason: final review requires reasoning across coupled current policy, generated templates, and structural validation rather than a single-file check.
12. Parallel execution: No; start after the implementation diff and required checks are complete.
13. Blast radius if wrong: Medium; missed policy-route drift can impair future harness operation without affecting runtime data.
14. Write authority: None; the reviewer returns findings to the execution controller.

## Implementation tasks

### `TASK-001` Specify the single-router and renamed-reference checks

Dependencies: Approved combined planning package and fresh operator authorization.

Interfaces:

1. Consumes: `SPEC-001`, `SPEC-002`, `snapshots/test-cases.snapshot.md`, current router, former architecture reference, and current validator assertions.
2. Produces: focused failing or updated structural assertions in `test_harness_policy.py` that identify the new filename, sole router location, retained content taxonomy, and removed duplicate route table.

Implementation:

1. Update the validator's canonical-reference and required-file path lists to expect `references/maintenance-architecture.md` and to reject a current dependency on `policy-architecture.md`.
2. Add focused assertions that `SKILL.md` remains the sole surface with the `## Operation router` table, `maintenance-architecture.md` has no `## Router Inputs` heading, and the maintenance file no longer contains the work-item snapshot path.
3. Add content assertions that retain Normative policy, Advisory guidance, and Example, while rejecting `Artifact schema`, `Operator-facing summary`, `Historical snapshot`, and `Reusable policy source?` in the maintenance taxonomy.
4. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and record the expected initial failure caused solely by the unreconciled old file and content.

Exit criteria: The validator encodes the approved routing and taxonomy contract and fails before documentation surfaces are migrated.

#### `CHECK-001` Structural-contract red phase

Covers: `VER-001`, `VER-002`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after `TASK-001` assertions and before moving the reference.

Expected result: The validator reports the expected missing renamed reference or obsolete router/taxonomy condition; no unrelated new failure is introduced.

Evidence record: Command output in the execution task and the final validation summary.

### `TASK-002` Move the maintenance architecture and focus its content

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: `SPEC-001`, `SPEC-002`, `DEC-001`, the former reference content, and failing validator assertions.
2. Produces: `references/maintenance-architecture.md` as the current owner of `module:architecture`, with no duplicate operational router.

Implementation:

1. Move the reference to `.agents/skills/dev-doc-harness/references/maintenance-architecture.md` without changing `module:architecture` or stable rule IDs.
2. Replace the purpose with a maintenance-only statement that describes module ownership, identifiers, dependencies, and validation constraints; remove the non-distributable Phase 01 work-item snapshot reference and the aspirational "future validation" phrasing.
3. Retain only Normative policy, Advisory guidance, and Example in Content Types; remove the unused rows and the `Reusable policy source?` column, while retaining the catalog's useful content-type classification.
4. Delete `## Router Inputs` entirely and remove the standalone release-compatibility summary if its only function duplicates the release route in `SKILL.md`; retain maintenance-only module catalog, rule-ID conventions, dependency direction, validation model, route/duplication budget, and lifecycle-decomposition sections.
5. Replace stale "next activity" wording in maintenance guidance with `next lifecycle stage` wherever this work touches that terminology.

Exit criteria: The renamed reference is self-contained for maintenance work, no longer introduces ordinary task routing, and satisfies the taxonomy/content assertions.

#### `CHECK-002` Maintenance-reference focus

Covers: `VER-001`, `VER-002`.

Method: Run focused `rg` searches for `policy-architecture.md`, `Router Inputs`, `Reusable policy source?`, the removed content types, and `docs/work-items/2026-06-05-refactor-as-code`; inspect the renamed reference and validator results.

Expected result: No current reusable harness surface retains the old path or removed content; only `SKILL.md` exposes the operation router; the maintenance reference retains its required ownership and validation material.

Evidence record: Focused search output and `test_harness_policy.py` output.

### `TASK-003` Align operational routing and defer freeze-gate loading

Dependencies: `TASK-002`.

Interfaces:

1. Consumes: `SPEC-001`, `SPEC-003`, `DEC-001`, `DEC-002`, lifecycle, quality, naming, model policy, and freeze-gate ownership boundaries.
2. Produces: a compact `SKILL.md` orientation and planning-template metadata that distinguish draft-time inputs from review/freeze inputs.

Implementation:

1. Replace the eager first-reference paragraph in `SKILL.md` with an orientation that begins with work sizing through `module:lifecycle`; keep naming, artifact style, and release owners discoverable only where their routes require them.
2. Keep `module:architecture` in the maintenance routes—template/router updates and validator or ownership maintenance—and do not cite it as a default normal-invocation dependency.
3. In normal new-spec/plan routes, make `module:naming` an explicit required input alongside lifecycle, quality, and models; describe artifact style, evidence preservation, amendments, and architecture snapshots only with their documented conditional triggers.
4. Preserve `Freeze planning packages` as a distinct route that requires `module:freeze-gate` and lifecycle; do not add gate procedures to drafting routes or repeat gate procedure in the router.
5. Remove `module:freeze-gate` and `rule:freeze.*` from draft plan and phase-plan source-block policy-reference lines and draft-time instructions; retain only artifact-state wording needed before freeze, with the gate document as the later authority for approval, commit, and pause.
6. Regenerate outputs with `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` after source-block changes.

Exit criteria: A planner can load exactly the draft-time modules needed for an executable plan, while the full gate is loaded only when a package actually reaches review or freeze.

#### `CHECK-003` Route and template deferral

Covers: `VER-003`.

Method: Inspect `SKILL.md` routes and source-block policy references; run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`; run focused searches for freeze references across drafting routes and generated plan/phase-plan templates.

Expected result: Draft planning routes and policy-reference metadata do not make the gate a required input; the freeze route remains present and gate-owned; generated templates exactly match source blocks.

Evidence record: Assembly output, focused search output, and validator output.

### `TASK-004` Complete validation and record implementation evidence

Dependencies: `TASK-003`.

Interfaces:

1. Consumes: revised router, maintenance reference, template source blocks, generated templates, validator assertions, and the frozen test-case snapshot.
2. Produces: passed validation evidence, `changelog/implementation.md`, and a scoped implementation diff ready for the planned cohesive commit.

Implementation:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and resolve every failure without loosening freeze-gate or historical-artifact protection.
2. Run `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint` after adding `changelog/implementation.md` with a newest-first entry headed `2026-08-01 refactor: router-maintenance-architecture -- isolate maintenance and freeze context` and the required metadata.
3. Run `git diff --check`, `git status --short`, and a scoped name-only diff; verify the old reference is removed, generated templates are explained by their source changes, and no frozen historical artifact changed.
4. Dispatch `independent-final-policy-reviewer` only after `CHECK-002` through `CHECK-004` pass. Give it the curated review package stated above; record its evidence-backed findings in `review/independent-implementation-review.md`, resolve every load-bearing finding, and rerun affected checks.
5. Record any equivalent non-material adjustment in `implementation-notes/variance-log.md` only if it would materially help a later reader; stop for amendment approval if the change affects gate behavior, lifecycle semantics, model policy, or current package boundaries.

Exit criteria: `VER-001` through `VER-004` have passing, recorded evidence and the implementation scope is limited to the approved surfaces.

#### `CHECK-004` Full policy and diff validation

Covers: `VER-004`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`, `git diff --check`, and review the scoped name-only diff.

Expected result: Harness validation and changelog lint exit 0, no whitespace errors are reported, and the changed paths match the approved router/reference/template/validator/changelog scope without historical rewrites.

Evidence record: Command output and the final execution summary.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: router-maintenance-architecture -- approve routing cleanup` |
| Implementation | `refactor: router-maintenance-architecture -- isolate maintenance and freeze context` |

One cohesive implementation commit is appropriate because router text, reference ownership, generated templates, and validator assertions must agree atomically.

## Validation and variance

1. `CHECK-001` is an intentional red-phase structural check; `CHECK-002` through `CHECK-004` must pass before implementation completion.
2. Equivalent wording or section ordering is permitted when it preserves the single-router, maintenance-only, and deferred-gate commitments.
3. Record a noteworthy equivalent implementation adjustment in `implementation-notes/variance-log.md` only when it helps later readers understand the evidence or ownership graph.
4. Stop for an amendment and operator approval before changing any freeze-gate behavior, lifecycle-stage meaning, model/sub-agent policy, release semantics, historical artifact, or the selected single-router architecture.

## Implementation handoff

### Next-stage recommendation

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

Method: `superpowers:executing-plans`; Run in: `new Codex task`; Plan Task reviewers: executing-plans checkpoints and the operator-approved independent final reviewer `independent-final-policy-reviewer` using Sol at high reasoning.

#### Model

Model: executor `Terra` (`balanced`, economy-default baseline) at `medium`; final reviewer `Sol` (`flagship`) at `high`.

#### Fallbacks and limits

1. Frozen package: approved spec, plan, architecture snapshot, test-case snapshot, and planning-approval changelog source.
2. Artifact rehydration: read applicable `AGENTS.md`, the active harness, the frozen package, current router/reference/template sources, and the variance stop condition before edits.
3. Fallback: use the next available execution method in the documented method cascade if Superpowers is unavailable. If Sol at high reasoning is unavailable for final review, disclose the assurance gap and obtain a fresh operator decision before any substitute reviewer allocation.
4. Variance stop condition: seek approval through an amendment for any material change named in Validation and variance.

## Readiness

- [x] Current planning task facts are separate from the Next-stage recommendation: Next lifecycle stage, Orchestration, Model, and Fallbacks and limits.
- [x] Inputs, scope, tasks, checks, documentation, and changelog source are clear.
- [x] The sole-router and deferred-gate boundaries are explicit.
- [x] The upcoming-stage sub-agent assessment records the operator-approved, read-only Sol-high final reviewer with curated context, no write authority, one review boundary, and a no-substitution fallback.
- [x] No required decision, placeholder, or ownerless deferral remains.

## Approval

- Status: Approved
- At freeze, relabel the grouped recommendation **Approved next stage** and mirror it in chat.
- Superseded by: None
