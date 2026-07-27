# Plan Amendment 002: Compact Bootstrap and Add Skill Metadata

Work ID: `2026-07-27_harness-execution-flow-clarity`
Short ID: `harness-execution-flow-clarity`
Status: Approved
Harness release: `0.8+`
Schema: `schema:plan.amendment`
Policy references: `module:architecture`, `module:lifecycle`, `module:naming`, `module:models`, `module:freeze-gate`, `module:execution-quality`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:models.strategy-required`, `rule:naming.derived-patterns`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-002`
- Frozen package: `spec_harness-execution-flow-clarity.md`, `plan_harness-execution-flow-clarity.md`, `snapshots/architecture.snapshot.md`, `snapshots/test-cases.snapshot.md`, and `plan_amendment-001_operator-authorized-no-review_harness-execution-flow-clarity.md`
- Approval commits: `219258cfc5a3b79c19175121ed8076976d440701` and `37f2713f5d28e732b4c5493edbe1f83eaf29bd1a`
- Affected sections: original plan routing and bootstrap surfaces, validator ownership, operator-facing summaries, documentation integration, and post-implementation review scope
- Original instruction: keep `AGENTS.md` aligned with the canonical router and execution rules, validate current harness surfaces, and maintain operator-facing documentation without creating a second policy owner.

## Discovered issue

Post-implementation review found that root `AGENTS.md` is consistent but repeats more canonical compatibility and execution detail than its bootstrap-and-repository-override role requires. An aggressive pointer-only rewrite would weaken deliberately protected discovery and safety anchors, while leaving the current text unchanged would preserve avoidable maintenance duplication.

The distributable skill also lacks the recommended `agents/openai.yaml` UI metadata. Adding that file creates a new package interface and validator requirement that the frozen implementation plan did not name. The operator additionally requires the current uncommitted README rewrite to be included in the implementation boundary.

This is a material scope adjustment because it adds a distributable skill metadata surface and changes bootstrap validation. Frozen artifacts remain unchanged; this amendment governs only the follow-up files and checks named below.

## Proposed change

1. Compact `AGENTS.md` conservatively to approximately 300-350 words while preserving explicit bootstrap anchors for harness activation, the very-small-mechanical exception, `economy-default`, Superpowers/harness ownership, `docs/work-items/<work-id>`, combined small/medium planning, the guarded `docs/superpowers` exception, execution-start routing and operator overrides, and source-repository-only distribution maintenance.
2. Remove the introductory module inventory, excess subheadings, detailed execution-method cascade, standalone spec-kit explanation, and release-runbook summary. Route those details to the active Dev Doc Harness skill and canonical modules.
3. Change validator assertions that require exact `AGENTS.md` sentences into semantic anchor checks. Preserve the safety and discovery coverage rather than deleting it.
4. Add `.agents/skills/dev-doc-harness/agents/openai.yaml` with only these generated interface values:

   ```yaml
   interface:
     display_name: "Dev Doc Harness"
     short_description: "Plan and govern repository development work"
     default_prompt: "Use $dev-doc-harness to guide this repository development task through the appropriate planning, execution, and validation lifecycle."
   ```

5. Treat the metadata file as required distributable content. Validate the interface keys, the 25-64 character short description, and the explicit `$dev-doc-harness` reference without adding a runtime dependency to the repository validator.
6. Include the operator's current README changes in the implementation commit. Preserve their wording except for a narrowly necessary validation correction that is reported before use.
7. Retain the current installation-neutral `SKILL.md` path wording in the implementation boundary.
8. Do not change `.agents/skills/dev-doc-harness/docs/operator-note.md`, canonical policy meaning, templates, frozen planning artifacts, or release notes during this implementation. The operator-authorized later paragraph-only unwrap of README and operator note is separate mechanical work.

## Implementation tasks

### `AMD-002-TASK-001` Compact the bootstrap and add skill UI metadata

**Files**

- Modify: `AGENTS.md`
- Modify: `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py`
- Create: `.agents/skills/dev-doc-harness/agents/openai.yaml`
- Preserve and include: `README.md`
- Preserve and include: `.agents/skills/dev-doc-harness/SKILL.md`
- Update: `docs/work-items/2026-07-27_harness-execution-flow-clarity/deltas/testing-guide.delta.md`
- Update: `docs/work-items/2026-07-27_harness-execution-flow-clarity/changelog/implementation.md`
- Do not modify: `.agents/skills/dev-doc-harness/docs/operator-note.md`

**Interfaces**

- Consumes: the active `AGENTS.md` bootstrap contract, `SKILL.md` router, `module:architecture` dependency direction, existing golden-traversal checks, the approved operator README diff, and the `openai.yaml` schema from the installed skill-authoring guidance.
- Produces: a shorter behavior-equivalent root bootstrap, semantic validator coverage for its required anchors, and UI metadata for the `dev-doc-harness` skill.

1. Add `skill.openai-metadata` to the validator check IDs and add the expected metadata path to required files. Add focused assertions for the exact three interface fields, short-description length, `$dev-doc-harness` reference, and absence of unrequested interface fields.
2. Replace exact-sentence `AGENTS.md` expectations with semantic anchor checks that still fail if activation, policy selection, artifact/lifecycle precedence, canonical work-item location, combined planning, the `docs/superpowers` guard, execution-start routing, or distribution scope disappears.
3. Add a compactness assertion for the source repository's root `AGENTS.md` with a maximum of 360 whitespace-delimited words.
4. Run `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`. Expected RED result: `skill.openai-metadata` fails because `agents/openai.yaml` does not exist, and any new compactness or semantic fixture that the current bootstrap does not satisfy reports its specific missing condition.
5. Rewrite `AGENTS.md` to the approved conservative form. Keep the validator-protected anchors explicit and route detailed compatibility and execution mechanics to the active skill.
6. Generate the metadata deterministically with the installed skill creator's `generate_openai_yaml.py`, passing the three approved interface values. Do not hand-add optional icons, brand color, dependencies, or invocation policy.
7. Run the focused validator again. Expected GREEN result: `PASS skill.openai-metadata` and the existing compatibility, lifecycle, discovery, execution, and scenario checks pass.
8. Run the installed skill creator's `quick_validate.py` against `.agents/skills/dev-doc-harness`. Expected result: `Skill is valid!`
9. Run one fresh-agent bootstrap smoke test using the changed `AGENTS.md` and active skill without supplying the expected answer. The scenario must require the agent to discover work sizing, combined planning, Superpowers/harness ownership, and the guarded legacy compatibility route. Record the review outcome in the implementation handoff; do not add another durable report unless the reviewer produces material evidence.
10. Update `deltas/testing-guide.delta.md` with the semantic bootstrap and metadata validation coverage. Update `changelog/implementation.md` before the implementation commit and keep its heading synchronized with the planned subject.
11. Run the full harness validator, `python .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check`, changelog lint, metadata searches, `git diff --check`, and a changed-file inspection. Confirm `operator-note.md`, templates, frozen artifacts, and release notes are absent from the diff.
12. Dispatch one independent final reviewer with a bootstrap-regression and package-metadata lens. Provide the amendment, changed files, RED/GREEN evidence, smoke-test result, and verification output. Address actionable findings and repeat complete verification.
13. Commit the reviewed implementation with the planned subject below.

## Impact assessment

- Outcome: agents retain the current bootstrap behavior with less duplicated prose, while Codex UI surfaces can identify and invoke the skill with human-facing metadata.
- Evidence: semantic bootstrap checks, a failing-then-passing metadata check, the full validator, official skill validation, and a fresh-agent smoke test.
- Interfaces: root repository instructions, validator fixtures, and the new `agents/openai.yaml` UI metadata file. No canonical rule, template schema, runtime API, or external service changes.
- Documentation: include the current README changes and testing-guide delta; leave `operator-note.md` unchanged during this implementation because it already provides the package-local operator explanation and does not own UI metadata.
- Data, infrastructure, security, privacy, and compliance: no change.
- Risk: excessive compaction could hide a bootstrap guard; semantic anchor checks and fresh-agent validation preserve those guards without exact prose coupling. Metadata could drift from `SKILL.md`; validator assertions protect the approved identity and default prompt.
- Rollback: revert the implementation commit to restore the longer bootstrap and remove the UI metadata file.

## Current planning Codex task

- Model/profile: current Codex model; exact resolved profile is not exposed.
- Reasoning: not exposed.
- Context visibility: not exposed.

## Next-stage recommendation

### Activity

- Next activity: implement this amendment after approval freeze and fresh authorization.
- First Plan Task: `AMD-002-TASK-001`.

### Orchestration

- Method: `superpowers:executing-plans` for the single tightly coupled documentation, metadata, and validator task.
- Run in: same Codex task to preserve the operator-owned README and current skill/test working-tree changes.
- Plan Task reviewers: one independent final reviewer after the task; authorized by amendment approval.

### Model

- Implementation: balanced tier, medium reasoning; Terra medium when available.
- Final review: balanced tier, medium reasoning; Terra medium when available.

### Fallbacks and limits

- Sub-agents: None for implementation because all changed surfaces share one bootstrap and validation contract; one fresh-agent smoke test and one independent final review are the bounded validation uses.
- If the reviewer cannot run, use the approved disclosure and one-time operator-decision route in `module:models`.
- Stop for another amendment before removing a protected bootstrap anchor, changing canonical policy meaning, editing `operator-note.md` as part of this implementation, adding optional metadata fields, or modifying unrelated package/release surfaces. The separately authorized paragraph-only unwrap remains routine mechanical follow-up work.

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: operator approved the written amendment, required inclusion of the current README changes, and separately authorized a later paragraph-only unwrap of README and operator note in the current Codex task on 2026-07-28.
- Superseded by: None

## Planned commits

| Stage | Planned subject |
|---|---|
| Amendment approval | `amendment 002: harness-execution-flow-clarity -- compact bootstrap and add skill metadata` |
| Amended implementation | `feat: harness-execution-flow-clarity -- compact bootstrap and add skill metadata` |

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until this amendment is approved and frozen in its own planning commit, followed by fresh operator authorization.
