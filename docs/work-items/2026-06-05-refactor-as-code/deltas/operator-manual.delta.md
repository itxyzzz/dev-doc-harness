# Operator Manual Delta: Harness Validation

Work ID: `2026-06-05-refactor-as-code`
Status: Proposed delta

## Operator-facing behavior

Operators can ask an agent to run the harness validation command before a planning freeze, implementation commit, handoff, or plan-only PR checkpoint:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1
```

The command is a lightweight local check for current harness surfaces. It helps catch missing files, broken module or rule anchors, missing template schemas, router drift, safety discoverability gaps, copied policy phrases, unresolved placeholders, and golden traversal drift.

## Review boundaries

A validation failure is a review signal, not permission to rewrite frozen planning artifacts or weaken process safeguards. The agent should inspect the failed check, repair the current canonical owner or route when the approved scope allows it, and use the amendment process for high-impact changes.

The existing plan-only PR and stop-before-implementation flow remains unchanged. Validation can support a freeze gate, but it does not replace explicit operator approval, changelog discipline, or the post-freeze start authorization step.
