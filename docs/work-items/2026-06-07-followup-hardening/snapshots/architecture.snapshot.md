# Follow-up Hardening Architecture Snapshot

Work ID: `2026-06-07-followup-hardening`
Status: Final

## Graph Validation Model

The policy graph validator should treat current harness files as a directed graph of declared owners and consumers.

Owner sets:

- `module:*`: declared by canonical module owner files, primarily `references/*.md`.
- `rule:*`: declared in owner tables in canonical references.
- `schema:*`: declared in template/schema files.
- `scenario:*` and `metric:*`: declared in current snapshots, architecture references, or validation docs when intended for current checks.

Reference sets:

- Template `Policy references:` lines.
- `SKILL.md` router rows and completion checklist references.
- README route and validation documentation.
- Validation script check definitions.
- Current architecture and testing docs that are not historical frozen artifacts.

Validation invariants:

- Every current reference has an owner.
- Every current rule and schema has one owner unless explicitly allowlisted.
- Owner-table local headings resolve in the owner file.
- Router route targets resolve to existing files, modules, rules, or templates.
- Template policy references satisfy required modules and rules for the corresponding operation route.
- Historical `docs/work-items/` artifacts may cite old policy and should not be used as current reusable-policy owners.

## Route Budget Model

The validator should preserve the architecture snapshot's intent: common operations should not drift back into eager loading.

Recommended enforcement:

- Count required route modules from the `SKILL.md` route table.
- Treat template paths and approved work-item artifacts as route inputs, not canonical policy modules.
- Fail or warn when routine routes exceed the documented required-module budget without an explicit exception.
- Keep final or evidence-heavy review routes allowed to load additional supplemental references when the route says so.

## Duplicate-Block Model

Duplicate-block detection should identify broad reusable policy copied across current harness surfaces. It should not penalize short intentional summaries, table headings, examples, or frozen historical artifacts.

Recommended approach:

- Normalize whitespace and punctuation enough to compare paragraph-sized blocks.
- Ignore code fences, tables where possible, headings, schema placeholder text, and work-item historical artifacts.
- Start with a conservative threshold, such as 40 or more repeated normalized words or repeated policy paragraphs above a minimum length.
- Keep the existing high-signal phrase blacklist as a fast regression check.

## Lifecycle Decomposition Recommendation

Do not split `artifact-contract.md` in this work item. First land graph validation so future splits can be checked automatically.

Recommended next decomposition options:

1. Section-level ownership only: keep `artifact-contract.md` intact but make each lifecycle rule ID, local heading, and cross-reference validated. This is lowest churn.
2. Two-file split: move changelog and documentation matrix policy to a documentation module, leaving work sizing, artifact layout, immutability, and variance in lifecycle. This is likely the first useful split if edit pressure continues.
3. Larger split: separate artifact schema/layout, lifecycle/freeze integration, documentation/changelog, and variance/amendment. Use only if future changes keep touching unrelated sections together.

Choose the smallest split that reduces real edit fan-out without increasing common-route traversal beyond budget.
