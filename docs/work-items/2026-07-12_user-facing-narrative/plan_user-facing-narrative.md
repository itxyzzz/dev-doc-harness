# User-Facing Narrative Plan

Work ID: `2026-07-12_user-facing-narrative`
Short ID: `user-facing-narrative`
Status: Approved
Harness release: `0.5+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:artifact-style`, `module:models`, `module:freeze-gate`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

Artifact style baseline: implementation edits must use final operator-facing prose, progressive disclosure, short sections, and one purpose per paragraph. Canonical policy remains linked rather than duplicated.

## Input Artifacts

Read these before implementation:

1. Approved spec: `spec_user-facing-narrative.md`.
2. Architecture input: architecture snapshot not applicable; the spec records the presentation decision and unchanged policy boundary.
3. Required snapshots or deltas: None.
4. Target documents: `README.md`, `.agents/skills/dev-doc-harness/docs/operator-note.md`, and `AGENTS.md`.
5. Canonical comparison inputs: `.agents/skills/dev-doc-harness/SKILL.md`, `references/artifact-contract.md`, `references/durable-planning-quality.md`, `references/artifact-style.md`, `references/planning-freeze-gates.md`, `references/subagent-model-policy.md`, `references/context-and-quality-gates.md`, `references/release-policy.md`, and `docs/release-branch-process.md`.
6. Unresolved implementation context: None identified.

## Commitment-Disposition Mapping

| Specification Commitment | Disposition | Implementation Tasks |
|---|---|---|
| `SPEC-001` foreground problems and ordinary use | Implement | `TASK-001`, `TASK-002` |
| `SPEC-002` preserve and correct the lifecycle diagram | Implement | `TASK-001` |
| `SPEC-003` apply progressive disclosure to the README | Implement | `TASK-001`, `TASK-004` |
| `SPEC-004` make the package note self-explanatory | Implement | `TASK-002`, `TASK-004` |
| `SPEC-005` summarize protected release synchronization accurately | Implement | `TASK-003`, `TASK-004` |
| `SPEC-006` preserve mature scope and policy ownership | Verification-only after documentation edits | `TASK-004` |

## Verification-Execution Mapping

| Verification Criterion | Plan Checks | Expected evidence stage |
|---|---|---|
| `VER-001` value and normal use are immediately clear | `CHECK-001`, `CHECK-002` | Review and pre-commit |
| `VER-002` diagram routes both planning shapes correctly | `CHECK-003` | Review |
| `VER-003` README is materially shorter and easier to navigate | `CHECK-001`, `CHECK-002` | Review and pre-commit |
| `VER-004` downstream note works without the README | `CHECK-004` | Review |
| `VER-005` AGENTS summary matches the runbook | `CHECK-005` | Review |
| `VER-006` concise surfaces remain policy-consistent | `CHECK-006`, `CHECK-007` | Pre-commit |
| `VER-007` the three documents tell one audience-aware story | `CHECK-004`, `CHECK-006`, `CHECK-007` | Final review and pre-commit |

Architecture coverage:

1. Architecture input: `## Architecture Decisions` in the spec; no separate snapshot.
2. Plan usage: tasks preserve canonical policy ownership and change only documentation presentation.
3. Drift path: edit the draft spec and plan before freeze; after freeze, use variance and amendment rules for policy, scope, or verification changes.
4. Reinterpretation guard: no task may change canonical workflow behavior to simplify the narrative.

## Implementation Approach

Rewrite the README as an operator journey rather than a module inventory. Keep the corrected main lifecycle diagram near the beginning, then move adoption and ordinary conversational use ahead of deeper contracts. Consolidate repeated material and move validation, template assembly, hooks, and repository maintenance under a clearly labeled maintainer section.

Edit the package-local operator note independently enough to stand without the README: add a concise value statement, preserve the compact operating contract, and relabel tooling as maintainer guidance. Keep root `AGENTS.md` terse by changing only the release-flow summary.

Perform final validation as one integrated documentation review. Word reduction is a quality target, not a license to drop any capability in `SPEC-006`.

## Change Surfaces

Expected edits:

1. `README.md`: restructure, tighten, correct the Mermaid lifecycle path, foreground problems and ordinary use, consolidate compatibility and internal inventories, and reduce low-value examples.
2. `.agents/skills/dev-doc-harness/docs/operator-note.md`: add adoption rationale, reinforce ordinary use, and distinguish maintainer tooling.
3. `AGENTS.md`: replace the stale post-release reset phrase with protected-PR synchronization and verification wording.
4. `docs/work-items/2026-07-12_user-facing-narrative/changelog/implementation.md`: record the implementation commit before committing.

Stable interfaces:

1. Canonical module and rule ownership remains unchanged.
2. Distributable package boundary remains root `AGENTS.md` plus `.agents/`.
3. Normal freeze, handoff, model, changelog, compatibility, and release behaviors remain unchanged.

Changed interfaces:

1. Human-facing information order, wording, diagram topology, and example selection.

Implementation boundaries:

1. Canonical references, templates, scripts, release notes, runbook commands, and historical work items stay out of scope because the work corrects summaries rather than policy.
2. `docs/superpowers` stays absent because the continuity precondition is not satisfied.

## Model and Sub-agent Strategy

Selection dimensions:

1. Model generation: `not exposed`.
2. Capability tier: `balanced`.
3. Reasoning effort: `medium`; use `high` as the approved fallback for final cross-document semantic review if ambiguity remains.
4. Orchestration mode: `single-agent`.
5. Resolved profile: `not exposed`.
6. Availability/fallback: runtime details are `not exposed`; fallback is the same orchestration thread with higher reasoning and deterministic validation.
7. Execution continuity: `same task`.
8. Context visibility: `not exposed`.
9. Artifact rehydration required: `Yes; reread the frozen package and current documents before editing.`
10. Model-policy source: root `AGENTS.md` active `economy-default`.
11. Override scope and expiry: None.

Fit assessment:

1. Complexity: medium because three documents must be restructured as one narrative without changing policy.
2. Risk and blast radius: medium because README and package guidance shape future agent and operator behavior.
3. Ambiguity: low after operator approval of rewrite depth, retained diagram, and ordinary-use principle.
4. Budget and latency fit: a single agent avoids coordination overhead across tightly coupled prose surfaces.

Recommended selection change:

1. None.

Sub-agents:

1. None. The edits are tightly coupled, share terminology, and require one integrated narrative voice; deterministic checks and main-thread final review provide better value than delegation.

## Implementation Tasks

### `TASK-001` Implementation Task — restructure the README and correct the lifecycle diagram

Dependencies:

1. Frozen combined planning package and fresh post-freeze start authorization.

Implementation:

1. Record the pre-edit README word count for `CHECK-001`.
2. Replace the duplicated opening with one concise positioning statement and an early problems/outcomes section.
3. Preserve the main Mermaid diagram and split the large/phased route so anchor freeze leads to phase-plan drafting and a later phase-plan freeze before implementation.
4. Order the remaining content by progressive disclosure: lifecycle overview, adoption and ordinary use, core operator contracts, compatibility, maintainer internals, limitations, and contributing.
5. Remove the Scrum analogy; consolidate repeated Superpowers, canonical-owner, override, and internal-inventory explanations.
6. Present normal usage as ordinary work requests plus conversation and approval checkpoints. Retain only examples that express a meaningful exception, stop, review, or plan-only PR checkpoint.
7. Preserve every operator capability listed by `SPEC-006` and keep canonical links sufficient for deeper detail.

Exit criteria:

1. The corrected diagram passes manual path tracing.
2. README section order matches `SPEC-003` and the word count is approximately 20-30% below baseline or has a documented review reason for a small variance.
3. No mature capability in `SPEC-006` is omitted.

### `TASK-002` Implementation Task — make the package-local operator note stand alone

Dependencies:

1. `TASK-001` narrative choices so the compact package note uses consistent terminology without copying the README.

Implementation:

1. Add a short opening that explains the lost-context, premature-execution, silent-drift, conformance, and handoff problems the harness addresses.
2. State that operators ask for work normally and use conversation plus explicit approval checkpoints rather than harness commands.
3. Preserve copy/adoption instructions, planning shapes, conformance model, Superpowers restriction, freeze/handoff behavior, variance, and changelog fragments.
4. Rename or introduce a final maintainer-only heading for validation, template assembly, and repository-local hook guidance.
5. Tighten repeated wording without importing repository-only history or root README dependencies.

Exit criteria:

1. The note explains why, what to copy, normal use, pause points, and maintainer-only tooling when read independently.

### `TASK-003` Implementation Task — correct the release-flow summary in root instructions

Dependencies:

1. Frozen combined planning package.

Implementation:

1. Replace “post-release `master` reset” with concise wording that names the protected post-release PR and post-merge remote verification before later development branches.
2. Keep `docs/release-branch-process.md` as the sole owner of exact commands and failure handling.

Exit criteria:

1. Root `AGENTS.md` has no stale reset wording and remains concise.

### `TASK-004` Implementation Task — validate the integrated narrative and prepare the commit

Dependencies:

1. `TASK-001`, `TASK-002`, and `TASK-003`.

Implementation:

1. Run every Plan Check and record its execution instance, output, and status.
2. Review the three documents side by side for audience boundaries, contradictions, duplicated policy, missing capabilities, placeholders, broken Markdown, and generated noise.
3. Update `docs/work-items/2026-07-12_user-facing-narrative/changelog/implementation.md` with the approved implementation title and required release metadata.
4. Inspect the path-scoped diff and worktree status; stage only the three target documents and implementation changelog fragment.
5. Commit with `docs: user-facing-narrative -- streamline operator guidance` only when all applicable Verification Criteria pass.

Exit criteria:

1. `CHECK-001` through `CHECK-007` pass, the implementation fragment is synchronized, and the staged diff contains no unrelated paths.

## Plan Checks

### `CHECK-001` Plan Check — compare README size and headings

Covers:

1. `VER-001`.
2. `VER-003`.

Procedure:

1. Before and after editing, run PowerShell word and heading counts over `README.md` using `Get-Content -Raw` for words and `Select-String '^#{1,3} '` for headings.
2. Calculate the percentage reduction and compare the final heading order to `SPEC-003`.

Expected result:

1. Approximately 20-30% fewer words, one introduction, and headings ordered by progressive disclosure. A small variance is acceptable only when final review confirms that further removal would hide an in-scope capability.

Evidence record:

1. Completion report entry for the `CHECK-001` execution instance with before/after counts and final heading list.

Stage or environment:

1. Pre-edit baseline and pre-commit review in the repository workspace.

Task/check coordination:

1. Baseline enables `TASK-001`; final result gates `TASK-004`.

### `CHECK-002` Plan Check — review problem and usage framing

Covers:

1. `VER-001`.
2. `VER-003`.

Procedure:

1. Inspect the README before its first maintainer-internals heading and verify it names the problems in `SPEC-001`, states that ordinary requests are sufficient, and contains no default-use prompt that reads like a required command.
2. Review every retained usage example and map it to an explicit exception, stop condition, review checkpoint, or plan-only PR checkpoint.

Expected result:

1. Problems and ordinary use precede internals; every retained example adds non-default value.

Evidence record:

1. Completion report entry listing retained examples and their purpose.

Stage or environment:

1. Final documentation review.

Task/check coordination:

1. Gates completion of `TASK-001` and `TASK-004`.

### `CHECK-003` Plan Check — trace lifecycle diagram paths

Covers:

1. `VER-002`.

Procedure:

1. Trace the Mermaid source for three cases: very-small edit; combined small/medium spec-and-plan; large/phased anchor followed by phase plan.
2. Confirm every implementation route has the applicable planning freeze, pause, documented next activity, and continuity selection.

Expected result:

1. The very-small path remains direct; combined small/medium reaches implementation only after its combined freeze; large/phased reaches implementation only after anchor freeze, later phase-plan drafting, and phase-plan freeze.

Evidence record:

1. Completion report entry with the three traced node sequences.

Stage or environment:

1. README review before pre-commit validation.

Task/check coordination:

1. Gates completion of `TASK-001`.

### `CHECK-004` Plan Check — review the operator note independently

Covers:

1. `VER-004`.
2. `VER-007`.

Procedure:

1. Read `.agents/skills/dev-doc-harness/docs/operator-note.md` without relying on README context and answer four questions from its text: why adopt, what to copy, how normal use works, and which guidance is maintainer-only.

Expected result:

1. Each answer is explicit and consistent with the canonical package boundary and lifecycle.

Evidence record:

1. Completion report entry with the four concise answers.

Stage or environment:

1. Final documentation review.

Task/check coordination:

1. Gates completion of `TASK-002` and `TASK-004`.

### `CHECK-005` Plan Check — compare release summary with runbook

Covers:

1. `VER-005`.

Procedure:

1. Run `rg -n "post-release|master reset|protected|pull request|verification" AGENTS.md docs/release-branch-process.md`.
2. Compare the root summary with the runbook's post-release topic-branch, PR, ancestry, and changelog-comparison requirements.

Expected result:

1. No stale `master reset` phrase remains; root instructions name protected PR synchronization and verification without duplicating commands.

Evidence record:

1. Completion report entry with relevant search lines and pass/fail status.

Stage or environment:

1. Final documentation review.

Task/check coordination:

1. Gates completion of `TASK-003`.

### `CHECK-006` Plan Check — verify capability and compatibility preservation

Covers:

1. `VER-006`.
2. `VER-007`.

Procedure:

1. Review the final documents against the full `SPEC-006` capability list.
2. Run `rg -n "docs/superpowers|Specification Commitment|Verification Criterion|Plan Check|changelog|Superpowers|spec-kit|new task|variance|architecture" README.md .agents/skills/dev-doc-harness/docs/operator-note.md AGENTS.md`.
3. Run `git status --short` and confirm no file exists under `docs/superpowers`.

Expected result:

1. Every capability remains discoverable where appropriate, compatibility restrictions remain consistent, and no `docs/superpowers` artifact is added.

Evidence record:

1. Completion report checklist plus focused search and status results.

Stage or environment:

1. Pre-commit repository review.

Task/check coordination:

1. Gates `TASK-004`.

### `CHECK-007` Plan Check — run full harness validation

Covers:

1. `VER-006`.
2. `VER-007`.

Procedure:

1. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.
2. Review `git diff --check` and the path-scoped final diff.

Expected result:

1. Validator exits `0` with all checks passing; `git diff --check` reports no whitespace errors; the diff contains only approved documentation and changelog changes.

Evidence record:

1. Completion report entry with command outputs and execution status.

Stage or environment:

1. Pre-commit repository workspace.

Task/check coordination:

1. Final gate for `TASK-004` and the implementation commit.

## Planned commits

Planning approval commit:

1. Planned subject: `plan: user-facing-narrative -- approve concise operator story`.
2. Changelog title or snippet: `2026-07-12_user-facing-narrative -- approve concise operator story`.
3. Notes: approval commit for this spec, plan, and `changelog/planning-approval.md`.

Implementation commit:

1. Planned subject: `docs: user-facing-narrative -- streamline operator guidance`.
2. Changelog title or snippet: `2026-07-12_user-facing-narrative -- streamline operator guidance`.
3. Notes: target documents and `changelog/implementation.md` after all Plan Checks pass.

## Check execution and completion records

For every Plan Check execution, record the `CHECK` ID, a unique execution instance, stage or environment, actual result, evidence location or inline evidence, and `pass`, `fail`, or `blocker` status. Repeated executions of an unchanged procedure produce distinct records. A material procedure change follows approved variance or amendment rather than silently reusing the ID.

Completion reports cite executed Plan Checks, resulting Verification Criterion status, remaining task or disposition status, variance, and residual risk. Task completion alone does not establish conformance.

## Plan variance handling

Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for canonical policy, workflow behavior, package boundary, scope, Verification Criterion, Plan Check, or feasibility changes.

## Planning artifact freeze gate

1. Draft review status: approved by the operator on 2026-07-12.
2. Approval commit: created by the freeze gate; see repository history for the final hash.
3. Post-freeze implementation authorization: not granted.
4. Stop condition: do not edit `README.md`, `.agents/skills/dev-doc-harness/docs/operator-note.md`, or `AGENTS.md` until the package is approved, frozen, committed, and followed by a fresh explicit start instruction.

## Next-task handoff

1. Planning shape: `combined small/medium plan`.
2. Frozen package: `spec_user-facing-narrative.md` and `plan_user-facing-narrative.md`.
3. Next activity: implement the documentation restructure and correction beginning with `TASK-001`.
4. Execution continuity: `same task`.
5. Context visibility: `not exposed`.
6. Artifact rehydration required: `Yes; reread the frozen package, current target documents, and worktree state before editing.`
7. Exact authoritative artifacts: this plan and `spec_user-facing-narrative.md`.
8. Approved strategy and fallback: `## Model and Sub-agent Strategy` above.
9. First activity: `TASK-001`.
10. Variance stop condition: stop for approval before changing canonical policy, templates, scripts, release behavior, package boundaries, committed scope, Verification Criteria, or Plan Checks.

## Plan readiness checklist

- [x] Input artifacts and relevant repository context have been read and listed.
- [x] Every in-scope Specification Commitment has an authorized disposition and every applicable Verification Criterion has Plan Check coverage.
- [x] Risks, scope boundaries, interfaces, and documentation decisions are covered by tasks or explicit no-op reasons.
- [x] Task detail is sufficient for a fresh implementation agent to execute without inventing order, file scope, validation, or documentation steps.
- [x] Plan Checks have complete procedure, result, evidence-record, and stage/environment fields.
- [x] Planned commits and changelog title snippets are synchronized.
- [x] Variance handling is clear for likely implementation drift.
- [x] The work fits one orchestration thread.
- [x] Sub-agents are explicitly not used with a fit rationale.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Completion criteria

- Applicable Verification Criteria have evidence-backed status, and required Implementation Tasks are complete.
- `CHECK-001` through `CHECK-007` have passed and been recorded.
- README retains the corrected main lifecycle diagram and the mature capability set while meeting the approved concision goal.
- Operator note stands alone and labels maintainer tooling.
- Root AGENTS release summary matches the protected runbook flow.
- The implementation changelog fragment is current before commit.
- The implementation commit uses the approved subject, or approved variance records a changed subject.
- Variance log is present only if nontrivial implementation variance occurs.
- De-facto execution reports single-agent use and any fallback reasoning applied.

## Approval

- Status: Approved
- Superseded by: None
