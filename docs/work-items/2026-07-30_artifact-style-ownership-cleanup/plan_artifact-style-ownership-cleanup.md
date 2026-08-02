# Artifact Style Ownership Cleanup Plan

Work ID: `2026-07-30_artifact-style-ownership-cleanup`
Short ID: `artifact-style-ownership-cleanup`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:architecture`, `module:lifecycle`, `module:quality`, `module:artifact-style`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`
Execution method: `superpowers:executing-plans`
Current planning Codex task: Model/profile, reasoning, and context visibility: `not exposed`.

## Input Artifacts

1. Draft spec: `spec_artifact-style-ownership-cleanup.md`.
2. Architecture input: None; the spec records architecture snapshot status as not applicable.
3. Required snapshots or deltas: `snapshots/test-cases.snapshot.md`.
4. Relevant repository files: `.agents/skills/dev-doc-harness/references/artifact-style.md`, `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`, `.agents/skills/dev-doc-harness/references/policy-architecture.md`, `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md`, generated spec templates, `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, and `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`.
5. Unresolved implementation context to confirm before editing: None identified.

## Traceability approach

Local links connect `SPEC-001` to `TASK-001` and `CHECK-001`, `SPEC-002` to `TASK-001` and `CHECK-002`, and `SPEC-003` to `TASK-002` and `CHECK-003`. This mapping gives deterministic coverage without a requirement-to-task matrix.

## Change surfaces

1. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`: add `rule:quality.plain-language` under Baseline artifact readability.
2. `.agents/skills/dev-doc-harness/references/artifact-style.md`: retain conditional readability rules, remove misplaced or duplicate owners, consolidate traceability, preserve the operator's reflow, and fix the identified doubled space only.
3. `.agents/skills/dev-doc-harness/references/policy-architecture.md`: align module ownership descriptions with the revised owner graph.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md`: reference the Quality plain-language rule.
5. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md` and `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`: generated outputs refreshed from the source block.
6. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: update owner-set and plain-language validator assertions without weakening the active-surface modal check or controlled exclusions.
7. `snapshots/test-cases.snapshot.md`, `changelog/implementation.md`, and `review/independent-implementation-review.md`: validation scenarios, implementation changelog source, and independent-review findings.

## Implementation approach

First make the canonical ownership change, then adjust source templates and validator assertions, regenerate templates, and run focused and full validation. The existing Artifact Style reflow is an input to preserve, not a formatting task to repeat or reverse.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: one bounded independent reviewer after implementation.
2. Fit reason: the coupled owner migration can appear coherent locally while leaving a stale rule reference, generated-template mismatch, or weakened validator exclusion; an independent diff review reduces that risk.
3. Authorization state: Approved by the operator on 2026-07-30.

Sub-agent `independent-policy-reviewer`:

1. Purpose: independently review the completed policy, template, generated-output, validator, and changelog diff for owner drift, enforcement weakening, accidental reformatting, and unmet `SPEC-001` through `SPEC-003` obligations.
2. Context strategy: curated artifacts.
3. Input context: frozen spec and plan, `snapshots/test-cases.snapshot.md`, changed-file diff, `CHECK-001` through `CHECK-003` results, and applicable changelog source.
4. Output artifact: `review/independent-implementation-review.md` with evidence-backed findings, severity, validation path, residual risk, and recommendation.
5. Model policy: `economy-default` from the repository `AGENTS.md`.
6. Model generation: not exposed.
7. Capability tier: balanced.
8. Resolved profile: not exposed.
9. Availability/fallback: use an available independent sub-agent; if unavailable, record the controller's focused self-review limitation and the unavailable-review reason in the completion report.
10. Reasoning effort: medium; the review is bounded to a small policy graph and concrete validation evidence.
11. Selection reason: independent inspection is most valuable after generated outputs and validator assertions are aligned, when stale ownership references are easy for the implementer to miss.
12. Parallel execution: No; review starts after the implementation diff and required checks are complete.
13. Blast radius if wrong: Medium; missed owner or validator drift can make future planning routes inconsistent without directly affecting runtime data.
14. Write authority: None; the reviewer returns findings for the execution controller to record in `review/independent-implementation-review.md`.

## Implementation tasks

### `TASK-001` Consolidate readability-policy ownership

Dependencies: Approved combined planning package and fresh operator authorization.

Interfaces:

1. Consumes: `SPEC-001`, `SPEC-002`, current Artifact Style reflow, and the current Quality Verification Criterion semantics.
2. Produces: one baseline plain-language owner and one conditional Artifact Style traceability owner, reflected in the policy architecture.

Implementation:

1. Add `rule:quality.plain-language` to Quality's owned-rule table and place the author-facing `must`/`should` and concise-wording guidance immediately below `## Baseline artifact readability`.
2. Remove Plain language and `rule:style.plain-language` from Artifact Style; do not copy the validator exception sentence into Quality.
3. Replace Artifact Style's exhaustive ownership-exclusion paragraph with a concise presentation-versus-lifecycle/domain-policy boundary.
4. Remove `rule:style.verification-criterion-placement` and its section, relying on Quality's existing local and cross-cutting Verification Criterion guidance.
5. Consolidate Entity presentation, Proportional traceability, Traceability density, and blank-line guidance into Scannable structure plus one Traceability section owned by the retained `rule:style.trace-density` ID. Retire the duplicate current style rule IDs.
6. Preserve the current one-line paragraph reflow in Artifact Style and correct only the doubled space in `validation  signals` while editing nearby content.
7. Update the policy-architecture catalog so Quality includes baseline plain language and Artifact Style lists only its retained owners.

Exit criteria: `SPEC-001` and `SPEC-002` have one clear owner per rule, and Artifact Style is limited to conditional readability policy.

### `TASK-002` Align templates, validation, and evidence

Dependencies: `TASK-001`.

Interfaces:

1. Consumes: revised Quality and Artifact Style owner graph.
2. Produces: refreshed generated templates, validator coverage for the new owner, evidence snapshot, and implementation changelog source.

Implementation:

1. Change the common commitments-and-verification source block to cite `rule:quality.plain-language`, then run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` to refresh generated templates without direct generated-file editing.
2. Update `test_harness_policy.py` so its plain-language constants and owner assertions point to Quality, remove the definition-only-exception count and exclusion, and retain the synthetic active-surface failure plus frozen-artifact, legal-text, and fixture exclusions.
3. Update the commitment-verification owner test so it no longer requires the retired Artifact Style Verification Criterion or entity-presentation rules and still verifies Quality's canonical commitment and Verification Criterion owners.
4. Create `snapshots/test-cases.snapshot.md` covering plain-language owner migration, no author-facing `shall` exception, retained active-surface modal enforcement, consolidated Artifact Style ownership, template assembly, and historical-artifact preservation.
5. Create `changelog/implementation.md` with a newest-first entry headed `2026-07-30 refactor: artifact-style-ownership-cleanup -- consolidate readability policy`, the required metadata, and concise change bullets.
6. Run `CHECK-001` through `CHECK-003`, then dispatch the approved independent reviewer with the curated review package. Record findings in `review/independent-implementation-review.md`, resolve every load-bearing finding, and inspect the scoped diff before committing one cohesive implementation package.

Exit criteria: `SPEC-003` is satisfied, source blocks and generated templates agree, and validation demonstrates the new owner graph without weakened enforcement.

## Plan checks

### `CHECK-001` Plain-language owner and template assembly

Covers: `VER-001`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` and search current reusable surfaces for `rule:style.plain-language` and `rule:quality.plain-language`.

Expected result: assembly exits 0, no current reusable surface cites the retired style rule, and Quality plus generated spec templates cite the Quality rule.

### `CHECK-002` Artifact Style owner consolidation

Covers: `VER-002`.

Method: Inspect `artifact-style.md`, `durable-planning-quality.md`, and `policy-architecture.md`; run targeted searches for the retired style rule IDs and duplicated Verification Criterion placement prose across current reusable policy.

Expected result: Artifact Style has no separate Plain language or Verification Criterion placement owner, Quality remains the sole semantic owner of Verification Criterion placement, and one retained traceability owner covers the necessary presentation guidance.

### `CHECK-003` Full validator and diff integrity

Covers: `VER-003`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`, `git diff --check`, and review `git status --short` plus the scoped name-only diff.

Expected result: all validator checks and changelog lint pass, no whitespace errors remain, the modal scanner still rejects a synthetic active-surface `shall`, controlled exclusions remain valid, and no unrelated reflow or historical-artifact rewrite appears.

### `CHECK-004` Independent implementation review

Covers: `VER-001`, `VER-002`, `VER-003`.

Method: Dispatch the approved `independent-policy-reviewer` after `CHECK-001` through `CHECK-003` pass, using the curated artifacts named in Model and Sub-agent Strategy. Resolve any load-bearing finding and rerun the affected Plan Checks.

Expected result: `review/independent-implementation-review.md` contains evidence-backed findings and a recommendation; no unresolved high- or medium-severity finding remains before commit.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: artifact-style-ownership-cleanup -- approve policy consolidation` |
| Implementation | `refactor: artifact-style-ownership-cleanup -- consolidate readability policy` |

One cohesive implementation commit is appropriate because policy, templates, generated output, and validator assertions must change together to maintain a valid owner graph.

## Validation and variance

1. `CHECK-001` through `CHECK-003` are all required.
2. Equivalent wording and section ordering may vary when Quality remains the sole plain-language and Verification Criterion semantic owner, Artifact Style remains conditional readability guidance, and validator coverage stays equally strong.
3. Record noteworthy equivalent implementation details in `implementation-notes/variance-log.md` only when useful for later readers.
4. Stop for an amendment and operator approval before widening source reformatting, changing plain-language enforcement scope or exclusions, changing the conditional Artifact Style routing, or modifying historical frozen artifacts.

## Implementation handoff

### Next-stage recommendation

#### Activity

Next activity: implement the approved policy consolidation; First Plan Task: `TASK-001`.

#### Orchestration

Method: `superpowers:executing-plans`; Run in: `new Codex task`; Plan Task reviewers: one operator-approved independent reviewer sub-agent after implementation, serving as the final whole-package reviewer. If unavailable, record the execution controller's focused self-review limitation and unavailable-review reason.

#### Model

Model: balanced tier; Reasoning: medium.

#### Fallbacks and limits

1. Frozen package: approved spec, plan, `snapshots/test-cases.snapshot.md`, and applicable changelog source fragments.
2. Artifact rehydration: load applicable `AGENTS.md`, the repository-local harness, the frozen package, the existing Artifact Style reflow, and the variance stop condition before edits.
3. Fallback: native Codex in a new task only if Superpowers is unavailable; the execution task must follow the applicable independent-review policy before proceeding.
4. Variance stop condition: operator approval is required for the material changes named in Validation and variance.

## Readiness

- [x] Current planning Codex task facts are separate from the Next-stage recommendation.
- [x] Inputs, scope, tasks, checks, documentation, and changelog sources are clear.
- [x] The user-authored Artifact Style reflow is an explicit preserved input.
- [x] The operator-approved independent reviewer has a bounded purpose, curated context, output artifact, model policy, no-write authority, concurrency boundary, and fallback.
- [x] No required decision, placeholder, or ownerless deferral remains.

## Approval

- Status: Approved
- At freeze, relabel the grouped recommendation **Approved next stage** and mirror it in chat.
- Superseded by: None
