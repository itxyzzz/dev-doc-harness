# Naming Conventions Test Cases Snapshot

Work ID: `2026-07-01-naming-conventions`
Short ID: `naming-conventions`
Status: Approved
Harness release: `0.3.0`
Policy references: `module:lifecycle`, `module:quality`, `module:freeze-gate`

## Purpose

Capture validation expectations for centralizing harness naming conventions before implementation begins.

## Test cases

| ID | Scenario | Command or review | Expected result |
|---|---|---|---|
| `scenario:naming.reference-owner` | New naming reference is part of the policy graph | `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | The validator recognizes `module:naming` and all concrete `rule:naming.*` references without dangling-owner failures. |
| `scenario:naming.current-surfaces` | Current reusable surfaces point to naming policy instead of duplicating stale forms | `rg -n "module:naming|rule:naming" .agents/skills/dev-doc-harness/references .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/assets/templates README.md` | Matches include the new owner file plus concise references from lifecycle, router, templates, README, and operator-facing guidance. |
| `scenario:naming.old-patterns` | Old hyphen-only placeholders are removed from current reusable surfaces | `rg -n "YYYY-MM-DD-short-kebab-title|YYYY-MM-DD-ISSUE-short-kebab-title|spec-<short-id>|plan-<short-id>|plan-phase|plan-amendment-NNN-short-title" .agents/skills/dev-doc-harness README.md AGENTS.md` | No matches remain in current reusable surfaces except historical release notes or intentional migration notes with clear context. |
| `scenario:naming.historical-preservation` | Frozen historical artifacts are not renamed to match the new convention | `git status --short docs/work-items` | Implementation status shows no mass rename of pre-existing historical work-item paths. |
| `scenario:naming.commit-deduplication` | Commit-message examples avoid redundant elaboration snippets | Manual review of `.agents/skills/dev-doc-harness/references/naming-conventions.md` and updated templates | Bad duplicate examples are either absent or explicitly labeled as bad; good examples show omitted elaboration when the kebab title is self-explanatory. |
| `scenario:naming.changelog-grammar` | Changelog grammar supports date plus full commit message or work ID plus optional elaboration | Manual review of `.agents/skills/dev-doc-harness/references/naming-conventions.md` and `artifact-contract.md` | The canonical reference defines both accepted forms and lifecycle references point to it. |

## Notes

These cases validate current reusable policy surfaces only. Historical work-item artifacts and previous changelog entries remain snapshots of the rules active when they were written.
