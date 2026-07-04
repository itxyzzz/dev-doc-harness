# Small/Medium Plan Template Update Spec

Work ID: `2026-07-01_small-medium-plan-template-structure`
Short ID: `small-medium-plan-template-structure`
Status: Approved
Harness release: `0.4+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Improve the small/medium work-item plan template so it turns the newly improved spec template into an executable implementation handoff without duplicating the spec or making ordinary small/medium work feel large/phased.

## Source and Intent

Source input:

- Follow-up operator request after commit `63597af docs: small-medium-template-structure -- improve spec-template scaffolding`.
- Current plan template at `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`.
- Updated spec template at `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`.
- Prior research report at `docs/work-items/2026-07-01_small-medium-template-structure/handoff/research-verification.md`.
- Operator feedback that one completion check should verify sufficient detail and guard against orchestration saturation.

Desired operator/user outcome:

- Future small/medium plans should be easier for implementation agents to execute and easier for human reviewers to audit against the approved spec.

Success summary:

- The plan template clearly separates spec-derived decisions from implementation sequencing, asks for enough detail for each assigned execution part to be safe, and includes a check that the small/medium work remains deliberately orchestrated within one coordinating thread with a bounded sub-agent strategy when delegation is useful.
- The update remains focused on the plan template and does not change lifecycle policy, the spec template, or large/phased templates. Clarify `subagent-model-policy.md` only if implementation review shows the current wording is ambiguous for small/medium plans.

## Scope Boundary

### In scope

- Update `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`.
- Add prompts that make the plan consume the updated spec structure: requirements, acceptance criteria, risks, interfaces, documentation matrix decisions, and readiness checks.
- Improve task guidance so tasks are specific, measurable, achievable, relevant, and bounded to lifecycle checkpoints.
- Add explicit plan readiness and completion checks for sufficient implementation detail, orchestration-thread fit, and bounded sub-agent delegation.
- Replace the current wide sub-agent table with a more readable structure that references canonical model-policy requirements instead of duplicating them.
- Clarify `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` only if needed to make its small/medium plan applicability unambiguous without changing policy semantics.
- Preserve required metadata, policy references, planned commits, variance handling, freeze-gate, completion criteria, and approval sections.
- Update `CHANGELOG.md` before the implementation commit.

### Non-scope

- No changes to the small/medium spec template.
- No changes to large/phased templates.
- No changes to canonical lifecycle, freeze-gate, naming, quality, or model-policy references unless validation or implementation review shows a directly caused ambiguity in how the plan template should cite them.
- No wholesale adoption of Superpowers plan format, Spec Kit tasks, Gherkin, or other external task systems.
- No update to `.agents/skills/dev-doc-harness/VERSION`; the marker is known stale on master, so this work item uses `0.4+` without changing release identity.

### Assumptions

- The updated spec template from commit `63597af` is the baseline the plan template should align with.
- Small/medium plans should be executable by one orchestration thread, with optional bounded sub-agents for review, parallel exploration, or specialized tasks when the model policy justifies them.
- Each part assigned to one thread or sub-agent should be executable from the plan and its cited artifacts without hidden context.
- If a plan needs many sub-agents, multiple waves, or additional planning hierarchy to stay understandable, it is likely large/phased rather than small/medium.
- Current UI readability still favors bullets and short card-style blocks over wide tables with long cells.
- Validation can be covered by the harness validator plus targeted text checks for headings and forbidden wording.

### Open questions

- None identified after repository-context review.

## Repository Context

### Current state

- The current plan template includes metadata, implementation summary, files and interfaces, model/sub-agent strategy, tasks, planned commits, validation commands, variance handling, freeze-gate status, completion criteria, and approval.
- The plan template is useful but basic. It does not explicitly tell the author how to map the new spec requirements and acceptance criteria into tasks and validation.
- The current sub-agent strategy table is wide and contains long-cell content, which is harder to read in the current UI.
- The current completion criteria cover acceptance criteria, validation, docs, changelog, commits, variance, and de-facto sub-agent reporting, but they do not explicitly ask whether the plan has enough implementation detail or whether it still fits one orchestration thread with bounded delegation.

### Evidence read

- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/references/naming-conventions.md`
- `docs/work-items/2026-07-01_small-medium-template-structure/handoff/research-verification.md`

### Constraints and compatibility

- The plan template must preserve harness lifecycle and freeze-gate behavior instead of re-describing canonical policy at length.
- Required model/sub-agent strategy fields must remain available when sub-agents are proposed, by referencing `module:models` and `rule:models.strategy-required` instead of duplicating the policy.
- The plan must stay small/medium friendly: enough structure for safe execution, not a large/phased phase-plan clone.
- Completion criteria should include an orchestration saturation guard: if execution cannot be coordinated by one orchestration thread with a bounded sub-agent strategy and safely executable delegated parts, the work should be split, re-scoped, or escalated to large/phased handling before implementation.

## Requirements

REQ-001: The plan template consumes the approved spec instead of restating it.

Rationale:

- The updated spec now owns source intent, scope, requirements, acceptance criteria, repository context, risks, and interface decisions. The plan should turn those into execution steps and checks.

Acceptance links:

- Covered by AC-001 and AC-002.

Notes:

- The plan may summarize the implementation approach, but it should not become a second spec.

REQ-002: The plan template includes traceability from spec requirements and acceptance criteria to tasks and validation.

Rationale:

- Implementing agents and reviewers need to see that every approved outcome has an execution path and verification method.

Acceptance links:

- Covered by AC-002 and AC-005.

Notes:

- Traceability should be readable with bullets or compact blocks, not a wide multi-column table with long cells.

REQ-003: The plan template guides SMART task quality without forcing vertical slicing at the task level.

Rationale:

- Tasks should be specific and verifiable, but plan authors should be free to order shared setup, tests, refactors, and implementation in the sequence that best fits the codebase.

Acceptance links:

- Covered by AC-003.

Notes:

- Vertical slicing remains preferred at the spec/outcome level when useful; task sequencing may group setup or shared work first.

REQ-004: The plan template includes exact validation commands with expected signals tied to acceptance criteria.

Rationale:

- A plan is not executable enough if an implementation agent must invent the validation strategy after code changes.

Acceptance links:

- Covered by AC-004 and AC-005.

Notes:

- Validation may include commands, manual checks, review findings, or operator acceptance when commands are not enough.

REQ-005: The model and sub-agent strategy section remains policy-complete while becoming easier to read.

Rationale:

- The current wide table preserves required fields but is awkward in the UI. The template should keep the required model-policy prompts available through a clearer card-style structure and direct references to the canonical policy.

Acceptance links:

- Covered by AC-006.

Notes:

- If no sub-agents are proposed, the template should make the `None` rationale concise.
- If sub-agents are useful for review, parallel exploration, or specialized tasks, the template should help authors record a bounded strategy without making small/medium plans large/phased.

REQ-006: Completion criteria include sufficient execution detail and orchestration saturation checks.

Rationale:

- A plan can appear complete while still being too vague for a fresh implementation agent or delegated sub-agent, or too broad for one orchestration thread to coordinate safely. The template should catch both failure modes before freeze.

Acceptance links:

- Covered by AC-007.

Notes:

- The check should direct agents to split, re-scope, or escalate to large/phased handling when the plan cannot fit one orchestration thread with bounded delegation.

REQ-007: The plan template preserves existing harness commit, changelog, variance, freeze-gate, and approval surfaces.

Rationale:

- This is a template-shape improvement, not a lifecycle-policy change.

Acceptance links:

- Covered by AC-008 and AC-009.

Notes:

- Keep policy prose compact and route reusable rules to canonical references.

## Acceptance Criteria

AC-001: The revised plan template includes an input-artifacts or spec-traceability section that tells authors to read the approved spec, related snapshots/deltas, and relevant repository files before implementation planning is finalized.

Verifies:

- REQ-001

Method:

- Review `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` after implementation.

AC-002: The revised plan template prompts authors to map spec requirements and acceptance criteria to implementation tasks and validation methods.

Verifies:

- REQ-001 and REQ-002

Method:

- Review heading and prompt text in the revised template.

AC-003: The revised task guidance uses SMART-style quality prompts and cautions that task order should follow implementation dependency rather than blindly forcing vertical slices.

Verifies:

- REQ-003

Method:

- Review task section prompt text.

AC-004: The revised validation section asks for exact commands, manual checks, review findings, or operator acceptance paths with expected signals.

Verifies:

- REQ-004

Method:

- Review validation section prompt text and run the planned heading scan.

AC-005: The revised completion/readiness checks require every acceptance criterion to have a task and validation path before implementation.

Verifies:

- REQ-002 and REQ-004

Method:

- Review completion/readiness checklist.

AC-006: The revised model/sub-agent section preserves required strategy fields without relying on a wide table with long content.

Verifies:

- REQ-005

Method:

- Review the revised model/sub-agent section against `rule:models.strategy-required`.

AC-007: The revised completion/readiness checks include both sufficient detail for a fresh implementation agent or delegated sub-agent and a guard that the plan still fits one orchestration thread with bounded delegation.

Verifies:

- REQ-006

Method:

- Review completion/readiness checklist and completion criteria.

AC-008: The revised plan template preserves required metadata, policy references, planned commits, variance handling, planning freeze gate, completion criteria, and approval sections.

Verifies:

- REQ-007

Method:

- Review the template diff.

AC-009: The implementation remains limited to the small/medium plan template, `CHANGELOG.md`, and any directly required validator or model-policy clarification.

Verifies:

- REQ-007

Method:

- Run `git status --short` and inspect the implementation diff.

## Interfaces, Data, and Control Flow

### Interfaces affected

- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` is the primary implementation target.
- `CHANGELOG.md` must receive a newest-first implementation entry before the implementation commit.

### Data, config, and persistence

- No runtime data, configuration, persistence, or release identity changes are expected.

### State and control flow

- The authoring flow changes only by template guidance: future plans should include stronger spec traceability, task detail, validation mapping, and readiness checks before freeze.

### Safety, security, privacy, migration, and rollback

- None identified after repository-context review.

## Risks and Rejected Alternatives

RISK-001: The plan template could become too heavy for small/medium work.

Decision or mitigation:

- Keep prompts concise, use compact blocks, and avoid requiring full phase-plan detail unless the work itself demands it.

RISK-002: The plan template could duplicate the spec.

Decision or mitigation:

- Make the plan consume the spec through traceability and task mapping rather than restating source intent, requirements, and risks in full.

RISK-003: An orchestration saturation guard could be ignored if it is buried in generic completion criteria.

Decision or mitigation:

- Add it as an explicit plan readiness and completion criterion, using direct wording about one orchestration thread, bounded sub-agent strategy, and safely executable delegated parts.

RISK-004: Replacing the sub-agent table could accidentally omit required model-policy fields.

Decision or mitigation:

- Reference `module:models` and preserve prompts for every required strategy field in card-style blocks. If the canonical policy wording is unclear for small/medium plans, clarify that reference instead of copying policy into the template.

RISK-005: Applying vertical slicing too aggressively at task level could make implementation worse.

Decision or mitigation:

- The task section should say to order work by dependency and reviewability, including shared setup and tests when appropriate.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spike: small-medium-plan-template-structure -- approve plan-template update plan` | `2026-07-01_small-medium-plan-template-structure -- approve plan-template update plan` | Approval commit for this spec and plan. |
| Implementation | `docs: small-medium-plan-template-structure -- improve plan-template scaffolding` | `2026-07-01_small-medium-plan-template-structure -- improve plan-template scaffolding` | Implementation commit for the small/medium plan template update and changelog entry. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required before approval and implementation commits; title snippets synchronized with planned commit subjects. |
| Test cases | Snapshot | No | Not applicable | Not applicable | Validation commands in the plan cover this template-only change. |
| Testing guide delta | Living delta | No | Not applicable | Not applicable | No testing-guide process change yet. |
| Operator manual delta | Living delta | No | Not applicable | Not applicable | This changes authoring scaffolding, not operator-facing workflow semantics. |
| API reference delta | Living delta | No | Not applicable | Not applicable | No public API changes. |
| Architecture snapshot | Snapshot | No | Not applicable | Not applicable | No architecture decision change. |
| Architecture summary delta | Living delta | No | Not applicable | Not applicable | No long-lived architecture-doc change. |

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
- [x] No unresolved placeholders remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
