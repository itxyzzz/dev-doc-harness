# Testing Guide Delta: Harness Validation

Work ID: `2026-06-05-refactor-as-code`
Status: Proposed delta

## Validation command

Run this command from the repository root before commits that change `AGENTS.md`, `.agents/skills/dev-doc-harness/SKILL.md`, canonical harness references, harness templates, README, or validation artifacts:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
```

## Expected output

The command exits `0` and prints one `PASS <check-id>` line for each check:

- `paths.required-files`
- `ids.module-owners`
- `ids.safety-rules`
- `templates.schema-anchors`
- `router.required-routes`
- `discoverability.safety`
- `phrases.duplicated-policy`
- `placeholders.current-surfaces`
- `scenarios.golden-traversal`

## Failure triage

Inspect the reported check ID and failure detail. Fix the current canonical owner, route, template schema anchor, or documentation surface that drifted.

Do not weaken planning freeze gates, variance handling, changelog-before-commit, model/sub-agent authorization, or immutable snapshot behavior merely to satisfy the script. Validation failures are review signals. If a needed repair changes architecture, scope, safety-critical policy, rule-versioning scope, or approved phase feasibility, use the harness amendment process before proceeding.

## Scope

The script checks current harness surfaces and golden traversal evidence. It does not validate every historical work-item artifact, and it must not be used to rewrite frozen artifacts to mimic current policy.
