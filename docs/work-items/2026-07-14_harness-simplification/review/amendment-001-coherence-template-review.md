# Amendment 001 coherence and template review

Work ID: `2026-07-14_harness-simplification`
Amendment: `AMD-001`
Review status: Approved

## Scope

Read-only final re-review of the staged Amendment 001 candidate. The review
checked that the amendment preserves the frozen simplification decisions: no
mandatory commitment classification, complete mapping, or per-procedure
approval mechanism; concise optional verification applicability/ownership;
clear multi-check semantics; generated-template synchronization; and coherent
validation evidence.

## Files inspected

- `plan_amendment-001_coherence-template-retention_harness-simplification.md`
- `spec_harness-simplification.md`, `plan_harness-simplification.md`, and all
  frozen snapshot files under `snapshots/`
- `evidence/amendment-001-validation.md`
- The current uncommitted diff, including the README, template source blocks,
  assembled templates, policy validator, and amendment changelog fragment

## Commands and checks

| Check | Result |
| --- | --- |
| `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exit 0: all 30 policy checks passed, including `tracking.work-items`. |
| `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` | Exit 0: all assembled templates are current. |
| Frozen fixed-manifest PowerShell count command | Exit 0: 21 files, 1,843 nonblank lines, and 18,942 words; all per-file rows and aggregates match the evidence. |
| `git diff --cached --check` | Exit 0 with no output. |
| `python -X utf8 .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint` | Exit 0 with no output. |
| Manual staged/current diff and source/template inspection | Completed; findings below. |

## Findings

### Resolved — Plan Check cue offers both approved modes

`assets/templates/blocks/plan.050.common.task-plan.md` now asks whether all
checks are required or whether they are equivalent alternatives, and requires
an equivalence reason for the latter. Both assembled plan consumers contain
the same cue. The focused validator assertion now requires the two modes and
their reason, while fixtures keep them distinct.

This resolves the prior P1 finding without restoring per-procedure approval.

### Resolved — Tracking-aware policy validator result now reproduces

With the work-item artifacts staged, the policy validator exits 0 and all 30
checks pass, including `tracking.work-items`. This resolves the prior P1
finding about the recorded validator result.

### Resolved — Fixed-manifest evidence matches the final literal rows

The corrected cue adds one nonblank line to its source block and each of its
two assembled plan consumers. The frozen count command now returns 1,843
nonblank lines and 18,942 words, for deltas of -292 lines and -5,313 words
from the frozen baseline. The evidence now records the matching final rows:

- `plan.050.common.task-plan.md`: `18` / `119`.
- `small-medium-work-item-plan.md`: `111` / `975`.
- `large-phased-work-item-phase-plan.md`: `138` / `1,272`.

The literal rows and aggregate now agree, satisfying Amendment TASK-003's
fixed-manifest evidence requirement.

### Resolved — Staged whitespace check is clean

`git diff --cached --check` now exits 0 with no output. This resolves the
prior staged-whitespace finding.

## Confirmed behavior

- Both readiness source blocks and their assembled small/large specification
  templates remove mandatory `classified` wording while retaining atomic and
  bounded commitments.
- The README uses the canonical materiality rule: equivalent implementation or
  validation changes that retain scope, outcome, and evidence purpose are
  allowed variance; only material change or invalid evidence requires an
  amendment. It does not restore per-procedure approval.
- The verification applicability/owning-phase cue is short and explicitly
  optional in the source block and both assembled specification templates. It
  supplies a conditional cross-phase ownership prompt without a universal
  field.
- Generated specification and plan templates are synchronized with their
  changed source blocks. No mandatory classification, mapping, or
  per-procedure approval mechanics were reintroduced.
- The actual fixed-manifest measurement remains below the frozen baseline by
  292 nonblank lines and 5,313 words.

## Assumptions and residual risk

- This review treats the staged candidate as the implementation candidate and
  preserves all frozen artifacts as historical evidence.
- The validation commands establish current policy, assembly, changelog,
  staged-whitespace, and fixed-manifest consistency.
- The optional ownership cue uses `when useful` rather than the amendment's
  example wording `omit when universal`; it is sufficiently conditional, but
  a future validator should keep that distinction from becoming a mandatory
  schema.

## Model and fallback details

- Policy: active repository `economy-default`.
- Review strategy: delegated, read-only reviewer using `curated artifacts`;
  the approved allocation is `balanced` / `high`.
- Model generation, resolved profile, runtime reasoning effort, and context
  visibility: not exposed.
- Availability/fallback: reviewer available; no fallback exercised. If
  unavailable, the orchestration thread performs the same read-only review
  against these artifacts.

## Recommended next step

The amendment candidate is approved. Stage this final review-report update,
then commit the approved implementation and amendment-owned evidence using the
planned subject.
