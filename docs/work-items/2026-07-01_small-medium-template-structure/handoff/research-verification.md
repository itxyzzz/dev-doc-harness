# Research Verification: Small/Medium Spec Template Structure

Work ID: `2026-07-01_small-medium-template-structure`
Status: Approved
Snapshot policy: source evidence is referenced below; this report is a derived research artifact for review.

## Verification summary

This pass now focuses on the small/medium spec template only. Plan and task-template improvements are intentionally deferred until the spec structure is settled.

The current small/medium spec template covers the required harness contract, but it behaves more like a section checklist than an agent-ready review artifact. The useful upgrade is stronger information architecture:

- separate source intent, repository context, scope boundaries, requirements, acceptance criteria, and review readiness;
- make unresolved decisions visible before freeze;
- prompt for evidence and known unknowns without forcing a large-work research phase;
- distinguish requirements from acceptance criteria with examples;
- avoid wide tables with long text because they are hard to read in the current UI.

For this harness, the spec should remain a compact durable handoff artifact at `spec_<short-id>.md`. Supplemental snapshots or deltas should remain optional and only appear when the documentation matrix says they are required.

## Verified claims

### Local harness fit

The local quality module requires durable specs to preserve goals, scope, interfaces, data, state/control flow, risks, tests, acceptance criteria, assumptions, known unknowns, and rejected alternatives. The current small/medium spec template has most of those headings, but it under-prompts for:

- source input and intended operator/user outcome;
- assumptions and open questions;
- repository evidence used while drafting;
- state/control flow when relevant;
- rejected alternatives and decision rationale;
- the difference between requirements and acceptance criteria.

Recent approved local work items show the desired level of specificity: concrete expected files, stable interface statements, non-scope boundaries, validation expectations, and planned commit/changelog synchronization. The spec template can better elicit that quality directly.

### GitHub Spec Kit patterns worth borrowing

GitHub Spec Kit presents a spec-driven workflow that creates a feature spec, then a technical implementation plan, then an actionable task list. Its README describes commands for specifying product intent, planning technical implementation, generating tasks, and implementing. Its templates emphasize user scenarios, independent tests, functional requirements, entities, success criteria, technical context, project structure, constitutional gates, and task grouping.

Borrow for the spec:

- clear separation of product/operator intent from technical implementation;
- user scenarios or operator scenarios with independent test statements;
- functional requirements and success criteria as different kinds of information;
- optional research/design outputs when decisions need evidence;
- consistency/readiness checks before implementation.

Adapt for this harness:

- Keep all default small/medium spec content in `spec_<short-id>.md`; do not create separate Spec Kit-style files by default.
- Replace constitutional gates with this harness's freeze-gate and documentation-matrix readiness checks.
- Treat research, data-model, contracts, and quickstart outputs as optional snapshots/deltas, not mandatory files.
- Use operator scenarios for documentation/process work where user stories would be artificial.

Avoid:

- feature-numbered branch semantics that conflict with harness work IDs;
- mandatory user stories for all work;
- full Spec Kit executable-spec framing as a policy change.

### Kiro and EARS patterns to treat cautiously

Kiro's requirements/design/tasks split is directionally similar to Spec Kit, but its EARS-style requirement phrasing is not a good fit for this harness's default template voice. In particular, the template should not use "shall" language.

Borrow only the underlying discipline:

- acceptance criteria should name a condition or trigger when that makes behavior clearer;
- acceptance criteria should describe observable behavior;
- requirements should be structured enough that reviewers can spot ambiguity.

Avoid:

- "shall" phrasing;
- forcing EARS notation into the template;
- presenting EARS as a preferred framework when the useful parts are already covered by clearer scenario and acceptance-criteria patterns.

### BDD/Gherkin patterns worth borrowing carefully

Cucumber's Gherkin reference frames examples around initial context, event, and expected outcome. That can be useful for a spec when borrowed carefully.

Borrow:

- short examples that focus on observable outcomes;
- Given/When/Then examples when they clarify behavior better than prose;
- small data examples when several cases are easy to misunderstand.

Adapt:

- Use examples inside the spec as review aids, not executable `.feature` files.
- Keep examples optional. Many documentation/process changes are clearer with plain acceptance bullets.
- Prefer outcome-focused examples over UI-step scripts unless manual UI validation is the actual acceptance surface.

Avoid:

- one scenario per requirement as a hard rule;
- imperative click-path scenarios when the spec should define behavior.

### INVEST and SMART patterns for specs

Bill Wake's INVEST guidance is powerful, but most of it is more useful before the spec is written, while the operator and agent are negotiating possible requirements and scope.

Use INVEST like this:

- `N` Negotiable and `V` Valuable are most useful while splitting, prioritizing, deferring, or re-scoping candidate requirements. They help compare value against complexity/cost before the approved spec settles. Once the spec is approved, there is much less room to apply them.
- `E` Estimable and `S` Small should be adapted to this harness as "bounded enough for the context window" and "likely implementable in one thread." If that is not true, the work may need large/phased handling.
- `I` Independent and `T` Testable remain critical in the spec. Requirements should be separable enough to review, defer, or validate, and each accepted outcome should have a clear verification path.
- Vertical slicing is preferred at the spec/outcome level: scope should be organized around independently valuable outcomes where possible. Do not automatically carry that into the later task breakdown, where vertical slices can be counter-productive if shared setup, refactors, or test scaffolding need to happen first.

Use SMART more directly in the spec:

- Specific: each requirement names the concrete behavior, documentation surface, interface, or decision being changed.
- Measurable: each acceptance criterion has an observable result or review signal.
- Achievable: the spec stays within small/medium scope and calls out when work may exceed one implementation thread.
- Relevant: every requirement connects back to the stated operator/user outcome.
- Time-bounded: the spec names the lifecycle boundary, such as before freeze, before implementation, during validation, or before commit. Use calendar deadlines only when the operator gives one.

## Requirements versus acceptance criteria

A requirement says what the work must provide or preserve. It belongs in the spec because it defines scope.

An acceptance criterion says how a reviewer, test, command, or manual check can tell that the requirement has been satisfied. It belongs near the requirement, but it is not the same thing.

Example:

```md
Requirement REQ-001: The small/medium spec template captures unresolved decisions before planning freeze.

Rationale:
Agents need a visible place to preserve ambiguity instead of silently filling gaps or losing them during handoff.

Acceptance criteria:

- AC-001: Given a draft spec with an unresolved interface decision, the spec contains an `Open questions` entry that names the decision and the owner or later event needed to resolve it.
- AC-002: Given a draft spec with no unresolved decisions, the `Open questions` section explicitly says `None identified after repository-context review`.
- AC-003: During draft review, a reviewer can find unresolved decisions without reading the plan or chat history.
```

In this example, `REQ-001` defines the required capability of the template. `AC-001` through `AC-003` define observable checks for whether the template and a filled-out spec actually satisfy it.

## Recommended small/medium spec structure

Use this as the structural target for a later template edit:

```md
# <Work Item Name> Spec

<metadata block>

## Source and Intent
- Source input:
- Desired operator/user outcome:
- Success summary:

## Scope Boundary
### In scope
### Non-scope
### Assumptions
### Open questions

## Repository Context
### Current state
### Evidence read
### Constraints and compatibility

## Requirements

REQ-001: <specific requirement>

Rationale:
<why this requirement belongs in scope>

Acceptance:
- <linked acceptance criterion IDs or short summary>

Notes:
- <optional constraints, dependencies, or deferrals>

## Acceptance Criteria

AC-001: <observable outcome or scenario>

Verifies:
- <requirement ID or scope item>

Method:
- <test command, manual check, review finding, or operator acceptance>

## Interfaces, Data, and Control Flow
### Interfaces affected
### Data/config/persistence
### State/control flow
### Security/privacy/migration/rollback

## Risks and Rejected Alternatives

RISK-001: <risk or rejected alternative>

Decision or mitigation:
- <decision, mitigation, or reason for rejection>

## Planned Commits

## Documentation Artifact Matrix

## Spec Readiness Checklist
- [ ] Source input and desired outcome are captured.
- [ ] Scope and non-scope are explicit.
- [ ] Assumptions and open questions are either listed or explicitly absent.
- [ ] Requirements are specific, relevant, and bounded enough for small/medium work.
- [ ] Acceptance criteria are observable and testable.
- [ ] Repository evidence and compatibility constraints are recorded.
- [ ] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [ ] Documentation matrix decisions have paths or reasons.
- [ ] No unresolved placeholders remain.

## Approval
```

Notes:

- Use ID-style labels only where they help review and later plan traceability.
- Avoid wide tables with long content. Prefer short bullets or card-style blocks for requirements, criteria, risks, and rejected alternatives.
- `Evidence read` should list repository files/docs already inspected, not every possible file.
- `Open questions` may be `None` only after the agent has made reasonable local-context checks.
- `Interfaces, Data, and Control Flow` can contain `None` entries for documentation-only work, but the prompts should force the check.

## Prioritized spec-only options

### Option A: Minimal structural upgrade

Add only these changes:

- `Source and Intent`
- `Assumptions` and `Open questions`
- `Evidence read`
- separate `Requirements` and `Acceptance Criteria`
- `Spec Readiness Checklist`

This is the best first implementation because it improves handoff quality without making the template feel heavy.

### Option B: Scenario-centered upgrade

Add optional operator/user scenario examples and optional Given/When/Then examples for acceptance criteria.

This is useful for feature and behavior changes, but should remain optional because many harness work items are documentation/process changes.

### Option C: Full external-framework adoption

Adopt Spec Kit, Kiro, EARS, or Gherkin formats wholesale.

This is not recommended. The useful ideas should be adapted into the harness spec template without importing external workflow assumptions.

### Option D: Presentation pass

Improve headings, tables, examples, placeholder style, and reviewer readability.

Defer this until after the spec structure is settled. Presentation should make the template easier to fill out, not add new policy requirements.

## Future plan/template pointers

These are intentionally deferred until the spec template direction is approved:

- map spec acceptance criteria to plan tasks and validation commands;
- decide how SMART should shape task wording;
- decide where task dependency/order notes belong;
- avoid forcing vertical slices in implementation tasks when setup, shared tests, or refactors should happen first;
- keep any plan traceability readable in the current UI.

## Future presentation pointers

- Prefer examples that demonstrate the expected filled-out level of detail over long instruction prose.
- Mark optional sections clearly with "Use when..." prompts.
- Use consistent placeholder tokens, and avoid angle-bracket placeholders where the validator or reader might mistake them for unresolved final content.
- Add a brief "delete this row when not applicable" convention to example blocks.
- Keep any table to short labels or two columns when cells contain more than a couple of words.

## Quality assessment

The recommendations are compatible with the local harness if implemented as template scaffolding, not as new lifecycle policy. The safest near-term change is Option A. Option B can be included as optional examples. Option C should be rejected. Option D should be tracked for later presentation work.

## References

- Local: `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- Local: `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- Local: `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- Local: `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- Local: `docs/work-items/2026-06-23-documentation-improvements/spec-documentation-improvements.md`
- Local: `docs/work-items/2026-06-23-documentation-improvements/plan-documentation-improvements.md`
- Local: `docs/work-items/2026-07-01-naming-conventions/spec-naming-conventions.md`
- Local: `docs/work-items/2026-07-01-naming-conventions/plan-naming-conventions.md`
- GitHub Spec Kit repository and README: https://github.com/github/spec-kit
- GitHub Spec Kit methodology: https://raw.githubusercontent.com/github/spec-kit/main/spec-driven.md
- GitHub Spec Kit spec template: https://raw.githubusercontent.com/github/spec-kit/main/templates/spec-template.md
- GitHub Spec Kit plan template: https://raw.githubusercontent.com/github/spec-kit/main/templates/plan-template.md
- GitHub Spec Kit tasks template: https://raw.githubusercontent.com/github/spec-kit/main/templates/tasks-template.md
- Kiro specs concepts: https://kiro.dev/docs/specs/concepts/
- EARS official guide: https://alistairmavin.com/ears/
- Cucumber Gherkin reference: https://cucumber.io/docs/gherkin/reference/
- Bill Wake, INVEST and SMART tasks: https://xp123.com/invest-in-good-stories-and-smart-tasks/
