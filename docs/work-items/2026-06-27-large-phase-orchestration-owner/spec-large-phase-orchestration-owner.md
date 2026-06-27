# Large Phase Orchestration Owner Spec

Work ID: `2026-06-27-large-phase-orchestration-owner`
Short ID: `large-phase-orchestration-owner`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:architecture`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:quality.spec-handoff`

## Goal

Make the harness architecture identify one canonical owner for the ordering of large/phased planning, so future changes to anchor-spec-first sequencing have a clear home without turning artifact shape, freeze mechanics, or model policy into competing orchestration sources.

## Scope

- Add a dedicated lifecycle rule for large/phased planning orchestration, including the normal state sequence from anchor-spec draft through phase-plan drafting and implementation authorization.
- Keep artifact shape in lifecycle, freeze mechanics in freeze-gate, and sub-agent/model choices in model policy.
- Update architecture catalog and router/template references so agents can discover the orchestration owner.
- Update structural validation so current surfaces retain the new orchestration owner and references.
- Update `CHANGELOG.md` before the implementation commit.

## Non-scope

- Do not create a new canonical module unless implementation proves section-level lifecycle ownership is insufficient.
- Do not split `artifact-contract.md`.
- Do not change the anchor-spec-first behavior implemented by `2026-06-27-phased-planning-orchestration`.
- Do not rewrite frozen historical work-item artifacts.
- Do not add a semantic parser for plan quality.

## Current state

The harness now says large/phased work starts with an anchor-spec-only package, pauses at anchor freeze, and resumes phase-plan drafting only after fresh operator instruction. That behavior is correct, but the ordering invariant is spread across lifecycle layout text, freeze-gate multi-gate wording, model-policy sub-agent guidance, templates, and router summaries.

The modular architecture already has the right dependency direction: `module:lifecycle` owns work item lifecycle, `module:freeze-gate` owns approval mechanics, `module:models` owns delegation and model selection, and `module:architecture` names owners and routes. What is missing is a named lifecycle rule that owns the large/phased planning state machine as distinct from file layout and spec quality.

## Proposed behavior

Add a lifecycle rule such as `rule:lifecycle.large-phase-orchestration` under a new section in `artifact-contract.md`, for example `## Large or phased planning orchestration`.

That section should own the state sequence:

1. Anchor spec draft.
2. Anchor spec draft review.
3. Anchor spec freeze or explicit handoff snapshot.
4. Stop before implementation and before phase-plan drafting.
5. Post-anchor phase-plan drafting after fresh operator instruction.
6. Phase-plan freeze.
7. Implementation after post-phase-plan authorization.
8. Amendment gate for high-impact changes.

`planning-freeze-gates.md` should continue to own the approval checkpoint mechanics, but cite the lifecycle orchestration rule for the sequencing invariant. `subagent-model-policy.md` should continue to own curated-artifact sub-agent guidance, but cite lifecycle for phase order. Templates and `SKILL.md` should cite the new lifecycle rule where they describe large anchor specs or phase plans.

## Interfaces and data

No runtime APIs, product config, schemas, persistence, CLI flags, or service interfaces change.

Affected process surfaces are expected to include:

- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`
- `CHANGELOG.md`

README and operator-note changes are optional and should be avoided unless the implementation changes operator-visible behavior. The expected change is architecture ownership, not behavior.

## Risks

- Adding a new rule could duplicate existing lifecycle wording instead of clarifying ownership. Mitigation: keep the new section compact and move or reference sequence wording rather than repeating long policy blocks.
- Cross-references could increase routine route load. Mitigation: keep normal routes within the current route budget and avoid adding a new module.
- Validation checks could become brittle. Mitigation: check stable owner IDs and high-signal phrases, not full paragraphs.

## Acceptance criteria

- `artifact-contract.md` owns a new lifecycle rule for large/phased planning orchestration and names the canonical state sequence.
- `policy-architecture.md` includes the new rule family in the lifecycle module description or related architecture guidance.
- `planning-freeze-gates.md` cites lifecycle orchestration for ordering while preserving freeze-gate ownership of approval mechanics.
- `subagent-model-policy.md` cites lifecycle orchestration for phase order while preserving model-policy ownership of curated-artifact sub-agent strategy.
- `SKILL.md` and large/phased templates cite the new lifecycle orchestration rule where they route or prompt anchor-spec and phase-plan work.
- `Test-HarnessPolicy.ps1` would fail if current surfaces lose the new orchestration owner or its key route/template references.
- Harness validation passes after implementation.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `large-phase-orchestration-owner spec: define large phase orchestration owner` | `2026-06-27-large-phase-orchestration-owner: define large phase orchestration owner` | Approval commit for this spec and plan. |
| Implementation | `large-phase-orchestration-owner docs: add large phase orchestration owner` | `2026-06-27-large-phase-orchestration-owner: add large phase orchestration owner` | Add lifecycle rule owner, align references/templates/router, strengthen validation, and update changelog. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries synchronized with the planned approval and implementation subjects |
| Test cases | Snapshot | No | Not applicable | `snapshots/test-cases.snapshot.md` | Existing structural validator is strengthened instead of adding a new frozen scenario snapshot |
| Testing guide delta | Living delta | No | Not applicable | `deltas/testing-guide.delta.md` | Validation command remains the same |
| Operator manual delta | Living delta | No | Not applicable | `deltas/operator-manual.delta.md` | No operator-visible flow change expected |
| API reference delta | Living delta | No | Not applicable | `deltas/api-reference.delta.md` | No API surface changes |
| Architecture snapshot | Snapshot | No | Not applicable | `snapshots/architecture.snapshot.md` | Current architecture reference carries the ownership refinement |
| Architecture summary delta | Living delta | No | Not applicable | `deltas/architecture-summary.delta.md` | No long-lived external architecture document is changed |

## Approval

- Status: Approved
- Superseded by: None
