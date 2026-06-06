# Phase 05 Golden Traversal Test Cases

Work ID: `2026-06-05-refactor-as-code`
Status: Final

## Source references

- Approved spec: `../spec-refactor-as-code.md`
- Approved amendment: `../plan-amendment-001-architecture-guardrails-refactor-as-code.md`
- Architecture snapshot: `architecture.snapshot.md`
- Approved Phase 05 plan: `../plan-phase-05-validation-hardening-refactor-as-code.md`

## Purpose

This snapshot records traversal and policy-drift test cases for the refactored harness. These are static harness behavior checks, not runtime product tests.

The validation command checks current harness surfaces and evidence paths. It does not rewrite historical work-item artifacts, and full rule versioning remains deferred.

## Golden scenarios

| Scenario ID | Entrypoint | Required files or modules | Expected behavior | Script evidence checked |
|---|---|---|---|---|
| `scenario:work-size.very-small-skip` | `AGENTS.md` then `.agents/skills/dev-doc-harness/SKILL.md` | `module:lifecycle`, `rule:lifecycle.work-sizing`, `references/artifact-contract.md` | Agent may explicitly classify a typo or tiny mechanical edit as very small, preserve behavior, run relevant checks, and skip durable work-item artifacts when no durable planning was requested. | Root sizing summary, router sizing route, and lifecycle sizing rule. |
| `scenario:planning.small-medium` | `AGENTS.md` then `.agents/skills/dev-doc-harness/SKILL.md` | `module:lifecycle`, `module:quality`, small/medium spec and plan templates, `module:models` when strategy is assessed | Agent creates `docs/work-items/<work-id>/spec-<short-id>.md`, `plan-<short-id>.md`, documentation matrix, and model/sub-agent strategy or `None`; drafts are staged without committing before approval. | Small/medium router route and both small/medium schema IDs. |
| `scenario:planning.large-anchor-freeze` | `AGENTS.md` then `.agents/skills/dev-doc-harness/SKILL.md` | `module:lifecycle`, `module:quality`, large/phased spec template, `module:freeze-gate` | Agent drafts an anchor spec preserving scope, non-scope, assumptions, risks, rejected alternatives, acceptance criteria, phase decomposition, documentation matrix, and freeze-gate approval path; freeze happens only after approval and changelog commit. | Large-anchor router route, large spec schema, and freeze-gate owner. |
| `scenario:planning.phase-plan-freeze` | Frozen anchor spec plus `.agents/skills/dev-doc-harness/SKILL.md` | Approved spec and amendments, prior phase outputs, `module:quality`, `module:lifecycle`, `module:models`, phase-plan template, `module:freeze-gate` | Agent drafts a fresh-thread-executable phase plan, preserves anchor decisions, stages for review, commits only after approval, and stops before implementation. | Phase-plan route, fresh-thread rule, phase schema, and freeze owner. |
| `scenario:execution.post-freeze-authorization` | Approved phase plan plus implementation authorization | Approved spec, amendments, phase plan, `module:lifecycle`, `module:execution-quality` | Agent executes only the approved phase scope, updates variance log when needed, updates changelog before commit, and does not ask for a second sub-agent-specific confirmation for the approved strategy. | Fresh authorization text, variance rule, and scope quality gate. |
| `scenario:variance.high-impact-amendment` | Approved plan plus discovered high-impact variance | `rule:lifecycle.variance-policy`, `module:freeze-gate`, plan amendment template | Agent stops, drafts `plan-amendment-NNN-short-title-<short-id>.md`, stages for approval, and does not continue implementation until amendment freeze and reauthorization. | Amendment path, amendment freeze, and amendment schema. |
| `scenario:models.sub-agent-authorization` | Approved plan with bounded sub-agent strategy | `module:models`, optional `module:role-examples`, approved plan strategy | Agent may use approved strategy after post-freeze implementation authorization; fresh confirmation is required only for unplanned agents, unrecorded stronger model or reasoning, write-scope escalation, platform-restricted actions, or more than three concurrent agents. | Approved-strategy rule, fresh-confirmation rule, and strategy table evidence. |
| `scenario:compat.superpowers` | Superpowers active during harness-managed work | `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, `rule:lifecycle.superpowers-compatibility` | Superpowers may own brainstorming, execution, review, or TDD method, while the harness owns artifact location, planning freeze gates, variance records, changelog, and model/sub-agent policy notation. | Root compatibility text, router compatibility text, and lifecycle compatibility rule. |
| `scenario:history.historical-artifact-handling` | Current policy differs from old frozen artifact without explicit exception | `rule:lifecycle.immutable-snapshots`, `module:architecture`, relevant historical artifact | Agent follows current canonical policy for new execution, treats old artifact as historical evidence, and avoids rewriting it to hide drift. | Immutable-snapshot rule, historical artifact handling rule, and source scenario row. |

## Validation command

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
```

Expected result: the command exits `0` and prints one `PASS <check-id>` line for every Phase 05 check.
