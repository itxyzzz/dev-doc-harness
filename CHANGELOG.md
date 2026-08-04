# Changelog

All notable changes to this repository are documented here.

Entries are newest-first by release, then grouped by change type.

## Unreleased

## Release 0.9

### 2026-08-04 docs: documentation-assessment-simplification -- simplify documentation assessment

Meta -- `0.9.0` : `repository-only`

#### Changed

- Replaced the documentation matrix with a compact five-item assessment and isolated current changelog authoring in the implementation-stage module.
- Regenerated planning templates and added static checks for the new policy and ownership boundaries.

### 2026-08-03 docs: plan-template-alignment -- align assembled plan templates

Meta -- `0.9.0` : `distributable`

#### Changed

- Moved the shared plan strategy after implementation tasks and replaced the small-plan readiness checks with fresh-session coverage criteria.
- Clarified phase session sizing, separated phase execution handoff from completion reporting, and preserved rolling, batched, and parallel coordination boundaries.
- Regenerated both plan templates and strengthened structural validation for their revised ordering, handoff, readiness, and lifecycle contracts.
- Removed the duplicate freeze relabel instruction from both Approval blocks and normalized prose wrapping across all plan source blocks and their assembled templates.
- Renamed the next-stage fallback group to `Execution requirements and contingencies`, made its scope explicit, and added matched execution-startup headings to the small and phase handoffs.

### 2026-08-02 docs: task-orchestration-model-policy -- tighten selection templates

Meta -- `0.9.0` : `distributable`

#### Changed

- Constrained fixed-stage templates to planning- or execution-appropriate Method and Review prompts.
- Added an explicit Orchestration mode fit rationale across canonical notation, template sources, generated artifacts, freeze presentation, and validation.
- Added the large-anchor draft-to-frozen heading transition and replaced position-dependent policy references with stable rule IDs.

### 2026-08-02 docs: task-orchestration-model-policy -- restore four-field orchestration

Meta -- `0.9.0` : `distributable`

#### Changed

- Restored Method, Orchestration mode, `Run in`, and Review as the complete Orchestration field set.
- Moved conditional rationale into canonical strategy prose covering the combined Orchestration and Model selection when non-obvious.
- Removed the mode-specific rationale field from freeze guidance, templates, generated artifacts, README guidance, and validation fixtures.

### 2026-08-02 docs: task-orchestration-model-policy -- correct policy ownership structure

Meta -- `0.9.0` : `distributable`

#### Changed

- Reorganized the canonical model policy into explicit orchestration, model-selection, review, and sub-agent responsibility groups.
- Added a stable execution-review contract rule and corrected nested rule-owner mappings and consumers.
- Made owner-heading validation enforce exact nested heading levels and documented the operator-authorized structure-only policy variance.

### 2026-08-02 docs: task-orchestration-model-policy -- clarify session and stage selection

Meta -- `0.9.0` : `distributable`

#### Changed

- Reorganized the model policy around lifecycle-owned stages and stage-appropriate orchestration, review, continuity, and model selection.
- Replaced top-level Codex-task terminology with portable orchestration-session terminology across current policy and templates.
- Preserved sub-agent authorization, context, concurrency, review, reporting, and integration safeguards with focused validation.
- Added focused validation that keeps current-session metadata independent from resolved-profile observations.

### 2026-08-02 docs: task-orchestration-model-policy -- align orchestration and model selection

Meta -- `0.9.0` : `distributable`

#### Changed

- Made Orchestration mode an explicit next-stage field across policy, templates, freeze presentation, and validation.
- Defined portable model facets and host-native fallbacks while simplifying optional current-session diagnostics.
- Required canonical continuity and preserved independent high-risk review as distinct from final integration.

### 2026-08-03 docs: spec-template-alignment -- align assembled spec templates

Meta -- `0.9.0` : `distributable`

#### Changed

- Reordered shared specification context, renamed its impact assessment, and retained both generated spec templates as block-assembled outputs.
- Simplified the small staged spec-only handoff and readiness checks while preserving the default combined planning transition.
- Clarified large-anchor routing, operations, handoff ownership, and readiness checks; updated structural validation for the revised contracts.

### 2026-08-03 plan: spec-template-alignment -- approve spec template cleanup

Meta -- `0.9.0` : `repository-only`

#### Planned

- Approved the bounded source-block, generated-template, and validator plan for the small/medium and large/phased specification-template alignment.

### 2026-08-01 refactor: changelog-fragment-clarity -- clarify current fragment lifecycle

Meta -- `0.9.0` : `distributable`

#### Changed

- Renamed current implementation and phase changelog examples to explicit `-fragment` filenames while preserving generic discovery for frozen historical paths.
- Moved frozen legacy-format and root-migration guidance into a final compatibility section, leaving routine authoring and consolidation guidance first.
- Normalized root changelog entry separators deterministically and added regression coverage for spacing, release-heading preservation, and idempotent reruns.

### 2026-08-01 fix: changelog-lifecycle-simplification -- restore implementation fragment lint guard

Meta -- `0.9.0` : `distributable`

#### Fixed

- Restored the pre-commit fragment-lint guard and its policy-validator expectation; planning routes remain free of changelog authoring requirements.

### 2026-08-01 refactor: router-maintenance-architecture -- isolate maintenance and freeze context

Meta -- `0.9.0` : `distributable`

#### Changed

- Made `SKILL.md` the sole operational router and moved maintenance-only module ownership to `references/maintenance-architecture.md`.
- Removed duplicate routing and unused maintenance taxonomy content while preserving module ownership, dependency, validation, and lifecycle-maintenance guidance.
- Made naming an explicit planning input, deferred freeze-gate references from draft plan templates, regenerated the templates, and strengthened structural validation for those boundaries.

### 2026-08-01 refactor: changelog-lifecycle-simplification -- retain only implementation delivery records

Meta -- `0.9.0` : `distributable`

#### Changed

- Moved current changelog authoring and consolidation policy into an implementation-only module and removed planning-approval changelog requirements from routing, freeze gates, templates, and validation.
- Replaced root entry metadata with a compact tagged line, removed every root planning-only entry, and retained frozen legacy-fragment parsing for compatibility.
- Added deterministic root migration and idempotency coverage, while keeping release-note curation manual and removing the obsolete root `TODO.md` package-boundary reference.

### 2026-08-01 docs: lifecycle-stage-boundaries -- align README stage terminology

Meta -- `0.9.0` : `repository-only`

#### Changed

- Aligned the README lifecycle summary and next-stage recommendation list with the canonical `Next lifecycle stage` terminology, and normalized its long prose line wraps.

### 2026-07-31 docs: task-bound-checks -- make checks task-bound

Meta -- `0.9.0` : `distributable`

#### Changed

- Made the executable plan body a flat task list and nested every check under one parent task.
- Replaced shared-check allocation with explicit integration tasks for end-to-end validation.

### 2026-07-31 docs: spec-quality-bar -- clarify planning inputs

Meta -- `0.9.0` : `distributable`

#### Changed

- Clarified the concise spec inputs needed for planning and the spec-to-plan self-containedness boundary.

### 2026-07-31 docs: lifecycle-stage-boundaries -- clarify freeze lifecycle stages

Meta -- `0.9.0` : `distributable`

#### Changed

- Defined canonical lifecycle-stage boundaries, made the approval commit the only formal planning-freeze route, and preserved fresh authorization and variance boundaries.
- Updated template source blocks and regenerated templates to render `Next lifecycle stage` instead of task-level transition fields; the policy validator now enforces that contract and rejects retired handoff-snapshot wording.
- Confirmed that the intentionally simplified README remains semantically compatible and left it unchanged.
- Used the assembler's required `--write` mode before its freshness check; this is equivalent to the planned regeneration step.
- Included the operator-authorized formatting-only line-wrap change in `references/evidence-and-report-artifacts.md` without changing its semantics.

### 2026-07-31 docs: entity-section-ownership -- clarify spec-plan hierarchy

Meta -- `0.9.0` : `distributable`

#### Changed

- Nested `SPEC`/`VER` under spec quality and `TASK`/`CHECK` under plan quality, with a concise task-to-check-to-criterion cue.

### 2026-07-30 refactor: artifact-style-ownership-cleanup -- consolidate readability policy

Meta -- `0.9.0` : `distributable`

#### Changed

- Moved author-facing plain-language guidance to Quality as `rule:quality.plain-language` and kept Quality as the Verification Criterion semantic owner.
- Focused Artifact Style on conditional presentation, consolidated its traceability guidance under the retained `rule:style.trace-density`, and preserved the scoped one-line reflow while correcting the identified whitespace.
- Regenerated the spec templates from their source block and updated policy validation to enforce the Quality owner without a definition-only modal exception.

### 2026-07-30 docs: task-check-conformance -- clarify execution evidence

Meta -- `0.9.0` : `distributable`

#### Added

- Defined `TASK` as a first-class durable-plan entity and clarified task-local versus cross-cutting Plan Check placement.
- Added execution-quality ownership for implementation evidence and `VER` conformance statuses.

#### Changed

- Kept `CHECK` → `VER` as the conformance-evidence relationship and made task links operational only.
- Regenerated plan templates and extended validator coverage for task/check placement, execution-time status recording, and the preserved readability reordering.

### 2026-07-30 docs: durable-planning-quality-clarity -- clarify plans and conformance

Meta -- `0.9.0` : `distributable`

#### Changed

- Applied one quality bar to all durable specs and plans, with a separate execution-size requirement only for phase plans.
- Clarified the plain-language and material-open-question rules, preserved material operator-provided source context in durable handoffs, and removed duplicate rejected-alternatives wording.
- Defined a lightweight evidence model: `SPEC` commitments are established by `VER` criteria, while `CHECK` records the method, result, and evidence without mandatory mapping tables.
- Regenerated affected plan templates and replaced the unreachable mandatory-matrix validator fixture with active local-link coverage.

### 2026-07-29 docs: worktree-continuity-rules -- clarify new-task worktree baselines

Meta -- `0.9.0` : `distributable`

#### Changed

- Reworked the freeze-gate continuity guidance into separate new-task and
  same-task rules while preserving the existing authorization and fallback
  safeguards.
- Required each new task to select and report its Git starting state, disclose
  copied uncommitted paths, and avoid the implicit default-branch fallback.
- Added policy-test coverage for the readable continuity section and the
  starting-state safeguards.

### 2026-07-29 docs: naming-convention-review-fixes -- reconcile review feedback

Meta -- `0.9.0` : `distributable`

#### Changed

- Aligned current naming policy on two-digit amendment identifiers, kebab-case planning artifact types, optional issue-key work IDs, and one commit-subject changelog heading grammar.
- Removed duplicate local grammar from current lifecycle and naming guidance while retaining filename-kind references and concrete examples.
- Updated focused harness-policy validation without rewriting historical work-item artifacts or changelog entries.

### 2026-07-29 fix: harness-execution-flow-clarity -- deduplicate plan state and restore conditional style routing

Meta -- `0.9.0` : `distributable`

- Placed plan-state fields at their single lifecycle boundaries, restored conditional artifact-style loading for routine small/medium artifacts, regenerated active templates, and added focused structural regression coverage.
- **Consolidate reviewed changelog fragments:** Refreshed root `CHANGELOG.md` at the operator-owned post-integration checkpoint.

### 2026-07-28 refactor: harness-execution-flow-clarity -- separate transition flow from context loading

Meta -- `0.9.0` : `distributable`

- Consolidated planning transitions and chat projection in the freeze-gate owner, narrowed execution-quality to context loading and startup consumption, and aligned architecture and validator ownership checks without changing operator-visible behavior.

### 2026-07-28 fix: harness-execution-flow-clarity -- replace no-review blocker with operator decision

Meta -- `0.9.0` : `distributable`

- Replaced the hard no-review execution blocker with disclosure, one-time operator decision, recorded authorization, focused validation, and completion-report evidence while retaining independent review as the default.

### 2026-07-28 fix: harness-execution-flow-clarity -- consolidate post-freeze transition guidance

Meta -- `0.9.0` : `distributable`

- Folded freeze mechanics into the approval checklist, moved continuation rules into structured post-freeze routing, and made execution handoffs apply explicit operator overrides to the frozen approved selection without rewriting the frozen artifact.

### 2026-07-28 fix: harness-execution-flow-clarity -- clarify freeze transition routing

Meta -- `0.9.0` : `distributable`

- Moved the four-group next-stage explanation to draft review, clarified runtime-override recording, made approved agent task creation the default new-task continuation with manual creation as fallback, and stated the normal multi-gate large/phased flow.

### 2026-07-28 feat: harness-execution-flow-clarity -- compact bootstrap and add skill metadata

Meta -- `0.9.0` : `distributable`

- Compacted the repository bootstrap while preserving its semantic guards, added minimal generated skill UI metadata with focused validation, retained installation-neutral skill routing, and included the operator's README improvements.

### 2026-07-28 docs: harness-execution-flow-clarity -- clarify operator guidance and Superpowers workspace

Meta -- `0.9.0` : `distributable`

- Reworked the package-local operator note as a human-facing harness explanation, clarified the harness and Superpowers responsibilities, ignored the plan-specific Superpowers workspace, and corrected a README typo.

### 2026-07-27 fix: harness-execution-flow-clarity -- harden next-stage validation

Meta -- `0.9.0` : `distributable`

- Require known-suitable profile, suitable or immaterial context risk, and a concrete continuity benefit for same-Codex-task fixtures; reject mixed draft/frozen state labels.

### 2026-07-27 fix: harness-execution-flow-clarity -- clarify frozen handoff heading

Meta -- `0.9.0` : `distributable`

- Made plan-handoff source blocks select one draft or frozen next-stage heading and extended focused validation to reject simultaneous headings in source and generated plans.

### 2026-07-27 feat: harness-execution-flow-clarity -- simplify next-stage presentation

Meta -- `0.9.0` : `distributable`

- Simplified the next-stage interface into four plain-language groups, added execution terminology and chat projection, refreshed generated templates, and added focused validation.

### 2026-07-27 feat: harness-execution-flow-clarity -- restore execution and review defaults

Meta -- `0.9.0` : `distributable`

- Restored the canonical execution-method cascade, route-specific reviewer contract, and start-override validation, including a model-only override fixture that records the selection without requiring an amendment solely for that runtime choice.

### 2026-07-27 feat: harness-execution-flow-clarity -- enforce combined planning

Meta -- `0.9.0` : `distributable`

- Enforced complete combined small/medium packages at review and freeze, retained authorized staged and large-anchor exceptions, and added focused package-shape validation.

### 2026-07-27 docs: harness-execution-flow-clarity -- clarify drift and changelog guidance

Meta -- `0.9.0` : `distributable`

- Reworked README as a user-facing harness overview and aligned its focused model-selection checks with the simpler prose and Markdown line wrapping.

### 2026-07-21 docs: harness-distribution-instructions -- separate reusable and release-maintenance guidance

Meta -- `0.9.0` : `distributable`

#### Changed

- Separated copyable harness instructions from distribution-only release-maintenance guidance.
- Moved the release-branch runbook into the package, aligned the release policy and README, and updated validation.
## Release 0.8

### 2026-07-18_superpowers-adapter-contract -- align durable planning and execution

Meta -- `0.8.0` : `distributable`

#### Added

- Added conditional Superpowers execution metadata, Global Constraints, task-interface, and explicit dispatch-allocation prompts to canonical plan templates.
- Added focused structural validation and synthetic fixtures for adapter placement, lifecycle, task form, fallback, and model-envelope behavior.

#### Changed

- Aligned project, global-bootstrap, lifecycle, execution-quality, model-policy, router, README, and operator guidance around one durable harness route with ephemeral Superpowers execution aids.

### 2026-07-18_planning-template-clarity -- clarify models handoffs and phases

Meta -- `0.8.0` : `repository-only`

#### Added

- Added focused structural validation for concise current planning-template contracts, including model selection, transition ownership, rolling phases, and delegation routing.

#### Changed

- Separated planning-task observations from approved execution selections across canonical policy and generated template prompts.
- Made combined-plan and phase-transition ownership explicit, regenerated source-derived templates, and aligned operator guidance with rolling phase execution.
- Simplified commitment and planned-commit prompts while preserving canonical validation, freeze, variance, and changelog rules.

### 2026-07-18_lifecycle-doc-clarity -- repair lifecycle diagram flow

Meta -- `0.8.0` : `repository-only`

#### Fixed

- Restored the large-path node identity and the existing same-task/new-task
  handoff labels while retaining the approved fresh-transition nodes and
  feedback loops.

### 2026-07-18_lifecycle-doc-clarity -- clarify lifecycle gates and planning guidance

Meta -- `0.8.0` : `repository-only`

#### Changed

- Corrected the user-facing lifecycle graph so feedback returns to each draft
  and fresh instructions or start authorization follow every freeze boundary.
- Replaced the formal planning trace-ID graph with proportional, plain-language
  guidance and aligned the operator note with pre-freeze execution selection
  and phased approval boundaries.

### 2026-07-18_lifecycle-doc-clarity -- clarify lifecycle confirmation gates

Meta -- `0.8.0` : `repository-only`

#### Fixed

- Rendered the post-freeze operator confirmations as decision nodes and placed
  the same-task/new-task handoff label on each outgoing transition.

### 2026-07-18_lifecycle-doc-clarity -- clarify README planning terminology

Meta -- `0.8.0` : `repository-only`

#### Changed

- Replaced generic preamble terminology with Specification Commitments,
  Verification Criteria, and Plan Checks; added per-stage model and
  reasoning-effort recommendations; and removed the premature spec-kit claim.
## Release 0.7

### 2026-07-15 docs: harness-simplification -- align policy and template cues

Meta -- `0.7.0` : `repository-only`

### Changed

- Aligned current policy and retained concise template cues, then regenerated
  the assembled templates and recorded amendment-owned validation evidence.

### 2026-07-14_harness-simplification -- restore focused template cues

Meta -- `0.7.0` : `repository-only`

### Changed

- Approved amendment 001 to align current guidance, restore two concise
  template cues, and reconcile amendment-owned validation evidence without
  rewriting frozen implementation records.

### 2026-07-14_harness-simplification -- reduce policy and mapping overhead

Meta -- `0.7.0` : `repository-only`

### Changed

- Simplified current harness policy, templates, and operator guidance while
  keeping stable IDs, meaningful freeze boundaries, and material-change review.
- Added deterministic scenarios for proportional mappings, uninterrupted
  approved execution, variance routing, and the copy-ready README bootstrap.

### 2026-07-14_harness-simplification -- ignore local implementation worktrees

Meta -- `0.7.0` : `repository-only`

### Changed

- Added an ignore rule for local `.worktrees/` implementation isolation.

### 2026-07-13_multi-changelog-fragments -- validate multiple fragment entries

Meta -- `0.7.0` : `distributable`

#### Added

- Added entry-scoped changelog fragment parsing and the grammar-only `--lint` gate.

#### Changed

- Updated ordinary commit, release preparation, and operator guidance to preserve checkpoint-owned root consolidation.

### 2026-07-13_model-selection-calibration -- retain subagent review default

Meta -- `0.7.0` : `distributable`

#### Changed

- Retained independent sub-agent review as the default and made separate task/thread review an operator-managed fallback pending proven inter-task reporting.

### 2026-07-13_model-selection-calibration -- calibrate economy model guidance

Meta -- `0.7.0` : `distributable`

#### Changed

- Calibrated the canonical `economy-default` model-selection guidance and aligned supporting reviewer examples, model-strategy prompts, generated templates, and policy validation.
- Added focused regression protection for allocation, lifecycle/approval, reviewer-evidence, and canonical-owner boundaries.

### 2026-07-14_plain-language-artifacts -- require ordinary modal wording

Meta -- `0.7.0` : `distributable`

#### Changed

- Added the canonical plain-language rule and made its style module mandatory for small/medium planning.
- Added the concise commitment prompt, updated the small/medium source-block route cues, regenerated every affected template, and protected current authoring paths with focused validation.
## Release 0.6

### 2026-07-12_user-facing-narrative -- streamline operator guidance

Meta -- `0.6.0` : `distributable`

#### Changed

- Restructured the README around operator problems, lifecycle, ordinary conversational use, adoption, and maintainer detail while preserving the main lifecycle diagram.
- Corrected the large/phased diagram route so anchor-spec freeze leads to phase-plan drafting and phase-plan freeze before implementation.
- Completed freeze-boundary routing in the diagram so anchor and amendment packages visibly select their documented next activity and approved continuity before work resumes.
- Added a standalone rationale and a maintainer-only tooling boundary to the package-local operator note.
- Corrected root agent instructions to name protected post-release PR synchronization and remote verification.

### 2026-07-12_user-facing-narrative -- approve concise operator story

Meta -- `0.6.0` : `distributable`

#### Added

- Added the approved combined small/medium specification and implementation plan for restructuring the harness's user-facing narrative.

#### Changed

- Planned a corrected retained lifecycle diagram, early problem framing, ordinary conversational usage guidance, a standalone package-local rationale, and accurate protected post-release synchronization wording.

### 2026-07-12_new-task-handoff-visibility -- create configured continuity tasks

Meta -- `0.6.0` : `distributable`

#### Changed

- Defined combined and explicitly staged planning shapes with transition targets selected from the actual frozen package.
- Added visible approval-gated configured task creation, exact-setting checks, and the manual copy-ready handoff fallback.
- Split handoff template prompts by artifact shape, regenerated current templates, and aligned operator guidance and validation.

### 2026-07-12_new-task-handoff-visibility -- clarify transition targets

Meta -- `0.6.0` : `distributable`

#### Added

- Added the approved combined small/medium specification package for explicit planning shape, actual handoff target, visible transition handoff, and approval-gated configured task creation.

#### Changed

- Recorded the default combined small/medium flow, explicit staged exception, large-anchor continuation, manual fallback, and focused validation plan.

### 2026-07-12_new-task-handoff-visibility -- align handoff block names

Meta -- `0.6.0` : `distributable`

#### Changed

- Renamed handoff source blocks to the standard spec/plan order-scope grammar and aligned manifests plus validation without changing generated template behavior.

### 2026-07-12 spec: commitment-verification-model -- define readable conformance layers

Meta -- `0.6.0` : `repository-only`

### Added

- Approved the canonical Specification Commitment, Architecture Decision, Verification Criterion, Implementation Task, and Plan Check semantic model.
- Added the work-item architecture snapshot and the Superpowers pointer to the canonical planning package.

### Changed

- Defined the Specification Package to Plan information flow and the separate evidence-to-conformance loop that later implementation planning must preserve.

### 2026-07-11_model-selection-dimensions -- separate model tier and optimize execution handoff

Meta -- `0.6.0` : `distributable`

#### Changed

- Separated model generation, vendor-neutral capability tier, reasoning effort, resolved profile, and availability/fallback across canonical policy and planning templates.
- Classified `ultra` as platform multi-agent orchestration and clarified recommendation, harness authorization, runtime permission, platform availability, and approved fallback boundaries.
- Added artifact-grounded fresh-task startup and same-task model-switch rehydration guidance without inferring unexposed context or compaction thresholds.
- Added a reusable next-task handoff block to all four primary template assemblies and regenerated their outputs.
- Added focused validation for selection dimensions, orchestration semantics, execution continuity, handoff parity, and the shared handoff assembly contract.

### 2026-07-11_commitment-verification-model -- separate commitments, criteria, and checks

Meta -- `0.6.0` : `distributable`

#### Changed

- Established canonical Specification Commitment, Verification Criterion, Plan Check, asymmetric traceability, and conformance-status rules with exact full-name entity grammar.
- Replaced current reusable specification and plan schemas with atomic commitments, correctly placed criteria, separate disposition/execution mappings, complete tasks/checks, and reproducible execution records.
- Regenerated the primary templates from authoritative source blocks and aligned architecture, amendment, variance, readiness, lifecycle, operator, and package guidance consumers.
- Added deterministic positive and negative structural fixtures, real frozen historical compatibility coverage, and current-surface legacy-vocabulary checks.
- Preserved fresh-context RED/GREEN/REFACTOR behavior transcripts and completed a blocking-finding-free semantic re-review.

### 2026-07-12_superpowers-stub-continuity -- prohibit bootstrapping compatibility pointers

Meta -- `0.6.0` : `distributable`

#### Changed

- Required a pre-existing `docs/superpowers` directory containing previous documentation packages before new continuity pointers may be added, and prohibited creating or seeding that state during current work.
- Retained the minimal pointer-stub schema and added golden traversal coverage across live compatibility surfaces.

#### Removed

- Removed the repository's six current Superpowers pointer stubs.

### 2026-07-11_post-release-pr-flow docs: require protected post-release synchronization

Meta -- `0.6.0` : `repository-only`

#### Changed

- Required post-release development state to reach protected `master` through a topic-branch pull request, followed by remote ancestry and released-changelog verification before new development branches are created.

### 2026-07-11_model-selection-dimensions -- define tier, orchestration, and handoff axes

Meta -- `0.6.0` : `distributable`

#### Added

- Added an approved implementation plan for explicit model generation, capability tier, reasoning effort, orchestration mode, fallback, and execution-continuity policy.
- Added approved architecture and evidence snapshots covering GPT-5.6 Sol, Terra, Luna, `ultra`, restrictive sub-agent authorization, model-transition risk, context visibility, and fresh-task startup.

#### Changed

- Planned minimal copy-ready handoffs and canonical artifact-grounded task startup so model transitions do not require context rediscovery.

### 2026-07-09_changelog-fragment-consolidation -- add work-item changelog sources

Meta -- `0.6.0` : `distributable`

#### Added

- Added work-item-local changelog fragment policy, template guidance, operator documentation, and a consolidation script for inserting reviewed unreleased fragments into root `CHANGELOG.md`.
- Added harness validation coverage for fragment parsing, duplicate-safe consolidation, check-mode failures, operator-owned checkpoints, and Dev Doc Harness distribution release-source compatibility.

#### Changed

- Changed routine harness commit guidance so independent work items update `docs/work-items/<work-id>/changelog/*.md` before commit and consolidate root `CHANGELOG.md` only at explicit checkpoints.
- Clarified that Dev Doc Harness distribution release policy is separate from release processes for downstream applications, packages, or agentic systems that use the harness.

### 2026-07-09_plan-task-block-format -- replace checklist task rows

Meta -- `0.6.0` : `distributable`

#### Changed

- Replaced checklist-shaped plan task prompts with sectioned task blocks and centralized requirement and acceptance traceability matrix guidance.
- Added harness validation coverage so current plan templates must keep task-block fields, traceability matrix headers, and no checkbox task examples.

### 2026-07-07_superpowers-compat-guidance -- document adapter flow and fix release baseline

Meta -- `0.6.0` : `distributable`

#### Added

- Added Superpowers adapter guidance to the operator README, package-local operator note, harness entrypoint, and canonical lifecycle and freeze-gate references.
- Restored package-local `0.5.0` release notes verbatim from `origin/release/0.5` as the latest concrete release-note file.

#### Changed

- Updated the harness development marker and validator expectations from `0.4+` to `0.5+` while keeping release notes on concrete released versions.
- Updated the release branch process so future release prep synchronizes `VERSION`, release policy, release notes, validator expectations, and the post-release development marker.
## Release 0.5

### 2026-07-04_release-branch-process -- document release branch workflow

Meta -- `0.5.0` : `distributable`

#### Added

- Added a root-level agent-executable release branch runbook and an `AGENTS.md` pointer for chat-triggered release branch creation, including remote release version derivation, package-local release notes, release branch push, and post-release `master` reset steps.
- Aligned release policy and validation with stable release-note filenames such as `0.5.0.md`, while allowing post-release development markers such as `0.5+` in `VERSION`.

### 2026-07-03_artifact-style-guidance -- add artifact style module

Meta -- `0.5.0` : `distributable`

#### Added

- Added `module:artifact-style` as the canonical owner for final artifact content, scannable structure, placeholder control, traceability density, and template prompt style.
- Added validator coverage for artifact-style ownership, large-anchor routing, template style cues, decision/amendment/variance IDs, and canonical model-policy examples.

#### Changed

- Made artifact-style guidance mandatory for large anchor specs and conditional for other large or hard-to-scan artifacts while preserving routine small/medium route budgets.
- Updated planning templates, the architecture snapshot template, amendment template, and variance log template with stronger final-state fields, unresolved-decision readiness checks, evidence cross-references, and model-policy source prompts.
- Updated operator-facing docs and 0.4+ release notes to mention artifact-style guidance and template readability hardening.

### 2026-07-03_work-item-architecture-decisions -- make architecture snapshots first-class

Meta -- `0.5.0` : `distributable`

#### Added

- Added lifecycle, quality, router, template, documentation, and validator support for work-item architecture decisions and the reusable `architecture-snapshot.md` template.

#### Changed

- Updated spec and plan templates so specs capture architecture decisions, plans consume architecture inputs, and repository-level `ARCHITECTURE.md` documents remain future work.

### 2026-07-02_template-block-assembly -- generate 0.4+ templates from shared blocks

Meta -- `0.5.0` : `distributable`

#### Added

- Added ordered source blocks, explicit assembly manifests, `assemble_templates.py`, and validation coverage so the four primary planning templates stay generated and self-contained.
- Added a root-local non-mutating pre-commit hook for harness repository development.

#### Changed

- Updated the package-local release marker and current release notes to `0.4+`.
- Regenerated the small/medium and large/phased spec and plan templates from shared blocks, with tag-header examples for requirement, acceptance-criterion, and risk entries.

### 2026-07-02_orchestration-sizing-large-templates -- align sizing and phased templates

Meta -- `0.5.0` : `distributable`

#### Changed

- Clarified harness sizing around one orchestration thread with bounded delegation and aligned README, small/medium template wording, and large/phased templates with that distinction.
- Updated large/phased spec and phase-plan templates to inherit the improved small/medium structure while adding anchor-specific phase decomposition and fresh-thread phase execution prompts.

### 2026-07-01_small-medium-plan-template-structure -- label task dependencies in plan template

Meta -- `0.5.0` : `distributable`

#### Changed

- Labeled task dependencies explicitly in the small/medium plan template task guidance and examples.

### 2026-07-01_small-medium-plan-template-structure -- improve plan-template scaffolding

Meta -- `0.5.0` : `distributable`

#### Changed

- Updated the small/medium plan template with input-artifact grounding, spec traceability, implementation/change-surface prompts, SMART task guidance, validation mapping, readable sub-agent strategy blocks, readiness checks, and orchestration saturation guards.
- Clarified that compact model and sub-agent strategy notation applies to substantial small/medium plans as well as large or phased planning artifacts.

### 2026-07-01_small-medium-template-structure -- improve spec-template scaffolding

Meta -- `0.5.0` : `distributable`

#### Changed

- Updated the small/medium spec template with source/intent, scope boundary, repository context, requirements, acceptance criteria, interface/control-flow, risks/rejected alternatives, and readiness checklist prompts while deferring plan-template changes.

### 2026-07-01-naming-conventions: deduplicate naming pattern references

Meta -- `0.5.0` : `distributable`

#### Added

- Added derived naming pattern variables for work-item paths, durable artifact filenames, commit subjects, changelog headings, and variance-log paths.

#### Changed

- Replaced repeated naming grammar in current lifecycle, freeze-gate, quality, template, operator-facing, and validation surfaces with references to the naming owner.

### 2026-07-01-naming-conventions: centralize naming convention rules

Meta -- `0.5.0` : `distributable`

#### Added

- Added a canonical naming conventions reference for work-item IDs, artifact filenames, commit subjects, changelog entries, collision handling, and title normalization.

#### Changed

- Updated lifecycle, router, template, operator-facing, example, and validation surfaces to cite the naming reference and use the new underscore-separated semantic field examples.

### 2026-06-28-implementation-commit-completion: require commit or blocker at implementation completion

Meta -- `0.5.0` : `distributable`

#### Changed

- Clarified that implementation completion with uncommitted implementation changes is exceptional: agents must either create the planned implementation commit or report the exact blocker or explicit no-commit instruction with current worktree status.

### 2026-06-28-changelog-release-sections: group changelog by release

Meta -- `0.5.0` : `distributable`

#### Changed

- Grouped the root changelog under `Unreleased` and `Release 0.1` through `Release 0.4` sections based on the existing release branch contents.
- Updated the harness validator to accept release-grouped changelog entries when checking `0.3.0` release-note sources.

### 2026-06-27-portable-harness-validator: replace PowerShell validator with Python

Meta -- `0.5.0` : `distributable`

#### Changed

- Replaced the PowerShell-only harness validator with a Python standard-library validator and updated current harness validation guidance to use the cross-platform command.

### 2026-06-27-large-phase-orchestration-owner: add large phase orchestration owner

Meta -- `0.5.0` : `distributable`

#### Changed

- Added `rule:lifecycle.large-phase-orchestration` as the lifecycle-owned state sequence for large/phased planning and aligned freeze-gate, model-policy, router, template, and validation references to cite that owner.

### 2026-06-27-phased-planning-orchestration: enforce anchor-spec-first phase planning

Meta -- `0.5.0` : `distributable`

#### Changed

- Clarified large/phased harness guidance so the initial planning package is anchor-spec-only by default, phase-plan drafting starts after anchor freeze and fresh operator instruction, and curated-artifact sub-agents are preferred for bounded phase-plan drafting when justified and supported.
## Release 0.4

### 2026-06-23-documentation-improvements: migrate backlog to Notion

Meta -- `0.4.0` : `repository-only`

#### Changed

- Migrated the active follow-up backlog from root `TODO.md` into a private Notion `Dev Doc Harness Backlog` database with grouped cards, priorities, complexity estimates, dependency notes, and clarified scope.
- Removed root `TODO.md` so the repository no longer carries a duplicate backlog source.

### 2026-06-23-documentation-improvements: improve harness documentation surfaces

Meta -- `0.4.0` : `distributable`

#### Added

- Added a package-local operator note that travels with copied harness packages.
- Added a portfolio-oriented README summary for non-operator readers.

#### Changed

- Clarified that validator evolution should stay structural, graph-oriented, and high-signal instead of becoming a heavy semantic parser.
- Reorganized `TODO.md` into a priority-labeled backlog with consistent item fields and current documentation-review follow-ups.

### 2026-06-17-commit-outcome-reporting: clarify completion reports

Meta -- `0.4.0` : `repository-only`

#### Changed

- Updated the execution-quality gate so completion reports consistently include the commit hash and subject when a commit was created, or state why no commit was created.

### 2026-06-17-freeze-gate-status-reminders: clarify approval reminders

Meta -- `0.4.0` : `repository-only`

#### Changed

- Updated the planning freeze gate to require approved artifacts to move from draft or proposed status to approved status before the approval commit.
- Expanded the post-freeze operator reminder to include compacting the thread alongside pushing or creating a draft plan-only PR.

### 2026-06-14-version-pointer: surface harness version marker

Meta -- `0.4.0` : `distributable`

#### Changed

- Updated the harness entrypoint to point agents at the package-local `VERSION` marker before they stamp work-item artifacts as `unknown`.

### 2026-06-14-commit-message-format: unify commit subject pattern

Meta -- `0.4.0` : `repository-only`

#### Changed

- Changed harness approval commit examples and templates to use the same `SHORT-ID TYPE: TITLE-SNIPPET` pattern as implementation commits, with artifact approval types such as `spec`, `plan`, `phase N plan`, and `amendment NNN`.

### 2026-06-14-commit-message-format: define harness commit message format

Meta -- `0.4.0` : `repository-only`

#### Added

- Added `rule:lifecycle.commit-message-format` as the canonical harness commit-subject policy for short-ID-prefixed approval and typed implementation commits.
- Added planned commit subject sections to the current work-item templates so operators can review commit names alongside specs, plans, phase plans, and amendments.

#### Changed

- Updated freeze-gate, changelog, and README guidance so approval commits use planned subjects and commit title snippets stay synchronized with matching changelog entries.
## Release 0.3

### 2026-06-07-release-versioning: complete Phase 03 release hardening

Meta -- `0.3.0` : `distributable`

#### Added

- Added release validation checks for package identity, release notes, current release-versioning changelog schema, package boundary, template release context, and release routing.
- Added the Phase 03 testing-guide delta and final release validation scenarios for the `0.3.0` checkpoint.

#### Changed

- Updated `0.3.0` release notes and repository validation guidance to include release package consistency checks without adding generated release-note machinery.

### 2026-06-07-release-versioning: complete Phase 02 release package implementation

Meta -- `0.3.0` : `distributable`

#### Added

- Added package-local release identity, release policy, and `0.3.0` release notes under `.agents/skills/dev-doc-harness/`.
- Added `Harness release: <version or unknown>` to current work-item templates.
- Added Phase 02 operator-manual and architecture-summary deltas for package adoption, rollback, and compatibility guidance.

#### Changed

- Routed release/package/adoption work through `module:release` and replaced the broad rule-versioning deferral with the `0.3.0` release-level compatibility model.
- Normalized current release-versioning changelog entries with release target, package impact, and release-note relevance.

### 2026-06-07-release-versioning: complete Phase 01 release policy architecture

Meta -- `0.3.0` : `repository-only`

#### Added

- Added the Phase 01 architecture snapshot defining the `0.3.0` release identity model, distributable package boundary, changelog-to-release-notes contract, release-note shape, compatibility model, artifact release-context decision, team adoption flow, rollback flow, validation direction, and Phase 02 inputs.
- Added the Phase 01 variance log with no variance recorded.

#### Changed

- Established the go-forward changelog schema that records release target, package impact, and release-note relevance so release notes can be curated from changelog entries without turning spec, plan, and implementation entries for the same feature into separate release-note items.
## Release 0.2

### 2026-06-07-followup-hardening: complete implementation

#### Added

- Added structural graph validation for current harness policy owners, references, route budgets, template route consistency, duplicate reusable policy blocks, and tracked work-item Markdown artifacts.
- Added follow-up testing, operator-manual, and architecture-summary deltas for graph validation, tracked work-item history, required model-policy routing, and lifecycle decomposition guidance.
- Added previously ignored historical work-item Markdown artifacts under `docs/work-items` to tracked repository history.

#### Changed

- Removed the local-only `docs/work-items` ignore rule and documented work-item artifacts as repository development history.
- Made `module:models` required for substantial small, medium, and large durable planning routes.
- Documented the structural validation model, route and duplication budgets, and lifecycle decomposition direction in the policy architecture reference.

### 2026-06-07-followup-hardening: approve implementation plan

#### Added

- Added the approved plan, validation test snapshot, architecture snapshot, and variance log for follow-up hardening of tracked work-item docs, model-policy routing, graph validation, route/de-duplication checks, and lifecycle decomposition guidance.

### 2026-06-07-followup-hardening: approve planning package

#### Added

- Added the approved spec for tracking work-item docs, requiring model policy in substantial small/medium planning, structural policy graph validation, route and duplicate-policy checks, and lifecycle-module decomposition planning.

### 2026-06-05-refactor-as-code: complete Phase 05 validation hardening

#### Added

- Added a lightweight harness validation script for current harness files, module and rule IDs, template schema anchors, router routes, safety discoverability, duplicate policy phrases, placeholder checks, and golden traversal scenarios.
- Added a Phase 05 golden scenario snapshot plus testing, operator-manual, and architecture-summary deltas for the validation command and expected review behavior.

#### Changed

- Documented the validation command in README and routed current-surface validation through `SKILL.md`.
- Preserved frozen historical artifacts, the active model-policy selector in `AGENTS.md`, and the rule-versioning deferral while completing Phase 05.

### 2026-06-05-refactor-as-code: approve Phase 05 validation hardening plan

#### Added

- Added the approved Phase 05 plan for lightweight harness validation checks, golden traversal scenarios, validation documentation deltas, and README validation guidance.

#### Changed

- Preserved frozen historical artifacts, the active model-policy selector in `AGENTS.md`, and the rule-versioning deferral for Phase 05.

### 2026-06-05-refactor-as-code: complete Phase 04 entrypoint docs

#### Changed

- Updated `SKILL.md` into an operation router that sends common harness work to canonical modules, supplemental references, templates, and current work-item artifacts.
- Aligned root `AGENTS.md` as the repository bootstrap and active model-policy selector while keeping detailed lifecycle policy in routed canonical references.
- Refreshed README operator guidance to explain the router, ownership map, canonical module references, and README's non-normative summary role.
- Kept Phase 04 out of templates and frozen historical work-item artifacts, and preserved the `AGENTS.md` active model-policy selector.

### 2026-06-05-refactor-as-code: approve Phase 04 entrypoint docs plan

#### Added

- Added the approved Phase 04 plan for updating `SKILL.md`, root instructions, README, and compact compatibility guidance to route through the canonical module and rule ownership map.

#### Changed

- Preserved the active model-policy selector in `AGENTS.md`, the rule-versioning deferral, and the boundary that Phase 04 must not rewrite templates or frozen historical work-item artifacts.

### 2026-06-05-refactor-as-code: centralize active model policy wording

#### Changed

- Clarified that `AGENTS.md` is the single repository-local selection point for the active model policy.
- Replaced repeated `economy-default` default wording in current README, template examples, and model-policy examples with active-policy wording.

### 2026-06-05-refactor-as-code: complete Phase 03 template slimming

#### Added

- Added compact schema IDs and canonical policy-reference anchors to the current harness templates.

#### Changed

- Reduced reusable sub-agent authorization, variance handling, and freeze-gate procedure prose in templates while preserving artifact-shape prompts and fresh-thread usability.
- Kept Phase 03 scoped to templates and `CHANGELOG.md`; `SKILL.md`, `README.md`, root `AGENTS.md`, canonical references, and historical work-item artifacts were not updated.

### 2026-06-05-refactor-as-code: approve Phase 03 template slimming plan

#### Added

- Added the approved Phase 03 plan for slimming harness templates with schema IDs, canonical policy citations, reduced reusable policy prose, preserved fresh-thread usability, and an operator-selected `enterprise-default` policy for Phase 03.

### 2026-06-05-refactor-as-code: complete Phase 02 canonical modules

#### Added

- Added `policy-architecture.md` as the compact canonical module catalog and rule-interface reference for the harness.
- Added stable module and rule IDs to current canonical references, including lifecycle, freeze-gate, model/sub-agent, quality, execution-quality, evidence, and role-example ownership.

#### Changed

- Labeled evidence and role-example references as supplemental or advisory so examples do not become competing policy.
- Kept `artifact-contract.md` intact for Phase 02, using an ownership block instead of splitting the lifecycle reference.

### 2026-06-05-refactor-as-code: approve Phase 02 canonical modules plan

#### Added

- Added the approved Phase 02 plan for creating a canonical policy architecture reference, declaring module and rule IDs in current canonical references, preserving detailed rule ownership, and deferring template, README, root instruction, and entrypoint updates to later phases.

### 2026-06-05-refactor-as-code: complete Phase 01 policy architecture

#### Added

- Added the Phase 01 architecture snapshot defining precedence, dependency direction, content taxonomy, operation routing, rule-interface conventions, validation budgets, golden scenario tests, work-item artifact locality, Phase 02 inputs, and open risks.
- Added the Phase 01 variance log with no variance recorded.

#### Changed

- Recorded the explicit rule-versioning deferral so later phases use stable rule IDs without introducing a full versioning system in Phase 01.

### 2026-06-05-refactor-as-code: approve Phase 01 policy architecture plan

#### Added

- Added the approved Phase 01 plan for producing a policy architecture snapshot, variance log, rule-interface conventions, operation router taxonomy, validation budgets, golden scenario tests, and work-item artifact locality guidance using the selected `enterprise-default` policy.

### 2026-06-05-refactor-as-code: approve architecture guardrails amendment

#### Added

- Added the approved amendment requiring Phase 01 to define precedence, dependency direction, content types, operation routing, measurable architecture checks, golden scenario tests, and work-item artifact locality while deferring full rule versioning.

### 2026-06-05-refactor-as-code: approve anchor spec

#### Added

- Added the approved large/phased anchor spec for refactoring harness instructions as maintainable policy modules with stable rule interfaces, slimmer templates, retrieval routing, and validation hardening.

## Release 0.1

### 2026-06-05-subagent-context-strategy: implement context strategy field

#### Changed

- Added `Context strategy` to the canonical sub-agent strategy notation, templates, and role examples.
- Documented curated prompt, curated artifacts, full-history fork, and no repo context strategies, including full-history fork inheritance trade-offs.
- Extended de-facto sub-agent reporting to include actual context strategy and observed context/model inheritance behavior.
- Updated the README operator flow to treat context strategy as part of model, reasoning-effort, and sub-agent planning.

### 2026-06-05-subagent-context-strategy: approve planning package

#### Added

- Added the approved spec and plan for making sub-agent context strategy a first-class planning field, including curated context options, full-history fork guidance, and de-facto context reporting.

### 2026-06-05-subagent-autonomy-policy: implement approved sub-agent autonomy behavior

#### Changed

- Updated the canonical sub-agent policy so substantial plans proactively assess justified sub-agent use instead of treating missing operator mention as a prohibition.
- Clarified that approved frozen plans authorize their listed sub-agent strategy after normal post-freeze implementation authorization, while preserving fresh confirmation for unplanned or escalated delegation.
- Reframed the normal sub-agent cap as three concurrent sub-agents, with wave-based long-running use allowed when approved.
- Added de-facto sub-agent and model/model-class reporting expectations to policy, templates, and operator-facing documentation.

### 2026-06-05-subagent-autonomy-policy: approve planning package

#### Added

- Added the approved spec and plan for proactive sub-agent strategy planning, approved-strategy authorization, 3-concurrent-sub-agent limits, wave-based long-running use, and de-facto sub-agent/model reporting.

### 2026-06-01-collapse-execution-approval: clarify ambiguous confirmation follow-up

#### Changed

- Clarified that agents should ask a concise follow-up when execution settings are confirmed without clear start authorization, instead of passively waiting for another implementation instruction.

### 2026-06-01-collapse-execution-approval: implement combined start confirmation

#### Changed

- Updated the planning freeze gate so the post-freeze prompt combines execution-setting confirmation with whether implementation should begin now.
- Clarified that clear post-gate start responses can satisfy both confirmation and implementation authorization while ambiguous settings-only confirmations remain insufficient.
- Aligned plan templates and the README operator flow with the combined post-freeze confirmation behavior.

### 2026-06-01-collapse-execution-approval: approve planning package

#### Added

- Added the approved spec and plan for combining post-freeze execution-setting confirmation with implementation authorization when the operator clearly says to begin.

### 2026-05-31-local-planning-docs-distribution: keep repo planning docs local

#### Changed

- Ignored this repository's local `docs/work-items/` planning packages so they are not treated as distributable project content.
- Documented the contribution convention that harness changes, user-facing documentation, and changelog entries are tracked, while this repo's own planning packages remain local.

### 2026-05-31-work-items-artifact-root: implement work item package layout

#### Changed

- Moved the canonical harness package root to `docs/work-items/<work-id>/`, added short-ID durable artifact filenames, and flattened package documentation into `snapshots/` and `deltas/`.
- Clarified Superpowers compatibility so `docs/superpowers` files may only be minimal pointer stubs to canonical `docs/work-items/<work-id>/` packages.
- Migrated existing local planning packages into the new `docs/work-items/` layout.

### 2026-05-31-work-items-artifact-root: approve planning package

#### Added

- Added the approved spec and plan for moving durable harness planning packages to `docs/work-items/<work-id>/`, adding short-ID artifact filenames, flattening snapshots and deltas, and clarifying Superpowers pointer-stub compatibility.

### 2026-05-31-planning-approval-freeze-flow: implement approval-first freeze flow

#### Changed

- Updated the canonical freeze-gate workflow so agents stage draft planning artifacts for approval without committing, revise drafts directly on feedback, and freeze planning packages only after explicit approval and commit.
- Aligned the skill entry point, artifact lifecycle reference, durable planning quality reference, templates, and README with the approval-first planning review loop.

### 2026-05-31-planning-approval-freeze-flow: approve planning package

#### Added

- Added the approved spec and plan for changing the harness planning lifecycle so draft review stages artifacts without committing, feedback edits drafts directly, and the freeze happens only after explicit approval and commit.

### 2026-05-28-work-item-scope: broaden harness beyond features

#### Changed

- Reframed the harness artifact contract around substantial work items, including features, bug fixes, prior issue investigations, refactors, migrations, and documentation/process changes.
- Updated the skill, README, templates, and references so substantial bug fixes and investigations use the same durable planning, documentation, variance, and freeze-gate quality bar as features.
- Renamed reusable template files from feature-specific names to work-item names matching the small/medium and large/phased sizing model.

### 2026-05-28-template-durable-spec-hardening: complete TODO items

#### Changed

- Expanded plan and large-feature spec template sub-agent strategy prompts with the required policy fields for safe delegation and operator confirmation.
- Aligned the canonical sub-agent policy notation example with the required field list.
- Clarified model-policy wording so the human operator is not described as mismatched to the work.
- Expanded the large-feature spec template with explicit durable-spec sections for behavior, interfaces, state flow, safety, validation, operations, unknowns, and rejected alternatives.
- Removed the completed template-hardening follow-ups from `TODO.md`.

### 2026-05-28-review-hardening: address review feedback

#### Added

- Added TODO follow-ups for full sub-agent strategy fields in plan templates and explicit durable-spec sections in the large-feature spec template.

#### Changed

- Changed copied template references to point to repository-root harness reference paths.
- Clarified freeze-gate commits must stage only finalized planning artifacts and `CHANGELOG.md`, excluding unrelated worktree changes.

### 2026-05-26-root-readme: explain operator process impact

#### Added

- Added `README.md` with an operator-focused overview of how the harness changes development process, pause points, handoffs, variance handling, and outcomes.
- Added a compact styled Mermaid flow diagram to show the operator-facing harness loop.

#### Changed

- Clarified the README diagram with separate small, small/medium, and large/phased paths plus an explicit normal implementation flow.

### 2026-05-26-agentic-instruction-extraction: add reusable references

#### Added

- Added concise references for context loading, quality gates, sub-agent role examples, and evidence/report artifacts.
- Added TODO follow-ups using only public repository references for extracted instruction patterns.

#### Changed

- Clarified when to skip loading supplemental evidence/report artifact guidance.
- Removed completed TODO items for the fake small-feature harness test and common sub-agent role examples.

### 2026-05-26-agentic-instruction-research: track cross-repo review

#### Added

- Added a TODO item to review public repositories, including `https://github.com/itxyzzz/gen-ai-se-hw`, for reusable agentic instruction patterns.

### 2026-05-25-root-todo: collect future harness work

#### Added

- Added `TODO.md` with remaining future work from the original handoff and follow-up design discussion.
- Grouped future work from near-term validation through riskier adapter, governance, and process-maturity additions.

### 2026-05-25-durable-planning-quality: strengthen planning and model policy

#### Added

- Added `durable-planning-quality.md` as the canonical quality bar for durable specs, phase plans, and handoff preservation.
- Added model and sub-agent strategy requirements that account for orchestration fit, risk, ambiguity, blast radius, budget, and latency.
- Added sub-agent report and final integration ownership requirements.

#### Changed

- Strengthened large feature templates to require fresh-thread executable phase plans and explicit model/reasoning fit assessment.

### 2026-05-25-freeze-gate-reference: consolidate freeze-gate rules

#### Added

- Added `planning-freeze-gates.md` as the canonical reference for commit-and-pause gates.

#### Changed

- Replaced repeated freeze-gate explanations in the skill, artifact contract, and templates with short references to the canonical freeze-gate document.

### 2026-05-25-planning-freeze-gates: commit-and-pause planning workflow

#### Added

- Added mandatory Planning Artifact Freeze Gates for finalized specs, plans, phase plans, and plan amendments.
- Added draft plan-only PR reminders and model or reasoning confirmation requirements at each freeze gate.
- Added support for multiple freeze gates across anchor specs, phase-plan batches, and high-impact amendments for very large features.

### 2026-05-25-harness-review-updates: tighten artifact workflow

#### Added

- Added root changelog requirements to the harness workflow and artifact contract.
- Added issue-tracker-aware feature ID guidance for specs, plans, amendments, and variance logs.
- Added large-feature spec handoff requirements so phase plans preserve initial planning decisions.

#### Changed

- Simplified harness invocation guidance to use it for all development work except very small mechanical edits.
- Clarified that sub-agent notation and large-feature spec rows are examples to replace, not required phase or agent choices.
- Flattened large-feature phase plans and amendments into `specs/<feature-id>/` as `plan-phase-NN-*.md` and `plan-amendment-NNN-*.md`.

#### Removed

- Removed person-oriented approval fields from spec and plan templates; superseded artifacts now reference the artifact that replaces them.
