# Artifact Style Guidance Plan

Work ID: `2026-07-03_artifact-style-guidance`
Short ID: `artifact-style-guidance`
Status: Approved
Harness release: `0.4+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `module:evidence`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:lifecycle.work-item-architecture-decisions`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`, `rule:evidence.preservation`

## Input Artifacts

Read these before implementation:

1. Approved spec: `spec_artifact-style-guidance.md`.
2. Architecture input: `snapshots/architecture.snapshot.md`.
3. Required snapshots or deltas: `snapshots/architecture.snapshot.md`; no other snapshots or deltas are required.
4. Relevant repository files:
   - `.agents/skills/dev-doc-harness/SKILL.md`
   - `.agents/skills/dev-doc-harness/references/policy-architecture.md`
   - `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
   - `.agents/skills/dev-doc-harness/references/artifact-contract.md`
   - `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
   - `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
   - `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`
   - `.agents/skills/dev-doc-harness/assets/templates/`
   - `.agents/skills/dev-doc-harness/assets/templates/blocks/`
   - `.agents/skills/dev-doc-harness/assets/templates/assemblies/`
   - `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`
   - `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
   - `README.md`
   - `.agents/skills/dev-doc-harness/docs/operator-note.md`
   - `.agents/skills/dev-doc-harness/docs/releases/0.4+.md`
   - `CHANGELOG.md`
5. Review evidence:
   - Three read-only extra-high-reasoning sub-agent review reports from the 2026-07-03 review wave.
6. Historical artifact exclusion set:
   - `docs/work-items/2026-07-02_orchestration-sizing-large-templates/`
   - `docs/work-items/2026-07-02_template-block-assembly/`
   - `docs/work-items/2026-07-03_work-item-architecture-decisions/`
7. Unresolved implementation context to confirm before editing: None identified after planning review.

If architecture is missing, ambiguous, or changed before freeze, update the draft spec or architecture snapshot before finalizing this plan. If architecture changes after freeze, use variance handling and an amendment when `rule:lifecycle.variance-policy` requires approval.

## Spec Traceability

Requirement coverage:

1. `REQ-001`: implemented by `T-001`; verified by `V-001`, `V-002`, and `V-011`.
2. `REQ-002`: implemented by `T-002` and `T-003`; verified by `V-002`, `V-003`, and `V-006`.
3. `REQ-003`: implemented by `T-002` and `T-003`; verified by `V-003`, `V-006`, and `V-011`.
4. `REQ-004`: implemented by `T-003` and `T-006`; verified by `V-004`, `V-006`, `V-009`, and `V-011`.
5. `REQ-005`: implemented by `T-003`, `T-004`, and `T-006`; verified by `V-004`, `V-005`, `V-006`, and `V-011`.
6. `REQ-006`: implemented by `T-003`; verified by `V-004`, `V-006`, and `V-011`.
7. `REQ-007`: implemented by `T-004`; verified by `V-007` and `V-011`.
8. `REQ-008`: implemented by `T-004`; verified by `V-008` and `V-011`.
9. `REQ-009`: implemented by `T-003` and `T-006`; verified by `V-005`, `V-006`, and `V-011`.
10. `REQ-010`: implemented by `T-005` and `T-007`; verified by `V-009`, `V-010`, `V-011`, and `V-012`.
11. `REQ-011`: implemented by `T-008`; verified by `V-013`.

Acceptance coverage:

1. `AC-001`: `T-001`; `V-001`, `V-011`.
2. `AC-002`: `T-001`, `T-002`; `V-002`, `V-011`.
3. `AC-003`: `T-002`, `T-003`; `V-003`, `V-011`.
4. `AC-004`: `T-003`, `T-006`; `V-004`, `V-006`, `V-011`.
5. `AC-005`: `T-003`, `T-004`, `T-006`; `V-004`, `V-005`, `V-006`, `V-011`.
6. `AC-006`: `T-003`; `V-004`, `V-011`.
7. `AC-007`: `T-004`; `V-007`, `V-011`.
8. `AC-008`: `T-003`, `T-005`; `V-006`, `V-011`.
9. `AC-009`: `T-004`; `V-008`, `V-011`.
10. `AC-010`: `T-006`; `V-005`, `V-011`.
11. `AC-011`: `T-005`; `V-009`, `V-011`.
12. `AC-012`: `T-007`; `V-010`, `V-011`.
13. `AC-013`: `T-008`; `V-013`.

Risk and boundary coverage:

1. `RISK-001`: `T-001`, `T-002`; style module stays narrow and router guidance preserves boundaries.
2. `RISK-002`: `T-002`, `T-003`; baseline guidance and template cues remain visible without loading the module.
3. `RISK-003`: `T-002`; style routing is conditional except for large anchor specs and materially large documents.
4. `RISK-004`: `T-003`; templates use concise cues and route to the module for reusable policy.
5. `RISK-005`: `T-005`; validator stays structural and high-signal.
6. `RISK-006`: `T-004`; evidence preservation remains in `module:evidence`.
7. `RISK-007`: `T-008`; historical implemented specs are excluded from the diff.
8. `RISK-008`: `T-002`; router wording distinguishes policy architecture from work-item architecture.
9. `RISK-009`: `T-001`, `T-002`, `T-003`; style-loading conditions define practical readability triggers.

Architecture coverage:

1. Architecture input: `snapshots/architecture.snapshot.md`, especially `DEC-001` through `DEC-004`.
2. Plan usage: tasks sequence module ownership, routing, templates, validator checks, and docs so boundaries are explicit before implementation.
3. Drift path: edit this draft before approval freeze; after freeze, use variance or amendment for changes to module ownership, route mandatory conditions, historical-artifact immutability, or evidence ownership.
4. Reinterpretation guard: implementation must not make `module:artifact-style` always required for routine small/medium planning unless an amendment is approved.

## Implementation Approach

Implement in one orchestration thread. Start with policy ownership and routing so all later template and validation changes have a clear source of truth. Then update templates from source blocks, regenerate generated templates, and add validator checks that enforce the new structural contracts.

Keep the new style module small. It should define durable artifact readability rules and examples, not a broad writing manual. Baseline guidance outside the module should be only a short reminder that final artifacts must remove authoring scaffolds, resolve required decisions, and use scannable structures.

Do not modify already implemented July 2 and July 3 work-item specs, plans, or snapshots. Treat their review findings as input evidence for future-facing policy and template changes.

## Change Surfaces

Expected edits:

1. `.agents/skills/dev-doc-harness/references/artifact-style.md`: create the new canonical style module.
2. `.agents/skills/dev-doc-harness/references/policy-architecture.md`: add the module catalog entry, router input guidance, dependency boundaries, and route-budget wording for conditional style loading.
3. `.agents/skills/dev-doc-harness/SKILL.md`: update operation routes so large anchor specs require style guidance, large or hard-to-scan artifacts load it, and routine small/medium routes keep a compact baseline.
4. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`: add the short baseline readability block and cross-reference style and evidence without duplicating their rules.
5. `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`: add only narrow clarification if needed so mutable external evidence used in specs or reports is clearly preserved under existing evidence rules.
6. `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`: replace non-canonical model-policy example wording.
7. `.agents/skills/dev-doc-harness/assets/templates/blocks/`: update primary template source blocks for style cues, readiness, model-policy source, validation IDs, approval metadata, and controlled states.
8. `.agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md`: add decision IDs and trace fields.
9. `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`: tighten amendment IDs, approval evidence, and final-state fields where practical.
10. `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`: tighten variance IDs, class choices, approval evidence, and final-state fields where practical.
11. `.agents/skills/dev-doc-harness/assets/templates/*.md`: regenerate generated templates and manually update standalone templates.
12. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: add structural checks for the style module, policy-reference coverage, block usage, controlled placeholder or visible-prompt regressions, generated-template freshness, and historical-spec exclusion review where practical.
13. `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md`: add concise discoverability for artifact-style guidance.
14. `.agents/skills/dev-doc-harness/docs/releases/0.4+.md`: update if new distributable surfaces must be noted for release consistency.
15. `CHANGELOG.md`: add planning and implementation entries at the required commit points.

Stable interfaces:

1. Existing lifecycle, naming, freeze, model, evidence, release, and quality rule ownership remains stable.
2. Existing generated-template assembly command names remain stable.
3. Existing validator command remains `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

Changed interfaces:

1. A new canonical module ID `module:artifact-style` and new `rule:style.*` IDs become current harness references.
2. Operation routing gains mandatory style loading for large anchor specs and large or hard-to-scan documents.
3. Template policy references and validation expectations expand to include artifact-style guidance where relevant.

Implementation boundaries:

1. Historical implemented specs, plans, and snapshots from the three reviewed work items stay out of scope because they are frozen implementation history.
2. Handoff snapshot schema stays out of scope because it needs separate lifecycle design.
3. Changelog legacy heading normalization stays out of scope because it is not needed to deliver artifact-style guidance.

## Model and Sub-agent Strategy

Current orchestration:

1. Model/profile and reasoning effort if known: Codex desktop thread; exact model/profile and reasoning effort are not exposed in repository artifacts.

Fit assessment:

1. Complexity: Medium. The work touches canonical references, templates, validation, and operator-facing docs, but no runtime product code.
2. Risk and blast radius: Medium. It affects future harness planning behavior and artifact quality; overreach could make routine planning heavier.
3. Ambiguity: Low to medium. Operator has selected approach 2 and clarified the conditional style-routing requirements.
4. Budget and latency fit: Acceptable for one orchestration thread. The prior three read-only extra-high sub-agent reviews already supplied independent scrutiny for planning.

Recommended orchestration change:

1. Use the active repository policy, `economy-default`.
2. Use stronger reasoning for final policy/template review if the environment exposes a reasoning choice, because this changes canonical harness policy boundaries.

Sub-agents:

1. No write-capable implementation sub-agents are proposed. The implementation surfaces are tightly coupled and should be integrated by the orchestration thread.
2. Optional read-only final review is allowed after the implementation diff exists if it improves confidence and fits the active model policy. Fresh confirmation is required before using more than one additional reviewer, using write-capable sub-agents, or exceeding the approved strategy.

Planning review already performed:

1. Purpose: Three independent read-only review passes on durable artifacts, template surfaces, and policy architecture.
2. Context strategy: Curated prompts and curated repository artifacts.
3. Input context: Current harness references, templates, recent work-item specs/plans/snapshot, validator output, and operator scope.
4. Output artifact: Review findings reconciled into this spec and plan.
5. Model policy: Operator-requested extra-high review wave; exact model/profile not exposed.
6. Reasoning effort: Extra-high by operator request for review wave.
7. Selection reason: Review quality and policy/template blast radius.
8. Parallel execution: Yes, three concurrent read-only reviewers.
9. Blast radius if wrong: Medium; missed ambiguity could make future planning artifacts harder to consume.

Optional final review sub-agent:

1. Purpose: Review the completed diff for over-broad style policy, route-budget drift, duplicated evidence policy, and historical-artifact edits.
2. Context strategy: Curated prompt.
3. Input context: Approved spec, approved plan, architecture snapshot, implementation diff, validator output, and changed reference/template files.
4. Output artifact: Findings summarized in the completion report or variance log if material.
5. Model policy: Active repository policy unless operator changes it.
6. Model class/profile: Latest strongest available profile if exposed; otherwise inherited model.
7. Reasoning effort: High or extra-high if available, because this is final review of canonical policy boundaries.
8. Selection reason: Independent review can catch subtle route and ownership regressions.
9. Parallel execution: No; run after the implementation diff exists.
10. Blast radius if wrong: Medium; missed regressions could confuse future harness users.

## Task Plan

- [ ] `T-001` Dependencies: Approved planning package; create `.agents/skills/dev-doc-harness/references/artifact-style.md` with `module:artifact-style`, owned `rule:style.*` IDs, and concise guidance for artifact readability, structure choice, template prompts, examples/placeholders, controlled states, traceability density, and final cleanup; Traces: `REQ-001`, `REQ-003`, `RISK-001`, `RISK-009`.
- [ ] `T-002` Dependencies: `T-001`; update `policy-architecture.md`, `SKILL.md`, README, and operator note so style guidance is discoverable, optional for routine small/medium work, mandatory for large anchor specs, required for large or hard-to-scan artifacts, and distinct from `module:architecture` work-item architecture decisions; Traces: `REQ-002`, `REQ-003`, `RISK-002`, `RISK-003`, `RISK-008`, `RISK-009`.
- [ ] `T-003` Dependencies: `T-001`, `T-002`; update `durable-planning-quality.md` with a short baseline readability block outside the style module, including final artifact content, no unresolved required decisions, controlled deferrals, and scannable structures; Traces: `REQ-002`, `REQ-006`, `RISK-002`.
- [ ] `T-004` Dependencies: `T-001` through `T-003`; update template source blocks for concise style cues, stronger readiness checks, controlled final-state fields, model-policy source notation, validation IDs, conditional style loading, and reduced conversational prompt residue; Traces: `REQ-004`, `REQ-005`, `REQ-006`, `REQ-007`, `REQ-009`, `RISK-004`.
- [ ] `T-005` Dependencies: `T-001`; update `subagent-role-examples.md`, model-strategy prompts, and evidence cross-references so model-policy examples use canonical selectors and mutable external evidence routes through `module:evidence`; Traces: `REQ-007`, `REQ-008`, `RISK-006`.
- [ ] `T-006` Dependencies: `T-004`; update standalone `architecture-snapshot.md`, `plan-amendment.md`, and `variance-log.md` templates for decision, amendment, variance, trace, approval, and supersession fields with final values instead of authoring instructions; Traces: `REQ-005`, `REQ-009`.
- [ ] `T-007` Dependencies: `T-004`, `T-006`; run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`, inspect regenerated templates, and correct source blocks until generated outputs are current; Traces: `REQ-004`, `REQ-010`.
- [ ] `T-008` Dependencies: `T-001` through `T-007`; update `test_harness_policy.py` with structural checks for artifact-style ownership, template policy-reference coverage, block usage, controlled placeholder or visible-prompt regressions, generated-template freshness, and high-signal historical-spec exclusion review; Traces: `REQ-010`, `REQ-011`, `RISK-005`, `RISK-007`.
- [ ] `T-009` Dependencies: `T-001` through `T-008`; update `.agents/skills/dev-doc-harness/docs/releases/0.4+.md` if release validation or distributable-package clarity requires it; Traces: `REQ-010`.
- [ ] `T-010` Dependencies: `T-001` through `T-009`; update `CHANGELOG.md` with `2026-07-03_artifact-style-guidance -- add artifact style module`; Traces: `REQ-010`.
- [ ] `T-011` Dependencies: `T-010`; run the full validation plan, verify historical implemented specs are untouched, perform final diff review, optionally run the planned read-only final review sub-agent if useful, and create the implementation commit with the approved subject; Traces: all acceptance criteria.

## Planned commits

Planning approval commit:

1. Planned subject: `spec: artifact-style-guidance -- approve artifact style plan`.
2. Changelog title or snippet: `2026-07-03_artifact-style-guidance -- approve artifact style plan`.
3. Notes: Approval commit for `spec_artifact-style-guidance.md`, `plan_artifact-style-guidance.md`, `snapshots/architecture.snapshot.md`, and `CHANGELOG.md`.

Implementation commit:

1. Planned subject: `docs: artifact-style-guidance -- add artifact style module`.
2. Changelog title or snippet: `2026-07-03_artifact-style-guidance -- add artifact style module`.
3. Notes: Implementation commit for artifact style module, policy architecture, router guidance, quality/evidence/model supporting text, templates, validator, README, operator note, release notes if needed, and changelog.

## Validation Plan

| ID | Command or check | Expected result |
|---|---|---|
| `V-001` | `rg -n "module:artifact-style|rule:style\\." .agents/skills/dev-doc-harness/references/artifact-style.md` | Matches show the new module and owned style rules; covers `AC-001`. |
| `V-002` | `rg -n "module:artifact-style|artifact-style|artifact readability" .agents/skills/dev-doc-harness/references/policy-architecture.md .agents/skills/dev-doc-harness/references/durable-planning-quality.md` | Matches show catalog, boundary, router-input, and baseline quality guidance; covers `AC-002`. |
| `V-003` | `rg -n "large anchor|large.*artifact-style|hard-to-scan|readability risk" .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/references/policy-architecture.md` | Matches show mandatory style loading for large anchor specs and materially large or hard-to-scan artifacts; covers `AC-003`. |
| `V-004` | `rg -n "unresolved.*decision|deferred.*owner|final artifact|scannable|conversation|authoring" .agents/skills/dev-doc-harness/assets/templates/blocks .agents/skills/dev-doc-harness/assets/templates/*work-item*.md` | Matches show template-level style cues and readiness checks; covers `AC-004`, `AC-006`, and `AC-008`. |
| `V-005` | `rg -n "DEC-001|Source spec|Validation cues|Superseded by: None" .agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md` | Matches show decision ID, trace, validation, and final-state fields; covers `AC-005` and `AC-010`. |
| `V-006` | `rg -n "AMD-001|VAR-001|Approval|Superseded by: None|Variance class" .agents/skills/dev-doc-harness/assets/templates/plan-amendment.md .agents/skills/dev-doc-harness/assets/templates/variance-log.md` | Matches show amendment and variance templates have stronger IDs and final-state fields; covers `AC-005` and `AC-008`. |
| `V-007` | `rg -n "standard-review" .agents/skills/dev-doc-harness/references/subagent-role-examples.md .agents/skills/dev-doc-harness/assets/templates` | No matches; `rg` exits 1 when no matches are found; covers `AC-007`. |
| `V-008` | `rg -n "rule:evidence.preservation|module:evidence|mutable external|external evidence" .agents/skills/dev-doc-harness/references/artifact-style.md .agents/skills/dev-doc-harness/references/durable-planning-quality.md .agents/skills/dev-doc-harness/assets/templates` | Matches show evidence durability routes to the evidence owner; covers `AC-009`. |
| `V-009` | `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` | Exits 0 and prints that all assembled templates are current; covers `AC-012`. |
| `V-010` | `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | All checks print `PASS` and command exits 0, including new style and template checks; covers `AC-011`. |
| `V-011` | `git diff --check` | No whitespace errors. |
| `V-012` | `git diff --name-only -- docs/work-items/2026-07-02_orchestration-sizing-large-templates docs/work-items/2026-07-02_template-block-assembly docs/work-items/2026-07-03_work-item-architecture-decisions` | No output; historical implemented specs, plans, and snapshots are untouched; covers `AC-013`. |
| `V-013` | `git status --short` | Before implementation commit, only approved implementation targets and `CHANGELOG.md` are modified. |

Every validation entry states the expected signal before implementation starts.

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

Likely local variance that may proceed with a note in the completion report:

1. Exact `rule:style.*` rule names change while preserving the module boundary and acceptance coverage.
2. Baseline guidance lands in `durable-planning-quality.md`, `SKILL.md`, templates, or a combination, as long as minimal direction is visible without loading `module:artifact-style`.
3. Validator style checks use a narrower high-signal pattern set than the plan examples to avoid false positives.
4. Release notes do not need updates if validation and release policy do not require them.

Variance requiring operator approval before continuing:

1. Making `module:artifact-style` mandatory for every routine small/medium planning route.
2. Removing mandatory style loading for large anchor specs.
3. Duplicating evidence preservation policy in the style module instead of routing through `module:evidence`.
4. Rewriting already implemented July 2 or July 3 specs, plans, or snapshots.
5. Turning validation into semantic prose grading.
6. Creating a broad repository documentation style guide outside the harness package.
7. Changing freeze-gate approval or implementation-authorization rules.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Draft review status: Operator approved the staged planning package on 2026-07-03.
Approval commit status: Approved for the planning freeze commit.
Post-freeze implementation authorization status: Not authorized; implementation requires a fresh explicit operator instruction after the approval commit.

## Plan readiness checklist

- [x] Input artifacts and relevant repository context have been read and listed.
- [x] Every spec requirement and acceptance criterion has at least one task and one validation path.
- [x] Risks, scope boundaries, interfaces, and documentation decisions are either covered by tasks or explicitly marked as no-op with a reason.
- [x] Task detail is sufficient for a fresh implementation agent or delegated sub-agent to execute its assigned part without inventing task order, file scope, validation, or documentation steps.
- [x] Validation entries have exact commands, manual checks, review findings, or operator acceptance paths with expected signals.
- [x] Planned commits and changelog title snippets are synchronized.
- [x] Variance handling is clear for likely implementation drift.
- [x] The work still fits one orchestration thread with a bounded sub-agent strategy. If it does not, split, re-scope, or escalate to large/phased handling before freeze.
- [x] Sub-agent strategy follows `module:models`, including de-facto reporting of the planning review wave.
- [x] No unresolved placeholders, unresolved required decisions, missing required sections, or ownerless deferrals remain before approval or handoff.

## Completion criteria

- Acceptance criteria in `spec_artifact-style-guidance.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- The frozen plan had enough detail for the implementation thread and optional final reviewer to proceed safely.
- Execution remained within one orchestration thread with the approved bounded sub-agent strategy; otherwise the work was split, re-scoped, or amended before implementation.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present when nontrivial drift occurs.
- De-facto sub-agent use is reported, including the three planning reviewers and any optional final reviewer used during implementation.
- Historical implemented specs, plans, and snapshots from the reviewed July 2 and July 3 packages remain unmodified.

## Approval

- Status: Approved
- Superseded by: None
