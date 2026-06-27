# Architecture Summary Delta: Portable Harness Validator

Work ID: `2026-06-27-portable-harness-validator`
Short ID: `portable-harness-validator`
Status: Proposed
Harness release: `0.3.0`

## Proposed Update

The current harness validator is implemented as `.agents/skills/dev-doc-harness/scripts/test_harness_policy.py` and uses only Python standard-library modules. The validator remains structural, graph-oriented, and high-signal: it checks current harness file presence, policy owner/reference consistency, route budgets, duplicate reusable policy blocks, placeholder cleanup, tracked work-item artifacts, golden traversal evidence, and release package consistency.

The validator boundary is unchanged by the language migration. It is not a semantic parser for plan quality, operator approval, policy interpretation, or implementation correctness.
