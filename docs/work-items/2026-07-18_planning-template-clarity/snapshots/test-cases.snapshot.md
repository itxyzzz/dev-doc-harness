# Planning Template Clarity Test Cases

Work ID: `2026-07-18_planning-template-clarity`
Short ID: `planning-template-clarity`
Status: Approved
Harness release: `0.7+`
Schema: `schema:snapshot.test-cases`

## `TC-001` Completion guidance is a literal checklist

Given an agent finishes harness-managed work, when it reads the `SKILL.md` completion section, then every verification item uses literal Markdown checkbox syntax and remains a scannable unordered checklist.

## `TC-002` Every commitment has the complete structure

Given a spec contains `SPEC-002` or a later commitment, when an author follows the shared template, then that commitment uses the same Statement and local Verification Criterion structure as `SPEC-001`, unless a genuinely cross-cutting criterion explicitly covers it.

## `TC-003` Undefined commitment classification is absent

Given an author reads current quality policy and either generated spec template, when no classification taxonomy is defined or consumed, then the artifact does not prompt for `Classification is optional` or the illustrative `Constraint · Preserve` line.

## `TC-004` Planned commits store only stage and subject

Given a current spec, plan, phase plan, or amendment records planned commits, when the author fills the section, then the table or list contains the stage and planned subject. It does not require separate changelog-title or Notes fields; an essential exception note may follow as prose.

## `TC-005` Commit boundaries are meaningful rather than task-count driven

Given a plan contains several tasks, when it plans implementation commits, then one cohesive commit is the default and a split occurs only at a stable, independently reviewable and revertible boundary with relevant checks passing. A Superpowers task is not automatically a commit boundary.

## `TC-006` Planning observations may remain unknown

Given the platform does not expose the planning task's model generation, profile, reasoning effort, or context state, when the plan records planning-task observations, then those observation fields may say `not exposed` without weakening the future execution recommendation.

## `TC-007` Approved execution selection is actionable

Given a substantial plan is ready to freeze, when it records the approved execution selection, then it names an actionable target model/profile or policy-relative selection instruction, capability tier, reasoning effort, orchestration mode, fallback, execution continuity, and rehydration requirement. None of those recommendation fields says `not exposed`.

## `TC-008` Unknown suitability prefers a fresh curated task

Given substantial execution will use a different intended profile, or the current model/profile or context suitability cannot be verified, when continuity is selected, then the default is a new task with curated-artifact handoff. Given the current profile is known suitable or a concrete continuity reason is recorded, same-task continuation remains allowed.

## `TC-009` Superpowers execution data is plan metadata

Given a frozen plan will use Superpowers after fresh authorization, when the generated plan is read, then its execution method and workflow appear in the actual metadata header and the document does not contain a normal `## Superpowers execution meta-header` section.

## `TC-010` Combined small/medium handoff has one owner

Given a combined small/medium package freezes, when transition routing runs, then the spec identifies the plan as transition owner without repeating the complete handoff, and the plan supplies the exact implementation handoff. Given a spec-only staged exception, the spec instead records its reason and plan-drafting next activity.

## `TC-011` Large phases use a rolling loop

Given an approved large anchor contains multiple phases, when normal orchestration proceeds, then it drafts and freezes phase 1, implements phase 1, records its actual outputs, and uses those outputs to draft phase 2. Planning or freezing several phases before implementation requires an explicit stable-and-independent-phases exception.

## `TC-012` Phase plans distinguish two transitions

Given a phase plan is ready to freeze, when its handoffs are reviewed, then it separately names the current-phase implementation handoff and the expected post-phase transition to next-phase planning or work-item completion. At completion, the executor reports actual outputs, validation, variance, and commit state for that transition.

## `TC-013` Superpowers respects harness plan form and commits

Given Superpowers methodology is active, when its generic defaults conflict with the approved harness plan, then the canonical work-item location, numbered harness task steps, approved commit boundaries, recorded execution method, and harness freeze route take precedence. Other Superpowers methodology remains available inside that boundary.

## `TC-014` Active validation remains structural and history-safe

Given the focused policy validator runs, when it checks this clarification, then it validates canonical owners, source blocks, assemblies, generated templates, and synthetic fixtures. It does not judge subjective model fit, derive commit quality from task count, or reject frozen historical work-item artifacts.

## `TC-015` Every upcoming stage assesses bounded delegation

Given a harness transition is about to start spec drafting, plan or phase-plan drafting, amendment or replanning, implementation, or consequential review, when the orchestration agent selects the strategy, then it evaluates whether bounded sub-agents would materially improve isolation, independent review, parallelism, specialized execution, or risk reduction. It records either a concrete proposed strategy or `Sub-agents: None` with a stage-specific fit reason.

## `TC-016` Useful delegation triggers one scoped approval request

Given the upcoming-stage assessment finds useful sub-agent work that is not already authorized, when the transition is presented, then the agent asks the operator to approve the recorded roles, context, outputs, model/effort envelope, write authority, concurrency, and fallback before dispatch. Explicit approval permits in-envelope use without another generic confirmation, but does not override unavailable tooling, higher-priority platform restrictions, task scope, or out-of-envelope reapproval.

## Approval

- Status: Approved
- Superseded by: None
