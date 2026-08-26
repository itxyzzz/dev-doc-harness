# Route Name Simplification Plan

Work ID: `2026-08-21_route-name-simplification`
Short ID: `route-name-simplification`
Status: Approved
Harness release: `0.9+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`
Execution method: `superpowers:subagent-driven-development`

## Input Artifacts

1. Draft spec: `spec_route-name-simplification.md`.
2. Architecture input: the Not applicable decision in the draft spec; no architecture snapshot is required.
3. Required snapshots or deltas: `snapshots/test-cases.snapshot.md`.
4. Relevant repository files: `README.md`, `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, active references, template manifests and blocks, generated templates, `scripts/assemble_templates.py`, and `scripts/test_harness_policy.py`.
5. Unresolved implementation context to confirm before editing: none; the ordered cutover and no-alias boundary are approved in the draft spec.

## Traceability approach

The task/check mapping below provides deterministic coverage: `TASK-001` and `CHECK-001` cover `VER-001` and the medium half of `VER-002`; `TASK-002` and `CHECK-002` cover the small half of `VER-002`; `TASK-003` and `CHECK-003` through `CHECK-006` cover `VER-001`, `VER-003`, and `VER-004`.

Mapping benefit: deterministic validation.

## Global Constraints

Self-containment reason: every task must preserve the approved nomenclature boundary without relying on prior chat context.

1. Perform the ordered cutover exactly once: `small/medium` and `small-medium` become `medium` before `lean/small` and `lean-small` become `small`.
2. Do not create aliases, dual schemas, compatibility copies, or old-name normalization.
3. Do not rename `large/phased` or `large-phased`.
4. Do not rewrite frozen work items, existing changelog history, or release notes.
5. Regenerate templates only through `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`.

## Change surfaces

1. `README.md`, `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, and `.agents/skills/dev-doc-harness/docs/operator-note.md`: replace active route labels while preserving large/phased behavior.
2. `.agents/skills/dev-doc-harness/references/{artifact-contract.md,artifact-style.md,context-and-quality-gates.md,maintenance-architecture.md,planning-freeze-gates.md,subagent-model-policy.md}`: replace every active route-owned label and identifier while retaining the large/phased route.
3. `.agents/skills/dev-doc-harness/assets/templates/{assemblies,blocks}/`: rename former-medium namespaces to `medium` before former-small namespaces receive `small`.
4. `.agents/skills/dev-doc-harness/assets/templates/`: rename generated template paths and refresh their content from the renamed manifests and blocks.
5. `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`: change the explicit assembly registry to the four renamed small/medium paths while retaining the two large-phased paths.
6. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: align route maps, permitted block scopes, schemas, paths, fixture/scenario identifiers, and negative assertions with the new canonical names.
7. `snapshots/test-cases.snapshot.md`: record the ordered migration and active-surface validation cases.

## Implementation approach

The first task frees `small` by moving every former small/medium identity to `medium`, including generated-source ownership and validator expectations. The second task assigns the freed namespace to the former lean route. The final task regenerates and validates the complete active harness, confirms preserved-history boundaries, and records implementation evidence before the cohesive commit.

## Implementation tasks

### `TASK-001` Rename the former medium route

Dependencies: Approved combined planning package and fresh execution authorization.

Interfaces:

1. Consumes: `SPEC-001`, `SPEC-002`, active former-medium paths named `small-medium-*`, and former-medium source blocks named `.small.`.
2. Produces: A collision-free `medium` namespace for the former small/medium route, leaving `small` available for `TASK-002`.

Implementation:

1. Rename `small-medium-work-item-spec.md`, `small-medium-work-item-plan.md`, and their assembly JSON files to `medium-work-item-spec.md` and `medium-work-item-plan.md`; change each manifest `output` path to its renamed generated template.
2. Rename every former-medium source block currently named `.small.` to `.medium.`, then update the two renamed assembly manifests to reference those block paths.
3. Replace active former-medium operator language (`small/medium`, `combined small/medium`, and route-specific uses) with `medium` or `combined medium` in `README.md`, `AGENTS.md`, `SKILL.md`, `docs/operator-note.md`, and every in-scope reference file: `artifact-contract.md`, `artifact-style.md`, `context-and-quality-gates.md`, `maintenance-architecture.md`, `planning-freeze-gates.md`, and `subagent-model-policy.md`. Preserve all `large/phased` wording.
4. Update the assembler registry, schema literals (`schema:spec.medium` and `schema:plan.medium`), validator route maps, active path assertions, permitted block scopes, and former-medium test descriptions so they identify the renamed route only as `medium`.
5. Regenerate the templates through the assembler after manifest and block changes.

Exit criteria: No former-medium active path, schema, manifest output, source block, generated template, or validator assertion retains the `small-medium` or former-medium `.small.` namespace.

#### `CHECK-001` Medium namespace is complete before small is assigned

Covers: `VER-001`, `VER-002`.

Method: Run the assembler freshness check and targeted searches for `small-medium`, `schema:*.small-medium`, and former-medium `.small.` block references across active harness surfaces before beginning `TASK-002`.

Expected result: The assembler reports current outputs; targeted searches return no former-medium route-owned occurrences; no former-small file or block has yet been renamed to `small`.

Evidence record: Implementation evidence for `VER-001` and `VER-002` in this work item's required implementation-changelog source, created under `module:implementation-changelog` immediately before the implementation commit.

### `TASK-002` Rename the former lean route

Dependencies: `TASK-001` and `CHECK-001` must complete successfully.

Interfaces:

1. Consumes: The now-unambiguous `medium` namespace, former-small paths named `lean-small-*`, and former-small source blocks named `.lean.`.
2. Produces: The canonical `small` namespace for the former lean/small route.

Implementation:

1. Rename `lean-small-work-item-spec.md`, `lean-small-work-item-plan.md`, and their assembly JSON files to `small-work-item-spec.md` and `small-work-item-plan.md`; set manifest outputs to those renamed template paths.
2. Rename former-small `.lean.` source blocks to `.small.`, then update the renamed manifests and generated-template headers to use `schema:spec.small` and `schema:plan.small`.
3. Replace active former-small operator language (`lean/small`, `lean-small`, route-specific `lean`, and `combined lean/small`) with `small`, `small-*`, and `combined small` in `README.md`, `AGENTS.md`, `SKILL.md`, `docs/operator-note.md`, and every in-scope reference file: `artifact-contract.md`, `artifact-style.md`, `context-and-quality-gates.md`, `maintenance-architecture.md`, `planning-freeze-gates.md`, and `subagent-model-policy.md`. Retain generic non-route uses of `lean` only when they do not denote this route.
4. Update the assembler registry, validator route maps, schema assertions, permitted block scopes, active-template paths, fixture path references, and route-specific scenario IDs to use the canonical `small` namespace and reject the obsolete one.
5. Regenerate templates through the assembler after all former-small manifests and blocks are aligned.

Exit criteria: The former lean route has only the `small` route name and `small-*` machine namespace; the `medium` route remains untouched by this task; no active route label uses `lean/small` or `lean-small`.

#### `CHECK-002` Small namespace is complete after medium cutover

Covers: `VER-001`, `VER-002`.

Method: Run the assembler freshness check and targeted searches for `lean/small`, `lean-small`, `schema:*.lean-small`, and `.lean.` source blocks across active harness surfaces.

Expected result: The assembler reports current outputs; targeted searches return no former-small route-owned occurrence; `small` occurs only for the former small route and `medium` only for the former medium route.

Evidence record: Implementation evidence for `VER-001` and `VER-002` in this work item's required implementation-changelog source.

### `TASK-003` Verify the active cutover and historical boundary

Dependencies: `TASK-001`, `CHECK-001`, `TASK-002`, and `CHECK-002`.

Interfaces:

1. Consumes: The two completed rename passes, regenerated templates, and updated validator.
2. Produces: Reproducible migration evidence and a cohesive implementation-ready diff.

Implementation:

1. Add `snapshots/test-cases.snapshot.md` with the ordered medium-first/small-second migration cases, schema/path checks, large/phased preservation check, and frozen-history boundary check.
2. Run the active harness policy validator and template freshness check.
3. Run focused content and filename searches that exclude immutable work-item history and release notes; verify old route identifiers are absent and active `large/phased`/`large-phased` occurrences remain.
4. Inspect the scoped diff to confirm that only active harness surfaces, regenerated templates, this work item's evidence, and the required implementation-changelog source changed. Do not modify existing root changelog entries or release notes.
5. Immediately before the implementation commit, load `module:implementation-changelog` and create or update the required source in this work item with the executed checks and their results.

Exit criteria: All automated checks pass, active-name searches are clean, large/phased is preserved, historical files are untouched, and implementation evidence is recorded.

#### `CHECK-003` Generated templates are current

Covers: `VER-002`, `VER-003`.

Method: `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.

Expected result: `All assembled templates are current.`

Evidence record: Implementation-changelog source for this work item.

#### `CHECK-004` Policy contracts pass

Covers: `VER-003`.

Method: `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: The script exits with code `0` and reports its complete policy-validation success summary.

Evidence record: Implementation-changelog source for this work item.

#### `CHECK-005` Active obsolete names are absent

Covers: `VER-001`, `VER-003`.

Method: Run focused `rg` content searches and `rg --files` filename searches against `README.md`, `AGENTS.md`, and `.agents/skills/dev-doc-harness`, excluding `docs/releases/**`, for `lean/small`, `small/medium`, `lean-small`, `small-medium`, `schema:spec.lean-small`, `schema:plan.lean-small`, `schema:spec.small-medium`, and `schema:plan.small-medium`.

Expected result: No active canonical surface matches an obsolete route label, identifier, template name, or schema key.

Evidence record: Implementation-changelog source for this work item.

#### `CHECK-006` Historical and large-route boundaries hold

Covers: `VER-004`.

Method: Review `git diff --check`, `git diff --name-only`, and focused `rg` output for `large/phased` and `large-phased` in active harness paths.

Expected result: No whitespace errors; no edits to existing frozen work items, historical root changelog entries, or release notes; active large/phased terminology remains present and unchanged.

Evidence record: Implementation-changelog source for this work item.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: Bounded sequential executor/reviewer strategy.
2. Fit reason: The required order and shared validator state make concurrent write-capable workers unsafe, while isolated task review reduces the risk of stale namespace references between the two rename passes.
3. Authorization state: Pending operator approval as part of this planning package; the earlier authorization covered the completed read-only audits only.

Sub-agent `TASK-001/TASK-002 executor`:

1. Purpose: Execute each ordered rename task in a fresh, bounded context and report changed paths plus validation evidence.
2. Context strategy: Curated artifacts.
3. Input context: Approved spec, approved plan, the specific task, current diff, assembler, and validator.
4. Output artifact: Bounded patch and task validation report.
5. Active model policy: `economy-default`.
6. Recommended sub-agent model: Generation `latest available`; Capability tier `balanced`; Reasoning effort `medium` because the task combines a file namespace migration with validator integration.
7. Availability/fallback: If task-specific execution or reviewer tooling is unavailable, the orchestration session executes sequentially and records the unavailable-review disclosure required by `module:models`.
8. Selection reason: Fresh context avoids accidental reliance on the former route names while preserving the required order.
9. Parallel execution: No; `TASK-002` depends on a validated `TASK-001`.
10. Blast radius if wrong: Medium; stale names can make template generation or policy validation fail.
11. Write authority: Only the active paths named in the assigned plan task; no historical artifacts.
12. Concurrency: One executor at a time.

Sub-agent `task and final reviewer`:

1. Purpose: Independently inspect each completed task and the final whole-change diff for stale route ownership, order violations, and historical-file edits.
2. Context strategy: Curated artifacts.
3. Input context: Approved spec and plan, assigned task or final diff, validation output, and changed-file list.
4. Output artifact: Evidence-backed review findings with severity, reproduction or validation path, and disposition.
5. Active model policy: `economy-default`.
6. Recommended sub-agent model: Generation `latest available`; Capability tier `balanced`; Reasoning effort `high` because the review must distinguish generic wording from route-owned terminology and catch cross-file inconsistencies.
7. Availability/fallback: If independent reviewer tooling is unavailable, the orchestration session performs the focused review and records the assurance limitation.
8. Selection reason: The migration has broad textual reach but a narrow semantic boundary, making an independent stale-reference review valuable.
9. Parallel execution: No; review follows each executor task and the completed branch.
10. Blast radius if wrong: Medium; missed stale references can leave an incoherent public harness contract.
11. Write authority: Read-only.
12. Concurrency: One reviewer after each task and one final whole-change review.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `docs: route-name-simplification -- approve canonical small and medium naming` |
| Implementation | `refactor: route-name-simplification -- simplify active harness route names` |

One cohesive implementation commit is required because the active namespace must not be left half-migrated.

## Validation and variance

`CHECK-001` through `CHECK-006` are required. Any discovery of an external compatibility dependency, an unintended large/phased change, a required historical-file edit, or a need for aliases is a material variance: stop, update the draft or prepare an amendment as required by `rule:lifecycle.variance-policy`, and obtain operator approval before continuing.

## Implementation handoff

### Next-stage recommendation

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

- Method: `superpowers:subagent-driven-development`.
- Orchestration mode: `bounded delegated sub-agents`.
- Run in: `same orchestration session`.
- Review: Independent read-only reviewer after each Plan Task and an independent final whole-change reviewer.

#### Model

- Generation: `latest available`.
- Capability tier: `balanced`.
- Reasoning: `medium`.

#### Execution requirements and contingencies

Use the approved frozen spec and plan as curated artifacts; execute `TASK-001` fully before `TASK-002`; stop for any material variance; use the documented single-agent/review fallback only when task-specific agent tooling is unavailable.

### Execution startup

1. Frozen package: `spec_route-name-simplification.md`, `plan_route-name-simplification.md`, and `snapshots/test-cases.snapshot.md`.
2. Artifact rehydration: Load the frozen package and the active files named by the assigned Plan Task under `rule:execution-quality.execution-thread-start`.
3. Variance stop condition: Any compatibility alias, external dependency, large/phased wording change, historical-record edit, or deviation from medium-first sequencing requires a stop and the applicable approval route.

## Readiness

- [x] This plan is self-sufficient for a fresh executor session.
- [x] Each task has a bounded outcome, dependencies, interfaces, executable steps, and observable exit criteria.
- [x] Plan Checks cover `VER-001` through `VER-004` and identify evidence records.
- [x] Required documentation outputs are assigned to tasks.
- [x] The next-stage method, model, and sub-agent strategy are explicit.
- [x] No placeholder, unresolved implementation decision, missing owner, or ownerless deferral remains.

## Completion

- Required work and evidence are complete; any noteworthy variance is recorded.
- Planned changes are committed, or the blocker is stated.

## Approval

- Status: Approved
- Superseded by: None
