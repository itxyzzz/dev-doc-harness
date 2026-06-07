# Follow-up Hardening Test Cases Snapshot

Work ID: `2026-06-07-followup-hardening`
Status: Final

## Purpose

Capture the validation cases that must exist before implementation begins. These cases focus on policy graph correctness, route-budget drift, duplicate reusable policy blocks, and tracked work-item documentation behavior.

## Test cases

| Case ID | Purpose | Expected validation signal |
|---|---|---|
| `case:graph.module-owner` | Every referenced `module:*` in current harness surfaces has exactly one current owner. | Missing or duplicate module owners fail with file path and ID. |
| `case:graph.rule-owner` | Every referenced `rule:*` in current harness surfaces has a current canonical owner. | Dangling rule references fail with file path and ID. |
| `case:graph.schema-owner` | Every referenced `schema:*` has exactly one current template/schema owner. | Missing or duplicate schema anchors fail with file path and ID. |
| `case:graph.owner-heading` | Owner-table local headings exist in the same owner file. | Missing heading fails with owner file, ID, and heading text. |
| `case:graph.template-route` | Template `Policy references:` lists include the required modules for the corresponding router operation. | Mismatch fails with template path, route name, and missing module/rule. |
| `case:graph.route-targets` | Router routes reference existing files, modules, rules, and templates. | Missing route target fails with route name and missing target. |
| `case:graph.negative-dangling-rule` | A safe local mutation that adds a temporary `rule:test.missing-owner` reference fails validation. | Validation exits nonzero and reports missing owner; temporary mutation is reverted before commit. |
| `case:route.depth-budget` | Common routes stay within the documented required-module budget. | Over-budget route fails or reports actionable route-budget drift. |
| `case:duplicate.reusable-policy-block` | Broad reusable policy duplication across current harness surfaces is detected. | Duplicate block above threshold fails or reports file pairs; historical work items are excluded. |
| `case:tracking.work-items` | `docs/work-items/` historical Markdown artifacts are tracked and no nested instruction blocks tracking. | `git ls-files docs/work-items` includes present Markdown artifacts; `docs/work-items/AGENTS.md` is absent. |

## Negative-check safety

Negative checks must not leave temporary mutations in the worktree. Prefer a script mode, temporary copy, or documented manual mutation followed by immediate restoration. Do not commit intentional failing references.
