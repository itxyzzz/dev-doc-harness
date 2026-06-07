# Refactor As Code Architecture Snapshot

Work ID: `2026-06-05-refactor-as-code`
Source spec: `../spec-refactor-as-code.md`
Source amendment: `../plan-amendment-001-architecture-guardrails-refactor-as-code.md`
Status: Final

## Goal

Define the target policy architecture for the repository-local documentation harness before later phases move policy text, slim templates, or update public routing. This snapshot is the Phase 01 handoff for preserving current safeguards while making the harness behave like a small policy library with canonical owners, stable rule interfaces, explicit retrieval paths, and measurable drift controls.

Phase 01 does not move existing harness behavior. Later phases must treat this snapshot as the architecture contract for reorganizing canonical references, templates, the skill entrypoint, root instructions, README summaries, and validation checks.

## Precedence and Authority Model

Conflict order, highest authority first:

| Rank | Source | Authority rule |
|---:|---|---|
| 1 | System, developer, tool, sandbox, and platform constraints | Always win. Repository policy cannot permit an action that these constraints prohibit, and cannot waive required tool or safety behavior. |
| 2 | Current operator instruction | Wins over repository defaults when it is explicit and does not conflict with rank 1. The operator may select model policy, execution scope, phase authorization, and approved exceptions. |
| 3 | Repository `AGENTS.md` and nested applicable `AGENTS.md` files | Bootstrap repository-local harness behavior and repository-specific overrides. More specific nested instructions apply to their subtree unless rank 1 or 2 says otherwise. |
| 4 | Repository-local `dev-doc-harness` `SKILL.md` | Public harness entrypoint and operation router. It determines which canonical references, templates, or supplemental references an agent should load. |
| 5 | Canonical references under `.agents/skills/dev-doc-harness/references/` | Own reusable normative policy, artifact lifecycle rules, quality bars, model and sub-agent policy, and supplemental evidence guidance. |
| 6 | Approved and frozen work-item artifacts | Own work-specific decisions, selected policy IDs, approvals, exceptions, variance records, and phase scope for that work item. Frozen artifacts do not silently override current canonical policy unless they record an explicit approved exception or phase-specific operator decision. |
| 7 | Templates under `.agents/skills/dev-doc-harness/assets/templates/` | Own artifact shape, required sections, and prompts for work-specific decisions. Templates do not own reusable policy beyond references to canonical rule IDs or schemas. |
| 8 | README and operator-facing summaries | Explain usage and outcomes. They may link to canonical owners, but they are not normative when a canonical reference differs. |
| 9 | Examples, sample rows, and historical artifacts from unrelated work items | Advisory only unless a current plan explicitly adopts them. Examples must not become hidden policy. |

Frozen work-item artifacts preserve historical decisions and review evidence. Current canonical policy controls execution for future work unless a frozen artifact records an explicit approved exception, such as a phase-specific model policy, a documented variance, or an amendment approved by the operator. If a frozen artifact appears to conflict with current safety-critical canonical policy and does not record an explicit approved exception, later agents must follow current canonical policy and record the mismatch as context, not rewrite the frozen artifact.

The repository `AGENTS.md` currently sets `economy-default` as the active default model policy, while Phase 01 execution was explicitly authorized by the operator with `enterprise-default` and latest strongest available architecture review. That operator instruction controls this phase only and does not permanently change repository policy.

## Dependency Graph

Allowed dependency direction:

```text
System/developer/tool constraints
  -> Operator instruction
    -> AGENTS.md and nested AGENTS.md
      -> SKILL.md operation router
        -> Canonical references
          -> Supplemental references
        -> Templates
        -> Work-item artifacts
      -> README/operator summaries
```

Required and allowed edges:

| Source | May reference | Rules |
|---|---|---|
| `AGENTS.md` | Repository-local `SKILL.md`; repository-specific overrides such as active model policy | Bootstrap only. Keep detailed lifecycle, template, and validation policy in canonical references. |
| `SKILL.md` | Operation router, canonical references, supplemental references, templates | Route by operation. Avoid requiring every reference for every task. |
| Canonical references | Other canonical references only when the dependency is part of the public rule interface | Name dependencies explicitly. Avoid circular authority and deep chains for common operations. |
| Supplemental references | Canonical references and bounded optional guidance | Provide examples, evidence/report patterns, or environment compensation without becoming required for every operation. |
| Templates | Artifact schemas, canonical module IDs, rule IDs, and short reminders | Capture artifact shape and work-specific prompts. Do not restate long reusable policy blocks. |
| Work-item artifacts | Approved plans, selected decisions, statuses, approvals, exceptions, variance entries, cited rule IDs, validation evidence | Record the work item's contract and history. Do not become the canonical source for future reusable policy. |
| README | `AGENTS.md`, `SKILL.md`, canonical reference names, high-level diagrams | Summarize operator outcomes and retrieval entrypoints. Do not own normative rules. |

Banned back-references:

- Canonical references must not depend on README summaries for policy meaning.
- Canonical references must not depend on templates for normative text.
- Templates must not copy long sub-agent authorization, variance, or freeze-gate procedure prose after Phase 03; they should cite policy IDs and artifact sections instead.
- Historical work-item artifacts must not be edited to simulate current policy.
- Examples must not be cited as mandatory policy unless promoted into a canonical reference.
- Future validation scripts or checklists must not become the only copy of a lifecycle rule; they enforce canonical owners.

Maximum intended graph shape for common operations is shallow: root instructions route to `SKILL.md`, `SKILL.md` routes to one to three canonical references or templates, and work-item artifacts record decisions without adding another reusable-policy layer.

## Content-Type Taxonomy

| Content type | Definition | Allowed locations | Authoritative as policy? | Later-phase handling |
|---|---|---|---:|---|
| Normative policy | Reusable instructions that agents must follow for lifecycle, authority, safety, model choice, variance, artifact ownership, or validation. | `AGENTS.md` for bootstrap and repository overrides; `SKILL.md` for routing; canonical references for detailed rules. | Yes, according to precedence. | Assign one owner per rule family. Convert duplicated copies to rule IDs or links. |
| Artifact schema | Required shape of specs, plans, snapshots, deltas, reports, and variance logs. | Templates and canonical schema sections or future schema reference. | Yes for artifact structure; no for unrelated lifecycle policy. | Keep schemas executable by fresh agents while moving long reusable policy to canonical owners. |
| Example | Sample role rows, sample work IDs, sample plan entries, or illustrative prompts. | Templates, supplemental references, README examples. | No, unless explicitly adopted by a current plan or promoted into a canonical rule. | Label examples visibly. Remove placeholder-like text from finalized artifacts. |
| Advisory guidance | Recommended techniques, diagnostics, environment compensation, review patterns, or optional role patterns. | Supplemental references and brief canonical reference subsections. | Conditionally: follow when invoked by the router or plan, but it does not override normative owners. | Keep optional and bounded. Avoid hidden requirements in advisory text. |
| Operator-facing summary | Human-readable overview of outcomes, flow, and repository usage. | README, root instructions, handoff summaries. | No when it conflicts with canonical references; yes only for explicit repository-local overrides in `AGENTS.md`. | Link to owners. Do not duplicate detailed procedure. |
| Historical snapshot | Approved, frozen, or handed-off work-item artifact preserving decisions at a time. | `docs/work-items/<work-id>/`, especially specs, phase plans, amendments, snapshots, and variance logs. | Yes for that work item's approved decisions and exceptions; no for reusable future policy. | Preserve immutability. Add amendments or new snapshots for high-impact changes instead of rewriting. |

Future phases should trim or rewrite text based on this taxonomy. If prose tells all future agents what they must do, it belongs in a normative owner. If prose tells a specific work item what was approved, it belongs in that work item. If prose merely illustrates a possible row or prompt, it must be marked as example content and must not carry hidden policy.

## Operation Router Taxonomy

The Phase 02 and Phase 04 router should use operation-oriented retrieval rather than eager-loading all core references.

| Operation | Required references or module categories | Safety-critical rules | Max traversal depth |
|---|---|---|---:|
| Classify work size | `AGENTS.md`; `SKILL.md`; artifact contract sizing rules | Very small mechanical skip is explicit and narrow; substantial development uses harness artifacts. | 3 |
| Draft small/medium spec and plan | Artifact contract; durable planning quality; small/medium templates; model/sub-agent policy if substantial | Work item folder and short ID; documentation matrix; sub-agent strategy or `None`; draft remains uncommitted before approval. | 4 |
| Draft large anchor spec | Artifact contract; durable planning quality; large/phased spec template; model/sub-agent policy | Anchor spec preserves handoff decisions and phase decomposition; phase plans derive from spec. | 4 |
| Draft phase plan | Approved anchor spec and amendments; durable planning quality; phase-plan template; model/sub-agent policy; artifact contract for variance reminders | Do not narrow or reinterpret frozen spec decisions; phase plan must be fresh-thread executable. | 4 |
| Freeze planning package | Planning freeze gates; artifact contract changelog and immutability rules; current work-item artifacts | Stage draft first; commit only approved planning artifacts and `CHANGELOG.md`; stop before implementation until fresh operator start authorization. | 4 |
| Execute approved phase | Approved spec, amendments, and phase plan; artifact contract variance policy; context and quality gates; validation commands from phase plan | Stay in approved scope; do not edit frozen plans to hide drift; update changelog before commit. | 4 |
| Record implementation variance | Artifact contract variance policy; existing variance log; approved plan or amendment | High-impact architecture/API/data/security/scope/feasibility variance requires amendment and operator approval before continuing. | 4 |
| Use or review sub-agent strategy | Sub-agent model policy; sub-agent role examples when useful; approved plan strategy | Use approved strategy after post-freeze authorization; fresh confirmation for unplanned or escalated delegation; report de-facto use. | 4 |
| Review durable artifact quality | Durable planning quality; planning freeze gates when reviewing draft/freeze state; artifact contract documentation matrix | No placeholders, undecided required items, or missing required sections unless explicitly deferred with owner and reason. | 4 |
| Update templates | Architecture snapshot; artifact contract or future schema owner; canonical policy modules; affected templates | Templates own shape, not long reusable policy. Preserve fresh-thread usability. | 4 |
| Handle Superpowers or spec-kit compatibility | `AGENTS.md`; artifact contract compatibility; `SKILL.md` compatibility notes; relevant external workflow rules | Harness owns artifact location and lifecycle; do not duplicate full specs or plans in alternate locations. | 4 |
| Update README/operator guidance | Architecture snapshot; canonical owners for referenced behavior; README | README summarizes and links; it does not become competing policy. | 3 |

The router should identify supplemental references separately from required references. For example, evidence/report guidance is required for evidence-heavy work, not for routine Phase 01 documentation execution.

## Rule Interface Conventions

Later phases should use stable, manually maintained IDs for reusable policy and module surfaces. The ID scheme should be simple enough to read in prose and search with `rg`.

Recommended shape:

```text
module:<area>
rule:<area>.<short-name>
schema:<artifact>.<short-name>
scenario:<area>.<short-name>
metric:<area>.<short-name>
```

Examples:

| ID | Intended owner | Meaning |
|---|---|---|
| `module:lifecycle` | Artifact contract or future lifecycle reference | Work item lifecycle, snapshots, variance, changelog, and amendments. |
| `module:freeze-gate` | Planning freeze gates reference | Draft review and approval freeze procedure. |
| `module:models` | Sub-agent model policy reference | Model, reasoning, sub-agent authorization, and reporting. |
| `module:quality` | Durable planning quality reference | Spec and phase-plan handoff quality bars. |
| `rule:lifecycle.immutable-snapshots` | Lifecycle owner | Frozen planning artifacts are not silently rewritten. |
| `rule:freeze.stop-before-implementation` | Freeze-gate owner | Approval commits pause before implementation until fresh start authorization. |
| `rule:models.approved-strategy-authorized` | Model policy owner | Approved sub-agent strategy is authorized after post-freeze implementation start. |
| `schema:plan.phase` | Phase-plan template or future schema owner | Required shape for large/phased phase plans. |
| `metric:router.max-depth` | Future validation owner | Common operation traversal stays within the budget in this snapshot. |

Conventions:

- IDs are stable anchors, not prose replacements. The canonical owner still states the rule in normal language.
- IDs should appear near the canonical rule heading or owner table and may be cited by templates and work-item artifacts.
- IDs should be lowercase, ASCII, kebab-case or dot-separated, and easy to search.
- Do not encode dates or full semantic versions in Phase 02 IDs.
- Use `Superseded by:` notes or errata for changed IDs until a later versioning system exists.
- Templates may cite IDs in compact reminders, but should avoid copying the full rule text unless fresh-thread executability requires a short local summary.
- Work-item artifacts may cite selected IDs and record approved exceptions. They should not reproduce whole canonical modules.

## Architectural Metrics and Budgets

Later validation should be able to pass or fail these budgets:

| Metric ID | Budget | Validation direction |
|---|---:|---|
| `metric:router.max-depth` | Common operations should traverse no more than 4 repository harness layers after system/operator context: `AGENTS.md` -> `SKILL.md` -> canonical owner -> template or artifact. README update operations should traverse no more than 3. | Manual review in Phase 02-04; automated link graph if added in Phase 05. |
| `metric:router.eager-reference-count` | `SKILL.md` should require at most 3 canonical references for any routine operation before optional supplemental references. Freeze execution may require 4 when changelog/immutability and quality checks are separate. | Router table review and sample scenario tests. |
| `metric:router.eager-word-budget` | Initial required reading for routine classify/draft/freeze paths should target 3,000 words or less after `AGENTS.md` and current work-item artifacts; large anchor and final review paths may target 5,000 words. | Word-count sampling in Phase 05. |
| `metric:template.duplicated-policy-prose` | No template should contain more than one short paragraph or five bullets of reusable policy for the same rule family. Long freeze, variance, and sub-agent authorization blocks should be replaced by owner references and IDs. | `rg` phrase searches and manual review. |
| `metric:policy.duplicate-block` | No reusable policy block of 40 or more near-identical words should appear in more than one non-historical current harness file unless the duplication is an intentional short summary. | Phase 05 duplicate prose check or reviewer checklist. |
| `metric:references.broken-tolerance` | Zero broken reference paths, broken rule IDs, or missing canonical owners in current harness files. | Static path and ID checks. |
| `metric:safety.discoverability` | Freeze gate, variance/amendment policy, changelog-before-commit rule, and model/sub-agent policy must each be discoverable from `AGENTS.md` through `SKILL.md` in no more than 3 clicks or path opens. | Golden scenario review. |
| `metric:historical.no-rewrite` | Zero broad rewrites of frozen historical work-item artifacts for policy-drift cleanup. | Diff review and git path checks. |

These budgets are targets for the refactor, not retroactive pass/fail gates for Phase 01. Phase 05 should turn the feasible subset into automated or checklist validation.

## Golden Scenario Tests

Golden scenarios define expected behavior that the refactor must preserve. Phase 05 should convert these into static checks, sample traversal tests, or review scripts where practical.

| Scenario ID | Setup | Expected loaded references | Expected behavior |
|---|---|---|---|
| `scenario:work-size.very-small-skip` | Operator asks for a typo or tiny mechanical edit with no durable artifact request. | `AGENTS.md`; `SKILL.md` sizing route or artifact contract sizing section. | Agent may explicitly classify as very small mechanical, preserve behavior, run relevant checks, and skip work-item artifacts. |
| `scenario:planning.small-medium` | Operator asks for a bounded substantial bug fix or documentation/process change. | `AGENTS.md`; `SKILL.md`; artifact contract; durable planning quality; small/medium templates; model policy if sub-agent strategy is assessed. | Agent creates `docs/work-items/<work-id>/spec-<short-id>.md`, `plan-<short-id>.md`, documentation matrix, and model/sub-agent strategy or `None`; stages drafts without committing before approval. |
| `scenario:planning.large-anchor-freeze` | Operator asks for a broad or phased refactor. | `AGENTS.md`; `SKILL.md`; artifact contract; durable planning quality; large/phased spec template; planning freeze gates. | Agent drafts an anchor spec preserving scope, non-scope, assumptions, risks, rejected alternatives, acceptance criteria, phase decomposition, documentation matrix, and freeze-gate approval path; freezes only after approval and changelog commit. |
| `scenario:planning.phase-plan-freeze` | Anchor spec is frozen and operator asks for Phase NN planning. | Frozen anchor spec and amendments; durable planning quality; phase-plan template; planning freeze gates; model policy. | Agent drafts a fresh-thread executable phase plan that preserves anchor decisions, stages for review, commits only after approval, and stops before implementation. |
| `scenario:execution.post-freeze-authorization` | Phase plan is approved and operator gives clear start authorization plus model/reasoning policy choices. | Approved spec, amendments, phase plan; artifact contract variance rules; context and quality gates; validation commands. | Agent executes only the approved phase scope, updates variance log as needed, updates changelog before commit, and does not ask for a second sub-agent-specific confirmation for approved strategy. |
| `scenario:variance.high-impact-amendment` | Implementation discovers a post-freeze change to architecture, public API, data, security, privacy, compliance, scope, acceptance criteria, or feasibility. | Artifact contract variance policy; planning freeze gates; current approved plan. | Agent stops, drafts a `plan-amendment-NNN-short-title-<short-id>.md`, stages for approval, and does not continue implementation until the amendment is frozen and execution is reauthorized. |
| `scenario:models.sub-agent-authorization` | Approved plan includes a bounded reviewer or worker strategy. | Sub-agent model policy; optional role examples; approved plan strategy. | Agent may use approved strategy after post-freeze implementation authorization; asks for fresh confirmation only for unplanned agents, stronger unrecorded model/reasoning, write-scope escalation, platform-restricted actions, or more than 3 concurrent agents. |
| `scenario:compat.superpowers` | Superpowers is installed and active for normal development methodology. | `AGENTS.md`; `SKILL.md`; artifact contract compatibility; relevant Superpowers skill. | Superpowers may own brainstorming, execution, review, or TDD method, while the harness owns artifact location, planning freeze gates, variance records, changelog, and model/sub-agent policy notation. |
| `scenario:history.historical-artifact-handling` | Current policy differs from an old frozen work-item artifact that did not record an explicit exception. | Artifact contract immutable snapshot rules; current canonical reference for the rule family; historical artifact if relevant. | Agent follows current canonical policy for new execution, treats old artifact as historical evidence, and avoids rewriting it to hide drift. |

## Work-Item Artifact Locality

This repository generally ignores `docs/work-items/` because ordinary harness-development planning packages are local working notes, not distributable project content. The current `docs/work-items/AGENTS.md` expresses that default.

This refactor work item is an explicit exception because the operator approved and froze the planning package as repository-tracked architecture work for the harness itself. The approved Phase 01 plan also states that the work item's Phase 01 artifacts must be force-added even though the directory is ignored.

Locality rules:

- Default: harness-development work-item artifacts under `docs/work-items/` remain local-only and should not be staged, committed, packaged, or distributed.
- Exception: a harness-development work item may be tracked when the operator explicitly approves tracking or when a frozen plan for the harness itself requires tracked planning artifacts.
- Force-add required: ignored but approved tracked artifacts under `docs/work-items/` must be added with `git add -f`.
- Scope discipline: when force-adding work-item artifacts, stage only the approved work-item paths and the required `CHANGELOG.md` entry.
- Preservation: future agents must not assume ignored means disposable when `git ls-files docs/work-items/<work-id>` already shows tracked approved artifacts.
- Cleanup: do not remove tracked work-item artifacts merely to satisfy the default local-only convention. Use a future approved cleanup plan if distribution policy changes.

For this work item, Phase 01 must track:

- `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`

## Rule Versioning Deferral

Phase 01 does not create a full rule versioning system. Rule IDs and module IDs introduced by later phases are stable identifiers for retrieval, ownership, and drift checks during this refactor, not a complete compatibility or migration framework.

Later phases must avoid choices that would prevent future versioning, deprecation, or supersession metadata. In particular:

- Keep IDs stable and search-friendly.
- Avoid encoding transient dates or implementation details into IDs.
- Prefer `Superseded by:` notes, errata, or explicit replacement mappings when an ID changes.
- Do not require historical work-item artifacts to update their cited IDs after freeze.
- Leave room for a future rule manifest to add fields such as owner, status, introduced-in, superseded-by, and compatibility notes.

Full rule versioning remains future work unless the operator explicitly expands scope with an approved amendment.

## Phase 02 Inputs

Phase 02 must consume these decisions before reorganizing canonical references:

- Authority order: canonical references own reusable policy; templates and README do not.
- Current canonical owners: `artifact-contract.md` owns layout, lifecycle, changelog, variance, immutable snapshots, and Superpowers compatibility; `planning-freeze-gates.md` owns draft review and approval freeze; `subagent-model-policy.md` owns model/sub-agent selection and reporting; `durable-planning-quality.md` owns spec and plan quality.
- Potential module surfaces: lifecycle, freeze gate, models, quality, schemas, compatibility, validation, and optional evidence/report guidance.
- Dependency rule: references may cite other references only through explicit rule-interface dependencies and should avoid cycles.
- Router budget: common operations should need at most 3 canonical references before optional supplemental context; freeze/execution may need 4.
- Template direction: templates should keep artifact shape and work-specific prompts while replacing long reusable policy prose with owner references and IDs.
- Validation direction: Phase 05 should check broken paths/rule IDs, duplicated policy prose, template policy blocks, traversal depth, and discoverability of freeze, variance, changelog, and model/sub-agent rules.
- Historical handling: old frozen work-item artifacts are historical snapshots and are not migration targets for copied policy cleanup.
- Locality exception: this refactor work item's approved artifacts are tracked with `git add -f`; the default local-only docs/work-items rule still applies otherwise.

Phase 02 should decide whether to split `artifact-contract.md`, add a compact ownership map/manifest first, or keep files intact with explicit section IDs. It should favor the smallest change that makes ownership, retrieval, and later template slimming safe.

## Open Risks

- Over-splitting canonical references could improve ownership while making traversal deeper; Phase 02 should use router budgets before creating new files.
- Keeping canonical references intact but adding many IDs could reduce churn while leaving files too broad; Phase 02 must judge whether section-level ownership is enough.
- Templates need enough local guidance for fresh-thread executability; Phase 03 should avoid making them so terse that agents miss required fields.
- Duplicate-prose detection can produce false positives for short safety summaries; Phase 05 should distinguish intentional summaries from copied policy blocks.
- README and root instructions may need careful wording in Phase 04 so operator-facing summaries remain helpful without competing with canonical references.
- Rule IDs may become stale if later phases do not assign explicit owners and drift checks; Phase 05 should validate all current references.

No open risk discovered in Phase 01 changes scope, acceptance criteria, architecture/API/data/security behavior, or plan feasibility. No amendment is required before Phase 02 planning.
