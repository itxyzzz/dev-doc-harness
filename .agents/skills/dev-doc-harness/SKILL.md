---
name: dev-doc-harness
description: Use for repository development work except very small mechanical edits.
---

# Dev Doc Harness

This skill is the repository-local entrypoint and operation router for the documentation harness. It routes agents to canonical policy modules, templates, supplemental references, and current work-item artifacts without making every task load every reference.

For the canonical module catalog, rule ID conventions, dependency direction, content types, and release compatibility routing, use `references/policy-architecture.md` (`module:architecture`). For release identity, package boundary, release notes, changelog source, compatibility, artifact release context, and team adoption, use `references/release-policy.md` (`module:release`). When an artifact or template needs the current harness release value, read the package-local marker at `.agents/skills/dev-doc-harness/VERSION` (this skill directory's `VERSION` file) before falling back to `unknown`.

## When to invoke

Use this skill for all repository development work except very small mechanical edits. Classify work size through `module:lifecycle` in `references/artifact-contract.md`, especially `rule:lifecycle.work-sizing`.

Very small mechanical edits may skip this harness when the operator has not requested durable planning.

## Operation router

Load by operation. Include the current operator instruction, applicable `AGENTS.md` files, and active work-item artifacts before following a route.

| Operation family | Required route | Optional or conditional route | Required outcomes |
|---|---|---|---|
| Classify work size | `references/artifact-contract.md` (`module:lifecycle`, `rule:lifecycle.work-sizing`) | None | Very small mechanical skip stays explicit and narrow; substantial work uses harness artifacts. |
| Draft or review small/medium specs and plans | `module:lifecycle`, `module:quality`, `module:models`, small/medium templates in `assets/templates/` | None | Work item folder, short artifact ID, documentation matrix, validation commands, model/sub-agent strategy, and draft review state are recorded. |
| Draft or review large anchor specs | `module:lifecycle`, `module:quality`, `module:models`, `assets/templates/large-phased-work-item-spec.md` | Prior approved amendments when present | Anchor spec preserves handoff decisions and phase decomposition under `rule:lifecycle.large-anchor-spec`. |
| Draft or review phase plans | Approved spec, amendments, prior phase outputs, `module:quality`, `module:lifecycle`, `module:models`, `assets/templates/large-phased-work-item-phase-plan.md` | `module:architecture` when phase scope changes router or ownership behavior | Phase plan is fresh-thread executable under `rule:quality.phase-plan-fresh-thread` and does not reinterpret frozen decisions. |
| Freeze planning packages | `references/planning-freeze-gates.md` (`module:freeze-gate`), `module:lifecycle` | Current work-item artifacts | Use `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.changelog-before-commit`, and `rule:lifecycle.immutable-snapshots`. |
| Execute approved work and record variance | Approved artifacts, `module:lifecycle`, `module:execution-quality` | Phase validation commands and relevant project docs or tests | Stay in approved scope, update `CHANGELOG.md` before commits, use planned commit subjects, and use `rule:lifecycle.variance-policy` for drift. |
| Release, package, or team adoption work | `references/release-policy.md` (`module:release`) | `module:architecture` when module ownership changes; `module:lifecycle` when changelog or work-item artifacts change | Preserve the package boundary, release-note source contract, release compatibility model, artifact release context, and minimal adoption/rollback flow. |
| Use or review sub-agent strategy | `references/subagent-model-policy.md` (`module:models`, `rule:models.strategy-required`) | `references/subagent-role-examples.md` (`module:role-examples`) when examples help | Record the active repository policy, context strategy, authorization boundary, and de-facto use when applicable. |
| Evidence-heavy review or reports | `references/evidence-and-report-artifacts.md` (`module:evidence`) | Current plan or operator-specified evidence sources | Preserve evidence and stop when evidence rules require review before continuing. |
| Validate current harness surfaces | `module:execution-quality`, `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | `module:architecture` when rule, route, or ownership drift is inspected | Run the lightweight validation command before commits that change current harness entrypoints, references, templates, README, or validation artifacts. |
| Update templates or router guidance | `module:architecture` plus the canonical owner for each referenced rule family | Affected templates | Templates own schema and prompts, not long reusable policy. |
| Superpowers or spec-kit compatibility | Applicable `AGENTS.md`, `module:lifecycle`, this skill's compatibility notes, and relevant external workflow instructions | `module:execution-quality` when environment compensation matters | The harness owns artifact location, freeze gates, variance records, commit-message and changelog discipline, and model/sub-agent notation. |

Use these supplemental references when relevant:

- `references/context-and-quality-gates.md` (`module:execution-quality`) for context load order, task preflight, environment compensation, and increment quality gates.
- `references/subagent-role-examples.md` (`module:role-examples`) for compact policy-relative role examples.
- `references/evidence-and-report-artifacts.md` (`module:evidence`) for spikes, investigations, agent reports, or review evidence.

## Workflow

1. Classify the work as small/mechanical, small/medium work item, or large/phased work item through the router.
2. Choose a work ID using `YYYY-MM-DD-short-kebab-title`, or `YYYY-MM-DD-ISSUE-short-kebab-title` when a JIRA key or other issue-tracker ID is available.
3. Create or update the work item folder under `docs/work-items/<work-id>/`.
4. Draft the required artifacts using `assets/templates/` and the routed canonical modules.
5. Keep draft artifacts editable until explicit approval, approval commit, or explicit handoff.
6. Run the Planning Artifact Freeze Gate before implementation or later planning continues.
7. During implementation, use approved artifacts plus routed execution references, record justified variance, and update `CHANGELOG.md` before every commit.

## Planning Artifact Freeze Gate

When durable planning artifacts are ready for review, approval, handoff, or freeze, follow `module:freeze-gate` in `references/planning-freeze-gates.md`. It owns `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

## Superpowers compatibility

When Superpowers is installed and active, use it for its normal development methodology. This harness still owns artifact location, planning freeze gates, variance records, commit-message and changelog discipline, and model/sub-agent policy notation. The lifecycle owner is `module:lifecycle`, especially `rule:lifecycle.superpowers-compatibility`.

## spec-kit compatibility

If spec-kit is installed and active, prefer a project-local adapter that points back to this skill and `module:lifecycle`. Do not make spec-kit templates the canonical source of harness rules.

## Completion checklist

- The work item folder follows `docs/work-items/<work-id>/`.
- Top-level durable artifact filenames include the short ID suffix, such as `spec-<short-id>.md` and `plan-<short-id>.md`.
- Required small/medium or large/phased artifacts exist and meet `module:quality`.
- Each approved or handed-off spec, plan, phase plan, or amendment has passed `module:freeze-gate`.
- The documentation artifact matrix uses `rule:lifecycle.documentation-matrix`.
- Commit subjects follow `rule:lifecycle.commit-message-format`, and `CHANGELOG.md` is updated before commits under `rule:lifecycle.changelog-before-commit`.
- Frozen snapshots follow `rule:lifecycle.immutable-snapshots`.
- Variance follows `rule:lifecycle.variance-policy`.
- Plans include validation commands and expected outputs.
- Sub-agent use, if any, follows the active repository policy notation from `module:models`.
