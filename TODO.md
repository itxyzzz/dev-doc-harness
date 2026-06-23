# TODO

This backlog tracks future improvements for the Dev Doc Harness repository.
Items use a common format so they can be promoted into harness work items when
they are ready.

Priority labels:

- `P0`: Required before the next meaningful adoption or release checkpoint.
- `P1`: High-value near-term work with a clear owner path.
- `P2`: Useful after the core workflow has more evidence.
- `P3`: Deferred, experimental, or governance-heavy work.

Item format:

```md
- [ ] [P1] Short title.
  - Value: Why this matters.
  - Scope: Expected work.
  - Depends on: Prior decision, evidence, or none.
```

## P0 Current Documentation Work

- [x] [P0] Add a package-local operator note.
  - Value: Adopters who copy only root `AGENTS.md` plus `.agents/` get a compact usage explanation.
  - Scope: Add `.agents/skills/dev-doc-harness/docs/operator-note.md` and keep it summary-level.
  - Depends on: `2026-06-23-documentation-improvements`.
- [x] [P0] Add a portfolio-oriented README summary.
  - Value: Non-operator readers can understand the repository quickly.
  - Scope: Add a concise summary near the top of `README.md`.
  - Depends on: `2026-06-23-documentation-improvements`.
- [x] [P0] Clarify the validator evolution boundary.
  - Value: Future checks stay lightweight and structural instead of becoming a heavy semantic parser.
  - Scope: Add guidance to `references/policy-architecture.md`.
  - Depends on: `2026-06-23-documentation-improvements`.
- [x] [P0] Normalize this backlog.
  - Value: Future work is easier to compare, prioritize, and convert into work items.
  - Scope: Reformat `TODO.md` with priority labels, consistent fields, and current review follow-ups.
  - Depends on: `2026-06-23-documentation-improvements`.

## P1 Validation And Adoption Evidence

- [ ] [P1] Run a disposable large-work trial.
  - Value: Exercises the harness promise end to end before more adoption polish.
  - Scope: Use a throwaway sample repository or contained fixture to exercise an anchor spec, phase plan, freeze gate, amendment, validation, and rollback note.
  - Depends on: None.
- [ ] [P1] Add CI wiring for `Test-HarnessPolicy.ps1`.
  - Value: Creates a shared safety net for harness changes.
  - Scope: Add a minimal CI workflow that runs the existing PowerShell validator.
  - Depends on: Current validator staying stable.
- [ ] [P1] Add a planning-only PR note or checklist.
  - Value: Makes the freeze gate usable as a draft PR checkpoint before implementation.
  - Scope: Document what to include in a plan-only PR and where to link approved artifacts.
  - Depends on: Existing freeze-gate behavior.
- [ ] [P1] Track validation failures caught during real use.
  - Value: Turns validator value into evidence and helps prioritize future checks.
  - Scope: Add a lightweight record in work-item evidence, changelog notes, or a small validation learnings file.
  - Depends on: At least one real or disposable validation failure worth recording.
- [ ] [P1] Test a Superpowers-generated spec or plan conversion.
  - Value: Confirms this harness layers over Superpowers without duplicating methodology.
  - Scope: Convert a Superpowers artifact into `docs/work-items/<work-id>/` and record friction.
  - Depends on: A representative Superpowers artifact or controlled trial.

## P2 Validator And Artifact Tooling

- [ ] [P2] Split the PowerShell validator by logical check groups if it continues to grow.
  - Value: Keeps validation maintainable as new checks are added.
  - Scope: Extract path, graph, router, placeholder, release, and scenario checks only when the current single file becomes hard to review.
  - Depends on: Clear pressure from additional validation work.
- [ ] [P2] Create optional portable artifact validator.
  - Value: Helps adopters in environments where PowerShell is not a good baseline.
  - Scope: Add a standard-library Python script such as `scripts/check-agent-artifacts.py` for work-item folder shape checks.
  - Depends on: Confirmed cross-platform adoption need.
- [ ] [P2] Add validator usage notes.
  - Value: Helps operators understand which checks are mandatory, optional, or maintenance-only.
  - Scope: Reference validation from the router, package-local note, or a short maintenance note without making every downstream project run it.
  - Depends on: Validator boundary staying clear.
- [ ] [P2] Decide whether to add pre-commit wiring.
  - Value: Catches issues earlier for contributors who opt in.
  - Scope: Evaluate pre-commit only after CI behavior is clear.
  - Depends on: CI validation experience.

## P2 Examples And Documentation Artifacts

- [ ] [P2] Add a small examples directory.
  - Value: Gives adopters concrete models for a completed work item and a plan-only PR narrative.
  - Scope: Curate examples as illustrative content that points back to canonical references.
  - Depends on: Disposable large-work trial and at least one real work item worth summarizing.
- [ ] [P2] Define sparse snapshot templates.
  - Value: Makes test-case, architecture, and API-contract snapshots easier to create consistently.
  - Scope: Add templates for `snapshots/test-cases.snapshot.md`, `snapshots/architecture.snapshot.md`, and `snapshots/api-contract.snapshot.md`.
  - Depends on: More evidence from real use.
- [ ] [P2] Define sparse living-delta templates.
  - Value: Makes documentation deltas easier to review and merge later.
  - Scope: Add templates for testing guide, operator manual, API reference, and architecture summary deltas.
  - Depends on: Clearer ownership and approval rules for living docs.
- [ ] [P2] Define evidence-heavy report templates.
  - Value: Gives investigations a compact evidence format.
  - Scope: Include checked claims, commands run, results, discrepancies, remaining gaps, and references.
  - Depends on: Evidence/report guidance proving useful in real work.
- [ ] [P2] Consider templates for migration, rollout, runbook, and troubleshooting notes.
  - Value: Covers operational work without overloading the core spec and plan.
  - Scope: Add only after repeated need appears.
  - Depends on: Real work items showing recurring operational documentation gaps.

## P2 Compatibility And Adapters

- [ ] [P2] Verify Superpowers invocation in target environments.
  - Value: Avoids documenting compatibility based on assumptions.
  - Scope: Confirm install, invocation, default output locations, pointer-stub behavior, and freeze-gate interaction.
  - Depends on: Access to representative target environments.
- [ ] [P2] Document the Superpowers copy/convert flow.
  - Value: Gives agents a safe bridge from Superpowers artifacts into `docs/work-items/<work-id>/`.
  - Scope: Add a short compatibility reference only if the existing section grows too large.
  - Depends on: Superpowers conversion trial.
- [ ] [P2] Verify spec-kit version and adapter mechanics.
  - Value: Prevents building an adapter against unsupported assumptions.
  - Scope: Check preset, override, template, and extension behavior.
  - Depends on: Installed spec-kit access.
- [ ] [P2] Create a minimal spec-kit adapter if local behavior supports it.
  - Value: Lets spec-kit users keep the harness lifecycle contract.
  - Scope: Add short templates or presets that point back to canonical harness references.
  - Depends on: Verified spec-kit composition behavior.

## P3 PR Workflow And Governance

- [ ] [P3] Define PR artifact-link expectations.
  - Value: Makes reviews connect implementation diffs to approved planning artifacts.
  - Scope: Decide whether every PR must link work-item folders, validation output, amendments, and variance logs.
  - Depends on: Plan-only PR checklist experience.
- [ ] [P3] Define preserved-source versus derived-review artifact handling.
  - Value: Keeps evidence immutable while allowing cleaned summaries.
  - Scope: Describe where source evidence and repaired summaries should live.
  - Depends on: Evidence-heavy report usage.
- [ ] [P3] Design in-team distribution.
  - Value: Makes harness updates adoptable across multiple repositories.
  - Scope: Define publishing, versioning, migration, audit, rollback, and ownership.
  - Depends on: Single-repository usage stabilizing.
- [ ] [P3] Harden testing-related documentation policy.
  - Value: Improves acceptance criteria and correctness claims.
  - Scope: Define when test snapshots, testing-guide deltas, validation evidence, and coverage notes are required.
  - Depends on: More work-item evidence across features, bugs, investigations, and refactors.
- [ ] [P3] Define plan-amendment approval markers.
  - Value: Makes controlled changes after freeze easier to audit.
  - Scope: Decide how approval is represented in artifacts and PRs.
  - Depends on: More amendment examples.
- [ ] [P3] Define documentation debt tracking.
  - Value: Prevents deferred documentation work from disappearing.
  - Scope: Pick a lightweight tracking model before adding process.
  - Depends on: Living-delta workflow evidence.
- [ ] [P3] Define retention and archive policy for old work-item folders.
  - Value: Keeps repository history useful without clutter becoming unbounded.
  - Scope: Decide how long to keep artifacts and how to archive superseded work.
  - Depends on: Repository history volume becoming material.
- [ ] [P3] Define migration path for older repositories.
  - Value: Helps teams adopt the harness without rewriting useful historical docs.
  - Scope: Describe how to map older specs and plans into current work-item layout.
  - Depends on: At least one older repository migration.
- [ ] [P3] Define cross-repository harness versioning policy.
  - Value: Makes team-wide updates predictable.
  - Scope: Expand beyond current release marker only after adoption creates real compatibility needs.
  - Depends on: In-team distribution design.
- [ ] [P3] Add a bootstrapping script.
  - Value: Reduces manual setup if copying becomes repetitive.
  - Scope: Add only after repeated manual setup is proven painful.
  - Depends on: Multiple adoption attempts.

## Parking Lot

- [ ] [P3] Review public agentic-instruction repositories for reusable patterns.
  - Value: May surface compact patterns for context loading, evidence handling, role examples, and stop conditions.
  - Scope: Review public repositories such as `https://github.com/itxyzzz/gen-ai-se-hw` and extract only portable, non-project-specific ideas.
  - Depends on: Timeboxed research scope.
- [ ] [P3] Confirm current model classes available in the operator environment.
  - Value: Helps policy examples stay accurate without hardcoding model names unnecessarily.
  - Scope: Record environment observations only when concrete names become necessary.
  - Depends on: Stable platform exposure of model/profile details.
