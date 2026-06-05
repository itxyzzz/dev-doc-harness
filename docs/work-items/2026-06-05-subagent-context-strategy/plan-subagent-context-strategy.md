# Sub-Agent Context Strategy Plan

Work ID: `2026-06-05-subagent-context-strategy`
Short ID: `subagent-context-strategy`
Status: Approved

## Implementation summary

Update the harness so context shaping is a first-class sub-agent planning decision. The canonical change belongs in `subagent-model-policy.md`: add `Context strategy` to required notation, define the expected strategy vocabulary, explain why full-history forks require deliberate use, and require de-facto reporting of the context strategy actually used.

After the canonical policy is updated, align the reusable templates and sub-agent role examples so new specs/plans naturally include this field. Finally, update README and changelog so operators know that sub-agent planning now covers both model/reasoning choices and context-shaping choices.

## Files and interfaces

Expected files to change:

- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`
- `README.md`
- `CHANGELOG.md`

Interfaces expected to remain stable:

- Work item folder naming and required artifact layout.
- Planning freeze gate commit-and-pause behavior.
- Approved-plan authorization for listed sub-agent strategies.
- 3-concurrent-sub-agent guardrail and wave allowance.
- Active `economy-default` repository policy.
- Final integration ownership by the orchestration thread.

## Model and Sub-agent Strategy

Current orchestration: GPT-5 Codex, reasoning effort not explicitly provided.
Fit assessment: low implementation risk and moderate process risk. The change is documentation-only, but it affects future delegation quality and context hygiene. Budget and latency support one bounded post-implementation reviewer because consistency across policy, templates, role examples, and README is the main risk.
Recommended change: None.

Sub-agents: Use 1 reviewer sub-agent after the main-thread implementation, if sub-agent tooling is available. This is within the normal concurrent cap of 3 and does not require a model/reasoning override.

| Purpose | Context strategy | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|---|
| Documentation consistency review | curated prompt | Approved spec, approved plan, changed policy/templates/role examples/README, and changelog entry | Review findings in final implementation notes or chat summary | `economy-default` | standard or smaller/faster reviewer | medium | Bounded review with clear inputs; context can be summarized without full-history fork | No | Low; orchestration thread owns final integration and validation |

## Tasks

- [ ] Update `subagent-model-policy.md` required field list to include `Context strategy`.
- [ ] Update the canonical Model and Sub-agent Strategy table example to include a `Context strategy` column.
- [ ] Define context strategy guidance for `curated prompt`, `curated artifacts`, `full-history fork`, and `no repo context`.
- [ ] Document that full-history forks should be deliberate and may force inherited model/reasoning/agent-type behavior depending on platform.
- [ ] Update de-facto reporting requirements to include context strategy actually used and observed context/model inheritance behavior.
- [ ] Add `Context strategy` to the small/medium plan template table and instructions.
- [ ] Add `Context strategy` to the large/phased spec template table and instructions.
- [ ] Add `Context strategy` to the large/phased phase-plan template table and instructions.
- [ ] Update `subagent-role-examples.md` so the portable role shape includes context strategy.
- [ ] Update `README.md` so operators understand context strategy is part of sub-agent planning.
- [ ] Add a newest-first `CHANGELOG.md` entry for the implementation work before committing implementation changes.
- [ ] Run a documentation consistency review, using the planned reviewer sub-agent if available.
- [ ] Review changed docs for consistent terminology around `context strategy`, `curated prompt`, `curated artifacts`, `full-history fork`, `fork_context`, `inheritance`, and `de-facto`.

## Validation commands

| Command | Expected result |
|---|---|
| `rg -n "Context strategy|context strategy|curated prompt|curated artifacts|full-history fork|fork_context|no repo context|inherit|de-facto" .agents README.md CHANGELOG.md docs/work-items/2026-06-05-subagent-context-strategy` | Remaining matches show the new context-strategy policy, template columns, README explanation, changelog entry, and approved planning context |
| `rg -n "\\| Purpose \\| Input context \\| Output artifact \\| Model policy|\\| Phase \\| Purpose \\| Input context \\| Output artifact \\| Model policy" .agents/skills/dev-doc-harness/references/subagent-model-policy.md .agents/skills/dev-doc-harness/assets/templates` | No stale Model and Sub-agent Strategy tables remain without `Context strategy` |
| `git diff --check` | No whitespace errors |
| `git status --short` | Only intended harness documentation, README, changelog, and local planning files are modified or staged |

## Plan variance handling

Before approval, operator feedback edits this draft directly and does not require an amendment. After the approval commit or explicit handoff snapshot, approved plans are immutable snapshots. Record nontrivial implementation variance in `implementation-notes/variance-log.md` if implementation departs from this plan. Create a plan amendment and request operator approval before proceeding when post-freeze variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

When this plan is ready for operator review, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage the draft without committing, request approval or feedback, revise directly on feedback, and commit only after explicit approval.

After the approval commit, use the canonical post-freeze prompt to confirm model, reasoning-effort, and sub-agent policy choices and ask whether implementation should begin now. Approval of this plan plus a clear post-freeze instruction to begin authorizes the listed reviewer sub-agent without a separate sub-agent-specific confirmation.

## Completion criteria

- Acceptance criteria in `spec-subagent-context-strategy.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- De-facto sub-agent use is reported when applicable, including count, roles/scopes, concurrency or waves, context strategy, and de-facto model/model class/profile when known.
- No variance log is required unless implementation departs nontrivially from this approved plan.

## Approval

- Status: Approved
- Superseded by: None
