# Small/Medium Spec Template Update Spec

Work ID: `2026-07-01_small-medium-template-structure`
Short ID: `small-medium-template-structure`
Status: Approved
Harness release: `0.4+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:evidence`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Improve the small/medium work-item spec template so filled specs capture source intent, scope boundaries, repository evidence, requirements, acceptance criteria, risks, and readiness checks clearly enough for both implementing agents and human reviewers.

## Scope

- Update `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`.
- Add spec-only prompts for source intent, scope boundary, assumptions, open questions, repository context, evidence read, constraints, requirements, acceptance criteria, interfaces/data/control flow, risks, rejected alternatives, and readiness review.
- Distinguish requirements from acceptance criteria with compact, human-readable block examples instead of wide tables with long text.
- Incorporate the review decisions from `handoff/research-verification.md`: borrow Spec Kit structure carefully, avoid EARS notation and "shall" wording, use Given/When/Then only as optional examples, apply SMART directly, and apply INVEST mainly before approval plus independence/testability inside the spec.
- Preserve existing required metadata, policy references, planned commits, documentation artifact matrix, and approval sections.
- Update `CHANGELOG.md` before the implementation commit.

## Non-scope

- No plan-template structure changes yet.
- No changes to large/phased templates.
- No changes to harness lifecycle, freeze gates, naming policy, model policy, validation scripts, release files, or canonical rule ownership unless validation shows a directly caused defect.
- No attempt to adopt GitHub Spec Kit, Kiro, EARS, BDD, INVEST, or SMART formats wholesale.
- No update to `.agents/skills/dev-doc-harness/VERSION`; the version marker is known stale on master, so this work item uses `0.4+` in its artifacts without changing release identity.

## Current state

The small/medium spec template includes the required harness surfaces: goal, scope, non-scope, current state, proposed behavior, interfaces and data, risks, acceptance criteria, planned commits, documentation matrix, and approval metadata.

The spec template is functional but basic. It prompts for required categories, but it does not strongly guide agents to:

- distinguish product/operator outcomes from implementation details,
- distinguish requirements from acceptance criteria,
- state independent test scenarios or acceptance examples when useful,
- record repository evidence used to ground the spec,
- separate decisions from open questions,
- preserve a compact review checklist before freeze.

Recent approved small/medium artifacts are more helpful than the raw template because they include concrete file expectations, stable interfaces, explicit non-scope, and validation expectations. The template should scaffold that quality directly.

## Proposed behavior

After implementation, the small/medium spec template keeps its current metadata and harness-managed sections, but its body is reorganized around this spec-first flow:

- A short metadata header with the canonical work ID, status, schema, release, policy references, and source input.
- Source and intent before scope details.
- Scope boundary with in-scope, non-scope, assumptions, and open questions.
- Repository context with current state, evidence read, and compatibility constraints.
- Requirements as card-style blocks with ID, statement, rationale, acceptance links, and notes.
- Acceptance criteria as card-style blocks with ID, observable outcome, verified requirement or scope item, and validation method.
- Interfaces, data, and control-flow prompts that force agents to check public APIs, config, schemas, persistence, state flow, safety, security, privacy, migration, and rollback.
- Risks and rejected alternatives as compact card-style blocks.
- INVEST guidance adapted to spec drafting: use negotiable/value tradeoffs before approval, use boundedness for context-window/single-thread fit, and preserve independence/testability in the approved spec.
- SMART-style quality prompts for requirements and acceptance criteria.
- Optional Given/When/Then examples only when they improve clarity.
- A small spec readiness checklist that catches unresolved placeholders, stale documentation matrix decisions, and high-impact unanswered questions before freeze.

The template must not use EARS notation or "shall" language.

## Interfaces and data

Expected implementation targets:

- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `CHANGELOG.md`

Possible supporting edits if needed:

- `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`

The validation script is not expected to change, but it is listed as a possible supporting edit if validation shows the template schema or placeholder handling needs a directly related update.

No runtime APIs, persistence schemas, external services, or command-line interfaces are affected.

## Risks

- Over-structuring the small/medium spec template could make ordinary work feel like large/phased work.
- Borrowed patterns could conflict with this harness if they duplicate freeze-gate, naming, or model-policy ownership.
- IDs can become busywork if every section gets IDs but no downstream use.
- Given/When/Then examples could be misread as mandatory for documentation-only changes where simple observable acceptance criteria are enough.
- EARS-style "shall" phrasing would make the template worse and should not be used.
- Template changes made later could accidentally touch large/phased templates or current policy files that already have unrelated uncommitted changes.
- The current worktree contains unrelated harness-policy edits; implementation must stage and commit only this work item's approved files and later scoped implementation files.

## Acceptance criteria

- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md` includes source/intent, scope boundary, repository context, requirements, acceptance criteria, interfaces/data/control flow, risks/rejected alternatives, and spec readiness sections.
- The revised template preserves required metadata, policy references, planned commits, documentation artifact matrix, and approval sections.
- Requirements and acceptance criteria are explained as different concepts with compact examples or prompts.
- The revised template avoids wide tables with long text in new sections.
- The revised template does not include EARS notation or "shall" wording.
- INVEST and SMART guidance is adapted as spec-drafting prompts, not copied as a mandatory agile story format.
- Plan-template and large/phased template changes are deferred.
- `CHANGELOG.md` contains a newest-first entry for the implementation commit before committing.
- Harness validation passes after implementation, or any failure is recorded with a blocker and no false success claim.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spike: small-medium-template-structure -- approve spec-template update plan` | `2026-07-01_small-medium-template-structure -- approve spec-template update plan` | Approval commit for this spec, plan, and research report. |
| Implementation | `docs: small-medium-template-structure -- improve spec-template scaffolding` | `2026-07-01_small-medium-template-structure -- improve spec-template scaffolding` | Implementation commit for the small/medium spec template update and changelog entry. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required before approval and implementation commits; title snippets synchronized with planned commit subjects. |
| Research verification | Derived report | Yes | Before implementation | `handoff/research-verification.md` | Captures findings, options, recommendations, and sources. |
| Test cases | Snapshot | No | Not applicable | Not applicable | Validation commands in the plan cover this template-only change. |
| Testing guide delta | Living delta | No | Not applicable | Not applicable | No testing-guide process change yet. |
| Operator manual delta | Living delta | No | Not applicable | Not applicable | This changes authoring scaffolding, not operator-facing workflow semantics. |
| API reference delta | Living delta | No | Not applicable | Not applicable | No public API changes. |
| Architecture snapshot | Snapshot | No | Not applicable | Not applicable | No architecture decision change in this research step. |
| Architecture summary delta | Living delta | No | Not applicable | Not applicable | No long-lived architecture-doc change in this research step. |

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
