# Artifact Style Ownership Cleanup Test Cases

Work ID: `2026-07-30_artifact-style-ownership-cleanup`
Status: Approved

| Scenario | Input | Method | Expected result |
|---|---|---|---|
| `scenario:quality.plain-language-owner` | Revised Quality, Artifact Style, template source block, and generated templates | Run targeted rule-ID searches and `assemble_templates.py --check` | `rule:quality.plain-language` is the sole current plain-language owner and templates cite it. |
| `scenario:validator.plain-language-enforcement` | Revised validator and synthetic active Markdown containing `shall` | Run `test_harness_policy.py` | The synthetic active-surface occurrence fails; frozen, legal, and fixture exclusions remain outside the active scan; no definition-only policy exception is required. |
| `scenario:style.owner-consolidation` | Revised Artifact Style, Quality, and policy architecture | Inspect owner tables and run the full validator | Artifact Style has no Plain language or Verification Criterion placement rule; Quality owns the relevant semantic rules; one retained traceability rule remains. |
| `scenario:artifact-style.reflow-preservation` | Operator-authored Artifact Style reflow | Review scoped diff and run `git diff --check` | One-line paragraph reflow remains; only the identified doubled space is corrected; no unrelated formatting churn appears. |
| `scenario:historical-artifact-preservation` | Existing `docs/work-items/` history | Review name-only implementation diff | No frozen historical artifact changes solely to reflect the revised current owner graph. |
