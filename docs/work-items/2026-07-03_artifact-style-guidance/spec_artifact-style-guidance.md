# Artifact Style Guidance Spec

Work ID: `2026-07-03_artifact-style-guidance`
Short ID: `artifact-style-guidance`
Status: Approved
Harness release: `0.4+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:evidence`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.work-item-architecture-decisions`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`, `rule:evidence.preservation`

## Goal

Add a focused artifact-style owner and template hardening so harness specs, plans, snapshots, and related review artifacts are easier for humans and agents to read, fill, freeze, and resume without hidden chat context.

## Source and Intent

Source input:

1. Operator request on 2026-07-03 for a scrupulous review and polish pass after three consecutive harness improvements:
   - `docs/work-items/2026-07-02_orchestration-sizing-large-templates/spec_orchestration-sizing-large-templates.md`
   - `docs/work-items/2026-07-02_template-block-assembly/spec_template-block-assembly.md`
   - `docs/work-items/2026-07-03_work-item-architecture-decisions/spec_work-item-architecture-decisions.md`
2. Three read-only extra-high-reasoning sub-agent reviews covering durable artifacts, template surfaces, and policy architecture.
3. Operator approval of the reconciled direction on 2026-07-03:
   - Use the recommended approach: a small canonical style module plus targeted template and validation hardening.
   - Keep style loading conditional, but require it when documents become large and make it mandatory for large anchor specs.
   - Keep a very short baseline guidance block outside the new module so minimal direction remains available without loading it.
   - Make templates themselves stronger guidance surfaces.
   - Route mutable evidence handling through existing evidence guidance.
   - Do not modify already implemented specs.

Desired operator/user outcome:

1. Future planning artifacts read as durable engineering documents rather than copied chat or template prompts.
2. Future agents know when to load style guidance, what minimal readability standard applies without loading it, and how templates should be filled.
3. The current harness preserves route-budget discipline while still giving large documents and anchor specs stronger readability requirements.

Success summary:

1. The harness gains a lightweight `module:artifact-style` with clear ownership of artifact voice, placeholder grammar, structure choice, and scanability.
2. Templates and validation make the style contract visible and harder to regress without changing frozen historical work-item artifacts.

## Scope Boundary

### In scope

1. Add a canonical artifact-style reference under `.agents/skills/dev-doc-harness/references/`.
2. Update policy architecture, router guidance, and operator-facing summaries so artifact-style routing is discoverable and route-budget aware.
3. Add a short baseline readability guidance block outside the new style module, most likely in `durable-planning-quality.md` and reinforced by templates.
4. Make `module:artifact-style` mandatory for large anchor spec drafting and required when any spec, plan, snapshot, amendment, report, or handoff becomes large enough that readability risk is material.
5. Update source blocks and generated templates so templates themselves steer agents toward precise, final, non-conversational artifact content.
6. Harden approval, supersession, unresolved-decision, model-policy-source, validation-ID, architecture-snapshot, amendment, and variance-log prompts where needed.
7. Route mutable external evidence preservation through `module:evidence` rather than adding evidence policy to the style module.
8. Update lightweight validation to catch high-signal style and template regressions without becoming a semantic writing grader.
9. Update README, operator note, release notes if needed by validator expectations, and `CHANGELOG.md` at the approval and implementation checkpoints.

### Non-scope

1. Do not rewrite, normalize, or polish already approved or implemented specs, plans, or snapshots from the July 2 and July 3 work items.
2. Do not create a general repository-level documentation style guide outside the harness package.
3. Do not add a full handoff snapshot schema in this work item; that remains a follow-up unless implementation reveals a blocking ambiguity.
4. Do not rewrite historical changelog entries solely to match current naming grammar.
5. Do not make style validation judge prose quality, intent, or semantic completeness beyond high-signal structural checks.
6. Do not make `module:artifact-style` a fourth always-required module for every routine small/medium planning route.

### Assumptions

1. The active repository model policy remains `economy-default` unless the operator changes it.
2. The existing `module:quality` remains the owner for durable handoff completeness: what a spec, plan, or phase plan must preserve.
3. The new style module owns artifact readability and authoring style: how durable artifacts stay readable, precise, and maintainable.
4. Existing `module:evidence` remains the owner for preserving mutable or derived evidence used for review or handoff.
5. The current validator should stay structural and high-signal.
6. Current generated template assembly remains the source-of-truth workflow for the four primary planning templates.

### Open questions

1. None identified after repository-context review and operator scope confirmation.

## Repository Context

### Current state

1. `policy-architecture.md` defines canonical modules for lifecycle, naming, freeze gates, models, quality, release, execution quality, evidence, and role examples, but not artifact readability or template voice.
2. `durable-planning-quality.md` defines what durable specs and phase plans must preserve, but it does not define a precise style contract for final artifact prose, table/list choices, or placeholder cleanup.
3. The generated templates are current and structurally valid, but visible prompts still use conversational verbs and broad angle-bracket fill text.
4. Readiness checklists currently mention unresolved placeholders, but not unresolved decisions, unresolved open questions, or deferred items without owner/event.
5. Template policy-reference headers are useful but not yet checked for all body-cited rule IDs.
6. `subagent-role-examples.md` contains a non-canonical `model_policy: standard-review` example.
7. `module:evidence` already states that evidence used for review, comparison, or handoff should be preserved under the work item folder.

### Evidence read

1. `.agents/skills/dev-doc-harness/SKILL.md`
2. `.agents/skills/dev-doc-harness/references/policy-architecture.md`
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md`
4. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
5. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
6. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
7. `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
8. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`
9. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
10. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
11. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
12. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
13. `.agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md`
14. `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
15. `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`
16. `.agents/skills/dev-doc-harness/assets/templates/blocks/`
17. `.agents/skills/dev-doc-harness/assets/templates/assemblies/`
18. `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`
19. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
20. `README.md`
21. `.agents/skills/dev-doc-harness/docs/operator-note.md`
22. `CHANGELOG.md`
23. `docs/work-items/2026-07-02_orchestration-sizing-large-templates/`
24. `docs/work-items/2026-07-02_template-block-assembly/`
25. `docs/work-items/2026-07-03_work-item-architecture-decisions/`
26. Sub-agent review reports from the artifact, template, and policy-architecture review passes.

### Constraints and compatibility

1. The work is substantial repository development and must use the harness.
2. The planning package must stop at the freeze gate before implementation.
3. Current route-budget guidance says routine routes should not require more than three canonical modules before optional supplemental context.
4. The operator explicitly approved conditional style routing only if baseline guidance remains outside the new module, large documents require the module, large anchor specs always require it, and templates carry more of the guidance burden.
5. Frozen historical work-item artifacts must not be rewritten to hide template residue or align with new style rules.
6. Generated templates must be edited through source blocks and assembly manifests, then regenerated.
7. Validation changes should remain structural, deterministic, and low-maintenance.

## Requirements

### `REQ-001` Canonical artifact-style module exists

Rationale:

1. Current style decisions are scattered across templates, historical artifacts, and local review findings. A canonical owner is needed so future agents know where artifact readability rules live.

Acceptance links:

1. Covered by `AC-001`, `AC-002`, and `AC-012`.

Notes:

1. The module should be lightweight and should not duplicate lifecycle, naming, freeze, model, evidence, variance, or quality semantics.

### `REQ-002` Baseline readability guidance remains available without loading the style module

Rationale:

1. Conditional style loading is acceptable only if agents still see minimal guidance during routine planning routes.

Acceptance links:

1. Covered by `AC-002`, `AC-003`, and `AC-008`.

Notes:

1. The baseline should be short enough to keep route budgets useful. It should tell agents to write final artifact content, remove authoring scaffolds, resolve required decisions, and prefer scannable structures.

### `REQ-003` Style routing is conditional but mandatory for large anchor specs and large documents

Rationale:

1. Routine small/medium planning should not always load a fourth module, but large artifacts create enough consumption risk to justify style guidance as required context.

Acceptance links:

1. Covered by `AC-003`, `AC-004`, and `AC-012`.

Notes:

1. Large anchor specs must load `module:artifact-style`.
2. Any spec, plan, phase plan, snapshot, amendment, report, handoff, or operator-facing document that becomes large enough to create readability risk must load `module:artifact-style`.

### `REQ-004` Templates become stronger artifact-writing guidance surfaces

Rationale:

1. When style routing is conditional, templates must carry concise local cues that prevent conversational residue, unresolved scaffolds, and hard-to-scan artifact layouts.

Acceptance links:

1. Covered by `AC-004`, `AC-005`, `AC-006`, `AC-007`, and `AC-008`.

Notes:

1. Template content should guide final artifact shape without embedding long reusable policy blocks.

### `REQ-005` Approval, supersession, and deferred-state fields are final artifact fields

Rationale:

1. Reviewers found approved artifacts retaining supersession instructions instead of final values. Future artifacts should record final values such as `None`, concrete artifact paths, commit hashes, owners, events, or explicit not-applicable reasons.

Acceptance links:

1. Covered by `AC-005` and `AC-008`.

### `REQ-006` Unresolved decisions and incomplete deferrals are freeze-blocking in templates

Rationale:

1. The freeze gate already requires no unresolved decisions or missing required sections. Template readiness checks should say this directly so agents do not treat placeholder cleanup as the only freeze quality check.

Acceptance links:

1. Covered by `AC-006`, `AC-008`, and `AC-012`.

### `REQ-007` Model-policy examples and strategy prompts record policy source

Rationale:

1. Durable artifacts need to distinguish repository policy, operator override, scope, and expiry so future agents do not infer an outdated model-policy choice from memory.

Acceptance links:

1. Covered by `AC-007` and `AC-012`.

Notes:

1. Correct the non-canonical `standard-review` example.

### `REQ-008` Mutable evidence handling routes through `module:evidence`

Rationale:

1. Reviewers identified mutable external URLs as a durability risk. The harness already has an evidence owner, so style guidance should cross-reference evidence preservation rather than owning evidence policy.

Acceptance links:

1. Covered by `AC-009` and `AC-012`.

### `REQ-009` Snapshot, amendment, variance, and validation surfaces gain stronger IDs and trace fields

Rationale:

1. Decision IDs, variance IDs, amendment IDs, validation IDs, and trace fields improve fresh-agent consumption and reduce row-counting or prose scanning.

Acceptance links:

1. Covered by `AC-005`, `AC-010`, and `AC-012`.

### `REQ-010` Validator catches high-signal style and template regressions

Rationale:

1. Current validation passes even though template voice, policy-reference coverage, and unused block coverage have known gaps.

Acceptance links:

1. Covered by `AC-011` and `AC-012`.

Notes:

1. The validator must not grade prose quality or become a semantic parser for artifact writing.

### `REQ-011` Already implemented specs are not modified

Rationale:

1. The operator explicitly excluded rewriting already implemented specs, and the harness treats frozen artifacts as immutable snapshots.

Acceptance links:

1. Covered by `AC-013`.

## Acceptance Criteria

### `AC-001` Artifact-style owner is declared

Verifies:

1. `REQ-001`.

Method:

1. Review `.agents/skills/dev-doc-harness/references/artifact-style.md` and confirm it declares `module:artifact-style`, owns concrete `rule:style.*` rules, and limits itself to readability, style, placeholder, structure, examples, and template-prompt guidance.

### `AC-002` Module catalog and boundary are updated

Verifies:

1. `REQ-001` and `REQ-002`.

Method:

1. Review `policy-architecture.md` and confirm `module:artifact-style` is listed as a canonical module with boundaries that keep `module:quality`, `module:lifecycle`, `module:models`, and `module:evidence` as their existing semantic owners.

### `AC-003` Conditional routing includes mandatory large-document cases

Verifies:

1. `REQ-002` and `REQ-003`.

Method:

1. Review `SKILL.md` and `policy-architecture.md` route guidance. Confirm routine small/medium routes keep style optional, large anchor spec drafting requires `module:artifact-style`, and any large or hard-to-scan artifact must load the style module.

### `AC-004` Templates carry concise local style cues

Verifies:

1. `REQ-003` and `REQ-004`.

Method:

1. Review primary template source blocks and generated templates. Confirm they include concise cues for final artifact voice, scannable structure, controlled states, and cleanup without duplicating the new style module.

### `AC-005` Final-state metadata replaces instruction residue

Verifies:

1. `REQ-004`, `REQ-005`, and `REQ-009`.

Method:

1. Review template blocks and standalone templates. Confirm approval, supersession, deferred, validation, architecture-decision, amendment, and variance fields prompt concrete final values such as `None`, IDs, paths, owners, events, commit hashes, or not-applicable reasons.

### `AC-006` Readiness checks cover unresolved decisions

Verifies:

1. `REQ-006`.

Method:

1. Review spec, plan, phase-plan, snapshot, amendment, and variance readiness or approval sections. Confirm they block unresolved required decisions, unresolved open questions, missing required sections, and deferred items without owner or resolving event.

### `AC-007` Model-policy examples use canonical policy notation

Verifies:

1. `REQ-007`.

Method:

1. Review `subagent-role-examples.md`, model-strategy source blocks, and generated templates. Confirm examples use active repository policy or the canonical `enterprise-default` and `economy-default` selectors, and record override source, scope, and expiry when an override is used.

### `AC-008` Placeholder grammar is stricter and visible prompts are less conversational

Verifies:

1. `REQ-002`, `REQ-004`, `REQ-005`, and `REQ-006`.

Method:

1. Review generated templates and validator output. Confirm arbitrary free-form angle placeholders and visible authoring verbs are reduced or controlled, while structural tokens such as `<work-id>` remain allowed.

### `AC-009` Evidence durability routes through evidence guidance

Verifies:

1. `REQ-008`.

Method:

1. Review `artifact-style.md`, `durable-planning-quality.md`, templates, and router guidance. Confirm mutable external sources are directed to `module:evidence` or `rule:evidence.preservation` and are not governed by duplicate evidence policy inside the style module.

### `AC-010` Architecture snapshot template includes decision trace

Verifies:

1. `REQ-009`.

Method:

1. Review `.agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md` and confirm it supports decision IDs, selected approach, affected boundaries, source spec sections, rejected alternatives, and validation cues.

### `AC-011` Validator protects the new contracts

Verifies:

1. `REQ-010`.

Method:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and confirm it passes with checks for style-module ownership, template policy-reference coverage, block usage, controlled placeholder or visible-prompt patterns, and generated-template freshness.

### `AC-012` Current template assembly remains valid

Verifies:

1. `REQ-001` through `REQ-010`.

Method:

1. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` and confirm all assembled templates are current after source-block updates.

### `AC-013` Historical implemented specs remain untouched

Verifies:

1. `REQ-011`.

Method:

1. Review `git diff --name-only` before the implementation commit and confirm it does not include already implemented spec, plan, or snapshot files from:
   - `docs/work-items/2026-07-02_orchestration-sizing-large-templates/`
   - `docs/work-items/2026-07-02_template-block-assembly/`
   - `docs/work-items/2026-07-03_work-item-architecture-decisions/`

## Architecture Decisions

Architecture snapshot status:

1. `Required`: this work adds a new canonical module, changes routing behavior, and adjusts template/validation boundaries.

Decision summary:

1. Drivers: Durable artifact readability, route-budget discipline, large-document consumption risk, template guidance quality, immutable historical artifacts, and existing evidence-policy ownership.
2. Constraints: `module:quality` owns completeness, `module:lifecycle` owns lifecycle and variance, `module:models` owns model strategy, `module:evidence` owns evidence preservation, and `module:architecture` already means policy architecture.
3. Selected approach: Add `module:artifact-style` as a lightweight style owner, route it conditionally, make it mandatory for large anchor specs and materially large documents, and embed concise local style cues in templates.
4. Affected boundaries: Canonical references, operation router, generated templates, standalone templates, validation script, README, operator note, release notes if required, and future work-item artifact authoring.
5. Rejected alternatives: Template-only cleanup, always-required style loading for every planning route, broad documentation-style-guide expansion, and rewriting frozen implemented specs.
6. Validation cues: New module owner appears in the policy graph, route guidance preserves budget intent, generated templates remain current, validator passes, and historical implemented specs remain out of the implementation diff.

Repository-level durable architecture documents such as `ARCHITECTURE.md` remain out of scope.

## Interfaces, Data, and Control Flow

### Interfaces affected

1. Operation router entries in `.agents/skills/dev-doc-harness/SKILL.md`.
2. Canonical module catalog and router input guidance in `policy-architecture.md`.
3. Template source blocks, standalone templates, assembly manifests if needed, and generated templates.
4. Validator check IDs and structural validation behavior in `test_harness_policy.py`.
5. Operator-facing documentation in `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`.

### Data, config, and persistence

1. No runtime data model, persistence, migration, or infrastructure change.
2. Package-local release context may require release-note updates if current validator checks demand them for new distributable surfaces.

### State and control flow

1. Planning route behavior changes so style guidance is optional for routine small/medium planning, mandatory for large anchor specs, and required when artifact size creates readability risk.
2. Template assembly control flow remains the same: edit source blocks, regenerate flat templates, validate freshness.
3. Validator flow gains additional structural checks.

### Safety, security, privacy, migration, and rollback

1. No security, privacy, compliance, or destructive-operation impact.
2. Rollback is a normal revert of the planning approval or implementation commit.
3. Main safety risk is over-validating prose or overloading routine routes; mitigations are route-budget constraints and high-signal structural validation only.

## Risks and Rejected Alternatives

### `RISK-001` Style module could become a broad writing manual

Decision or mitigation:

1. Keep `module:artifact-style` narrow: artifact readability, structure choice, placeholders, examples, template prompts, and final cleanup only.

### `RISK-002` Conditional style loading could leave routine artifacts under-guided

Decision or mitigation:

1. Add a short baseline guidance block outside the module and strengthen template prompts so routine artifacts still receive minimal direction.

### `RISK-003` Mandatory style loading could violate route-budget intent

Decision or mitigation:

1. Require style loading for large anchor specs and materially large documents, but keep it optional for routine small/medium planning unless readability or presentation is in scope.

### `RISK-004` Templates could duplicate the new module

Decision or mitigation:

1. Templates should carry concise local cues and schema prompts, not reusable policy prose.

### `RISK-005` Validator could become a semantic writing judge

Decision or mitigation:

1. Limit validation to high-signal structural checks such as module ownership, policy-reference coverage, unused blocks, allowed placeholders, visible authoring residue, generated-template freshness, and historical-spec diff exclusion where practical.

### `RISK-006` Evidence durability could be duplicated in style policy

Decision or mitigation:

1. Route mutable evidence preservation to `module:evidence` and only cross-reference it from style or quality guidance.

### `RISK-007` Frozen implemented specs could be rewritten during polish

Decision or mitigation:

1. Keep historical implemented specs, plans, and snapshots out of the implementation diff. Use future template and policy changes to prevent recurrence.

### `RISK-008` `module:architecture` terminology could remain ambiguous

Decision or mitigation:

1. Clarify router wording so `module:architecture` means policy architecture, while work-item architecture decisions remain lifecycle-owned.

### `RISK-009` Large-document threshold could be vague

Decision or mitigation:

1. Define the condition operationally: load `module:artifact-style` when an artifact is a large anchor spec, when template content would exceed routine readability, when wide tables or long sections hide decisions, or when future agents are expected to consume the artifact without chat history.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spec: artifact-style-guidance -- approve artifact style plan` | `2026-07-03_artifact-style-guidance -- approve artifact style plan` | Approval commit for this spec, plan, architecture snapshot, and `CHANGELOG.md`. |
| Implementation | `docs: artifact-style-guidance -- add artifact style module` | `2026-07-03_artifact-style-guidance -- add artifact style module` | Implementation commit for style module, router/catalog guidance, templates, validator, docs, and changelog. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries synchronized with planned commit subjects |
| Test cases | Snapshot | No | Before implementation | Not applicable | Validation is covered by executable validator and assembly checks in the plan |
| Testing guide delta | Living delta | No | During or after implementation | Not applicable | Validator command remains unchanged; implementation updates current README/operator guidance instead |
| Operator manual delta | Living delta | No | After implementation | Not applicable | Current operator-facing docs are direct implementation targets: `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md` |
| API reference delta | Living delta | No | During or after API work | Not applicable | No public API surface |
| Architecture snapshot | Snapshot | Yes | Before implementation | `snapshots/architecture.snapshot.md` | Required because the work adds a canonical module and changes route/template/validation boundaries |
| Architecture summary delta | Living delta | No | After review | Not applicable | No long-lived repository architecture document update is in scope |

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Requirements are specific, relevant, bounded, and linked to acceptance criteria.
- [x] Acceptance criteria are observable, testable, and tied to requirements or scope items.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed or explicitly absent after review.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: None
