# Phased Planning Orchestration Spec

Work ID: `2026-06-27-phased-planning-orchestration`
Short ID: `phased-planning-orchestration`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:freeze-gate`, `module:architecture`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:quality.spec-handoff`

## Goal

Make the harness steer large or phased work through an anchor-spec-first planning flow, with phase plans created only after the anchor spec is approved or explicitly handed off, and with curated-context sub-agent phase-plan drafting treated as the preferred orchestration when it fits the work and the platform supports it.

## Scope

- Clarify canonical lifecycle policy for large or phased work so the initial planning package contains the anchor spec and required supporting artifacts, not all concrete phase plans, unless the operator explicitly asks for combined planning.
- Clarify freeze-gate policy so the anchor-spec gate is a real stop before later phase-plan drafting.
- Clarify model and sub-agent policy so curated-artifact sub-agents are the preferred default for bounded phase-plan drafting after anchor-spec freeze when phases are independent enough and tools allow it.
- Update the large/phased spec and phase-plan templates so their prompts distinguish planned future phase-plan outputs from phase-plan files to create now.
- Update router and operator-facing documentation so agents and operators see the anchor-first flow without reading every canonical reference.
- Strengthen structural validation checks so current harness surfaces keep evidence for anchor-spec-only planning, post-anchor phase-plan drafting, and curated sub-agent planning.

## Non-scope

- Do not change the Planning Artifact Freeze Gate requirement that implementation starts only after a fresh operator response following approval freeze.
- Do not make sub-agents mandatory for every large or phased work item.
- Do not introduce a new artifact type beyond existing specs, plans, phase plans, amendments, snapshots, deltas, and variance logs.
- Do not rewrite frozen historical work-item artifacts to match the new wording.
- Do not add a heavy semantic validator for plan quality; validation stays structural and high-signal.

## Current state

The harness already says the anchor spec is the central handoff and that the initial planning session must preserve decisions before later sessions produce phase plans. The freeze gate also says to stop before the next planning stage. In practice, agents still tend to create the anchor spec plus every visible phase plan in one shot because:

- The large/phased layout lists concrete `plan-phase-*` filenames alongside the anchor spec.
- The large/phased spec template lists phase-plan output filenames without clearly marking them as future artifacts.
- The multi-gate policy allows phase-plan freeze after one or more phase plans, which is useful later but does not strongly separate the anchor-spec gate.
- The sub-agent policy prefers curated context but does not connect that preference to phase-plan drafting as the normal post-anchor orchestration.

## Proposed behavior

For large or phased work, the harness should make the normal sequence explicit:

1. Draft the anchor spec and any required supporting snapshots or deltas.
2. Stage the anchor-spec planning package for review.
3. Freeze the anchor spec only after explicit approval or handoff snapshot.
4. Stop before implementation and before phase-plan drafting.
5. After a fresh operator instruction, draft phase plans from the approved anchor spec, amendments, and prior phase outputs.
6. Prefer curated-artifact sub-agent phase-plan drafting when phases are independent enough, the task benefits from bounded context, and the platform supports it.
7. Use main-thread phase-plan drafting when sub-agents are unavailable, phases are tightly coupled, or coordination overhead is higher than the value.

The spec may still list planned phase-plan filenames in its phase decomposition. Those entries are planned future outputs, not permission to materialize the phase-plan files during the anchor-spec planning package unless the operator explicitly requests combined planning.

## Interfaces and data

No runtime product API, config, schema, persistence, CLI, or service interface changes.

The change affects repository process surfaces:

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/docs/operator-note.md`
- `README.md`
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`
- `CHANGELOG.md`

## Risks

- Over-tightening the rule could block legitimate combined spec-and-phase-plan planning when the operator explicitly wants it. Mitigation: allow combined planning only when explicitly requested and recorded.
- Making curated sub-agents the preferred default could be misread as a universal requirement. Mitigation: phrase it as preferred when supported and justified, with a recorded fallback to main-thread planning.
- Validation wording checks may become brittle. Mitigation: check durable phrases that correspond to policy commitments rather than exact paragraphs.
- Updating operator-facing summaries could duplicate canonical policy. Mitigation: keep summaries short and route detailed rules to canonical references.

## Acceptance criteria

- `artifact-contract.md` states that the normal initial large/phased planning package is anchor-spec-only and that listed phase-plan files are future outputs unless the operator explicitly requests combined planning.
- `planning-freeze-gates.md` states that anchor-spec freeze stops before phase-plan drafting as well as before implementation, and phase-plan drafting resumes only after fresh operator instruction.
- `subagent-model-policy.md` states that post-anchor phase-plan drafting should prefer curated-artifact sub-agents when justified and supported, with recorded fallback when not used.
- `large-phased-work-item-spec.md` tells agents not to create phase-plan files during the anchor-spec planning package unless the operator explicitly requests combined planning.
- `large-phased-work-item-phase-plan.md` keeps phase plans grounded in the approved anchor spec, amendments, prior phase outputs, and recorded context strategy.
- `SKILL.md`, `README.md`, and `docs/operator-note.md` surface the anchor-spec-first flow and curated-context phase-plan option without becoming the canonical rule owners.
- `Test-HarnessPolicy.ps1` contains structural evidence checks that would fail if current surfaces lose the anchor-spec-only and curated phase-plan orchestration guidance.
- The harness validation command passes after implementation.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `phased-planning-orchestration spec: clarify phased planning orchestration` | `2026-06-27-phased-planning-orchestration: clarify phased planning orchestration` | Approval commit for this spec and related planning artifacts. |
| Implementation | `phased-planning-orchestration docs: enforce anchor-spec-first phase planning` | `2026-06-27-phased-planning-orchestration: enforce anchor-spec-first phase planning` | Update canonical references, templates, operator docs, validation checks, and changelog. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries synchronized with the planned approval and implementation subjects |
| Test cases | Snapshot | No | Not applicable | `snapshots/test-cases.snapshot.md` | The existing validator is strengthened; no new frozen test-case snapshot is required for this bounded process change |
| Testing guide delta | Living delta | No | Not applicable | `deltas/testing-guide.delta.md` | The existing validation command remains the same |
| Operator manual delta | Living delta | No | Not applicable | `deltas/operator-manual.delta.md` | Operator-facing current docs are updated directly in `README.md` and package-local `docs/operator-note.md` |
| API reference delta | Living delta | No | Not applicable | `deltas/api-reference.delta.md` | No API surface changes |
| Architecture snapshot | Snapshot | No | Not applicable | `snapshots/architecture.snapshot.md` | This is a bounded policy clarification, not a new architecture decomposition |
| Architecture summary delta | Living delta | No | Not applicable | `deltas/architecture-summary.delta.md` | Current canonical references and operator docs carry the change |

## Approval

- Status: Approved
- Superseded by: None
