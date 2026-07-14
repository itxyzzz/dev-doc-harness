# Plan Amendment 001: Coherence and Template Retention

Work ID: `2026-07-14_harness-simplification`
Short ID: `harness-simplification`
Status: Approved
Harness release: `0.6+`
Schema: `schema:plan.amendment`
Policy references: `module:lifecycle`, `module:naming`, `module:freeze-gate`, `module:quality`, `module:models`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-001`
- Files: `spec_harness-simplification.md`, `plan_harness-simplification.md`, and `snapshots/architecture.snapshot.md`
- Sections or tasks: `SPEC-001` through `SPEC-006`, `TASK-002` through `TASK-005`, `CHECK-001` through `CHECK-006`, and `DEC-001` through `DEC-003`
- Original instruction: Simplify current authoring surfaces while retaining stable IDs, proportional traceability, one freeze/start boundary, evidence-purpose variance handling, and a measurable reduction in active prose.

## Discovered issue

The completed implementation has two current instruction conflicts and two
small template omissions that weaken the approved outcome:

1. Both specification readiness blocks still require commitments to be
   classified, although `SPEC-001` and `rule:quality.specification-commitments`
   make classification optional.
2. The README says every change to a Specification Commitment, Verification
   Criterion, or Plan Check needs an amendment. This conflicts with `SPEC-004`:
   an equivalent implementation or validation adjustment that preserves scope,
   outcome, and evidence purpose is allowed variance.
3. A Verification Criterion template no longer prompts an author to identify a
   non-universal condition, environment, or owning phase. Cross-phase evidence
   can therefore lack a clear owner.
4. A Plan Check template no longer asks whether several checks for one criterion
   are all required or are documented equivalent alternatives. This can make
   evidence expectations ambiguous.

The delivery record also omits the fixed manifest's required per-file rows and
records final aggregate counts that do not reproduce from the committed tree.
The frozen earlier report and delta remain historical evidence and will not be
rewritten.

## Proposed change

1. Change both specification readiness source blocks to require commitments to
   be atomic and bounded, without requiring classification. Regenerate their
   small and large specification consumers through the source-block assembler.
2. Replace the README drift summary with the canonical materiality rule:
   amendments cover material outcome, architecture, interface, data, security,
   privacy, compliance, scope, or invalidated evidence; an equivalent method
   that retains scope, outcome, and evidence purpose is allowed variance.
3. Add one concise optional cue after each Verification Criterion's expected
   evidence: `Applicability/owner: <condition, environment, or owning phase;
   omit when universal>.`
4. Add one concise Plan Check cue: when several checks support one criterion,
   state whether all are required; label equivalent alternatives and explain
   why they are equivalent.
5. Add focused validator assertions and fixtures for all four instructions,
   including generated-template coverage, a cross-phase owner cue, and a
   required-versus-equivalent multi-check distinction.
6. Add a new amendment validation record containing the literal fixed-manifest
   per-file rows, baseline and final aggregates, commands, results, review
   metadata, assumptions, residual risk, and recommended next step. It will
   reconcile the old aggregate claim without changing frozen evidence.
7. Remove the two README trailing-space errors found by `git diff --check`.

## Impact assessment

| Area | Impact |
|---|---|
| Outcome and scope | Restores four concise guidance cues required to make the approved simplification coherent; no return to mandatory mapping, formal classification, or execution-record boilerplate. |
| Verification evidence | Adds deterministic coverage for README materiality, optional classification, verification ownership, and multi-check semantics. |
| Templates | Changes three source blocks and their assembled small/large specification and small/large plan consumers. |
| API, data, migration, security, privacy, compliance | None. |
| Documentation | Updates README and creates new amendment-owned validation and review evidence; prior frozen reports, deltas, snapshots, and changelog fragments remain unchanged. |
| Size measure | The fixed manifest remains unchanged. The final aggregate may increase slightly from the restored cues but must remain below the verified baseline of 2,135 nonblank lines and 24,255 words. |
| Risk | Restored prompts could reintroduce formality. The exact wording is optional and conditional, and focused scenarios prohibit treating the restored cues as universal mandatory schemas. |

## Model and sub-agent strategy

Model policy: active repository `economy-default`.

1. Model generation and resolved profile: `not exposed`.
2. Capability tier and reasoning effort: `balanced` / `medium` for bounded
   source, template, documentation, and validator changes.
3. Orchestration mode: `bounded delegated sub-agents`.
4. Execution continuity: `same task`; the implementation thread re-reads this
   approved amendment, the frozen original package, current source blocks, and
   the validator before editing.
5. Context visibility: `not exposed`.
6. Artifact rehydration required: `Yes`, because this amendment changes
   current authoring policy while preserving frozen evidence.
7. Availability/fallback: use the nearest balanced/medium runtime; if the
   reviewer is unavailable, the orchestration thread performs the same
   read-only review and records that fallback.

Sub-agent `amendment-review-001`:

1. Purpose: independently review the completed diff for accidental return of
   mandatory classification, mapping, or per-procedure approval mechanics, and
   verify the two restored cues remain concise and correctly scoped.
2. Context strategy: `curated artifacts`.
3. Input context: this amendment, the frozen original package, current diff,
   validator output, assembly check, and amendment validation record.
4. Output artifact: `review/amendment-001-coherence-template-review.md`.
5. Capability tier and reasoning effort: `balanced` / `high`.
6. Parallel execution: no; it runs after implementation validation.
7. Blast radius if wrong: medium; an incorrect recommendation could recreate
   the policy burden this work intentionally removed.

## Implementation plan

### `TASK-001` Add failing regression coverage for the four gaps

Files:

1. Modify `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Steps:

1. Add focused assertions that both readiness source blocks and their generated
   specification templates do not require commitments to be `classified`.
2. Add a README assertion that accepts the canonical equivalent-evidence
   variance route and rejects the old unconditional Plan Check amendment list.
3. Add source-block and assembled-template assertions for the optional
   Verification Criterion applicability/owner cue and the multi-check
   required-versus-equivalent cue.
4. Add compact positive and negative fixtures: a cross-phase criterion with an
   owning phase passes; an all-required two-check criterion differs from an
   equivalent-alternative pair with an explicit equivalence reason.
5. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
   before changing policy or templates. Expected result: failure only for the
   four missing cues or the README conflict.

Exit criteria:

1. The new assertions fail on the current committed state for the intended
   reasons and do not require full mapping tables, `Kind:`/`Intent:` fields, or
   exact frozen command strings.

### `TASK-002` Align current policy summaries and template source blocks

Files:

1. Modify `README.md`.
2. Modify `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.small.readiness-approval.md`.
3. Modify `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.large.readiness-approval.md`.
4. Modify `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md`.
5. Modify `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md`.

Steps:

1. Replace the README's unconditional commitment/criterion/check amendment
   list with the canonical evidence-purpose materiality rule from
   `artifact-contract.md`.
2. Remove `classified` from both readiness checklists while retaining the
   atomic, bounded, statement-contained-obligation check.
3. Add the optional applicability/owner cue to local and cross-cutting
   Verification Criterion examples without making it a required field.
4. Add the one-sentence multi-check cue to the Plan Checks section without
   restoring execution-instance, stage, or evidence-record boilerplate.
5. Remove the two whitespace errors reported by `git diff --check`.

Exit criteria:

1. Current human-facing guidance agrees with the canonical materiality rule,
   and the restored template prompts are optional, concise, and do not expand
   scope beyond the four reviewed gaps.

### `TASK-003` Assemble, validate, and create amendment-owned evidence

Files:

1. Regenerate affected assembled templates through
   `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`.
2. Create `docs/work-items/2026-07-14_harness-simplification/evidence/amendment-001-validation.md`.
3. Create `docs/work-items/2026-07-14_harness-simplification/review/amendment-001-coherence-template-review.md`.
4. Create `docs/work-items/2026-07-14_harness-simplification/changelog/amendment-001.md`.

Steps:

1. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`.
2. Run `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, then
   `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.
   Expected result: all checks pass and all assembled templates are current.
3. Run the exact counting command frozen in
   `snapshots/active-authoring-baseline.md`. Copy all 21 per-file rows, both
   final aggregates, the original verified baseline (2,135 lines and 24,255
   words), and the before/after deltas into the new evidence record.
4. Run `git diff --check`. Expected result: no output.
5. Run `amendment-review-001` with the curated artifacts listed above. Record
   its required scope, inspected files, commands, assumptions, residual risk,
   recommended next step, model/fallback details, and all findings in the new
   review record. Resolve any blocking finding before the implementation
   commit.
6. Add the implementation changelog entry only after the implementation
   subject is final, then run
   `python -X utf8 .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`.

Exit criteria:

1. The current implementation is reproducibly validated, the fixed size
   manifest is fully recorded without changing historical evidence, no
   blocking review finding remains, and the changelog fragment is valid.

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: Operator approval of the staged amendment package in this Codex task on 2026-07-14.
- Superseded by: None

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Amendment approval | `amendment 001: harness-simplification -- restore focused template cues` | `2026-07-14_harness-simplification -- restore focused template cues` | Approval commit for this amendment only. |
| Amended implementation | `docs: harness-simplification -- align policy and template cues` | `2026-07-14_harness-simplification -- align policy and template cues` | Current policy, source blocks, generated templates, validator, and amendment-owned evidence. |

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until this amendment is explicitly approved, committed, and followed by a fresh instruction to begin `TASK-001`.
