# Maintenance Architecture

## Purpose

This document defines the maintenance architecture for the repository-local
harness: module ownership, stable identifiers, allowed dependencies, and
validation constraints. It supports maintenance of routes, templates, and the
policy validator; `SKILL.md` is the sole operational router for ordinary work.

This reference owns `module:architecture`. It does not replace detailed rule
owners in the other canonical references; it provides stable module and rule
IDs so maintenance surfaces can cite ownership without copying policy prose.

## Content Types

| Content type | Meaning |
|---|---|
| Normative policy | Reusable instructions agents must follow for lifecycle, authority, safety, model choice, variance, artifact ownership, or validation. |
| Advisory guidance | Recommended diagnostics, review patterns, environment compensation, or optional role patterns. It does not override normative owners. |
| Example | Sample rows, work IDs, roles, prompts, or illustrative artifact fragments. It applies only when a current plan explicitly adopts it or a canonical reference promotes it. |

## Canonical Module Catalog

| Module ID | Owner file | Content type | Owned rule families |
|---|---|---|---|
| `module:architecture` | `references/maintenance-architecture.md` | Normative policy | Content-type taxonomy, module catalog, rule ID conventions, dependency direction, validation constraints, route budget, duplication budget, and lifecycle decomposition direction. |
| `module:naming` | `references/naming-conventions.md` | Normative policy | Work ID fields, derived naming patterns, normalization, work-item paths, artifact filenames, commit-message grammar, collision handling, and redundancy deduplication. |
| `module:lifecycle` | `references/artifact-contract.md` | Normative policy | Work item artifact layout, work sizing, lifecycle stage boundaries, combined or explicitly staged planning shape, large/phased anchors and planning orchestration, compatibility, immutable snapshots, documentation assessment, variance, and commit planning. |
| `module:implementation-changelog` | `references/implementation-changelog.md` | Normative policy | Implementation-stage fragment location, names, headings, commit synchronization, compact metadata schema, legacy fragment compatibility, root consolidation, and approved root cleanup. |
| `module:freeze-gate` | `references/planning-freeze-gates.md` | Normative policy | Draft review, approval freeze, stop-before-implementation, continuity-selected post-freeze routing, multi-gate flow, and freeze-gate compatibility. |
| `module:models` | `references/subagent-model-policy.md` | Normative policy | Task/session terminology, upcoming-stage orchestration, independent generation/tier/reasoning selection, orchestration mode, next-stage continuity, sub-agent strategy, context strategy, approved-strategy authorization, fresh confirmation, concurrency caps, review, runtime reporting, and final integration ownership. |
| `module:quality` | `references/durable-planning-quality.md` | Normative policy | Baseline plain-language and durable spec and plan quality, including additional phase-plan quality, Specification Commitments, Verification Criteria, Plan Tasks, task-bound Plan Checks, asymmetric plan coverage, static conformance semantics, and handoff preservation. |
| `module:artifact-style` | `references/artifact-style.md` | Normative policy | Conditional final-artifact presentation, scannable structure, traceability presentation, placeholder and example control, traceability density, and template prompt style. |
| `module:release` | `references/release-policy.md` | Normative policy | Dev Doc Harness distribution release identity, distributable package boundary, changelog as release source, package-local release notes, release compatibility, artifact release context, and team adoption flow. |
| `module:execution-quality` | `references/context-and-quality-gates.md` | Advisory guidance | Context loading, consumer-side execution startup after the authorized transition, task preflight, environment compensation, implementation-time conformance evidence, and increment quality gates; no planning-transition or model-selection semantics. |
| `module:evidence` | `references/evidence-and-report-artifacts.md` | Advisory guidance | Evidence preservation, report sections, and evidence stop conditions. |
| `module:role-examples` | `references/subagent-role-examples.md` | Example | Optional sub-agent role patterns, portable role shape, and role report examples. |

`module:evidence` and `module:role-examples` are supplemental unless a router
entry, spec, plan, phase plan, or operator instruction explicitly invokes them.
`module:artifact-style` is conditional for routine small/medium work, required
for large anchor specs, and required for large or hard-to-scan artifacts.

## Rule ID Conventions

Use stable, manually maintained IDs with this shape:

```text
module:<area>
rule:<area>.<short-name>
schema:<artifact>.<short-name>
scenario:<area>.<short-name>
metric:<area>.<short-name>
```

IDs are retrieval and ownership anchors, not full semantic versions. Keep them
lowercase, ASCII, and easy to search with `rg`. The canonical owner still
states the rule in normal language.

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

## Validation Model

Current validation treats the harness as a graph of declared owners and
references. Owner sets come from canonical module declarations, rule owner
tables, template schema anchors, and current scenario or metric anchors.
Reference sets come from template `Policy references:` lines, the operation
router, README route tables, validation documentation, and validation script
check definitions, including the `execution-thread-start` route.

Validation should fail when a current reference has no owner, when a current
rule or schema has more than one owner, when an owner-table local heading is
missing, when a template policy-reference list omits modules required by the
matching router operation, or when a router target points to a missing file,
module, rule, or template.

Validator evolution should stay structural, graph-oriented, and high-signal.
Add checks that protect discoverability, package boundaries, ownership, route
consistency, placeholder cleanup, or other explicitly declared artifact
contracts. Do not turn validation into a heavy semantic parser for plan quality,
operator judgment, or policy interpretation that belongs in canonical
references, approved work-item artifacts, focused tests, or human review.

Historical artifacts are tracked documentation for repository development.
They preserve review history and may cite older policy text, but they are not
current reusable-policy owners and are excluded from duplicate-policy cleanup
enforcement.

## Route And Duplication Budgets

Maintain the operation routes in `SKILL.md` within the architecture budget:
routine planning routes should not require more than four canonical modules
before optional supplemental context, and large anchor routes may require five
when naming and artifact-style checks are both required. Freeze and execution
routes may require four when changelog, immutability, or execution-quality
checks are separate.

Use `module:artifact-style` as a required route only when the artifact shape
makes readability a policy input: large anchor specs always qualify, and any
other artifact qualifies when size, wide tables, long sections, dense
traceability, or fresh-agent handoff risk makes the document hard-to-scan. Keep
the short baseline readability guidance in `module:quality` available for
routine routes that do not load the style module.

Duplicate-block validation should detect broad reusable policy blocks copied
across current harness surfaces. It should ignore frozen historical work-item
artifacts, code fences, tables, headings, and short intentional summaries. Keep
the high-signal phrase blacklist as a fast regression check.

## Lifecycle Decomposition Direction

The implementation-changelog module is the approved lifecycle split for
commit-time delivery records and root consolidation. It owns only implementation
changelog behavior; work sizing, artifact layout, planning orchestration,
immutability, documentation-assessment decisions, and variance remain lifecycle-owned.
Large/phased planning orchestration remains `rule:lifecycle.large-phase-orchestration`.
