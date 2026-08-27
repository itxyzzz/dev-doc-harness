# Quality and Efficiency Policy Spec

Work ID: `2026-08-27_quality-efficiency-policy`
Short ID: `quality-efficiency-policy`
Status: Approved
Harness release: `0.10+`
Schema: `schema:spec.medium`
Companion plan: `plan_quality-efficiency-policy.md`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:lifecycle.documentation-assessment`, `rule:lifecycle.work-item-architecture-decisions`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make the model and delegation policy easier to select from by naming its two profile biases `quality-first` and `efficiency-first`, placing model selection beside orchestration selection, and preserving the shared quality, authorization, and review foundation.

## Source and Intent

Source input:

1. The operator's 2026-08-27 review of the current `enterprise-default` and `economy-default` policies, their fit to GPT-5.6 Sol, Terra, and Luna, and the current delegation model.
2. The operator approved `quality-first` and `efficiency-first` as the replacement profile names.
3. The operator directed that the generic model, delegation, isolation, write-authority, authorization, escalation, and review rules remain canonical outside the profiles.
4. The operator directed that model selection sit under `## Upcoming-stage selection` beside orchestration selection, and that the profile section cover both model and orchestration selection.

Desired operator outcome:

1. A planner can see that model and orchestration are coordinated next-stage decisions, then choose a lightweight quality or efficiency bias without re-reading a second set of generic rules.
2. A maintainer can use extra sub-agent coverage under `quality-first`, or constrain optional fan-out under `efficiency-first`, without weakening the shared independent-review floor.

Success summary:

1. Current policy, active guidance, template prompts, generated templates, and validator fixtures use the new profile names and the same selection hierarchy.
2. The profiles add only tie-breaking model and orchestration biases; they do not create a new calculation, planning field, reviewer exception, or delegation authorization route.

## Scope Boundary

### In scope

1. Reorganize `subagent-model-policy.md` so `### Model selection` is a peer of `### Orchestration selection` below `## Upcoming-stage selection`; move Model facets and policies beneath it and rename the policy heading to `#### Model and orchestration selection policies`.
2. Replace current-profile vocabulary and owned rule IDs with `quality-first` and `efficiency-first` in all live policy and distribution surfaces.
3. Define profile-local model and orchestration biases: quality-first favors justified capability, reasoning, coverage, and fan-out; efficiency-first favors the least total expected delivery cost while preserving required review and isolation.
4. Keep the current Terra/Sol allocation ladder, direct high-impact `flagship/high` exception, and narrowed fast/economy boundary as agreed during the review.
5. Update active `AGENTS.md` and README bootstrap wording, model-strategy source blocks, generated templates, validator helpers/assertions/fixtures, and implementation documentation outputs.
6. Validate canonical hierarchy, profile semantics, source/generated parity, current live references, and historical immutability.

### Non-scope

1. Change the generic model facets, GPT-5.6 Sol/Terra/Luna mapping, shared allocation and escalation rules outside the profile bodies, authorization rules, write-authority rules, concurrency cap, reviewer contract, or final integration owner. The agreed profile-local Terra/Sol selection ladder refinements and fast/economy boundary are in scope.
2. Add Pro-mode guidance, runtime probing, cost calculation, a new plan field, a new approval gate, or a delegation business-case artifact.
3. Treat Ultra as a preferred delegation mechanism; profile wording must assess the available suite of bounded sub-agents, platform multi-agent/Ultra, and hybrid orchestration as applicable.
4. Rewrite frozen work items, historical root changelog entries, or released `0.7.0` release notes that retain the retired names as historical evidence.
5. Release or package a new Dev Doc Harness distribution version.

## Repository Context

### Current state

1. `subagent-model-policy.md` has `### Orchestration selection` under `## Upcoming-stage selection`, but starts `## Model selection` later at the top level.
2. The policy calls the profiles `enterprise-default` and `economy-default`; the first separately assesses platform multi-agent/Ultra, while shared rules already govern authorization, context, allocation, review, and fan-out.
3. The root `AGENTS.md`, README bootstrap example, two model-strategy source blocks, three generated templates, and focused validator still name `economy-default` or `enterprise-default`.
4. `test_harness_policy.py` extracts Model selection with an H2-only helper and contains current-profile assertions and literal policy fixtures.
5. On branch `policies-update`, `assemble_templates.py --check` and `test_harness_policy.py` pass before planning changes.

### Evidence read

1. Operator discussion in this task, including the agreed hierarchy, profile names, delegation constraints, and planning request.
2. `.agents/skills/dev-doc-harness/SKILL.md`.
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md`, `durable-planning-quality.md`, `naming-conventions.md`, `planning-freeze-gates.md`, `context-and-quality-gates.md`, and `subagent-model-policy.md`.
4. `.agents/skills/dev-doc-harness/assets/templates/medium-work-item-spec.md`, `medium-work-item-plan.md`, `architecture-snapshot.md`, the two affected source blocks, assembly manifests, and `scripts/assemble_templates.py`.
5. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, root `AGENTS.md`, root `README.md`, and the prior `2026-08-02_task-orchestration-model-policy` package.
6. The 2026-08-27 passing output from `assemble_templates.py --check` and `test_harness_policy.py`.

### Constraints and compatibility

1. Canonical reusable policy remains in `subagent-model-policy.md`; templates prompt and generated files render it without duplicating it.
2. Template outputs are generated only through `assemble_templates.py --write` after source-block edits.
3. Current live names and rule IDs migrate together. Historical artifacts retain old terms and are not compatibility consumers.
4. `quality-first` and `efficiency-first` are profile biases over the generic foundation, not replacement policy systems.
5. The planning package must freeze before any implementation starts.

## Assumptions and Open Questions

### Assumptions

1. `quality-first` and `efficiency-first` replace the old names without a live compatibility alias because no current live consumer selects the old profile names.
2. The existing conditional next-stage rationale is sufficient for non-obvious total-delivery tradeoffs; it can name decisive factors but must not become an estimation procedure.
3. The execution method can use bounded delegated sub-agents with task-local write ownership and independent review after each task, as allowed by the selected method and operator authorization.

### Open questions

1. None identified after repository-context review.

## Commitments and verification

### `SPEC-001` Align the next-stage selection hierarchy

Statement:

1. The canonical policy must place Model selection as a peer of Orchestration selection under Upcoming-stage selection, give both topics clear nested ownership, and preserve all existing generic policy sections outside the profile bodies.

#### `VER-001` Nested selection contract

Covers: `SPEC-001`.

Criterion: Canonical headings, owner-table links, and validator section extraction identify the new hierarchy without weakening Model facets, Current-session diagnostics, or Required notation.

Expected evidence: Focused validator assertions and policy diff inspection.

### `SPEC-002` Rename and bound the policy profiles

Statement:

1. Live reusable surfaces must call the profiles `quality-first` and `efficiency-first` and use matching rule IDs.
2. Quality-first must favor justified quality, independent coverage, and decomposable fan-out; efficiency-first must favor the least total expected delivery cost while retaining shared review and isolation requirements.
3. Neither profile may add a calculation, mandatory field, new authorization route, or different write-authority rule.

#### `VER-002` Profile semantics and live-name parity

Covers: `SPEC-002`.

Criterion: Canonical text and focused validator assertions capture both profile biases, current live sources contain only the new names, and any old-name match is confined to immutable history.

Expected evidence: Validator output, scoped `rg` result, and path-limited diff inspection.

### `SPEC-003` Preserve efficient, quality-safe delegation

Statement:

1. The shared independent-review, authorization, isolation, context, write-authority, concurrency, and integration rules must remain the floor for both profiles.
2. The existing concise rationale for a non-obvious combined Model and Orchestration selection must be extended only to permit decisive factors such as coverage, coordination risk, elapsed time, or expected rework.
3. Fast/economy work must remain bounded supporting work with no final decision authority, and a direct `flagship/high` exception must stay narrowly documented for known high-blast-radius work requiring both difficult judgment and broad traversal.

#### `VER-003` Delegation and escalation guardrails

Covers: `SPEC-003`.

Criterion: The canonical policy preserves the generic guardrails, uses the agreed lightweight rationale wording, and validator checks reject a profile wording that demotes the required reviewer floor or broadens fast/economy authority.

Expected evidence: Focused assertions, policy review, and independent reviewer findings.

### `SPEC-004` Propagate current consumers and generated templates

Statement:

1. Active guidance, template source blocks, generated templates, and validator fixtures must migrate together; generated files must be refreshed only through the assembler.
2. The work item must record the policy and operator-guidance changes, but must not modify historical artifacts or release records.

#### `VER-004` Current-consumer parity

Covers: `SPEC-004`.

Criterion: The assembler and full validator pass, source and generated prompts agree, root guidance selects efficiency-first, and the final diff excludes pre-existing work items and historical release records.

Expected evidence: Assembler output, full validator output, scoped search output, `git diff --check`, and final diff review.

## Architecture Decisions

Architecture snapshot status:

1. Required — the policy hierarchy, profile identity, and selection boundaries govern all future harness work and must be available to a fresh executor.

Decision summary:

1. Drivers: clear profile names, model/orchestration symmetry, preserved generic safeguards, and low planning overhead.
2. Constraints: stable module path, source-generated template ownership, immutable history, current validation baseline, and no Pro-mode scope.
3. Selected approach: use the three decisions in `snapshots/architecture.snapshot.md` as execution constraints.
4. Affected boundaries: canonical model policy, root distribution guidance, template sources/outputs, validator structure/fixtures, and this work-item documentation.
5. Rejected alternatives: retain `enterprise-default`; introduce a compatibility alias; make profiles duplicate generic rules; add numerical delegation-cost estimation; or treat Ultra as the preferred topology.
6. Validation cues: `VER-001` through `VER-004`, their nested Plan Checks, and independent policy review.

## Impact Surfaces

### Interfaces

1. Textual policy-name and rule-ID interface: current `enterprise-default`/`economy-default` selection values and their owner IDs become `quality-first`/`efficiency-first`.
2. Template prompt interface: active model-policy choices in the two source blocks and three generated templates change to the new pair.

### Data, config, and persistence

1. Root `AGENTS.md` changes the selected profile text from economy-default to efficiency-first. No runtime configuration, persistence, or migration exists.

### State and control flow

1. The canonical heading hierarchy changes how readers and the validator traverse the next-stage selection policy; lifecycle stages and execution flow stay unchanged.

### Safety, security, privacy, migration, and rollback

1. Incorrect policy text could weaken future review or delegation decisions. Focused assertions and independent review mitigate this.
2. The textual rename is not backward-compatible in new live artifacts; frozen artifacts remain unchanged and release notes record the migration when the distribution is later released.

## Risks and Rejected Alternatives

### `RISK-001` Generic safeguards are copied or weakened

Decision or mitigation:

1. Keep profiles limited to tie-breaking allocation and orchestration language. Assert that they defer to shared review, authorization, context, write-authority, and concurrency rules.

### `RISK-002` Rename leaves a live stale consumer

Decision or mitigation:

1. Update canonical policy, root guidance, source blocks, generated outputs, validator assertions, and literal fixtures in one change; use a scoped search that excludes immutable history only after inspecting remaining matches.

### `RISK-003` Efficiency introduces planning overhead

Decision or mitigation:

1. Extend only the existing conditional rationale to name decisive factors. Do not add a calculation, estimate, approval step, or required field.

### `RISK-004` Parallelism is mistaken for quality

Decision or mitigation:

1. Quality-first assesses bounded sub-agents, platform multi-agent/Ultra, and hybrid arrangements together. Both profiles retain generic partitioning, authorization, isolation, and reviewer rules.

## Documentation assessment

- `DOC-TEST-CASE`: Required — `snapshots/test-cases.snapshot.md`; Plan Task: `TASK-001`.
- `DOC-TEST-GUIDE`: Not required — contributor test instructions do not change.
- `DOC-OPS-GUIDE`: Required — `deltas/operator-manual.delta.md`; Plan Task: `TASK-003`.
- `DOC-API-GUIDE`: Not required — no public API changes.
- `DOC-ARCH-SUMMARY`: Not required — the work-item architecture snapshot is sufficient; repository-wide architecture documentation is out of scope.

## Planned commits

| Stage | Planned subject |
|---|---|
| Planning approval | `plan: quality-efficiency-policy -- approve profile selection update` |
| Implementation | `docs: quality-efficiency-policy -- align model and orchestration profiles` |

One cohesive implementation commit is expected. It will include the implementation changelog fragment but will not consolidate root `CHANGELOG.md`.

## Planning shape and transition ownership

1. Planning shape: `combined medium`.
2. Companion plan: `plan_quality-efficiency-policy.md` is drafted and presented with this spec in the same planning turn.
3. Transition owner: `plan_quality-efficiency-policy.md` owns the `plan execution` transition after the combined package freezes.
4. Next lifecycle stage: `plan execution`.

## Spec readiness checklist

- [x] Goal, source and intent, scope, constraints, architecture decisions, commitments, and verifications are mutually consistent.
- [x] All material operator input is preserved in this specification, the architecture snapshot, and the test-case snapshot.
- [x] Commitments are bounded and cover the agreed canonical, profile, guardrail, and consumer-propagation outcomes.
- [x] Verification criteria cover every commitment without introducing hidden process or scope.
- [x] This specification and its required snapshots can guide a fresh executor without reconstructing the original discussion.
- [x] Documentation assessment assigns every required output to a Plan Task.
- [x] No unresolved placeholders, plan-affecting decisions, or ownerless deferrals remain.

## Approval

- Status: Approved
- Superseded by: None
