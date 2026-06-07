# Testing Guide Delta

Work ID: `2026-06-07-release-versioning`
Phase: Phase 03 release hardening

## Validation Command

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
```

Expected result: the command exits `0` and prints these pass markers:

- `PASS paths.required-files`
- `PASS graph.references`
- `PASS graph.owner-headings`
- `PASS graph.template-routes`
- `PASS router.required-routes`
- `PASS router.route-budget`
- `PASS discoverability.safety`
- `PASS phrases.duplicated-policy`
- `PASS phrases.duplicate-blocks`
- `PASS placeholders.current-surfaces`
- `PASS tracking.work-items`
- `PASS scenarios.golden-traversal`
- `PASS release.identity`
- `PASS release.notes`
- `PASS release.changelog-schema`
- `PASS release.package-boundary`
- `PASS release.template-context`
- `PASS release.route`

## Release Checks

Strict changelog schema validation is scoped to current `2026-06-07-release-versioning` entries. Older changelog history is not rewritten or parsed for the `0.3.0` release metadata schema.

Release-note generation remains manual for `0.3.0`. Validation confirms required release-note headings and checks that source changelog entries listed in release notes exist as headings in `CHANGELOG.md`.
