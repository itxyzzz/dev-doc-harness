# Commitment Verification Model Test Cases Snapshot

Work ID: `2026-07-11_commitment-verification-model`
Short ID: `commitment-verification-model`
Status: Approved
Harness release: `0.5+`
Schema: `schema:snapshot.test-cases`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:evidence`, `module:freeze-gate`, `rule:lifecycle.immutable-snapshots`, `rule:models.strategy-required`, `rule:evidence.preservation`, `rule:freeze.approval-freeze`

## Purpose

Freeze the raw skill-behavior scenarios, comparison rules, blocking-failure rubric, and structural fixture contracts before current harness guidance or templates change. Implementation uses this snapshot to produce uncontaminated RED, GREEN, REFACTOR, structural, and compatibility evidence.

## Execution Contract

1. The RED control is commit `3954a44`, before commitment-verification implementation edits.
2. RED agents receive only the raw scenario, the named control artifact or template, applicable repository instructions, and a request to produce the requested artifact excerpt. They do not receive this snapshot's assessment rubric, the frozen spec, expected decomposition, earlier outputs, or reviewer conclusions.
3. GREEN agents receive an equivalent fresh scenario plus the revised current skill and template package. They do not receive RED output or assessment conclusions.
4. REFACTOR agents receive the loophole variant for the same scenario family plus the revised package. They do not receive prior outputs or conclusions.
5. Use the approved `economy-default` bounded roles: `balanced` at medium reasoning, two read-only agents at most in parallel. If that tier is unavailable, use the approved `fast/economy` RED fallback or the main-agent high-reasoning GREEN comparison fallback recorded in the plan.
6. Preserve raw prompts and outputs without corrective rewriting in `evidence/skill-behavior-tests.md`. Derived assessments must be visibly separate and cite the source run.
7. Each execution record names its scenario ID, wave, agent role, artifact version or commit, runtime model details when exposed, actual result, evidence location, and pass/fail/blocker status.
8. A failed required report, contaminated context, missing raw output, or unresolved blocking failure stops the affected comparison; it is not converted into a pass by editorial repair.

## Scenario Families

### `scenario:commitment.authoring-decomposition`

Purpose:

1. Test whether a fresh spec author separates independently consequential obligations, architecture choices, conformance propositions, procedures, and lifecycle state.

RED raw scenario:

```text
Use the current repository harness to draft the normative and verification
portion of a small/medium work-item spec for this change:

The harness must move model-transition work to a fresh task when the selected
model generation or profile changes. It should keep same-task continuation
when the current profile remains suitable. If a same-task model switch occurs,
the agent must reread the frozen artifacts and reconcile scope before editing.
The handoff should name the exact frozen artifacts and startup rule, and it
must not claim a precise remaining-context value when the platform does not
expose one. An architecture decision selects a minimal handoff that references
authoritative artifacts instead of copying their requirements. Reviewers must
be able to verify the behavior through policy text, templates, and a fresh-task
scenario.

Return only the proposed spec section. Do not inspect prior work-item outputs
that solve this scenario.
```

GREEN equivalent mutation:

1. Replace the model-transition subject with a release-branch synchronization rule containing independently changeable branch-state, handoff, and no-unexposed-state clauses. Retain one architecture choice and one cross-surface verification proposition.

REFACTOR loophole mutation:

1. Put one prohibition in a `Notes` paragraph, one new obligation only in an Architecture Decision, and one shell command inside the requested evidence description.

Blocking failures:

1. Independently implementable, deferrable, amendable, or verifiable clauses remain combined.
2. A rationale, note, decision, or criterion creates delivery scope absent from a normative statement.
3. A verification proposition contains a concrete procedure or claims a completed result.
4. A mapped architecture decision contains a selected clause unsupported by the normative statements.
5. Required classification facets are missing, overlap, or contradict the documented precedence.
6. A single-target criterion is separated from its commitment, or a multi-target criterion is duplicated rather than defined once.

### `scenario:commitment.plan-asymmetric-coverage`

Purpose:

1. Test whether a fresh planner derives coordinated delivery dispositions and evidence-producing checks without assigning every specification entity both a task and a check.

RED raw scenario:

```text
Use the current repository harness to draft the traceability, task, and
validation portions of an implementation plan from this approved package:

- SPEC-001 changes current reusable templates to a new heading grammar.
- SPEC-002 preserves frozen historical work-item artifacts unchanged.
- SPEC-003 updates operator guidance.
- SPEC-004 is explicitly assigned by the frozen spec to a later release phase.
- DEC-001 selects source-block edits followed by generated-template assembly
  and maps to SPEC-001.
- VER-001 covers SPEC-001 and requires current template structure to conform.
- VER-002 covers SPEC-002 and requires path-scoped historical preservation.
- VER-003 covers SPEC-001 and SPEC-003 and requires terminology coherence.
- VER-004 covers SPEC-004 and is owned by the later release phase.

One assembly command can provide evidence for VER-001 and part of VER-003.
Historical preservation needs inspection but no product edit. The later release
phase is already authorized by the frozen spec. Return only the proposed plan
sections. Do not inspect prior work-item outputs that solve this scenario.
```

GREEN equivalent mutation:

1. Replace templates/operator guidance with policy/validator surfaces, retain one preservation-only commitment, one mapped decision, one frozen later-phase disposition, two local criteria, and one cross-cutting criterion exercised partly by a shared procedure.

REFACTOR loophole mutation:

1. Add a reusable command that supports two semantically distinct criteria, a cross-phase criterion whose final prerequisite lands later, and a tempting but unauthorized convenience deferral.

Blocking failures:

1. The plan uses one symmetric entity-to-task-and-validation matrix instead of separate commitment-disposition and verification-execution mappings.
2. A preservation-only commitment receives an artificial implementation task rather than verification-only treatment.
3. The plan creates a deferral not authorized by the frozen package.
4. `DEC-001` is treated as independent scope or is not consumed under its mapped commitment.
5. A Verification Criterion lacks Plan Check coverage, or a Plan Check lacks Verification Criterion coverage.
6. Shared procedure causes distinct criteria to be merged semantically.
7. A cross-phase criterion is reported passable before its final prerequisite or lacks one owning stage.
8. Tasks and checks are not coordinated through dependencies or stages.

### `scenario:commitment.check-execution-records`

Purpose:

1. Test stable Plan Check identity, alternatives, repeated execution, environment coverage, and completion reporting.

Raw scenario:

```text
Draft plan checks and the expected completion-record shape for these cases:

1. A template assembly check runs once.
2. The full validator runs before review and again before commit without its
   procedure changing.
3. A compatibility inspection runs once against current files and once against
   frozen historical files.
4. Either of two equivalent Markdown render inspections may satisfy one visual
   readability criterion when their equivalence is explained.

The plan must make later execution reproducible and must let a completion
reviewer trace actual evidence back to the conformance propositions. Return
only the checks and completion-record shape.
```

Blocking failures:

1. A check omits `Covers`, `Procedure`, `Expected result`, `Evidence record`, or `Stage or environment`.
2. One `CHECK` ID is reused to mean materially different procedures.
3. Repeated executions overwrite one another or omit execution-instance identity.
4. Alternatives lack an explicit `Any one of` grouping or equivalence rationale.
5. A completion record omits actual result, evidence location, or pass/fail/blocker status.
6. Completion equates task completion with conformance without check evidence.

### `scenario:commitment.current-historical-boundary`

Purpose:

1. Test deterministic enforcement of the new current schema without rewriting or rejecting frozen history.

Fixture contract:

1. Current positive fixtures contain exact full-name `SPEC`, `DEC`, `VER`, `TASK`, and `CHECK` headings, required fields, valid coverage, local/cross-cutting placement, separate plan mappings, and check records.
2. Current negative fixtures independently exercise malformed headings, duplicate IDs, empty or invalid `Covers`, wrong criterion placement, missing mapping rows, orphan checks, missing check fields, and legacy entity headings in current templates.
3. Historical positive fixtures contain frozen `REQ`, `AC`, `T`, and `V` content under `docs/work-items/` and remain outside current-schema enforcement.
4. The validator checks explicit current reusable paths; it must not infer currentness by scanning all Markdown indiscriminately.

Blocking failures:

1. Any declared current negative fixture passes.
2. Any current positive fixture fails.
3. A frozen historical fixture is modified, rejected as current schema, or counted as duplicate current policy.
4. Structural validation attempts to grade atomicity, prose quality, or logical sufficiency of evidence.

## Comparison and Gate Rules

1. RED assessment identifies actual failures from the preserved output; it does not require every listed failure to appear.
2. Before implementation continues past the first GREEN comparison, every blocking failure actually recorded in RED must be corrected and no new blocking classification or traceability failure may appear.
3. REFACTOR passes only when the corrected behavior survives the loophole mutation without receiving the intended decomposition or reviewer conclusions.
4. Structural fixtures pass only when every positive and negative case behaves as declared and historical fixtures remain untouched.
5. A final flagship/high semantic review decides whether terminology, ownership, topology, and compatibility are coherent; deterministic checks are supporting evidence, not a substitute for this review.

## Required Evidence Report Shape

`evidence/skill-behavior-tests.md` must contain:

1. Scope and tested artifact versions.
2. Raw prompts grouped by scenario and wave.
3. Verbatim or clearly delimited raw outputs.
4. RED blocking findings with source citations.
5. GREEN comparison against each recorded RED blocker.
6. REFACTOR loophole findings.
7. Structural fixture commands and results.
8. Final semantic-review findings.
9. Model, context, concurrency, fallback, assumptions, uncertainty, and residual risk.
10. Gate status: pass, fail, or blocked.

## Approval

- Status: Approved
- Superseded by: None
