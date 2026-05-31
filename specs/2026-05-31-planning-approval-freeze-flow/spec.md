# Planning Approval Freeze Flow Spec

Work ID: `2026-05-31-planning-approval-freeze-flow`
Status: Approved

## Goal

Make the harness planning lifecycle match the operator review loop: agents draft planning artifacts, stage them for review without committing, revise those drafts in response to feedback, and only commit the planning package after explicit operator approval. Planning artifacts become immutable only after that approval-and-commit checkpoint, not after the first draft review request.

## Scope

- Update the canonical freeze-gate rules so the review checkpoint is split into:
  - draft and stage planning artifacts without committing;
  - request operator approval or feedback;
  - revise staged drafts when feedback arrives;
  - commit only after explicit approval;
  - treat the package as frozen only after the approval commit or explicit handoff.
- Update lifecycle language in the skill entry point, artifact contract, durable planning quality reference, templates, and README where needed.
- Preserve the amendment process for changes discovered after the planning package is frozen.
- Preserve the requirement to stop before implementation until a fresh explicit operator instruction is given after the approval commit.

## Non-scope

- No change to work item sizing, folder naming, required artifact types, variance classes, or model/sub-agent policy.
- No implementation code changes; this repository currently stores the harness as documentation, templates, and process references.
- No automation to enforce staging or commits beyond the written harness contract.
- No change to ordinary implementation commits after planning has been approved.

## Current state

The canonical freeze-gate reference currently tells agents to update `CHANGELOG.md`, stage finalized planning artifacts, commit them, and then ask for operator confirmation before implementation. In practice, this can make the first draft review request look like a freeze event. If the operator gives feedback after that point, agents may treat the reviewed documents as immutable and incorrectly create an amendment instead of simply editing the draft.

Supporting documents and templates reinforce this by using phrases such as "commit-and-pause" and by describing finalized artifacts as frozen at the same checkpoint where the operator is meant to review them.

## Proposed behavior

The planning lifecycle should distinguish draft review from freeze:

1. The agent creates or updates planning artifacts as drafts.
2. The agent stages the draft planning artifacts so the operator can inspect the exact package under review, but does not commit.
3. The agent asks the operator for approval or feedback.
4. If the operator gives feedback, the agent edits the draft planning artifacts, refreshes staging, and asks for approval again.
5. When the operator explicitly approves, the agent updates `CHANGELOG.md`, performs final placeholder and completeness checks, stages only the approved planning artifacts and `CHANGELOG.md`, commits them, reports the commit hash and artifact paths, and suggests a plan-only PR.
6. From that approval commit onward, the planning package is frozen. Later high-impact changes use amendments.

Explicit handoff remains a valid freeze trigger when the operator asks to preserve a planning snapshot for another thread without using the normal review loop.

## Interfaces and data

Affected repository interfaces are documentation-facing:

- `.agents/skills/dev-doc-harness/SKILL.md`
- `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`
- `.agents/skills/dev-doc-harness/references/artifact-contract.md`
- `.agents/skills/dev-doc-harness/references/durable-planning-quality.md`
- `.agents/skills/dev-doc-harness/assets/templates/*.md`
- `README.md`
- `CHANGELOG.md`

No public API, runtime config, schemas, persistence, CLI flags, or generated data formats are affected.

## Risks

- Agents may still infer the old flow from stale wording if not all canonical and operator-facing references are updated consistently.
- If the new language over-emphasizes staging, agents might stage unrelated work. The updated gate must retain the existing "stage only relevant paths" rule.
- If the new language makes approval too vague, agents could commit after ambiguous feedback. The implementation should require explicit operator approval before committing.
- The plan-only PR suggestion should move to the post-approval commit checkpoint so draft review remains lightweight.

## Acceptance criteria

- `planning-freeze-gates.md` clearly defines a draft review checkpoint that stages but does not commit planning artifacts.
- `planning-freeze-gates.md` clearly defines the approval commit checkpoint and states that planning artifacts freeze only after explicit approval and commit, or explicit handoff.
- Feedback before approval is handled by editing draft artifacts and re-requesting approval, not by creating amendments.
- Amendment language remains reserved for high-impact variance after the planning package is frozen.
- `SKILL.md`, `artifact-contract.md`, templates, and README no longer imply that the first review request commits or freezes planning artifacts.
- The README operator flow reflects draft review before the freeze/approval commit.
- `CHANGELOG.md` receives a newest-first entry before the implementation commit.
- Validation confirms no stale "commit-and-pause" language remains where it describes the pre-approval review loop.

## Documentation artifact matrix

| Artifact | Type | Required? | Stage | Output path | Notes |
|---|---|---:|---|---|---|
| Changelog | Living | Yes | Before each commit | `CHANGELOG.md` | Required for the approval planning commit and final implementation commit |
| Test cases | Snapshot | No | Not applicable | docs/snapshots/test-cases.snapshot.md | Documentation/process wording change only |
| Testing guide delta | Living delta | No | Not applicable | docs/living/testing-guide.delta.md | No test workflow change |
| Operator manual delta | Living delta | No | Not applicable | docs/living/operator-manual.delta.md | README and harness references are the operator-facing docs for this repo |
| API reference delta | Living delta | No | Not applicable | docs/living/api-reference.delta.md | No API change |
| Architecture snapshot | Snapshot | No | Not applicable | docs/snapshots/architecture.snapshot.md | No architecture change |
| Architecture summary delta | Living delta | No | Not applicable | docs/living/architecture-summary.delta.md | No long-lived architecture summary change |

## Approval

- Status: Approved
- Superseded by: None
