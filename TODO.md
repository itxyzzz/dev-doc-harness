# TODO

Future work collected from the original handoff and follow-up design discussion. Items are ordered from more useful short-term additions to more complex, risky, or governance-heavy work.

## Near-Term Validation And Polish

- [ ] Test the harness on one fake small feature.
  - Exercise `spec.md`, `plan.md`, documentation matrix choices, `variance-log.md`, `CHANGELOG.md`, and the planning freeze gate.
- [ ] Test the harness on one fake large feature.
  - Exercise `spec.md` as the anchor handoff, `plan-phase-NN-*.md`, multiple freeze gates, model/sub-agent strategy, and amendment flow.
- [ ] Test a Superpowers-generated spec or plan converted into `specs/<feature-id>/`.
  - Confirm the harness layers cleanly over Superpowers without duplicating its methodology.
- [ ] Add a few examples for common sub-agent roles.
  - Keep examples policy-relative and short: explorer, reviewer, test-risk reviewer, bounded implementer, final review.
- [ ] Confirm current model classes available in the operator environment.
  - Keep policy language model-class based unless concrete names are required by the environment.
- [ ] Add a short planning-only PR note or checklist.
  - Document how to use the freeze gate as the point to push a draft plan-only PR before implementation.

## Mechanical Validation

- [ ] Create optional `scripts/check-agent-artifacts.py`.
  - Use only the Python standard library.
  - Support `python scripts/check-agent-artifacts.py specs/<feature-id>`.
  - Validate feature folder presence, `spec.md`, `plan.md` or `plan-phase-*.md`, `implementation-notes/variance-log.md`, expected docs folders, and `CHANGELOG.md`.
  - Avoid semantic review of plan quality.
- [ ] Add validator usage notes to the harness.
  - Reference the script from the skill or a short operator note without making it mandatory.
- [ ] Decide whether to wire validation into CI or pre-commit later.
  - Keep this separate from the zero-dependency script until the script has stabilized.

## Superpowers Compatibility

- [ ] Verify how Superpowers is installed and invoked in target environments.
- [ ] Confirm whether Superpowers writes specs or plans to fixed default locations.
- [ ] Document the exact copy/convert flow from Superpowers artifacts into `specs/<feature-id>/`.
- [ ] Confirm freeze gates interrupt the normal "implement this plan" transition cleanly.
- [ ] Add a separate `references/superpowers-compatibility.md` only if the compatibility section grows too large.

## spec-kit Adapter

- [ ] Verify installed spec-kit version and local command behavior.
- [ ] Check available preset, override, template, and extension behavior.
- [ ] Decide whether the first adapter should use a preset, full local template overrides, or a later extension.
- [ ] Create a minimal `.specify/presets/dev-doc-harness/` adapter if local spec-kit behavior supports it.
- [ ] Keep adapter templates short and point back to the canonical harness references.
- [ ] Test template resolution with local spec-kit commands.
- [ ] Document version-specific assumptions and unsupported composition behavior.
- [ ] Preserve draft plan-only PR workflow as a first-class adapter use case.

## Documentation Artifact Schemas

- [ ] Define a sparse template for `docs/snapshots/test-cases.snapshot.md`.
- [ ] Define a sparse template for `docs/snapshots/architecture.snapshot.md`.
- [ ] Define a sparse template for `docs/snapshots/api-contract.snapshot.md`.
- [ ] Define sparse templates for living deltas:
  - `docs/living/testing-guide.delta.md`
  - `docs/living/operator-manual.delta.md`
  - `docs/living/api-reference.delta.md`
  - `docs/living/architecture-summary.delta.md`
- [ ] Consider future templates for migration notes, rollout notes, runbooks, and troubleshooting guides.
- [ ] Decide whether living deltas are automatically merged into long-lived docs or only proposed for review.
- [ ] Define ownership and approval rules for living docs.

## PR And Review Workflow

- [ ] Define whether every feature folder must be linked from PR descriptions.
- [ ] Define whether every PR must include artifact validation output.
- [ ] Define how approved amendments should appear in GitHub, Bitbucket, or Stash PRs.
- [ ] Add a planning-only PR checklist for finalized specs/plans.
- [ ] Add an implementation PR checklist that references freeze-gate commits and variance logs.

## Governance And Process Maturity

- [ ] Define plan-amendment approval markers.
- [ ] Define who may approve controlled variances.
- [ ] Define documentation debt tracking.
- [ ] Define retention and archive policy for old `specs/` folders.
- [ ] Define migration path for existing specs and plans in older repositories.
- [ ] Define harness versioning and update policy across repositories.
- [ ] Add an examples library only after the core contract has been tested on fake and real features.
- [ ] Add a bootstrapping script only if repeated manual setup becomes painful.

## Deferred Or Riskier Ideas

- [ ] Add CI validation after the optional validator is stable.
- [ ] Add pre-commit integration after CI behavior is clear.
- [ ] Add advanced spec-kit composition only after verifying the installed version supports the needed behavior.
- [ ] Add detailed supplemental documentation schemas only after the snapshot-vs-living lifecycle has proven useful.
- [ ] Add team/enterprise governance around approvers, ownership, retention, and cross-repo rollout only after individual-repo usage stabilizes.
