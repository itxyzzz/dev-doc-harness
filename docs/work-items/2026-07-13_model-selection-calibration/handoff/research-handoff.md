# Research Handoff: Model Selection Calibration

Work ID: `2026-07-13_model-selection-calibration`

Status: Source evidence for the approved combined planning package; it does not authorize implementation.

## Purpose

Draft a concise harness policy change that makes `economy-default` more operationally efficient after the GPT-5.6 Sol/Terra/Luna model-family update. Preserve the durable tier model and existing authorization boundaries while making selection, escalation, de-escalation, and independent-review use more evidence-based.

## Read first

1. `AGENTS.md`
2. `.agents/skills/dev-doc-harness/SKILL.md`
3. `.agents/skills/dev-doc-harness/references/artifact-contract.md`
4. `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
5. `docs/work-items/2026-07-13_model-selection-calibration/evidence/model-selection-research.md`
6. This handoff.

## Agreed design direction

1. Keep the harness concise and small. Prefer a few clear defaults, decision rules, and informative examples over a large decision tree or duplicated guidance.
2. Frame model, effort, and reviewer allocations as suggested options. The operator approves the recorded strategy and may always override it.
3. Use Terra medium as the suggested baseline for substantial bounded work under `economy-default`.
4. Treat the tier and reasoning effort as separate decisions:
   - effort escalation means the task model remains correct but needs more deliberate traversal;
   - tier escalation means ambiguity handling, judgment, or capability is the limiting factor.
5. Make lifecycle progression material: completed spec and plan stages should lower expected ambiguity and unknowns. A later-stage escalation must name the residual uncertainty or new variance that justifies it.
6. Do not escalate ceremonially because the phase is labelled planning, implementation, or final review.
7. Treat missing product input, an undecided requirement, or a plan contradiction as a variance/approval problem, not a prompt to spend more on a stronger model.
8. Reviewers are already routinely useful. Avoid creating duplicate review mechanics; refine existing reviewer guidance to require efficient independence and a defined lens.
9. Historical calibration is preserved in `evidence/model-selection-research.md`. In the 15 newest harness specs, four are Terra-medium authoring candidates, seven Terra-high candidates, and four Sol-medium candidates; none needs Sol high as its first-pass author configuration. Sol high is instead concentrated in bounded independent review of foundational or high-risk transition work.

## Proposed compact decision model

### Baseline and changes

| Situation | Suggested allocation | Change signal |
|---|---|---|
| Substantial bounded work with explicit outputs and validation | Terra medium | Default |
| Same correct approach needs fuller dependency/edge-case traversal | Terra high | More effort, not a tier jump |
| Ambiguity, competing interpretations, unclear causal chain, or difficult judgment remains | Sol medium | Stronger tier, keep effort moderate first |
| Sol medium leaves a high-impact conflict or unresolved evidence | Sol high | Exceptional escalation with written reason |

### De-escalation

Return to Terra medium or high when a frozen spec/plan, explicit acceptance criteria, deterministic checks, or a fixed review lens make the remaining work bounded. Do not retain Sol/high merely because it was used earlier in the lifecycle.

### Efficient independent review

Use the existing reviewer strategy but make independence explicit:

- separate task or thread, not a full-history fork;
- curated approved artifacts, diff, validation evidence, and a short role prompt;
- no executor chain-of-thought or self-justification;
- one defined lens, such as requirements traceability, regression risk, security/migration, test adequacy, or adversarial counterexamples;
- evidence-backed findings with severity and a reproduction or validation path;
- orchestration thread keeps final integration ownership.

Suggested review allocation:

| Change profile | Executor | Independent reviewer |
|---|---|---|
| Normal bounded change | Terra medium | None, or Terra high for a named lens |
| Important multi-file change with a clear plan | Terra medium/high | Terra high, separate task |
| High-blast change with a clear plan | Terra high | Sol medium, adversarial review |
| Uncertain architecture or irreversible decision | Sol medium | Sol high only for the bounded decision/review pass |

Spending more on an independent reviewer than on a clear-plan executor is permitted and often desirable. It is quality-control allocation, not evidence that the executor's task is highly ambiguous.

## Current policy surfaces likely to need review

Do not assume every surface changes. During spec drafting, identify the smallest coherent set, likely centered on:

- `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`
- `.agents/skills/dev-doc-harness/references/subagent-role-examples.md`
- relevant reusable model-strategy template blocks and generated templates
- `README.md` only if a concise operator-facing explanation is needed
- `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` for enforceable, non-duplicative policy checks

The previous 2026-07-11 model-selection package is relevant context but remains frozen historical evidence. Do not edit it.

## Next activity and stop condition

Next activity: use the approved combined package to create a new implementation task with curated artifacts, then begin the documented first implementation task only after fresh authorization.

Stop condition: do not modify current policy, templates, README, validation, or generated outputs until the new spec and plan have passed the Planning Artifact Freeze Gate and the operator gives a fresh post-freeze instruction.

## Known worktree state

At the time of research, `docs/work-items/2026-07-12_new-task-handoff-visibility/changelog/implementation.md` was already modified and is unrelated. Preserve it.
