# Model-Selection Research Verification

Research date: 2026-07-13

## Verification summary

The evidence supports an economy-default policy with Terra at medium reasoning as the normal substantial-work baseline. Sol remains materially stronger on broad capability measures, but its tier cost and latency make it an escalation choice. Increasing effort within a tier yields a smaller average capability lift than moving from Terra to Sol. The sources are early-release evidence rather than repository-local evaluation, so the final policy should require local calibration and operator approval rather than claim a universal optimum.

## Verified claims

1. OpenAI positions Sol for complex professional reasoning and coding, Terra for balancing intelligence and cost, and Luna for cost-sensitive high-volume work. Sol is priced at $5 input / $30 output per million tokens; Terra at $2.50 / $15; Luna at $1 / $6.
   - Source: https://developers.openai.com/api/docs/models
   - Source: https://openai.com/index/gpt-5-6/

2. The independent Artificial Analysis Intelligence Index compares quality, price, speed, latency, and context. Its documented composite currently covers nine evaluations including agentic coding, tool use, long-context reasoning, science, and knowledge reliability.
   - Source and methodology: https://artificialanalysis.ai/models/comparisons/gpt-5-6-sol-medium-vs-gpt-5-6-terra-medium

3. Current comparison values on the Artificial Analysis pages are:

   | Configuration | Intelligence Index | Output speed | Time to first answer |
   |---|---:|---:|---:|
   | Terra medium | 46 | 139 tokens/s | 1.87 s |
   | Terra high | 49 | 126 tokens/s | 6.36 s |
   | Sol medium | 54 | 63 tokens/s | 4.04 s |
   | Sol high | 56 | 69 tokens/s | 29.31 s |

   - Terra medium versus high: https://artificialanalysis.ai/models/comparisons/gpt-5-6-terra-high-vs-gpt-5-6-terra-medium
   - Sol medium versus Terra medium: https://artificialanalysis.ai/models/comparisons/gpt-5-6-sol-medium-vs-gpt-5-6-terra-medium
   - Sol high versus Terra high: https://artificialanalysis.ai/models/comparisons/gpt-5-6-sol-high-vs-gpt-5-6-terra-high
   - Sol high versus medium: https://artificialanalysis.ai/models/comparisons/gpt-5-6-sol-high-vs-gpt-5-6-sol-medium

4. The values imply that the tier move is larger than the effort move in this aggregate metric: Terra medium to high is +3 points; Sol medium to high is +2; Terra medium to Sol medium is +8. Terra high to Sol medium is an inferred +5 from the published values. The displayed blended token price is about 2x for Sol versus Terra, while actual per-task cost can rise further with reasoning-token use.

5. A hard multistage scientific-reasoning evaluation reports substantial gains from extra reasoning on its own workload: Sol rises from 22.5% at medium to 24.4% at high, and to 28.7% at max. This supports effort escalation for genuinely deep, constraint-heavy work, not as a default for ordinary implementation.
   - Source: https://cdn.openai.com/pdf/21938268-21af-442f-af93-3b2249afb241/genebench-pro.pdf

6. Independent practitioner evidence is mixed but informative. Simon Willison's controlled image prompt comparison found calculated costs from $0.0071 for Luna without reasoning to $0.4855 for Sol at max; it demonstrates that tier and effort are first-order cost decisions, not a universal task-cost estimate.
   - Source: https://simonwillison.net/2026/Jul/9/gpt-5-6/

7. CodeRabbit's early production-style review benchmark found that Sol detected more issues than Terra, but produced more raw comments and lower actionable precision. This supports paying for an independent high-capability reviewer when missed defects are expensive, while requiring evidence-backed findings and avoiding unfiltered comment volume.
   - Source: https://www.coderabbit.ai/blog/gpt-5-6-sol-and-terra-benchmark

## Quality assessment and caveats

- Official sources establish product positioning, prices, and vendor benchmarks; they do not establish the best route for this repository.
- Artificial Analysis is independent and publishes methodology, but its composite is not a substitute for repository-local task evaluation.
- CodeRabbit's results are useful reviewer evidence but are one vendor's benchmark and show a recall/precision trade-off.
- Community observations are too new and variable to be normative. Use them only as a reason to measure local completion cost, latency, and rework.
- No source proves that an implementation agent needs the same or stronger configuration as an independent reviewer. The recommended separation is a policy inference from the different roles and observed review trade-offs.

## Policy implications carried into the handoff

1. Terra medium is the suggested baseline for substantial bounded work.
2. Escalate effort when the task model is correct but requires more deliberate traversal; escalate tier when capability, ambiguity handling, or judgment is the limiting factor.
3. The harness lifecycle is a prior: finalized spec and plan artifacts should reduce unknowns. Later-stage escalation requires a named residual or newly discovered exception.
4. An independent reviewer may appropriately use more budget or a stronger tier than the executor when the plan is clear but an undetected defect has high cost.
5. All allocations remain suggested options. Operator approval and explicit overrides remain authoritative.

## Historical calibration: recent harness specifications

Method: read the 15 most recent dated work-item specifications available on 2026-07-13, from `2026-07-02_orchestration-sizing-large-templates` through `2026-07-13_multi-changelog-fragments`. The recommendation is for drafting the specification, not executing the resulting change. It estimates de-facto complexity from documented scope, unresolved decisions, cross-surface coupling, and consequences if the policy is framed incorrectly. It does not claim the original author used, or should retrospectively have used, a particular runtime configuration.

| Work item | De-facto drafting complexity | Suggested author | Independent review when warranted |
|---|---|---|---|
| `2026-07-13_multi-changelog-fragments` | Bounded parser/CLI, hook, release-flow, and fixture change with explicit semantics | Terra high | Terra high, focused on entry-boundary and release-gate regressions |
| `2026-07-12_user-facing-narrative` | Large but evidence-grounded documentation rewrite with unchanged canonical policy | Terra medium | Terra high only for policy-coverage review |
| `2026-07-12_superpowers-stub-continuity` | Narrow compatibility constraint and deletion with clear prior rule | Terra medium | None, or Terra high for cross-surface wording parity |
| `2026-07-12_new-task-handoff-visibility` | Cross-cutting lifecycle state transition and platform-capability boundary | Sol medium | Sol high, separate adversarial transition review |
| `2026-07-11_post-release-pr-flow` | Concrete runbook derived from stated operator process and Git safety checks | Terra medium | Terra high for remote/branch-safety review |
| `2026-07-11_model-selection-dimensions` | New model taxonomy, authorization layers, provider mapping, and handoff semantics | Sol medium | Sol high, independent policy/conflation review |
| `2026-07-11_commitment-verification-model` | Foundational conformance vocabulary and schema redesign across lifecycle and templates | Sol medium | Sol high, independent semantic/compatibility review |
| `2026-07-09_plan-task-block-format` | Bounded template-schema and validator change with clear design constraints | Terra high | Terra high for template/output parity |
| `2026-07-09_changelog-fragment-consolidation` | Parser, consolidation semantics, commit/release workflow, and compatibility constraints | Terra high | Sol medium only for adversarial data-loss/release-risk review |
| `2026-07-07_superpowers-compat-guidance` | Broad current-surface alignment plus a defined release-baseline correction | Terra high | Terra high for no-duplication and release-baseline review |
| `2026-07-04_release-branch-process` | Concrete agent-executed runbook from operator-specified branch and version rules | Terra medium | Terra high for safety/preflight review |
| `2026-07-03_work-item-architecture-decisions` | New durable decision boundary and lifecycle/template ownership model | Sol medium | Sol high, independent architecture/variance review |
| `2026-07-03_artifact-style-guidance` | Conditional module ownership and template hardening with stated non-duplication constraints | Terra high | Terra high for ownership/route-budget review |
| `2026-07-02_template-block-assembly` | Assembly tooling, generated-template workflow, hook, and release-marker alignment | Terra high | Terra high for regeneration/validator recursion review |
| `2026-07-02_orchestration-sizing-large-templates` | Sizing policy clarification and large-template restructuring with explicit intent | Terra high | Sol medium only if the reviewer finds an unresolved lifecycle/architecture conflict |

### Calibration result

- Terra medium: 4 of 15. These were primarily operator-specified or canonical-source-grounded runbooks, documentation, or narrow compatibility changes.
- Terra high: 7 of 15. These had many coupled current surfaces or exact edge cases, but their decision model was documented and bounded.
- Sol medium: 4 of 15. These introduced or materially revised foundational lifecycle, semantic, model, or architecture boundaries.
- Sol high: 0 of 15 as the preferred first-pass author. Its best role is a bounded, independent review of the four foundational changes and the highest-risk transition work.

This sample supports a concise default: most mature harness specifications should not begin above Terra medium or high. The larger model is a targeted authoring or reviewer choice when the spec itself must resolve a new governing abstraction, ambiguous state transition, or high-impact architectural boundary.
