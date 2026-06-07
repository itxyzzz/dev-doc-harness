# Plan Amendment 001: Architecture Guardrails

Work ID: `2026-06-05-refactor-as-code`
Short ID: `refactor-as-code`
Status: Approved

## Original plan reference

- File: `docs/work-items/2026-06-05-refactor-as-code/spec-refactor-as-code.md`
- Section or task: `Proposed behavior`, `Phase decomposition`, and `Acceptance criteria`
- Original instruction: Refactor harness instructions into maintainable policy modules with stable rule interfaces, slimmer templates, retrieval routing, and validation hardening.

## Discovered issue

The approved anchor spec captures the main refactor direction, but several architecture guardrails should be explicit before Phase 01 planning starts. Without these guardrails, the refactor could still produce ambiguous authority, unclear dependency direction, examples that behave like policy, an under-specified retrieval router, or validation that checks links without proving real harness behavior.

Full rule versioning is intentionally deferred. Taking on a complete versioning and compatibility system during this refactor would expand the scope too far. Phase 01 should still avoid choices that make later rule versioning impossible.

## Proposed change

Phase 01 must add these architecture deliverables before later phases split references or slim templates:

- Precedence and authority model: define which instruction source wins when `AGENTS.md`, `SKILL.md`, canonical references, templates, frozen work-item artifacts, README summaries, and operator instructions disagree.
- Dependency graph: define allowed reference directions, such as `AGENTS.md` to `SKILL.md`, `SKILL.md` to router and modules, templates to schemas/rule IDs, README to summaries, and work items to selected decisions and exceptions.
- Content-type taxonomy: label or structure instruction material as normative policy, artifact schema, example, advisory guidance, or operator-facing summary so examples and summaries do not become competing policy.
- Operation router taxonomy: define common harness operations and the minimum required modules for each operation, including classify work, draft small/medium artifacts, draft large anchor specs, freeze planning packages, draft phase plans, execute approved work, record variance, use sub-agents, review artifacts, and update templates.
- Architectural metrics: define measurable budgets or checks for maximum common-operation traversal depth, eager-load words, duplicated policy prose, template policy prose, and broken rule references.
- Golden scenario tests: define sample harness behaviors that must continue to work, including very-small mechanical skip, small/medium planning, large anchor freeze, phase-plan freeze, post-freeze implementation authorization, variance amendment, sub-agent authorization, Superpowers compatibility, and historical artifact handling.
- Work-item artifact locality: define when this harness repository tracks its own `docs/work-items/` planning packages even though that folder is generally ignored for local planning work.

Full rule versioning remains deferred. Phase 01 should record a lightweight compatibility note explaining that rule IDs are stable identifiers for the refactor, not a complete versioned policy system, and should list rule versioning as future work unless the operator explicitly expands scope.

## Reason this change is necessary

The implementation cannot safely proceed from the approved spec alone because the highest-risk architectural failure mode is not just duplicated text. It is ambiguous ownership: agents may not know which instruction wins, which files may depend on which other files, whether a block is policy or example, or whether a retrieval path is safe. These decisions should be settled before implementation changes multiple harness files.

## Impact assessment

| Area | Impact |
|---|---|
| Scope | Expands Phase 01 planning deliverables; does not expand implementation beyond the approved harness refactor. Full rule versioning is deferred. |
| Acceptance criteria | Adds explicit architecture acceptance criteria for precedence, dependency direction, content typing, operation routing, metrics, scenario tests, and artifact locality. |
| API/interface | Affects the internal harness instruction interface: rule IDs, router entries, module references, and template references. |
| Data model/migration | No repository data migration. Historical work-item artifacts remain immutable snapshots unless explicitly superseded. |
| Security/privacy/compliance | No direct security or privacy impact. Reduces process-safety risk by clarifying authority and avoiding accidental weakening of gates. |
| Tests | Requires Phase 01 or Phase 05 to define golden scenario tests and measurable static checks. |
| Documentation | Requires architecture snapshot and later operator/architecture deltas to include these guardrails. |
| Rollout/operations | Keeps rollout phased. Later phases must validate that common operation paths remain discoverable and safe. |

## Approval

- Required: Yes
- Status: Approved
- Superseded by: None

## Planning artifact freeze gate

When this amendment is ready for operator review, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage the draft amendment without committing, request approval or feedback, revise directly on feedback, and commit only after explicit approval. Implementation and phase planning remain paused until the approved amendment is frozen.
