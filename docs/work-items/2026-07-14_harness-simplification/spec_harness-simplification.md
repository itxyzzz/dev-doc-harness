# Harness Simplification Spec

Work ID: `2026-07-14_harness-simplification`
Short ID: `harness-simplification`
Status: Approved
Harness release: `0.6+`
Schema: `schema:spec.small-medium`
Planning shape: `combined small/medium`

## Goal

Make the harness a concise, useful information-flow tool for both the operator
and the agent. Preserve the commitment, verification, and check architecture,
but remove policy and template mechanics whose cognitive cost exceeds their
practical benefit.

## Source and intent

The operator reported that agents now use legalistic, defensive language,
request permission for routine work, propose amendments for ordinary execution
adjustments, and sometimes pause after individual planned tasks. The preceding
investigation found two contributors:

1. GPT-5.6 is more persistent and follows dense prompt contracts closely.
2. The current harness repeats authority, freeze, amendment, and conformance
   rules across policy and templates, and treats routine check procedures too
   much like frozen contracts.

Desired outcome:

1. Humans can quickly find the decisions and skip optional detail.
2. Agents receive enough structure to preserve scope and coverage without
   treating ordinary work as a legal process.
3. One freeze gate keeps the operator in control; an approved implementation
   then proceeds through its planned tasks without repeated confirmation.
4. The changed active authoring surfaces are smaller overall.

## Scope boundary

### In scope

1. Current repository-local harness policy, current templates and source
   blocks, generated templates, current validator guidance, and current
   operator-facing documentation.
2. The copy-ready global `AGENTS.md` bootstrap in `README.md`, limited to
   deferring repository-specific lifecycle details to the selected local
   harness. The operator will copy that suggested text into their global file.
3. Keep `SPEC`, `VER`, `TASK`, `CHECK`, `DEC`, and variance IDs as stable list
   anchors, while simplifying their presentation and relationships.
4. Make mappings optional unless they materially help coverage, handoff, or
   deterministic validation. A required mapping must state the benefit it
   provides.
5. Re-establish a narrow amendment threshold and use the variance log for
   noteworthy but allowed execution drift.
6. Add focused deterministic and scenario-based checks for the intended agent
   workflow, plus a measured before/after size report for changed author-facing
   Markdown surfaces.

### Non-scope

1. Do not rewrite frozen work items, snapshots, reports, evidence, or prior
   changelog fragments.
2. Do not remove the core commitment / criterion / plan-check architecture or
   stable entity IDs.
3. Do not weaken platform permissions, safety restrictions, destructive-action
   safeguards, or the need for an explicit post-freeze start instruction.
4. Do not add a second documentation system, a prose-quality linter, an agent
   runtime, or a general purpose requirements-management system.
5. Do not make an unconditional model or reasoning-effort escalation. Review
   escalation is evidence-triggered under the active `economy-default` policy.
6. Do not change the freeze gates in
   `references/planning-freeze-gates.md`, including the separate actual gates
   for large/phased anchor, phase-plan, and amendment packages, or the main
   README workflow diagram. Remove only consumer text that invents extra pauses
   within one approved execution path.

### Assumptions

1. A combined small/medium package is sufficient because one orchestration
   thread can integrate the cross-surface edits and bounded review feedback.
2. Frozen history remains useful evidence but is not a migration target.
3. A small number of concise scenario fixtures is a better regression control
   than attempting to automatically grade all prose or agent judgment.

### Open questions

1. None. The operator approved the scope, optional-mapping default, historical
   boundary, and use of focused reviewer sub-agents.

## Repository context

Relevant current sources include:

1. The README's global `AGENTS.md` bootstrap, which should give copy-ready
   precedence and lifecycle advice without restating local freeze details.
2. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`, which
   already intends one real freeze boundary and one fresh start instruction.
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md` and
   `references/durable-planning-quality.md`, which currently make Plan Checks
   and their mappings too broadly amendment-sensitive.
4. `.agents/skills/dev-doc-harness/references/artifact-style.md`, the existing
   current authoring-style owner, and current template source blocks under
   `.agents/skills/dev-doc-harness/assets/templates/blocks/`.

Compatibility constraints:

1. The source-block assembler remains the only supported way to change
   generated primary templates.
2. The active repository model policy remains `economy-default`.
3. The repository-local harness remains the canonical source for this
   repository's artifact lifecycle.

## Specification commitments and verification criteria

### `SPEC-001` Preserve useful identifiers and reduce presentation overhead

Kind: `Constraint`

Intent: `Preserve`

Statement:

1. Current harness artifacts must retain stable `SPEC`, `VER`, `TASK`,
   `CHECK`, `DEC`, and variance IDs where later work cites them.
2. Whenever one of those entity lists is used, its entries must use the
   applicable IDs as concise reader-facing anchors; an ID family may be absent
   only when that entity type is not present.
3. Current authoring guidance and templates must present IDs as concise anchors
   with short titles. Classification metadata is optional; when useful, it must
   appear on one compact line such as `Constraint · Preserve`, not as separate
   `Kind:` and `Intent:` fields.

#### `VER-001` IDs remain usable without mandatory formal presentation

Criterion:

1. Current templates and guidance retain the entity ID families and use concise
   examples, while removed presentation fields are not required by the policy
   validator.

Expected evidence:

1. Focused validator assertions, generated-template inspection, and a reviewed
   diff of the changed authoring surfaces.

### `SPEC-002` Make traceability proportional to its benefit

Kind: `Behavior`

Intent: `Change`

Statement:

1. Plans must use local links between an item and its related task or check when
   that is enough for a reader to follow the work.
2. A complete mapping table may be added when it materially prevents a coverage
   gap, supports a fresh handoff, or supplies deterministic validator input.
3. A plan must not require a complete commitment-disposition or
   verification-execution matrix merely because entity IDs exist.

#### `VER-002` Mapping guidance is optional and benefit-based

Criterion:

1. Current plan templates and quality guidance describe mappings as an optional
   tool with named use cases, and no validator requires a full mapping for a
   small straightforward plan.

Expected evidence:

1. Scenario fixtures and template/validator checks cover a concise local-link
   plan and a larger plan where an explicit mapping is justified.

### `SPEC-003` Keep one meaningful approval boundary

Kind: `Behavior`

Intent: `Change`

Statement:

1. Current consumer guidance must describe a freeze gate as one pause at a real
   approved package boundary, without changing the canonical freeze-gate module.
2. A fresh instruction that starts implementation must authorize execution of
   the approved plan through its planned tasks.
3. Agents must not request routine confirmation between planned tasks, for
   planned local edits, or for non-destructive validation.

#### `VER-003` Approved execution proceeds without per-task approvals

Criterion:

1. Current guidance and scenario checks distinguish the single freeze/start
   boundary from routine progress within approved implementation.

Expected evidence:

1. Policy text inspection and a scenario fixture covering a multi-task
   implementation path.

### `SPEC-004` Reserve amendments for material change and use variance notes

Kind: `Behavior`

Intent: `Change`

Statement:

1. An equivalent local implementation or validation adjustment that preserves
   scope and the evidence purpose may proceed and receives a variance-log note
   only when it is noteworthy.
2. An amendment and approval are required only for material scope, outcome,
   architecture, API, data, security, privacy, compliance, or genuinely
   invalidated verification changes.
3. A Plan Check must describe useful evidence, not create an automatically
   amendment-sensitive frozen procedure contract.

#### `VER-004` Routine drift uses the variance log; material drift stops

Criterion:

1. Current policy and scenarios route an equivalent check adjustment to a
   variance note and route a changed outcome or invalidated proof to an
   amendment.

Expected evidence:

1. Focused validator assertions and scenario fixtures for both cases.

### `SPEC-005` Use plain, centralized operator language

Kind: `Quality`

Intent: `Change`

Statement:

1. Current author-facing guidance, templates, status wording, and handoffs must
   use direct operational language and avoid legalistic authority or compliance
   phrasing when a simpler statement communicates the same action.
2. The README's copy-ready global bootstrap must direct readers to the selected
   repository-local harness for ordinary freeze/changelog details rather than
   restating conflicting requirements.
3. Reusable approval and autonomy rules must have one canonical owner and
   short consumers rather than duplicated instructions.

#### `VER-005` Current guidance has one coherent, plain workflow

Criterion:

1. The README bootstrap and repository-local guidance agree on the ordinary
   freeze/changelog path, and current templates route to concise canonical
   policy instead of restating it.

Expected evidence:

1. Cross-surface validator checks, a focused reviewer report, and the updated
   README bootstrap snippet.

### `SPEC-006` Demonstrate a net reduction in active authoring prose

Kind: `Quality`

Intent: `Change`

Statement:

1. The implementation must measure before and after nonblank-line and word
   counts for every path in `snapshots/active-authoring-baseline.md`, using its
   fixed command and source/generated-file rule.
2. The manifest's aggregate must show a net reduction in both measures unless a
   reviewer documents that a smaller indispensable regression control requires
   an exception and the operator approves it as material variance.

#### `VER-006` Simplification is measured rather than asserted

Criterion:

1. Implementation evidence records the counting method and shows the required
   net reduction or an approved exception.

Expected evidence:

1. A reproducible count command, its before/after output, and final reviewer
   confirmation.

## Architecture decisions

Architecture snapshot status: `Required`.

Decision summary:

1. Preserve the four entity families as identifiers, not as a universal
   requirements-management grammar.
2. Put lifecycle and approval rules in their canonical owners; templates give
   short task-time cues only.
3. Use progressive traceability: local links by default and a mapping only when
   it demonstrably helps coverage, handoff, or automation.
4. Treat Plan Checks as evidence guidance; the evidence purpose, rather than an
   exact command string, determines whether a change is material.
5. Use a mandatory focused reviewer after implementation validation and permit a
   flagship escalation only for an unresolved high-impact conflict.

Rejected alternatives:

1. Revert the commitment-verification architecture entirely; this loses useful
   stable identifiers and coverage vocabulary.
2. Keep the current architecture but change only modal words; this leaves the
   approval and amendment mechanics unchanged.
3. Split human and agent documentation into separate complete overlays; this
   creates duplicate sources and more maintenance burden.

## Interfaces, data, and control flow

Interfaces affected:

1. The durable-artifact schema and template prompts change, but no public
   software API, persistence schema, or runtime service changes.
2. The README's copy-ready global bootstrap is documentation only; the operator
   owns any later copy into a personal global guidance file.

Control flow after the change:

1. Draft artifacts may be refined directly.
2. One approved package freezes and pauses once.
3. A fresh instruction begins the documented next activity.
4. The agent completes planned tasks and safe validation without extra approval.
5. Noteworthy allowed drift uses the variance log; material drift uses an
   amendment and operator approval.

## Risks and mitigations

### `RISK-001` Simplification removes a useful coverage signal

Decision or mitigation:

1. Keep IDs and local links. Require a mapping when its benefit is specific and
   test both the concise and mapping-justified scenarios.

### `RISK-002` Different instruction layers drift again

Decision or mitigation:

1. Give each rule one owner, make consumer text short, and validate the global
   and repository-local ordinary-freeze agreement when the global file is in
   scope and writable.

### `RISK-003` A prose reduction weakens safety boundaries

Decision or mitigation:

1. Preserve explicit confirmation for external, destructive, costly, and
   material scope-expanding actions; reviewer scenarios test those boundaries.

### `RISK-004` Review becomes another bureaucratic gate

Decision or mitigation:

1. Use one named, read-only reviewer with a fixed lens and evidence-backed
   findings. Escalate only if that review finds an unresolved high-impact issue.

## Model and sub-agent strategy

Model policy: active repository `economy-default`.

Baseline execution:

1. Model generation: `not exposed`.
2. Capability tier: `balanced`.
3. Reasoning effort: `medium`.
4. Orchestration mode: `bounded delegated sub-agents`; the only delegate is the
   named read-only reviewer and the orchestration thread owns every write.
5. Resolved profile: `not exposed`.
6. Availability/fallback: use the nearest available balanced/medium profile;
   use fast/economy medium only for mechanical validation, and use the
   orchestration thread for an unavailable reviewer.
7. Execution continuity: `same task` when the frozen package and active model
   remain available.
8. Context visibility: `not exposed`.
9. Artifact rehydration: `Yes`; read the frozen package, current guidance,
   target policy, templates, validator, and generated outputs before editing.
10. Fit assessment: medium complexity and policy blast radius; bounded review
    improves detection of accidental over-correction without a second planning
    hierarchy.
11. Recommended change: `None`; `review-002` is an evidence-triggered,
    documented escalation rather than a default.

Sub-agent `review-001`:

1. Purpose: review the validated implementation diff for retained legalistic
   phrasing, duplicated authority rules, accidental loss of useful coverage,
   and over-broad amendment changes.
2. Context strategy: `curated artifacts`.
3. Input context: frozen package, changed diff, before/after counts, validator
   output, assembly output, and the changed canonical sources.
4. Output artifact: `review/harness-simplification-review.md` with severity,
   evidence, reproduction/validation path, and recommendation.
5. Model policy and generation: active `economy-default`; generation and
   resolved profile are `not exposed` unless the runtime exposes them.
6. Capability tier and reasoning effort: `balanced`, `high`.
7. Availability/fallback: orchestration-thread review of the same curated
   inputs if a delegated reviewer is unavailable.
8. Parallel execution: no; runs after implementation validation.
9. Blast radius if wrong: medium; poor advice could preserve an undesirable
   policy, but the orchestration thread retains integration ownership.

Sub-agent `review-002`:

1. Trigger: `review-001` finds an unresolved conflict about safety, global
   instruction precedence, or a material loss of verification evidence.
2. Purpose: adversarial resolution of that single unresolved conflict.
3. Context strategy: `curated artifacts`.
4. Model policy and generation: active `economy-default`; generation and
   resolved profile are `not exposed` unless the runtime exposes them.
5. Capability tier and reasoning effort: `flagship`, `medium`, with the written
   trigger as the escalation rationale.
6. Availability fallback: the orchestration thread performs the same narrow
   review; do not make an unplanned broad escalation.
7. Parallel execution: no; runs only after `review-001`.

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `plan: harness-simplification -- approve leaner agent workflow` | `2026-07-14_harness-simplification -- approve leaner agent workflow` | Draft package after operator approval. |
| Implementation | `docs: harness-simplification -- reduce policy and mapping overhead` | `2026-07-14_harness-simplification -- reduce policy and mapping overhead` | Current policy, templates, tests, and evidence. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog source | Living | Yes | Before each commit | `changelog/planning-approval.md`, `changelog/implementation.md` | Fragment titles match planned subjects. |
| Root changelog consolidation | Living | As needed | Operator-owned checkpoint | `CHANGELOG.md` | The repository-local policy is authoritative for ordinary work-item commits. |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Covers workflow, mapping, variance, and size scenarios. |
| Active authoring baseline | Snapshot | Yes | Before implementation | `snapshots/active-authoring-baseline.md` | Freezes the size manifest and counting command. |
| Architecture snapshot | Snapshot | Yes | Before planning approval | `snapshots/architecture.snapshot.md` | Preserves the simplification boundaries. |
| Testing guide delta | Living delta | Yes | Implementation | `deltas/testing-guide.delta.md` | Records the focused validator, assembler, and size checks. |
| Operator manual delta | Living delta | Yes | Implementation | `deltas/operator-manual.delta.md` | Explains the simpler freeze, mapping, and variance behavior. |
| API reference delta | Living delta | No | Not applicable | Not applicable | No public API change. |
| Architecture summary delta | Living delta | No | Not applicable | Not applicable | Work-item snapshot is sufficient. |
| Review evidence | Derived evidence | Yes | Before implementation commit | `review/harness-simplification-review.md` | Produced by `review-001` or the documented fallback. |
| Variance log | Execution record | Conditional | During implementation | `implementation-notes/variance-log.md` | Create only for actual noteworthy permitted drift. |

## Next-task handoff

1. Planning shape: `combined small/medium`.
2. Frozen package after approval: this spec, the implementation plan,
   `snapshots/architecture.snapshot.md`, `snapshots/test-cases.snapshot.md`,
   and `snapshots/active-authoring-baseline.md`.
3. Next activity: implement the approved simplification tasks, beginning with
   the baseline and focused failing checks.
4. Variance stop condition: stop for an amendment only when a change meets the
   material threshold defined by `SPEC-004`.

## Approval

- Status: Approved
- Superseded by: None
