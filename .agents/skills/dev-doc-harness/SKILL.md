---
name: dev-doc-harness
description: Use for repository development work except very small mechanical edits.
---

# Dev Doc Harness

This skill is the repository-local entrypoint and operation router for the documentation harness. It routes agents to canonical policy modules, templates, supplemental references, and current work-item artifacts without making every task load every reference.

For the canonical module catalog, rule ID conventions, dependency direction, content types, and release compatibility routing, use `references/policy-architecture.md` (`module:architecture`). For naming grammar across work IDs, artifact filenames, commit messages, changelog source fragments, and changelog entries, use `references/naming-conventions.md` (`module:naming`). For artifact readability, final artifact content, scannable structure, placeholder control, and template prompt style, use `references/artifact-style.md` (`module:artifact-style`) when the route requires it or when readability risk is material. For Dev Doc Harness distribution release identity, package boundary, release notes, changelog source, compatibility, artifact release context, and team adoption, use `references/release-policy.md` (`module:release`). When an artifact or template needs the current harness release value, read the package-local marker at `.agents/skills/dev-doc-harness/VERSION` (this skill directory's `VERSION` file) before falling back to `unknown`.

For a compact package-local orientation that travels with copied harness packages, see `docs/operator-note.md`. It is an operator-facing summary and does not override this router or the canonical references.

## When to invoke

Use this skill for all repository development work except very small mechanical edits. Classify work size through `module:lifecycle` in `references/artifact-contract.md`, especially `rule:lifecycle.work-sizing`.

Very small mechanical edits may skip this harness when the operator has not requested durable planning.

## Operation router

Load by operation. Include the current operator instruction, applicable `AGENTS.md` files, and active work-item artifacts before following a route.

| Operation family | Required route | Optional or conditional route | Required outcomes |
|---|---|---|---|
| Classify work size | `references/artifact-contract.md` (`module:lifecycle`, `rule:lifecycle.work-sizing`) | None | Very small mechanical skip stays explicit and narrow; substantial work uses harness artifacts. |
| Draft or review small/medium specs and plans | `module:lifecycle`, `module:quality`, `module:models`, `module:artifact-style`, small/medium templates in `assets/templates/` | `module:naming` for work IDs or planned subjects; `assets/templates/architecture-snapshot.md` when useful | Record the work item, stable IDs, useful local links or a justified mapping, checks, documentation, execution strategy, and the upcoming-stage sub-agent assessment. |
| Draft or review large anchor specs | `module:lifecycle`, `module:quality`, `module:models`, `module:artifact-style`, `assets/templates/large-phased-work-item-spec.md` | `module:naming` for work IDs or planned subjects; prior approved amendments when present; `assets/templates/architecture-snapshot.md` when architecture decisions need a dedicated snapshot | Anchor spec preserves handoff decisions, work-item architecture snapshot status, phase decomposition, scannable large-document structure, and the upcoming-stage sub-agent assessment under `rule:lifecycle.large-anchor-spec`; `rule:lifecycle.large-phase-orchestration` makes the normal output an anchor-spec-only draft review state unless combined planning was explicitly requested. |
| Draft or review phase plans | Approved spec, amendments, prior phase outputs, recorded model/context strategy, architecture snapshot when present, `module:quality`, `module:lifecycle`, `module:models`, `assets/templates/large-phased-work-item-phase-plan.md` | `module:artifact-style` when the phase artifact becomes large or hard to scan; `module:architecture` when phase scope changes router or ownership behavior | Phase plan is post-anchor under `rule:lifecycle.large-phase-orchestration`, fresh-thread executable under `rule:quality.phase-plan-fresh-thread`, consumes architecture decisions, records the upcoming-stage sub-agent assessment, and does not reinterpret frozen decisions. |
| Freeze planning packages | `references/planning-freeze-gates.md` (`module:freeze-gate`), `module:lifecycle` | Current work-item artifacts | Use `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`, `rule:lifecycle.planning-shape`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.changelog-before-commit`, and `rule:lifecycle.immutable-snapshots`; identify the frozen package, transition owner, next activity, and upcoming-stage sub-agent assessment before continuity routing; stage changelog source fragments for ordinary plan-only freezes. |
| Execute approved work and record variance | Approved artifacts, architecture snapshot when present, `module:lifecycle`, `module:execution-quality` | Plan Checks and relevant project docs or tests | Use `rule:execution-quality.execution-thread-start`, record `Sub-agents: None` with a stage-specific fit reason or an approved bounded strategy, then complete planned safe work, update the matching changelog fragment, and use `rule:lifecycle.variance-policy` for noteworthy drift. |
| Release, package, or team adoption work | `references/release-policy.md` (`module:release`) | `module:architecture` when module ownership changes; `module:lifecycle` when changelog or work-item artifacts change | Preserve the Dev Doc Harness distribution package boundary, consolidated root changelog release-note source contract, release compatibility model, artifact release context, and minimal adoption/rollback flow. |
| Use or review sub-agent strategy | `references/subagent-model-policy.md` (`module:models`, `rule:models.strategy-required`) | `references/subagent-role-examples.md` (`module:role-examples`) when examples help | Record independent model-selection dimensions, orchestration mode, continuity, active repository policy, context strategy, authorization boundary, fallback, and de-facto use when applicable. |
| Evidence-heavy review or reports | `references/evidence-and-report-artifacts.md` (`module:evidence`) | Current plan or operator-specified evidence sources | Preserve evidence and stop when evidence rules require review before continuing. |
| Validate current harness surfaces | `module:execution-quality`, `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | `module:architecture` when rule, route, or ownership drift is inspected | Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` before commits that change current harness entrypoints, references, templates, README, or validation artifacts. |
| Update templates or router guidance | `module:architecture` plus the canonical owner for each referenced rule family | `module:naming` when naming examples or grammar change; affected templates | Templates own schema and prompts, not long reusable policy. |
| Superpowers or spec-kit compatibility | Applicable `AGENTS.md`, `module:lifecycle`, this skill's compatibility notes, and relevant external workflow instructions | `module:execution-quality` when environment compensation matters | The harness owns artifact location, freeze gates, variance records, commit-message and changelog discipline, and model/sub-agent notation. |

Use these supplemental references when relevant:

- `references/context-and-quality-gates.md` (`module:execution-quality`) for context load order, task preflight, environment compensation, and increment quality gates.
- `references/subagent-role-examples.md` (`module:role-examples`) for compact policy-relative role examples.
- `references/evidence-and-report-artifacts.md` (`module:evidence`) for spikes, investigations, agent reports, or review evidence.
- `references/artifact-style.md` (`module:artifact-style`) for large anchor specs, large or hard-to-scan artifacts, template prompt style, and durable artifact readability.

## Workflow

1. Classify the work as small/mechanical, small/medium work item, or large/phased work item through the router.
2. Choose a work ID using `rule:naming.work-item-paths`.
3. Create or update the work item folder at `<work-item-path>` from `rule:naming.derived-patterns`.
4. Draft the required artifacts using `assets/templates/` and the routed canonical modules.
5. Keep draft artifacts editable until explicit approval, approval commit, or explicit handoff.
6. Run the Planning Artifact Freeze Gate before implementation or later planning continues.
7. During implementation, use approved artifacts plus routed execution references, record justified variance, and update the matching `docs/work-items/<work-id>/changelog/*.md` source fragment before every commit.

## Planning Artifact Freeze Gate

When durable planning artifacts are ready for review, approval, handoff, or freeze, follow `module:freeze-gate` in `references/planning-freeze-gates.md`. It owns `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

## Superpowers compatibility

When Superpowers is installed and active, use it for its normal development methodology. This harness still owns artifact location, planning freeze gates, variance records, commit-message and changelog discipline, and model/sub-agent policy notation. Applicable project or global `AGENTS.md` guidance overrides Superpowers' default spec and plan locations for harness-managed work. The lifecycle owner is `module:lifecycle`, especially `rule:lifecycle.superpowers-compatibility`.

Before implementation, any Superpowers-produced spec or plan content that will govern the work must be copied or converted into the canonical harness work item package and pass the harness freeze gate. Add `docs/superpowers` documents only when the directory already exists and contains previous documentation packages from before the current work; never create or seed it to satisfy this compatibility condition. When allowed for continuity, every new file must be a minimal pointer stub to the canonical harness artifact.

## spec-kit compatibility

If spec-kit is installed and active, prefer a project-local adapter that points back to this skill and `module:lifecycle`. Do not make spec-kit templates the canonical source of harness rules.

## Completion checklist

- [ ] The work item folder follows `<work-item-path>` from `rule:naming.derived-patterns`.
- [ ] Top-level durable artifact filenames follow `rule:naming.derived-patterns`, including `<spec-filename>` and `<plan-filename>`.
- [ ] Required small/medium or large/phased artifacts exist and meet `module:quality`.
- [ ] Each approved or handed-off spec, plan, phase plan, or amendment has passed `module:freeze-gate`.
- [ ] The documentation artifact matrix uses `rule:lifecycle.documentation-matrix`.
- [ ] Commit subjects follow `rule:lifecycle.commit-message-format`, and the matching changelog source fragment is updated before commits under `rule:lifecycle.changelog-before-commit`.
- [ ] Frozen snapshots follow `rule:lifecycle.immutable-snapshots`.
- [ ] Variance follows `rule:lifecycle.variance-policy`.
- [ ] Plans include validation commands and expected outputs.
- [ ] Sub-agent use, if any, follows the active repository policy notation from `module:models`; useful unapproved delegation has an explicit operator request, otherwise `Sub-agents: None` records a stage-specific fit reason.
