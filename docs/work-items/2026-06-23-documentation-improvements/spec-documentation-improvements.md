# Documentation Improvements Spec

Work ID: `2026-06-23-documentation-improvements`
Short ID: `documentation-improvements`
Status: Approved
Harness release: `0.3.0`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:quality.spec-handoff`

## Goal

Improve the documentation surfaces for readers and adopters without changing the harness lifecycle contract. The work should make the repository easier to understand as a portfolio project, make the copyable package more self-explanatory when root repository docs are not copied, clarify how validator checks should evolve, and make `TODO.md` easier to triage.

## Scope

- Add a short portfolio-oriented summary near the top of root `README.md` for non-operator readers.
- Add a compact package-local operator note inside `.agents/skills/dev-doc-harness/` so adopters who copy only root `AGENTS.md` plus `.agents/` get a strong usage explanation.
- Clarify the validator evolution boundary in the canonical architecture or validation guidance so validation remains lightweight structural checking rather than a heavy semantic parser.
- Revise root `TODO.md` into a cleaner, common format with priority suggestions and the follow-up items from the current documentation review conversation.
- Preserve current license handling as out of scope because the license is already handled on the relevant branch context and should not be duplicated here.

## Non-scope

- No license changes.
- No CI, pre-commit, portable validator, demo repository, examples directory, or validation-failure tracking implementation in this work item.
- No changes to harness lifecycle, freeze-gate semantics, model/sub-agent policy, release identity, package boundary, or work-item artifact schemas beyond documentation wording needed for this scope.
- No rewrite of frozen historical work-item artifacts.

## Current state

Root `README.md` is operator-oriented and explains the harness flow, outcomes, usage, and package boundary. It does not yet open with a compact portfolio-style project summary for readers who are evaluating the repository before deciding whether to adopt the harness.

The distributable package boundary is root `AGENTS.md` plus `.agents/`. Root `README.md`, `CHANGELOG.md`, `TODO.md`, and `docs/work-items/` are excluded from downstream copies. Because of that boundary, adopters who copy only the distributable package may not receive the most helpful operator-facing explanation unless they inspect the package-local references.

The validator is implemented as `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`. The architecture reference describes graph and structure validation, route budgets, duplicate-block validation, and lifecycle decomposition direction. It does not yet state a concise boundary for future validator evolution that guards against turning validation into a heavyweight parser.

Root `TODO.md` contains useful future work, including fake large-work trials, portable validator ideas, CI/pre-commit deferrals, examples, PR workflow, governance, and adapters. It is currently a mix of headings, nested bullets, deferred items, and priority hints, which makes it harder to scan and maintain.

## Proposed behavior

After implementation:

- `README.md` opens with a brief project summary that works for portfolio or non-operator readers while keeping the existing operator-focused overview intact.
- A package-local operator note exists under `.agents/skills/dev-doc-harness/` and summarizes the practical adoption workflow, pause points, freeze behavior, and where canonical policy lives. It should be explicitly summary-level, not a competing normative source.
- The validator evolution boundary is explicit: checks should remain structural, graph-oriented, and high-signal; semantic quality review belongs in human/operator review, specs/plans, or focused tests rather than parser-like policy interpretation.
- `TODO.md` uses a common, maintainable format with priority labels or sections, consistent item structure, and clear treatment of newly discussed items: package-local note, portfolio README summary, validator boundary clarification, CI/pre-commit, disposable large-work trial, examples, validation-failure tracking, validator split, and portable validator.

## Interfaces and data

No public APIs, schemas, CLI flags, persistence, or runtime interfaces change.

Files expected to change during implementation:

- `README.md`
- `TODO.md`
- `.agents/skills/dev-doc-harness/docs/operator-note.md` or a similarly named package-local note file
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- Possibly `.agents/skills/dev-doc-harness/SKILL.md` or package-local release/adoption docs only if a short pointer to the operator note is needed for discoverability
- `CHANGELOG.md`

## Risks

- Duplicating canonical policy prose in README, TODO, or the package-local note could create a second source of truth.
- Making TODO too elaborate could turn a cleanup into process overhead.
- The package-local operator note could be mistaken for normative policy unless it clearly points back to canonical references.
- Validator-boundary wording could accidentally weaken useful validation if it is phrased as a prohibition on future checks instead of a guardrail against heavy semantic parsing.

## Acceptance criteria

- `README.md` includes a concise portfolio-oriented summary before or near the current operator-focused introduction.
- A package-local operator note is added inside `.agents/skills/dev-doc-harness/`, is included by the distributable package boundary, and explains adoption and operation without overriding canonical references.
- The validator evolution boundary is clarified in the appropriate canonical validation or architecture guidance.
- `TODO.md` is reorganized into a consistent format with priority suggestions and includes the documentation-review follow-up items from this conversation.
- Existing package boundary guidance remains accurate: downstream adopters copy root `AGENTS.md` plus `.agents/`, not this repository's `docs/work-items/`.
- Harness validation passes after implementation.
- No license changes are made in this work item.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `documentation-improvements spec: document planned documentation updates` | `2026-06-23-documentation-improvements: document planned documentation updates` | Approval commit for this spec and related planning artifact. |
| Implementation | `documentation-improvements docs: improve harness documentation surfaces` | `2026-06-23-documentation-improvements: improve harness documentation surfaces` | Expected implementation commit for README, package-local note, validator-boundary wording, TODO cleanup, validation evidence, and changelog. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required before approval and implementation commits; title snippets synchronized with planned commit subjects. |
| Test cases | Snapshot | No | Not applicable | snapshots/test-cases.snapshot.md | No behavior or test matrix changes; validation commands in the plan are sufficient. |
| Testing guide delta | Living delta | No | Not applicable | deltas/testing-guide.delta.md | No testing guide behavior changes in this documentation-only scope. |
| Operator manual delta | Living delta | No | Not applicable | deltas/operator-manual.delta.md | The package-local operator note itself is the operator-facing output. |
| API reference delta | Living delta | No | Not applicable | deltas/api-reference.delta.md | No public API changes. |
| Architecture snapshot | Snapshot | No | Not applicable | snapshots/architecture.snapshot.md | Validator-boundary wording is a current canonical documentation clarification, not a new architecture decision needing a frozen snapshot. |
| Architecture summary delta | Living delta | No | Not applicable | deltas/architecture-summary.delta.md | No separate long-lived architecture summary exists beyond the canonical architecture reference being edited. |

## Approval

- Status: Approved
- Superseded by: not applicable
