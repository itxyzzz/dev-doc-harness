# Sub-Agent Autonomy Policy Plan

Work ID: `2026-06-05-subagent-autonomy-policy`
Short ID: `subagent-autonomy-policy`
Status: Approved

## Implementation summary

Update the harness wording so agents treat sub-agent use as a deliberate planning decision for substantial work. The canonical change belongs in `subagent-model-policy.md`: it should state that missing operator mention is not a prohibition, approved plans authorize their listed strategy after the normal post-freeze implementation authorization, repeated sub-agent-specific confirmations are only needed for unplanned or escalated delegation, and the normal cap applies to concurrent sub-agents rather than total sub-agents across a long-running orchestration.

After the canonical policy is updated, align the plan/spec templates so future artifacts teach the same behavior. Finally, update the README operator overview so users understand they can approve a plan containing a justified sub-agent strategy and then say `Confirm, proceed` without repeating sub-agent permission again.

## Files and interfaces

Expected files to change:

- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md`
- `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md`
- `README.md`
- `CHANGELOG.md`

Interfaces expected to remain stable:

- Work item folder naming and required artifact layout.
- Planning freeze gate commit-and-pause behavior.
- Requirement for fresh post-freeze authorization before implementation starts.
- Active `economy-default` repository policy.
- Final integration ownership by the orchestration thread.
- Amendment requirements for high-impact post-freeze variance.

## Model and Sub-agent Strategy

Current orchestration: GPT-5 Codex, reasoning effort not explicitly provided.
Fit assessment: moderate process risk and low implementation risk. The change is documentation-only, but it affects how future agents interpret delegation authority, approval semantics, and cost/risk boundaries. Budget and latency support one bounded reviewer sub-agent after implementation because consistency across policy, templates, and README is the main risk.
Recommended change: None.

Sub-agents: Use 1 reviewer sub-agent after the main-thread implementation, if sub-agent tooling is available. This is within the normal concurrent cap of 3 and does not require a model/reasoning override.

| Purpose | Input context | Output artifact | Model policy | Model class/profile | Reasoning effort | Reason | Parallel? | Blast radius if wrong |
|---|---|---|---|---|---|---|---|---|
| Documentation consistency review | Approved spec, approved plan, changed policy/templates/README, and changelog entry | Review findings in final implementation notes or chat summary | `economy-default` | standard or smaller/faster reviewer | medium | Bounded review with clear inputs; catches old confirmation language without making final decisions | No | Low; orchestration thread owns final integration and validation |

## Tasks

- [ ] Update `subagent-model-policy.md` to say agents must assess justified sub-agent use for substantial work even when the operator did not explicitly request sub-agents.
- [ ] Add language requiring a brief fit reason when substantial-work plans record `Sub-agents: None`.
- [ ] Replace the blanket confirmation-before-applying rule with approval semantics: approved frozen plans authorize their listed sub-agent strategy after the normal post-freeze implementation-start authorization.
- [ ] Document the normal cap of 3 concurrent sub-agents and require explicit extraordinary justification plus approval for more than 3 concurrent sub-agents.
- [ ] Clarify that long-running orchestrations may use more than 3 total sub-agents in separate waves when the approved plan supports it and no more than 3 run concurrently.
- [ ] Preserve fresh confirmation requirements for unplanned sub-agents, exceeding approved concurrent count, more than 3 concurrent sub-agents, non-recorded model/reasoning escalation, write-scope escalation, and platform-restricted actions.
- [ ] Add a completion-report requirement for de-facto sub-agent use, including count, roles/scopes, concurrency or waves, and de-facto model, model class, or profile when known.
- [ ] Align `small-medium-work-item-plan.md` with the new proactive assessment and approved-strategy authorization behavior.
- [ ] Align `large-phased-work-item-spec.md` with the new proactive assessment and approved-strategy authorization behavior.
- [ ] Align `large-phased-work-item-phase-plan.md` with the new proactive assessment and approved-strategy authorization behavior.
- [ ] Update `README.md` so the operator-facing flow explains that approved plans can authorize justified sub-agent use without repeated permission prompts.
- [ ] Add a newest-first `CHANGELOG.md` entry for the implementation work before committing implementation changes.
- [ ] Run a documentation consistency review, using the planned reviewer sub-agent if available.
- [ ] Review all changed docs for consistent terminology around `sub-agent`, `operator mention`, `approval`, `post-freeze authorization`, `confirmation`, `concurrent cap`, `waves`, `de-facto model`, and `escalation`.

## Validation commands

| Command | Expected result |
|---|---|
| `rg -n "sub-agent|Sub-agents|operator confirmation|explicit operator confirmation|before applying|approved strategy|more than 3|normal cap|concurrent|waves|de-facto|Confirm, proceed" .agents README.md CHANGELOG.md docs/work-items/2026-06-05-subagent-autonomy-policy` | Remaining matches are consistent with the approved-strategy authorization model, normal 3-concurrent-sub-agent cap, wave allowance, and de-facto reporting requirement |
| `git diff --check` | No whitespace errors |
| `git status --short` | Only intended harness documentation, README, changelog, and local planning files are modified or staged |

## Plan variance handling

Before approval, operator feedback edits this draft directly and does not require an amendment. After the approval commit or explicit handoff snapshot, approved plans are immutable snapshots. Record nontrivial implementation variance in `implementation-notes/variance-log.md` if implementation departs from this plan. Create a plan amendment and request operator approval before proceeding when post-freeze variance affects architecture, APIs, data, security, privacy, compliance, scope, acceptance criteria, or plan feasibility.

## Planning artifact freeze gate

When this plan is ready for operator review, follow the repository-root reference `.agents/skills/dev-doc-harness/references/planning-freeze-gates.md`: stage the draft without committing, request approval or feedback, revise directly on feedback, and commit only after explicit approval.

After the approval commit, use the canonical post-freeze prompt to confirm model, reasoning-effort, and sub-agent policy choices and ask whether implementation should begin now. Approval of this plan plus a clear post-freeze instruction to begin authorizes the listed reviewer sub-agent without a separate sub-agent-specific confirmation.

## Completion criteria

- Acceptance criteria in `spec-subagent-autonomy-policy.md` are met.
- Required validation commands have been run and recorded.
- Required documentation artifacts have been created or updated.
- `CHANGELOG.md` has a newest-first entry for the work before each commit.
- No variance log is required unless implementation departs nontrivially from this approved plan.

## Approval

- Status: Approved
- Superseded by: None
