# Dev Doc Harness

This repository contains a lightweight documentation harness for agent-assisted
development. Its job is to make the development process more inspectable,
reviewable, and durable from the operator's point of view.

The harness does not replace Superpowers, spec-kit, test-driven development, or
normal engineering judgment. It gives those workflows a repository-local
contract for where planning artifacts live, when planning freezes, and what must
be preserved for future agents or future threads.

The current harness is organized around a small ownership map. `AGENTS.md`
bootstraps the harness and selects repository-specific defaults,
`.agents/skills/dev-doc-harness/SKILL.md` routes common operations, canonical
references own reusable policy, templates own artifact shape, and this README is
only the operator-facing overview.

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
feedback. Explicit approval runs the freeze gate: changelog, approval commit,
reported artifact paths, and a pause before implementation. The next operator
response can confirm execution settings and authorize implementation in one
step, giving the operator a clean plan-only review point before product changes.

Sub-agent use is a planning judgment, not a keyword the operator must repeat on
every request. For substantial work, the agent records either a bounded strategy
or a reason for using none, then reports de-facto use at completion when
sub-agents were authorized or used. The active repository policy is selected in
`AGENTS.md`; detailed model, reasoning, context-strategy, and authorization
rules live in `references/subagent-model-policy.md`.

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
- Explicit model, reasoning-effort, context strategy, and justified sub-agent choices for substantial work.
- De-facto reporting of sub-agent count, roles, concurrency or waves, context strategy, inheritance behavior, and observed model details when available.
- A visible record of plan variance instead of silent drift.
- Documentation updates that are tied to the work instead of remembered later.
- A compact audit trail for decisions, tests, acceptance criteria, and risks.

## How to use it

Agents discover this harness through `AGENTS.md`, then load the operation
router:

```text
.agents/skills/dev-doc-harness/SKILL.md
```

The router sends each operation to the minimum useful owner modules:

| Need | Route |
|---|---|
| Work sizing and artifact lifecycle | `module:lifecycle` in `references/artifact-contract.md` |
| Planning review and freeze checkpoints | `module:freeze-gate` in `references/planning-freeze-gates.md` |
| Durable spec and phase-plan quality | `module:quality` in `references/durable-planning-quality.md` |
| Model and sub-agent strategy | `module:models` in `references/subagent-model-policy.md` |
| Router, ownership map, and rule IDs | `module:architecture` in `references/policy-architecture.md` |
| Execution-time quality checks | `module:execution-quality` in `references/context-and-quality-gates.md` |

There is not an installation script yet. After checking out this repository, use
the harness in either of these ways:

- Copy `AGENTS.md` and the `.agents/` folder into the repository where you want
  to use the harness. If the destination repository already has an `AGENTS.md`,
  merge or append the harness instructions instead of replacing the file.
- Install it globally. Codex can do this for you, or you can manually copy the
  contents of `.agents/skills/dev-doc-harness/` into
  `$HOME\.agents\skills\dev-doc-harness`.

To make sure the skill is reliably discovered and followed, you can also append
compact bootstrap instructions like this to your global `AGENTS.md`:

```md
## Harness activation

**For any repository development work, apply `dev-doc-harness` before implementation.** Use the harness selected by normal precedence: repository-local harness instructions when present, otherwise the installed global `dev-doc-harness`.

For substantial development work, use the selected harness entrypoint as the operation router. The router owns which canonical references, templates, and work-item artifacts to load for work sizing, planning, freeze gates, implementation, variance, changelog, compatibility, and model/sub-agent notation.

Only a **very small mechanical edit** may skip durable harness artifacts when the routed lifecycle sizing rules allow it. If uncertain, default to using the harness.

Before editing implementation-target files for substantial work, complete the harness planning and freeze flow. After the freeze gate, begin implementation only after a fresh explicit operator instruction.

Treat `dev-doc-harness` as the canonical source for repository artifact location and lifecycle. README summaries and templates do not override canonical harness references.

When Superpowers or spec-kit is active, use those tools for their normal methodology, but keep the harness as the artifact-location and lifecycle contract.
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

- `AGENTS.md` bootstraps the harness and selects repository-specific defaults.
- `.agents/skills/dev-doc-harness/SKILL.md` is the operation router.
- `references/policy-architecture.md` defines the module catalog, rule ID
  conventions, content types, dependency direction, router inputs, and
  rule-versioning status.
- `references/artifact-contract.md` defines work item folders, short-ID
  artifact filenames, snapshots, deltas, changelog rules, and variance
  handling.
- `references/planning-freeze-gates.md` defines the approval-first planning
  workflow.
- `references/durable-planning-quality.md` defines the quality bar for durable
  specs and phase plans.
- `references/subagent-model-policy.md` defines the available sub-agent and
  model policies. The active repository policy is selected in `AGENTS.md`.
- `assets/templates/` contains the reusable spec, plan, amendment, and variance
  templates. Templates own artifact shape and prompts, not reusable policy.

Read the routed owner documents for the full contract. The README is only the
operator overview and does not override canonical references.

## What this is not

This harness is not a project management system, a replacement for human review,
or a demand that every typo fix gets a spec folder. It is a process guardrail for
work where planning quality, reviewability, future handoff, or implementation
drift matters.

Its best use is to make agentic development feel less like a disappearing chat
transcript and more like a controlled engineering workflow with clear checkpoints
and reusable artifacts.

## Contributing

Planning artifacts for this harness repository's own development are usually
local working notes, not distributable project content. Keep them under
`docs/work-items/`, which is ignored by git in this repository, unless an
approved plan explicitly tracks a work-item package as a repository artifact.

Contributions should commit the harness changes themselves, any user-facing
documentation updates, and the relevant `CHANGELOG.md` entry, but not ordinary
local planning packages for this repo's development.
