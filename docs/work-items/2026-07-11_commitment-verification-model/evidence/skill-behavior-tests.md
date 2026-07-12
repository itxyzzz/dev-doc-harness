# Commitment Verification Model Skill-Behavior Evidence

Work ID: `2026-07-11_commitment-verification-model`
Status: In progress
Control commit: `3954a44`

## Scope and tested artifact versions

1. RED control: commit `3954a44`, harness marker `0.5+`.
2. Roles: `behavior-red-a`, `behavior-red-b`, and retry role `behavior-red-checks-retry`; all read-only with curated raw prompts.
3. Planned role profile: `balanced` / medium reasoning. Concrete model and context telemetry were not exposed.
4. The first check-record role returned no required report and was invalidated. The retry received the same raw scenario and no prior output or conclusions.

## RED raw prompts and outputs

### `scenario:commitment.authoring-decomposition`

Raw prompt: the frozen snapshot's RED authoring scenario, supplied without the snapshot, frozen spec, expected decomposition, or reviewer findings.

Raw output from `behavior-red-a`:

```md
## Requirements

### `REQ-001` Route model or profile transitions to a fresh task

When the approved execution selection changes the main model generation, capability tier, resolved profile, or platform multi-agent profile, execution must move to a new task using a curated-artifact handoff before implementation edits begin.

Rationale:

1. A fresh task gives the changed execution profile a clean, authoritative starting context and prevents stale conversational state from silently governing implementation.

Acceptance links:

1. Covered by `AC-001` and `AC-004`.

### `REQ-002` Preserve suitable same-task continuation

When the current model generation and profile remain suitable for the approved work, the harness must preserve same-task continuation unless another explicit execution constraint requires a new task.

Rationale:

1. Model-transition handling must not create unnecessary task churn when no material profile transition exists.

Acceptance links:

1. Covered by `AC-002`.

### `REQ-003` Rehydrate after any same-task model switch

If an approved model switch nevertheless occurs within the same task, the agent must, before editing:

1. Re-read every frozen artifact named by the handoff.
2. Check applicable amendments and the variance log.
3. Reconcile the immediate implementation scope against those authoritative artifacts.
4. Stop under `rule:lifecycle.variance-policy` if reconciliation exposes approval-required variance.

This requirement applies regardless of whether the switch was operator-requested, platform-managed, or accompanied by runtime-managed compaction.

Rationale:

1. A same-task switch can change the effective reasoning context even though the task identity remains unchanged.

Acceptance links:

1. Covered by `AC-003`.

### `REQ-004` Produce a minimal authoritative-artifact handoff

A transition handoff must:

1. Name the exact frozen spec, plan or phase plan, architecture snapshot, amendments, and required evidence artifacts.
2. Cite `rule:execution-quality.execution-thread-start` as the startup rule.
3. Refer to the approved model and sub-agent strategy and its fallback.
4. Name the first implementation activity.
5. State the approval-required variance stop condition.
6. Include a copy-ready startup prompt when execution moves to a fresh task or a different model/profile.
7. Reference authoritative artifacts instead of copying or paraphrasing their requirements.

The handoff must not state a precise remaining-context value, infer a compaction threshold, or prescribe compaction from an estimate when the platform does not expose exact remaining context.

Rationale:

1. A compact handoff avoids creating a second requirements source while preserving everything needed for deterministic startup.

Acceptance links:

1. Covered by `AC-001`, `AC-004`, `AC-005`, and `AC-006`.

### `REQ-005` Expose reviewer-verifiable transition behavior

The behavior must be verifiable through:

1. Canonical model-continuity policy text.
2. The primary spec, plan, and phase-plan templates.
3. The execution-start policy.
4. Automated policy validation.
5. A frozen fresh-task scenario covering an actual generation or profile transition.

Rationale:

1. Reviewers need evidence that the behavior is normative, prompted by generated artifacts, and executable as a concrete handoff rather than merely documented in one location.

Acceptance links:

1. Covered by `AC-004`, `AC-005`, and `AC-007`.

## Acceptance Criteria

### `AC-001` Changed generation or profile starts in a fresh task

Verifies:

1. `REQ-001` and `REQ-004`.

Method:

1. Review the frozen fresh-task scenario and its resulting handoff.

Scenario:

1. Given approved execution artifacts whose selected main model generation or profile differs from the current task,
2. when implementation is authorized,
3. then no implementation edit is made in the old task,
4. and the handoff starts a fresh task using the exact frozen artifacts and `rule:execution-quality.execution-thread-start`,
5. and the fresh task completes execution preflight before its first edit.

### `AC-002` Suitable current profile remains in the same task

Verifies:

1. `REQ-002`.

Method:

1. Review a policy example or scenario in which the current generation and profile remain suitable.

Scenario:

1. Given no change to the selected main model generation or profile and no independent continuity constraint,
2. when implementation continues,
3. then execution continuity remains `same task`,
4. and no fresh-task handoff is required solely for model selection.

### `AC-003` Same-task switch rehydrates before editing

Verifies:

1. `REQ-003`.

Method:

1. Review the same-task-switch scenario or execution record.

Scenario:

1. Given a model switch occurs without moving to a fresh task,
2. when the switched model resumes,
3. then the execution record shows that it re-read the named frozen package, checked amendments and variance, and reconciled immediate scope before any edit,
4. and any approval-required mismatch stops execution.

### `AC-004` Policy and templates carry the complete transition contract

Verifies:

1. `REQ-001`, `REQ-004`, and `REQ-005`.

Method:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Confirm exit code `0`.
3. Confirm the validator checks the canonical continuity owner, execution-start owner, primary template handoff sections, artifact rehydration, first activity, variance stop condition, fresh-task preference, and the prohibition on unexposed precise context estimates.

### `AC-005` Handoff names exact authoritative artifacts and startup rule

Verifies:

1. `REQ-004`.

Method:

1. Inspect the rendered handoff produced from the approved package.

Expected result:

1. The handoff names exact frozen spec, plan, architecture snapshot, and test snapshot paths.
2. The handoff cites `rule:execution-quality.execution-thread-start`.
3. The handoff refers to the approved strategy and fallback in the frozen plan.
4. The handoff names the first activity and approval-required variance stop condition.
5. The handoff does not reproduce the requirements from the frozen artifacts.

### `AC-006` Unexposed context is reported without invented precision

Verifies:

1. `REQ-004`.

Method:

1. Inspect policy text, template prompts, the frozen scenario, and the produced handoff.

Expected result:

1. When exact remaining context is unavailable, the artifact records `Context visibility: not exposed`.
2. No percentage, token count, remaining-context value, inferred threshold, or compaction instruction is presented as known.

### `AC-007` Fresh-task scenario is durable and reviewable

Verifies:

1. `REQ-005`.

Method:

1. Review the frozen test-case snapshot.

Expected result:

1. The snapshot contains a scenario with a changed model generation or profile.
2. It asserts that editing remains blocked in the original task.
3. It names the curated frozen-artifact inputs to the fresh task.
4. It exercises the startup preflight, first activity, and variance stop condition.
5. It includes a negative assertion against copied requirements and invented remaining-context precision.

## Architecture Decisions

### `DEC-001` Use a minimal reference-based transition handoff

Selected approach:

1. Transition handoffs contain only exact authoritative artifact paths, the startup rule, approved strategy and fallback reference, first activity, and variance stop condition.
2. Frozen requirements remain exclusively in their authoritative artifacts.
```

Role report: no files changed; current harness, quality/lifecycle/model/execution references, current spec template, architecture template, and a validator excerpt were inspected. No test ran. Concrete model/profile and exact context were not exposed.

### `scenario:commitment.plan-asymmetric-coverage`

Raw prompt: the frozen snapshot's RED planning scenario, supplied without expected mappings or reviewer findings.

Raw output from `behavior-red-b`:

```md
## Spec Traceability

| Requirement or acceptance criterion | Primary tasks | Validation |
|---|---|---|
| `SPEC-001` Current reusable templates adopt the new heading grammar | `T-001`, `T-003` | `VER-001`, `VER-003` |
| `SPEC-002` Frozen historical work-item artifacts remain unchanged | `T-004` | `VER-002` |
| `SPEC-003` Operator guidance uses the new grammar and coherent terminology | `T-002`, `T-003` | `VER-003` |
| `SPEC-004` Later-release requirement | `T-005` preserves the frozen phase assignment; no current-phase implementation | `VER-004` in the later release phase |
| `VER-001` Current template structure conforms | `T-001`, `T-003` | `V-001` |
| `VER-002` Historical artifacts are preserved path by path | `T-004` | `V-002` |
| `VER-003` Terminology is coherent across current templates and operator guidance | `T-001`, `T-002`, `T-003` | `V-001`, `V-003` |
| `VER-004` Later-release validation | `T-005` preserves ownership; no current-phase execution | `V-004` in the later release phase |

## Task Plan

### `T-001` Apply the new heading grammar to template source blocks

Dependencies: frozen `SPEC-001` and `DEC-001`.

Implementation: update authoritative source blocks, preserve assembly boundaries, and do not edit generated templates directly.

### `T-002` Update operator guidance

Dependencies: `T-001`.

Implementation: update the operator note and preserve unrelated workflow and historical boundaries.

### `T-003` Assemble and review generated current templates

Dependencies: `T-001`, `T-002`.

Implementation: run `assemble_templates.py --write`, review manifest outputs, and confirm generated changes derive from sources.

### `T-004` Verify path-scoped historical preservation

Dependencies: `T-003`.

Implementation: inspect the work-item diff relative to control commit `3954a44`; make no product edit for `SPEC-002`.

### `T-005` Preserve later-release ownership

Dependencies: frozen `SPEC-004` phase assignment.

Implementation: keep `SPEC-004` and `VER-004` out of the current phase while retaining their later-phase assignment.

## Validation Plan

| Command | Expected result |
|---|---|
| `assemble_templates.py --write` | Provides `V-001` evidence for `VER-001` and part of `VER-003`. |
| Path-scoped historical diff | Provides `V-002` evidence for `VER-002`. |
| Manual coherence review | Completes `V-003` evidence for `VER-003`. |
| Later release executes `VER-004` | Current phase records only preserved ownership. |
```

Role report: no files changed; control-commit current plan template, assembly manifest, router, and operator note were inspected. `assemble_templates.py --list` exited `0`. Concrete model/profile and context telemetry were not exposed.

### `scenario:commitment.check-execution-records`

The first role returned no report and was invalidated. Retry raw output:

```text
Checks

CHK-ASM-001: one assembly procedure/execution with command, working directory, inputs, version, timestamp, exit code, and artifact evidence.
CHK-VAL-001: one stable validator procedure identity with separate pre-review and pre-commit execution records.
CHK-COMP-001 / CHK-COMP-002: current and historical compatibility scopes represented as separate check identities.
CHK-READ-001: an any-of alternative group with CHK-READ-001-A and CHK-READ-001-B and an equivalence rationale.

Completion record: a custom YAML document keyed by proposition IDs, procedure revisions, execution IDs, checkpoints, inputs, exit codes, evidence locations, reviewer trace, exceptions, residual risks, and reviewer decision.
```

Role report: no files inspected or changed and no commands ran; exact repository commands and required field names were unavailable. Concrete runtime model and context telemetry were not exposed.

## RED blocking findings

1. Authoring run: independently amendable handoff obligations remain combined in `REQ-004`; the current template provides no `Kind`/`Intent`; criteria use global `AC` placement; `Method` mixes procedures into criteria; and the legacy entity grammar persists.
2. Planning run: one symmetric matrix maps both specification and verification entities to tasks and validation; preservation-only `SPEC-002` receives artificial `T-004`; no complete `CHECK` blocks exist; and task/check coordination cannot be expressed through check dependencies or stages.
3. Check-record run: custom `CHK-*` IDs and YAML replace the required full-name `CHECK-*` Plan Check blocks; required `Covers`, `Procedure`, `Expected result`, `Evidence record`, and `Stage or environment` fields are not preserved as the plan schema; current/historical scopes become different check identities even when the intended procedure is shared; blocker status is absent from the execution examples.
4. These are the blocking RED failures GREEN must correct. The evidence is uncontaminated: agents did not receive the snapshot rubric, expected decomposition, frozen spec, or prior conclusions.

## GREEN raw prompts and outputs

### Authoring transfer

The fresh release-synchronization output used four classified, atomic `SPEC` blocks, local `VER-001` through `VER-004`, one cross-cutting `VER-005`, and mapped `DEC-001`/`DEC-002` decisions. It kept procedures out of Expected evidence, named lifecycle and exposure boundaries in Statements, and used exact full-name headings. The complete role output was returned directly to the orchestration thread; no RED output or assessment was in its context.

### Planning transfer

The fresh policy/validator output produced separate commitment-disposition and verification-execution mappings; used verification-only treatment for historical preservation; retained the exact frozen later-release disposition; consumed `DEC-001` only under `SPEC-003`; and defined full `TASK-001` through `TASK-003` plus complete `CHECK-001` through `CHECK-003` blocks with stages and coordination. No RED output or assessment was in its context.

### Complete raw GREEN authoring output

Raw prompt: the release-branch synchronization equivalent scenario recorded for `behavior-green-a`; no RED output, rubric, or expected decomposition was supplied.

```md
## Specification Commitments and Local Verification Criteria

### `SPEC-001` Specification Commitment — Refuse an unsafe release start

Kind: `Behavior`

Intent: `Prevent`

Concerns: `release safety, repository synchronization`

Statement:

1. When release-branch creation is requested, the workflow shall refresh the authoritative remote refs and refuse to create or modify a release branch unless the current branch is `master`, the worktree and index are clean, and local `master` and the refreshed authoritative remote `master` ref identify the same commit.
2. Refusal shall occur before release files, commits, branches, or remote refs are changed and shall identify the failed precondition without claiming facts not established by the checks.

#### `VER-001` Verification Criterion — Unsafe start states are rejected

Covers:

1. `SPEC-001`.

Criterion:

1. The workflow makes no release-related repository change for each unsafe branch, worktree, ahead, behind, or diverged state and proceeds only when every precondition is demonstrated.

Expected evidence:

1. Tests for every rejection state and the accepted synchronized state.
2. Evidence that rejection precedes release-marker edits, commits, branch creation, or pushes.
3. Failure output identifying the unmet precondition.

### `SPEC-002` Specification Commitment — Derive release identity from remote release refs

Kind: `Behavior`

Intent: `Change`

Concerns: `version source, deterministic release identity`

Statement:

1. After preflight passes, derive the latest released version exclusively from refreshed remote refs exactly matching `release/<major>.<minor>`.
2. Local-only branches, tags, package markers, changelog headings, and copied handoff text shall not be competing authorities.
3. Increment the greatest remote release branch's minor component, reset patch to `0`, and derive `release/<major>.<minor>`.
4. Stop for operator direction on no source, ambiguity, or an existing remote release branch.

#### `VER-002` Verification Criterion — Remote refs control version derivation

Covers:

1. `SPEC-002`.

Criterion:

1. Controlled fixtures select the greatest valid remote ref, derive the specified next minor, ignore malformed and local-only names, and refuse unresolved or colliding cases.

Expected evidence:

1. Accepted and rejected remote-ref fixtures with derived identities and stop-state evidence.

### `SPEC-003` Specification Commitment — Restore master development state after release work

Kind: `Behavior`

Intent: `Maintain`

Concerns: `branch lifecycle, package markers`

Statement:

1. Return to `master` after release work and before the post-release reset.
2. Reset every current-development surface to the derived development marker, including `VERSION`, release policy, validator expectations, and root changelog development state.
3. Keep concrete release-note paths and released changelog content tied to the concrete release.
4. Stop without reporting completion if synchronized `master` or the protected integration path cannot be demonstrated.

#### `VER-003` Verification Criterion — Post-release state is coherent

Covers:

1. `SPEC-003`.

Criterion:

1. Fresh execution ends on the authorized `master` development state with current-development surfaces reset and release artifacts retaining the concrete version.

Expected evidence:

1. Final branch/commit identity, marker readbacks, preserved release artifacts, and passing harness validation.

### `SPEC-004` Specification Commitment — Produce a reference-based execution handoff

Kind: `Deliverable`

Intent: `Establish`

Concerns: `fresh-task execution, context integrity`

Statement:

1. Name exact authoritative instruction, runbook, policy, approved work-item, amendment, and evidence paths.
2. Require `rule:execution-quality.execution-thread-start`, name strategy/fallback, first activity, and variance stop condition.
3. Reference rather than copy requirements.
4. Report runtime and repository facts only when exposed or checked; otherwise use `not exposed` or require fresh verification.

#### `VER-004` Verification Criterion — Fresh-task handoff is sufficient and bounded

Covers:

1. `SPEC-004`.

Criterion:

1. A reviewer using only the handoff can locate authority, apply startup, identify activity/stop conditions, and distinguish verified from unexposed facts.

Expected evidence:

1. Completed handoff, fresh-task dry run, and inspection for invented facts.

## Cross-cutting Verification Criteria

### `VER-005` Verification Criterion — Policy, templates, and fresh execution agree

Covers:

1. `SPEC-001`.
2. `SPEC-002`.
3. `SPEC-003`.
4. `SPEC-004`.

Criterion:

1. Policy, runbook, templates, sources/manifests, validator, and a fresh scenario encode one consistent release lifecycle.

Expected evidence:

1. Cross-surface trace, generated-artifact consistency, passing validator, and contradiction-free current-surface inspection.

Applicability:

1. Final completion.

### `DEC-001` Architecture Decision — Use remote refs as version authority

Selected approach:

1. Refreshed matching remote release refs are the sole version source.

Source spec sections:

1. `SPEC-001`.
2. `SPEC-002`.

### `DEC-002` Architecture Decision — Preserve handoff authority by reference

Selected approach:

1. Handoffs name exact frozen artifacts and startup rules instead of copying normative text.

Source spec sections:

1. `SPEC-004`.
```

Role report: read-only; current router, quality/lifecycle/model/execution/release references, spec and architecture templates, release runbook, and `0.5+` marker inspected; no tests; exact model/profile/context not exposed.

### Complete raw GREEN planning output

Raw prompt: the policy/validator equivalent scenario recorded for `behavior-green-b`; no RED output, rubric, or expected mapping was supplied.

```md
## Commitment-Disposition Mapping

| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` Change canonical policy owner text | Implement | `TASK-001`, `TASK-003` |
| `SPEC-002` Preserve frozen historical snapshots | Verification-only | None; `CHECK-003` |
| `SPEC-003` Update validator behavior | Implement under `DEC-001` | `TASK-002`, `TASK-003` |
| `SPEC-004` Later-release scope | Exact frozen later-release assignment | None in this release |

## Verification-Execution Mapping

| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` Current policy ownership | `CHECK-002` | Pre-commit |
| `VER-002` Historical preservation | `CHECK-003` | Review and pre-commit |
| `VER-003` Policy/validator coherence | `CHECK-001`, `CHECK-002` | Implementation and pre-commit |
| `VER-004` Later-release verification | None in this release; frozen later owner | Later release |

## Implementation Tasks

### `TASK-001` Implementation Task — Update the canonical policy owner

Dependencies:

1. Frozen `SPEC-001`.

Implementation:

1. Change only the current owner text and keep frozen history outside the edit set.

Exit criteria:

1. `CHECK-002` passes for `VER-001` with no historical change.

### `TASK-002` Implementation Task — Align validator behavior and fixtures

Dependencies:

1. `TASK-001`, `SPEC-003`, and `DEC-001`.

Implementation:

1. Update deterministic validation and positive/negative fixtures while preserving historical compatibility.

Exit criteria:

1. Focused fixtures and the full validator pass for `VER-003`.

### `TASK-003` Implementation Task — Record lifecycle evidence

Dependencies:

1. `TASK-001`, `TASK-002`, and `CHECK-001` through `CHECK-003`.

Implementation:

1. Record executions, update the changelog fragment, and report later-release ownership separately.

Exit criteria:

1. Completion distinguishes task status from criterion status.

## Plan Checks

### `CHECK-001` Plan Check — Run focused structural fixtures

Covers:

1. `VER-003`.

Procedure:

1. Run focused positive and negative fixtures.

Expected result:

1. Positives pass, negatives fail for intended reasons, and history is not edited.

Evidence record:

1. Command/entry point, execution ID, output, environment, and status.

Stage or environment:

1. Implementation; gates `CHECK-002`.

### `CHECK-002` Plan Check — Run the full harness validator

Covers:

1. `VER-001`.
2. `VER-003`.

Procedure:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result:

1. Exit `0` with coherent current ownership and no regression.

Evidence record:

1. Command, execution ID, result, environment, and status.

Stage or environment:

1. Pre-commit after `CHECK-001`.

### `CHECK-003` Plan Check — Inspect frozen historical paths

Covers:

1. `VER-002`.

Procedure:

1. Inspect the diff against the exact frozen path set and confirm compatibility without rewriting.

Expected result:

1. Empty historical diff and retained compatibility.

Evidence record:

1. Frozen paths, diff output, execution ID, environment, and status.

Stage or environment:

1. Review and pre-commit.
```

Role report: read-only; current router, quality/lifecycle/model references, plan template, marker, and bounded validator excerpts inspected; no tests; exact model/profile/context not exposed.

## GREEN comparison

| Recorded RED blocker | GREEN result |
|---|---|
| Combined independently consequential obligations | Corrected: authoring output split branch gate, version derivation, post-release state, and handoff into separate commitments. |
| Scope hidden in notes, decisions, or criteria | Corrected: normative obligations were Statements and decisions mapped through `Source spec sections`. |
| Missing/ambiguous facets | Corrected: every commitment used one permitted Kind and Intent. |
| Procedure mixed into criterion | Corrected: criteria stated propositions/evidence; procedures appeared only in Plan Checks. |
| Wrong local/cross-cutting placement | Corrected: single-target criteria were local and the multi-target criterion appeared once cross-cutting. |
| Symmetric traceability | Corrected: two complete mappings were produced. |
| Artificial preservation task | Corrected: preservation was verification-only. |
| Missing Plan Check schema and coordination | Corrected: full-name checks included all required fields, stages, and task/check dependencies. |
| Unapproved deferral | Corrected: the later-release case cited frozen authorization rather than inventing a deferral. |

GREEN gate: `pass`; every recorded RED blocker was corrected and no new blocking classification or traceability failure appeared.

## REFACTOR loophole prompts, outputs, and findings

1. Hidden-scope authoring variant: the agent promoted telemetry found only in an Architecture Decision into `SPEC-002`, preserved the old-config baseline in `SPEC-001`, kept the concrete Python command for a future Plan Check, and defined the two-target coherence criterion once under Cross-cutting Verification Criteria. Result: `pass`.
2. Planning variant: the agent kept distinct `VER-001`/`VER-002` meanings while one `CHECK-001` suite produced criterion-specific evidence, assigned cross-cutting `VER-003` to the post-documentation final-prerequisite stage, gave preservation verification-only treatment, and refused the convenience deferral of `SPEC-004`. Result: `pass`.
3. Check-record transfer: the agent produced full-name `CHECK-001` through `CHECK-004` blocks with every required field; reused stable `CHECK-002` for distinct review/pre-commit executions; used one compatibility procedure with separately identified current/historical scope evidence; and defined an explicit `Any one of` render group with an equivalence rationale. Expected completion records retained unique execution identities and pass/fail/blocker-capable status. Result: `pass`.

## Structural fixture commands and results

1. RED execution: `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` exited `1` only for missing new rule owners, absent/legacy current schema surfaces, and the planned evidence file's intermediate untracked state. Positive fixtures passed; every declared negative fixture was rejected; the historical fixture remained accepted; no prose-semantic grading was added.
2. GREEN execution via `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` exited `0`, reported `All assembled templates are current.`, and passed all 27 checks including `quality.commitment-verification`, `templates.commitment-verification`, and `compat.current-historical`.
3. Current-surface legacy-heading search returned no matches. Path review found no frozen work-item change; this work item's evidence file was the only work-item implementation artifact.

## Final semantic-review findings

The first flagship semantic review classified two findings as blocking: the structural fixture matrix did not yet cover the complete negative matrix or a real frozen historical fixture, and the durable evidence did not preserve exact raw GREEN and REFACTOR outputs. The implementation added the missing duplicate-ID, adjacency, missing-row, orphan-check, invalid-target, full-name decision, and real-history fixtures. The following section supersedes the editorial GREEN/REFACTOR summaries above with accepted fresh-role outputs preserved verbatim.

The closure re-review found no remaining Critical or Important findings. It confirmed duplicate `TASK` rejection and its independent negative fixture, and confirmed that every accepted GREEN, REFACTOR, and check-record role pairs a verbatim raw prompt with its complete raw output. Verdict: `pass`; TASK-009 and commit may proceed.

Several intermediate reruns were discarded: three roles stalled while attempting sandboxed reads, and later schema-only retries omitted required literal grammar. Discarded outputs are not used as passing evidence. The accepted roles below received fresh contexts, no prior outputs or conclusions, no repository-write authority, the raw scenario, and only the public schema contract needed to avoid the degraded Windows read path.

## Exact accepted fresh-role outputs

### `evidence-green-authoring-final-v2`

Raw prompt (verbatim):

~~~~text
Fresh GREEN read-only behavior role. No tools, files, edits, prior outputs, expected decomposition, rubric, or conclusions.

Use the literal skeleton and keep exact punctuation:
```markdown
### `SPEC-NNN` Specification Commitment — Title

Kind:

1. `AllowedValue`.

Intent:

1. `AllowedValue`.

Statement:

1. Text.

#### `VER-NNN` Verification Criterion — Title

Covers:

1. `SPEC-NNN`.

Criterion:

1. Proposition.

Expected evidence:

1. Evidence.

## Cross-cutting Verification Criteria

### `VER-NNN` Verification Criterion — Title

Covers:

1. `SPEC-NNN`.
2. `SPEC-NNN`.

Criterion:

1. Proposition.

Expected evidence:

1. Evidence.

Applicability:

1. Stage.

### `DEC-NNN` Architecture Decision — Title

Selected approach:

1. Approach.

Source spec sections:

1. `SPEC-NNN`.
```
Allowed Kind values only: `Outcome`, `Behavior`, `Quality`, `Constraint`, `Deliverable`. Allowed Intent values only: `Establish`, `Change`, `Preserve`, `Maintain`, `Prevent`. One-target criteria are adjacent; the single multi-target criterion is under the exact cross-cutting heading. Criteria are propositions, not commands.

Scenario: Release-branch synchronization must (a) reject start unless on clean synchronized master before mutation; (b) derive next identity solely from refreshed matching remote release refs and stop when authority is missing, ambiguous, or colliding; (c) leave master in a coherent post-release development-marker state while retaining concrete released artifacts; and (d) produce a bounded reference-based fresh-task handoff without copied requirements or invented facts. Include local criteria, one criterion spanning all commitments, and decisions for remote-ref authority and reference-based handoff.

Before returning, silently check that every Kind/Intent is in the allowed set, every entity ID is backticked, every field label has a colon, and the cross-cutting heading is present.

Return `## Proposed Markdown excerpt`, complete excerpt, then `## Role report` with exactly: `No files inspected; no commands or tests run; no files changed; concrete runtime model, profile, and context telemetry was not exposed.`
~~~~

Complete raw output:

~~~~md
## Proposed Markdown excerpt

### `SPEC-001` Specification Commitment — Clean Synchronized Master Precondition

Kind:

1. `Behavior`.

Intent:

1. `Prevent`.

Statement:

1. Release-branch synchronization rejects its start before any mutation unless the current branch is `master`, the worktree is clean, and local `master` is synchronized with its refreshed remote authority.

#### `VER-001` Verification Criterion — Precondition Rejection Is Non-Mutating

Covers:

1. `SPEC-001`.

Criterion:

1. Any invocation that begins off `master`, with a dirty worktree, or with local `master` out of synchronization is rejected before repository mutation occurs.

Expected evidence:

1. Automated scenario evidence records each invalid starting state, the rejection result, and an unchanged repository state.

### `SPEC-002` Specification Commitment — Authoritative Next Release Identity

Kind:

1. `Behavior`.

Intent:

1. `Establish`.

Statement:

1. The next release identity is derived solely from refreshed remote release references matching the defined release-reference pattern, and processing stops when that authority is missing or ambiguous or when the derived identity collides with an existing reference.

#### `VER-002` Verification Criterion — Remote-Derived Identity Is Unambiguous and Collision-Free

Covers:

1. `SPEC-002`.

Criterion:

1. A release identity is produced only when refreshed matching remote release references provide one unambiguous authority and the derived identity does not collide with an existing reference.

Expected evidence:

1. Automated scenario evidence covers successful remote-reference derivation and stopped outcomes for missing authority, ambiguous authority, and identity collision.

### `SPEC-003` Specification Commitment — Coherent Post-Release Master State

Kind:

1. `Outcome`.

Intent:

1. `Maintain`.

Statement:

1. After release-branch synchronization, `master` has a coherent post-release development-marker state while concrete artifacts for the released identity remain retained.

#### `VER-003` Verification Criterion — Development Marker and Released Artifacts Coexist

Covers:

1. `SPEC-003`.

Criterion:

1. The completed synchronization leaves `master` carrying the intended post-release development marker and leaves the concrete released artifacts present with their released identity.

Expected evidence:

1. Repository-state evidence identifies the resulting `master` development marker and the retained concrete released artifacts.

### `SPEC-004` Specification Commitment — Bounded Reference-Based Fresh-Task Handoff

Kind:

1. `Deliverable`.

Intent:

1. `Establish`.

Statement:

1. The synchronization produces a bounded fresh-task handoff that identifies authoritative references without copying requirements or introducing facts not supported by those references.

#### `VER-004` Verification Criterion — Handoff Contains References Without Restated Requirements

Covers:

1. `SPEC-004`.

Criterion:

1. The produced fresh-task handoff stays within its defined bounds, points to authoritative references, contains no copied requirements, and contains no unsupported facts.

Expected evidence:

1. Handoff inspection evidence shows its bounded content, resolvable authoritative references, absence of copied requirement text, and absence of claims beyond referenced facts.

## Cross-cutting Verification Criteria

### `VER-005` Verification Criterion — End-to-End Release Synchronization Integrity

Covers:

1. `SPEC-001`.
2. `SPEC-002`.
3. `SPEC-003`.
4. `SPEC-004`.

Criterion:

1. Every successful release-branch synchronization begins from a clean synchronized `master`, uses an unambiguous collision-free identity derived solely from refreshed matching remote release references, leaves `master` in the coherent development-marker state with released artifacts retained, and produces the bounded reference-based fresh-task handoff.

Expected evidence:

1. End-to-end scenario evidence correlates the accepted initial state, authoritative identity derivation, final repository state, retained release artifacts, and resulting handoff for one synchronization run.

Applicability:

1. Release-branch synchronization from preflight through post-release handoff.

### `DEC-001` Architecture Decision — Refreshed Remote Release References Are the Identity Authority

Selected approach:

1. Derive the next release identity exclusively from refreshed remote references matching the defined release-reference pattern, with missing authority, ambiguity, and collisions treated as stopping conditions.

Source spec sections:

1. `SPEC-002`.

### `DEC-002` Architecture Decision — Fresh-Task Handoff Uses Authoritative References

Selected approach:

1. Produce a bounded handoff that directs a fresh task to authoritative references instead of copying requirements or supplementing them with unverified facts.

Source spec sections:

1. `SPEC-004`.

## Role report

No files inspected; no commands or tests run; no files changed; concrete runtime model, profile, and context telemetry was not exposed.
~~~~

### `evidence-green-planning-final`

Raw prompt (verbatim):

~~~~text
Fresh GREEN behavior role. No tools, files, edits, prior outputs, expected mapping, rubric, or reviewer conclusions.

Use exact current plan schema: separate `## Commitment-Disposition Mapping` (`Specification Commitment | Disposition | Implementation Tasks`) and `## Verification-Execution Mapping` (`Verification Criterion | Plan Checks | Expected evidence stage`); `## Implementation Tasks` with literal full headings `### `TASK-NNN` Implementation Task — Title` and fields Dependencies, Implementation, Exit criteria; `## Plan Checks` with literal full headings `### `CHECK-NNN` Plan Check — Title` and fields Covers, Procedure, Expected result, Evidence record, Stage or environment. Use colons, blank lines, numbered items, and backtick every entity ID. CHECK Covers only VER IDs.

Scenario: `SPEC-001` changes current policy owner text and is verified by `VER-001`; `SPEC-002` preserves frozen historical snapshots, is verification-only, and is verified by `VER-002`; `SPEC-003` changes validator behavior under `DEC-001` and is verified by `VER-003`; `SPEC-004` and `VER-004` have an exact frozen later-release assignment. Produce a compact complete plan with current policy implementation, validator/fixture implementation, lifecycle evidence work, separate mappings, preservation without an artificial task, full tasks/checks, and explicit coordination. Do not invent current work for the later-release scope.

Return `## Proposed Markdown excerpt`, complete excerpt, then `## Role report` with exactly: `No files inspected; no commands or tests run; no files changed; concrete runtime model, profile, and context telemetry was not exposed.`
~~~~

Complete raw output:

~~~~md
## Proposed Markdown excerpt

## Scope

This plan implements the current-release work for `SPEC-001` and `SPEC-003`, verifies preservation under `SPEC-002`, and retains the frozen later-release assignment for `SPEC-004` and `VER-004`. It introduces no current implementation or verification work for that later-release scope.

## Commitment-Disposition Mapping

| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` | Implement in the current release by changing the current policy owner text. | `TASK-001` |
| `SPEC-002` | Verification-only preservation of frozen historical snapshots; no implementation change is permitted or required. | None |
| `SPEC-003` | Implement in the current release under `DEC-001` by changing validator behavior and its fixtures. | `TASK-002` |
| `SPEC-004` | Frozen assignment to the later release; excluded from current implementation. | None — later release |

## Verification-Execution Mapping

| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` | `CHECK-001` | Current-release implementation verification |
| `VER-002` | `CHECK-002` | Current-release preservation verification |
| `VER-003` | `CHECK-003` | Current-release validator verification |
| `VER-004` | None in this plan | Later release — exact frozen assignment matching `SPEC-004` |

## Implementation Tasks

### `TASK-001` Implementation Task — Update Current Policy Owner Text

Dependencies:

1. The approved wording and ownership boundary defined by `SPEC-001`.
2. Coordination with `TASK-002` if validator fixtures quote or otherwise depend on the current policy text.

Implementation:

1. Update only the current policy owner text governed by `SPEC-001`.
2. Leave frozen historical snapshots unchanged.
3. Identify any current, non-frozen references that must remain consistent with the revised owner text.

Exit criteria:

1. The current policy presents the owner text required by `SPEC-001`.
2. No frozen historical snapshot has changed.
3. The implementation is ready for `CHECK-001` and `CHECK-002`.

### `TASK-002` Implementation Task — Implement Validator Behavior and Fixtures

Dependencies:

1. `DEC-001` as the controlling validator decision.
2. The finalized current-policy result from `TASK-001` where validator expectations depend on current policy content.

Implementation:

1. Change validator behavior exactly as required by `SPEC-003` and constrained by `DEC-001`.
2. Add or update focused positive and negative fixtures for the changed behavior.
3. Retain coverage proving that frozen historical snapshots remain acceptable and unchanged where applicable.

Exit criteria:

1. Validator behavior conforms to `SPEC-003` and `DEC-001`.
2. Focused fixtures distinguish accepted and rejected cases.
3. Existing unaffected validator coverage remains passing.
4. The implementation is ready for `CHECK-003`.

## Plan Checks

### `CHECK-001` Plan Check — Verify Current Policy Owner Text

Covers:

1. `VER-001`

Procedure:

1. Inspect the implemented current policy at its authoritative location.
2. Confirm that the owner text matches `SPEC-001`.
3. Confirm that all changed non-frozen references remain internally consistent.

Expected result:

1. The current policy contains the required owner text with no stale current references.

Evidence record:

1. Record the inspected authoritative location, the relevant diff, and the verification result in the current work item’s implementation evidence.
2. Link any automated documentation or consistency check output used to support the result.

Stage or environment:

1. Current-release implementation branch after `TASK-001`.

### `CHECK-002` Plan Check — Verify Frozen Historical Snapshot Preservation

Covers:

1. `VER-002`

Procedure:

1. Compare frozen historical snapshot paths and contents against the pre-implementation baseline.
2. Run any repository check that detects unauthorized frozen-snapshot changes.
3. Confirm that neither `TASK-001` nor `TASK-002` altered frozen historical records.

Expected result:

1. All frozen historical snapshots are byte-for-byte unchanged, or otherwise unchanged according to the repository’s canonical freeze comparison.
2. No implementation task is created solely for `SPEC-002`.

Evidence record:

1. Record the baseline reference, compared snapshot set, comparison command or method, and result in the current work item’s implementation evidence.
2. Preserve the comparison output needed for later review or audit.

Stage or environment:

1. Current-release implementation branch after `TASK-001` and `TASK-002`, before final handoff.

### `CHECK-003` Plan Check — Verify Validator Behavior and Fixtures

Covers:

1. `VER-003`

Procedure:

1. Run the focused validator tests and fixtures introduced or updated by `TASK-002`.
2. Run the relevant broader regression suite.
3. Review the observed accepted and rejected cases against `DEC-001`.

Expected result:

1. Focused positive cases pass.
2. Focused negative cases fail for the intended reason.
3. Validator behavior matches `SPEC-003` under `DEC-001`.
4. Relevant regression coverage passes without unauthorized historical-snapshot changes.

Evidence record:

1. Record test commands, fixture identifiers, exit status, and relevant output in the current work item’s implementation evidence.
2. Record any environment-specific variance through the repository’s normal lifecycle mechanism rather than silently changing expected results.

Stage or environment:

1. Current-release implementation branch after `TASK-002`, using the repository’s canonical validator test environment.

## Coordination

1. Complete `TASK-001` before finalizing any `TASK-002` fixture whose expectation depends on current policy content.
2. Keep `SPEC-002` verification-only: `CHECK-002` supplies preservation evidence without creating an artificial implementation task.
3. Execute `CHECK-001` and `CHECK-003` against the completed current-release changes, then execute `CHECK-002` across the combined change set.
4. Store evidence from all current checks in the same lifecycle evidence location, with traceability to the applicable `VER` identifier.
5. Preserve the exact paired later-release assignment of `SPEC-004` and `VER-004`; do not create a current `TASK` or `CHECK` for either item.
6. If current work reveals a need to change the frozen later-release assignment, stop and use the repository’s formal plan-amendment process before expanding scope.

## Role report

No files inspected; no commands or tests run; no files changed; concrete runtime model, profile, and context telemetry was not exposed.
~~~~

### `evidence-refactor-authoring-v5`

Raw prompt (verbatim):

~~~~text
Fresh read-only behavior role. No tools, inspection, edits, prior outputs, expected decomposition, rubric, or reviewer conclusion.

Use this literal schema skeleton, including every colon, backtick, heading level, and em dash:
```markdown
### `SPEC-NNN` Specification Commitment — Title

Kind:

1. `AllowedValue`.

Intent:

1. `AllowedValue`.

Statement:

1. Normative text.

#### `VER-NNN` Verification Criterion — Title

Covers:

1. `SPEC-NNN`.

Criterion:

1. Proposition.

Expected evidence:

1. Evidence.

## Cross-cutting Verification Criteria

### `VER-NNN` Verification Criterion — Title

Covers:

1. `SPEC-NNN`.
2. `SPEC-NNN`.

Criterion:

1. Proposition.

Expected evidence:

1. Evidence.

Applicability:

1. Stage.

### `DEC-NNN` Architecture Decision — Title

Selected approach:

1. Approach.

Source spec sections:

1. `SPEC-NNN`.
```
Kind is one of Outcome, Behavior, Quality, Constraint, Deliverable. Intent is one of Establish, Change, Preserve, Maintain, Prevent. One-target VER is adjacent; multi-target VER appears once cross-cutting. Criteria are propositions; commands belong only in Plan Checks.

Scenario: The old configuration remains accepted as a named regression baseline; a new configuration becomes preferred; telemetry distinguishing old versus new use is currently mentioned only in an Architecture Decision; known command `python scripts/validate_config.py`. Draft a compact excerpt. Make telemetry normative, keep commitments atomic, include a coherence criterion covering preference and telemetry, and omit the command.

Return `## Proposed Markdown excerpt`, complete excerpt, then `## Role report` stating no files inspected, no commands/tests run, no files changed, and runtime telemetry exposure.
~~~~

Complete raw output:

~~~~md
## Proposed Markdown excerpt

### `SPEC-001` Specification Commitment — Legacy Configuration Baseline

Kind:

1. `Behavior`.

Intent:

1. `Preserve`.

Statement:

1. The old configuration remains accepted as the named legacy regression baseline.

#### `VER-001` Verification Criterion — Legacy Baseline Acceptance

Covers:

1. `SPEC-001`.

Criterion:

1. The named legacy regression baseline is accepted without configuration-validation failure.

Expected evidence:

1. Validation results for a representative legacy-baseline configuration.

### `SPEC-002` Specification Commitment — Preferred Configuration

Kind:

1. `Behavior`.

Intent:

1. `Change`.

Statement:

1. The new configuration is the preferred configuration for new use.

#### `VER-002` Verification Criterion — New Configuration Preference

Covers:

1. `SPEC-002`.

Criterion:

1. Default guidance and selection behavior identify the new configuration as preferred.

Expected evidence:

1. Configuration guidance and selection-result evidence showing the new configuration as preferred.

### `SPEC-003` Specification Commitment — Configuration-Use Telemetry

Kind:

1. `Outcome`.

Intent:

1. `Establish`.

Statement:

1. Runtime telemetry distinguishes use of the named legacy regression baseline from use of the preferred new configuration.

#### `VER-003` Verification Criterion — Configuration-Use Classification

Covers:

1. `SPEC-003`.

Criterion:

1. Runtime telemetry classifies legacy-baseline use and preferred-configuration use as distinct values.

Expected evidence:

1. Captured telemetry records for representative uses of both configurations.

## Cross-cutting Verification Criteria

### `VER-004` Verification Criterion — Preference and Telemetry Coherence

Covers:

1. `SPEC-002`.
2. `SPEC-003`.

Criterion:

1. The configuration identified as preferred is represented by the preferred-configuration telemetry classification, while the legacy baseline is represented by the distinct legacy classification.

Expected evidence:

1. Correlated configuration-selection and telemetry records for both configurations.

Applicability:

1. Runtime verification.

### `DEC-001` Architecture Decision — Configuration Transition Strategy

Selected approach:

1. Preserve the old configuration as a named regression baseline, prefer the new configuration, and distinguish their runtime use through telemetry.

Source spec sections:

1. `SPEC-001`.
2. `SPEC-002`.
3. `SPEC-003`.

## Role report

No files inspected. No commands or tests run. No files changed. Runtime telemetry exposure: configuration choice is exposed through distinct legacy-baseline and preferred-configuration classifications.
~~~~

### `evidence-refactor-planning-v5`

Raw prompt (verbatim):

~~~~text
Fresh read-only behavior role. No tools, inspection, edits, prior outputs, expected mapping, rubric, or reviewer conclusion.

Use this literal schema skeleton, including every colon, backtick, section heading, and em dash:
```markdown
## Commitment-Disposition Mapping
| Specification Commitment | Disposition | Implementation Tasks |

## Verification-Execution Mapping
| Verification Criterion | Plan Checks | Expected evidence stage |

## Implementation Tasks
### `TASK-NNN` Implementation Task — Title
Dependencies:
1. ...
Implementation:
1. ...
Exit criteria:
1. ...

## Plan Checks
### `CHECK-NNN` Plan Check — Title
Covers:
1. `VER-NNN`.
Procedure:
1. ...
Expected result:
1. ...
Evidence record:
1. ...
Stage or environment:
1. ...
```
Backtick every entity ID in tables and fields. CHECK Covers only VER IDs. Preservation may be verification-only; no invented deferrals; shared commands may yield separately identified evidence.

Scenario: `SPEC-001` and `SPEC-002` are implemented now with local `VER-001` and `VER-002`; one shared command produces separately identified evidence. `VER-003` is cross-cutting and evaluated only after documentation, the final prerequisite. `SPEC-003` is historical preservation mapped to `VER-004`, verification-only. `SPEC-004` is current-release scope mapped to `VER-005`; convenience deferral is suggested without approved later-release assignment. Draft a compact complete plan excerpt.

Return `## Proposed Markdown excerpt`, complete excerpt, then `## Role report` stating no files inspected, no commands/tests run, no files changed, and runtime telemetry exposure.
~~~~

Complete raw output:

~~~~md
## Proposed Markdown excerpt

## Commitment-Disposition Mapping
| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` | Implement now. | `TASK-001` |
| `SPEC-002` | Implement now. | `TASK-001` |
| `SPEC-003` | Preserve historical behavior; verification-only. | None. |
| `SPEC-004` | Implement in the current release; no approved later-release assignment exists. | `TASK-002` |

## Verification-Execution Mapping
| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` | `CHECK-001` | Local verification after `TASK-001`. |
| `VER-002` | `CHECK-001` | Local verification after `TASK-001`. |
| `VER-003` | `CHECK-002` | Cross-cutting verification after `TASK-003`, the final prerequisite. |
| `VER-004` | `CHECK-003` | Preservation verification after implementation and documentation are complete. |
| `VER-005` | `CHECK-004` | Current-release verification after `TASK-002`. |

## Implementation Tasks
### `TASK-001` Implementation Task — Implement the two local commitments
Dependencies:
1. None.
Implementation:
1. Implement `SPEC-001`.
2. Implement `SPEC-002`.
3. Preserve separately identifiable outputs for `VER-001` and `VER-002` when the shared verification command runs.
Exit criteria:
1. `SPEC-001` and `SPEC-002` are implemented locally.
2. `CHECK-001` can distinguish the evidence for `VER-001` from the evidence for `VER-002`.

### `TASK-002` Implementation Task — Implement the current-release commitment
Dependencies:
1. None.
Implementation:
1. Implement `SPEC-004` in the current release.
2. Do not defer `SPEC-004` without an approved later-release assignment.
Exit criteria:
1. `SPEC-004` is implemented and ready for `CHECK-004`.

### `TASK-003` Implementation Task — Complete required documentation
Dependencies:
1. `TASK-001`.
2. `TASK-002`.
Implementation:
1. Complete the documentation required for the implemented commitments.
2. Treat documentation completion as the final prerequisite for `CHECK-002`.
Exit criteria:
1. Required documentation is complete.
2. All prerequisites for evaluating `VER-003` are satisfied.

## Plan Checks
### `CHECK-001` Plan Check — Verify both local commitments with shared execution
Covers:
1. `VER-001`.
2. `VER-002`.
Procedure:
1. Run the shared local verification command once.
2. Capture and label the result associated with `VER-001`.
3. Capture and label the result associated with `VER-002`.
Expected result:
1. The `VER-001` result passes.
2. The `VER-002` result passes.
Evidence record:
1. A separately identified evidence entry for `VER-001`.
2. A separately identified evidence entry for `VER-002`.
Stage or environment:
1. Local verification after `TASK-001`.

### `CHECK-002` Plan Check — Evaluate the cross-cutting criterion
Covers:
1. `VER-003`.
Procedure:
1. Confirm `TASK-003` is complete.
2. Run the cross-cutting verification across the implemented changes and completed documentation.
Expected result:
1. The integrated implementation and documentation satisfy `VER-003`.
Evidence record:
1. Cross-cutting evidence recorded for `VER-003`.
Stage or environment:
1. Post-documentation verification after the final prerequisite.

### `CHECK-003` Plan Check — Verify historical preservation
Covers:
1. `VER-004`.
Procedure:
1. Exercise or inspect the historical behavior governed by `SPEC-003`.
2. Compare the observed behavior with the preserved baseline.
Expected result:
1. Historical behavior remains unchanged and satisfies `VER-004`.
Evidence record:
1. Preservation evidence recorded for `VER-004`.
Stage or environment:
1. Final verification after implementation and documentation are complete.

### `CHECK-004` Plan Check — Verify current-release scope
Covers:
1. `VER-005`.
Procedure:
1. Verify the implementation of `SPEC-004` in the current-release scope.
2. Confirm no unapproved convenience deferral remains.
Expected result:
1. `SPEC-004` satisfies `VER-005` in the current release.
Evidence record:
1. Current-release evidence recorded for `VER-005`.
Stage or environment:
1. Current-release verification after `TASK-002`.

## Role report

No files were inspected, no commands or tests were run, and no files were changed. Runtime telemetry was not exposed to this role.
~~~~

### `evidence-check-records-v3`

Raw prompt (verbatim):

~~~~text
Fresh read-only behavior role. Do not use tools, inspect files, or edit anything. You receive only this scenario and current public schema; no prior output, expected decomposition, rubric, or reviewer conclusion.

Schema: under `## Plan Checks`, use `### `CHECK-NNN` Plan Check — <title>` with numbered `Covers:`, `Procedure:`, `Expected result:`, `Evidence record:`, `Stage or environment:`. CHECK-001 covers VER-001 compatibility; CHECK-002 covers VER-002 rendering. For every execution record include stable CHECK ID, unique execution instance, stage/environment, actual result, evidence location or inline evidence, and status exactly `pass`, `fail`, or `blocker`. Repeated unchanged procedures reuse the CHECK ID with distinct execution instances. Alternatives require explicit `Any one of` plus equivalence rationale.

Scenario: Stable CHECK identity must span review and later pre-commit executions. The CHECK-001 compatibility procedure covers current and historical scopes but records scope-specific evidence. CHECK-002 may use either `python scripts/render.py --check` or `python scripts/render_alt.py --check`; these are equivalent entry points to the same renderer and rule set. Example execution records must collectively demonstrate pass, fail, and blocker statuses.

Return exactly two sections: (1) the complete proposed Markdown excerpt, and (2) a concise role report stating no files inspected, no commands/tests run, no files changed, and whether runtime model/profile/context telemetry was exposed.
~~~~

Complete raw output:

~~~~md
# 1. Complete Proposed Markdown Excerpt

## Plan Checks

### `CHECK-001` Plan Check — Compatibility across current and historical scopes

1. **Covers:** `VER-001` compatibility for both the current scope and the historical scope.
2. **Procedure:** Run the compatibility procedure against both scopes without changing its steps or identity. Capture separate, scope-specific results and evidence for the current and historical scopes.
3. **Expected result:** Both scopes satisfy the compatibility rules, with independently traceable evidence for each scope.
4. **Evidence record:**
   - **Stable CHECK ID:** `CHECK-001`
   - **Execution instance:** `CHECK-001-review-001`
   - **Stage or environment:** Review / Windows test environment
   - **Actual result:** The current scope passed; the historical scope contained one incompatible legacy fixture.
   - **Evidence location or inline evidence:** Current scope: `evidence/review/check-001-current.txt`; historical scope: `evidence/review/check-001-historical.txt`.
   - **Status:** `fail`
   - **Stable CHECK ID:** `CHECK-001`
   - **Execution instance:** `CHECK-001-precommit-001`
   - **Stage or environment:** Pre-commit / Windows test environment
   - **Actual result:** The unchanged compatibility procedure passed for both current and historical scopes.
   - **Evidence location or inline evidence:** Current scope: `evidence/precommit/check-001-current.txt`; historical scope: `evidence/precommit/check-001-historical.txt`.
   - **Status:** `pass`
5. **Stage or environment:** Review and pre-commit environments; reuse `CHECK-001` for every unchanged execution and assign each run a distinct execution instance.

### `CHECK-002` Plan Check — Renderer rule validation

1. **Covers:** `VER-002` rendering.
2. **Procedure:** **Any one of**:
   - `python scripts/render.py --check`
   - `python scripts/render_alt.py --check`

   **Equivalence rationale:** Both commands are equivalent entry points to the same renderer and apply the same rendering rule set, so either produces evidence for the same plan check.
3. **Expected result:** The selected entry point completes successfully and reports no rendering-rule violations.
4. **Evidence record:**
   - **Stable CHECK ID:** `CHECK-002`
   - **Execution instance:** `CHECK-002-review-001`
   - **Stage or environment:** Review / renderer environment unavailable
   - **Actual result:** The rendering check could not execute because the required renderer dependency was unavailable.
   - **Evidence location or inline evidence:** Inline evidence: `Renderer dependency unavailable; no rendering assertions executed.`
   - **Status:** `blocker`
5. **Stage or environment:** Review and pre-commit environments; reuse `CHECK-002` when either equivalent entry point is executed and assign each run a distinct execution instance.

# 2. Concise Role Report

No files were inspected, no commands or tests were run, and no files were changed. Runtime model/profile/context telemetry was not exposed.
~~~~

## Runtime strategy and residual risk

RED ran in two waves with at most two roles active. Context strategy was curated prompt/artifact path; full-history fork was not used. Runtime model details were not exposed. One missing-report run was invalidated and repeated fresh.

Post-compaction evidence repair used three read-only roles concurrently in three waves, exceeding the frozen cap of two. No repository write was delegated. The operator approved this execution-strategy variance on 2026-07-12; it is recorded in `implementation-notes/variance-log.md`. Across the full implementation there were 28 read-only sub-agent role instances, including invalidated retries and the final reviewer. Behavior roles used fresh curated contexts; the final reviewer used the completed review context. Delegated model generation, resolved profile, and exact context telemetry were not exposed.

## Gate status

Status: `pass — GREEN, REFACTOR, deterministic validation, compatibility, and final semantic re-review complete`
