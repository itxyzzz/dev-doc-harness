# Documentation Assessment Simplification Specification

Work ID: `2026-08-04_documentation-assessment-simplification`
Short ID: `documentation-assessment-simplification`
Status: Approved
Harness release: `0.8+`
Schema: `schema:spec.small-medium`
Companion plan: `plan_documentation-assessment-simplification.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:architecture`, `rule:lifecycle.documentation-assessment`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Replace the repeated documentation artifact matrix with a compact, mandatory documentation assessment and finish isolating changelog authoring rules in the implementation-stage module.

## Source and Intent

Source input:

1. Operator review of `artifact-contract.md` and the generated planning templates found the current documentation artifact matrix long, repetitive, and often dominated by unused rows.
2. The operator approved a compact canonical consideration list, readable IDs, status bullets in specs, generic readiness checks, separate architecture-snapshot ownership, and full implementation-only changelog ownership.

Desired operator/user outcome:

1. A planning agent visibly assesses every documentation prompt without copying policy paths, timing, or explanations into every work item.
2. An executor identifies every required or deferred documentation output from the approved package, while current fragment naming, entry syntax, linting, and consolidation instructions load only at implementation or release time.

Success summary:

1. The harness has one compact policy list of five documentation prompts and self-contained spec templates with five readable status bullets.
2. Static policy validation protects the policy, template, readiness, and changelog-ownership contracts without attempting to parse or judge every historical work item.

## Scope Boundary

### In scope

1. Replace `rule:lifecycle.documentation-matrix` and its full matrix with `rule:lifecycle.documentation-assessment` in `artifact-contract.md`.
2. Keep the compact consideration list in `artifact-contract.md` with exactly `DOC-TEST-CASE`, `DOC-TEST-GUIDE`, `DOC-OPS-GUIDE`, `DOC-API-GUIDE`, and `DOC-ARCH-SUMMARY`.
3. Replace the shared spec matrix source block with a five-bullet `## Documentation assessment` template. Each bullet uses `Not required`, `Required`, or `Deferred`; required entries name a path and Plan Task, and deferred entries name an owner and resolution point.
4. Keep architecture-snapshot status exclusively in `## Architecture Decisions`; exclude it from the documentation assessment.
5. Update small and phase plan prompts and readiness checks so plans assign only required or deferred documentation work, without restating catalog triggers or a full five-item assessment.
6. Remove detailed changelog rows and planning-template wording from the assessment flow. Retain one concise implementation-commit reminder in plan prompts.
7. Move current changelog fragment paths, filename variants, and entry-heading/synchronization rules from lifecycle and naming guidance into `module:implementation-changelog`; retain generic commit-subject grammar in `module:naming`.
8. Replace current README, operator-note, quality, amendment-template, and planning-template changelog procedure with a concise implementation-stage handoff or an implementation-reference link, as appropriate to that document's audience.
9. Regenerate every affected assembled template and update static harness-policy assertions for the new policy, template body, readiness-checklist, route, and ownership boundaries.
10. Update directly affected maintenance architecture wording from documentation-matrix to documentation-assessment ownership.

### Non-scope

1. Adding a validator that parses, infers, or semantically judges documentation decisions in arbitrary created work-item specs or plans.
2. Rewriting frozen historical work-item artifacts that contain a documentation artifact matrix.
3. Changing architecture-snapshot eligibility or the Architecture Decisions template section.
4. Changing implementation changelog fragment syntax, linting behavior, root-consolidation behavior, release policy, release-branch procedure, or the existing implementation-changelog router placement.
5. Moving the five-item consideration list to a separate reference. It remains in `artifact-contract.md` unless later growth makes that file unreadable.

## Repository Context

### Current state

1. `artifact-contract.md` defines an eight-row documentation artifact matrix containing changelog, test, documentation-delta, and architecture-snapshot rows, and also ties planned commit subjects to changelog entry headings.
2. `blocks/spec.080.common.documentation-matrix.md` repeats the matrix in both assembled specification templates. Its changelog timing already differs from the contract wording.
3. `blocks/plan.080.phase.documentation-tasks.md` repeats the artifact categories and changelog timing in phase plans; small-plan readiness refers to the matrix directly.
4. `references/implementation-changelog.md` already owns detailed implementation-only changelog lifecycle and metadata rules, but `naming-conventions.md` still owns fragment path patterns, filenames, and heading grammar.
5. `README.md`, `docs/operator-note.md`, `durable-planning-quality.md`, and `plan-amendment.md` repeat current changelog actions outside the implementation module.
6. `planning-freeze-gates.md` already excludes root `CHANGELOG.md` from a plan-only checkpoint. The actual repository `AGENTS.md` has no contrary freeze-gate changelog requirement.
7. `scripts/test_harness_policy.py` validates current policy and template surfaces, including the matrix phrase in the small-plan readiness block and a changelog-fragment contract that currently expects naming and template duplication; it does not validate individually created work-item packages.

### Evidence read

1. `AGENTS.md` and `.agents/skills/dev-doc-harness/SKILL.md`.
2. Lifecycle, planning-freeze, implementation-changelog, quality, maintenance-architecture, naming, and model-policy references.
3. The small/medium spec and plan, large/phased spec and phase-plan templates; their assembly manifests; and affected source blocks.
4. `assemble_templates.py`, the focused assertions in `test_harness_policy.py`, current README/operator guidance, release policy/runbook, and the approved 2026-08-01 and 2026-08-03 related work-item packages.

### Constraints and compatibility

1. Source blocks and manifests are authoritative; generated flat templates must be regenerated by `assemble_templates.py`, never hand-edited.
2. Current template schemas and published paths remain stable; only their prose and source-block names may change.
3. The five assessment IDs are exact current-policy identifiers. The static validator may check their presence and order in policy/templates, but must not become an actual-work-item semantic validator.
4. Historical frozen artifacts remain immutable evidence and may retain the former matrix.
5. Planning and freeze routes must not load detailed changelog mechanics. The concise plan reminder points to `module:implementation-changelog` before implementation commits; the implementation and release routes retain their purpose-specific detailed guidance.

## Assumptions and Open Questions

### Assumptions

1. The existing source-block assembler can replace the shared spec block and regenerate all affected published templates without a schema or assembler change.
2. This is small/medium work: policy wording, template source blocks, generated outputs, and one static validator comprise a bounded, cohesive change.
3. Existing Impact Surfaces and Architecture Decisions remain the reviewer evidence for challenging an implausible `Not required` decision.
4. README and operator-note may retain a one-sentence description of implementation changelog behavior, but no command, schema, filename, or consolidation procedure.

### Open questions

None identified after repository-context review. The operator selected the IDs, policy location, architecture-snapshot boundary, enforcement levels, and changelog boundary.

## Commitments and verification

### `SPEC-001` Compact canonical assessment policy

Statement:

1. `rule:lifecycle.documentation-assessment` must replace the matrix rule and define one compact five-item consideration list with readable IDs and trigger-oriented descriptions.
2. The policy must define the three statuses and require each new substantial specification to assess every ID.
3. Changelog records and architecture snapshots must not be assessment entries: changelog remains implementation-stage policy and architecture snapshot status remains owned by Architecture Decisions.

#### `VER-001` Policy remains compact and complete

Covers: `SPEC-001`.

Criterion: The lifecycle reference exposes the five approved IDs once, explains assessment status semantics, and contains neither a multi-column documentation matrix nor changelog or architecture-snapshot entries in that list.

Expected evidence: Focused policy-validator assertions and direct review of the updated section.

### `SPEC-002` Readable spec assessment and proportionate plan handoff

Statement:

1. Both generated spec templates must render a five-bullet `## Documentation assessment` scaffold using the approved IDs in the approved order.
2. Template instructions must require paths and Plan Task links only for required outputs, and owners plus resolution points only for deferred outputs.
3. Small and phase plan templates must assign required or deferred documentation work without restating catalog triggers or a full five-item assessment.

#### `VER-002` Templates expose one decision record and focused execution handoff

Covers: `SPEC-002`.

Criterion: Generated specs have the same compact status-bullet scaffold; plan and phase-plan prompts refer to approved assessment outputs rather than reproducing a catalog or matrix.

Expected evidence: Assembly freshness, focused heading/text searches, and static policy-validator checks.

### `SPEC-003` Three-layer enforcement without a work-item parser

Statement:

1. Policy owns IDs, consideration prompts, statuses, and decision semantics.
2. Template bodies own the five work-item status bullets and the required/deferred detail shape.
3. Readiness checklists contain only generic completeness/task-or-deferral checks and do not list the IDs or repeat policy triggers.
4. The static policy validator must protect these three boundaries and must not add a work-item command or claim to validate semantic decisions in created packages.

#### `VER-003` Validation protects the right surfaces

Covers: `SPEC-003`.

Criterion: The harness validator detects restoration of the old matrix or missing/duplicated assessment/template/readiness contracts, while its scope remains limited to current policy and template surfaces.

Expected evidence: Targeted validator assertions and full `test_harness_policy.py` success.

### `SPEC-004` Implementation-only changelog detail

Statement:

1. `module:implementation-changelog` must own current fragment location and filename variants, entry-heading/synchronization rules, metadata schema, lint, consolidation, compatibility, and root cleanup.
2. `module:naming` retains generic commit-subject grammar but no longer defines changelog-specific paths, filenames, headings, or synchronization instructions; lifecycle no longer repeats those rules.
3. Documentation assessment, phase documentation-task, spec planned-commit, amendment, and readiness prompts must not list changelog fragments, root consolidation, paths, timing, or detailed procedures.
4. Small and phase plan prompts may retain only a concise reminder to follow `module:implementation-changelog` before implementation commits.
5. README and operator-note may retain an implementation-only audience summary and link, while release policy/runbook retain release-stage consolidation instructions. Planning freeze remains free of changelog actions.

#### `VER-004` Planning context no longer carries changelog procedure

Covers: `SPEC-004`.

Criterion: Current fragment/entry authoring rules appear only in the implementation-changelog module; planning sources contain at most the approved concise handoff; release sources retain only release-stage consolidation context; and planning freeze has no changelog action.

Expected evidence: Targeted repository searches, validator assertions, and review of generated templates.

## Cross-cutting verification

### `VER-005` Generated-template integrity

Covers: `SPEC-001`, `SPEC-002`, `SPEC-003`, `SPEC-004`.

Criterion: All assembled templates match their source blocks/manifests, current schemas and paths remain intact, and no whitespace errors are introduced.

Expected evidence: `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`, `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, and `git diff --check`.

## Architecture Decisions

Architecture snapshot status: `Not applicable` because the work simplifies the established lifecycle/template ownership model without adding a runtime, component, interface, data boundary, or architecture decision that later work must consume.

Decision summary:

1. Drivers: reduce planning noise, retain visible anti-omission prompts, make actual documentation outputs readable, and defer detailed changelog context until it is usable.
2. Constraints: preserve canonical lifecycle ownership, template assembly, frozen historical evidence, and the existing implementation-only changelog module.
3. Selected approach: keep five compact prompts in lifecycle policy; render five status bullets in specs; use generic readiness checks; relocate remaining current changelog authoring rules to the implementation module; retain only plan-level handoff and purpose-specific README/operator/release summaries; update static policy/template checks.
4. Affected boundaries: lifecycle and naming policy, implementation-changelog ownership, maintainer/operator summaries, source blocks and manifests, generated templates, and static policy validation.
5. Rejected alternatives: retain the matrix; record only required outputs with no mandatory assessment; add a new catalog file now; create a work-item semantic validator; put architecture snapshot or changelog rows back in the assessment.
6. Validation cues: `VER-001` through `VER-005`, assembly freshness, validator success, and scoped text/diff review.

## Impact Surfaces

### Interfaces

1. Maintainer authoring interface changes from a wide documentation matrix to five readable assessment bullets in generated specification templates.
2. Current schema identifiers and generated-template locations remain stable.

### Data, config, and persistence

None. The change affects Markdown policy/templates and Python static assertions only.

### State and control flow

1. Planning flow becomes policy consideration list -> spec status bullets -> plan task/deferral handoff -> generic readiness review.
2. Changelog flow becomes implementation start -> implementation-changelog reference (path, entry, lint) -> operator-owned consolidation -> release curation; it is not part of plan drafting or planning freeze.

### Safety, security, privacy, migration, and rollback

1. No product security, privacy, compliance, migration, or destructive-operation impact is expected.
2. Process risk is an overly weak or duplicated prompt; compact static contract assertions, assembly checks, and freeze review mitigate it.
3. Rollback is a cohesive revert of the implementation commit. Frozen historic packages remain untouched.

## Risks and Rejected Alternatives

### `RISK-001` Short status bullets encourage unconsidered negatives

Decision or mitigation:

1. Require all five IDs in every generated spec scaffold and retain the trigger list in canonical policy. Freeze review compares the assessment against Impact Surfaces and Architecture Decisions.

### `RISK-002` Validator expands into a second documentation framework

Decision or mitigation:

1. Limit validation to active policy/template/readiness text contracts. Do not add a parser, data file, or semantic checker for arbitrary work-item prose.

### `RISK-003` Changelog procedure leaks back into planning templates

Decision or mitigation:

1. Move current fragment and entry instructions into `implementation-changelog.md`; allow only the one plan-level pre-commit reminder plus audience-appropriate README/operator/release summaries; assert that planning sources do not regain procedural detail.

### `RISK-004` Shared source-block changes produce stale generated templates

Decision or mitigation:

1. Edit source blocks/manifests first, regenerate all affected outputs with the assembler, then run its freshness check and the policy validator.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: documentation-assessment-simplification -- approve compact documentation prompts` |
| Implementation | `docs: documentation-assessment-simplification -- simplify documentation assessment` |

One cohesive implementation commit is planned because lifecycle policy, source blocks, generated templates, and their static contract assertions must agree.

## Documentation assessment

- `DOC-TEST-CASE`: Required — `snapshots/test-cases.snapshot.md`; record the policy/template/readiness cases before implementation.
- `DOC-TEST-GUIDE`: Not required.
- `DOC-OPS-GUIDE`: Required — update `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md` with an implementation-only changelog handoff; `TASK-003`.
- `DOC-API-GUIDE`: Not required.
- `DOC-ARCH-SUMMARY`: Not required.

## Planning shape and transition ownership

1. Planning shape: `combined small/medium`.
2. Companion plan: `plan_documentation-assessment-simplification.md` is drafted and presented with this spec in the same planning turn.
3. Transition owner: `plan_documentation-assessment-simplification.md` owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Goal, source and intent, scope, constraints, architecture decisions, commitment statements, and verifications are mutually consistent.
- [x] All relevant operator input is preserved in this specification or through `module:evidence` and `rule:evidence.preservation`.
- [x] Commitment statements are atomic, bounded, and form a complete set that covers the full scope and achieves the goal; no obligation exists only in rationale or examples.
- [x] Verification criteria form a complete set that covers all Commitments and have no hidden procedure or scope.
- [x] This specification file is self-contained so a fresh session can implement the actionable plan without reconstructing original session context.
- [x] Documentation assessment has all five IDs; its required output has a path and planned task; architecture-snapshot status remains in Architecture Decisions.
- [x] No unresolved placeholders, plan-affecting decisions, missing sections, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
