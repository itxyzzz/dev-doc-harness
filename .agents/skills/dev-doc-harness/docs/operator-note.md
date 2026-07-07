# Dev Doc Harness Operator Note

This note travels with the copyable harness package. It is a compact usage
summary for operators and adopters; canonical policy still lives in
`AGENTS.md`, `SKILL.md`, and the routed references under
`.agents/skills/dev-doc-harness/references/`.

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
mechanical edit, the agent should load:

```text
.agents/skills/dev-doc-harness/SKILL.md
```

The router sends the agent to the smallest useful set of canonical references
for sizing, planning, freeze gates, implementation, variance, changelog, release
context, naming conventions, and model or sub-agent policy.

For substantial work, expect a work item package under:

```text
<work-item-path>
```

Small or medium work usually gets a spec and plan. Large or phased work gets an
anchor spec first. Phase plans come later from the approved anchor spec unless
you explicitly ask for combined planning.

Work-item architecture decisions live in the spec and, when useful, in
`snapshots/architecture.snapshot.md`. The snapshot is work-item-bound: it
preserves drivers, constraints, selected approach, affected boundaries, and
rejected alternatives for later implementation or phase planning. Plans consume
that architecture input instead of making hidden architecture decisions.
Repository-level durable documents such as `ARCHITECTURE.md` are future work for
a separate harness extension.

Artifact readability has its own routed owner. Routine artifacts use the short
baseline guidance in `references/durable-planning-quality.md` and the templates.
Large anchor specs, and any artifact that becomes large or hard to scan, load
`references/artifact-style.md` for final artifact content, scannable structure,
placeholder control, traceability density, and template prompt style.

Current naming grammar lives in `references/naming-conventions.md`. For example,
`2026-05-31_artifact-root` uses `spec_artifact-root.md` and
`plan_artifact-root.md`.

## Using Superpowers

Operators do not need to choose between Superpowers and the harness. When both
are active, Superpowers may shape the agent's working method, while the harness
remains the visible repository record for specs, plans, snapshots, variance,
changelog entries, and freeze gates.

The reviewable package should still appear under the harness work item folder
before implementation starts. If a Superpowers workflow also leaves files under
`docs/superpowers`, expect those files to be short pointers to the harness
package rather than duplicate specs or plans.

## Review And Pause Points

The normal substantial-work flow is:

1. The agent drafts the planning artifacts.
2. The agent stages the draft planning package and asks for approval.
3. Operator feedback edits the drafts directly.
4. Operator approval triggers the freeze gate: changelog, approved artifacts,
   approval commit, and a pause.
5. The next operator response may confirm execution settings and authorize
   implementation.

For large or phased work, the anchor-spec freeze also pauses before phase-plan
drafting. Later phase-plan drafting can happen in the main thread, or through
curated-context sub-agents when the phases are independent enough and the
platform supports it.

Frozen planning artifacts should not be silently rewritten to make later
implementation look cleaner. Nontrivial drift is recorded as variance. Drift
that changes architecture, public APIs, data, security, privacy, compliance,
scope, acceptance criteria, or feasibility requires an amendment and approval.

## Useful Prompts

```text
Plan this as a large work item and stop after the freeze gate.
```

```text
Stage the planning package for approval before committing it.
```

```text
Use the harness, but treat this as a small mechanical edit if it qualifies.
```

```text
Preserve this handoff for a future thread before implementation.
```

```text
Create a plan-only PR checkpoint before code changes.
```

## Validation

For harness maintenance work, run the package validation command when practical:

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
