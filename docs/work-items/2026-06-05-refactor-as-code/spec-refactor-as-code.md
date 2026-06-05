# Refactor Harness Instructions As Code Spec

Work ID: `2026-06-05-refactor-as-code`
Short ID: `refactor-as-code`
Status: Approved

## Goal

Refactor the repository documentation harness so its textual instructions behave more like maintainable code: small modules with clear ownership, minimal duplicated policy prose, stable interfaces, explicit retrieval paths, and testable drift controls.

This work needs phase planning because it changes the architecture of the harness itself. The current harness is usable, but focused policy changes can touch many files because policy text is repeated across references, templates, generated work-item artifacts, and summary documentation. A single implementation pass would risk breaking the approval/freeze lifecycle while attempting to reduce that very coupling.

## Planning handoff quality bar

This spec is the central handoff for later phase plans. Phase planners must preserve the architectural intent: turn reusable policy into single-owner modules and keep work-item artifacts declarative unless they must record a work-specific decision.

Phase plans must derive from this spec. If later planning discovers missing context before this spec is frozen, update the draft spec directly. If missing context is discovered after freeze, create an amendment.

Follow the repository-root reference `.agents/skills/dev-doc-harness/references/durable-planning-quality.md` before asking for approval to freeze this spec.

## Scope

- Reorganize harness policy ownership across `.agents/skills/dev-doc-harness/SKILL.md`, `references/`, `assets/templates/`, root `AGENTS.md`, `README.md`, and any supporting validation or adapter documentation needed to keep behavior discoverable.
- Reduce policy prose duplicated across templates and generated work-item artifacts.
- Define a stable rule or module interface that lets templates and docs refer to shared policy without restating it.
- Improve retrieval efficiency by making the entrypoint route agents to the minimum necessary references for common operations.
- Improve traversal efficiency by making rule ownership and reference paths explicit, shallow, and auditable.
- Preserve the existing planning approval/freeze lifecycle, variance policy, changelog discipline, and active `economy-default` sub-agent model policy unless explicitly amended.
- Add lightweight validation checks or review procedures that detect duplicated policy blocks, unresolved placeholders, broken references, and drift between templates and canonical modules.

## Non-scope

- Replacing the harness with Superpowers, spec-kit, or another external methodology.
- Removing durable planning artifacts, planning freeze gates, changelog requirements, variance logs, or immutable snapshot behavior.
- Rewriting frozen historical work-item artifacts merely to update copied policy prose.
- Building a complex parser, compiler, or full documentation generation system unless later phase discovery proves a small script is insufficient.
- Changing the active repository sub-agent policy from `economy-default`.
- Changing Codex platform behavior, tool availability, or global instructions outside this repository.

## Current state

The harness has a modular file layout, but policy responsibilities leak across files.

- `AGENTS.md` bootstraps the repository-local harness and overrides the global model policy to `economy-default`.
- `.agents/skills/dev-doc-harness/SKILL.md` is the public skill entrypoint and requires four core references before creating or reviewing artifacts.
- `references/artifact-contract.md` owns layout, lifecycle, documentation matrix, variance handling, changelog rules, and compatibility pointers.
- `references/planning-freeze-gates.md` owns the approval-first draft and freeze workflow.
- `references/subagent-model-policy.md` owns model and sub-agent behavior.
- `assets/templates/` contains work-item templates, but several templates embed reusable policy prose for model/sub-agent behavior, variance handling, and freeze-gate reminders.
- Existing `docs/work-items/*` artifacts contain copied policy text generated from prior templates. These artifacts are historical planning snapshots and may be frozen or review-significant.

The observed problem is that focused harness policy changes can require edits across many files because shared rules are copied into consumers instead of referenced through stable interfaces.

## Proposed behavior

The harness should behave like a small policy library with explicit public interfaces.

- Each reusable rule family has one canonical owner and a stable rule or module identifier.
- The skill entrypoint acts as a router: it classifies the operation and lists the minimum references needed for that operation.
- Templates provide artifact shape and work-specific prompts, not long reusable policy explanations.
- Work-item artifacts record work-specific decisions, selected policy IDs, status, approvals, and exceptions. They do not become stale copies of current harness policy.
- README and root instructions summarize behavior and point to canonical owners instead of duplicating detailed policy.
- Validation can detect broken references, duplicated large policy blocks, missing required sections, and drift-prone template prose.

## Interfaces and data

Affected repository-facing instruction interfaces include:

- Root bootstrap instructions: `AGENTS.md`.
- Skill public entrypoint: `.agents/skills/dev-doc-harness/SKILL.md`.
- Canonical references under `.agents/skills/dev-doc-harness/references/`.
- Reusable templates under `.agents/skills/dev-doc-harness/assets/templates/`.
- Project-facing summary documentation: `README.md`.
- Work-item artifact schema under dated work item folders in `docs/work-items/`.
- Optional validation scripts or checklists, if introduced by phase plans.

The refactor may introduce new reference files, for example a compact rule manifest, lifecycle policy module, artifact schema module, integrations module, changelog policy module, or validation guide. Exact filenames should be decided during phase planning based on minimizing churn and keeping traversal shallow.

Historical work-item artifacts are not treated as mutable runtime policy. A phase plan may add guidance explaining that old artifacts preserve planning history and that current harness policy wins unless a frozen artifact records an explicit approved exception.

## State flow and control flow

The desired harness control flow is:

1. Agent reads root repository instructions.
2. Agent invokes `.agents/skills/dev-doc-harness/SKILL.md` for non-mechanical development work.
3. Skill entrypoint classifies the operation and routes to the smallest relevant policy modules.
4. Agent creates or reviews artifacts using template schemas and canonical policy IDs.
5. Draft artifacts remain editable until review, approval, or explicit handoff.
6. Planning freeze gates still pause before implementation or later planning stages.
7. Implementation uses frozen plans plus current canonical harness policy.
8. Variance is recorded in the variance log or amendments according to canonical lifecycle policy.
9. Validation checks confirm that references, templates, and docs remain consistent.

The refactor should reduce reference-chain depth for common operations. A common operation such as "create a small/medium plan" should not require reading every reference file before the agent can start drafting.

## Safety, security, privacy, compliance, migration, and rollback

No privacy, security, or compliance-sensitive runtime behavior is expected to change. The safety risk is process drift: if the refactor accidentally weakens freeze gates, variance handling, or sub-agent authorization, future agents may implement work without the intended approvals.

Migration should be incremental. Each phase should preserve current behavior unless the phase explicitly changes behavior and documents the acceptance criteria. Rollback should be possible by reverting the phase commit because the harness has no generated runtime state.

Frozen historical work items should not be rewritten to hide drift. If a phase must clarify how old artifacts relate to current policy, it should do so in current harness guidance or a new delta, not by mass-editing old frozen snapshots.

## Validation strategy

Validation should combine static checks and manual review.

- Inspect the diff for duplicated reusable policy prose and accidental broad rewrites.
- Verify references named by `SKILL.md`, templates, and README exist.
- Check that templates contain no unresolved placeholders outside intentional template placeholders.
- Check that canonical policy modules have one owner per rule family.
- Check that planning freeze gate, variance, changelog, and `economy-default` model policy remain discoverable from root instructions.
- Run any repository validation script added by the phase plan.

Each phase plan must list exact validation commands and expected outputs. If validation scripts do not yet exist, early phases should use `rg`-based checks before adding more formal tooling.

## Triage, debugging, and operations

Because this repository is primarily textual, debugging focuses on instruction traversal and policy drift.

Useful diagnostics include:

- `rg` searches for repeated policy phrases such as `Fresh confirmation`, `Planning artifact freeze gate`, `Context strategy must`, and `Before approval`.
- File/word counts for references and templates to measure conciseness trends.
- Link/path checks for references from `SKILL.md`, templates, README, and `AGENTS.md`.
- Review of a sample task path, such as creating a small/medium work item, freezing an anchor spec, and recording implementation variance.

Phase completion reports should include which policy owners changed, which consumers were updated, which duplicated prose remains intentionally, and which retrieval paths were exercised.

## Assumptions

- The repository-local harness remains the canonical artifact and lifecycle contract.
- The active sub-agent model policy remains `economy-default`.
- Superpowers, when active, continues to provide general development methodology, while this harness owns artifact location and lifecycle.
- The desired end state is a leaner instruction architecture, not fewer safeguards.
- Templates can rely on policy references and rule IDs without becoming less useful to a fresh agent.
- Historical work-item artifacts should be preserved unless an operator explicitly requests archival cleanup.

## Risks

- Over-modularization could make agents chase too many tiny files.
- Excessively terse templates could reduce fresh-thread executability.
- Rule IDs could become another maintenance burden if not simple and stable.
- Updating the entrypoint router could accidentally omit a required reference for a safety-critical operation.
- Changing template wording could alter generated artifact quality before validation catches regressions.
- README/root instruction summaries could drift from canonical references if ownership is not explicit.

## Known unknowns

- Whether validation should be a simple checklist, a small script, or both.
- The exact rule ID naming scheme and whether IDs should be grouped by module, lifecycle stage, or artifact type.
- Whether `artifact-contract.md` should be split immediately or first receive an internal ownership map.
- Whether old work-item artifacts need an explicit compatibility note outside this spec.
- Whether generated templates should include full tables or compact links to reusable table schemas.

## Rejected alternatives

- Big-bang rewrite of all harness files in one phase: rejected because it would make behavior regressions hard to isolate.
- Leave templates unchanged and only edit canonical references: rejected because it does not solve the current file fan-out problem.
- Make `README.md` the canonical source for harness behavior: rejected because README should summarize, not own operational policy.
- Rewrite frozen work-item artifacts to match the new architecture: rejected because it violates the snapshot discipline and creates historical churn.
- Remove phase/freeze/changelog/variance safeguards to make the harness shorter: rejected because the goal is maintainability, not weaker process control.

## Acceptance criteria

- A future focused policy change can usually be made in one canonical reference plus narrow consumer pointers, without updating every template that mentions the rule family.
- Templates no longer contain long reusable policy blocks for sub-agent authorization, variance handling, or freeze-gate procedure.
- The skill entrypoint includes a retrieval router or equivalent load-order table that avoids eager loading all core references for every operation.
- Each reusable rule family has an explicit owner and a stable reference mechanism.
- Current planning freeze, variance, changelog, immutable snapshot, Superpowers compatibility, and `economy-default` policy behavior remain discoverable and enforceable.
- Historical work-item artifacts are not silently rewritten to hide policy drift.
- Validation can identify broken policy references and obvious duplicated policy prose.
- README and root instructions summarize the architecture without becoming competing canonical policy sources.

## Phase decomposition

| Phase | Objective | Output |
|---|---|---|
| 01 | Define the target policy architecture and rule-interface conventions without moving behavior yet. | `plan-phase-01-policy-architecture-refactor-as-code.md` |
| 02 | Split or reorganize canonical references so each reusable rule family has one owner and shallow traversal. | `plan-phase-02-canonical-modules-refactor-as-code.md` |
| 03 | Slim templates so they capture artifact shape and work-specific decisions while referencing canonical policy IDs. | `plan-phase-03-template-slimming-refactor-as-code.md` |
| 04 | Update entrypoint, root instructions, README, and compatibility guidance to use the new router and ownership map. | `plan-phase-04-entrypoint-docs-refactor-as-code.md` |
| 05 | Add validation checks and run sample traversal tests for common harness operations. | `plan-phase-05-validation-hardening-refactor-as-code.md` |

Phase 01 should produce the concrete module/rule map and decide whether later phases split files, add a manifest, or use explicit section IDs in existing files. Phase 02 should make canonical ownership real before Phase 03 edits templates, so templates have stable targets to reference. Phase 04 should update public-facing summaries after the internal policy API exists. Phase 05 should harden against regression after the new structure is in place.

## Planning artifact freeze gates

When this spec, later phase-plan batches, or high-impact amendments are ready for operator review, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage the draft without committing, request approval or feedback, revise directly on feedback, and commit only after explicit approval or explicit handoff.

## Model and Sub-agent Strategy

Current orchestration: Codex in this desktop thread; exact model/profile and reasoning effort are not exposed in repository artifacts.
Fit assessment: This is a documentation architecture refactor with medium-to-high process risk, moderate ambiguity, and high leverage for future context efficiency. Cost and usage limits matter under the repository `economy-default` policy, but final architecture and review should not rely solely on lower-capability review.
Recommended change: None for the orchestration thread unless later phase planning exposes subtle conflicts in lifecycle policy.

| Phase | Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | Policy architecture review | curated artifacts | This spec, current `SKILL.md`, references, templates, README, and root `AGENTS.md` | Review notes or phase-plan findings | `economy-default` | standard or latest strongest if ambiguity remains | medium/high | Rule ownership mistakes have high downstream cost | No | High: bad boundaries can increase traversal or weaken safeguards |
| 03 | Template duplication review | curated prompt | Canonical module map plus changed templates | Review findings on duplicated policy prose and fresh-thread usability | `economy-default` | smaller/faster or standard | medium | Bounded text review with clear inputs | Yes | Medium: missed duplication preserves current pain |
| 05 | Final harness behavior review | curated artifacts | Completed diffs, validation output, entrypoint router, variance log | Final review findings | `economy-default` | latest strongest | high | Final process review has high blast radius | No | High: missed regression can affect future repository work |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries grouped by change type |
| Test cases | Snapshot | Deferred | Phase 05 | `snapshots/test-cases.snapshot.md` | Defer until the validation phase defines concrete traversal/test cases |
| Testing guide delta | Living delta | Deferred | Phase 05 | `deltas/testing-guide.delta.md` | Required if validation commands or scripts are added |
| Operator manual delta | Living delta | Yes | Phase 04 or 05 | `deltas/operator-manual.delta.md` | Harness usage and traversal behavior changes affect operators and agents |
| API reference delta | Living delta | No | Not applicable | `deltas/api-reference.delta.md` | No public API is expected |
| Architecture snapshot | Snapshot | Yes | Phase 01 | `snapshots/architecture.snapshot.md` | Capture the module/rule ownership map before broad edits |
| Architecture summary delta | Living delta | Yes | Phase 04 or 05 | `deltas/architecture-summary.delta.md` | Update long-lived architecture summary if README or harness docs change |

## Approval

- Status: Approved
- Superseded by: None
