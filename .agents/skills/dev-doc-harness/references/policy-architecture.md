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
| `module:lifecycle` | `references/artifact-contract.md` | Normative policy | Work item folders, short artifact IDs, work sizing, large/phased anchors and planning orchestration, compatibility, immutable snapshots, documentation matrix, variance, commit-message format, and changelog rules. |
| `module:freeze-gate` | `references/planning-freeze-gates.md` | Normative policy | Draft review, approval freeze, stop-before-implementation, multi-gate flow, and freeze-gate compatibility. |
| `module:models` | `references/subagent-model-policy.md` | Normative policy | Model policy, sub-agent strategy, context strategy, approved-strategy authorization, fresh confirmation, concurrency caps, final review, and final integration ownership. |
| `module:quality` | `references/durable-planning-quality.md` | Normative policy | Durable spec quality, phase-plan quality, and handoff preservation. |
| `module:release` | `references/release-policy.md` | Normative policy | Release identity, distributable package boundary, changelog as release source, release notes, release compatibility, artifact release context, and team adoption flow. |
| `module:execution-quality` | `references/context-and-quality-gates.md` | Advisory guidance | Context load order, task preflight, environment compensation, and increment quality gates. |
| `module:evidence` | `references/evidence-and-report-artifacts.md` | Advisory guidance | Evidence preservation, report sections, and evidence stop conditions. |
| `module:role-examples` | `references/subagent-role-examples.md` | Example | Optional sub-agent role patterns, portable role shape, and role report examples. |

`module:evidence` and `module:role-examples` are supplemental unless a router entry, spec, plan, phase plan, or operator instruction explicitly invokes them.

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
| Draft or review durable specs and plans | `module:lifecycle`, `module:quality`, `module:models` for substantial planning |
| Freeze planning packages | `module:freeze-gate`, `module:lifecycle` |
| Execute approved work and record variance | `module:lifecycle`, `module:execution-quality` |
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

Common operation routes should stay within the architecture budget: routine routes should not require more than three canonical modules before optional supplemental context, and freeze or execution routes may require four when changelog, immutability, or execution-quality checks are separate.

Duplicate-block validation should detect broad reusable policy blocks copied across current harness surfaces. It should ignore frozen historical work-item artifacts, code fences, tables, headings, and short intentional summaries. Keep the high-signal phrase blacklist as a fast regression check.

## Lifecycle Decomposition Direction

Do not split `references/artifact-contract.md` until graph validation is in place. Prefer section-level lifecycle ownership unless future edit pressure proves a file split is worthwhile. Large/phased planning orchestration is lifecycle-owned as `rule:lifecycle.large-phase-orchestration`; freeze-gate and model-policy references should cite it for ordering instead of owning the sequence. If a split becomes useful, first consider moving changelog and documentation-matrix policy to a documentation module while leaving work sizing, artifact layout, orchestration, immutability, and variance in lifecycle.
