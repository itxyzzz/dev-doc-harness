# Work-Item Architecture Decisions Plan

Work ID: `2026-07-03_work-item-architecture-decisions`
Short ID: `work-item-architecture-decisions`
Status: Approved
Harness release: `0.4+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `module:architecture`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:lifecycle.documentation-matrix`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Input Artifacts

Read these before finalizing implementation planning:

1. Approved spec: `spec_work-item-architecture-decisions.md`.
2. Required snapshots or deltas: `snapshots/architecture.snapshot.md`.
3. Relevant repository files, tests, docs, logs, or review comments:
   - Root `AGENTS.md`
   - `.agents/skills/dev-doc-harness/SKILL.md`
   - `.agents/skills/dev-doc-harness/VERSION`
   - `.agents/skills/dev-doc-harness/references/artifact-contract.md`
   - `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
   - `.agents/skills/dev-doc-harness/references/naming-conventions.md`
   - `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
   - `.agents/skills/dev-doc-harness/references/policy-architecture.md`
   - `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
   - `.agents/skills/dev-doc-harness/assets/templates/blocks/`
   - `.agents/skills/dev-doc-harness/assets/templates/assemblies/`
   - `.agents/skills/dev-doc-harness/assets/templates/*.md`
   - `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`
   - `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
   - `README.md`
   - `.agents/skills/dev-doc-harness/docs/operator-note.md`
   - `CHANGELOG.md`
   - Historical architecture snapshots listed in the spec.
4. Unresolved implementation context to confirm before editing: None identified after repository-context review.

## Spec Traceability

Map the approved spec to execution without restating the spec. Use compact numbered lists or short blocks; avoid wide tables when cells need more than a few words.

Requirement coverage:

1. `REQ-001`: implemented by `T-001`, `T-002`, `T-003`, `T-004`, and `T-005`; verified by `V-001`, `V-002`, `V-003`, and `AC-001` through `AC-005`.
2. `REQ-002`: implemented by `T-001`, `T-003`, and `T-004`; verified by `V-001`, `V-002`, and `AC-001` through `AC-003`.
3. `REQ-003`: implemented by `T-001`, `T-002`, `T-003`, `T-005`, and `T-006`; verified by `V-002`, `V-003`, `V-004`, and `AC-003` through `AC-005`.
4. `REQ-004`: implemented by `T-002`, `T-005`, and `T-006`; verified by `V-003`, `V-004`, and `AC-004` through `AC-005`.
5. `REQ-005`: implemented by `T-004` and `T-008`; verified by `V-005`, `V-009`, and `AC-006` through `AC-008`.
6. `REQ-006`: implemented by `T-001`, `T-004`, `T-007`, and `T-008`; verified by `V-005`, `V-006`, `V-007`, and `AC-006` through `AC-009`.
7. `REQ-007`: implemented by `T-008`, `T-009`, `T-010`, and `T-011`; verified by `V-008` through `V-012` and `AC-008` through `AC-011`.
8. `REQ-008`: implemented by `T-010` and `T-011`; verified by `V-011`, `V-012`, and `AC-011`.

Acceptance coverage:

1. `AC-001`: `T-001`, `T-002`, `V-001`.
2. `AC-002`: `T-001`, `T-003`, `T-004`, `V-001`, `V-002`.
3. `AC-003`: `T-003`, `T-009`, `V-002`, `V-008`.
4. `AC-004`: `T-005`, `T-009`, `V-003`, `V-008`.
5. `AC-005`: `T-002`, `T-005`, `V-003`, `V-004`.
6. `AC-006`: `T-004`, `T-008`, `V-005`, `V-009`.
7. `AC-007`: `T-006`, `T-007`, `V-006`.
8. `AC-008`: `T-008`, `T-009`, `V-009`, `V-010`.
9. `AC-009`: `T-007`, `V-007`.
10. `AC-010`: `T-009`, `V-008`.
11. `AC-011`: `T-010`, `T-011`, `V-011`, `V-012`.

Risk and boundary coverage:

1. `RISK-001`: `T-001` sets conditional snapshot triggers; `T-003` and `T-004` preserve not-applicable and deferred matrix choices.
2. `RISK-002`: `T-003` adds spec prompts; `T-004` adds the dedicated snapshot template.
3. `RISK-003`: `T-005` updates plan and phase-plan templates to consume architecture as input.
4. `RISK-004`: `T-001` keeps trigger ownership in lifecycle; `T-006` keeps router wording clear.
5. `RISK-005`: `T-004` and `T-007` state `ARCHITECTURE.md` is future work.
6. `RISK-006`: `T-008` adds structural validation only.

## Implementation Approach

Make `module:lifecycle` the canonical owner for the work-item architecture decision flow because it already owns work-item layout, snapshots, documentation matrix, immutable snapshots, and variance handling. Add a new lifecycle rule for work-item architecture decisions rather than overloading `module:architecture`, which already owns policy architecture.

Update `module:quality` to clarify handoff expectations: specs preserve architectural decisions; phase plans and implementation plans consume those decisions. Missing architecture before freeze is a draft-spec or draft-snapshot issue. High-impact architecture drift after freeze is a variance/amendment issue.

Add a dedicated work-item architecture snapshot template as a normal flat template. The primary spec and plan templates should still be maintained through blocks and assemblies. Insert concise architecture-decision prompts into spec blocks and architecture-input prompts into plan blocks, then regenerate flat templates through `assemble_templates.py --write`.

Keep operator-facing documentation short. README and operator note should say that architecture snapshots are work-item-bound and that long-lived durable docs such as `ARCHITECTURE.md` are future work. Avoid introducing ADR directories, durable architecture document workflows, or repository-wide architecture lifecycle rules in this implementation.

## Change Surfaces

Expected edits:

1. `.agents/skills/dev-doc-harness/references/artifact-contract.md`: add lifecycle rule ownership and guidance for work-item architecture decisions, snapshot triggers, documentation matrix states, and variance interaction.
2. `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`: clarify spec and phase-plan handoff quality for architecture decisions.
3. `.agents/skills/dev-doc-harness/SKILL.md`: make architecture snapshot routing discoverable for spec, large anchor, phase plan, and execution/variance operations.
4. `.agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md`: add a flat work-item architecture snapshot template.
5. `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.*.md`: add architecture decision prompts and documentation matrix wording.
6. `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.*.md`: add architecture input and drift-handling prompts.
7. `.agents/skills/dev-doc-harness/assets/templates/assemblies/*.json`: include any new blocks in generated template order.
8. `.agents/skills/dev-doc-harness/assets/templates/*.md`: regenerate flat templates from source blocks.
9. `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: add lightweight structural checks for architecture decision rule, snapshot template, docs wording, generated-template freshness, and no active `ARCHITECTURE.md` workflow.
10. `README.md`: add concise operator-facing work-item architecture explanation.
11. `.agents/skills/dev-doc-harness/docs/operator-note.md`: add package-local work-item architecture explanation.
12. `CHANGELOG.md`: add newest-first implementation entry before commit.

Stable interfaces:

1. Large/phased planning sequence remains unchanged.
2. Freeze-gate behavior remains unchanged.
3. Active repository model policy remains `economy-default`.
4. Published primary template paths remain unchanged.
5. `deltas/architecture-summary.delta.md` remains optional and does not become a durable-doc workflow.

Changed interfaces:

1. Work-item architecture snapshot trigger guidance becomes explicit.
2. Specs gain architecture decision prompts.
3. Plans gain architecture input/reference prompts.
4. A reusable architecture snapshot template becomes available.

Implementation boundaries:

1. Do not create or require `ARCHITECTURE.md`.
2. Do not add an ADR directory or ADR numbering system.
3. Do not change `.agents/skills/dev-doc-harness/VERSION`.
4. Do not rewrite frozen historical artifacts.
5. Do not turn validation into a semantic check of whether a future work item correctly classified its architecture needs.

## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this work item or phase.

Current orchestration:

1. Model/profile and reasoning effort if known: Codex desktop thread; exact model/profile and reasoning effort not exposed in repository artifacts.

Fit assessment:

1. Complexity: Medium. The work touches lifecycle policy, quality policy, router guidance, generated templates, one new snapshot template, validation, README, and operator note.
2. Risk and blast radius: Medium. It changes planning behavior but no runtime product behavior. The main risk is confusing work-item architecture with repository-level durable docs.
3. Ambiguity: Low to medium. The operator selected approach 2 and clarified the work-item-only boundary; implementation wording still needs care.
4. Budget and latency fit: Acceptable for one orchestration thread with one bounded read-only reviewer if available.

Recommended orchestration change:

1. Use the active repository policy, `economy-default`. Escalate to a latest strongest model class for final architecture-policy review only if implementation reveals subtle lifecycle conflicts.

Sub-agents:

1. Use one optional read-only reviewer after the implementation diff exists. If sub-agent tooling is unavailable or coordination cost is too high, the orchestration thread performs the same review and reports the fallback.

Sub-agent `architecture-policy-review`:

1. Purpose: Review the implemented lifecycle, quality, router, template, validator, and docs changes for ambiguous architecture ownership or accidental durable-doc workflow creation.
2. Context strategy: `curated prompt`.
3. Input context: Approved spec, architecture snapshot, plan, changed diff, `artifact-contract.md`, `durable-planning-quality.md`, `SKILL.md`, template blocks, generated templates, README, operator note, and validator output.
4. Output artifact: Review findings summarized in the implementation completion report or variance log if material.
5. Model policy: Active repository policy, `economy-default`.
6. Model class/profile: Policy-relative standard for the first review; latest strongest if the review finds subtle lifecycle or architecture ownership conflicts.
7. Reasoning effort: Medium; high only if conflicting policy guidance appears.
8. Selection reason: Independent read-only review reduces risk of confusing work-item architecture snapshots with durable repository architecture documents.
9. Parallel execution: No; run after implementation diff and validation output exist.
10. Blast radius if wrong: Medium; missed ambiguity could confuse future planning packages.

## Task Plan

Write one checkbox per implementation, test, validation, documentation, or handoff step. Tasks should be SMART.

- [ ] `T-001` Dependencies: Approved planning package; update `.agents/skills/dev-doc-harness/references/artifact-contract.md` with a new lifecycle-owned work-item architecture decision rule, including snapshot triggers, not-applicable/deferred matrix states, plan consumption, and post-freeze variance/amendment behavior; Traces: `REQ-001`, `REQ-002`, `REQ-003`, `REQ-006`, `RISK-001`, `RISK-004`, `RISK-005`.
- [ ] `T-002` Dependencies: `T-001`; update `.agents/skills/dev-doc-harness/references/durable-planning-quality.md` so spec quality includes preserving architectural decisions and phase-plan quality forbids silently reinterpreting frozen architecture; Traces: `REQ-001`, `REQ-003`, `REQ-004`, `RISK-003`.
- [ ] `T-003` Dependencies: `T-001`; update spec template source blocks and assemblies to add architecture decision prompts, architecture snapshot trigger guidance, and updated documentation matrix wording for small/medium and large/phased specs; Traces: `REQ-001`, `REQ-002`, `REQ-003`, `RISK-001`, `RISK-002`.
- [ ] `T-004` Dependencies: `T-001`, `T-003`; add `.agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md` as a work-item-bounded snapshot template with fields for drivers, constraints, selected approach, affected boundaries, rejected alternatives, validation cues, and future durable-doc boundary; Traces: `REQ-002`, `REQ-005`, `REQ-006`, `RISK-002`, `RISK-005`.
- [ ] `T-005` Dependencies: `T-001`, `T-002`; update plan and phase-plan source blocks and assemblies to list architecture artifacts as inputs, reference architectural decisions in traceability/change surfaces, and route missing or changed architecture to draft updates or amendments; Traces: `REQ-003`, `REQ-004`, `RISK-003`.
- [ ] `T-006` Dependencies: `T-001` through `T-005`; update `.agents/skills/dev-doc-harness/SKILL.md` router guidance so spec drafting, large anchor specs, phase plans, and variance/execution routes make work-item architecture snapshots discoverable without adding a new durable-doc route; Traces: `REQ-004`, `REQ-006`, `RISK-004`, `RISK-005`.
- [ ] `T-007` Dependencies: `T-001`, `T-004`, `T-006`; update `README.md` and `.agents/skills/dev-doc-harness/docs/operator-note.md` with concise work-item architecture guidance and explicit `ARCHITECTURE.md` future-work boundary; Traces: `REQ-006`, `RISK-005`.
- [ ] `T-008` Dependencies: `T-001` through `T-007`; update `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` with structural checks for the lifecycle rule, architecture snapshot template, docs discoverability, generated-template freshness, and no active `ARCHITECTURE.md` workflow; Traces: `REQ-005`, `REQ-006`, `REQ-007`, `RISK-006`.
- [ ] `T-009` Dependencies: `T-003`, `T-005`, `T-008`; run `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write`, inspect regenerated flat templates, and make source-block corrections until generated templates are current and validation passes; Traces: `REQ-007`.
- [ ] `T-010` Dependencies: `T-001` through `T-009`; update `CHANGELOG.md` with `2026-07-03_work-item-architecture-decisions -- make architecture snapshots first-class`; Traces: `REQ-008`, `AC-011`.
- [ ] `T-011` Dependencies: `T-010`; run the full validation plan, perform final diff review, run the optional `architecture-policy-review` sub-agent if available and useful, then commit with the approved implementation subject; Traces: `REQ-007`, `REQ-008`.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets. Update this section before committing if implementation changes the subject wording.

Planning approval commit:

1. Planned subject: `spike: work-item-architecture-decisions -- approve architecture-decision flow plan`.
2. Changelog title or snippet: `2026-07-03_work-item-architecture-decisions -- approve architecture-decision flow plan`.
3. Notes: Approval commit for `spec_work-item-architecture-decisions.md`, `plan_work-item-architecture-decisions.md`, `snapshots/architecture.snapshot.md`, and `CHANGELOG.md`.

Implementation commit:

1. Planned subject: `docs: work-item-architecture-decisions -- make architecture snapshots first-class`.
2. Changelog title or snippet: `2026-07-03_work-item-architecture-decisions -- make architecture snapshots first-class`.
3. Notes: Implementation commit for lifecycle, quality, router, template blocks, generated templates, architecture snapshot template, validator, README, operator note, and changelog.

## Validation Plan

| Command | Expected result |
|---|---|
| `rg -n "work-item architecture|architecture snapshot|architecture decisions" .agents/skills/dev-doc-harness/references/artifact-contract.md .agents/skills/dev-doc-harness/references/durable-planning-quality.md .agents/skills/dev-doc-harness/SKILL.md` | Matches show lifecycle owns the architecture decision rule, quality preserves handoff expectations, and router guidance is discoverable; covers `AC-001`, `AC-005`, and `AC-007`. |
| `rg -n "Architecture Decisions|architecture snapshot|drivers|constraints|rejected alternatives" .agents/skills/dev-doc-harness/assets/templates/*work-item-spec.md .agents/skills/dev-doc-harness/assets/templates/blocks` | Generated spec templates and source blocks contain architecture decision prompts; covers `AC-003`. |
| `rg -n "architecture.*input|architecture.*snapshot|amendment|reinterpret" .agents/skills/dev-doc-harness/assets/templates/*plan*.md .agents/skills/dev-doc-harness/assets/templates/blocks` | Generated plan templates and source blocks treat architecture as input and route drift to draft updates or amendments; covers `AC-004` and `AC-005`. |
| `Test-Path .agents/skills/dev-doc-harness/assets/templates/architecture-snapshot.md` | Returns `True`; covers `AC-006`. |
| `rg -n "ARCHITECTURE.md" .agents/skills/dev-doc-harness README.md AGENTS.md` | Matches, if any, state durable repository-level architecture docs are future work and do not instruct agents to create or update `ARCHITECTURE.md`; covers `AC-009`. |
| `rg -n "architecture-snapshot.md|work-item architecture|ARCHITECTURE.md" README.md .agents/skills/dev-doc-harness/docs/operator-note.md` | Operator-facing docs explain work-item architecture snapshots and future durable-doc boundary; covers `AC-007` and `AC-009`. |
| `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` | Exits 0 and prints that all assembled templates are current; covers `AC-010`. |
| `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | All checks print `PASS` and command exits 0, including generated-template freshness and new architecture-decision structural checks; covers `AC-008`. |
| `rg -n "2026-07-03_work-item-architecture-decisions -- make architecture snapshots first-class" CHANGELOG.md` | Changelog includes the implementation title snippet before implementation commit; covers `AC-011`. |
| `git diff --check` | No whitespace errors. |
| `git status --short` | Before implementation commit, only approved implementation targets and `CHANGELOG.md` are modified. |

Every validation entry states the expected signal before implementation starts. Add command exit behavior, important output text, manual observation, review criterion, or operator acceptance condition as applicable.

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

Likely local variance that may proceed with a note in the completion report:

1. The new architecture decision rule name changes slightly during implementation to avoid collision with existing `module:architecture` terminology.
2. The exact source block filename order changes while preserving generated template order and manifest clarity.
3. Validator checks cover discoverability through slightly different structural patterns than listed above.
4. README and operator note wording stays shorter than planned while preserving the work-item-only boundary.

Variance requiring operator approval before continuing:

1. Adding a required `ARCHITECTURE.md` or repository-level durable architecture document workflow.
2. Adding ADR directories, cross-work architecture registries, or durable-doc lifecycle rules.
3. Making architecture snapshots mandatory for every substantial work item.
4. Allowing plans or phase plans to own architecture decisions that are absent from the spec or snapshot.
5. Changing the large/phased freeze sequence or implementation authorization rules.
6. Removing the architecture snapshot template from scope.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this plan.

Draft review status: Approved by operator on 2026-07-03.
Approval commit status: Approved for freeze; commit hash will be reported in the checkpoint output.
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
- [x] Sub-agent strategy follows `module:models`, or `Sub-agents: None` has a brief fit rationale.
- [x] No unresolved placeholders remain before approval or handoff.

## Completion criteria

- Acceptance criteria in `spec_work-item-architecture-decisions.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- The frozen plan had enough detail for each assigned execution part or delegated sub-agent to proceed safely.
- Execution remained within one orchestration thread with a bounded sub-agent strategy; otherwise the work was split, re-scoped, or escalated before implementation.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current when nontrivial drift occurs.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
