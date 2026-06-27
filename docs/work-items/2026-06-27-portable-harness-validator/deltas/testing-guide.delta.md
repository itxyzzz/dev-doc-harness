# Testing Guide Delta: Portable Harness Validator

Work ID: `2026-06-27-portable-harness-validator`
Short ID: `portable-harness-validator`
Status: Proposed
Harness release: `0.3.0`

## Proposed Update

For harness maintenance work, validate current harness surfaces with:

```bash
python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py
```

Expected successful output:

```text
PASS paths.required-files
PASS graph.references
PASS graph.owner-headings
PASS graph.template-routes
PASS router.required-routes
PASS router.route-budget
PASS release.route
PASS discoverability.safety
PASS phrases.duplicated-policy
PASS phrases.duplicate-blocks
PASS placeholders.current-surfaces
PASS tracking.work-items
PASS scenarios.golden-traversal
PASS release.identity
PASS release.notes
PASS release.changelog-schema
PASS release.package-boundary
PASS release.template-context
```

The validator is a lightweight structural check. It supports review of current harness surfaces, golden traversal evidence, and release package consistency; it does not replace operator approval, plan review, or engineering judgment.
