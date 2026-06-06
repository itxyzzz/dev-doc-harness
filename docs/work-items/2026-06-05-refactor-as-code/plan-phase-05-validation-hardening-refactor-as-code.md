# Phase 05: Validation Hardening Plan

Work ID: `2026-06-05-refactor-as-code`
Short ID: `refactor-as-code`
Status: Approved
Schema: `schema:plan.phase`
Policy references: `module:lifecycle`, `module:architecture`, `module:quality`, `module:models`, `module:freeze-gate`, `module:execution-quality`, `rule:quality.phase-plan-fresh-thread`, `rule:models.strategy-required`, `rule:lifecycle.variance-policy`, `rule:lifecycle.documentation-matrix`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Objective

Add lightweight validation checks and sample traversal tests that harden the refactored harness architecture against drift after Phases 01 through 04.

Phase 05 converts the approved architecture snapshot's feasible validation budgets and golden scenarios into repository-local checks, records the traversal expectations as a durable work-item snapshot, and documents the validation command for future harness maintainers. It must preserve the current planning freeze, variance, changelog, immutable snapshot, Superpowers compatibility, and active repository model-policy selection behavior.

Phase 05 must not rewrite frozen historical work-item artifacts, introduce full rule versioning, replace the harness with another methodology, or change the active repository policy away from the `AGENTS.md` selection point.

## Input context

The implementing agent must read these current instructions, frozen planning artifacts, current harness surfaces, and prior phase outputs before editing:

- `AGENTS.md`
- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
- `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
- `.agents/skills/dev-doc-harness/assets/templates/`
- `README.md`
- `CHANGELOG.md`
- `docs/work-items/2026-06-05-refactor-as-code/spec-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-amendment-001-architecture-guardrails-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-phase-02-canonical-modules-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-phase-03-template-slimming-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/plan-phase-04-entrypoint-docs-refactor-as-code.md`
- `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`

Preserve these prior-phase decisions:

- Canonical references own reusable policy; templates own artifact shape; README is operator-facing summary.
- `.agents/skills/dev-doc-harness/SKILL.md` is the operation router.
- `AGENTS.md` remains the repository bootstrap and the single repository-local active model-policy selector.
- The active repository policy remains the `economy-default` policy selected in `AGENTS.md` unless the operator explicitly changes it.
- Rule IDs and module IDs are stable retrieval and ownership anchors, not a full versioning system.
- Historical work-item artifacts remain immutable snapshots and are not migration targets for copied policy cleanup.
- The Phase 01 architecture snapshot is frozen; Phase 05 may create a new test-case snapshot but must not edit `snapshots/architecture.snapshot.md`.

## Likely files and areas

Create during Phase 05 execution:

- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`
- `docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md`
- `docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md`
- `docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md`
- `docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md`

Modify during Phase 05 execution:

- `README.md`
- `CHANGELOG.md`

Modify only if required for validation command discoverability or if script implementation exposes a small current-surface routing gap:

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
- `.agents/skills/dev-doc-harness/references/policy-architecture.md`

Do not modify in Phase 05 unless an approved amendment changes the phase boundary:

- `AGENTS.md`
- `.agents/skills/dev-doc-harness/assets/templates/`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
- Frozen historical work-item artifacts under `docs/work-items/`, including this work item's approved spec, amendment, existing architecture snapshot, and Phase 01 through Phase 04 plans
- Any full rule-versioning manifest or generated documentation system

## Planned validation scope

The Phase 05 validation script should be lightweight PowerShell so it runs in the repository's default Windows environment without adding dependencies.

The script must check current harness files only, not every historical planning artifact. It should treat this work item's frozen artifacts as inputs for expectations and evidence, but it must not rewrite them.

Required script checks:

| Check ID | Purpose | Expected failure signal |
|---|---|---|
| `paths.required-files` | Verify current entrypoints, canonical references, templates, and planned work-item validation artifacts exist. | Nonzero exit with missing path list. |
| `ids.module-owners` | Verify current canonical references declare expected `module:*` IDs. | Nonzero exit with missing module owner list. |
| `ids.safety-rules` | Verify safety-critical rule IDs remain present in canonical owners and discoverable from `SKILL.md` or README where applicable. | Nonzero exit with missing rule ID list. |
| `templates.schema-anchors` | Verify current templates contain the Phase 03 schema IDs and policy-reference anchors. | Nonzero exit with missing schema or policy citation list. |
| `router.required-routes` | Verify `SKILL.md` routes common operation families to expected modules or references. | Nonzero exit with missing operation or route target list. |
| `discoverability.safety` | Verify work sizing, freeze, variance, changelog, immutable snapshot, quality, compatibility, and model policy remain reachable from public entrypoints. | Nonzero exit with missing discoverability topic list. |
| `phrases.duplicated-policy` | Detect previously removed long reusable policy phrases in templates, README, root instructions, and `SKILL.md`. | Nonzero exit with disallowed phrase matches. |
| `placeholders.current-surfaces` | Detect unresolved placeholders in current harness surfaces while allowing intentional template placeholders and the draft-status marker in the current draft phase plan before approval. | Nonzero exit with unexpected placeholder matches. |
| `scenarios.golden-traversal` | Run static sample traversal checks for the approved golden scenarios. | Nonzero exit with scenario ID and missing evidence. |

The script should output one `PASS <check-id>` line per passing check and `FAIL <check-id>` lines before exiting nonzero when any check fails.

The golden traversal checks must cover these scenario IDs from `snapshots/architecture.snapshot.md`:

- `scenario:work-size.very-small-skip`
- `scenario:planning.small-medium`
- `scenario:planning.large-anchor-freeze`
- `scenario:planning.phase-plan-freeze`
- `scenario:execution.post-freeze-authorization`
- `scenario:variance.high-impact-amendment`
- `scenario:models.sub-agent-authorization`
- `scenario:compat.superpowers`
- `scenario:history.historical-artifact-handling`

## Model and Sub-agent Strategy

Current orchestration: Codex in this desktop thread; exact model/profile and reasoning effort are not exposed in repository artifacts.
Fit assessment: Phase 05 is architecture-sensitive validation work with medium implementation complexity and high process blast radius. The script is small, but missed checks can allow future drift in freeze gates, variance handling, model policy, template schemas, or router behavior. The repository default is the active policy selected in `AGENTS.md`, currently `economy-default`.
Recommended change: Use the active repository policy. Use stronger reasoning in the orchestration thread for final validation review because Phase 05 is the final hardening pass for the refactor.

Sub-agents: One read-only final validation reviewer is authorized after the phase plan is frozen and implementation is separately authorized, if the platform and operator allow sub-agents. No write-capable sub-agents are authorized by this plan.

| Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|
| Final harness behavior review | curated artifacts | Approved spec, amendment, architecture snapshot, Phase 05 plan, completed diff, validation script output, and variance log | Review findings in the completion handoff | active repository policy | latest strongest available | high | Final process-safety review has high downstream impact and should not rely on a cheaper reviewer as final authority | No | High: missed regression can weaken future planning gates, variance handling, or model-policy authorization |

If sub-agents are unavailable or not authorized at implementation time, the orchestration thread must perform the final review and report `Sub-agents: None used` with the platform or authorization reason.

## Tasks

- [ ] **Step 1: Verify starting state**

  Run:

  ```powershell
  git status --short --branch
  ```

  Expected: branch is `refactor-as-code`; no unrelated staged or unstaged files are present before Phase 05 implementation edits.

- [ ] **Step 2: Re-read required inputs**

  Read every file and artifact listed in `## Input context`.

  Confirm these execution constraints before editing: no frozen historical artifact rewrite, no full rule-versioning system, no active model-policy selector change, no template edits unless an approved amendment changes scope, and no changes to Phase 01 through Phase 04 frozen plans.

- [ ] **Step 3: Inventory current validation targets**

  Run:

  ```powershell
  rg -n "module:|rule:|schema:|scenario:|metric:" AGENTS.md README.md .agents/skills/dev-doc-harness docs/work-items/2026-06-05-refactor-as-code
  rg -n "Planning Artifact Freeze Gate|variance|CHANGELOG|immutable|active repository policy|Superpowers compatibility|Status:[ ]Draft|T[D]B|T[O]DO|R[e]place|unresolved[ ]decision" AGENTS.md README.md .agents/skills/dev-doc-harness docs/work-items/2026-06-05-refactor-as-code
  ```

  Use the output to confirm the expected module IDs, rule IDs, schema IDs, scenario IDs, and drift-prone phrases before creating the script.

- [ ] **Step 4: Create the validation script directory and script**

  Create `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`.

  Script requirements:

  - Use PowerShell 5-compatible syntax.
  - Resolve repository root from the script path rather than the caller's current directory.
  - Check only repository-local files.
  - Use explicit arrays for required files, modules, rules, schemas, router routes, discoverability topics, disallowed phrases, and golden scenarios.
  - Print `PASS <check-id>` for each passing check.
  - Print `FAIL <check-id>: <detail>` for each failure.
  - Exit `0` only when every check passes.
  - Exit `1` when one or more checks fail.
  - Avoid network access and dependency installation.
  - Avoid modifying files.

  The script should include helper functions with these names so later maintainers can extend it without adding a framework:

  - `Join-RepoPath`
  - `Read-RepoText`
  - `Add-Failure`
  - `Assert-PathExists`
  - `Assert-TextContains`
  - `Assert-TextNotContains`
  - `Assert-RouteContains`
  - `Assert-ScenarioEvidence`
  - `Write-CheckResult`

- [ ] **Step 5: Add required-file and ID checks**

  In `Test-HarnessPolicy.ps1`, add the `paths.required-files`, `ids.module-owners`, `ids.safety-rules`, and `templates.schema-anchors` checks.

  Required files must include:

  - `AGENTS.md`
  - `README.md`
  - `CHANGELOG.md`
  - `.agents/skills/dev-doc-harness/SKILL.md`
  - `.agents/skills/dev-doc-harness/references/policy-architecture.md`
  - `.agents/skills/dev-doc-harness/references/artifact-contract.md`
  - `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
  - `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
  - `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
  - `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`
  - `.agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md`
  - `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md`
  - `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
  - `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
  - `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
  - `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md`
  - `.agents/skills/dev-doc-harness/assets/templates/variance-log.md`
  - `docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md`
  - `docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md`

  Module IDs must include `module:architecture`, `module:lifecycle`, `module:freeze-gate`, `module:models`, `module:quality`, `module:execution-quality`, and `module:evidence`.

  Safety-critical rule IDs must include `rule:lifecycle.work-sizing`, `rule:lifecycle.immutable-snapshots`, `rule:lifecycle.variance-policy`, `rule:lifecycle.changelog-before-commit`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`, `rule:models.strategy-required`, `rule:models.approved-strategy-authorized`, `rule:models.fresh-confirmation`, `rule:quality.phase-plan-fresh-thread`, and `rule:lifecycle.documentation-matrix`.

  Template schema IDs must include `schema:spec.small-medium`, `schema:plan.small-medium`, `schema:spec.large-phased`, `schema:plan.phase`, `schema:plan.amendment`, and `schema:variance-log`.

- [ ] **Step 6: Add router and safety discoverability checks**

  In `Test-HarnessPolicy.ps1`, add `router.required-routes` and `discoverability.safety`.

  The router check must verify that `.agents/skills/dev-doc-harness/SKILL.md` contains operation rows or route text for these operation families:

  - Classify work size.
  - Draft or review small/medium specs and plans.
  - Draft or review large anchor specs.
  - Draft or review phase plans.
  - Freeze planning packages.
  - Execute approved work and record variance.
  - Use or review sub-agent strategy.
  - Evidence-heavy review or reports.
  - Update templates or router guidance.
  - Superpowers or spec-kit compatibility.

  The discoverability check must verify that `AGENTS.md`, `SKILL.md`, README, or canonical references expose these topics with a route or owner:

  - Work sizing.
  - Planning freeze gates.
  - Stop before implementation.
  - Immutable snapshots.
  - Variance and amendments.
  - Changelog before commit.
  - Documentation matrix.
  - Active repository model policy.
  - Superpowers compatibility.
  - Historical artifact handling.

- [ ] **Step 7: Add duplicate-policy phrase and placeholder checks**

  In `Test-HarnessPolicy.ps1`, add `phrases.duplicated-policy` and `placeholders.current-surfaces`.

  Disallowed long reusable policy phrase patterns must include:

  - `Fresh confirmation is still required`
  - `Long-running .*more than 3 total sub-agents`
  - `Context strategy must say how`
  - `Before approval, operator feedback edits this draft directly`
  - `When this .*ready for operator review, follow`
  - `After this .*approved, frozen, and followed`

  Placeholder checks must scan current harness surfaces and should not fail on intentional template placeholders such as `<work-id>`, `<short-id>`, `<Phase Name>`, `<YYYY-MM-DD-short-kebab-title>`, and the draft-status marker in templates or the current draft plan. Unexpected `T[D]B`, `T[O]DO`, `R[e]place`, `blank u[n]less`, and `unresolved d[e]cision` matches in current non-template surfaces must fail.

- [ ] **Step 8: Create the golden scenario snapshot**

  Create `docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md`.

  The snapshot must be immutable after approval and must include:

  - Work ID and status.
  - Source references: approved spec, architecture guardrails amendment, architecture snapshot, and this Phase 05 plan.
  - A compact scenario table for all nine golden scenario IDs listed in `## Planned validation scope`.
  - For each scenario: entrypoint, required files or modules, expected behavior, and script evidence checked.
  - A note that these are traversal and policy-drift checks, not runtime product tests.
  - A note that rule versioning remains deferred.

- [ ] **Step 9: Add golden scenario checks to the script**

  In `Test-HarnessPolicy.ps1`, add `scenarios.golden-traversal`.

  Each scenario check must verify evidence in current files that the scenario can be followed. Use string evidence rather than a complex parser.

  Required examples:

  - `scenario:work-size.very-small-skip` checks `AGENTS.md`, `SKILL.md`, and `artifact-contract.md` for very small mechanical sizing.
  - `scenario:planning.phase-plan-freeze` checks `SKILL.md`, `durable-planning-quality.md`, `planning-freeze-gates.md`, and `large-phased-work-item-phase-plan.md` for phase-plan draft review and fresh-thread quality.
  - `scenario:execution.post-freeze-authorization` checks `planning-freeze-gates.md`, `artifact-contract.md`, and `context-and-quality-gates.md` for post-freeze authorization, approved scope, variance, and changelog expectations.
  - `scenario:models.sub-agent-authorization` checks `subagent-model-policy.md` and current plan templates for approved strategy authorization and fresh confirmation boundaries.
  - `scenario:history.historical-artifact-handling` checks `artifact-contract.md` and `policy-architecture.md` for immutable snapshots and historical artifact handling.

- [ ] **Step 10: Document validation command and durable follow-up docs**

  Create `docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md`.

  Required content:

  - The validation command:

    ```powershell
    powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
    ```

  - When to run it: before harness commits that change `AGENTS.md`, `SKILL.md`, canonical references, templates, README, or validation artifacts.
  - Expected output: `PASS <check-id>` lines for every check and exit code `0`.
  - Failure triage: inspect the reported check ID, fix the canonical owner or route, and do not weaken freeze, variance, changelog, model, or immutable snapshot behavior to satisfy the script.
  - Scope: the script checks current harness surfaces and golden traversal evidence, not all historical work-item artifacts.

  Create `docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md`.

  Required content:

  - Explain that operators can ask agents to run the harness validation command before plan freeze, implementation commit, or handoff.
  - Explain that validation failures are review signals, not automatic permission to rewrite frozen artifacts.
  - Preserve the plan-only PR and stop-before-implementation behavior.

  Create `docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md`.

  Required content:

  - Summarize that the harness now has a validation script covering required files, module and rule IDs, template schemas, router routes, safety discoverability, duplicate policy phrases, placeholders, and golden traversal scenarios.
  - Link the validation checks back to Phase 01 metrics and golden scenarios.
  - Record that full rule versioning remains deferred.

- [ ] **Step 11: Update README validation guidance**

  Modify `README.md` to mention the validation command in the operator-facing overview or "How to use it" section.

  Required outcomes:

  - State that the validation command is a lightweight local check for current harness surfaces.
  - Link the command to the script path.
  - Keep README as an operator-facing summary, not a canonical policy owner.
  - Do not copy the full script checklist into README.

- [ ] **Step 12: Add small current-surface validation route only if needed**

  If adding the script leaves validation undiscoverable from the harness entrypoint, make the smallest necessary update to `.agents/skills/dev-doc-harness/SKILL.md` or `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`.

  Allowed outcomes:

  - Add a compact route or quality-gate note that harness validation uses `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`.
  - Keep detailed validation behavior in the script and durable deltas.
  - Preserve `SKILL.md` as a router, not a validation policy reference.

  Stop and draft an amendment instead if the needed change would add a new canonical module, change lifecycle authority, require full rule versioning, alter active model policy selection, or revise freeze-gate behavior.

- [ ] **Step 13: Run validation and fix local script defects**

  Run:

  ```powershell
  powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
  ```

  Expected: exit code `0`; output contains `PASS paths.required-files`, `PASS ids.module-owners`, `PASS ids.safety-rules`, `PASS templates.schema-anchors`, `PASS router.required-routes`, `PASS discoverability.safety`, `PASS phrases.duplicated-policy`, `PASS placeholders.current-surfaces`, and `PASS scenarios.golden-traversal`.

  If the script fails because of an implementation bug in the new script, fix the script and rerun it.

  If the script fails because current approved harness behavior conflicts with the frozen Phase 05 plan, stop and follow the variance rules instead of weakening safeguards or rewriting frozen artifacts.

- [ ] **Step 14: Run static scope and placeholder checks**

  Run:

  ```powershell
  rg -n "Status:[ ]Draft|T[D]B|T[O]DO|R[e]place|blank[ ]unless|unresolved[ ]decision" .agents/skills/dev-doc-harness/scripts README.md .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/references/context-and-quality-gates.md .agents/skills/dev-doc-harness/references/policy-architecture.md docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md docs/work-items/2026-06-05-refactor-as-code/deltas
  git diff --name-only -- docs/work-items/2026-06-05-refactor-as-code/spec-refactor-as-code.md docs/work-items/2026-06-05-refactor-as-code/plan-amendment-001-architecture-guardrails-refactor-as-code.md docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md docs/work-items/2026-06-05-refactor-as-code/plan-phase-01-policy-architecture-refactor-as-code.md docs/work-items/2026-06-05-refactor-as-code/plan-phase-02-canonical-modules-refactor-as-code.md docs/work-items/2026-06-05-refactor-as-code/plan-phase-03-template-slimming-refactor-as-code.md docs/work-items/2026-06-05-refactor-as-code/plan-phase-04-entrypoint-docs-refactor-as-code.md
  ```

  Expected:

  - The `rg` command has no unexpected placeholder matches. Exit code may be `1` because no matches were found.
  - The `git diff --name-only -- <frozen paths>` command has no output.

- [ ] **Step 15: Update changelog for Phase 05 execution**

  Before the Phase 05 execution commit, add a newest-first `CHANGELOG.md` entry titled:

  ```text
  2026-06-05-refactor-as-code: complete Phase 05 validation hardening
  ```

  The entry must mention the validation script, golden scenario snapshot, testing/operator/architecture deltas, README validation guidance, and the decision not to rewrite frozen historical artifacts or introduce full rule versioning.

- [ ] **Step 16: Final validation review**

  Review the completed diff against the approved spec, amendment, Phase 01 architecture snapshot, Phase 02 module map, Phase 03 template boundaries, and Phase 04 router behavior.

  Confirm:

  - The validation script checks current harness surfaces without modifying files.
  - Golden scenarios map to current entrypoints and canonical owners.
  - Safety-critical lifecycle, freeze, variance, changelog, model, and immutable snapshot behavior remains discoverable.
  - Templates were not modified unless an approved amendment changed scope.
  - Root `AGENTS.md` was not modified and remains the active model-policy selector.
  - README remains an operator summary.
  - Historical work-item artifacts were not rewritten.
  - Rule versioning remains deferred.

  If the authorized read-only final validation reviewer is used, include its findings in this review and resolve or document all findings before committing. The orchestration thread owns the final integration decision.

- [ ] **Step 17: Commit Phase 05 outputs**

  Review the diff to confirm Phase 05 changed only allowed files and `CHANGELOG.md`.

  Force-add ignored approved work-item artifacts that Phase 05 creates:

  ```powershell
  git add -f docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md
  ```

  Stage current harness files and changelog normally:

  ```powershell
  git add .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1 README.md CHANGELOG.md
  ```

  Include `.agents/skills/dev-doc-harness/SKILL.md`, `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`, or `.agents/skills/dev-doc-harness/references/policy-architecture.md` in the normal `git add` command only if Phase 05 made the allowed discoverability or validation-route edits.

  Commit with message:

  ```text
  Complete Phase 05 validation hardening
  ```

## Tests and validation

| Command | Expected result |
|---|---|
| `git status --short --branch` | Shows branch `refactor-as-code`; before implementation edits, no unrelated staged or unstaged files are present; before the Phase 05 execution commit, only allowed Phase 05 files are modified or staged. |
| `Test-Path .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Outputs `True` after the script is created. |
| `powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Exits `0` and outputs `PASS` lines for all required check IDs. |
| `rg -n "scenario:(work-size\\.very-small-skip|planning\\.small-medium|planning\\.large-anchor-freeze|planning\\.phase-plan-freeze|execution\\.post-freeze-authorization|variance\\.high-impact-amendment|models\\.sub-agent-authorization|compat\\.superpowers|history\\.historical-artifact-handling)" docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Outputs matches for every golden scenario ID in both the snapshot and validation script. |
| `rg -n "PASS (paths\\.required-files|ids\\.module-owners|ids\\.safety-rules|templates\\.schema-anchors|router\\.required-routes|discoverability\\.safety|phrases\\.duplicated-policy|placeholders\\.current-surfaces|scenarios\\.golden-traversal)" .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` | Outputs matches proving the script reports every required check ID. |
| `rg -n "Status:[ ]Draft|T[D]B|T[O]DO|R[e]place|blank[ ]unless|unresolved[ ]decision" .agents/skills/dev-doc-harness/scripts README.md .agents/skills/dev-doc-harness/SKILL.md .agents/skills/dev-doc-harness/references/context-and-quality-gates.md .agents/skills/dev-doc-harness/references/policy-architecture.md docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md docs/work-items/2026-06-05-refactor-as-code/deltas` | No unexpected output. Exit code may be `1` because `rg` found no matches. |
| `git diff --name-only -- AGENTS.md .agents/skills/dev-doc-harness/assets/templates .agents/skills/dev-doc-harness/references/artifact-contract.md .agents/skills/dev-doc-harness/references/planning-freeze-gates.md .agents/skills/dev-doc-harness/references/subagent-model-policy.md .agents/skills/dev-doc-harness/references/durable-planning-quality.md .agents/skills/dev-doc-harness/references/evidence-and-report-artifacts.md docs/work-items/2026-06-05-refactor-as-code/spec-refactor-as-code.md docs/work-items/2026-06-05-refactor-as-code/plan-amendment-001-architecture-guardrails-refactor-as-code.md docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md docs/work-items/2026-06-05-refactor-as-code/plan-phase-01-policy-architecture-refactor-as-code.md docs/work-items/2026-06-05-refactor-as-code/plan-phase-02-canonical-modules-refactor-as-code.md docs/work-items/2026-06-05-refactor-as-code/plan-phase-03-template-slimming-refactor-as-code.md docs/work-items/2026-06-05-refactor-as-code/plan-phase-04-entrypoint-docs-refactor-as-code.md` | No output unless an approved amendment permits changes to one of these protected paths. |
| `git diff --name-only` | Before staging for the Phase 05 execution commit, includes only `CHANGELOG.md`, `README.md`, `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1`, Phase 05 work-item snapshot and deltas, and any explicitly justified allowed validation-route files. |

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Newest-first entry for Phase 05 planning approval and implementation completion |
| Test cases | Snapshot | Yes | During Phase 05 implementation | `docs/work-items/2026-06-05-refactor-as-code/snapshots/test-cases.snapshot.md` | Captures golden traversal scenarios and expected script evidence |
| Testing guide delta | Living delta | Yes | During Phase 05 implementation | `docs/work-items/2026-06-05-refactor-as-code/deltas/testing-guide.delta.md` | Documents validation command, expected output, and failure triage |
| Operator manual delta | Living delta | Yes | During Phase 05 implementation | `docs/work-items/2026-06-05-refactor-as-code/deltas/operator-manual.delta.md` | Records operator-facing validation use and freeze/variance boundaries |
| API reference delta | Living delta | No | Not applicable | `docs/work-items/2026-06-05-refactor-as-code/deltas/api-reference.delta.md` | No public API is expected |
| Architecture snapshot | Snapshot | No | Already complete | `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md` | Frozen Phase 01 architecture snapshot; do not edit |
| Architecture summary delta | Living delta | Yes | During Phase 05 implementation | `docs/work-items/2026-06-05-refactor-as-code/deltas/architecture-summary.delta.md` | Summarizes validation hardening and links to Phase 01 metrics/scenarios |

## Documentation tasks

- Update `CHANGELOG.md` before the Phase 05 implementation commit.
- Create `snapshots/test-cases.snapshot.md` and force-add it because this tracked work item is an approved exception under ignored `docs/work-items/`.
- Create `deltas/testing-guide.delta.md`, `deltas/operator-manual.delta.md`, and `deltas/architecture-summary.delta.md`; force-add them for the same approved tracked exception.
- Update `README.md` with a compact validation command mention.
- Update `.agents/skills/dev-doc-harness/SKILL.md`, `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md`, or `.agents/skills/dev-doc-harness/references/policy-architecture.md` only if needed for validation discoverability.
- Do not update `docs/work-items/2026-06-05-refactor-as-code/snapshots/architecture.snapshot.md`; it is a frozen Phase 01 snapshot.
- Update `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md` only if Phase 05 execution departs from this approved plan.
- Do not create a full rule-versioning manifest or generated docs pipeline.

## Variance rules

Before approval, operator feedback edits this draft directly and does not require an amendment. After the approval commit or explicit handoff snapshot, this phase plan is immutable.

During Phase 05 implementation, record nontrivial local technical variance in `docs/work-items/2026-06-05-refactor-as-code/implementation-notes/variance-log.md`. Create a plan amendment named `plan-amendment-NNN-short-title-refactor-as-code.md` and request operator approval before proceeding when post-freeze variance affects architecture, public interfaces, data, security, privacy, compliance, scope, acceptance criteria, active model-policy selection, compatibility authority, rule-versioning scope, validation feasibility, or plan feasibility.

## Planning artifact freeze gate

For draft review, stage only this phase plan with:

```powershell
git add -f docs/work-items/2026-06-05-refactor-as-code/plan-phase-05-validation-hardening-refactor-as-code.md
```

Then ask the operator to approve the staged draft or provide feedback. Do not commit before explicit approval.

After explicit approval, update `CHANGELOG.md`, verify the approved plan has no unresolved required items, stage only this phase plan and `CHANGELOG.md`, commit the approved planning package, and stop before implementation. Report the commit hash and approved artifact path, remind the operator they may push and create a draft plan-only PR, and ask the operator to confirm model, reasoning-effort, and sub-agent policy choices plus whether Phase 05 implementation should begin.

## Handoff output

At Phase 05 completion, the implementing agent must report:

- Assigned scope.
- Files inspected.
- Files changed.
- Commands and validation results.
- Validation script checks added, grouped by required files, IDs, templates, router routes, safety discoverability, duplicate phrases, placeholders, and golden traversal scenarios.
- Golden scenario snapshot coverage.
- Documentation deltas created and what long-lived docs they should update.
- README validation guidance changes and confirmation that README remains non-normative.
- Confirmation that root `AGENTS.md`, templates, protected canonical references, and frozen historical work-item artifacts were not modified, or an approved amendment reference if any were modified.
- Any variance entries or a statement that no variance occurred.
- Sub-agent use, including count, roles/scopes, concurrency or waves, context strategy, observed inheritance behavior, and de-facto model/model class/profile when known.
- Residual risks and recommended next action after Phase 05.

## Completion criteria

- Phase objective is met.
- `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` exists and runs without modifying files.
- The validation script checks required files, module owners, safety-critical rule IDs, template schema anchors, router routes, safety discoverability, disallowed duplicated policy phrases, unresolved placeholders, and golden traversal scenarios.
- `snapshots/test-cases.snapshot.md` records all nine golden scenario IDs and their expected traversal evidence.
- `deltas/testing-guide.delta.md`, `deltas/operator-manual.delta.md`, and `deltas/architecture-summary.delta.md` exist and describe the validation hardening follow-up.
- README mentions the validation command without becoming a canonical policy owner.
- Validation commands have been run and recorded.
- `CHANGELOG.md` has a newest-first entry for Phase 05 before the implementation commit.
- Variance log is present and current.
- No active model-policy selector change occurs.
- No full rule-versioning system is introduced.
- No protected templates, protected canonical references, or frozen historical work-item artifacts are rewritten without an approved amendment.
- De-facto sub-agent use is reported when applicable.
