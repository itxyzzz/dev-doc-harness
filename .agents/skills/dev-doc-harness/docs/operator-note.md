# Dev Doc Harness Operator Note

This note travels with the copyable harness package. It is a compact usage summary for operators and adopters; canonical policy still lives in `AGENTS.md`, `SKILL.md`, and the routed references under `.agents/skills/dev-doc-harness/references/`.

The harness keeps important development decisions out of disappearing chat history. It creates reviewable plans before substantial edits, separates delivery commitments from evidence, preserves handoffs for fresh threads, records meaningful drift, and avoids routine root-changelog conflicts across parallel work.

At each review or start boundary, the artifact and chat show what happens next, how it will run, and any decision you need to make.

Normal use remains simple: ask for the work you want and refine it through the conversation. The agent applies the harness when needed; explicit prompts are useful only when you want a special stop point or review checkpoint.

## What To Copy

The distributable package is:

- root `AGENTS.md`
- `.agents/`

Do not copy this repository's root `README.md`, `CHANGELOG.md`, `TODO.md`, or `docs/work-items/` into downstream projects. Downstream repositories keep their own work-item history.

If the destination repository already has an `AGENTS.md`, merge the harness instructions with the local repository instructions instead of replacing local policy. Commit the harness adoption separately from product work so rollback is a normal revert of that dedicated update.

## How Operators Use It

Ask for the work normally. For repository development beyond a very small mechanical edit, the harness applies its planning and approval flow automatically; you do not need to invoke the skill or know its internal routes.

For substantial work, expect a reviewable package under `docs/work-items/<work-id>/`. Lean/small is an additive combined spec-and-plan route for bounded, low-risk work with a known local surface; you may explicitly select it. If material architecture, interface, migration, security, or uncertainty appears, the work must escalate before freeze to small/medium or large/phased. Small or medium work normally has a combined spec and plan. You can request or approve a staged spec-only package when you want planning to stop before the plan is drafted. Large work keeps separate anchor and phase-plan boundaries. The established small/medium and large/phased names remain pending a separate terminology work item. Stable IDs provide reference points for review and handoff without requiring you to follow an internal traceability scheme.

Some work items include a short architecture snapshot when an important decision or tradeoff needs to survive the handoff. This work-item architecture records decisions for that package; a repository-wide `ARCHITECTURE.md` or similar durable repository-wide documents are not covered by the harness.

## Review And Pause Points

The normal flow is simple:

1. The agent drafts the current planning package; you review and approve it; the agent then freezes it and pauses.
2. The documented next activity begins only after your fresh instruction: phase-plan drafting after an anchor freeze, or implementation after a combined or phase-plan freeze.
3. Once started, planned safe work continues without routine pauses between tasks.
4. Small equivalent adjustments are recorded as drift. Material changes to outcomes, architecture, APIs, data, security, privacy, compliance, scope, or evidence return to you for an amendment and approval.
5. When the plan includes an independent reviewer, its findings are resolved or reported before completion.

A combined small/medium plan hands off directly to implementation. Large work normally freezes its anchor, then plans, freezes, and implements one phase at a time so actual results can inform the next phase. Before each stage, the planning package provides the full recommended orchestration and model selection strategy for this stage, including the use of sub-agents and what for. An approved strategy is not presented for confirmation again unless circumstances change.

Independent review remains the default. If review cannot run or you decline it, the agent explains the assurance gap and compensating validation, then asks once whether to proceed when your decision is still needed. At execution start, you may choose another available method, model, reasoning effort, or task location without changing the plan solely for that runtime choice.

For implementation-stage changelog authoring, follow `module:implementation-changelog`. Root `CHANGELOG.md` remains the later consolidated publication view at a project-owned checkpoint. A downstream product/application release keeps its own release process.

## Using Superpowers

You do not need to choose between Superpowers and the harness. They are responsible for different layers in the planning and execution process, and the harness is designed to work well alongside Superpowers.

The harness owns the durable plan and its lifecycle, adding structure and controlled flow, and explicitly overriding the default work-item folder. It oversees orchestration of the workflow on the higher level, first creating the durable planning documents, including the spec and detailed implementation plan with tasks and checks, and then handing this plan off controllably to implementation. For implementation, it explicitly prefers `superpowers:subagent-driven-development`, when available and suitable, followed by `superpowers:executing-plans`.

When invoked this way, Superpowers consumes the durable plan and takes responsibility for its implementation. When `superpowers:subagent-driven-development` is used, it creates another layer of sub-agents orchestration, one per Plan Task. This workflow uses a plan-specific, git-ignored workspace under `.superpowers/sdd/<plan-basename>/` for its ledger, briefs, reports, and review packages.

When both are active, Superpowers may shape how the agent works, while the harness remains the visible repository record for planning, approval, drift, and completion evidence. If Superpowers is unavailable, the same plan and checks still support ordinary agent execution. In either case, the harness retains final integration and completion-report ownership.

The harness does not create a parallel `docs/superpowers` package. If that directory already exists and contains previous documentation packages from before the current work, a new compatibility file is only a short pointer to the canonical harness package.

## Useful Explicit Requests

Use ordinary work requests by default. These requests are useful when you need to make a special boundary unambiguous:

```text
Plan this as a large work item and stop after the freeze gate.
```

```text
Create a plan-only PR checkpoint before code changes.
```

```text
Use one additional security-lens review sub-agent with a flagship-tier model at high reasoning.
```

## Changelog

Each work item may keep an implementation changelog fragment under `docs/work-items/<work-id>/changelog/`. It records delivered implementation work and keeps that entry aligned with the implementation commit subject without turning the root `CHANGELOG.md` into a working log.

The root changelog remains the curated publication view. Reviewed fragments can be consolidated at a project-owned checkpoint, such as after work branches merge or before release-note preparation or a product/application release:

```bash
python .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py
```

This separation gives the harness a consistent record while downstream projects keep their own release processes.

## For Harness Maintainers

The following is for people changing the copied harness itself, not ordinary operators using it for product work. Run the package validation command when practical:

```bash
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

The validator is a lightweight structural check. It supports review; it does not replace operator approval or engineering judgment.

Primary planning templates are maintained from ordered source files:

```text
.agents/skills/dev-doc-harness/assets/templates/blocks/
.agents/skills/dev-doc-harness/assets/templates/assemblies/
.agents/skills/dev-doc-harness/scripts/assemble_templates.py
```

Edit blocks or manifests, then run:

```bash
python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write
```

The command writes the flat templates, checks that they are current, and runs the full validator. Use `--list` to inspect the block order or `--check` for a non-mutating freshness check.

Optional root-local hook files under `.githooks/` are development aids for this repository only. They are outside the distributable package and are not copied to downstream adopters.
