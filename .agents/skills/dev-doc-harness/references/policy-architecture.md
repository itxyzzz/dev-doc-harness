# Policy Architecture

## Purpose

This document defines the canonical module catalog and rule-interface conventions for the repository-local harness. It is the compact operational counterpart to the Phase 01 architecture snapshot at `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`.

This reference owns `module:architecture`. It does not replace detailed rule owners in the other canonical references; it names them so templates, router guidance, and future validation can cite stable module and rule IDs without copying policy prose.

## Content Types

| Content type | Meaning | Reusable policy source? |
|---|---|---:|
| Normative policy | Reusable instructions agents must follow for lifecycle, authority, safety, model choice, variance, artifact ownership, or validation. | Yes, when owned by `AGENTS.md`, `SKILL.md`, or canonical references. |
| Artifact schema | Required shape of specs, plans, snapshots, deltas, reports, and variance logs. | Yes for structure; no for unrelated lifecycle policy. |
| Example | Sample rows, work IDs, roles, prompts, or illustrative artifact fragments. | No, unless a current plan explicitly adopts it or a canonical reference promotes it. |
| Advisory guidance | Recommended diagnostics, review patterns, environment compensation, or optional role patterns. | Only when invoked by the router or an approved plan; it does not override normative owners. |
| Operator-facing summary | Human-readable overview of harness outcomes, flow, and usage. | No, except explicit repository overrides in `AGENTS.md`. |
| Historical snapshot | Approved, frozen, or handed-off work-item artifact preserving decisions at a point in time. | Yes for that work item; no for reusable future policy. |

## Canonical Module Catalog

| Module ID | Owner file | Content type | Owned rule families |
|---|---|---|---|
| `module:architecture` | `references/policy-architecture.md` | Normative policy | Content-type taxonomy, module catalog, rule ID conventions, dependency direction, and router inputs. |
| `module:naming` | `references/naming-conventions.md` | Normative policy | Work ID fields, derived naming patterns, normalization, work-item paths, artifact filenames, commit-message grammar, changelog-entry grammar, collision handling, and redundancy deduplication. |
| `module:lifecycle` | `references/artifact-contract.md` | Normative policy | Work item artifact layout, work sizing, combined or explicitly staged planning shape, large/phased anchors and planning orchestration, compatibility, immutable snapshots, documentation matrix, variance, commit planning, and changelog-before-commit rules. |
| `module:freeze-gate` | `references/planning-freeze-gates.md` | Normative policy | Draft review, approval freeze, stop-before-implementation, continuity-selected post-freeze routing, multi-gate flow, and freeze-gate compatibility. |
| `module:models` | `references/subagent-model-policy.md` | Normative policy | Execution terminology, model selection dimensions, orchestration mode, execution continuity, sub-agent strategy, context strategy, approved-strategy authorization, fresh confirmation, concurrency caps, final review, and final integration ownership. |
| `module:quality` | `references/durable-planning-quality.md` | Normative policy | Baseline plain-language and durable spec and plan quality, including additional phase-plan quality, Specification Commitments, Verification Criteria, Plan Tasks, task-bound Plan Checks, asymmetric plan coverage, static conformance semantics, and handoff preservation. |
| `module:artifact-style` | `references/artifact-style.md` | Normative policy | Conditional final-artifact presentation, scannable structure, traceability presentation, placeholder and example control, traceability density, and template prompt style. |
| `module:release` | `references/release-policy.md` | Normative policy | Dev Doc Harness distribution release identity, distributable package boundary, changelog as release source, package-local release notes, release compatibility, artifact release context, and team adoption flow. |
| `module:execution-quality` | `references/context-and-quality-gates.md` | Advisory guidance | Context loading, consumer-side execution startup after the authorized transition, task preflight, environment compensation, implementation-time conformance evidence, and increment quality gates; no planning-transition or model-selection semantics. |
| `module:evidence` | `references/evidence-and-report-artifacts.md` | Advisory guidance | Evidence preservation, report sections, and evidence stop conditions. |
| `module:role-examples` | `references/subagent-role-examples.md` | Example | Optional sub-agent role patterns, portable role shape, and role report examples. |

`module:evidence` and `module:role-examples` are supplemental unless a router entry, spec, plan, phase plan, or operator instruction explicitly invokes them. `module:artifact-style` is conditional for routine small/medium work, required for large anchor specs, and required for large or hard-to-scan artifacts.

## Rule ID Conventions

Use stable, manually maintained IDs with this shape:

```text
module:<area>
rule:<area>.<short-name>
schema:<artifact>.<short-name>
scenario:<area>.<short-name>
metric:<area>.<short-name>
```

IDs are retrieval and ownership anchors, not full semantic versions. Keep them lowercase, ASCII, and easy to search with `rg`. The canonical owner still states the rule in normal language.

## Dependency Direction

Allowed reference direction:

```text
AGENTS.md -> SKILL.md -> canonical references -> supplemental references
                         -> templates
                         -> work-item artifacts
README/operator summaries -> canonical references
```

Rules:

- `AGENTS.md` bootstraps the repository-local harness and repository-specific overrides.
- `SKILL.md` routes operations to canonical references, templates, and supplemental references.
- Canonical references may cite other canonical references only when the dependency is part of the rule interface.
- Canonical references do not depend on README summaries or templates for policy meaning.
- Templates may cite schemas and rule IDs, but do not own long reusable policy.
- Work-item artifacts record selected decisions, statuses, approvals, exceptions, variance, and cited rule IDs.
- Historical artifacts are not updated to mimic current policy.
- README and operator summaries explain and link; they do not own normative rules unless they are also repository instructions such as `AGENTS.md`.

## Router Inputs

Future router work should load by operation rather than eagerly loading every reference. Common operations should identify the minimum module set needed for safe execution:

| Operation family | Typical modules |
|---|---|
| Classify work size | `module:lifecycle` |
| Draft or review routine small/medium specs and plans | `module:lifecycle`, `module:quality`, `module:models`; add `module:naming` for work IDs or planned subjects, and add `module:artifact-style` when readability risk is material |
| Draft or review large anchor specs | `module:lifecycle`, `module:quality`, `module:models`, `module:artifact-style` |
| Draft or review phase plans | `module:lifecycle`, `module:quality`, `module:models`; add `module:artifact-style` for large or hard-to-scan phase artifacts |
| Freeze planning packages | `module:freeze-gate`, `module:lifecycle`; determine planning shape, frozen package, and next activity before continuity routing |
| Execute approved work and record variance | `module:lifecycle`, `module:execution-quality`; use `rule:execution-quality.execution-thread-start` for fresh-task or same-task model-transition handoff |
| Use or review sub-agent strategy | `module:models`, optionally `module:role-examples` |
| Handle evidence-heavy review or reports | `module:evidence` |
| Update templates or router guidance | `module:architecture`, plus the canonical owner for each referenced rule family |

## Release Compatibility

Release compatibility is owned by `module:release` in `references/release-policy.md`.

Module and rule IDs are stable retrieval and ownership anchors, not full semantic versions. If an ID changes, prefer a clear replacement note such as `Superseded by:` in the canonical owner and do not rewrite frozen historical artifacts solely to update cited IDs.

## Validation Model

Current validation treats the harness as a graph of declared owners and references. Owner sets come from canonical module declarations, rule owner tables, template schema anchors, and current scenario or metric anchors. Reference sets come from template `Policy references:` lines, the operation router, README route tables, validation documentation, and validation script check definitions.

Validation should fail when a current reference has no owner, when a current rule or schema has more than one owner, when an owner-table local heading is missing, when a template policy-reference list omits modules required by the matching router operation, or when a router target points to a missing file, module, rule, or template.

Validator evolution should stay structural, graph-oriented, and high-signal. Add checks that protect discoverability, package boundaries, ownership, route consistency, placeholder cleanup, or other explicitly declared artifact contracts. Do not turn validation into a heavy semantic parser for plan quality, operator judgment, or policy interpretation that belongs in routed references, approved work-item artifacts, focused tests, or human review.

Historical artifacts are tracked documentation for repository development. Historical work-item artifacts preserve review history. They may cite older policy text, but they are not current reusable-policy owners and are excluded from duplicate-policy cleanup enforcement.

## Route And Duplication Budgets

Common operation routes should stay within the architecture budget: routine routes should not require more than three canonical modules before optional supplemental context, and freeze, execution, or large anchor routes may require four when changelog, immutability, execution-quality, or artifact-style checks are separate.

Use `module:artifact-style` as a required route only when the artifact shape makes readability a policy input: large anchor specs always qualify, and any other artifact qualifies when size, wide tables, long sections, dense traceability, or fresh-agent handoff risk makes the document hard to scan. Keep the short baseline readability guidance in `module:quality` available for routine routes that do not load the style module.

Duplicate-block validation should detect broad reusable policy blocks copied across current harness surfaces. It should ignore frozen historical work-item artifacts, code fences, tables, headings, and short intentional summaries. Keep the high-signal phrase blacklist as a fast regression check.

## Lifecycle Decomposition Direction

Do not split `references/artifact-contract.md` until graph validation is in place. Prefer section-level lifecycle ownership unless future edit pressure proves a file split is worthwhile. Large/phased planning orchestration is lifecycle-owned as `rule:lifecycle.large-phase-orchestration`; freeze-gate and model-policy references should cite it for ordering instead of owning the sequence. If a split becomes useful, first consider moving changelog and documentation-matrix policy to a documentation module while leaving work sizing, artifact layout, orchestration, immutability, and variance in lifecycle.
