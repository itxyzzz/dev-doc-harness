# Template Block Assembly Spec

Work ID: `2026-07-02_template-block-assembly`
Short ID: `template-block-assembly`
Status: Approved
Harness release: `0.4+`
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:naming`, `module:quality`, `module:models`, `module:release`, `rule:lifecycle.documentation-matrix`, `rule:lifecycle.commit-message-format`, `rule:release.package-boundary`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:quality.spec-handoff`

## Goal

Make harness template maintenance clearer by moving repeated template body sections into ordered reusable source blocks, assembling self-contained flat templates for agents, and validating that generated templates stay current.

## Source and Intent

Source input:

- Operator review of the completed `2026-07-02_orchestration-sizing-large-templates` implementation.
- Operator concern that large/phased spec and plan templates still duplicate too much small/medium template body text.
- Collaborative design decision to use source blocks plus assembled flat templates so maintainers see what is common and what is large-specific, while agents still consume complete Markdown templates.
- Operator conventions:
  - Block filenames must sort in the same order they appear in assembled templates.
  - Block filenames should include artifact family, step number, scope marker, and kebab name.
  - A Python assembly script should expose simple `--write`, `--check`, and `--list` modes.
  - `--write` should assemble and then validate.
  - Validator checks should fail stale generated templates.
  - Any pre-commit hook must be harness-repository development tooling only and must not become part of the distributable package.

Desired operator/user outcome:

- Harness maintainers edit a small set of ordered source blocks and explicit assembly manifests.
- Agents and downstream users still open complete self-contained templates under `.agents/skills/dev-doc-harness/assets/templates/`.
- Large/phased template differences become obvious because common sections are shared and large-only or phase-only sections are visibly distinct in manifests and block names.

Success summary:

- The template assembly workflow reduces common body duplication without introducing include syntax into published templates.
- The validator catches generated-template drift.
- Local pre-commit support is available for this repository without being copied to downstream harness adopters.

## Scope Boundary

### In scope

- Add ordered template block source files under `.agents/skills/dev-doc-harness/assets/templates/blocks/`.
- Add explicit assembly manifests under `.agents/skills/dev-doc-harness/assets/templates/assemblies/`.
- Add `.agents/skills/dev-doc-harness/scripts/assemble_templates.py` with `--write`, `--check`, and `--list`.
- Update flat templates under `.agents/skills/dev-doc-harness/assets/templates/` to include a brief generated-source note and to be produced from the assembly workflow.
- Refactor common repeated body text for small/medium specs, large anchor specs, small/medium plans, and large phase plans into the smallest practical shared blocks.
- Preserve large anchor and phase-plan specific sections as distinct blocks.
- Update `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` so harness validation includes the assembly freshness check.
- Add or update maintainer-facing guidance for the assembly command and local hook behavior.
- Add a repository-local pre-commit hook outside `.agents/` that runs the validator and therefore fails on stale assembled templates.
- Update the harness release marker and current release-policy or validator references from `0.3.0` to `0.4+`.
- Update current spec and plan templates so requirement, acceptance-criterion, and risk entries use `###` block headers with tagged IDs such as `REQ-001`, `AC-001`, and `RISK-001`.
- Prefer numbered lists in current templates for long ordered or review-heavy guidance where numbering improves readability; keep checkboxes, tables, and short unordered lists when they are the clearer artifact shape.
- Update `CHANGELOG.md` before the implementation commit.

### Non-scope

- No unresolved include directives in published templates.
- No change to durable work-item artifact schemas beyond template authoring structure.
- No change to root `AGENTS.md` active repository model policy.
- No change to the large/phased lifecycle sequence or freeze-gate semantics.
- No automatic installation of the pre-commit hook in downstream repositories.
- No runtime product behavior changes.
- No rewrite of frozen historical work-item artifacts.

### Assumptions

- Source blocks and assembly manifests become the maintainer-facing authoring surface, while assembled flat templates remain the agent-facing and downstream-user-facing surface.
- The distributable harness package remains root `AGENTS.md` plus `.agents/`; repo-local hook files outside `.agents/` do not travel with the package.
- The repository can use only Python standard-library functionality for assembly and validation.
- Template drift validation belongs in `test_harness_policy.py` so manual validation and local hooks share one authoritative check path.
- The operator-selected package-local release marker for this work is `0.4+`.
- Current release-policy and validator references to `0.3.0` must be updated deliberately rather than only changing the raw `VERSION` file.

### Open questions

- None identified after repository-context review.

## Repository Context

### Current state

- Current flat templates are self-contained Markdown files under `.agents/skills/dev-doc-harness/assets/templates/`.
- The small/medium and large/phased spec templates share many repeated prompts for requirements, acceptance criteria, risks, planned commits, documentation matrix, readiness, and approval.
- The small/medium plan and large phase-plan templates share many repeated prompts for model/sub-agent strategy, task quality, planned commits, validation, variance, freeze gate, readiness, completion criteria, and approval.
- `test_harness_policy.py` already validates template route references, release context, broad duplicate policy blocks, and current-surface structure, but it does not validate generated-template freshness.
- `release-policy.md` states the distributable package is root `AGENTS.md` plus `.agents/`, excluding local development files outside that package boundary.
- Current release identity files and validation still refer to `0.3.0`, including `.agents/skills/dev-doc-harness/VERSION`, release policy text, release notes path checks, and validator assertions.

### Evidence read

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/naming-conventions.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/references/release-policy.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
- `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`
- `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
- `docs/work-items/2026-07-02_orchestration-sizing-large-templates/spec_orchestration-sizing-large-templates.md`
- `docs/work-items/2026-07-02_orchestration-sizing-large-templates/plan_orchestration-sizing-large-templates.md`

### Constraints and compatibility

- Templates may cite schemas and rule IDs, but reusable policy remains owned by canonical references.
- Published templates must remain directly usable by agents without resolving source-block include syntax.
- Assembly source files under `.agents/` are package contents and must be useful or harmless to downstream adopters.
- Hook files must stay outside `.agents/` so they are harness-repo development conveniences, not distributable harness behavior.
- Validator changes must avoid recursion when `assemble_templates.py --write` runs validation and `test_harness_policy.py` runs assembly freshness checks.

## Requirements

### `REQ-001` Template source blocks are ordered and self-explanatory

Rationale:

- Maintainers need transparent source files that sort in template order and make common, small-specific, large-anchor-specific, and phase-specific content easy to identify.

Acceptance links:

- Covered by AC-001 and AC-002.

Notes:

- Use filename grammar `<artifact-family>.<order>.<scope>.<kebab-name>.md`.
- Use three-digit numeric order fields such as `010`, `020`, and `030`.
- Use scope values such as `common`, `small`, `large`, and `phase`.

### `REQ-002` Assembly manifests explicitly define each published template

Rationale:

- Filename order helps browsing, but explicit manifests are the durable source of which blocks compose each flat template.

Acceptance links:

- Covered by AC-002 and AC-003.

### `REQ-003` Published templates remain complete self-contained Markdown

Rationale:

- Agents and downstream users should not need to resolve include directives before using a harness template.

Acceptance links:

- Covered by AC-003 and AC-004.

### `REQ-004` Common repeated body text has one source block when sharing improves clarity

Rationale:

- The current large/phased templates obscure their differences by repeating common small/medium prompt text.

Acceptance links:

- Covered by AC-004 and AC-005.

Notes:

- Do not over-abstract large anchor or phase-plan sections that carry distinct lifecycle meaning.

### `REQ-005` Assembly tooling has clear write, check, and list modes

Rationale:

- Maintainers need a repair command, a guard command, and an inspection command.

Acceptance links:

- Covered by AC-006.

### `REQ-006` `--write` assembles and validates in one command

Rationale:

- The operator wants maintainer workflow to avoid a separate required validation step after regeneration.

Acceptance links:

- Covered by AC-006 and AC-007.

### `REQ-007` Harness validation fails stale assembled templates

Rationale:

- Validation must catch drift even when local hooks are not installed or are bypassed.

Acceptance links:

- Covered by AC-007.

### `REQ-008` Local pre-commit support is not part of the distributable package

Rationale:

- Downstream harness users should not inherit harness-repository development hook behavior as an annoyance.

Acceptance links:

- Covered by AC-008.

### `REQ-009` Documentation explains maintainer workflow and package boundary

Rationale:

- Future maintainers need to know which files to edit, which command to run, and why hook files are outside `.agents/`.

Acceptance links:

- Covered by AC-009.

### `REQ-010` Existing harness validation remains intact

Rationale:

- Template modularization should strengthen current checks without weakening graph, release, duplicate-policy, route, or golden traversal validation.

Acceptance links:

- Covered by AC-010.

### `REQ-011` Harness release identity is updated to `0.4+`

Rationale:

- The planning package and current harness package should use the operator-selected `0.4+` marker consistently instead of leaving the package-local release marker stale at `0.3.0`.

Acceptance links:

- Covered by AC-011.

Notes:

- Update the release marker, release-policy text, validator expectations, and release-note references as needed so validation passes with `0.4+`.

### `REQ-012` Current templates use tagged block headers for requirements, acceptance criteria, and risks

Rationale:

- Requirement, acceptance-criterion, and risk blocks are easier to scan and cross-reference when each starts with a Markdown heading and a tag-style ID.

Acceptance links:

- Covered by AC-012.

Notes:

- Prefer numbered lists for long guidance in templates where ordering or count helps readability.
- Preserve checkbox lists for task tracking and tables where matrix structure is clearer.

## Acceptance Criteria

### `AC-001` Block filenames follow the template block grammar

Block filenames under `.agents/skills/dev-doc-harness/assets/templates/blocks/` follow `<artifact-family>.<order>.<scope>.<kebab-name>.md` and sort in a readable template order.

Verifies:

- REQ-001

Method:

- Review file names and run a targeted naming validation command or validator check.

### `AC-002` Assembly manifests define ordered outputs

Each assembly manifest lists its output file and ordered block list without relying on implicit directory sorting.

Verifies:

- REQ-001 and REQ-002

Method:

- Review manifest files under `.agents/skills/dev-doc-harness/assets/templates/assemblies/`.

### `AC-003` Published templates are complete Markdown files

The four primary published templates contain complete Markdown content and no unresolved include directives.

Verifies:

- REQ-002 and REQ-003

Method:

- Run `rg -n "\{\{|include|blocks/" .agents/skills/dev-doc-harness/assets/templates/*.md` and review any generated-source comments so they do not create unresolved work for template consumers.

### `AC-004` Large and phase template differences remain visible

The assembled large anchor spec and phase-plan templates visibly preserve large-only and phase-only sections while common body sections come from shared blocks.

Verifies:

- REQ-003 and REQ-004

Method:

- Review manifests and assembled template headings.

### `AC-005` Common repeated body text is materially reduced

Common repeated body text across primary spec and plan templates is materially reduced without removing required template guidance.

Verifies:

- REQ-004

Method:

- Review diff and run duplicate-block or targeted repeated-line checks after implementation.

### `AC-006` Assembly command modes are deterministic

`assemble_templates.py --write`, `--check`, and `--list` behave deterministically with clear stdout and exit codes.

Verifies:

- REQ-005 and REQ-006

Method:

- Run each mode and confirm expected output.

### `AC-007` Validator catches stale assembled templates

`test_harness_policy.py` includes an assembly freshness check and exits nonzero when generated templates are stale.

Verifies:

- REQ-006, REQ-007, and REQ-010

Method:

- Review validator integration and run the full harness validator.

### `AC-008` Local hook support stays outside the package

Any pre-commit hook or hook helper lives outside `.agents/` and is documented as local harness-repository development tooling only.

Verifies:

- REQ-008

Method:

- Review hook file path and package-boundary documentation.

### `AC-009` Maintainer guidance explains the assembly workflow

Maintainer-facing guidance explains editing blocks and manifests, running `assemble_templates.py --write`, inspecting `--list`, and relying on validation or the local hook for drift checks.

Verifies:

- REQ-009

Method:

- Review README or package-local operator note updates.

### `AC-010` Existing harness validation passes

Existing harness validation passes after modularization.

Verifies:

- REQ-010

Method:

- Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`.

### `AC-011` Harness release marker and release checks use `0.4+`

Verifies:

- REQ-011

Method:

- Review `.agents/skills/dev-doc-harness/VERSION`, release policy text, release notes references, and validator checks; run the full harness validator.

### `AC-012` Template requirement, acceptance, and risk blocks use tag headers

Verifies:

- REQ-012

Method:

- Review current spec templates and generated outputs for heading examples containing tag IDs such as `REQ-001`, `AC-001`, and `RISK-001`; review long guidance lists for numbered-list fit.

## Interfaces, Data, and Control Flow

### Interfaces affected

- `.agents/skills/dev-doc-harness/assets/templates/blocks/`: new maintainer-facing source block directory.
- `.agents/skills/dev-doc-harness/assets/templates/assemblies/`: new assembly manifest directory.
- `.agents/skills/dev-doc-harness/assets/templates/*.md`: generated flat templates remain the agent-facing interface.
- `.agents/skills/dev-doc-harness/scripts/assemble_templates.py`: new maintainer command-line interface.
- `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`: validation interface gains assembly freshness coverage.
- `README.md` or `.agents/skills/dev-doc-harness/docs/operator-note.md`: maintainer workflow guidance.
- `.githooks/pre-commit` or equivalent root-local hook path: optional harness-repo development hook.

### Data, config, and persistence

- No runtime persistence or application data changes.
- Git hook configuration is not committed as repository config; hook files are optional local development aids.
- Assembly manifests are static source data for generating templates.

### State and control flow

- Maintainer edit flow changes from editing only flat templates to editing block files and manifests, then running `assemble_templates.py --write`.
- Validation flow changes so `test_harness_policy.py` calls the assembly freshness check.
- Local pre-commit flow, when installed by a maintainer, runs the validator and fails when assembled templates are stale.

### Safety, security, privacy, migration, and rollback

- No security, privacy, or migration impacts are expected.
- Rollback is straightforward: revert the modularization commit to restore hand-maintained flat templates and prior validation behavior.
- The hook must not mutate staged files during commit; it should fail with instructions to run the write command.

## Risks and Rejected Alternatives

### `RISK-001` Source blocks could make templates harder to understand than duplicated flat files

Decision or mitigation:

- Keep published flat templates self-contained and add `--list` so maintainers can inspect the block sequence.

### `RISK-002` Too many tiny blocks could create noisy maintenance overhead

Decision or mitigation:

- Minimize shared blocks to repeated sections that carry real maintenance risk. Keep artifact-specific sections in dedicated blocks.

### `RISK-003` A mutating pre-commit hook could change staged files unexpectedly

Decision or mitigation:

- The hook runs validation only. It does not run `--write` or alter files.

### `RISK-004` Packaging the hook would annoy downstream harness users

Decision or mitigation:

- Place hook files outside `.agents/` and document them as this repository's local development tooling.

### `RISK-005` Validator and assembly script could recurse into each other

Decision or mitigation:

- `assemble_templates.py --check` performs only assembly freshness checks. `assemble_templates.py --write` may run the full validator after writing. `test_harness_policy.py` calls only the check mode or shared non-recursive check function.

### `RISK-006` Over-sharing could hide large/phased semantic differences

Decision or mitigation:

- Large anchor and phase-plan responsibilities remain in large or phase-specific blocks and manifests.

### `RISK-007` YAML parsing could add dependency or syntax complexity

Decision or mitigation:

- Prefer a simple manifest format that can be parsed by the Python standard library, such as JSON or a constrained line-oriented text manifest. If YAML-like syntax is used, implement only the documented subset and validate it clearly.

### `RISK-008` Release marker updates could drift from release validation

Decision or mitigation:

- Treat the version marker, release-policy text, release-note references, and validator assertions as one implementation surface. Validation must pass after the marker changes to `0.4+`.

### `RISK-009` Numbered-list guidance could make templates feel over-structured

Decision or mitigation:

- Prefer numbered lists where they improve long guidance, sequencing, or reviewability. Keep bullets for short peer items and checkboxes for task tracking.

## Planned commits

Use `rule:lifecycle.commit-message-format`. Planned commit subjects are reviewable during spec and plan review, and their title snippets must stay synchronized with `CHANGELOG.md` headings or bullet-level snippets.

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Planning approval | `spike: template-block-assembly -- approve modular template plan` | `2026-07-02_template-block-assembly -- approve modular template plan` | Approval commit for this spec and plan. |
| Implementation | `docs: template-block-assembly -- generate 0.4+ templates from shared blocks` | `2026-07-02_template-block-assembly -- generate 0.4+ templates from shared blocks` | Implementation commit for release marker updates, blocks, manifests, assembler, generated templates, validation, maintainer docs, hook, and changelog. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required before approval and implementation commits; title snippets synchronized with planned commit subjects. |
| Test cases | Snapshot | No | Not applicable | Not applicable | Validator updates and script checks cover this tooling change. |
| Testing guide delta | Living delta | No | Not applicable | Not applicable | No project testing guide change expected beyond maintainer command documentation. |
| Operator manual delta | Living delta | No | Not applicable | Not applicable | README or package-local operator note update is sufficient for maintainer workflow. |
| API reference delta | Living delta | No | Not applicable | Not applicable | No public API changes. |
| Architecture snapshot | Snapshot | No | Not applicable | Not applicable | This is a template authoring refactor within existing harness architecture. |
| Architecture summary delta | Living delta | No | Not applicable | Not applicable | No long-lived architecture summary change expected. |

## Spec readiness checklist

- [x] Source input and desired outcome are captured.
- [x] Scope, non-scope, assumptions, and open questions are explicit.
- [x] Requirements are specific, relevant, bounded, and linked to acceptance criteria.
- [x] Acceptance criteria are observable, testable, and tied to requirements or scope items.
- [x] Repository evidence and compatibility constraints are recorded.
- [x] Interfaces, data, control flow, and safety/privacy/migration impacts are checked.
- [x] Risks and rejected alternatives are listed or explicitly absent after review.
- [x] Documentation artifact matrix decisions have paths or reasons.
- [x] Planned commit subjects and changelog title snippets are synchronized.
- [x] No unresolved placeholders remain before approval or handoff.

## Approval

- Status: Approved
- Superseded by: record only when this artifact is superseded
