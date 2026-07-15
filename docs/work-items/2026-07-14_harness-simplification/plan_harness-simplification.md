# Harness Simplification Implementation Plan

Work ID: `2026-07-14_harness-simplification`
Short ID: `harness-simplification`
Status: Approved
Harness release: `0.6+`
Schema: `schema:plan.small-medium`

**Goal:** Reduce active harness prose and unnecessary process while retaining
useful IDs, focused validation, one real freeze gate, and material-change
control.

**Architecture:** Canonical policy owns lifecycle, traceability, and style
rules once. Templates use short cues and preserve IDs without forcing complete
matrices. The validator protects a few concrete workflow scenarios rather than
enforcing a general legal-document grammar.

**Tech stack:** Markdown policy and template source blocks; Python standard
library validator and assembler; PowerShell/Git inspection; read-only reviewer
reports.

## Global constraints

1. Do not edit frozen work items or historical evidence.
2. Retain `SPEC`, `VER`, `TASK`, `CHECK`, `DEC`, and variance ID families.
3. Keep complete mappings optional and benefit-based.
4. Keep one post-freeze start instruction and no implementation-task approval
   checkpoints.
5. Use variance notes for noteworthy permitted drift; reserve amendments for
   material changes.
6. The changed active author-facing Markdown surfaces must be net smaller by
   nonblank lines and words unless an approved material variance records why.
7. Use the source-block assembler for generated templates.
8. Update only the README's copy-ready global-bootstrap section; the operator
   owns any later copy into `C:\Users\1\.codex\AGENTS.md`.
9. Do not change `references/planning-freeze-gates.md` or the README workflow
   diagram. Preserve separate gates for actual anchor, phase-plan, and amendment
   packages.

## Input artifacts

1. Draft spec: `spec_harness-simplification.md`.
2. Architecture snapshot: `snapshots/architecture.snapshot.md`.
3. Test cases: `snapshots/test-cases.snapshot.md`.
4. Active authoring baseline: `snapshots/active-authoring-baseline.md`.
5. README copy-ready global bootstrap and repository guidance: `README.md`,
   `AGENTS.md`, and `.agents/skills/dev-doc-harness/SKILL.md`.
6. Canonical sources: `references/artifact-contract.md`,
   `references/planning-freeze-gates.md`, `references/durable-planning-quality.md`,
   `references/artifact-style.md`, `references/context-and-quality-gates.md`, and
   `references/subagent-model-policy.md`.
7. Templates, assembler, and validator under
   `.agents/skills/dev-doc-harness/assets/templates/` and `scripts/`.

## Traceability approach

Local links are the default for this plan. The explicit mapping below exists
because this is a cross-surface policy change with six independent outcomes;
it lets the implementation reviewer check that no outcome was silently lost.

| Specification commitment | Implementation tasks | Verification |
|---|---|---|
| `SPEC-001` Useful IDs, lighter presentation | `TASK-002`, `TASK-003` | `CHECK-002` |
| `SPEC-002` Benefit-based mappings | `TASK-002`, `TASK-003`, `TASK-004` | `CHECK-003` |
| `SPEC-003` One approval boundary | `TASK-002`, `TASK-004` | `CHECK-004` |
| `SPEC-004` Variance before amendment | `TASK-002`, `TASK-003`, `TASK-004` | `CHECK-005` |
| `SPEC-005` Plain centralized guidance | `TASK-002`, `TASK-003`, `TASK-004` | `CHECK-001`, `CHECK-004` |
| `SPEC-006` Measured shrinkage | `TASK-001`, `TASK-005` | `CHECK-006` |

## Change surfaces

1. `README.md`: update only its copy-ready global `AGENTS.md` bootstrap so it
   defers repository-specific lifecycle details to the selected local harness;
   leave the README workflow diagram unchanged.
2. `.agents/skills/dev-doc-harness/SKILL.md`: concise route and ownership
   wording; no duplicate lifecycle procedure.
3. `references/artifact-contract.md`, `context-and-quality-gates.md`,
   `durable-planning-quality.md`, and
   `artifact-style.md`: simplify authority, mapping, check, variance, and
   operator-language rules in their canonical owners.
4. `references/subagent-model-policy.md`: retain focused independent review and
   remove only duplicated approval/continuity wording that belongs elsewhere.
5. Template source blocks: `spec.030.common.commitments-verification.md`,
   `plan.020.common.traceability-approach-surfaces.md`,
   `plan.050.common.task-plan.md`,
   `plan.070.common.validation-variance-freeze.md`, and the applicable header,
   handoff, amendment, and variance-log blocks.
6. Generated templates and `scripts/test_harness_policy.py`: regenerate outputs
   and protect the chosen concise policy with structural and scenario checks.
7. `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`:
   explain the simpler operator flow without duplicating canonical policy.

## Model and sub-agent strategy

Model generation: `not exposed`. Resolved profile: `not exposed`. Baseline:
`balanced` tier, medium reasoning, bounded delegated reviewer orchestration,
and same-task execution if the frozen package can be rehydrated. Context
visibility: `not exposed`. Artifact rehydration: `Yes`, because execution must
read the frozen package and current target surfaces. Availability/fallback: use
the nearest available balanced/medium profile; use fast/economy medium only for
mechanical validation and have the orchestration thread perform an unavailable
reviewer role. Fit: medium complexity with a repository-wide policy blast radius;
one read-only reviewer improves integration quality without a second planning
hierarchy. Recommended change: none unless the documented reviewer escalation
trigger occurs.

`review-001` runs after validation with curated artifacts and a `balanced` /
high allocation. It reviews only readability, duplicate authority rules,
mapping usefulness, variance thresholds, and changed scenario coverage. Its
model policy is `economy-default`; generation and resolved profile are `not
exposed` unless the runtime exposes them. Its blast radius is medium and it does
not run in parallel with repository writes.

`review-002` is allowed only if `review-001` leaves a high-impact conflict about
safety, global instruction precedence, or lost verification evidence. It uses a
`flagship` / medium allocation with the unresolved finding as its written
escalation reason. No reviewer writes repository files.

## Implementation tasks

### `TASK-001` Establish the simplification baseline and failing scenarios

Dependencies:

1. Frozen package and `snapshots/test-cases.snapshot.md`.

Implementation:

1. Run the fixed manifest command in
   `snapshots/active-authoring-baseline.md` and record its per-file and aggregate
   nonblank-line and word counts before editing. Do not add, remove, or replace
   a manifest path without an approved material variance.
2. Extend `scripts/test_harness_policy.py` with focused failing assertions for:
   optional mappings, one freeze/start boundary, allowed equivalent check
   adjustments, material-change amendment routing, and a README bootstrap that
   defers ordinary freeze details to local policy.
3. Keep fixtures narrow and scenario-based. Do not add a subjective prose
   grader, repository-wide scan, or a new permanent framework.
4. Run the focused validator against the pre-change state and record its expected
   failures in the execution record.

Exit criteria:

1. The baseline is reproducible and each planned behavior has a deterministic
   failing assertion or documented manual scenario.

### `TASK-002` Simplify canonical lifecycle and variance policy

Dependencies:

1. `TASK-001`.

Implementation:

1. In `artifact-contract.md`, narrow amendment triggers to material outcome,
   architecture/API/data/security/privacy/compliance, or invalidated evidence;
   state that noteworthy allowed local drift uses the variance log.
2. Leave `planning-freeze-gates.md` unchanged. In other lifecycle consumers,
   remove wording that implies pauses inside approved implementation, while
   preserving the existing one-freeze/one-fresh-start meaning.
3. In `durable-planning-quality.md`, retain the entity concepts but remove exact
   heading/classification, conjunctive-default, and frozen-procedure wording
   that does not change a decision. Make classification optional and render it
   as one compact `Constraint · Preserve`-style line when used. Define Plan
   Checks by evidence purpose.
4. In `artifact-style.md`, add concise human-first wording guidance and make
   repeated full entity names optional after first definition.
5. In `subagent-model-policy.md`, preserve the independent focused reviewer
   default and move or delete duplicated lifecycle/approval prose rather than
   creating a competing rule.

Exit criteria:

1. Each canonical owner has one concise rule, and ordinary execution no longer
   implies per-task authorization or an amendment for an equivalent procedure.

### `TASK-003` Make templates proportional and regenerate outputs

Dependencies:

1. `TASK-002`.

Implementation:

1. Update the commitment and plan source blocks so IDs and short titles remain,
   while optional classification fields, full-name repetition, mandatory
   complete mappings, and execution-record boilerplate are removed or made
   conditional on their benefit.
2. Replace handoff and readiness boilerplate with short references to the
   canonical freeze and variance rules.
3. Update amendment and variance templates so the variance log clearly handles
   noteworthy allowed drift and an amendment states the material change that
   blocks the approved plan.
4. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`.
5. Inspect every generated template changed by the assembler and remove output
   text that merely duplicates its source policy.

Exit criteria:

1. Generated templates are current, keep readable identifiers, and no longer
   demand a large mapping or record structure without a stated benefit.

### `TASK-004` Resolve instruction layering and update operator documentation

Dependencies:

1. `TASK-002` and `TASK-003`.

Implementation:

1. Update the repository router only where it needs a short route to the
   canonical owners.
2. Update only the README's copy-ready global `AGENTS.md` bootstrap. It must say
   that a repository-local harness owns ordinary freeze/changelog details and
   must not prescribe a root-changelog update or another model-policy
   confirmation at every local freeze.
3. Update the package operator note with a compact explanation:
   one freeze/start boundary, proportional mappings, variance for allowed drift,
   amendments for material drift, and focused reviewers.

Exit criteria:

1. Active instruction layers have no contradictory ordinary-freeze rule, or the
   external blocker is explicit and the repository change remains truthful.

### `TASK-005` Validate shrinkage, review, and record delivery evidence

Dependencies:

1. `TASK-003` and `TASK-004`.

Implementation:

1. Run the full policy validator and the assembler freshness check.
2. Run the scenario checks from the snapshot: concise local links, justified
   mapping, uninterrupted approved execution, allowed variance, material
   amendment, and README-bootstrap/local-policy agreement.
3. Re-run the identical fixed manifest command and compare per-file and
   aggregate nonblank-line and word totals. Treat a non-reduction as material
   variance requiring operator direction.
4. Run `review-001` with the curated diff and validation evidence. Resolve its
   blocking findings, then run `review-002` only if its defined trigger occurs.
5. Create the testing-guide and operator-manual deltas, implementation
   changelog fragment, and reviewer report. Create or append a variance log
   only if actual noteworthy permitted drift occurs. Record exact commands,
   results, residual risk, and external-guidance status.

Exit criteria:

1. Validation passes, active prose is demonstrably smaller, no blocking reviewer
   finding remains, and evidence clearly distinguishes permitted variance from
   an amendment.

## Plan checks

### `CHECK-001` Validate canonical ownership and instruction agreement

Procedure:

1. Run the focused policy-validator assertions for canonical rule ownership,
   short consumer routes, and README-bootstrap/local-policy agreement.

Expected result:

1. The assertions pass and the README bootstrap gives no conflicting ordinary
   freeze/changelog instruction.

### `CHECK-002` Verify concise ID presentation

Procedure:

1. Inspect changed source blocks and generated templates for retained ID
   families, short titles, and removal of mandatory full-name repetition or
   unused classification fields.

Expected result:

1. IDs remain visible and search-friendly; no removed formal field is required
   by the validator.

### `CHECK-003` Verify proportional mappings

Procedure:

1. Run the focused scenario assertions for a small plan using local links and a
   larger plan that records a concrete reason for a mapping.

Expected result:

1. Both forms pass, while an unjustified mandatory mapping is not required.

### `CHECK-004` Verify uninterrupted approved execution

Procedure:

1. Run the scenario assertion and inspect the freeze/handoff text for one
   freeze/start boundary and explicit continuation through planned tasks.

Expected result:

1. The rule asks for confirmation only at the package boundary or for external,
   destructive, costly, or material scope-expanding actions.

### `CHECK-005` Verify variance and amendment routing

Procedure:

1. Run the equivalent-validation-adjustment and material-outcome-change
   scenarios.

Expected result:

1. The equivalent adjustment produces an allowed variance route; the material
   change produces an amendment-and-approval route.

### `CHECK-006` Verify measured net reduction

Procedure:

1. Run the exact manifest command in
   `snapshots/active-authoring-baseline.md` before and after the change, then
   review its per-file and aggregate output with the changed active Markdown
   diff.

Expected result:

1. Both aggregate totals decrease and no manifest path is silently excluded.
   Any exception is explicitly recorded as material
   variance and has operator approval before completion.

## Planned commits

1. Planning approval: `plan: harness-simplification -- approve leaner agent workflow`.
2. Implementation: `docs: harness-simplification -- reduce policy and mapping overhead`.

## Variance handling

1. Before freeze, edit this draft directly for feedback.
2. After freeze, use the variance log for noteworthy permitted local drift.
3. Stop for an amendment only when `SPEC-004`'s material threshold is met.

## Next-task handoff

1. Planning shape: `combined small/medium`.
2. Frozen package after approval: `spec_harness-simplification.md`, this plan,
   `snapshots/architecture.snapshot.md`, `snapshots/test-cases.snapshot.md`,
   and `snapshots/active-authoring-baseline.md`.
3. Next activity: complete `TASK-001` through `TASK-005` in order.
4. First activity: establish the baseline and focused failing scenarios.
5. Reviewer policy: run `review-001` after validation; escalate to `review-002`
   only for its documented unresolved high-impact trigger.

## Approval

- Status: Approved
- Superseded by: None
