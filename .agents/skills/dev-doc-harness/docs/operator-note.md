# Dev Doc Harness Operator Note

This note travels with the copyable harness package. It is a compact usage
summary for operators and adopters; canonical policy still lives in
`AGENTS.md`, `SKILL.md`, and the routed references under
`.agents/skills/dev-doc-harness/references/`.

The harness keeps important development decisions out of disappearing chat
history. It creates reviewable plans before substantial edits, separates
delivery commitments from evidence, preserves handoffs for fresh threads,
records meaningful drift, and avoids routine root-changelog conflicts across
parallel work.

Normal use remains simple: ask for the work you want and refine it through the
conversation. The agent applies the harness when needed; explicit prompts are
useful only when you want a special stop point or review checkpoint.

## What To Copy

The distributable package is:

- root `AGENTS.md`
- `.agents/`

Do not copy this repository's root `README.md`, `CHANGELOG.md`, `TODO.md`, or
`docs/work-items/` into downstream projects. Downstream repositories keep their
own work-item history.

If the destination repository already has an `AGENTS.md`, merge the harness
instructions with the local repository instructions instead of replacing local
policy. Commit the harness adoption separately from product work so rollback is
a normal revert of that dedicated update.

## How Operators Use It

Ask for the work normally. For repository development work beyond a very small
mechanical edit, the agent loads:

```text
.agents/skills/dev-doc-harness/SKILL.md
```

The router sends the agent to the smallest useful set of canonical references
for sizing, planning, freeze gates, implementation, variance, changelog source
fragments, release context, naming conventions, and model or sub-agent policy.

For substantial work, expect a work item package under:

```text
<work-item-path>
```

Small or medium work normally has one spec-and-plan package. Large work keeps
its anchor and phase-plan boundaries. Stable `SPEC`, `VER`, `TASK`, `CHECK`, and
`DEC` IDs help readers navigate, but a full mapping is optional unless it helps
coverage, handoff, or deterministic validation.

Use a short architecture snapshot only when a future executor needs a decision
or tradeoff that does not fit clearly in the spec. It is work-item architecture;
`ARCHITECTURE.md` is future work for a separate extension.

## Using Superpowers

Operators do not need to choose between Superpowers and the harness. When both
are active, Superpowers may shape the agent's working method, while the harness
remains the visible repository record for specs, plans, snapshots, variance,
changelog source fragments, and freeze gates.

The reviewable package should still appear under the harness work item folder
before implementation starts. Add `docs/superpowers` documents only when the
directory already exists and contains previous documentation packages from
before the current work; never create or seed it to satisfy that compatibility
condition. When continuity permits a new file there, it must be a short pointer
stub to the harness package rather than a duplicate spec or plan.

The destination repository's project-level or merged global `AGENTS.md`
preference overrides Superpowers' default spec and plan locations. Once the
harness freeze and fresh instruction authorize execution, a conditional
Superpowers execution meta-header may describe that method; task briefs and
review aids remain ephemeral. If Superpowers is unavailable, keep the task
independently executable and verifiable with its recorded checks.

## Review And Pause Points

The normal flow is simple:

1. Draft and approve the planning package.
2. Freeze it once and start only after a fresh instruction.
3. Complete planned safe work without pausing between tasks.
4. Note noteworthy equivalent drift in the variance log; amend only material
   outcome, architecture, API, data, security, privacy, compliance, scope, or
   evidence changes.
5. Use a focused, read-only reviewer when the plan calls for one.

Before ordinary commits, update the work-item changelog fragment and run its
lint command. Root `CHANGELOG.md` is the later consolidated publication view at
a project-owned checkpoint. A downstream product/application release keeps its
own release process.

## Useful Explicit Requests

Use ordinary work requests by default. These requests are useful when you need
to make a special boundary unambiguous:

```text
Plan this as a large work item and stop after the freeze gate.
```

```text
Create a plan-only PR checkpoint before code changes.
```

## For Harness Maintainers

The following is for people changing the copied harness itself, not ordinary
operators using it for product work. Run the package validation command when
practical:

```bash
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

The validator is a lightweight structural check. It supports review; it does
not replace operator approval or engineering judgment.

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

The command writes the flat templates, checks that they are current, and runs
the full validator. Use `--list` to inspect the block order or `--check` for a
non-mutating freshness check.

Optional root-local hook files under `.githooks/` are development aids for this
repository only. They are outside the distributable package and are not copied
to downstream adopters.
