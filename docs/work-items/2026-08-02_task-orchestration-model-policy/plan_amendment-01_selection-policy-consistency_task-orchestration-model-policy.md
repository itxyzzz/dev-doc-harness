# Plan Amendment 01: Selection Policy Consistency

Work ID: `2026-08-02_task-orchestration-model-policy`
Short ID: `task-orchestration-model-policy`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.amendment`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:artifact-style`, `module:freeze-gate`, `module:models`, `module:architecture`, `module:execution-quality`, `module:implementation-changelog`, `rule:lifecycle.stage-boundaries`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.selection-dimensions`, `rule:models.orchestration-mode`, `rule:models.next-stage-continuity`, `rule:models.final-review`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-001`
- Frozen package:
  - `spec_task-orchestration-model-policy.md`
  - `plan_task-orchestration-model-policy.md`
  - `snapshots/architecture.snapshot.md`
- Approval commit: `b34b2c65fa2bfd2c646739d85a7b0a00d880f12e`
- Implemented baseline commit: `8832fce67e4a9dafb8c2b29254c340ecd3267db5`
- Affected original decisions and instructions: `SPEC-003` through `SPEC-008`, `DEC-001` through `DEC-004`, `TASK-001` through `TASK-003`, and `CHECK-003` through `CHECK-008`.
- Original instruction: make `module:models` own actionable next-stage orchestration and model selection, render the contract consistently through current consumers and templates, preserve reviewer safeguards, and validate terminology, stage applicability, model dimensions, and generated-template parity.

## Discovered issue

Post-implementation review found that the intended next-stage selection contract is not yet coherent across its canonical owner and consumers:

1. The accepted policy direction adds orchestration mode to the Orchestration group, but **Mode** is too generic a field name. The durable label must be **Orchestration mode**. Required notation, freeze-gate projection, source templates, generated templates, README guidance, and validator fixtures do not currently render or require it.
2. `planning-freeze-gates.md` still permits a non-execution transition with no `Run in` value and retains `same-task`, `current task`, and `new-task recommendation` wording for the governed continuity concept. This conflicts with the approved same/new-orchestration-session contract for planning, execution, and resumed amended stages.
3. Optional current-session diagnostics remain prominent and duplicative. They list generation, tier, reasoning, orchestration mode, resolved profile, and context visibility ahead of the actionable next-stage selection. The header prompt `omit when not exposed or material` is also logically inverted.
4. The canonical module defines capability tiers and reasoning effort but does not first define model selection as the three independent facets Generation, Capability tier, and Reasoning effort. Resolved profile remains mixed into several presentations as though it were an additional selection facet.
5. Method, Orchestration mode, `Run in`, and Review are not defined consistently at first use. The current orchestration-mode definition is implementation-specific even though the field applies to planning stages too.
6. Provider- and host-specific names remain in reusable policy. The execution fallback still says Native Codex, the economy policy leads with concrete Terra/Sol profiles instead of policy-relative choices plus equivalents, and the provider-portability statement does not distinguish model providers from host runtimes.
7. Proposed sub-agent notation separates Generation, Capability tier, and Reasoning effort with a peer Resolved profile field instead of presenting one recommended sub-agent model and an optional concrete target mapping.
8. Allocation wording can be read as discouraging isolated reviewers for tightly coupled or same-file implementation, and the final-review rule allows the orchestration session itself to satisfy high-blast-radius final review despite the independent-review default.
9. `planning-freeze-gates.md` repeats selection semantics owned by `module:models` instead of citing the owner and limiting itself to the draft/freeze chat projection.
10. Existing validator checks pass despite these contradictions because their fixtures do not require Orchestration mode or reject the no-`Run in` route.

These are material post-freeze corrections because the selection field schema, continuity contract, host portability, and independent-review assurance are externally consumed policy interfaces.

## Operator-owned local input

The current checkout on the non-default branch `0.9-clarifications` contains an operator-authored, uncommitted edit to `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`. Execution must preserve this edit as its local implementation baseline and build on top of it. The observed patch changes the next-stage summary as follows:

```diff
-1. **Next lifecycle stage** records the documented stage determined by `rule:lifecycle.stage-boundaries`.
-2. **Orchestration** records Method, `Run in`, and Review.
-3. **Model** records the independent Generation, Capability tier, and Reasoning effort.
+1. **Next lifecycle stage** records the next documented stage determined by `rule:lifecycle.stage-boundaries`.
+2. **Orchestration** records the Method and Mode, `Run in` (same or new orchestration session), and Review arrangement.
+3. **Model** records the independent Generation, Capability tier, and Reasoning effort for the next orchestration session.
```

The amended implementation retains the operator's first and third replacement lines. It refines the second replacement line only to use the agreed full label and continuity name:

```md
2. **Orchestration** records Method, Orchestration mode, `Run in` (next-stage continuity: same or new orchestration session), and the stage-appropriate Review arrangement.
```

Implementation remains in the current checkout on `0.9-clarifications`; no additional worktree or branch is required. Before other implementation edits, the executor must verify that the local policy diff still matches the patch above, preserve it without reset or overwrite, and then apply this amendment's refinements directly on top.

## Proposed change

### `AMD-001-DEC-001` Use the full Orchestration mode field label

The next-stage Orchestration group must use these four field labels consistently:

1. `Method`: the named workflow used for the documented next lifecycle stage.
2. `Orchestration mode`: the agent/controller topology used to perform that stage.
3. `Run in` (`next-stage continuity`): `same orchestration session` or `new orchestration session`.
4. `Review`: the planning-review or execution Plan Task/final-review arrangement appropriate to the stage.

Do not shorten `Orchestration mode` to `Mode` in canonical policy, templates, generated artifacts, chat projection guidance, or semantic validator fixtures.

### `AMD-001-DEC-002` Require continuity for every governed next stage

Remove the no-`Run in` exception. Every planning, execution, and resumed amended stage governed by the four-group next-stage selection must record one of the two canonical continuity values. Replace stale `same-task`, `current task`, and `new-task recommendation` wording when it denotes this continuity concept. Keep product task-creation terminology only where the text directly describes a host system's task-creation action, and distinguish that action from orchestration-session continuity.

### `AMD-001-DEC-003` Reorganize the canonical module around actionable selection

Reorder `subagent-model-policy.md` into this responsibility flow:

1. Task and session terminology.
2. Upcoming-stage selection with the four ordered groups and no expanded current-session diagnostic block.
3. Orchestration selection defining Method, Orchestration mode, `Run in`, and Review.
4. Model selection defining Generation, Capability tier, Reasoning effort, and Resolved profile as a runtime mapping rather than a fourth durable facet.
5. Optional current-session diagnostics near continuity: only Resolved model profile and Context visibility, omitted unless exposed and material.
6. Execution method and reviewer contract.
7. Upcoming-stage sub-agent assessment, authorization, context, allocation, policy profiles, independent review, and final integration.
8. Thin Required notation and Runtime report requirements.

The introductory substantial-work sentence must describe **upcoming-stage orchestration and model selection**, not model selection alone.

### `AMD-001-DEC-004` Make model and host terminology portable

1. Define Generation as a provider model family or version cohort, Capability tier as the durable vendor-neutral class, and Reasoning effort as the independently selected runtime effort.
2. Define Resolved profile as the concrete runtime mapping of those three choices when exposed; it is not another durable selection facet.
3. State intentionally that host runtimes and model providers may expose different concrete names and mappings.
4. Replace Native Codex as the generic fallback label with **host-native execution** in current reusable policy, lifecycle guidance, and validator scenarios. Retain Codex only where the product itself is the subject.
5. Express `economy-default` allocations policy-first: `balanced/medium (Terra medium or equivalent)`, `balanced/high (Terra high or equivalent)`, `flagship/medium (Sol medium or equivalent)`, and `flagship/high (Sol high or equivalent)`.
6. Keep active model policy separate from the recommended sub-agent model. Present a proposed role's model as Generation, Capability tier, and Reasoning effort together; include a Resolved target profile only when a concrete runtime mapping is exposed and useful.

### `AMD-001-DEC-005` Preserve independent review as a distinct assurance mechanism

1. Clarify that warnings about tightly coupled work, same-file edits, and coordination overhead primarily constrain concurrent write-capable workers; they do not make an isolated read-only reviewer unsuitable.
2. Keep read-only explorer and reviewer roles preferred before write-capable workers when their isolation or review quality justifies the cost.
3. Require high-blast-radius final review to use the independent reviewer contract, subject only to the existing documented unavailable/declined-review disclosure and operator-authorization exception.
4. Keep the orchestration session as final integration owner; it consumes reviewer findings but is not itself independent review.

### `AMD-001-DEC-006` Keep freeze-gate ownership thin

`module:freeze-gate` continues to own when the draft or approved selection is projected in chat. It must cite `rule:models.selection-dimensions` for the four-group schema and `rule:lifecycle.stage-boundaries` for Stage rather than restating planning/execution applicability semantics. It must still reconfirm the upcoming-stage sub-agent assessment and authorization state.

## Explicit non-scope: enterprise-default

Amendment 1 must not rename or otherwise revise:

1. `enterprise-default`.
2. `rule:models.enterprise-default`.
3. The `## Policy: enterprise-default` section.
4. Template or repository-policy references whose only change would be the future policy rename.

The operator has reserved that policy-name and policy-semantics review for amendment 2. Amendment 1 must not preselect `performance-default`, `quality-default`, `assurance-default`, or any other replacement.

## Change surfaces

### Canonical policy and direct consumers

1. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
3. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`.
4. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md` when its role notation or concrete profile examples consume the amended model contract.
5. `README.md` for the compact four-group and host-native execution summary.

### Template sources

1. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md`.
2. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.phase.header-objective-inputs.md`.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.040.common.model-strategy.md`.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.small.handoff.md`.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.phase.handoff.md`.
6. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.small.readiness-completion-approval.md`.
7. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.phase.readiness-completion-approval.md`.
8. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md`.
9. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.large.readiness-approval.md`.
10. Any additional current source block identified by the amended validator because it renders the same owned selection or diagnostic fields.

### Generated outputs and validation

1. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`.
2. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`.
3. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`.
4. Any other assembly-manifest output derived from a changed source block; generated outputs must be written only by `assemble_templates.py --write`.
5. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
6. `docs/work-items/2026-08-02_task-orchestration-model-policy/changelog/implementation-fragment.md`, updated newest-first before the amended implementation commit.

No frozen spec, original plan, architecture snapshot, prior amendment, root `CHANGELOG.md`, or `enterprise-default` surface is an implementation target.

## Amended implementation plan

### `AMD-001-TASK-001` Preserve operator input and establish failing policy checks

Outcome: the current non-default branch retains the implemented baseline and exact operator-authored policy edit, and validator expectations fail for the remaining amendment gaps.

Dependencies and inputs:

1. Approved amendment 1 and original frozen package.
2. Current checkout on `0.9-clarifications` with the operator-owned policy diff.
3. Implemented baseline commit `8832fce67e4a9dafb8c2b29254c340ecd3267db5` and the amendment approval commit.

Implementation:

1. Inspect the current branch, status, and policy diff. Stop if the policy diff differs materially from the patch recorded in this amendment or if unrelated local changes would overlap the amendment.
2. Confirm that the amendment approval commit descends from the implemented baseline and that the operator policy edit remains unstaged after the amendment-only approval commit.
3. Verify the exact operator patch from `## Operator-owned local input` before any other implementation edit; do not reset, replace, or reapply it.
4. Update `test_harness_policy.py` first so focused fixtures require the full `Orchestration mode` label, require `Run in` for planning/execution/resumed selections, reject missing or shorthand continuity, enforce compact optional current diagnostics, verify the three defined model facets and optional profile mapping, require host-native portability, protect the independent final-review contract, and preserve `enterprise-default` unchanged.
5. Run the focused/full validator before policy edits and confirm failures are limited to the newly asserted amendment gaps.

Exit criteria: operator input is demonstrably preserved in the current checkout, and red validation identifies every planned canonical or consumer correction without unrelated baseline failure.

#### `AMD-001-CHECK-001` Verify operator-edit carryover

Covers: operator instruction and `AMD-001-DEC-001`.

Method: run `git branch --show-current`, `git status --short`, and `git diff -- .agents/skills/dev-doc-harness/references/subagent-model-policy.md` before any further policy edit; compare the diff with `## Operator-owned local input`.

Expected result: the branch is `0.9-clarifications`, the amendment is frozen in the current history, the policy file remains the only unstaged implementation input, and its three-line replacement matches the amendment record exactly.

Evidence record: execution log and completion report.

#### `AMD-001-CHECK-002` Demonstrate red amendment fixtures

Covers: `AMD-001-DEC-001` through `AMD-001-DEC-006`.

Method: run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` after validator expectations change and before canonical/consumer implementation.

Expected result: the suite fails only on named amendment expectations such as missing `Orchestration mode`, the continuity exception, duplicated current diagnostics, absent model-facet definitions, host-specific fallback wording, or the final-review contradiction.

Evidence record: focused failure IDs and messages in the execution log.

### `AMD-001-TASK-002` Rewrite canonical policy and propagate its consumers

Outcome: canonical policy, lifecycle/freeze consumers, source templates, generated artifacts, operator guidance, and semantic fixtures agree on the amended contract.

Dependencies: `AMD-001-TASK-001` red fixtures and preserved local operator input.

Implementation:

1. Reorganize `subagent-model-policy.md` exactly by `AMD-001-DEC-003`, retaining the operator's accepted first and third summary changes and refining the second to the full `Orchestration mode` contract.
2. Apply `AMD-001-DEC-001`, `AMD-001-DEC-002`, `AMD-001-DEC-004`, and `AMD-001-DEC-005` at their canonical owners. Do not edit the `enterprise-default` owner row, heading, section, or semantics.
3. Update `artifact-contract.md` to use host-native execution as the generic cascade fallback while preserving the same Superpowers ordering and operator override behavior.
4. Update `planning-freeze-gates.md` to cite the canonical selection owner, render the full fields including Orchestration mode, require `Run in`, remove the non-execution exception, and replace stale task vocabulary where it denotes continuity.
5. Update role examples and README only where they directly consume the changed contract; keep them compact and noncanonical.
6. Update the named template source blocks. Current-session header metadata must contain only Resolved model profile and Context visibility and must say `omit unless exposed and material`. Handoff selections must render Method, Orchestration mode, `Run in`, Review, Generation, Capability tier, and Reasoning.
7. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` once after all source-block changes, inspect every generated diff, and run the assembler check.
8. Run the full policy suite and resolve failures at the canonical owner or source block rather than patching generated output directly.

Exit criteria: all current consumers and generated artifacts agree with the amended canonical policy, the suite is green, and `enterprise-default` remains byte-for-byte unchanged from the implemented baseline where possible.

#### `AMD-001-CHECK-003` Validate selection and continuity fixtures

Covers: `AMD-001-DEC-001`, `AMD-001-DEC-002`, and `AMD-001-DEC-006`.

Method: exercise validator fixtures for `plan drafting`, `phase-plan drafting`, `plan execution`, `phase execution`, and a resumed amended stage, including negative cases with missing `Orchestration mode`, `Mode` shorthand, missing `Run in`, and retired task-based continuity wording.

Expected result: every valid fixture contains Method, Orchestration mode, canonical `Run in`, and stage-appropriate Review; every negative fixture is rejected for its intended reason.

Evidence record: `presentation.next-stage-summary` and related focused check output.

#### `AMD-001-CHECK-004` Validate model, portability, and review semantics

Covers: `AMD-001-DEC-003` through `AMD-001-DEC-005`.

Method: run focused assertions and inspect the canonical sections for the three model facets, optional resolved-profile mapping, compact current-session diagnostics, host-native execution terminology, policy-first economy equivalents, reviewer-friendly allocation wording, independent high-blast-radius final review, and unchanged final-integration ownership.

Expected result: each concern has one canonical definition, current diagnostics do not duplicate the next-stage selection, host/provider distinctions are explicit, and independent review is not conflated with orchestration-session integration.

Evidence record: focused validator output and final policy review notes.

#### `AMD-001-CHECK-005` Verify template source/generated parity

Covers: `AMD-001-DEC-001` through `AMD-001-DEC-004`.

Method: run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` and inspect every generated template containing current-session metadata or the next-stage summary.

Expected result: the command exits `0` with `All assembled templates are current.`; generated selections use the full field labels and generated current-session metadata is compact and optional.

Evidence record: assembler output and generated-diff inspection notes.

### `AMD-001-TASK-003` Review, record, validate, and commit the amendment implementation

Outcome: one cohesive amended implementation commit has complete validation and independent-review evidence or the authorized disclosed fallback.

Dependencies: `AMD-001-TASK-002` complete.

Implementation:

1. Run `AMD-001-CHECK-003` through `AMD-001-CHECK-007` on the integrated diff.
2. Update `changelog/implementation-fragment.md` newest-first with an entry matching the amended implementation subject:

   ```md
   ### 2026-08-02 docs: task-orchestration-model-policy -- align orchestration and model selection

   Meta -- `unreleased` : `distributable`

   #### Changed

   - Made Orchestration mode an explicit next-stage field across policy, templates, freeze presentation, and validation.
   - Defined portable model facets and host-native fallbacks while simplifying optional current-session diagnostics.
   - Required canonical continuity and preserved independent high-risk review as distinct from final integration.
   ```

3. Run the independent final policy reviewer if the bounded strategy below is approved and available. Resolve blocking findings and rerun affected checks. Otherwise perform the recorded controller fallback and disclose the assurance gap.
4. Run changelog lint, template assembly check, the full harness policy suite, focused stale-term searches, `git diff --check`, and final diff inspection.
5. Verify that the original frozen spec, plan, architecture snapshot, the approved amendment, root `CHANGELOG.md`, and all `enterprise-default` surfaces are unchanged by implementation.
6. Stage only the amended implementation paths and changelog update, inspect the staged diff, and commit the planned subject.

Exit criteria: all checks pass, no blocking review finding remains, non-scope is intact, and the amended implementation is one independently revertible commit.

#### `AMD-001-CHECK-006` Run full policy and delivery validation

Covers: all amendment decisions.

Method: run:

1. `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`.
2. `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
3. `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`.
4. `git diff --check`.

Expected result: every command exits `0`, assembled templates are current, all harness check IDs pass, the changelog fragment is valid, and no whitespace error exists.

Evidence record: complete command summaries in the implementation completion report.

#### `AMD-001-CHECK-007` Verify scope, terminology, and enterprise-default exclusion

Covers: all amendment decisions and explicit non-scope.

Method:

1. Search current reusable surfaces for `same-task`, `new-task recommendation`, current-session field duplication, `Method:.*Run in:.*Review:` without Orchestration mode, generic Native Codex fallback wording, and concrete economy mappings without `or equivalent`.
2. Compare the `rule:models.enterprise-default` owner row, `## Policy: enterprise-default` section, template policy choices, and repository-policy references against commit `8832fce67e4a9dafb8c2b29254c340ecd3267db5`.
3. Inspect `git diff --name-only -- docs/work-items/2026-08-02_task-orchestration-model-policy`.

Expected result: no stale governed terminology or incomplete selection remains; enterprise-default surfaces are unchanged; work-item implementation changes are limited to the existing implementation fragment while frozen planning artifacts and the approved amendment remain unchanged.

Evidence record: search results, baseline comparisons, and work-item diff list.

#### `AMD-001-CHECK-008` Perform final independent policy review

Covers: `AMD-001-DEC-001` through `AMD-001-DEC-006`.

Method: give the approved read-only reviewer the original frozen package, approved amendment, operator patch, integrated diff, full validation output, template assembly result, and changelog fragment. Use the named lenses: ownership, selection-field parity, planning/execution applicability, continuity completeness, model-facet separation, portability, independent-review assurance, non-scope preservation, and preservation of the local operator edit.

Expected result: no blocking finding remains. Each finding includes severity and a validation path. If independent review is unavailable or declined, the controller records the reason, assurance gap, focused self-review, and operator authorization before proceeding.

Evidence record: reviewer findings or the authorized fallback disclosure in the completion report.

## Impact assessment

1. Outcome: the original policy-reorganization outcome is completed rather than changed; actionable next-stage orchestration and model selection become coherent and validator-backed.
2. Architecture: `module:models` remains the selection owner, lifecycle remains the stage owner, and freeze gate remains the presentation owner. No module or stable rule ID changes.
3. Interfaces: the Orchestration group adds the required full `Orchestration mode` label, and every governed selection requires canonical `Run in` continuity.
4. Data, API, security, privacy, compliance, and migration: no application data, runtime API, security, privacy, compliance, or destructive migration impact.
5. Compatibility: current reusable policy becomes more host-portable. Historical frozen artifacts remain immutable. Concrete GPT-5.6 names remain current mappings or parenthetical equivalents rather than permanent vocabulary.
6. Review assurance: high-blast-radius review remains independent except through the already governed unavailable/declined-review authorization path; final integration ownership stays with the orchestration session.
7. Rollback: revert the single amended implementation commit. The amendment approval commit remains historical planning evidence.
8. Documentation: canonical policy, lifecycle/freeze consumers, source templates, generated outputs, README, validator fixtures, and the implementation fragment change together.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Implementation changelog source | Living | Yes | Before amended implementation commit | `docs/work-items/2026-08-02_task-orchestration-model-policy/changelog/implementation-fragment.md` | Add the planned amended implementation entry newest-first |
| Root changelog consolidation | Living | As needed | Operator-owned implementation or release checkpoint | `CHANGELOG.md` | Not changed by planning or amended implementation |
| Test cases | Snapshot | No | Before implementation | Not created | Semantic validator fixtures provide deterministic coverage |
| Testing guide delta | Living delta | No | During or after implementation | Not created | No operator test flow changes |
| Operator manual delta | Living delta | No | After implementation | Not created | README is the compact current operator surface |
| API reference delta | Living delta | No | During or after API work | Not created | No application or public API change |
| Architecture snapshot | Snapshot | No | Before implementation | Not created | This amendment records the post-freeze selection-interface decisions; the original snapshot remains frozen |
| Architecture summary delta | Living delta | No | After review | Not created | No repository-level architecture manual exists |
| Current harness policy and templates | Normative/generated | Yes | During amended implementation | `.agents/skills/dev-doc-harness/` | Update canonical owners and source blocks, then regenerate outputs |
| Root operator guidance | Living documentation | Yes | During amended implementation | `README.md` | Keep the summary compact and noncanonical |

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: one read-only `amendment-final-policy-reviewer`; no executor sub-agents.
2. Fit reason: canonical policy, freeze behavior, templates, generated outputs, and validator fixtures are tightly coupled and should have one implementation controller. An isolated final reviewer is valuable specifically because the amendment addresses review assurance and cross-surface contradictions.
3. Authorization state: Approved by the operator on 2026-08-02.
4. Fallback: if the reviewer is unavailable or the operator declines it, use the controller review in `AMD-001-CHECK-008`, record the assurance gap and compensating evidence, and obtain or record the one required operator decision before implementation continues.

Sub-agent `amendment-final-policy-reviewer`:

1. Purpose: independently review the integrated amended diff for rule loss, duplicate ownership, missing Orchestration mode, continuity gaps, diagnostic duplication, portability regressions, weakened reviewer assurance, enterprise-default scope leakage, and failure to preserve the operator patch.
2. Context strategy: `curated artifacts`.
3. Input context: original frozen package, approved amendment, recorded operator patch, integrated diff, validation output, template assembly result, and implementation fragment.
4. Output artifact: evidence-backed findings with severity and validation path.
5. Model policy: active repository `economy-default` with a review-quality escalation.
6. Recommended model: Generation `latest available`; Capability tier `flagship`; Reasoning effort `high`.
7. Resolved target profile: `Sol high or equivalent` when available.
8. Availability/fallback: controller fallback from `AMD-001-CHECK-008` with disclosure and operator authorization.
9. Selection reason: the policy has broad process blast radius and the review must be independent from the controller that reconciles the tightly coupled surfaces.
10. Write authority: read-only.
11. Parallel execution: No; run after integrated validation.
12. Blast radius if wrong: High; a missed contradiction affects future planning and execution handoffs.
13. Concurrency: one reviewer after implementation.

## Planning shape and transition ownership

1. Planning shape: approved amendment to the frozen combined small/medium package.
2. Amendment file: `plan_amendment-01_selection-policy-consistency_task-orchestration-model-policy.md`.
3. Transition owner: this amendment.
4. Documented resumed stage: `plan execution`.
5. Frozen package after approval: original spec, original plan, original architecture snapshot, and this amendment.
6. Implementation baseline: amendment approval commit, which must descend from `8832fce67e4a9dafb8c2b29254c340ecd3267db5`.
7. Execution checkout: the current repository checkout on non-default branch `0.9-clarifications`; no additional worktree or branch is required.

## Approved next stage

### Next lifecycle stage

Stage: `plan execution`.

### Orchestration

Method: `superpowers:executing-plans`.
Orchestration mode: `bounded delegated sub-agents` with one read-only final reviewer and no executor sub-agents.
Run in: `same orchestration session`.
Review: execution-controller checkpoints plus the approved independent final policy reviewer; use the disclosed controller fallback only with the governed operator decision.

### Model

Generation: `latest available`.
Capability tier: `balanced`.
Reasoning: `high`.

### Fallbacks and limits

1. The independent reviewer strategy is operator-approved.
2. If Superpowers is unavailable, use host-native task-by-task execution with the same frozen scope, checks, reviewer decision, and final-integration ownership.
3. Load the original frozen package, approved amendment, approval/baseline commits, current branch state, and local operator diff before edits.
4. Stop for any change to `enterprise-default`, lifecycle stages, module or rule ownership, the execution-method ordering, capability-tier meanings, authorization boundaries, or another material scope not approved here.

## Planned commits

| Stage | Planned subject |
|---|---|
| Amendment approval | `amendment-01: task-orchestration-model-policy -- approve selection-policy corrections` |
| Amended implementation | `docs: task-orchestration-model-policy -- align orchestration and model selection` |

One cohesive amended implementation commit is required because canonical policy, lifecycle/freeze consumers, template sources, generated outputs, validation, and changelog evidence form one compatibility boundary.

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: Operator message `approved` on 2026-08-02
- Superseded by: None

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until the operator explicitly approves this amendment and its approval commit freezes it. After freeze, stop and require a fresh implementation instruction before changing implementation targets; the local operator edit remains in place throughout the amendment-only approval commit.
