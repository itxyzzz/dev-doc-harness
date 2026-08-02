# Router and Maintenance Architecture Test Cases

Work ID: `2026-08-01_router-maintenance-architecture`
Status: Approved

| Scenario | Input | Method | Expected result |
|---|---|---|---|
| `scenario:router.single-operational-owner` | Revised `SKILL.md` and `maintenance-architecture.md` | Inspect headings and run the focused validator assertion | `SKILL.md` contains the only operation router; the maintenance reference has no `Router Inputs` table. |
| `scenario:maintenance.reference-content` | Renamed reference | Search for removed provenance, obsolete content types, and `Reusable policy source?` | No `docs/work-items/` provenance or removed column exists; only Normative policy, Advisory guidance, and Example remain. |
| `scenario:planning.naming-input` | Revised small/medium and large planning routes | Inspect router required inputs and template policy references | New planning explicitly has naming, lifecycle, quality, and models input; artifact style, evidence, and architecture snapshots remain conditional by their documented triggers. |
| `scenario:freeze-gate-deferral` | Revised router and plan/phase-plan source blocks | Search draft-time route and template policy references for `module:freeze-gate` and `rule:freeze` | Drafting does not require the gate; `Freeze planning packages` remains a distinct required route and retains package-completeness, approval, commit, and stop-before-implementation checks. |
| `scenario:validator-rename-continuity` | Canonical reference lists, validator constants, source blocks, generated templates | Run template assembly check and `test_harness_policy.py` | All paths and assertions use `maintenance-architecture.md`; generated templates match source blocks; full validator passes. |
| `scenario:historical-artifact-preservation` | Scoped implementation diff | Review name-only diff and `git diff --check` | No frozen historical planning artifact is changed merely for the current reference rename; no whitespace error appears. |
