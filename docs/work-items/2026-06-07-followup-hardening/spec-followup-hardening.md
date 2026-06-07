# Harness Follow-up Hardening Spec

Work ID: `2026-06-07-followup-hardening`
Short ID: `followup-hardening`
Status: Approved
Schema: `schema:spec.small-medium`
Policy references: `module:lifecycle`, `module:quality`, `module:models`, `module:architecture`, `rule:lifecycle.documentation-matrix`, `rule:quality.spec-handoff`

## Goal

Address the highest-value gaps found after the refactor-as-code implementation: remove the remaining work-item tracking conflict, require model/sub-agent policy for substantial small/medium plans, strengthen policy graph validation, add route/de-duplication checks, and prepare a controlled split of the broad lifecycle module.

The desired outcome is a harness that is more internally consistent and harder to drift: tracked planning docs are no longer contradicted by nested instructions, substantial plans always load model policy, and validation checks the policy graph itself rather than only checking selected strings.

## Scope

- Remove `docs/work-items/AGENTS.md` and stop treating work-item artifacts as local-only for this repository.
- Track all historical `docs/work-items/` artifacts that are present in the repository working tree, including earlier planning packages.
- Update repository documentation and validation expectations so tracked work-item docs are allowed and preserved.
- Update the small/medium planning route so `module:models` is required for substantial small/medium specs and plans.
- Improve graph validation in `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`.
- Add validation for route depth and duplicated reusable policy blocks.
- Add an architecture/design step for splitting or decomposing `references/artifact-contract.md` after graph validation is stronger.

## Non-scope

- Implementing full rule versioning or semantic compatibility metadata for rule IDs.
- Rewriting frozen historical artifacts to modernize old policy prose.
- Changing the active repository model policy from `economy-default`.
- Removing the planning freeze gate, changelog discipline, immutable snapshots, or variance/amendment behavior.
- Replacing the current PowerShell validation script with a separate build system.
- Completing the lifecycle split in the same step as the first graph-validation hardening, unless the approved plan explicitly sequences it after validation safeguards.

## Current state

The refactor-as-code work made the harness substantially more modular:

- `SKILL.md` is now an operation router.
- `references/policy-architecture.md` defines module IDs, rule ID conventions, content types, dependency direction, router inputs, and rule-versioning deferral.
- Templates now carry schema anchors and policy-reference lists instead of long copied policy blocks.
- `Test-HarnessPolicy.ps1` checks required files, selected module/rule IDs, template anchors, routes, safety discoverability, copied phrases, placeholders, and golden traversal evidence.

Remaining gaps:

- `docs/work-items/AGENTS.md` says work-item planning docs must not be staged or committed, but the repository now intentionally tracks the refactor-as-code work item and should track all historical work-item docs.
- The small/medium route makes `module:models` conditional, while model/sub-agent strategy is required for substantial planning.
- Validation still relies heavily on curated string checks. It does not parse every declared `module:*`, `rule:*`, `schema:*`, `scenario:*`, and `metric:*` reference to prove the graph has owners and no dangling references.
- Validation does not yet enforce route-depth or broad duplicate-block budgets.
- `artifact-contract.md` remains a broad lifecycle module. It now has rule IDs, but future changes may still concentrate too much responsibility there.

## Proposed behavior

The harness should treat `docs/work-items/` as normal tracked documentation in this repository. The nested `docs/work-items/AGENTS.md` should be removed, all existing work-item artifacts should be added to git, and repository docs should describe planning packages as valid repository history instead of local-only scratch.

Small/medium substantial planning should always route through `module:models`. Very small mechanical edits may still skip durable planning when lifecycle sizing allows it, but every substantial plan should record model/sub-agent strategy or `Sub-agents: None` with rationale.

Graph validation should become structural:

1. Collect declared owners from current harness surfaces:
   - `module:*` owner declarations in canonical references.
   - `rule:*` owner tables in canonical references.
   - `schema:*` anchors in templates.
   - `scenario:*` and `metric:*` anchors in snapshots, validation docs, or architecture references when they are intended to be current.
2. Collect references from current harness surfaces:
   - `Policy references:` lines in templates.
   - Router rows in `SKILL.md`.
   - README route tables and validation documentation.
   - Validation script owner lists and scenario checks.
3. Fail validation when a referenced ID has no owner.
4. Fail validation when a rule or schema has more than one current canonical owner unless it is explicitly allowed.
5. Fail validation when an owner table references a local heading that does not exist in the same file.
6. Fail validation when a template `Policy references:` list omits a module required by the corresponding router route.
7. Fail validation when router route requirements point to missing files, modules, rules, or templates.
8. Report graph failures with file path, ID, and reason so the agent can repair the canonical owner or consumer.

Route-depth validation should check the current router against the budgets in the architecture snapshot: routine operation routes should stay within the intended number of required modules and should not force all references to load. Duplicate-block validation should detect reusable policy blocks across current harness files more generally than the current phrase blacklist, while still allowing short intentional summaries.

The lifecycle split should be planned after the graph checks exist. The split may be a file split or a section-level decomposition, but it should be guided by validation and by real edit pressure. The goal is to reduce future lifecycle fan-out without creating too many tiny files.

## Interfaces and data

Affected files and interfaces are expected to include:

- `docs/work-items/AGENTS.md` deletion.
- `.gitignore`, if needed to stop ignoring `docs/work-items/`.
- Existing `docs/work-items/**` artifacts staged as tracked repository docs.
- `.agents/skills/dev-doc-harness/SKILL.md` small/medium route.
- `.agents/skills/dev-doc-harness/references/policy-architecture.md` graph-validation and route-budget guidance.
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` graph, route-depth, and duplicate-block checks.
- `README.md` and relevant deltas or docs that describe work-item artifact tracking and validation behavior.
- `CHANGELOG.md` entries before commits.

No runtime product API, persistence schema, service interface, or user data model is affected.

## Risks

- Removing the ignored/local-only convention can increase repository size and make planning artifacts more visible than intended.
- Adding all historical work-item docs may introduce old policy prose into search results, which could confuse agents unless current-vs-historical authority remains clear.
- Graph validation can become brittle if it over-parses Markdown or treats illustrative text as current policy.
- Duplicate-block detection can generate false positives for short safety summaries, examples, or historical artifacts.
- Making `module:models` mandatory for small/medium substantial planning increases retrieval cost slightly.
- Splitting `artifact-contract.md` too soon could create churn before validation is strong enough to catch broken references.

## Acceptance criteria

- `docs/work-items/AGENTS.md` no longer blocks tracking approved or historical planning docs.
- All existing `docs/work-items/` Markdown artifacts are tracked in git or explicitly documented as excluded for a concrete reason.
- Root and README guidance no longer says this repository's work-item docs are generally local-only.
- The small/medium substantial planning route requires `module:models`.
- Validation passes after checking every current `module:*`, `rule:*`, and `schema:*` reference for an owner.
- Validation fails for a deliberately introduced dangling rule reference in a safe local test or documented manual check.
- Validation checks that owner-table local headings exist.
- Validation checks that template policy-reference lists satisfy router route requirements for the template's operation.
- Validation reports route-budget or route-depth drift for common operation routes.
- Validation detects broad duplicated reusable policy blocks across current harness surfaces, while excluding historical work-item artifacts from duplicate-policy cleanup.
- The lifecycle-module decomposition path is documented with a recommended next step and does not proceed until graph validation is in place.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entries grouped by work ID and phase/task |
| Test cases | Snapshot | Yes | Before implementation | `snapshots/test-cases.snapshot.md` | Include graph-validation negative cases and route-budget checks |
| Testing guide delta | Living delta | Yes | During implementation | `deltas/testing-guide.delta.md` | Update validation command and failure triage for graph checks |
| Operator manual delta | Living delta | Yes | During implementation | `deltas/operator-manual.delta.md` | Explain tracked work-item docs and validation expectations |
| API reference delta | Living delta | No | Not applicable | `deltas/api-reference.delta.md` | No public API changes |
| Architecture snapshot | Snapshot | Yes | Before or during implementation | `snapshots/architecture.snapshot.md` | Capture graph-validation model and lifecycle split recommendation |
| Architecture summary delta | Living delta | Yes | After implementation | `deltas/architecture-summary.delta.md` | Summarize graph validation and lifecycle decomposition path |

## Approval

- Status: Approved
- Superseded by: None
