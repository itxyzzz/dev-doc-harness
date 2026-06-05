# Phase 01: Policy Architecture Plan

Work ID: `2026-06-05-refactor-as-code`
Short ID: `refactor-as-code`
Status: Approved

## Objective

Define the target harness policy architecture and rule-interface conventions without moving existing harness behavior yet. Phase 01 produces a frozen architecture snapshot that later phases use before splitting references, slimming templates, or updating the public entrypoint.

## Input context

The implementing agent must read these approved artifacts first:

- `docs/work-items/2026-06-05-refactor-as-code/spec-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-amendment-001-architecture-guardrails-refactor-as-code.md`
- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `AGENTS.md`
- `README.md`

Then inspect these current harness consumers and examples:

- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
- `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
- `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`
- `.agents/skills/dev-doc-harness/assets/templates/`
- Existing tracked and local artifacts under `docs/work-items/`

Preserve all approved spec and amendment decisions. Do not narrow, drop, or reinterpret the requirement to define precedence, dependency direction, content types, operation routing, architecture metrics, golden scenario tests, work-item artifact locality, and rule-versioning deferral.

## Likely files and areas

Create:

- `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`

Modify during Phase 01 execution:

- `CHANGELOG.md`

Do not modify harness source, templates, `README.md`, or root `AGENTS.md` in Phase 01. Later phases will use the approved architecture snapshot to make those changes.

## Model and Sub-agent Strategy

Current orchestration: Codex in this desktop thread; exact model/profile is not exposed in repository artifacts. Operator selected `enterprise-default` for Phase 01 planning and subsequent Phase 01 work.
Fit assessment: Phase 01 is architecture design for the harness itself. The blast radius is high because the output determines policy authority, traversal, template behavior, and validation for all later phases. Under `enterprise-default`, correctness and risk reduction outrank cost minimization.
Recommended change: Use the strongest available reasoning profile for Phase 01 execution and final architecture review. If the platform exposes a latest strongest model/profile choice, use it for architecture review.

| Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|
| Architecture reviewer | curated artifacts | Approved spec, approved amendment, draft `snapshots/architecture.snapshot.md`, current `SKILL.md`, references, templates, README, and `AGENTS.md` | Review findings folded into the architecture snapshot or recorded as no blocking findings | `enterprise-default` | latest strongest available | high | Precedence and dependency mistakes would compromise later phases | No | High: bad architecture can preserve coupling or weaken safety gates |

If sub-agent tools are unavailable, the orchestration thread must perform the same review explicitly and record that limitation in the Phase 01 handoff.

## Tasks

- [ ] **Step 1: Verify clean starting state**

  Run `git status --short --branch`.

  Expected: current branch is `refactor-as-code`; no unstaged or staged files from unrelated work are present.

- [ ] **Step 2: Re-read approved planning inputs**

  Read `spec-refactor-as-code.md` and `plan-amendment-001-architecture-guardrails-refactor-as-code.md`.

  Capture these non-negotiable Phase 01 outputs in working notes before writing the snapshot: precedence model, dependency graph, content-type taxonomy, operation router taxonomy, architectural metrics, golden scenario tests, work-item artifact locality, and explicit deferral of full rule versioning.

- [ ] **Step 3: Inventory current instruction modules and consumers**

  Run these commands:

  ```powershell
  rg --files .agents/skills/dev-doc-harness AGENTS.md README.md docs/work-items
  rg -n "canonical source|only source|Do not|must|Before approval|After .*approved|Context strategy must|Fresh confirmation|Planning artifact freeze gate" .agents/skills/dev-doc-harness AGENTS.md README.md
  ```

  Use the output to identify current policy owners, duplicated policy blocks, template consumers, and root/README summaries.

- [ ] **Step 4: Create the architecture snapshot skeleton**

  Create `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md` with these headings:

  ```md
  # Refactor As Code Architecture Snapshot

  Work ID: `2026-06-05-refactor-as-code`
  Source spec: `../spec-refactor-as-code.md`
  Source amendment: `../plan-amendment-001-architecture-guardrails-refactor-as-code.md`
  Status: In progress

  ## Goal

  ## Precedence and Authority Model

  ## Dependency Graph

  ## Content-Type Taxonomy

  ## Operation Router Taxonomy

  ## Rule Interface Conventions

  ## Architectural Metrics and Budgets

  ## Golden Scenario Tests

  ## Work-Item Artifact Locality

  ## Rule Versioning Deferral

  ## Phase 02 Inputs

  ## Open Risks
  ```

- [ ] **Step 5: Define the precedence and authority model**

  In `## Precedence and Authority Model`, define the conflict order for at least these sources: system/developer/tool constraints, operator instruction, repository `AGENTS.md`, repository-local `SKILL.md`, canonical references, approved/frozen work-item artifacts, templates, README/operator summaries, and examples.

  The model must explicitly cover the approved direction that frozen artifacts record work-specific decisions and exceptions, while current canonical policy controls execution unless a frozen artifact records an explicit approved exception.

- [ ] **Step 6: Define the dependency graph**

  In `## Dependency Graph`, define allowed reference directions and banned back-references.

  Include at least these edges:

  - `AGENTS.md` may bootstrap `SKILL.md` and repository-specific overrides.
  - `SKILL.md` may route to canonical references and templates.
  - Canonical references may cite other references only when the dependency is part of the rule interface.
  - Templates may cite schemas and rule IDs, but must not restate long reusable policy.
  - README may summarize and link to canonical owners, but must not own normative policy.
  - Work-item artifacts may record selected decisions, statuses, approvals, exceptions, and cited rule IDs.

- [ ] **Step 7: Define the content-type taxonomy**

  In `## Content-Type Taxonomy`, define these instruction content types: normative policy, artifact schema, example, advisory guidance, operator-facing summary, and historical snapshot.

  For each type, specify where it may live, whether it can be cited as authoritative policy, and how future phases should trim or rewrite it.

- [ ] **Step 8: Define the operation router taxonomy**

  In `## Operation Router Taxonomy`, create a table with these operations and their required module categories:

  - Classify work size.
  - Draft small/medium spec and plan.
  - Draft large anchor spec.
  - Draft phase plan.
  - Freeze planning package.
  - Execute approved phase.
  - Record implementation variance.
  - Use or review sub-agent strategy.
  - Review durable artifact quality.
  - Update templates.
  - Handle Superpowers or spec-kit compatibility.
  - Update README/operator guidance.

  Each row must include operation, required references or module categories, safety-critical rules, and maximum intended traversal depth.

- [ ] **Step 9: Define rule interface conventions and versioning deferral**

  In `## Rule Interface Conventions`, define the naming shape for stable rule IDs or module IDs that later phases should use. Keep the scheme simple enough to maintain manually.

  In `## Rule Versioning Deferral`, state that Phase 01 does not create a full rule versioning system. Record that later phases must avoid choices that prevent future versioning, deprecation, or supersession metadata.

- [ ] **Step 10: Define architectural metrics and budgets**

  In `## Architectural Metrics and Budgets`, define measurable checks for:

  - Maximum traversal depth for common operations.
  - Maximum eager-load reference count or word budget for common operations.
  - Duplicate policy prose threshold for templates.
  - Broken reference or broken rule-ID tolerance.
  - Required discoverability of freeze gate, variance, changelog, and model/sub-agent policy.

  Use concrete thresholds so later validation can pass or fail them.

- [ ] **Step 11: Define golden scenario tests**

  In `## Golden Scenario Tests`, define scenario names, setup, expected loaded references, and expected behavior for:

  - Very-small mechanical edit skip.
  - Small/medium work item planning.
  - Large anchor spec freeze.
  - Phase-plan freeze.
  - Post-freeze implementation authorization.
  - Variance amendment.
  - Sub-agent strategy authorization.
  - Superpowers compatibility.
  - Historical artifact handling.

- [ ] **Step 12: Define work-item artifact locality**

  In `## Work-Item Artifact Locality`, resolve the repository-specific tension that `docs/work-items/` is generally ignored while this harness branch is tracking approved planning artifacts.

  Specify when harness-development work-item artifacts should be force-added and committed, when they remain local-only, and how future agents should avoid accidentally dropping required planning artifacts.

- [ ] **Step 13: Fill Phase 02 inputs and open risks**

  In `## Phase 02 Inputs`, list the decisions Phase 02 must consume before reorganizing canonical references.

  In `## Open Risks`, list any architecture risks still unresolved after Phase 01. If any open risk would change scope or acceptance criteria, stop and propose an amendment instead of continuing.

  When the snapshot content is complete, change the snapshot header from `Status: In progress` to `Status: Final`.

- [ ] **Step 14: Create or update the variance log**

  Create `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md` if it does not exist.

  Initial content:

  ```md
  # Variance Log

  Work ID: `2026-06-05-refactor-as-code`

  ## Entries

  - None recorded.
  ```

  If Phase 01 departs from the approved spec, approved amendment, or approved phase plan, replace `None recorded` with a dated entry explaining the variance, class, rationale, approval requirement, and resolution.

- [ ] **Step 15: Update changelog for Phase 01 execution**

  Before the Phase 01 execution commit, add a newest-first `CHANGELOG.md` entry titled `2026-06-05-refactor-as-code: complete Phase 01 policy architecture`.

  The entry must mention the architecture snapshot, rule-interface conventions, validation budgets, golden scenario tests, and the explicit rule-versioning deferral.

- [ ] **Step 16: Run validation commands**

  Run every command in `## Tests and validation` and record the result in the Phase 01 completion handoff.

- [ ] **Step 17: Review and commit Phase 01 outputs**

  Review the diff to confirm Phase 01 changed only the architecture snapshot, variance log, and `CHANGELOG.md` unless an approved amendment permits more.

  Commit the Phase 01 outputs with message:

  ```text
  Complete Phase 01 policy architecture
  ```

## Tests and validation

| Command | Expected result |
|---|---|
| `git status --short --branch` | Shows branch `refactor-as-code`; before the Phase 01 commit, only Phase 01 outputs are modified or staged. |
| `Test-Path docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md` | Outputs `True`. |
| `Test-Path docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md` | Outputs `True`. |
| `rg -n "Status:[ ]Draft|T[D]B|T[O]DO|R[e]place|blank[ ]unless|unresolved[ ]decision" docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md` | No output. Exit code may be `1` because `rg` found no matches. |
| `rg -n "## (Precedence and Authority Model|Dependency Graph|Content-Type Taxonomy|Operation Router Taxonomy|Rule Interface Conventions|Architectural Metrics and Budgets|Golden Scenario Tests|Work-Item Artifact Locality|Rule Versioning Deferral|Phase 02 Inputs)" docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md` | Outputs one match for each listed required section. |
| `rg -n "enterprise-default|latest strongest|Rule Versioning Deferral|Work-Item Artifact Locality" docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md docs/work-items/2026-06-05-refactor-as-code/plan-phase-01-policy-architecture-refactor-as-code.md` | Outputs matches proving Phase 01 recorded the selected policy, versioning deferral, and artifact-locality decision. |
| `git diff --name-only` | Before commit, includes only `CHANGELOG.md`, `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`, and `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`, unless an approved amendment permits more. |

## Documentation tasks

- Create `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`.
- Create or update `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`.
- Update `CHANGELOG.md` before the Phase 01 execution commit.
- Do not create `deltas/operator-manual.delta.md`, `deltas/architecture-summary.delta.md`, or `snapshots/test-cases.snapshot.md` in Phase 01 unless the architecture snapshot identifies an immediate need and the operator approves that expansion.

## Variance reminder

Before approval, operator feedback edits this draft directly and does not require an amendment. After the approval commit or explicit handoff snapshot, approved phase plans are immutable snapshots. Record nontrivial variance in `implementation-notes/variance-log.md`. Create a plan amendment named `plan-amendment-NNN-short-title-refactor-as-code.md` and request operator approval before proceeding when post-freeze variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

When this phase plan is ready for operator review, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage the draft without committing, request approval or feedback, revise directly on feedback, and commit only after explicit approval.

After the approval commit, use the canonical post-freeze prompt to confirm model, reasoning-effort, and sub-agent policy choices and ask whether Phase 01 execution should begin now.

## Handoff output

At Phase 01 completion, the implementing agent must report:

- Assigned scope.
- Files inspected.
- Files changed.
- Commands and validation results.
- Final architecture decisions by section.
- Any variance entries or a statement that no variance occurred.
- Sub-agent use, including count, role, context strategy, observed inheritance behavior, and model/model class/profile when known.
- Residual risks and recommended next phase action.

## Completion criteria

- Phase objective is met.
- `snapshots/architecture.snapshot.md` defines precedence, dependency direction, content types, operation routing, rule interface conventions, architectural metrics, golden scenario tests, work-item artifact locality, rule-versioning deferral, Phase 02 inputs, and open risks.
- Validation commands have been run and recorded.
- Documentation tasks are complete or explicitly deferred with reason.
- `CHANGELOG.md` has a newest-first entry for Phase 01 before the execution commit.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.
