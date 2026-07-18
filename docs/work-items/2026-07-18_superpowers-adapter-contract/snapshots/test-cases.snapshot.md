# Superpowers Adapter Contract Test Cases

Work ID: `2026-07-18_superpowers-adapter-contract`
Short ID: `superpowers-adapter-contract`
Status: Approved
Harness release: `0.7+`
Schema: `schema:snapshot.test-cases`

## `TC-001` Project guidance overrides the Superpowers default path

Given Superpowers proposes its default spec or plan location for harness-managed work, when an agent reads a merged project-specific `AGENTS.md` or the README's global `AGENTS.md` bootstrap snippet, then it uses `docs/work-items/<work-id>/` for every new durable spec, plan, snapshot, handoff, and changelog source.

## `TC-002` Historical continuity remains the only `docs/superpowers` exception

Given `docs/superpowers` is absent, empty, or created during the current work, when planning or execution needs an artifact, then no directory or duplicate file is created there. Given the directory predates the work and contains historical packages, a new continuity file may be only a title, status, and link to the canonical work-item artifact.

## `TC-003` Conditional execution metadata preserves harness authority

Given a frozen canonical plan records Superpowers as the approved execution method, when its generated plan shape includes the merged execution meta-header, then the header points to the post-freeze route and retains harness ownership of scope, model-policy bounds, variance, and final integration. Given Superpowers is not the approved method, the canonical plan does not require that header.

## `TC-004` Executable tasks use numbered steps rather than task checkboxes

Given a generated plan defines a `TASK-*` implementation sequence, when an executor reads the task, then the steps are numbered. A checkbox list inside that executable task sequence is rejected; a non-executable readiness indicator outside task steps is not treated as a task-step violation.

## `TC-005` Global Constraints are conditional and non-duplicative

Given approved commitments, architecture decisions, task instructions, and Plan Checks already make a task self-contained, when the plan is generated, then it does not add a Global Constraints section merely to repeat them. Given a concise shared constraint or reference is needed for a fresh executor, then the plan includes it or equivalent task-local context.

## `TC-006` Interfaces remain distinct from dependencies

Given one task needs an output from another, when the plan records their relationship, then Dependencies identify readiness or execution order and Interfaces identify the consumed inputs and produced outputs. A task that labels an ordering relationship as an interface, or an input/output contract only as a dependency, is rejected by the focused fixture.

## `TC-007` Superpowers aids remain inside the approved lifecycle

Given a plan has frozen and a fresh operator instruction authorizes execution, when Superpowers performs pre-flight review or creates a task brief, review package, or progress ledger, then those artifacts remain ephemeral and do not create a second approval route or canonical planning package. The plan does not ask a second generic Superpowers execution-mode question after this boundary.

## `TC-008` Fallback is independently executable and verifiable

Given Superpowers or explicit dispatch controls are unavailable, when execution continues under the approved harness strategy, then the orchestration thread performs the task with a concise independently-executable and verifiable task shape and the recorded validation checks. It does not adopt a competing detailed task-sizing method or silently broaden the execution strategy.

## `TC-009` Runtime values remain honest

Given the platform does not expose model generation, resolved profile, or reasoning effort, when planning or reporting allocation, then those fields use `not exposed` while the policy-relative recommendation remains visible. Given the platform or operator exposes a value, then the actual value is reported separately from the recommendation.

## `TC-010` Every Superpowers dispatch names an in-envelope allocation

Given Superpowers dispatches a small executor or reviewer under the approved `economy-default` strategy, when the dispatch is prepared, then it explicitly names its policy-relative capability tier and reasoning effort and stays within the recorded availability, fallback, concurrency, write-authority, and review boundaries. Silent inheritance of an unknown session allocation is rejected.

## `TC-011` Out-of-envelope dispatch requires approval

Given a proposed Superpowers dispatch would use a stronger tier or effort, more concurrency, broader write authority, or a different review boundary than the frozen strategy permits, when the difference is identified, then the workflow routes it through the existing approval path before dispatch.

## `TC-012` Validation targets active owners, not frozen history

Given structural validation runs after the adapter implementation, when it inspects the contract, then it checks active guidance, source blocks, generated templates, and synthetic fixtures. It does not rewrite or reject frozen historical work-item artifacts merely because their legacy Superpowers wording differs.

## Approval

- Status: Approved
- Superseded by: None
