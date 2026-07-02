# Orchestration Sizing And Large Template Alignment Spec

Work ID: `2026-07-02_orchestration-sizing-large-templates`
Short ID: `orchestration-sizing-large-templates`
Status: Approved
Harness release: `0.4+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Align the harness work-sizing rule, README, small/medium templates, and large/phased templates around a clear distinction: small/medium work fits one orchestration thread with bounded delegation, while large/phased work needs an anchor spec plus phase plans because one orchestration thread or one flat plan is not enough to coordinate execution safely.

## Source and Intent

Source input:

- Operator request to reflect the orchestration-thread sizing distinction in the harness before improving the large spec and phase-plan templates.
- Prior investigation in this thread concluding that "one orchestration thread with bounded delegation" is the most objective primary criterion, while current risk and breadth signals should remain escalation indicators.
- Existing harness sizing rule in `.agents/skills/dev-doc-harness/references/artifact-contract.md`.
- Existing model and sub-agent orchestration guidance in `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`.
- Existing README operator overview and reusable templates in `.agents/skills/dev-doc-harness/assets/templates/`.
- External examples requested by the operator:
  - `https://github.com/itxyzzz/gen-ai-se-hw/blob/main/homework-3/TASKS.md`
  - `https://github.com/itxyzzz/gen-ai-se-hw/blob/main/homework-3/specification.md`

Desired operator/user outcome:

- Future agents and human reviewers can classify small/medium versus large/phased work more consistently, understand why a large/phased anchor spec exists, and use large/phased templates that inherit the small/medium spec and plan improvements without copying policy prose everywhere.

Success summary:

- The lifecycle reference owns the core sizing definition and cites the model policy for sub-agent and orchestration details.
- README explains the distinction in operator-facing language, including a brief Scrum Guide analogy.
- Small/medium templates consistently use the orchestration-thread boundary.
- Large/phased templates use the updated spec and plan information architecture, but elaborate only where the anchor/phase handoff pattern is different.

## Scope Boundary

### In scope

- Update `.agents/skills/dev-doc-harness/references/artifact-contract.md` work-sizing text to make the one-orchestration-thread criterion primary.
- Add only narrow supporting wording to `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` if needed so lifecycle can defer sub-agent and orchestration mechanics there.
- Update `README.md` to explain small/medium versus large/phased in operator-facing terms, including a compact Scrum Guide analogy.
- Update `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md` to replace remaining one-implementation-thread language with one-orchestration-thread and bounded-delegation language.
- Review `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` and make only alignment edits needed after the lifecycle wording changes.
- Update `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md` so it inherits the improved spec structure: source and intent, scope boundary, repository context, requirements, acceptance criteria, interfaces/data/control flow, risks/rejected alternatives, planned commits, documentation matrix, readiness, and approval.
- Update `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md` so it inherits the improved plan structure: input artifacts, spec traceability, implementation approach, change surfaces, readable model/sub-agent strategy, SMART task guidance, dependency labels, validation plan with expected signals, readiness, completion, and handoff output.
- Use the requested homework `TASKS.md` and `specification.md` examples as inspiration for layered objectives and phase-level decomposition, without importing their FinTech domain content or homework-specific deliverable rules.
- Update `CHANGELOG.md` before the implementation commit.
- Update `test_harness_policy.py` only if implementation changes require validator evidence updates.

### Non-scope

- No change to the approved planning/freeze lifecycle sequence.
- No change to root `AGENTS.md` active repository policy.
- No change to `.agents/skills/dev-doc-harness/VERSION`; the release marker remains known stale relative to `0.4+`.
- No wholesale adoption of Spec Kit, Scrum, or the homework format as canonical harness policy.
- No new large/phased implementation package for this work item; this work itself is expected to stay small/medium because one orchestration thread can coordinate it.
- No rewrite of frozen historical work-item artifacts to match the new wording.

### Assumptions

- The operator's earlier `enterprise-default` selection applies to this template-improvement sequence unless changed before implementation.
- The core sizing distinction belongs in `module:lifecycle`, while sub-agent concurrency, context strategy, model selection, and final integration ownership remain in `module:models`.
- The large/phased templates should reuse the small/medium information architecture by section shape and traceability concepts, not by duplicating all explanatory prose.
- README should use the Scrum analogy as an explanatory aid only: the harness is not adopting Scrum events, roles, or sprint commitments.
- The requested homework examples are useful because they show layered intent and mid-level objectives, not because the harness should copy their finance-specific compliance content.

### Open questions

- None identified after repository-context and source-example review.

## Repository Context

### Current state

- `artifact-contract.md` currently defines small/medium work by examples and defines large/phased work by examples plus "work that needs phase plans to fit in one implementation thread."
- The small/medium plan template already uses one orchestration thread with bounded delegation, but the small/medium spec template still says one implementation thread in two places.
- The large/phased spec template is still structurally older than the updated small/medium spec template. It has useful anchor-spec wording, but lacks explicit source/intent, requirements, acceptance-criteria traceability, readiness checks, and the newer readability guidance.
- The large/phased phase-plan template is still structurally older than the updated small/medium plan template. It has useful fresh-thread handoff wording, but lacks spec traceability, dependency labels, exact validation expected signals, and plan readiness checks.
- README explains small/medium and large work in general terms, but does not currently expose the orchestration-thread criterion or Scrum analogy.

### Evidence read

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/naming-conventions.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
- `README.md`
- `docs/work-items/2026-07-01_small-medium-template-structure/handoff/research-verification.md`
- `docs/work-items/2026-07-01_small-medium-plan-template-structure/spec_small-medium-plan-template-structure.md`
- `https://github.com/itxyzzz/gen-ai-se-hw/blob/main/homework-3/TASKS.md`
- `https://github.com/itxyzzz/gen-ai-se-hw/blob/main/homework-3/specification.md`
- `https://raw.githubusercontent.com/github/spec-kit/main/spec-driven.md`
- `https://scrumguides.org/scrum-guide.html`

### Constraints and compatibility

- `artifact-contract.md` is the lifecycle owner for `rule:lifecycle.work-sizing`; templates and README must not become normative owners for the sizing rule.
- `subagent-model-policy.md` is the owner for context strategy, model selection, sub-agent concurrency caps, approved-strategy authorization, and final integration ownership.
- Template policy-reference lines must continue to satisfy `test_harness_policy.py` route checks.
- Current UI readability favors bullets and short card-style blocks over wide tables with long text. Existing canonical documentation matrix tables may remain, but new long-content sections should prefer short blocks.
- The harness validator watches current surfaces for dangling rule IDs, route drift, duplicate broad policy blocks, placeholders, required files, release package boundaries, and golden traversal evidence.

## Requirements

REQ-001: Work sizing uses one orchestration thread as the primary small/medium boundary.

Rationale:

- This criterion is more objective than "broad" or "complex" alone and better matches how Codex work actually saturates: the coordinating thread must hold scope, decisions, validation, variance, integration, and handoff.

Acceptance links:

- Covered by AC-001, AC-002, and AC-003.

Notes:

- Keep the existing risk and breadth examples as escalation indicators, not as the only definition.

REQ-002: Lifecycle sizing defers sub-agent mechanics to model policy.

Rationale:

- The lifecycle module should say when a work item stops fitting the small/medium planning shape. It should not copy concurrency caps, context strategy labels, or model-selection details owned by `module:models`.

Acceptance links:

- Covered by AC-002 and AC-008.

REQ-003: README explains the sizing distinction for operators.

Rationale:

- Operators need enough explanation to understand why an agent asks for an anchor spec first instead of drafting an executable plan immediately.

Acceptance links:

- Covered by AC-003.

Notes:

- Include a brief analogy to the Scrum Guide: Product Backlog items become ready when they can be completed in a Sprint; harness work becomes small/medium-ready when it can be coordinated by one orchestration thread. Avoid implying that the harness adopts Scrum events or roles.

REQ-004: Small/medium templates consistently use one orchestration thread with bounded delegation.

Rationale:

- The plan template was already updated after operator feedback, but the spec template still says one implementation thread. That mismatch can cause agents to reject useful bounded sub-agent strategies.

Acceptance links:

- Covered by AC-004.

REQ-005: The large/phased spec template inherits the updated spec structure while preserving anchor-specific purpose.

Rationale:

- Large anchor specs need the same durable spec quality as small/medium specs plus an additional handoff role: they preserve decisions for future phase-plan drafting.

Acceptance links:

- Covered by AC-005 and AC-007.

Notes:

- Use the homework example's layered mid-level objectives as inspiration for phase decomposition and cross-phase acceptance, but keep the harness schema and lifecycle language.

REQ-006: The large/phased phase-plan template inherits the updated plan structure while preserving phase-specific fresh-thread execution.

Rationale:

- Phase plans are executable handoffs. They should include input artifacts, traceability, dependencies, exact validation expected signals, documentation tasks, and completion criteria like the small/medium plan, but scoped to one phase.

Acceptance links:

- Covered by AC-006 and AC-007.

REQ-007: The update avoids broad duplicated policy prose.

Rationale:

- Previous harness refactors deliberately moved reusable rules into canonical modules. Template improvements should cite those rules and add artifact-shape prompts, not reintroduce duplicated policy blocks.

Acceptance links:

- Covered by AC-007 and AC-008.

REQ-008: Validation and changelog behavior remain intact.

Rationale:

- The implementation changes current harness surfaces and must keep structural validation passing and changelog discipline synchronized with planned commits.

Acceptance links:

- Covered by AC-008 and AC-009.

## Acceptance Criteria

AC-001: `artifact-contract.md` defines small/medium work as work that can be safely coordinated by one orchestration thread with bounded delegation, and defines large/phased work as work that needs anchor/phase planning because that criterion does not hold or staged review materially reduces risk.

Verifies:

- REQ-001

Method:

- Review the `## Work sizes` section after implementation.

AC-002: `artifact-contract.md` references `module:models` or `subagent-model-policy.md` for sub-agent strategy, context strategy, concurrency, and final integration ownership instead of copying those details.

Verifies:

- REQ-001 and REQ-002

Method:

- Review lifecycle wording and run duplicate-policy validation.

AC-003: README includes operator-facing wording that explains small/medium versus large/phased through the orchestration-thread boundary and includes the Scrum Guide analogy as an analogy only.

Verifies:

- REQ-003

Method:

- Review README diff.

AC-004: The small/medium spec and plan templates have no remaining guidance that frames the default boundary as one implementation thread instead of one orchestration thread with bounded delegation.

Verifies:

- REQ-004

Method:

- Run a targeted search for `one implementation thread` and review surrounding small/medium template wording.

AC-005: The large/phased spec template includes source/intent, scope boundary, repository context, requirements, acceptance criteria, interfaces/data/control-flow prompts, risks/rejected alternatives, phase decomposition, model/sub-agent strategy, documentation matrix, readiness checklist, planned commits, freeze-gate, and approval sections.

Verifies:

- REQ-005 and REQ-007

Method:

- Review template headings and prompt content after implementation.

AC-006: The large/phased phase-plan template includes input artifacts, spec traceability, implementation approach, change surfaces, readable model/sub-agent strategy, SMART task guidance with explicit dependencies, validation plan with expected signals, documentation tasks, variance handling, freeze gate, handoff output, readiness checklist, completion criteria, and approval sections.

Verifies:

- REQ-006 and REQ-007

Method:

- Review template headings and prompt content after implementation.

AC-007: The large/phased templates clearly distinguish anchor-spec responsibilities from phase-plan responsibilities without duplicating the full small/medium template prose or canonical policy text.

Verifies:

- REQ-005, REQ-006, and REQ-007

Method:

- Review diff and run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

AC-008: Harness validation passes after the implementation.

Verifies:

- REQ-002, REQ-007, and REQ-008

Method:

- Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

AC-009: The implementation commit updates `CHANGELOG.md` newest-first with a heading synchronized to the planned implementation commit subject.

Verifies:

- REQ-008

Method:

- Review changelog and commit subject before committing.

## Interfaces, Data, and Control Flow

### Interfaces affected

- `.agents/skills/dev-doc-harness/references/artifact-contract.md`: normative lifecycle sizing rule.
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`: possible narrow cross-reference support for lifecycle sizing.
- `README.md`: operator-facing overview.
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`: small/medium spec template wording.
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`: possible alignment wording.
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`: large anchor spec template structure.
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`: phase plan template structure.
- `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: possible validator evidence update.
- `CHANGELOG.md`: implementation entry before commit.

### Data, config, and persistence

- No runtime data, persistence, configuration, or package release identity changes are expected.

### State and control flow

- Planning control flow remains the same: small/medium uses spec+plan; large/phased uses anchor-spec-first followed by phase-plan drafting only after the appropriate freeze and fresh operator instruction.
- The classification guidance changes so the routing decision explicitly asks whether one orchestration thread can safely coordinate the work with bounded delegation.

### Safety, security, privacy, migration, and rollback

- No runtime security, privacy, migration, or rollback effects are expected.
- Process-safety effect: high-blast-radius, migration, security, privacy, compliance, or orchestration-heavy work should be more likely to take the large/phased path before implementation begins.

## Risks and Rejected Alternatives

RISK-001: The lifecycle rule could overfit to orchestration-thread capacity and ignore high-risk work that technically fits in one thread.

Decision or mitigation:

- Keep breadth and risk escalation indicators in `## Work sizes`, and define large/phased handling as appropriate when staged review materially reduces risk even if one thread might technically coordinate the work.

RISK-002: The templates could duplicate canonical policy while trying to make inheritance explicit.

Decision or mitigation:

- Use short local prompts and cite `module:lifecycle`, `module:quality`, `module:models`, and `module:freeze-gate` for reusable rules.

RISK-003: Large/phased templates could become too heavy to fill out.

Decision or mitigation:

- Use the updated small/medium structure as the information architecture, but phrase large-specific additions around anchor decisions, phase objectives, traceability, and fresh-thread executability.

RISK-004: The Scrum analogy could confuse operators into thinking the harness follows Scrum.

Decision or mitigation:

- State it as an analogy only and keep it to the sizing/readiness concept.

RISK-005: Borrowing from the homework examples could pull in domain-specific FinTech content.

Decision or mitigation:

- Borrow only the layered planning pattern: high-level objective, mid-level objectives, nonfunctional/policy expectations, implementation guardrails, beginning/ending context, and low-level executable tasks.

RISK-006: Validator golden traversal checks may expect old phrases.

Decision or mitigation:

- Run the harness validator and update only evidence patterns that directly need to follow the new wording.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spike: orchestration-sizing-large-templates -- approve sizing and large-template plan` | `2026-07-02_orchestration-sizing-large-templates -- approve sizing and large-template plan` | Approval commit for this spec and plan. |
| Implementation | `docs: orchestration-sizing-large-templates -- align sizing and phased templates` | `2026-07-02_orchestration-sizing-large-templates -- align sizing and phased templates` | Implementation commit for lifecycle, README, template, validator-if-needed, and changelog updates. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required before approval and implementation commits; title snippets synchronized with planned commit subjects. |
| Test cases | Snapshot | No | Not applicable | Not applicable | Existing harness validator plus targeted text checks cover this template/policy change. |
| Testing guide delta | Living delta | No | Not applicable | Not applicable | No testing-guide workflow change expected. |
| Operator manual delta | Living delta | No | Not applicable | Not applicable | README is the operator-facing update for this work. |
| API reference delta | Living delta | No | Not applicable | Not applicable | No public API changes. |
| Architecture snapshot | Snapshot | No | Not applicable | Not applicable | This clarifies existing lifecycle and template structure, not harness architecture ownership. |
| Architecture summary delta | Living delta | No | Not applicable | Not applicable | No long-lived architecture-doc change expected. |

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
