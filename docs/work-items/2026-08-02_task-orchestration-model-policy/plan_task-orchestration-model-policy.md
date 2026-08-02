# Orchestration and Model Policy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Use the bounded independent reviewer only when the operator approves it at freeze or in a later explicit instruction.

Work ID: `2026-08-02_task-orchestration-model-policy`
Short ID: `task-orchestration-model-policy`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:artifact-style`, `module:models`, `module:architecture`, `module:execution-quality`, `module:implementation-changelog`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`
Execution method: `superpowers:executing-plans`
Current planning Codex task: Model/profile, reasoning, and context visibility: `not exposed`.

**Goal:** Reorganize the current orchestration/model policy, adopt portable orchestration-session terminology, make method/review stage-sensitive, and propagate the resulting contract without losing existing safeguards.

**Architecture:** Add a lifecycle-owned stage-boundary rule, then make `module:models` consume the stage and own how it runs. Keep the stable module path and ID, update direct current consumers through source templates and generated outputs, and enforce the ownership, terminology, stage applicability, three model dimensions, and rule-preservation inventory with focused validator checks.

**Tech stack:** Markdown canonical policy and templates, JSON template assemblies, Python 3 template assembler and policy validator, Git.

## Global Constraints

1. Treat `spec_task-orchestration-model-policy.md` and `snapshots/architecture.snapshot.md` as authoritative; do not reconstruct scope from the original chat or copy the operator's partial draft wholesale.
2. Keep `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` and `module:models` stable.
3. Add `rule:lifecycle.stage-boundaries`; replace only the current continuity interface with `rule:models.next-stage-continuity`.
4. Keep lifecycle stages, planning shapes, execution-method cascade, `enterprise-default`, active `economy-default`, capability-tier meanings, GPT-5.6 mappings, context strategies, concurrency cap, authorization boundaries, and final-integration ownership unchanged.
5. Model selection has three independent dimensions: generation, capability tier, and reasoning effort. A resolved profile is a runtime mapping, not a fourth durable dimension.
6. Use **orchestration session** only for the top-level operator-facing conversation/controller context; retain Plan Task, agent/sub-agent run, and external method session as distinct concepts.
7. Preserve the model/reviewer assessment before spec drafting without adding a pre-spec artifact, stage, gate, or mandatory reviewer.
8. Update template source blocks before generated templates and regenerate only through `assemble_templates.py --write`.
9. Do not modify pre-existing frozen work-item artifacts, the original checkout's uncommitted draft, root `CHANGELOG.md`, runtime configuration, or provider tooling.
10. Keep one cohesive implementation commit because policy owners, current consumers, generated outputs, validation, and changelog source form one compatibility boundary.

## Input Artifacts

Read these before implementation:

1. Approved spec: `docs/work-items/2026-08-02_task-orchestration-model-policy/spec_task-orchestration-model-policy.md`.
2. Approved architecture snapshot: `docs/work-items/2026-08-02_task-orchestration-model-policy/snapshots/architecture.snapshot.md`.
3. Approved plan: `docs/work-items/2026-08-02_task-orchestration-model-policy/plan_task-orchestration-model-policy.md`.
4. Applicable root and nested `AGENTS.md` instructions plus `.agents/skills/dev-doc-harness/SKILL.md`.
5. Current canonical modules and template sources named under `Change surfaces`.
6. Prior related frozen context: `docs/work-items/2026-07-11_model-selection-dimensions/` for preserved model-dimension and handoff intent only; current canonical policy remains authoritative.
7. Unresolved implementation context: none. Material disagreement between the approved package and current repository state follows `rule:lifecycle.variance-policy`.

## Traceability approach

A compact mapping is required because one canonical rewrite has multiple generated and operator-facing consumers, and the mapping prevents a preservation or propagation gap.

| Commitment / criterion | Owning tasks | Final evidence |
|---|---|---|
| `SPEC-001` / `VER-001` Broadened scope and stable identity | `TASK-001`, `TASK-002` | `CHECK-006`, `CHECK-008` |
| `SPEC-002` / `VER-002` Lifecycle stage owner | `TASK-001` | `CHECK-006`, `CHECK-007` |
| `SPEC-003` / `VER-003` Session terminology and continuity | `TASK-001`, `TASK-002` | `CHECK-004`, `CHECK-006` |
| `SPEC-004` / `VER-004` Stage-sensitive method/review | `TASK-001`, `TASK-002` | `CHECK-003`, `CHECK-005`, `CHECK-006` |
| `SPEC-005` / `VER-005` Generation, tier, effort | `TASK-001`, `TASK-002` | `CHECK-003`, `CHECK-005`, `CHECK-006` |
| `SPEC-006` / `VER-006` Strategy-rule preservation | `TASK-001`, `TASK-003` | `CHECK-002`, `CHECK-006`, `CHECK-008` |
| `SPEC-007` / `VER-007` Thin notation | `TASK-001`, `TASK-002` | `CHECK-006`, `CHECK-008` |
| `SPEC-008` / `VER-008` Consumer/template parity | `TASK-002`, `TASK-003` | `CHECK-005`, `CHECK-006`, `CHECK-007` |
| `SPEC-009` / `VER-009` Pre-spec assessment boundary | `TASK-001`, `TASK-003` | `CHECK-006`, `CHECK-008` |

## Change surfaces

Canonical owners and consumers:

1. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: retitle and reorder the module; define terminology, upcoming-stage selection, stage method/review, next-stage continuity, three model dimensions, named strategy subsections, thin notation, reporting, review, and integration.
2. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: own `rule:lifecycle.stage-boundaries`, cite the renamed continuity interface, and use orchestration-session terminology where the text means the top-level owner.
3. `.agents/skills/dev-doc-harness/references/maintenance-architecture.md`: align the `module:models` catalog entry with its broadened current responsibilities.
4. `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: render stage-appropriate `Review`, use the new same/new-session values and continuity owner, and retain authorization/transition behavior.
5. `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`: use execution-session wording for the existing implementation-only startup protocol while retaining `rule:execution-quality.execution-thread-start` as a stable rule ID.
6. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`: use orchestration-session wording for the phase-plan coordination boundary.
7. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`: retain optional role examples and align top-level ownership/model-dimension terminology.
8. `.agents/skills/dev-doc-harness/SKILL.md`: broaden the model/orchestration operation route and completion wording without copying canonical rules.
9. `README.md` and `AGENTS.md`: align compact current operator guidance and continuity terms without becoming policy owners.

Template sources:

1. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.small.header-inputs.md`.
2. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.010.phase.header-objective-inputs.md`.
3. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.040.common.model-strategy.md`.
4. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.small.handoff.md`.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.phase.handoff.md`.
6. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.small.readiness-completion-approval.md`.
7. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.phase.readiness-completion-approval.md`.
8. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.060.large.phase-decomposition-model.md`.
9. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.085.small.handoff.md`.
10. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.085.large.handoff.md`.
11. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.090.large.readiness-approval.md`.

Generated outputs, written only by the assembler:

1. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`.
2. `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`.
3. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`.
4. `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`.

Validation and delivery:

1. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: update owner, terminology, selection, stage-method/review, presentation, template, execution-start, and scenario fixtures; add explicit preservation assertions where current coverage would otherwise be lost.
2. `docs/work-items/2026-08-02_task-orchestration-model-policy/changelog/implementation-fragment.md`: record the delivered distributable policy/template change before the implementation commit.

No assembly manifest change is planned because existing source blocks and output composition remain sufficient. Add or change a manifest only if implementation evidence proves that the approved placement cannot be achieved with the current blocks; that would be a routine variance only if output schema and ownership remain unchanged.

## Implementation approach

Use test-first policy maintenance. First change focused validator expectations to the approved owner and semantic contract and confirm that they fail against the old policy. Then rewrite canonical owners and narrow failures to direct consumers. Update current references and template source blocks, regenerate outputs, and make the full suite pass. Finish with a rule-preservation review, stale-term search, changelog fragment, and one cohesive commit.

Do not mechanically replace every occurrence of `task`, `thread`, or `session`. For each changed occurrence, verify that it denotes the top-level orchestration-session concept. Preserve Codex as a product/method name, Plan Task as an approved plan unit, sub-agent run as delegated execution, and external method session as a separate controller.

## Model and Sub-agent Strategy

Upcoming-stage sub-agent assessment:

1. Sub-agents: one operator-authorized read-only `final-policy-reviewer`; no executor sub-agents.
2. Fit reason: implementation is tightly coupled across one canonical policy and its consumers, so one execution controller should own all edits. An independent final reviewer can materially reduce the high process-blast-radius risk of lost rules or contradictory stage/session semantics.
3. Authorization state: `Approved` by the operator on 2026-08-02.
4. Fallback: if the reviewer is unavailable or not approved, the execution controller performs the explicit `CHECK-008` rule-preservation and contradiction review and discloses the lack of independent review in the completion report.

Sub-agent `final-policy-reviewer`:

1. Purpose: independently review the completed diff for rule loss, duplicate ownership, planning/execution applicability errors, session-term ambiguity, model-dimension conflation, template drift, and historical changes.
2. Context strategy: `curated artifacts`.
3. Input context: the frozen spec, plan, architecture snapshot, completed diff, template-assembler result, full validator result, stale-term search, and implementation changelog fragment.
4. Output artifact: evidence-backed blocking/nonblocking findings reported to the orchestration session and summarized in the implementation completion report.
5. Model policy: active repository `economy-default` with a justified review escalation.
6. Model generation: `GPT-5.6`.
7. Capability tier: `flagship`.
8. Resolved profile: `Sol`.
9. Availability/fallback: use Sol/high when available; otherwise use the focused controller self-review in `CHECK-008` and disclose that independent review could not run.
10. Reasoning effort: `high`, because missed process-policy regressions can affect every later work item.
11. Selection reason: independent adversarial review is more valuable than parallel implementation for this tightly coupled rewrite.
12. Write authority: read-only; findings only.
13. Parallel execution: `No`; run after all planned validation so the reviewer sees the integrated result.
14. Blast radius if wrong: `High`; a missed or incorrect finding can preserve a policy contradiction or block a valid current workflow.

Recommended execution allocation:

1. Method: `superpowers:executing-plans` because tasks share canonical concepts and several files; sequential controller ownership is safer than fresh executor sub-agents editing overlapping surfaces.
2. Model generation: `latest available`.
3. Capability tier: `balanced`.
4. Reasoning effort: `high` for careful cross-reference and rule-preservation traversal.
5. Orchestration mode: `bounded delegated sub-agents` with the authorized final reviewer; fall back to `single-agent` with the recorded assurance disclosure only if Sol/high is unavailable.
6. Continuity: `new Codex task` under the current pre-change policy, using the frozen package and the existing isolated worktree branch.

## Implementation tasks

### `TASK-001` Establish the new canonical ownership and semantics

Dependencies: frozen planning package and fresh implementation authorization.

Interfaces:

1. Consumes: approved `SPEC-001` through `SPEC-009`, `DEC-001` through `DEC-005`, current rule-owner tables, and the passing baseline.
2. Produces: updated canonical lifecycle/models/architecture owners and failing-then-focused validator expectations for direct consumers.

Implementation:

1. Re-read the frozen package, applicable instructions, current canonical targets, branch, worktree status, and the baseline command recorded in `CHECK-001` before editing.
2. Inventory every current `rule:models.*` owner and each distinct obligation under terminology, selection dimensions, orchestration, continuity, method/reviewer contract, common rules, both policy profiles, independent review, required notation, report requirements, escalation, final review, and final integration.
3. Update `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` first so focused assertions expect the broadened title/scope, `rule:lifecycle.stage-boundaries`, `rule:models.next-stage-continuity`, orchestration-session vocabulary, planning-stage and execution-stage Method/Review fixtures, three model dimensions, thin notation, preserved strategy/report/review obligations, and unchanged policy/cascade/tier/concurrency semantics.
4. Run the full validator and confirm it fails for the old canonical/current-consumer contract rather than unrelated baseline behavior.
5. Add `rule:lifecycle.stage-boundaries` to the lifecycle owner table and keep the existing stage mapping solely in that section. Change lifecycle references from top-level thread/task terminology to orchestration-session terminology only where they denote the governed concept.
6. Rewrite `subagent-model-policy.md` in this order: broader scope and owner table; task/session terminology; upcoming-stage selection; next-stage method and review; next-stage continuity; orchestration mode; model and reasoning; sub-agent strategy with required assessment/authorization, role/context, and fit/concurrency subsections; enterprise/economy policies; review and integration; required notation; runtime report requirements.
7. In the rewrite, preserve the implementation method cascade and exact route-specific reviewer obligations, keep spec drafting in the required assessment, and record the durable pre-spec selection mechanism as future work rather than an implemented gate.
8. Make `Required notation` a thin rendering contract and point optional examples to `module:role-examples`; remove the embedded four-row normative-file example table.
9. Update the `module:models` catalog entry in `maintenance-architecture.md` to reflect stage orchestration, three model dimensions, next-stage continuity, sub-agent strategy, review, reporting, and final integration.
10. Run the full validator. At this intermediate point, every remaining failure must identify a direct consumer scheduled in `TASK-002`; resolve any owner, canonical semantic, or unrelated failure before proceeding.

Exit criteria: canonical ownership and semantics match the approved architecture; the validator's remaining failures are limited to named direct consumers and generated outputs.

#### `CHECK-001` Confirm clean implementation baseline

Covers: `VER-008`.

Method: Run `git status --short`, `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`, and `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` before implementation edits.

Expected result: the isolated branch contains only the frozen planning package at its approval commit, template assembly reports current outputs, and every baseline harness check passes.

Evidence record: execution log and implementation completion report.

#### `CHECK-002` Preserve the canonical rule inventory

Covers: `VER-001`, `VER-002`, `VER-006`, `VER-007`, `VER-009`.

Method: Compare the pre-edit obligation inventory with the rewritten owner table/sections and run the focused model/lifecycle validator assertions after canonical edits.

Expected result: every material current obligation has one named destination, new/replaced rules have one owner, no lifecycle mapping is copied into `module:models`, and only planned consumer-parity failures remain.

Evidence record: validator output plus the rule-preservation notes summarized in the completion report.

### `TASK-002` Propagate the contract through current consumers and templates

Dependencies: `TASK-001` canonical owners and focused validator expectations.

Interfaces:

1. Consumes: updated canonical rule IDs, defined terminology, selection groups, Method/Review applicability, and current template assembly structure.
2. Produces: aligned freeze/startup/quality/router/example/root-guidance consumers, updated template source blocks, and regenerated primary templates.

Implementation:

1. Update `planning-freeze-gates.md` to render the general `Review` field, consume `rule:models.next-stage-continuity`, use `same/new orchestration session`, and preserve existing approval, override, task-creation, and post-freeze authorization behavior.
2. Update `context-and-quality-gates.md` to say execution session where the implementation-only startup rule currently says execution task/thread; retain `rule:execution-quality.execution-thread-start` as a stable identifier and do not generalize this implementation startup rule into a new planning gate.
3. Update `durable-planning-quality.md`, `subagent-role-examples.md`, and remaining lifecycle text where `orchestration thread` denotes the top-level orchestration session. Preserve role/report meaning and keep examples advisory.
4. Update `SKILL.md`, `README.md`, and `AGENTS.md` with compact current terminology and rule references. Do not duplicate canonical selection or continuity prose.
5. Update the two plan header blocks to replace `Current planning Codex task` with a compact optional `Current orchestration session` prompt listing generation, capability tier, reasoning, resolved profile, and context visibility; instruct artifact authors to record exposed facts or omit the line.
6. Update `plan.040.common.model-strategy.md` to prompt for the preserved strategy fields and separate generation, capability tier, reasoning effort, resolved profile, availability/fallback, authorization, context, concurrency, and blast radius without reintroducing semantic definitions owned by `module:models`.
7. Update small/phase handoff blocks to render: Stage; Method; `Run in`; general Review; Generation; Capability tier; Reasoning; and only applicable Fallbacks and limits. Use planning-stage review wording in the large anchor path and execution-stage Plan Task/final-review wording in execution plans.
8. Update readiness blocks and large-spec model/strategy blocks to de-emphasize optional current-session facts, use the new session values, and validate the three model dimensions and stage-appropriate Review field.
9. Update small/large spec handoff blocks to cite `rule:models.next-stage-continuity` while retaining current freeze/startup owners.
10. Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` once, inspect the four generated outputs, and then run `--check`.
11. Run the full policy validator and resolve every current consumer or fixture failure at its canonical/source owner. Do not patch generated output directly.

Exit criteria: all current consumers agree, all four generated templates match their sources, and the full validator passes.

#### `CHECK-003` Validate planning and execution selection fixtures

Covers: `VER-003`, `VER-004`, `VER-005`.

Method: Run the updated focused validator fixtures for one planning-stage selection (`phase-plan drafting` with planning Method/Review) and one execution-stage selection (`plan execution` with execution Method and Plan Task/final Review).

Expected result: both accept explicit Generation, Capability tier, Reasoning, and same/new orchestration-session continuity; execution-only reviewer terms are not required for the planning-stage fixture.

Evidence record: focused check IDs in full validator output.

#### `CHECK-004` Confirm scoped terminology migration

Covers: `VER-003`, `VER-009`.

Method: Run `rg -n "Codex task|Codex-task|Current planning Codex task|execution Codex task|orchestration thread|rule:models\.execution-continuity" .agents/skills/dev-doc-harness/references .agents/skills/dev-doc-harness/assets/templates .agents/skills/dev-doc-harness/SKILL.md README.md AGENTS.md` and inspect every result.

Expected result: no current occurrence remains where the text denotes the migrated top-level orchestration-session or continuity concept; any retained match is an intentional product-specific name, stable implementation-only identifier, or clearly documented compatibility exception.

Evidence record: scoped search output and exception list, if any, in the completion report.

#### `CHECK-005` Verify template source/generated parity

Covers: `VER-004`, `VER-005`, `VER-008`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` and inspect the selection blocks in all four generated primary templates.

Expected result: command exits `0` with `All assembled templates are current.`; generated selections use Stage, Method, Run in, Review, Generation, Capability tier, Reasoning, and applicable Fallbacks and limits with correct stage applicability.

Evidence record: assembler output and generated-template inspection notes.

### `TASK-003` Review, record, validate, and commit the integrated change

Dependencies: `TASK-002` complete with passing current consumers and generated outputs.

Interfaces:

1. Consumes: integrated canonical/consumer/template/validator diff and the authorized reviewer strategy.
2. Produces: final validation evidence, reviewer or fallback review findings, implementation changelog fragment, and one cohesive implementation commit.

Implementation:

1. Run `CHECK-004` through `CHECK-007` on the integrated diff and resolve all in-scope failures.
2. Verify `git diff --name-only -- docs/work-items` shows no modified pre-existing work-item artifact; the only uncommitted work-item path at implementation completion may be this work item's new implementation fragment.
3. Dispatch the authorized `final-policy-reviewer` with exactly the curated inputs recorded above when Sol/high is available. If it is unavailable, perform `CHECK-008` in the execution controller and record the independent-review limitation and fallback evidence.
4. Resolve blocking in-scope findings and rerun every affected check. Route a material ownership, scope, lifecycle, method-cascade, authorization, tier, or review-contract change through the amendment process.
5. Create `docs/work-items/2026-08-02_task-orchestration-model-policy/changelog/implementation-fragment.md` with exactly this initial entry:

   ```md
   ### 2026-08-02 docs: task-orchestration-model-policy -- clarify session and stage selection

   Meta -- `unreleased` : `distributable`

   #### Changed

   - Reorganized the model policy around lifecycle-owned stages and stage-appropriate orchestration, review, continuity, and model selection.
   - Replaced top-level Codex-task terminology with portable orchestration-session terminology across current policy and templates.
   - Preserved sub-agent authorization, context, concurrency, review, reporting, and integration safeguards with focused validation.
   ```

6. Run `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint`, the assembler check, the full policy validator, the scoped terminology search, and `git diff --check` after adding the fragment.
7. Inspect `git diff --stat` and the full diff for unrelated changes, copied policy, lost rules, placeholder text, direct generated edits, historical modifications, and accidental changes to the original checkout.
8. Stage only approved implementation paths and the implementation fragment, inspect `git diff --cached --name-only` and `git diff --cached --check`, then commit `docs: task-orchestration-model-policy -- clarify session and stage selection`.

Exit criteria: all commitments conform, review has no blocking findings, the fragment lints, one cohesive commit contains only approved implementation paths, and completion reports actual model/session/reviewer/fallback use.

#### `CHECK-006` Run the full harness policy suite

Covers: `VER-001`, `VER-002`, `VER-003`, `VER-004`, `VER-005`, `VER-006`, `VER-007`, `VER-008`, `VER-009`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Expected result: exit `0`; every owner, graph, template, lifecycle, model-selection, execution-start, presentation, compatibility, and clarity check passes.

Evidence record: complete command output summarized by check IDs in the implementation completion report.

#### `CHECK-007` Verify generated and repository diff integrity

Covers: `VER-002`, `VER-008`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`, `git diff --check`, `git diff --name-only -- docs/work-items`, and inspect `git diff --stat` plus the full diff.

Expected result: templates are current; no whitespace errors exist; no pre-existing historical work item changed; all generated changes derive from named source blocks; no unrelated file appears.

Evidence record: command outputs and final diff review summary.

#### `CHECK-008` Review rule preservation and contradictions

Covers: `VER-001`, `VER-003`, `VER-004`, `VER-006`, `VER-007`, `VER-009`.

Method: Use the authorized independent reviewer or the documented controller fallback to compare the frozen commitments/decisions, pre-edit rule inventory, and final integrated diff with named lenses: ownership, rule loss, duplicate semantics, stage applicability, terminology ambiguity, model-dimension separation, authorization/reviewer safety, and pre-spec boundary.

Expected result: no blocking finding remains; every nonblocking residual risk is recorded; the completion report identifies whether review was independent or fallback self-review.

Evidence record: reviewer findings or focused fallback review notes in the implementation completion report.

#### `CHECK-009` Validate implementation changelog source

Covers: `VER-008`.

Method: Run `python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint` after creating the fragment.

Expected result: exit `0`; fragment heading matches the planned implementation subject, metadata is `unreleased : distributable`, and the fragment is eligible for later operator-owned consolidation.

Evidence record: lint output and committed fragment path.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: task-orchestration-model-policy -- approve session-oriented selection contract` |
| Implementation | `docs: task-orchestration-model-policy -- clarify session and stage selection` |

The planning approval commit contains only the spec, plan, and architecture snapshot. The implementation commit contains current policy/consumer/template/validator changes plus `changelog/implementation-fragment.md`; it does not consolidate root `CHANGELOG.md`.

## Validation and variance

`CHECK-001` establishes the baseline. `CHECK-002` protects rule preservation during canonical movement. `CHECK-003` through `CHECK-005` protect semantics and template propagation. `CHECK-006` through `CHECK-009` provide final conformance, diff, review, and changelog evidence.

Routine variance may adjust exact prose, section subheading names, validator helper layout, or the set of source blocks touched when the approved owner, terminology, stage applicability, selection fields, and evidence purpose stay unchanged. Create an amendment and ask the operator before changing module/rule ownership, the orchestration-session definition, lifecycle stages, planning/execution method applicability, the three model dimensions, policy/tier semantics, authorization/reviewer obligations, pre-spec scope, historical immutability, or required evidence.

## Implementation handoff

### Approved next stage

#### Next lifecycle stage

Stage: `plan execution`.

#### Orchestration

Method: `superpowers:executing-plans`; Run in: `new Codex task`; Plan Task reviewers: `execution-controller checkpoints plus the authorized read-only GPT-5.6 Sol/high independent final policy reviewer, with the disclosed CHECK-008 controller fallback only if Sol/high is unavailable`.

#### Model

Generation: `latest available`; Capability tier: `balanced`; Reasoning: `high`.

#### Fallbacks and limits

1. If Superpowers is unavailable, use native Codex task-by-task execution with the same frozen scope, checks, and reviewer/fallback boundary.
2. The GPT-5.6 Sol/high final reviewer is operator-authorized. If Sol/high is unavailable, use the focused self-review fallback and disclose the assurance gap.
3. Frozen package: `spec_task-orchestration-model-policy.md`, `plan_task-orchestration-model-policy.md`, and `snapshots/architecture.snapshot.md` from this work item.
4. Artifact rehydration: load applicable instructions, harness, exact frozen package, approval commit, current branch/worktree state, and the documented plan-execution stage through `rule:execution-quality.execution-thread-start`.
5. Variance stop condition: stop for any material change named in `Validation and variance`.

Copy-ready handoff after freeze:

```text
Implement `2026-08-02_task-orchestration-model-policy` in the existing isolated
worktree on `codex/task-orchestration-model-policy` from its frozen package:

- `docs/work-items/2026-08-02_task-orchestration-model-policy/spec_task-orchestration-model-policy.md`
- `docs/work-items/2026-08-02_task-orchestration-model-policy/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-08-02_task-orchestration-model-policy/plan_task-orchestration-model-policy.md`

Follow applicable `AGENTS.md`, the repository harness, and
`rule:execution-quality.execution-thread-start`. Use
`superpowers:executing-plans`, latest-available balanced/high execution, and
the approved reviewer strategy or recorded fallback. Start with `TASK-001`,
preserve the original checkout's uncommitted draft, and stop for material
variance.
```

## Readiness

- [x] Current planning Codex task facts are separate from the actionable Approved next stage.
- [x] Inputs, scope, exact change surfaces, tasks, checks, documentation, and implementation changelog source are clear.
- [x] The execution selection, implementation handoff, and authorized Sol/high final reviewer are explicit.
- [x] Model generation, capability tier, and reasoning effort are selected independently.
- [x] Planning-stage versus execution-stage Method/Review behavior is preserved in tasks and checks.
- [x] Existing rule preservation and the pre-spec future boundary have explicit evidence paths.
- [x] No required decision, placeholder, or ownerless deferral remains.

## Completion

1. `SPEC-001` through `SPEC-009` conform through `CHECK-001` through `CHECK-009` as applicable.
2. Canonical owners, current consumers, source templates, generated outputs, root guidance, and validator fixtures agree.
3. No pre-existing historical work item or original-checkout operator draft changes.
4. The implementation fragment lints and the one cohesive implementation commit is complete.
5. Completion reports the de-facto model generation, tier, reasoning, orchestration mode, session continuity, reviewer use, fallback, validation evidence, variance, and residual risk.

## Approval

- Status: Approved
- Grouped selection: **Approved next stage**.
- Superseded by: None
