# Plain-language Artifact Policy Spec

Work ID: `2026-07-14_plain-language-artifacts`
Short ID: `plain-language-artifacts`
Status: Approved
Harness release: `0.6+`
Schema: `schema:spec.small-medium`
Planning shape: `combined small/medium`
Policy references: `module:architecture`, `module:lifecycle`, `module:quality`, `module:artifact-style`, `module:models`, `module:freeze-gate`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.immutable-snapshots`, `rule:quality.specification-commitments`, `rule:style.template-prompts`, `rule:models.strategy-required`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`

## Goal

Restore a direct, readable modal-language policy so current harness guidance and every newly authored durable artifact use ordinary `must` or `should` wording instead of legalistic requirement language.

## Source and intent

The operator observed that new specifications started using legalistic modal wording after the commitment-and-verification model became current. Repository inspection found the earlier prohibition only in frozen historical work items; current reusable policy, required routing, template prompts, and validator coverage do not preserve it.

The desired outcome is a durable three-layer control:

1. One canonical style rule defines the required modal voice.
2. The required drafting route and shared commitment-template block expose that rule when artifacts are authored.
3. The policy validator detects regression in active guidance and templates without rewriting history or legal text.

## Scope boundary

### In scope

1. Add one canonical artifact-style rule: use `must` for binding obligations and `should` for recommendations; do not use legalistic requirement language in author-facing current guidance or newly authored durable artifacts.
2. Make `module:artifact-style` a required route for small/medium spec and plan drafting, not only a conditional readability route.
3. Add a compact prompt to the shared commitment-and-verification source block; regenerate only the small/medium and large/phased specification templates that consume it.
4. Extend the deterministic harness policy validator to protect the canonical owner, required route, prompt, generated-template parity, and scoped prose scan.
5. Record the planning, implementation, validation, and variance evidence required by the harness, including the root changelog update required by repository instructions at the applicable freeze gate.

### Non-scope

1. Do not edit frozen work-item specs, plans, snapshots, evidence, reports, or changelog fragments.
2. Do not edit `LICENSE` or scan it as an authoring-policy target.
3. Do not change the semantics of Specification Commitments, Verification Criteria, Plan Checks, lifecycle gates, or immutable-snapshot policy.
4. Do not build a general prose-quality linter or enforce a writing style outside the targeted modal language.
5. Do not add a second canonical style owner, a new lifecycle gate, or a new template assembly mechanism.

### Assumptions

1. A single explicit exception may quote the prohibited word while defining the rule; validation treats that canonical definition and test fixtures as controlled exceptions rather than authoring examples.
2. Current reusable authoring surfaces are root `AGENTS.md` plus the active Dev Doc Harness package. Frozen `docs/work-items/**` content remains excluded.
3. The existing source-block assembler remains the only supported route for generated template changes.

### Open questions

1. None. The operator approved the three-layer design and the historical and license exclusions.

## Specification Commitments and Local Verification Criteria

### `SPEC-001` Specification Commitment — Define ordinary modal language

Kind: `Constraint`

Intent: `Establish`

Concerns: `Authoring`, `Style`, `Compatibility`

Statement:

1. Current harness authoring guidance and newly created durable artifacts must express binding obligations with `must` and recommendations with `should`.
2. Current harness authoring guidance and newly created durable artifacts must not use the prohibited legalistic modal, except where a validator fixture identifies the prohibited form without presenting it as authoring language.
3. The rule must be owned by `module:artifact-style` and must not redefine lifecycle or conformance semantics.

Rationale:

1. Ordinary language is easier to review and avoids the waterfall or legalistic tone that the operator rejected.

#### `VER-001` Verification Criterion — Canonical guidance states and routes the rule

Covers:

1. `SPEC-001`.

Criterion:

1. The current style owner states the modal-language rule, and the small/medium drafting route requires that owner before a spec or plan is authored.

Expected evidence:

1. A focused validator assertion and inspected current policy text identify the canonical rule and required route.

Applicability:

1. Current harness policy after the implementation commit.

### `SPEC-002` Specification Commitment — Prompt the intended artifact voice

Kind: `Behavior`

Intent: `Change`

Concerns: `Templates`, `Assembly`, `Specification`

Statement:

1. The shared commitment-and-verification source block must prompt authors to use `must` for binding statements and `should` for advice.
2. Every generated specification template that consumes that block must include the prompt after assembly.
3. The prompt must remain concise and route reusable semantics to the canonical style rule rather than duplicating its policy text.

#### `VER-002` Verification Criterion — Generated specification templates preserve the prompt

Covers:

1. `SPEC-002`.

Criterion:

1. The shared source block and both consuming generated specification templates contain the same compact modal-language prompt, and template assembly reports them current.

Expected evidence:

1. Focused validator output and a successful assembler `--check` result.

Applicability:

1. Current generated templates after the implementation commit.

### `SPEC-003` Specification Commitment — Protect the policy without rewriting history

Kind: `Constraint`

Intent: `Preserve`

Concerns: `Validation`, `History`, `Legal`

Statement:

1. The policy validator must reject unapproved uses of the prohibited modal in active authoring guidance and current templates.
2. The validator scope must exclude frozen work items, the legal license, controlled canonical-rule wording, and test fixtures that exercise the check.
3. The implementation must not modify excluded historical or legal files.

#### `VER-003` Verification Criterion — Validation distinguishes active policy from excluded material

Covers:

1. `SPEC-003`.

Criterion:

1. A validator fixture proves that an active-surface occurrence fails while each documented exclusion remains outside the enforcement set.

Expected evidence:

1. Focused validator assertions, full validator success, and a reviewed implementation diff limited to planned current-policy surfaces and work-item evidence.

Applicability:

1. Implementation and pre-commit review.

## Architecture decisions

Architecture snapshot status:

1. Required. The work creates a policy-to-route-to-template-to-validator control boundary that future planning agents depend on.

Decision summary:

1. Canonical owner: `references/artifact-style.md` owns the rule because it already owns authoring voice and template prompts.
2. Discovery boundary: `SKILL.md` makes `module:artifact-style` required when drafting small/medium specs and plans.
3. Prompt boundary: the shared `spec.030.common.commitments-verification.md` source block provides the short authoring cue; generated templates remain outputs.
4. Regression boundary: `test_harness_policy.py` extends `assert_artifact_style_guidance` or a focused companion assertion, using explicit active-path allowlists and narrow controlled exceptions.
5. Rejected alternatives: policy-only prose, scanning the entire repository, rewriting frozen artifacts, or treating the license as ordinary authoring text.

## Interfaces, data, and control flow

1. Authoring flow: router loads the style owner; the template repeats the concise cue; the author writes binding and advisory language with the approved modals.
2. Assembly flow: the shared source block changes; `assemble_templates.py --write` produces the two consuming specification templates; `--check` verifies freshness.
3. Validation flow: the policy validator checks the owner, route, source, output, and active-path scan; historical work items and `LICENSE` are not candidates.
4. No public application APIs, runtime data, persistence, or infrastructure change.

## Risks and rejected alternatives

### `RISK-001` The rule may be present but not loaded during ordinary planning

Mitigation:

1. Make `module:artifact-style` a required small/medium drafting input and test the router wording.

### `RISK-002` A broad text scan may damage historical compatibility

Mitigation:

1. Scan only an explicit set of active authoring paths and test the exclusion boundary; do not normalize frozen content.

### `RISK-003` Template prompts may become a second policy owner

Mitigation:

1. Keep the prompt to one operational sentence and refer readers to the canonical style rule.

### `RISK-004` The rule's explanatory wording can trigger its own validator

Mitigation:

1. Permit the named canonical rule text and test fixtures only; all other active-surface uses fail deterministically.

## Model and Sub-agent Strategy

Model generation: `GPT-5.6` when exposed; otherwise `not exposed`.

Capability tier: `balanced`.

Reasoning effort: `medium` for bounded policy, template, and validator work; `high` for the independent final review if a cross-surface scope conflict appears.

Orchestration mode: `single-agent` with one optional read-only reviewer after the implementation diff exists.

Resolved profile: `not exposed`.

Availability/fallback: use the nearest available `balanced` configuration; if unavailable, `fast/economy` medium may perform mechanical assembly and validator work, while a capability-tier escalation needs fresh operator confirmation.

Execution continuity: `new task with curated-artifact handoff`.

Context visibility: `not exposed`.

Artifact rehydration required: `Yes`; execution must read this frozen spec, plan, both snapshots, `AGENTS.md`, the repository skill, and the target canonical files before editing.

Fit assessment: this is bounded documentation-process work with medium process blast radius. One executor preserves cross-surface consistency; a read-only reviewer is useful only after the diff exists.

Sub-agent `review-001`:

1. Purpose: review the completed diff for policy duplication, accidental historical scope, self-exemption loopholes, and template assembly drift.
2. Context strategy: `curated artifacts`.
3. Input context: frozen package, changed diff, validator output, and target canonical files.
4. Output artifact: `review/plain-language-policy-review.md` with severity, evidence, and a reproduction or validation path per finding.
5. Model policy: active repository `economy-default`.
6. Model generation and resolved profile: `not exposed` unless the runtime exposes them.
7. Capability tier and reasoning effort: `balanced`, `high`.
8. Availability/fallback: orchestration-thread adversarial review using the same curated inputs.
9. Parallel execution: no; it runs after implementation validation.
10. Blast radius if wrong: medium; a missed loophole can affect future authored artifacts, but the executor retains final integration ownership.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `plan: plain-language-artifacts -- approve readable authoring policy` | `2026-07-14_plain-language-artifacts -- approve readable authoring policy` | Spec, plan, snapshots, planning fragment, and required root changelog update. |
| Implementation | `docs: plain-language-artifacts -- require ordinary modal wording` | `2026-07-14_plain-language-artifacts -- require ordinary modal wording` | Current policy, route, source block, generated templates, validator, review evidence, deltas, and implementation fragment. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `changelog/planning-approval.md`, `changelog/implementation.md` | Fragment titles match the planned commit subjects. |
| Root changelog consolidation | Living | Yes | Planning approval and implementation commits | `CHANGELOG.md` | Required by repository-level agent instructions for this work's freeze gates. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Defines active-path and exclusion behavior. |
| Testing guide delta | Living delta | Yes | Implementation | `deltas/testing-guide.delta.md` | Adds the focused policy-validator and assembly checks. |
| Operator manual delta | Living delta | No | Not applicable | Not applicable | The existing templates and canonical rule are the operator-facing contract. |
| API reference delta | Living delta | No | Not applicable | Not applicable | No API change. |
| Architecture snapshot | Snapshot | Yes | Before planning approval | `snapshots/architecture.snapshot.md` | Preserves owner, route, prompt, validation, and exclusion boundaries. |
| Architecture summary delta | Living delta | No | Not applicable | Not applicable | No repository-level architecture manual change. |
| Review evidence | Derived evidence | Yes | Before implementation commit | `review/plain-language-policy-review.md` | Created by `review-001` or the documented fallback. |
| Variance log | Execution record | Yes | During implementation | `implementation-notes/variance-log.md` | Records actual drift or explicit none. |

## Next-task handoff

1. Planning shape: `combined small/medium`.
2. Frozen package after approval: this spec, `plan_plain-language-artifacts.md`, `snapshots/architecture.snapshot.md`, and `snapshots/test-cases.snapshot.md`.
3. Next activity: implement `TASK-001` through `TASK-004` in the approved plan, beginning with the focused failing validator check.
4. Execution continuity: `new task with curated-artifact handoff`.
5. Approved strategy and fallback: the Model and Sub-agent Strategy above.
6. Variance stop condition: stop for an amendment if canonical ownership, validation scope, exceptions, template consumers, Specification Commitments, Verification Criteria, Plan Checks, or plan feasibility changes.

## Spec readiness checklist

- [x] Source input, outcome, scope, non-scope, assumptions, and decisions are explicit.
- [x] Specification Commitments are atomic, bounded, and linked to local Verification Criteria.
- [x] Current and historical compatibility boundaries are explicit.
- [x] Architecture, interfaces, validation, risks, documentation, and planned commits are covered.
- [x] The model and sub-agent strategy uses the active `economy-default` policy.
- [x] No unresolved required decisions, ownerless deferrals, or authoring placeholders remain.

## Approval

- Status: Approved
- Superseded by: None
