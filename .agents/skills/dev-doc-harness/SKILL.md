---
name: dev-doc-harness
description: Use for repository development work except very small mechanical edits.
---

# Dev Doc Harness

This skill is the entrypoint and sole operational router for the Dev Doc
Harness. Start by classifying work size through `module:lifecycle` in
`references/artifact-contract.md`, then use the operation router below to load
only the policy, template, supplemental, and work-item inputs required by the
operation.

For a compact package-local orientation that travels with copied harness packages, see `docs/operator-note.md`. It is an operator-facing summary and does not override this router or the canonical references.

## When to invoke

Use this skill for all repository development work except very small mechanical edits. Classify work size through `module:lifecycle` in `references/artifact-contract.md`, especially `rule:lifecycle.work-sizing`.

Very small mechanical edits may skip this harness when the operator has not requested durable planning.

## Operation router

Load by operation. Include the current operator instruction, applicable `AGENTS.md` files, and active work-item artifacts before following a route.

| Operation family | Required route | Optional or conditional route | Required outcomes |
|---|---|---|---|
| Classify work size | `references/artifact-contract.md` (`module:lifecycle`, `rule:lifecycle.work-sizing`) | None | Very small mechanical skip stays explicit and narrow; substantial work uses harness artifacts. |
| Draft or review small specs and plans | `module:lifecycle`, `module:naming`, `module:quality`, `module:freeze-gate`, small templates in `assets/templates/` | None by default; explicitly exclude `module:models`, `module:role-examples`, `module:artifact-style`, architecture snapshots, and `module:implementation-changelog` | Create and present the compact combined small spec-and-plan package with stable commitments, verification, approval, and `Stage: plan execution`; escalate before freeze if the small boundary no longer fits. |
| Draft or review medium specs and plans | `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, medium templates in `assets/templates/` | `module:artifact-style` when the artifact becomes large or hard to scan; `assets/templates/architecture-snapshot.md` when architecture decisions need dedicated shape | Create and present both `<spec-filename>` and `<plan-filename>` in the same turn as the normal combined package; record the work item, stable IDs, useful local links or a justified mapping, checks, documentation, execution strategy, and the upcoming-stage sub-agent assessment. A spec-only package needs an operator-requested or operator-approved staged reason and hands off only to plan drafting. |
| Draft or review large anchor specs | `module:lifecycle`, `references/large-phased-lifecycle.md`, `module:naming`, `module:quality`, `module:models`, `module:artifact-style`, `assets/templates/large-phased-work-item-spec.md` | Prior approved amendments when present; `assets/templates/architecture-snapshot.md` when architecture decisions need dedicated shape | Anchor spec preserves handoff decisions, work-item architecture snapshot status, phase decomposition, scannable large-document structure, and the upcoming-stage sub-agent assessment under `rule:lifecycle.large-anchor-spec`; `rule:lifecycle.large-phase-orchestration` makes the normal output an anchor-spec-only draft review state unless combined planning was explicitly requested. |
| Draft or review phase plans | Approved spec, amendments, prior phase outputs, recorded model/context strategy, architecture snapshot when present, `module:quality`, `module:lifecycle`, `references/large-phased-lifecycle.md`, `module:naming`, `module:models`, `assets/templates/large-phased-work-item-phase-plan.md` | `module:artifact-style` when the phase artifact becomes large or hard to scan | Phase plan is post-anchor under `rule:lifecycle.large-phase-orchestration`, fresh-thread executable under `rule:quality.phase-plan-fresh-thread`, consumes architecture decisions, records the upcoming-stage sub-agent assessment, and does not reinterpret frozen decisions. |
| Freeze planning packages | `references/planning-freeze-gates.md` (`module:freeze-gate`), `module:lifecycle` | Current work-item artifacts; `module:models` only for medium and large/phased packages | Use `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`, `rule:lifecycle.planning-shape`, `rule:lifecycle.commit-message-format`, and `rule:lifecycle.immutable-snapshots`; small freezes retain the same mechanics with `Stage: plan execution` but no model or sub-agent assessment. |
| Execute approved small work and record variance | Frozen small package, applicable instructions, `module:lifecycle`, `module:execution-quality` | Plan Checks and relevant project docs or tests; load `references/implementation-changelog.md` only immediately before an implementation commit | After fresh operator execution instruction, use the small startup protocol, manually orchestrate the approved work in the same operator context unless explicitly instructed otherwise, and use variance/amendment rules for material changes. |
| Execute approved work and record variance | Approved artifacts, architecture snapshot when present, `module:lifecycle`, `module:models`, `module:execution-quality`, `references/implementation-changelog.md` (`module:implementation-changelog`) | Plan Checks and relevant project docs or tests | Apply the execution-method cascade and `rule:models.execution-review-contract` after fresh authorization: use the approved method without a second generic method question, or record a fresh explicit operator override. Then use `rule:execution-quality.execution-thread-start`, complete planned safe work, update the implementation changelog fragment, and use `rule:lifecycle.variance-policy` for noteworthy drift. |
| Maintain or consolidate implementation changelog | `references/implementation-changelog.md` (`module:implementation-changelog`) | `module:release` for Dev Doc Harness release preparation | Lint fragments, preserve frozen legacy input, consolidate eligible implementation entries, and run approved root cleanup without loading planning artifacts by default. |
| Release, package, or team adoption work | `references/release-policy.md` (`module:release`) | `module:architecture` when module ownership changes; `module:lifecycle` when changelog or work-item artifacts change | Preserve the Dev Doc Harness distribution package boundary, consolidated root changelog release-note source contract, release compatibility model, artifact release context, and minimal adoption/rollback flow. |
| Use or review sub-agent strategy | `references/subagent-model-policy.md` (`module:models`, `rule:models.strategy-required`) | `references/subagent-role-examples.md` (`module:role-examples`) when examples help | Record independent model-selection dimensions, orchestration mode, continuity, active repository policy, context strategy, authorization boundary, fallback, and de-facto use when applicable. |
| Evidence-heavy review or reports | `references/evidence-and-report-artifacts.md` (`module:evidence`) | Current plan or operator-specified evidence sources | Preserve evidence and stop when evidence rules require review before continuing. |
| Validate current harness surfaces | `module:execution-quality`, `scripts/test_harness_policy.py` in this skill directory | `module:architecture` when validating rule, route, ownership, or policy-validator maintenance | Run the active skill's `scripts/test_harness_policy.py` before commits that change current harness entrypoints, references, templates, README, or validation artifacts. |
| Update templates or router guidance | `module:architecture` plus the canonical owner for each referenced rule family | `module:naming` when naming examples or grammar change; affected templates | Templates own schema and prompts, not long reusable policy. |
| Superpowers or spec-kit compatibility | Applicable `AGENTS.md`, `module:lifecycle`, this skill's compatibility notes, and relevant external workflow instructions | `module:execution-quality` when environment compensation matters | The harness owns artifact location, freeze gates, variance records, commit-message and changelog discipline, and model/sub-agent notation. |

Use these supplemental references when relevant:

- `references/context-and-quality-gates.md` (`module:execution-quality`) for context load order, task preflight, environment compensation, and increment quality gates.
- `references/subagent-role-examples.md` (`module:role-examples`) for compact policy-relative role examples.
- `references/evidence-and-report-artifacts.md` (`module:evidence`) for spikes, investigations, agent reports, or review evidence.
- `references/artifact-style.md` (`module:artifact-style`) for large anchor specs, large or hard-to-scan artifacts, template prompt style, and durable artifact readability.

## Workflow

1. Classify the work as small/mechanical, medium work item, or large/phased work item through the router.
2. Choose a work ID using `rule:naming.work-item-paths`.
3. Create or update the work item folder at `<work-item-path>` from `rule:naming.derived-patterns`.
4. For medium work, draft both `<spec-filename>` and `<plan-filename>` in the same turn. Draft a lone spec only when the operator requested or approved staged planning, with its reason and `plan drafting` next lifecycle stage recorded.
5. Draft the required artifacts using `assets/templates/` and the routed canonical modules.
6. Keep draft artifacts editable until explicit approval and the approval commit.
7. Run the Planning Artifact Freeze Gate before implementation or later planning continues.
8. During implementation, use approved artifacts plus routed execution references, record justified variance, and update the matching implementation changelog source before every implementation commit.

## Planning Artifact Freeze Gate

When durable planning artifacts are ready for review, approval, handoff, or freeze, follow `module:freeze-gate` in `references/planning-freeze-gates.md`. It owns `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

## Superpowers compatibility

When Superpowers is installed and active, use it for its normal development methodology. This harness still owns artifact location, planning freeze gates, variance records, commit-message and changelog discipline, and model/sub-agent policy notation. Applicable project or global `AGENTS.md` guidance overrides Superpowers' default spec and plan locations for harness-managed work. The lifecycle owner is `module:lifecycle`, especially `rule:lifecycle.superpowers-compatibility`.

Before implementation, any Superpowers-produced spec or plan content that will govern the work must be copied or converted into the canonical harness work item package and pass the harness freeze gate. Add `docs/superpowers` documents only when the directory already exists and contains previous documentation packages from before the current work; never create or seed it to satisfy this compatibility condition. When allowed for continuity, every new file must be a minimal pointer stub to the canonical harness artifact.

## spec-kit compatibility

If spec-kit is installed and active, use a project-local adapter when one exists, but keep the active Dev Doc Harness skill and `module:lifecycle` as the canonical source of harness rules.

## Completion checklist

- [ ] The work item folder follows `<work-item-path>` from `rule:naming.derived-patterns`.
- [ ] Top-level durable artifact filenames follow `rule:naming.derived-patterns`, including `<spec-filename>` and `<plan-filename>`.
- [ ] Required medium or large/phased artifacts exist and meet `module:quality`.
- [ ] A normal medium package contains both canonical files, `<spec-filename>` and `<plan-filename>`; a spec-only package records the operator-requested or operator-approved staged reason and `plan drafting` next lifecycle stage.
- [ ] Each approved spec, plan, phase plan, or amendment has passed `module:freeze-gate`.
- [ ] The documentation assessment uses `rule:lifecycle.documentation-assessment`.
- [ ] Implementation commit subjects follow `rule:lifecycle.commit-message-format`, and the matching implementation changelog source is updated under `module:implementation-changelog`.
- [ ] Frozen snapshots follow `rule:lifecycle.immutable-snapshots`.
- [ ] Variance follows `rule:lifecycle.variance-policy`.
- [ ] Plans include validation commands and expected outputs.
- [ ] Sub-agent use, if any, follows the active repository policy notation from `module:models`; useful unapproved delegation has an explicit operator request, otherwise `Sub-agents: None` records a stage-specific fit reason.
