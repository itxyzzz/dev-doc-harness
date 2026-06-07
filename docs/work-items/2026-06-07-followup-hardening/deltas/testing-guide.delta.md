# Testing Guide Delta: Structural Harness Validation

Work ID: `2026-06-07-followup-hardening`
Status: Final

## Validation command

Run this command from the repository root before commits that change `AGENTS.md`, `README.md`, `.agents/skills/dev-doc-harness/SKILL.md`, canonical harness references, harness templates, validation scripts, or current validation artifacts:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
```

## Expected output

The command exits `0` and prints one `PASS <check-id>` line for each current check:

- `paths.required-files`
- `graph.references`
- `graph.owner-headings`
- `graph.template-routes`
- `router.required-routes`
- `router.route-budget`
- `discoverability.safety`
- `phrases.duplicated-policy`
- `phrases.duplicate-blocks`
- `placeholders.current-surfaces`
- `tracking.work-items`
- `scenarios.golden-traversal`

## Graph checks

The graph checks validate that current module, rule, schema, scenario, and metric references have declared owners; that current rule and schema owners are not duplicated; that owner-table heading references resolve in their owner file; and that template policy references satisfy the router route for the matching operation family.

The route-budget check validates that common operation routes stay within the current architecture budget. Routine planning routes should not require more than three canonical modules. Freeze and execution routes may require more when separate freeze, lifecycle, model, or execution-quality ownership is intentionally loaded.

## Tracking checks

The work-item tracking check validates that `docs/work-items/AGENTS.md` is absent, that work-item Markdown is not ignored, and that all current Markdown artifacts under `docs/work-items` are tracked by git.

Historical work-item artifacts are preserved as repository documentation. They are not reusable current-policy owners, and they are excluded from duplicate reusable-policy block enforcement.

## Negative check

To validate dangling-reference detection without leaving a mutation in the repository, add a temporary current-surface reference to an unowned rule ID, run the validation script, confirm that `graph.references` fails, and then remove the temporary reference before committing.
