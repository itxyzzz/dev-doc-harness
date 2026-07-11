# Commitment Verification Model Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` task-by-task. Dispatch only the bounded RED, GREEN/REFACTOR, and final-review roles authorized in `## Model and Sub-agent Strategy`; the orchestration thread retains all writes and integration ownership.

Work ID: `2026-07-11_commitment-verification-model`
Short ID: `commitment-verification-model`
Status: Approved
Harness release: `0.5+`
Schema: `schema:plan.small-medium`
Vocabulary profile: Proposed `SPEC` / `DEC` / `VER` / `TASK` / `CHECK` plan shape; it becomes current reusable policy only in the planned implementation commit.
Policy references: `module:architecture`, `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:artifact-style`, `module:freeze-gate`, `module:execution-quality`, `module:evidence`, `module:release`, `rule:lifecycle.variance-policy`, `rule:models.strategy-required`, `rule:models.approved-strategy-authorized`, `rule:execution-quality.execution-thread-start`, `rule:evidence.preservation`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

**Goal:** Replace ambiguous current Requirements and Acceptance Criteria layers with a readable conformance model that keeps normative commitments, architecture decisions, verification criteria, implementation tasks, plan checks, execution evidence, and lifecycle decisions distinct.

**Architecture:** Make `module:quality` the semantic owner, `module:artifact-style` the readability owner, and template source blocks the concrete schema owners. Protect the contract with behavior-first evidence and deterministic structural validation, regenerate all primary templates from source manifests, and keep frozen historical artifacts outside current-schema enforcement.

**Tech stack:** Markdown policy and templates, JSON assembly manifests, Python 3 assembler and validator, fresh-context agent behavior tests, Git.

## Global Constraints

1. Use exact full-name headings for `SPEC-NNN` Specification Commitment, `DEC-NNN` Architecture Decision, `VER-NNN` Verification Criterion, `TASK-NNN` Implementation Task, and `CHECK-NNN` Plan Check entities.
2. Keep every implementation obligation in a Specification Commitment `Statement`; Architecture Decisions may only realize or constrain mapped commitment scope.
3. Require one commitment `Kind` and one `Intent` with the frozen definitions and precedence; keep `Concerns` optional and non-normative.
4. Keep single-commitment Verification Criteria local and multi-commitment criteria exactly once in `## Cross-cutting Verification Criteria`; preserve explicit `Covers` and cross-phase ownership.
5. Make applicable criteria, expected-evidence items, and mapped checks conjunctive by default; require explicit `Any one of` alternatives with an equivalence basis.
6. Keep commitment dispositions and verification execution as separate complete mappings coordinated through task/check dependencies and stages. Do not create plan-only deferrals.
7. Give every Plan Check the frozen required fields and keep procedure identity distinct from execution-instance records.
8. Keep approval/freeze, conformance verification, and optional outcome validation or delivery acceptance semantically distinct.
9. Preserve stable unversioned `schema:*`, `module:*`, and `rule:*` anchors and the `0.5+` development marker.
10. Do not rewrite frozen historical work items or introduce `RESULT` or `EVIDENCE` ID namespaces.
11. Keep automated validation structural and deterministic; do not grade atomicity, prose meaning, or evidence sufficiency.
12. Edit primary templates only through source blocks and assembly manifests, then regenerate them with `assemble_templates.py`.
13. Run behavior tests with raw scenarios and fresh contexts; do not leak expected decompositions or reviewer conclusions.
14. Preserve unrelated operator work and stop if overlapping edits cannot be integrated within the frozen scope.
15. Produce one cohesive implementation commit because current policy, template schema, generated outputs, validator expectations, and activation boundary must change together.

## Input Artifacts

1. Approved spec: `docs/work-items/2026-07-11_commitment-verification-model/spec_commitment-verification-model.md`.
2. Approved architecture input: `docs/work-items/2026-07-11_commitment-verification-model/snapshots/architecture.snapshot.md` (`DEC-001` through `DEC-007`).
3. Required test contract: `docs/work-items/2026-07-11_commitment-verification-model/snapshots/test-cases.snapshot.md`.
4. This plan and any later `plan_amendment-*.md`.
5. Applicable `AGENTS.md`, repository harness router, canonical modules, source blocks, manifests, generated templates, validator, README, and operator note named under `## Change Surfaces`.
6. Approval state: spec package frozen by commit `3954a44`; no amendments or variance log exist at plan drafting time.
7. Expected baseline: `assemble_templates.py --check` and `test_harness_policy.py` exit `0` before implementation edits.
8. Unresolved implementation context: none. Missing runtime tier controls or sub-agent availability use the approved fallback; semantic drift uses the variance stop condition.

## Commitment-Disposition Mapping

| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` Binding statement | Implement current lifecycle semantics and prompts | `TASK-003`, `TASK-004`, `TASK-006` |
| `SPEC-002` Criterion/check/evidence separation | Implement policy, plan schema, and completion records | `TASK-003`–`TASK-006` |
| `SPEC-003` Readable stable identifiers | Implement headings and structural checks | `TASK-003`–`TASK-005` |
| `SPEC-004` Atomic explicit scope | Implement canonical perimeter guidance; verify behavior | `TASK-004`, `TASK-007` |
| `SPEC-005` Orthogonal facets | Implement definitions, precedence, prompts, and behavior tests | `TASK-004`, `TASK-005`, `TASK-007` |
| `SPEC-006` Criteria without hidden procedures | Implement canonical fields and template topology | `TASK-003`–`TASK-005`, `TASK-007` |
| `SPEC-007` Deterministic criterion placement | Implement source schema and structural fixtures | `TASK-003`, `TASK-005` |
| `SPEC-008` Asymmetric plan mapping | Implement plan source blocks, fixtures, and behavior tests | `TASK-003`, `TASK-005`, `TASK-007` |
| `SPEC-009` Plan Check execution records | Implement plan/check and completion-report contracts | `TASK-003`–`TASK-006`, `TASK-007` |
| `SPEC-010` Distinct lifecycle decisions | Align lifecycle and completion consumers | `TASK-004`, `TASK-006`, `TASK-008` |
| `SPEC-011` Current/historical boundary | Implement activation and path-scoped compatibility checks | `TASK-003`, `TASK-004`, `TASK-008` |
| `SPEC-012` Ownership and consumers | Implement owners, routes, templates, examples, and operator docs | `TASK-004`–`TASK-006` |
| `SPEC-013` Structural contract | Add RED fixtures, implement checks, and run full validation | `TASK-003`, `TASK-005`, `TASK-008` |
| `SPEC-014` Test-first skill behavior | Run preserved RED/GREEN/REFACTOR waves and final review | `TASK-002`, `TASK-007`, `TASK-008` |

Architecture Decisions are consumed only under their mapped Specification Commitments: `DEC-001`, `DEC-005`, and `DEC-006` guide `TASK-004`–`TASK-006`; `DEC-002`–`DEC-004` guide `TASK-003`–`TASK-005`; `DEC-007` guides `TASK-002`, `TASK-003`, `TASK-007`, and `TASK-008`. No decision creates an independent task scope.

## Verification-Execution Mapping

| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` Lifecycle-aware commitments | `CHECK-005`, `CHECK-009` | Consumer review; final semantic review |
| `VER-002` Layer decomposition | `CHECK-002`, `CHECK-006` | RED; GREEN/REFACTOR |
| `VER-003` Self-explaining headings | `CHECK-003`, `CHECK-004`, `CHECK-005` | Structural RED/GREEN; assembly; current-surface search |
| `VER-004` Hidden/compound scope | `CHECK-002`, `CHECK-006`, `CHECK-009` | RED; GREEN/REFACTOR; final review |
| `VER-005` Facet guidance | `CHECK-006`, `CHECK-009` | GREEN/REFACTOR; final review |
| `VER-006` Criterion boundary | `CHECK-003`, `CHECK-006`, `CHECK-009` | Structural; behavior; final review |
| `VER-007` Placement cardinality | `CHECK-003`, `CHECK-004` | Structural fixtures; assembled templates |
| `VER-008` Distinct task/check coverage | `CHECK-002`, `CHECK-003`, `CHECK-006` | RED; structural; GREEN/REFACTOR |
| `VER-009` Reproducible check records | `CHECK-003`, `CHECK-006`, `CHECK-008` | Structural; behavior; final validation |
| `VER-010` Distinct lifecycle terms | `CHECK-005`, `CHECK-009` | Cross-surface review; final semantic review |
| `VER-011` Current/historical boundary | `CHECK-001`, `CHECK-005`, `CHECK-008` | Baseline; path review; final diff |
| `VER-012` Canonical consumer contract | `CHECK-004`, `CHECK-005`, `CHECK-008` | Assembly; owner/consumer review; full validator |
| `VER-013` High-signal structural checks | `CHECK-003`, `CHECK-004`, `CHECK-008` | Focused fixtures; assembly; full validator |
| `VER-014` Corrected behavior | `CHECK-002`, `CHECK-006`, `CHECK-009` | RED; GREEN/REFACTOR; final review |
| `VER-015` Lifecycle vocabulary coherence | `CHECK-005`, `CHECK-009` | Cross-surface review; final semantic review |
| `VER-016` Self-hosting artifact completeness | `CHECK-007`, `CHECK-009` | Plan freeze review; final semantic review |
| `VER-017` Structure plus history | `CHECK-003`, `CHECK-004`, `CHECK-005`, `CHECK-008` | Fixtures; assembly; boundary review; full validator |

Every criterion has check coverage. The mappings are conjunctive unless a Plan Check explicitly records an `Any one of` alternative; this plan defines no alternative check group.

## Implementation Approach

Use two coordinated TDD loops. First preserve current fresh-context behavior as RED evidence before any guidance edit. Second add focused deterministic validator expectations and fixtures, confirm they fail only because the new contract is absent, implement the canonical semantic owners, propagate concrete schema through source blocks, regenerate outputs, and align remaining consumers. After the minimum coherent package exists, run fresh GREEN and loophole-focused REFACTOR behavior tests, then complete path-scoped compatibility, full-validator, and flagship/high semantic reviews.

The orchestration thread owns every repository write because policy owners, source blocks, generated outputs, and validator checks are tightly coupled. Sub-agents receive curated artifacts or raw scenarios and return reports only. Intermediate TDD states remain uncommitted; the implementation boundary activates in one planned commit after all checks pass.

## Change Surfaces

Canonical owners and routes:

1. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md` — add reusable Specification Commitment, Verification Criterion, Plan Check, asymmetric traceability, and conformance semantics with owned rule IDs.
2. `.agents/skills/dev-doc-harness/references/artifact-style.md` — own full-name heading readability, local/cross-cutting scanability, and trace-density guidance.
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md` — align lifecycle, documentation matrix, immutable snapshots, variance references, and completion terminology without changing approval authority.
4. `.agents/skills/dev-doc-harness/references/policy-architecture.md`, `.agents/skills/dev-doc-harness/SKILL.md` — route ownership and current/historical compatibility without duplicating canonical semantics.
5. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`, `planning-freeze-gates.md`, `evidence-and-report-artifacts.md`, `release-policy.md`, `subagent-model-policy.md`, and `subagent-role-examples.md` — consume new entity names where they refer to current artifacts, checks, evidence, completion, or examples.

Template sources and generated outputs:

1. Rename `assets/templates/blocks/spec.030.common.requirements-acceptance.md` to `spec.030.common.commitments-verification.md` and replace it with the exact commitment/local-criterion/cross-cutting-criterion shape.
2. Update `spec.035.common.architecture-decisions.md`, `spec.090.small.readiness-approval.md`, and `spec.090.large.readiness-approval.md` for mapped decisions and new readiness coverage.
3. Update `plan.020.common.traceability-approach-surfaces.md` for separate commitment-disposition and verification-execution mappings.
4. Update `plan.050.common.task-plan.md` for full-name `TASK` blocks, full Plan Check blocks, task/check dependencies, and stages.
5. Update `plan.040.common.model-strategy.md`, `plan.090.small.readiness-completion-approval.md`, and `plan.090.phase.readiness-completion-approval.md` for current terminology and execution-record completion.
6. Update all four JSON manifests for the renamed spec block; do not change output schema IDs.
7. Regenerate `small-medium-work-item-spec.md`, `large-phased-work-item-spec.md`, `small-medium-work-item-plan.md`, and `large-phased-work-item-phase-plan.md` only through `assemble_templates.py --write`.
8. Update standalone `architecture-snapshot.md`, `plan-amendment.md`, and `variance-log.md` templates as current consumers; retain `DEC`, `AMD`, and `VAR` identities.

Validation, examples, and operator surfaces:

1. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` — add current-schema path sets, positive/negative structural fixtures, heading/field/coverage/placement/mapping checks, historical exclusions, and current vocabulary assertions; update existing assembly expectations from `T`/`V` and symmetric traceability.
2. `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md` — compact Specification Package, integrated Plan, and evidence-to-conformance explanations.
3. `docs/work-items/2026-07-11_commitment-verification-model/evidence/skill-behavior-tests.md` — preserve raw and derived RED/GREEN/REFACTOR/final-review evidence.
4. `docs/work-items/2026-07-11_commitment-verification-model/changelog/implementation.md` — implementation source fragment created immediately before the implementation commit.

Stable interfaces:

1. Harness release `0.5+`, stable `schema:*` IDs, existing `module:*` retrieval anchors, freeze authorization, immutable snapshots, variance classes, source/generated workflow, package boundary, and active `economy-default` policy.

Changed interfaces:

1. Current Markdown entity headings and fields, plan traceability topology, task IDs, check records, readiness/completion prompts, validator contract, and agent/operator terminology.

Implementation boundaries:

1. Frozen work-item history, release-note files, runtime configuration, external integrations, semantic prose grading, and separate result/evidence namespaces remain out of scope.

## Model and Sub-agent Strategy

Selection dimensions:

1. Model generation: `GPT-5.6` by operator instruction for planning and intended orchestration when available.
2. Capability tier: `flagship` for implementation integration and final review; `balanced` for bounded behavior-test roles.
3. Reasoning effort: `high` for orchestration and final review; `medium` for bounded RED/GREEN roles.
4. Orchestration mode: `bounded delegated sub-agents`; one main writer owns all repository edits and integration.
5. Resolved profile: `Sol` for the operator-selected orchestration task; delegated resolved profiles are `not exposed` until runtime assignment.
6. Availability/fallback: use the selected Sol/flagship/high main thread when permitted and available. Bounded roles fall back from balanced to fast/economy for RED, or to a main-agent high-reasoning comparison for GREEN. Final review falls back to a separate orchestration-thread high-reasoning pass.
7. Execution continuity: `new task with curated-artifact handoff` after plan freeze.
8. Context visibility: `not exposed`; do not infer an exact remaining-context threshold.
9. Artifact rehydration required: `Yes`; execution rereads the frozen spec, architecture snapshot, test snapshot, and plan.
10. Model-policy source: repository `economy-default` plus the operator's 2026-07-12 `GPT-5.6 Sol High` selection.
11. Override scope and expiry: model selection applies to this planning/execution handoff; any stronger tier, higher effort, broader write delegation, platform multi-agent mode, or concurrency above two requires fresh confirmation.

Fit assessment:

1. Complexity: medium; one orchestration thread can coordinate the cohesive policy/template/validator change.
2. Risk and blast radius: high; current harness vocabulary shapes future agent scope and verification behavior.
3. Ambiguity: low after the frozen spec; semantic review remains important because structural validators intentionally do not grade meaning.
4. Budget and latency fit: bounded two-agent behavior waves provide isolation without fragmenting tightly coupled writes.

Recommended selection change:

1. None. The operator-selected Sol/flagship/high profile matches plan synthesis and integration. Platform multi-agent/`ultra` remains unsuitable for the coupled edit set.

Sub-agent `behavior-red-a` and `behavior-red-b`:

1. Purpose: independently produce uncontaminated baseline outputs for the authoring and planning scenario families.
2. Context strategy: `curated prompt`.
3. Input context: raw scenario only, current unmodified skill/template, applicable instructions, and output-format request.
4. Output artifact: read-only report returned to the orchestration thread for preservation in `evidence/skill-behavior-tests.md`.
5. Model policy: `economy-default`.
6. Model generation: `not exposed` unless runtime reports it.
7. Capability tier: `balanced`.
8. Resolved profile: `not exposed`.
9. Availability/fallback: `fast/economy` with the same raw scenario.
10. Reasoning effort: `medium`.
11. Selection reason: fresh isolation is the behavior under test; no final authority is delegated.
12. Parallel execution: Yes, cap two.
13. Blast radius if wrong: Low; contaminated or misleading output invalidates that baseline run and must be repeated.

Sub-agent `behavior-green-a` and `behavior-green-b`:

1. Purpose: forward-test revised guidance and loophole mutations without seeing RED conclusions.
2. Context strategy: `curated artifacts`.
3. Input context: revised skill/template package plus the equivalent fresh raw scenario or loophole variant.
4. Output artifact: read-only comparison input preserved in `evidence/skill-behavior-tests.md`.
5. Model policy: `economy-default`.
6. Model generation: `not exposed` unless runtime reports it.
7. Capability tier: `balanced`.
8. Resolved profile: `not exposed`.
9. Availability/fallback: main-agent comparison using the preserved raw scenario at high reasoning.
10. Reasoning effort: `medium`.
11. Selection reason: independent transfer testing exposes ambiguity that the writer may miss.
12. Parallel execution: Yes within each wave, cap two; GREEN follows implementation and REFACTOR follows GREEN.
13. Blast radius if wrong: Medium; a false pass could ship ambiguous current guidance.

Sub-agent `final-semantic-reviewer`:

1. Purpose: review completed semantic integration, topology, historical compatibility, test evidence, and residual loopholes.
2. Context strategy: `curated artifacts`.
3. Input context: frozen package, completed diff, behavior report, assembler output, validator output, and planned changelog fragment.
4. Output artifact: blocking/non-blocking findings incorporated into the evidence report and completion summary.
5. Model policy: `economy-default` escalated for high blast radius.
6. Model generation: latest available or `not exposed`.
7. Capability tier: `flagship`.
8. Resolved profile: `not exposed` until runtime assignment.
9. Availability/fallback: separate orchestration-thread review at high reasoning.
10. Reasoning effort: `high`.
11. Selection reason: a cheaper agent must not be final authority for this semantic activation boundary.
12. Parallel execution: No; runs after all validation.
13. Blast radius if wrong: High; future artifacts could inherit semantic defects.

## Implementation Tasks

### `TASK-001` Implementation Task — Rehydrate the frozen package and baseline

Dependencies:

1. Frozen package and fresh post-plan-freeze start authorization.

Implementation:

1. Apply `rule:execution-quality.execution-thread-start`: read applicable instructions, frozen spec, architecture snapshot, test snapshot, plan, amendments, and variance log before implementation targets.
2. Verify branch, worktree, approval commit, sub-agent permission, runtime availability, and all target-path diffs.
3. Run `CHECK-001`; preserve exact baseline output in the implementation completion record.
4. Stop if the baseline is failing for a pre-existing reason or if overlapping operator edits cannot be safely preserved.

Exit criteria:

1. Frozen scope and strategy are rehydrated, ownership is clear, and baseline commands pass or an operator-approved pre-existing exception exists.

### `TASK-002` Implementation Task — Preserve RED behavior evidence

Dependencies:

1. `TASK-001`; no current skill, policy, template, README, operator-note, or validator implementation edit has begun.

Implementation:

1. Create the report shell at `evidence/skill-behavior-tests.md` with the required sections from the test snapshot.
2. Dispatch the two approved RED roles with only their raw scenario and current artifact version.
3. Preserve prompts and outputs unchanged, then assess actual blocking failures separately against the frozen rubric.
4. Run the check-execution-record scenario through one fresh bounded role in a later RED wave if the two-agent cap is occupied; preserve the same isolation rules.
5. Record runtime model/context/fallback details when exposed and invalidate contaminated runs.

Exit criteria:

1. `CHECK-002` has complete, uncontaminated RED records and an explicit list of blocking failures that GREEN must correct.

### `TASK-003` Implementation Task — Add failing structural contract checks

Dependencies:

1. `TASK-002` RED evidence.

Implementation:

1. In `test_harness_policy.py`, register focused check IDs `quality.commitment-verification`, `templates.commitment-verification`, and `compat.current-historical`.
2. Define an explicit current-schema path set containing canonical owners, template sources, generated current templates, standalone templates, README, and operator note; keep all `docs/work-items/**` history outside this set except the named self-hosting fixtures used by this work item.
3. Add positive and independently failing negative Markdown fixtures in temporary directories for exact heading grammar, required fields, ID uniqueness, non-empty valid `Covers`, local/cross-cutting placement, commitment-disposition coverage, verification-execution coverage, task/check origins, and complete Plan Check fields.
4. Update `assert_template_assembly()` expectations from `## Task Plan`, `T-*`, `V-*`, and the symmetric matrix to `## Implementation Tasks`, `TASK-*`, `## Plan Checks`, and the two approved mappings.
5. Add current-vocabulary assertions that reject legacy entity headings on current reusable surfaces but accept the equivalent frozen historical fixture.
6. Run the focused validator and then the full validator. Confirm failures are limited to the intentionally absent new owner/template/consumer contract; repair test defects before continuing.

Exit criteria:

1. `CHECK-003` is RED for the expected missing implementation only, including at least one passing historical fixture and no semantic prose grading.

### `TASK-004` Implementation Task — Implement canonical semantics and routing

Dependencies:

1. `TASK-003` focused RED.

Implementation:

1. Add owned rules in `durable-planning-quality.md` for specification commitments, verification criteria, plan checks, asymmetric plan coverage, and evidence-to-conformance status using the frozen semantics.
2. Add artifact-style rules for full-name headings, local/cross-cutting layout, and readable asymmetric traceability without duplicating semantic definitions.
3. Align lifecycle, execution-quality, evidence, release, model, and freeze consumers only where they name current entities, procedures, execution records, conformance, or lifecycle decisions.
4. Update the policy architecture catalog and router to expose the new quality owners and consumer route; keep templates as schema-shape owners.
5. Run focused checks after each owner/consumer group and keep remaining failures limited to scheduled template or operator surfaces.

Exit criteria:

1. Canonical ownership matches `DEC-001`–`DEC-007`, no consumer defines competing semantics, and focused failures have narrowed to unimplemented schema propagation.

### `TASK-005` Implementation Task — Propagate source schemas and regenerate templates

Dependencies:

1. `TASK-004` canonical owners.

Implementation:

1. Rename and replace the common spec block, update the architecture/readiness source blocks, and update both spec manifests.
2. Replace symmetric traceability with the two mappings; change task examples to full `TASK` headings; add complete `CHECK` blocks and task/check coordination; update plan readiness and completion blocks.
3. Update both plan manifests as needed while retaining stable output schema IDs.
4. Update standalone architecture, amendment, and variance templates with current entity references while preserving `DEC`, `AMD`, and `VAR` identity and lifecycle authority.
5. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`; inspect generated diffs and resolve source blocks rather than hand-editing outputs.
6. Run `CHECK-003` and `CHECK-004`; remaining failures must be limited to scheduled non-template consumers or behavior evidence.

Exit criteria:

1. Current source and generated templates share the exact approved entity grammar, mappings, check fields, and readiness/completion semantics, and assembly is current.

### `TASK-006` Implementation Task — Align examples and operator guidance

Dependencies:

1. `TASK-005` generated template contract.

Implementation:

1. Update README and package-local operator note with one compact Specification Package diagram/description, integrated Plan boundary, and separate evidence-to-conformance loop.
2. Update role examples and current lifecycle/evidence completion examples to use full entity names and new execution-record terminology.
3. Use canonical references instead of copying long policy; ensure ordinary lowercase non-entity uses remain natural.
4. Run `CHECK-005` and repair only current owning or consuming surfaces; do not normalize frozen history.

Exit criteria:

1. Agent and operator surfaces agree on relation meanings, current terminology has one owner, and historical paths remain unchanged.

### `TASK-007` Implementation Task — Demonstrate GREEN and REFACTOR behavior

Dependencies:

1. `TASK-006`; minimum coherent revised package available.

Implementation:

1. Dispatch the two approved GREEN roles with equivalent fresh raw scenarios and the revised package, without RED outputs or conclusions.
2. Compare each preserved GREEN output against every blocking RED failure; record corrections and any new blockers.
3. After GREEN passes, dispatch the loophole-focused REFACTOR variants in waves respecting the two-agent cap.
4. Run the check-execution-record scenario against the revised plan template and record stable/repeated/environment/alternative behavior.
5. Stop for wording/design revision if any blocking RED failure remains or a new blocking classification/traceability failure appears.

Exit criteria:

1. `CHECK-006` passes and the evidence report preserves raw outputs, comparisons, loophole results, runtime/fallback data, and residual uncertainty.

### `TASK-008` Implementation Task — Validate integration and historical compatibility

Dependencies:

1. `TASK-007` behavior gate.

Implementation:

1. Run `CHECK-003` through `CHECK-008`, inspect the full diff, and verify no frozen historical work item, release note, runtime config, or root changelog changed.
2. Confirm the self-hosting plan/test snapshot remain untouched after freeze and their IDs/mappings have no duplicate definitions, dangling coverage, missing stages, or unauthorized deferrals.
3. Dispatch the final semantic reviewer with curated artifacts; if unavailable, perform the approved separate high-reasoning main-agent fallback.
4. Classify findings as blocking or non-blocking, resolve in-scope findings, record any permitted local variance, and rerun affected checks.

Exit criteria:

1. `CHECK-007`, `CHECK-008`, and `CHECK-009` pass with no unresolved blocking finding or approval-required variance.

### `TASK-009` Implementation Task — Record activation and commit cohesively

Dependencies:

1. `TASK-008` complete validation and semantic review.

Implementation:

1. Create `changelog/implementation.md` with heading `### 2026-07-11_commitment-verification-model -- separate commitments, criteria, and checks`, required release metadata, and concise Changed bullets for policy, templates, validation, behavior evidence, and compatibility.
2. Re-run `CHECK-004`, `CHECK-008`, and `git diff --check` after the fragment is added.
3. Stage only approved implementation targets and the implementation fragment; inspect `git diff --cached --name-only` and the cached diff.
4. Commit `docs: commitment-verification-model -- separate commitments, criteria, and checks`.
5. Report commit hash, check execution records, Verification Criterion status, variance, de-facto model/sub-agent use, fallback, context visibility, and residual risk.

Exit criteria:

1. One cohesive implementation commit activates current repository policy without unrelated paths, and the completion report distinguishes task completion from evidence-backed conformance.

## Plan Checks

### `CHECK-001` Plan Check — Confirm the unchanged baseline

Covers:

1. `VER-011`.

Procedure:

1. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.
2. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
3. Run `git status --short` and path-scoped diffs for implementation targets.

Expected result:

1. Both Python commands exit `0`; assembly prints `All assembled templates are current.`; no unexpected implementation-target edits exist.

Evidence record:

1. Execution instance and notable output in the implementation completion record.

Stage or environment:

1. `TASK-001`, pre-edit repository baseline on the implementation branch.

### `CHECK-002` Plan Check — Preserve uncontaminated RED behavior

Covers:

1. `VER-002`.
2. `VER-004`.
3. `VER-008`.
4. `VER-014`.

Procedure:

1. Execute the RED scenario protocol from `snapshots/test-cases.snapshot.md` with fresh bounded agents and current unmodified guidance.
2. Preserve raw prompts/outputs, then assess actual blocking failures separately.

Expected result:

1. Every run records artifact version and isolation details; at least the actual observed failures are reproducible and no expected answer was leaked.

Evidence record:

1. `evidence/skill-behavior-tests.md`, RED section.

Stage or environment:

1. `TASK-002`, control commit `3954a44` before current guidance edits.

### `CHECK-003` Plan Check — Enforce the structural conformance contract

Covers:

1. `VER-003`.
2. `VER-006`.
3. `VER-007`.
4. `VER-008`.
5. `VER-009`.
6. `VER-013`.
7. `VER-017`.

Procedure:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after focused fixtures and checks are registered.
2. During RED, inspect failures for only the absent new contract. During GREEN, rerun after owners and templates are implemented.

Expected result:

1. RED rejects every declared current negative fixture and reports missing current contract; GREEN exits `0`, accepts all positive/current and historical fixtures, and performs no semantic prose scoring.

Evidence record:

1. RED/GREEN command output and fixture summary in `evidence/skill-behavior-tests.md`.

Stage or environment:

1. `TASK-003` RED, then `TASK-005` and `TASK-008` GREEN in the repository Python environment.

### `CHECK-004` Plan Check — Verify source/generated template parity

Covers:

1. `VER-003`.
2. `VER-007`.
3. `VER-012`.
4. `VER-013`.
5. `VER-017`.

Procedure:

1. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` after source/manifests change.
2. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.
3. Inspect generated diffs against the four manifest outputs.

Expected result:

1. Write mode regenerates only declared outputs and its embedded validator exits `0`; check mode exits `0` with `All assembled templates are current.`; generated files contain no unresolved source-block syntax.

Evidence record:

1. Execution instances in the completion report; structural summary in `evidence/skill-behavior-tests.md`.

Stage or environment:

1. `TASK-005` after source edits and `TASK-009` before commit.

### `CHECK-005` Plan Check — Review current vocabulary and historical preservation

Covers:

1. `VER-001`.
2. `VER-003`.
3. `VER-010`.
4. `VER-011`.
5. `VER-012`.
6. `VER-015`.
7. `VER-017`.

Procedure:

1. Run a current-surface `rg -n` search for full entity names, relation verbs, and legacy entity headings across `.agents/skills/dev-doc-harness` plus `README.md`.
2. Run `git diff --name-only -- docs/work-items` and `git diff -- docs/work-items`.
3. Manually classify ordinary lowercase words, historical examples, and entity names; do not use a global word ban.

Expected result:

1. Current reusable surfaces use one coherent entity/relation vocabulary; legacy entity schema remains only in frozen history or explicit compatibility explanation; no frozen work-item path changes except this work item's new implementation evidence and fragment.

Evidence record:

1. Search summary and path review in the implementation completion record and final-review section of `evidence/skill-behavior-tests.md`.

Stage or environment:

1. `TASK-006` and `TASK-008`, completed current-surface diff.

### `CHECK-006` Plan Check — Demonstrate GREEN and loophole correction

Covers:

1. `VER-002`.
2. `VER-004`.
3. `VER-005`.
4. `VER-006`.
5. `VER-008`.
6. `VER-009`.
7. `VER-014`.

Procedure:

1. Execute GREEN equivalent and REFACTOR loophole scenarios from the test snapshot using fresh contexts and the revised package.
2. Compare outputs against each actual RED blocker only after raw outputs are preserved.

Expected result:

1. Every RED blocker is corrected, no new blocking classification or traceability failure appears, and loophole variants retain the correction.

Evidence record:

1. `evidence/skill-behavior-tests.md`, GREEN/REFACTOR comparison and gate status.

Stage or environment:

1. `TASK-007`, revised current package before implementation commit.

### `CHECK-007` Plan Check — Review self-hosting planning artifacts

Covers:

1. `VER-016`.

Procedure:

1. Inspect the frozen spec, architecture snapshot, plan, and test snapshot for exact entity headings, unique IDs, valid coverage, deterministic placement, complete mappings, task/check integration, authorized dispositions, and readable trace density.
2. Run `rg -n "TBD|TODO|<describe|<specific|<observable|unresolved required"` against the plan and test snapshot.

Expected result:

1. No duplicate entity definitions, dangling coverage, wrong placement, missing disposition/check, unauthorized deferral, unresolved placeholder, or blocking readability finding exists.

Evidence record:

1. Plan-freeze review at approval and final semantic-review section during implementation.

Stage or environment:

1. Plan draft review/freeze and `TASK-008` post-implementation review.

### `CHECK-008` Plan Check — Run final deterministic validation

Covers:

1. `VER-009`.
2. `VER-011`.
3. `VER-012`.
4. `VER-013`.
5. `VER-017`.

Procedure:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.
3. Run `git diff --check`, `git diff --stat`, `git diff --name-only`, and inspect the full diff.

Expected result:

1. Commands exit `0`; all validator check IDs pass; assembly is current; no whitespace errors, unrelated paths, frozen-history edits, generated noise, or hidden implementation changes remain.

Evidence record:

1. Distinct execution instances before final review and before commit in the completion report.

Stage or environment:

1. `TASK-008` and `TASK-009`, completed implementation worktree.

### `CHECK-009` Plan Check — Complete flagship semantic review

Covers:

1. `VER-001`.
2. `VER-004`.
3. `VER-005`.
4. `VER-006`.
5. `VER-010`.
6. `VER-014`.
7. `VER-015`.
8. `VER-016`.

Procedure:

1. Review the frozen package, completed diff, behavior evidence, structural results, and compatibility search with the approved flagship/high reviewer or fallback.
2. Classify every finding as blocking or non-blocking and resolve or route it through variance policy.

Expected result:

1. No blocking semantic, ownership, topology, lifecycle, historical-compatibility, or self-hosting readability finding remains.

Evidence record:

1. `evidence/skill-behavior-tests.md`, final semantic-review section, plus completion summary.

Stage or environment:

1. `TASK-008`, after deterministic validation and before changelog/commit.

## Planned Commits

Planning approval:

1. Subject: `plan: commitment-verification-model -- map commitments to checks`.
2. Changelog title or snippet: `2026-07-11_commitment-verification-model -- map commitments to checks`.
3. Contents: this plan, `snapshots/test-cases.snapshot.md`, the Superpowers plan pointer, `changelog/plan-approval.md`, and root `CHANGELOG.md` only if the applicable operator-level freeze instruction still requires consolidation at approval time.

Implementation:

1. Subject: `docs: commitment-verification-model -- separate commitments, criteria, and checks`.
2. Changelog title or snippet: `2026-07-11_commitment-verification-model -- separate commitments, criteria, and checks`.
3. Contents: one cohesive current policy/template/validator/operator/evidence activation change plus `changelog/implementation.md`.

## Documentation Artifact Matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `changelog/plan-approval.md`, `changelog/implementation.md` | Create only at the matching approval or implementation checkpoint |
| Root changelog consolidation | Living | As instructed | Plan approval only if higher-priority freeze instructions require it | `CHANGELOG.md` | Do not include in implementation commit |
| Test cases | Snapshot | Yes | Before plan freeze | `snapshots/test-cases.snapshot.md` | Frozen with this plan |
| Skill-behavior evidence | Derived evidence | Yes | During implementation | `evidence/skill-behavior-tests.md` | Preserves RED/GREEN/REFACTOR/final review |
| Testing guide delta | Living delta | No | Not applicable | Not applicable | Existing validator entrypoint remains |
| Operator manual delta | Living delta | No | Not applicable | Not applicable | README and package-local operator note are direct targets |
| API reference delta | Living delta | No | Not applicable | Not applicable | No public software API |
| Architecture snapshot | Snapshot | Yes | Already frozen | `snapshots/architecture.snapshot.md` | Authoritative `DEC-001`–`DEC-007` |
| Architecture summary delta | Living delta | No | Not applicable | Not applicable | No repository-level architecture manual |
| Superpowers plan pointer | Pointer stub | Yes | Before plan freeze | `docs/superpowers/plans/2026-07-12-commitment-verification-model.md` | Minimal pointer to this canonical plan; no duplicated plan content |
| Package release notes | Release artifact | No | Later release branch | Not applicable | Development marker stays `0.5+` |

## Plan Variance Handling

Before freeze, operator feedback edits this Draft directly. After freeze, record nontrivial local implementation variance in `implementation-notes/variance-log.md`. Stop and create an amendment before changing entity semantics, lifecycle activation, heading grammar, facet definitions or precedence, criterion applicability or aggregation, hybrid or cross-phase placement, commitment disposition authority, Plan Check records, plan traceability, policy ownership, historical compatibility, test-first behavior contract, or implementation feasibility.

## Planning Artifact Freeze Gate

Draft review status: approved by the operator on 2026-07-12.

Approval freeze status:

1. This plan, `snapshots/test-cases.snapshot.md`, the Superpowers plan pointer, `changelog/plan-approval.md`, and the stricter top-level-instruction `CHANGELOG.md` entry form the approved plan-only package.
2. The approval commit subject is `plan: commitment-verification-model -- map commitments to checks`.
3. Implementation remains prohibited until a fresh post-freeze operator instruction confirms execution settings and authorizes the start.

## Next-Task Handoff

Execution continuity: `new task with curated-artifact handoff`.

Context visibility: `not exposed`; do not prescribe compaction.

Artifact rehydration required: `Yes`.

Exact authoritative artifacts after plan freeze:

1. `docs/work-items/2026-07-11_commitment-verification-model/spec_commitment-verification-model.md`.
2. `docs/work-items/2026-07-11_commitment-verification-model/snapshots/architecture.snapshot.md`.
3. `docs/work-items/2026-07-11_commitment-verification-model/snapshots/test-cases.snapshot.md`.
4. `docs/work-items/2026-07-11_commitment-verification-model/plan_commitment-verification-model.md`.
5. Any later approved `plan_amendment-*.md`.

Approved strategy and fallback: `## Model and Sub-agent Strategy` in this plan.

First activity: `TASK-001` Implementation Task — Rehydrate the frozen package and baseline.

Variance stop condition: stop for every approval-required class listed in `## Plan Variance Handling`; do not reinterpret the frozen spec.

Copy-ready post-freeze prompt:

```text
Implement `2026-07-11_commitment-verification-model` from its frozen package:

- `docs/work-items/2026-07-11_commitment-verification-model/spec_commitment-verification-model.md`
- `docs/work-items/2026-07-11_commitment-verification-model/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-07-11_commitment-verification-model/snapshots/test-cases.snapshot.md`
- `docs/work-items/2026-07-11_commitment-verification-model/plan_commitment-verification-model.md`

Follow applicable `AGENTS.md`, the repository harness, Superpowers execution
guidance, and `rule:execution-quality.execution-thread-start`. Rehydrate the
frozen package, use the approved model/sub-agent strategy and fallback, start
at `TASK-001`, and stop for approval-required variance rather than
reinterpreting the spec.
```

## Plan Readiness Checklist

- [x] Frozen inputs, approval state, repository baseline, and exact current change surfaces are recorded.
- [x] Every Specification Commitment has an authorized task or verification disposition.
- [x] Every Verification Criterion has one or more Plan Checks and an evidence stage.
- [x] Architecture Decisions are consumed through their mapped Specification Commitments rather than treated as independent scope.
- [x] Implementation Tasks and Plan Checks have explicit dependencies, stages, fields, and completion signals.
- [x] Behavior RED/GREEN/REFACTOR isolation, structural fixtures, compatibility, and final review are fully specified.
- [x] Model dimensions, bounded roles, cap two, fallback, integration ownership, continuity, and rehydration are recorded.
- [x] Planned subjects and changelog snippets are synchronized.
- [x] No unresolved placeholders, required decisions, missing sections, or ownerless deferrals remain.
- [x] The work still fits one orchestration thread with bounded read-only delegation.

## Completion Criteria

1. `VER-001` through `VER-017` have executed Plan Check evidence and pass status.
2. Canonical owners, routes, source blocks, manifests, generated templates, standalone templates, examples, README, operator note, validator, and completion guidance agree on the frozen model.
3. RED failures are preserved and corrected by GREEN/REFACTOR evidence without leaked expected answers.
4. Current structural checks pass while frozen historical artifacts remain unchanged and valid.
5. The planned implementation fragment and cohesive commit contain no unrelated paths.
6. Completion reports execution instances, criterion status, variance, residual risk, and de-facto model/sub-agent/fallback/context behavior.

## Approval

- Status: Approved
- Superseded by: None
