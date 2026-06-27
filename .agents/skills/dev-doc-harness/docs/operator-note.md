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
context, and model or sub-agent policy.

For substantial work, expect a work item package under:

```text
docs/work-items/<work-id>/
```

Small or medium work usually gets a spec and plan. Large or phased work gets an
anchor spec first. Phase plans come later from the approved anchor spec unless
you explicitly ask for combined planning.

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

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
```

The validator is a lightweight structural check. It supports review; it does
not replace operator approval or engineering judgment.
