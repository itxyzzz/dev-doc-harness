# Dev Doc Harness

This repository contains a lightweight documentation harness for agent-assisted
development. Its job is to make the development process more inspectable,
reviewable, and durable from the operator's point of view.

The harness does not replace Superpowers, spec-kit, test-driven development, or
normal engineering judgment. It gives those workflows a repository-local
contract for where planning artifacts live, when planning freezes, and what must
be preserved for future agents or future threads.

```mermaid
%%{init: {
  "flowchart": {
    "curve": "basis",
    "nodeSpacing": 50,
    "rankSpacing": 70
  }
}}%%

flowchart TD
    A["Operator asks for work"]:::house --> B{"Task size?"}:::house
    B -->|Very small| C["Direct edit, check, commit"]:::house
    B -->|Substantial| D["Create work item folder"]:::house

    D --> E{"Planning shape?"}:::house
    E -->|Small or medium| F["Draft spec and plan"]:::house
    E -->|Large or phased| G["Anchor spec, then phase plans"]:::house

    F --> H["Stage draft planning package"]:::house
    G --> H

    H --> I{"Operator approves?"}:::house
    I -->|Yes| J["Freeze gate: changelog, commit, pause"]:::house

    I -.->|Feedback| R["Revise draft planning package"]:::house
    R -.->|Resubmit| H

    J --> O["Optional plan-only PR"]:::house
    O --> P["Confirm settings and start"]:::house
    P --> Q["Implement approved plan"]:::house
    Q --> K{"High-impact variance?"}:::house

    K -->|No| L["Validate, update docs and changelog"]:::house
    L --> M["Commit implementation"]:::house

    K -->|Yes| N["Plan amendment and approval"]:::house
    N -.-> H

    classDef house fill:#242429,stroke:#71717a,stroke-width:1.5px,color:#fafafa
    linkStyle default stroke:#a1a1aa,stroke-width:1.75px
```

## What changes for operators

With this harness installed, substantial development work becomes more explicit
before code changes begin.

For very small mechanical edits, little changes. The agent can usually make the
edit directly, preserve behavior, and run the relevant checks.

For small or medium substantial work, expect the agent to create a work item
package under `docs/work-items/<work-id>/`. This applies to features, bug fixes with
nontrivial investigation, prior issue investigations that turn into changes,
refactors, migrations, and documentation/process changes. That folder captures
the spec, plan, required documentation updates, and any implementation variance.
The operator gets a stable place to review what is about to happen before the
agent starts changing the product.

The work item folder keeps the full dated ID for sorting and uniqueness, while
the durable artifact filenames include a shorter suffix for easier chat
references. For example, `2026-05-31-artifact-root` uses
`spec-artifact-root.md` and `plan-artifact-root.md`.

For large work, expect a more deliberate handoff. The agent first writes an
anchor `spec-<short-id>.md` that preserves goals, boundaries, decisions, risks,
tests, and acceptance criteria. Then it writes phase plans such as
`plan-phase-01-discovery-<short-id>.md` that a fresh agent or future thread can
execute without relying on hidden chat history.

When durable planning artifacts are ready for review, the agent stages the draft
planning package without committing it and asks the operator for approval or
feedback. Feedback before approval edits the draft artifacts directly; it does
not require an amendment. When the operator explicitly approves, the harness
runs the freeze gate: the agent updates the changelog, commits only the approved
planning artifacts and changelog, reports the commit hash and artifact paths,
and stops before implementation. The next operator response can confirm the
model, reasoning-effort, and sub-agent choices and authorize implementation in
one step, such as `Confirm, proceed`, when the agent's post-freeze prompt asks
for both. This gives the operator a clean review point, including the option to
push a planning-only draft PR before any product code changes.

Sub-agent use is a planning judgment, not a keyword the operator must repeat on
every request. For substantial work, the agent should decide whether sub-agents
are justified and record either a bounded strategy or a brief reason for using
none. Once the plan is approved and implementation is authorized after the
freeze gate, the approved sub-agent strategy can be used without another
sub-agent-specific confirmation. The normal guardrail is no more than three
concurrent sub-agents; long-running work can still use more than three total
sub-agents in separate waves when the approved plan supports that shape. At the
end, the agent reports the de-facto sub-agent use and the model, model class, or
profile actually used when that information is available.

During implementation, the agent should not quietly rewrite frozen plans to make
reality look tidier. If the work deviates in a meaningful way, the variance is
recorded. If the post-freeze deviation affects architecture, APIs, data,
security, scope, acceptance criteria, or feasibility, the agent must stop for an
amendment and operator approval.

Before commits, the agent updates `CHANGELOG.md` with newest-first entries tied
to the current work item, phase, task, or planning decision.

## Operator outcomes

The main benefit is control without constant micromanagement. You get clear
pause points, durable artifacts, and a written trail of what changed and why.

The harness is designed to produce these outcomes:

- Less lost context between planning, implementation, review, and later threads.
- Fewer surprise implementation turns after a planning discussion.
- Cleaner handoffs to fresh agents, reviewers, or future maintainers.
- More useful PRs, including plan-only PRs before expensive implementation.
- Explicit model, reasoning-effort, and justified sub-agent choices for substantial work.
- De-facto reporting of sub-agent count, roles, concurrency or waves, and observed model details when available.
- A visible record of plan variance instead of silent drift.
- Documentation updates that are tied to the work instead of remembered later.
- A compact audit trail for decisions, tests, acceptance criteria, and risks.

## How to use it

Agents discover this harness through `AGENTS.md`, then load:

```text
.agents/skills/dev-doc-harness/SKILL.md
```

There is not an installation script yet. After checking out this repository, use
the harness in either of these ways:

- Copy `AGENTS.md` and the `.agents/` folder into the repository where you want
  to use the harness. If the destination repository already has an `AGENTS.md`,
  merge or append the harness instructions instead of replacing the file.
- Install it globally. Codex can do this for you, or you can manually copy the
  contents of `.agents/skills/dev-doc-harness/` into
  `$HOME\.agents\skills\dev-doc-harness`.

To make sure the skill is reliably discovered and followed, you can also append
instructions like this to your global `AGENTS.md`:

```md
## Harness activation

**For any repository development work, apply `dev-doc-harness` before implementation.** Use the harness selected by normal precedence: repository-local harness instructions when present, otherwise the installed global `dev-doc-harness`.

Development work includes features, bug fixes, refactors, migrations, tests, documentation/process changes, investigations that may lead to repository changes, and review or handoff work.

Only a **very small mechanical edit** may skip durable harness artifacts. Before editing, the agent must explicitly state that the work is a very small mechanical edit and why. If uncertain, default to using the harness.

Before editing implementation-target files, complete the harness planning step. Implementation-target files include source code, tests, migrations, runtime configuration, project documentation, product documentation, scripts, and process docs. The only repository files that may be created or edited before the freeze gate are the required harness planning artifacts and the `CHANGELOG.md` entry required by the gate.

Core flow:

1. Size the work item using the harness sizing rules.
2. For anything beyond a very small mechanical edit, create or update the durable planning artifacts required by the harness.
3. Treat planning artifacts as drafts until operator approval or explicit handoff.
4. When durable planning artifacts are finalized, run the Planning Artifact Freeze Gate.
5. Stop after the freeze gate. Do not begin implementation, task execution, or the next planning stage.
6. Begin implementation only after a fresh explicit operator instruction given after the freeze gate.

The Planning Artifact Freeze Gate requires: update `CHANGELOG.md`; verify finalized artifacts have no placeholders, unresolved decisions, or missing required sections; stage and commit only the finalized planning artifacts and `CHANGELOG.md`; report the commit hash and finalized artifact paths; remind the operator they may push and create a draft plan-only PR; and ask the operator to confirm model, reasoning-effort, and sub-agent policy choices and whether implementation should begin now. After the operator authorizes implementation, the approved sub-agent strategy may be used without a separate sub-agent-specific confirmation. More than three concurrent sub-agents, unplanned sub-agents, unrecorded model or reasoning escalation, write-scope escalation, and platform-restricted actions still require fresh confirmation.

Treat `dev-doc-harness` as the canonical source for repository documentation and artifact lifecycle: work sizing, spec and plan layout, durable handoff quality, planning freeze gates, documentation matrices, variance logs, plan amendments, changelog requirements, model and sub-agent policy, and final integration ownership.

## Scope and precedence

User instructions, repository-local `AGENTS.md` files, and project-specific harness adapters override this global override when they are stricter or more specific.

If a repository provides its own `.agents/skills/dev-doc-harness/SKILL.md`, use that repo-local harness for that repository. Otherwise, use the installed global `dev-doc-harness` skill.

If a repository has no harness-specific instructions, apply the installed skill as the default artifact and documentation contract for substantial development work.

## Superpowers compatibility

When Superpowers is installed and active, use Superpowers for its normal software-development methodology: brainstorming, planning, TDD, execution, review, and finishing.

Use `dev-doc-harness` alongside Superpowers only for the repository artifact contract: where durable planning artifacts live, when planning freezes, how variance is recorded, and which model or sub-agent policy applies.

Do not duplicate Superpowers process rules in this file, and do not duplicate harness process rules in Superpowers artifacts. If Superpowers produces specs or plans outside the harness location, convert or copy the approved content into the harness work item folder before implementation, following the skill.
```

Operators usually do not need to invoke the internals by hand. Ask for the work
you want, and the agent should classify the size of the task and apply the
harness when it is needed.

Useful operator prompts include:

```text
Plan this as a large bug fix and stop after the freeze gate.
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

## What is inside

The internal machinery is intentionally small:

- `AGENTS.md` tells agents when to use the harness.
- `.agents/skills/dev-doc-harness/SKILL.md` is the entry point.
- `references/artifact-contract.md` defines work item folders, short-ID
  artifact filenames, snapshots, deltas, changelog rules, and variance
  handling.
- `references/planning-freeze-gates.md` defines the approval-first planning
  workflow.
- `references/durable-planning-quality.md` defines the quality bar for durable
  specs and phase plans.
- `references/subagent-model-policy.md` defines the active sub-agent and model
  policy. This repository currently uses `economy-default`.
- `assets/templates/` contains the reusable spec, plan, amendment, and variance
  templates.

Read those documents for the full contract. The README is only the operator
overview.

## What this is not

This harness is not a project management system, a replacement for human review,
or a demand that every typo fix gets a spec folder. It is a process guardrail for
work where planning quality, reviewability, future handoff, or implementation
drift matters.

Its best use is to make agentic development feel less like a disappearing chat
transcript and more like a controlled engineering workflow with clear checkpoints
and reusable artifacts.

## Contributing

Planning artifacts for this harness repository's own development are local
working notes, not distributable project content. Keep them under
`docs/work-items/`, which is ignored by git in this repository.

Contributions should commit the harness changes themselves, any user-facing
documentation updates, and the relevant `CHANGELOG.md` entry, but not local
planning packages for this repo's development.
