# Template Block Assembly Plan

Work ID: `2026-07-02_template-block-assembly`
Short ID: `template-block-assembly`
Status: Approved
Harness release: `0.4+`
Schema: `schema:plan.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:freeze-gate`, `module:release`, `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:release.package-boundary`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Input Artifacts

Read these before finalizing implementation planning:

- Approved spec: `spec_template-block-assembly.md`
- Required snapshots or deltas: None.
- Relevant repository files, tests, docs, logs, or review comments:
  - `.agents/skills/dev-doc-harness/SKILL.md`
  - `.agents/skills/dev-doc-harness/references/artifact-contract.md`
  - `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
  - `.agents/skills/dev-doc-harness/references/naming-conventions.md`
  - `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
  - `.agents/skills/dev-doc-harness/references/policy-architecture.md`
  - `.agents/skills/dev-doc-harness/references/release-policy.md`
  - `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
  - `.agents/skills/dev-doc-harness/VERSION`
  - `.agents/skills/dev-doc-harness/docs/releases/0.3.0.md`
  - `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
  - `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
  - `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
  - `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
  - `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
  - `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`
  - `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
  - `README.md`
  - `CHANGELOG.md`
  - `docs/work-items/2026-07-02_orchestration-sizing-large-templates/spec_orchestration-sizing-large-templates.md`
  - `docs/work-items/2026-07-02_orchestration-sizing-large-templates/plan_orchestration-sizing-large-templates.md`
- Unresolved implementation context to confirm before editing: None identified.

## Spec Traceability

Map the approved spec to execution without restating the spec.

Requirement coverage:

- `REQ-001`: implemented by `T-001`, `T-002`, and `T-003`; verified by `V-001`, `V-002`, and `AC-001`.
- `REQ-002`: implemented by `T-002`; verified by `V-002` and `AC-002`.
- `REQ-003`: implemented by `T-003`, `T-004`, `T-005`, and `T-006`; verified by `V-003`, `V-004`, and `AC-003`.
- `REQ-004`: implemented by `T-003`, `T-004`, and `T-005`; verified by `V-004`, `V-005`, and `AC-004` through `AC-005`.
- `REQ-005`: implemented by `T-006`; verified by `V-006`.
- `REQ-006`: implemented by `T-006` and `T-007`; verified by `V-006` and `V-007`.
- `REQ-007`: implemented by `T-007`; verified by `V-007` and `V-010`.
- `REQ-008`: implemented by `T-008`; verified by `V-008`.
- `REQ-009`: implemented by `T-009`; verified by `V-009`.
- `REQ-010`: implemented by `T-007`, `T-010`, and `T-011`; verified by `V-010`.
- `REQ-011`: implemented by `T-010`; verified by `V-011`.
- `REQ-012`: implemented by `T-003`, `T-004`, `T-005`, and `T-010`; verified by `V-012`.

Acceptance coverage:

- `AC-001`: `T-001`, `T-002`, `V-001`.
- `AC-002`: `T-002`, `V-002`.
- `AC-003`: `T-003`, `T-006`, `V-003`.
- `AC-004`: `T-003`, `T-004`, `T-005`, `V-004`.
- `AC-005`: `T-004`, `T-005`, `V-005`.
- `AC-006`: `T-006`, `V-006`.
- `AC-007`: `T-007`, `V-007`, `V-010`.
- `AC-008`: `T-008`, `V-008`.
- `AC-009`: `T-009`, `V-009`.
- `AC-010`: `T-010`, `T-011`, `V-010`.
- `AC-011`: `T-010`, `V-011`.
- `AC-012`: `T-003`, `T-004`, `T-005`, `T-010`, `V-012`.

Risk and boundary coverage:

- `RISK-001`: `T-006` provides `--list`, and `T-009` documents the workflow.
- `RISK-002`: `T-001` sets a small block taxonomy; `T-003` through `T-005` avoid splitting sections that are not worth sharing.
- `RISK-003`: `T-008` creates a non-mutating hook.
- `RISK-004`: `T-008` places hook files outside `.agents/`; `T-009` documents package boundary.
- `RISK-005`: `T-006` and `T-007` separate non-recursive assembly checking from full validation.
- `RISK-006`: `T-002` through `T-005` keep large and phase-specific blocks distinct.
- `RISK-007`: `T-002` and `T-006` use a simple standard-library parseable manifest format.
- `RISK-008`: `T-010`, `V-011`, and `V-010` keep release marker updates synchronized with validation.
- `RISK-009`: `T-003` through `T-005` use numbered lists selectively while preserving checkboxes and matrix tables.

## Implementation Approach

Introduce template assembly as a maintainer authoring layer while preserving the existing flat template interface. The block and manifest files are the source of truth for maintainers, but agents continue to consume the assembled Markdown files already routed by `SKILL.md`.

Use explicit manifests rather than relying on directory sorting for assembly. Filename order still matters for human browsing, so block names use a stable grammar with a three-digit order field. Manifests make the large/phased differences visible by listing common blocks beside large anchor or phase-plan specific blocks.

Implement the assembler with Python standard library only. `--check` must be non-recursive and only compare generated text to checked-in flat templates. `--write` writes templates, runs the non-recursive check, then runs `test_harness_policy.py`. The validator calls only the non-recursive check path.

Keep local hook support outside `.agents/`. The hook runs the validator only and fails with instructions when assembly drift exists; it does not mutate files during commit.

## Change Surfaces

Expected edits:

- `.agents/skills/dev-doc-harness/assets/templates/blocks/`: create ordered block files for shared and template-specific sections.
- `.agents/skills/dev-doc-harness/assets/templates/assemblies/`: create explicit manifest files for the four primary templates.
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`: regenerate as a flat template with generated-source note.
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`: regenerate as a flat template with generated-source note.
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`: regenerate as a flat template with generated-source note.
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`: regenerate as a flat template with generated-source note.
- `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`: create assembly command.
- `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: add assembly freshness check and any necessary block or manifest validation.
- `.agents/skills/dev-doc-harness/VERSION`: update package-local release marker to `0.4+`.
- `.agents/skills/dev-doc-harness/references/release-policy.md`: update current release identity references to `0.4+`.
- `.agents/skills/dev-doc-harness/docs/releases/`: add or update release-note references needed for `0.4+` validation.
- `README.md` or `.agents/skills/dev-doc-harness/docs/operator-note.md`: document maintainer workflow and package boundary.
- `.githooks/pre-commit`: add optional non-mutating local development hook.
- `CHANGELOG.md`: add newest-first implementation entry before commit.

Stable interfaces:

- `.agents/skills/dev-doc-harness/assets/templates/*.md`: remains the agent-facing template location.
- `SKILL.md` route table: should continue routing to the same flat template paths.
- `rule:lifecycle.large-phase-orchestration`, `rule:freeze.*`, and `rule:models.*`: no semantic changes.
- Root `AGENTS.md`: no changes expected.

Changed interfaces:

- Maintainer template edit workflow changes from editing flat templates directly to editing blocks and manifests, then running the assembler.
- Harness validation adds a generated-template freshness requirement.

Implementation boundaries:

- Do not create include-based published templates.
- Do not install or configure the hook automatically.
- Do not modularize `plan-amendment.md` or `variance-log.md` unless a very small common approval or header block falls out naturally and does not increase complexity; the primary target is the four large duplicated templates.
- Do not add third-party dependencies.

## Model and Sub-agent Strategy

Use `module:models`, including `rule:models.strategy-required`, `rule:models.context-strategy`, `rule:models.approved-strategy-authorized`, and `rule:models.fresh-confirmation`. Record only the compact strategy needed for this work item.

Current orchestration:

- Model/profile and reasoning effort if known: Codex desktop thread; exact model/profile not exposed in repository artifacts.

Fit assessment:

- Complexity: Medium. The work introduces a small generation tool and restructures template assets, but the behavior is deterministic and repository-local.
- Risk and blast radius: Medium. It changes the maintainer workflow for core harness templates and validator behavior, but keeps published template paths stable.
- Ambiguity: Low. The operator selected generated flat templates, ordered blocks, explicit manifests, validation integration, and non-distributable hook behavior.
- Budget and latency fit: Acceptable for one orchestration thread with one bounded review sub-agent if available.

Recommended orchestration change:

- Use the operator-selected `enterprise-default` policy for this work item.

Sub-agents:

- Use one optional read-only reviewer after the implementation diff exists. If sub-agent tooling is unavailable, the orchestration thread performs the same review and reports the fallback.

Sub-agent `assembly-design-review`:

- Purpose: Review the implemented block taxonomy, manifests, generated templates, validator integration, and hook placement for clarity and package-boundary mistakes.
- Context strategy: `curated prompt`.
- Input context: Approved spec and plan, changed diff, `release-policy.md`, `policy-architecture.md`, generated flat templates, block manifests, assembler script, validator output, and hook file path.
- Output artifact: Review findings summarized in the implementation completion report or variance log if material.
- Model policy: `enterprise-default`.
- Model class/profile: policy-relative standard; latest strongest only if review finds subtle package-boundary or validation recursion risk.
- Reasoning effort: Medium.
- Selection reason: Independent review reduces the chance of shipping confusing maintainer workflow or a distributable hook mistake.
- Parallel execution: No; run after implementation diff and validation output exist.
- Blast radius if wrong: Medium; missed drift or packaging mistakes could confuse future harness maintainers or downstream adopters.

## Task Plan

- [ ] `T-001` Dependencies: Approved planning package; define the final block taxonomy and naming grammar in implementation notes or maintainer docs, including `<artifact-family>.<order>.<scope>.<kebab-name>.md`, three-digit order fields, and scope markers; Traces: `REQ-001`, `RISK-002`.
- [ ] `T-002` Dependencies: `T-001`; create `.agents/skills/dev-doc-harness/assets/templates/blocks/` and `.agents/skills/dev-doc-harness/assets/templates/assemblies/`, then add manifest files for `small-medium-work-item-spec.md`, `large-phased-work-item-spec.md`, `small-medium-work-item-plan.md`, and `large-phased-work-item-phase-plan.md`; Traces: `REQ-001`, `REQ-002`, `RISK-007`.
- [ ] `T-003` Dependencies: `T-002`; split common spec sections into source blocks for shared header or metadata, goal/source/scope/context shape, requirements, acceptance criteria, interfaces/data/control flow, risks, planned commits, documentation matrix, readiness, and approval only where sharing improves clarity; update requirement, acceptance-criterion, and risk examples to use `###` headers with tag IDs; prefer numbered lists in long spec-template guidance where numbering improves reviewability; Traces: `REQ-003`, `REQ-004`, `REQ-012`, `RISK-001`, `RISK-002`, `RISK-009`.
- [ ] `T-004` Dependencies: `T-003`; create large anchor spec-specific blocks for large/phased rationale, phase decomposition, anchor model/sub-agent strategy, multi-gate planning language, and large readiness checks; preserve tag-header formatting for large-specific requirement, acceptance, and risk examples; Traces: `REQ-004`, `REQ-012`, `RISK-006`, `RISK-009`.
- [ ] `T-005` Dependencies: `T-002`; split common plan sections into source blocks for input artifacts, spec traceability shape, implementation approach, change surfaces, model/sub-agent strategy, task guidance, planned commits, validation plan, variance handling, freeze gate, readiness, completion, and approval, then create phase-plan-specific blocks for objective, approved anchor inputs, fresh-thread readiness, documentation tasks, and handoff output; prefer numbered lists in long plan-template guidance where numbering improves reviewability while keeping task checkboxes; Traces: `REQ-003`, `REQ-004`, `REQ-012`, `RISK-006`, `RISK-009`.
- [ ] `T-006` Dependencies: `T-002` through `T-005`; implement `.agents/skills/dev-doc-harness/scripts/assemble_templates.py` with `--list`, non-recursive `--check`, and `--write` that writes templates, re-runs the freshness check, and then runs the full harness validator; Traces: `REQ-005`, `REQ-006`, `RISK-001`, `RISK-005`, `RISK-007`.
- [ ] `T-007` Dependencies: `T-006`; update `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` to call the non-recursive assembly freshness check and add structural checks for manifest outputs, block naming, and absence of unresolved include directives in published templates; Traces: `REQ-007`, `REQ-010`, `RISK-005`.
- [ ] `T-008` Dependencies: `T-007`; add `.githooks/pre-commit` or an equivalent root-local hook file that runs `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`, fails on stale generated templates, does not mutate files, and is outside `.agents/`; Traces: `REQ-008`, `RISK-003`, `RISK-004`.
- [ ] `T-009` Dependencies: `T-006` through `T-008`; update maintainer-facing documentation in `README.md` or `.agents/skills/dev-doc-harness/docs/operator-note.md` with block editing, `--list`, `--write`, validator behavior, and hook package-boundary guidance; Traces: `REQ-009`, `RISK-001`, `RISK-004`.
- [ ] `T-010` Dependencies: `T-006` through `T-009`; update `.agents/skills/dev-doc-harness/VERSION`, release-policy text, release-note references, and validator release checks from `0.3.0` to `0.4+`; run `assemble_templates.py --write`, inspect generated flat template diffs, and update `CHANGELOG.md` with `2026-07-02_template-block-assembly -- generate 0.4+ templates from shared blocks`; Traces: `REQ-006`, `REQ-010`, `REQ-011`, `REQ-012`, `RISK-008`.
- [ ] `T-011` Dependencies: `T-010`; run validation commands, perform final diff review, run the optional `assembly-design-review` sub-agent if available, then commit with the approved implementation subject; Traces: `REQ-010`.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during plan approval, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets. Update this table before committing if implementation changes the subject wording.

Planning approval commit:

- Planned subject: `spike: template-block-assembly -- approve modular template plan`
- Changelog title or snippet: `2026-07-02_template-block-assembly -- approve modular template plan`
- Notes: Approval commit for `spec_template-block-assembly.md`, `plan_template-block-assembly.md`, and `CHANGELOG.md`.

Implementation commit:

- Planned subject: `docs: template-block-assembly -- generate 0.4+ templates from shared blocks`
- Changelog title or snippet: `2026-07-02_template-block-assembly -- generate 0.4+ templates from shared blocks`
- Notes: Implementation commit for release marker updates, block sources, assembly manifests, assembler, generated templates, validator integration, maintainer docs, hook file, and changelog.

## Validation Plan

| Command | Expected result |
|---|---|
| `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --list` | Lists each assembled output and ordered source blocks; output shows common blocks reused and large or phase-specific blocks distinct. |
| `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` | Exits 0 when checked-in flat templates match generated output; exits nonzero with named stale template paths if drift exists. |
| `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` | Writes generated flat templates, confirms freshness, runs full harness validation, and exits 0. |
| `rg -n "\{\{|include" .agents/skills/dev-doc-harness/assets/templates/*.md` | No unresolved include directives in published flat templates; generated-source comments are acceptable only if they do not require consumer action. |
| `rg -n "assets/templates/blocks|assets/templates/assemblies|assemble_templates.py" README.md .agents/skills/dev-doc-harness/docs/operator-note.md` | Maintainer guidance exists in at least one documented operator-facing location. |
| `Test-Path .githooks/pre-commit` | Returns `True` if a hook is added; hook path is outside `.agents/` and therefore outside the distributable package boundary. |
| `rg -n "test_harness_policy.py|assemble_templates.py" .githooks` | Hook runs the validator or documented equivalent and does not run `--write`. |
| `Get-Content .agents/skills/dev-doc-harness/VERSION` | Prints `0.4+` and no stale `0.3.0` marker remains in current release identity checks except historical release notes or changelog history. |
| `rg -n "REQ-001:|AC-001:|RISK-001:" .agents/skills/dev-doc-harness/assets/templates/*.md` | No current spec-template examples use colon-style IDs; requirement, acceptance, and risk examples use `###` headings with tag IDs. |
| `rg -n "### .*REQ-001|### .*AC-001|### .*RISK-001" .agents/skills/dev-doc-harness/assets/templates/*.md` | Current spec templates include tag-header examples for requirements, acceptance criteria, and risks. |
| `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | All checks print `PASS` and command exits 0, including assembly freshness. |
| `git diff --check` | No whitespace errors. |
| `git status --short` | Before implementation commit, only approved implementation targets and `CHANGELOG.md` are modified. |

Every validation entry states the expected signal before implementation starts. Include command exit behavior, important output text, manual observation, review criterion, or operator acceptance condition as applicable.

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, acceptance-criteria, or feasibility changes.

Likely local variance that may proceed with a note in the completion report:

- Manifest format uses JSON or a constrained text format instead of YAML to preserve standard-library parsing.
- The exact block count changes after implementation reveals a better minimum set.
- Maintainer guidance lands in README rather than package-local operator note, or in both, as long as package-boundary meaning remains clear.
- `plan-amendment.md` and `variance-log.md` remain flat hand-maintained files.
- Some short unordered lists remain bullets because numbering would reduce readability.

Variance requiring operator approval before continuing:

- Published templates require agents to resolve include directives.
- The hook is moved under `.agents/` or is installed automatically for downstream adopters.
- The validator no longer checks assembly freshness.
- `--write` no longer runs validation after writing.
- Large anchor or phase-plan specific sections are collapsed into common blocks in a way that hides their distinct lifecycle responsibilities.
- Release identity remains at `0.3.0` after implementation.
- Current templates keep colon-style requirement, acceptance, or risk examples instead of tag-header examples.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this plan.

Draft review status: Approved by operator on 2026-07-02.
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

- Acceptance criteria in `spec_template-block-assembly.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- The frozen plan had enough detail for each assigned execution part or delegated sub-agent to proceed safely.
- Execution remained within one orchestration thread with a bounded sub-agent strategy; otherwise the work was split, re-scoped, or escalated before implementation.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- Commit subjects match the approved planned subjects or recorded variance, and changelog title snippets are synchronized.
- Planned implementation changes are committed, or the completion report names the exact blocker or explicit no-commit instruction plus current worktree status.
- Variance log is present and current.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
