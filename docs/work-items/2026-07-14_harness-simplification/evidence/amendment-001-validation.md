# Amendment 001 validation

Work ID: `2026-07-14_harness-simplification`
Amendment: `001`
Status: Validated

## Fixed authoring-manifest measurement

The frozen manifest and token rule in
[`active-authoring-baseline.md`](../snapshots/active-authoring-baseline.md)
were run without changing their path list. The verified baseline was 2,135
nonblank lines and 24,255 words. The final measurement is 1,843 nonblank lines
and 18,942 words: a reduction of 292 lines and 5,313 words.

| Path | Final nonblank lines | Final words |
| --- | ---: | ---: |
| `.agents/skills/dev-doc-harness/SKILL.md` | 58 | 1,240 |
| `.agents/skills/dev-doc-harness/docs/operator-note.md` | 102 | 735 |
| `.agents/skills/dev-doc-harness/references/artifact-contract.md` | 227 | 2,807 |
| `.agents/skills/dev-doc-harness/references/context-and-quality-gates.md` | 65 | 633 |
| `.agents/skills/dev-doc-harness/references/durable-planning-quality.md` | 89 | 892 |
| `.agents/skills/dev-doc-harness/references/artifact-style.md` | 103 | 883 |
| `.agents/skills/dev-doc-harness/references/subagent-model-policy.md` | 166 | 2,499 |
| `.agents/skills/dev-doc-harness/assets/templates/blocks/spec.030.common.commitments-verification.md` | 24 | 164 |
| `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.020.common.traceability-approach-surfaces.md` | 9 | 71 |
| `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.050.common.task-plan.md` | 18 | 119 |
| `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.070.common.validation-variance-freeze.md` | 5 | 32 |
| `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.085.common.handoff.md` | 4 | 32 |
| `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.small.readiness-completion-approval.md` | 9 | 58 |
| `.agents/skills/dev-doc-harness/assets/templates/blocks/plan.090.phase.readiness-completion-approval.md` | 9 | 64 |
| `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-spec.md` | 150 | 1,618 |
| `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-spec.md` | 221 | 2,325 |
| `.agents/skills/dev-doc-harness/assets/templates/small-medium-work-item-plan.md` | 111 | 975 |
| `.agents/skills/dev-doc-harness/assets/templates/large-phased-work-item-phase-plan.md` | 138 | 1,272 |
| `.agents/skills/dev-doc-harness/assets/templates/plan-amendment.md` | 33 | 220 |
| `.agents/skills/dev-doc-harness/assets/templates/variance-log.md` | 16 | 96 |
| `README.md` | 286 | 2,207 |
| **Final aggregate (21 files)** | **1,843** | **18,942** |
| **Verified baseline (21 files)** | **2,135** | **24,255** |
| **Delta (final − baseline)** | **−292** | **−5,313** |

## Commands and results

| Command | Result |
| --- | --- |
| `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --write` | Exit 0; all 30 policy checks passed and all assembled templates are current. |
| `python -X utf8 .agents/skills/dev-doc-harness/scripts/test_harness_policy.py` | Exit 0; all 30 policy checks passed. |
| `python -X utf8 .agents/skills/dev-doc-harness/scripts/assemble_templates.py --check` | Exit 0; `All assembled templates are current.` |
| Exact PowerShell block in `snapshots/active-authoring-baseline.md` | Exit 0; 21 files, 1,843 nonblank lines, and 18,942 words. |
| `git diff --check` | Exit 0; no whitespace-error output. Git emitted seven informational LF-to-CRLF conversion warnings for already modified tracked files. |
| `python -X utf8 .agents/skills/dev-doc-harness/scripts/consolidate_changelog_fragments.py --lint` | Exit 0; fragment grammar and duplicate-heading checks passed. |

## Assumptions and residual risk

- The frozen baseline is the approved before-state for this amendment; it is
  reported as supplied and has not been rewritten.
- The manifest deliberately excludes validation code, evidence, changelog
  fragments, frozen history, and `LICENSE`; its reductions do not measure those
  surfaces.
- The checks establish policy and assembly consistency but do not replace the
  separate independent amendment review record.

## Recommended next step

Have the independent reviewer create and assess the amendment review record.
If it has no blocking finding, an operator can stage and commit the approved
implementation and amendment-owned evidence.
