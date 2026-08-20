# Changelog Lifecycle Simplification Test Cases

Work ID: `2026-08-01_changelog-lifecycle-simplification`
Status: Approved
Harness release: `0.8+`

| ID | Covers | Scenario | Expected evidence |
|---|---|---|---|
| TC-001 | VER-001 | Inspect the primary router, lifecycle, freeze, templates, and README after implementation. | Planning-stage sources do not require fragment creation; only implementation and changelog-maintenance router routes name the dedicated changelog reference. |
| TC-002 | VER-002 | Lint a compact fragment whose meta line contains tagged `unreleased` and `distributable` values. | Lint succeeds and extracts both tagged values. |
| TC-003 | VER-002 | Lint malformed compact metadata, a missing tag, and a current `planning-only` value. | Each invalid input fails with a precise grammar or value error. |
| TC-004 | VER-003 | Run the root migration then inspect `CHANGELOG.md`. | No plan-only entry or legacy metadata key remains; non-planning entries retain heading and body order. |
| TC-005 | VER-003 | Compare release notes and pre-0.8 fragments with the baseline commit. | No paths in the frozen set changed. |
| TC-006 | VER-004 | Lint a frozen legacy fragment. | Lint succeeds without rewriting the fragment. |
| TC-007 | VER-004 | Consolidate a compact eligible fragment into a fixture root, then run consolidation again. | First run inserts exactly one entry; second run reports no missing entries and does not change the file. |
| TC-008 | VER-004 | Supply duplicate headings in two fragments. | Lint or consolidation fails and identifies both source paths. |
| TC-009 | VER-005 | Search current release-policy and validator rules for root `TODO.md`. | No active policy or expectation refers to it. |
| TC-010 | VER-001 through VER-005 | Run the complete harness policy validator and fragment lint/check against the repository. | All checks pass; no unrelated files are modified. |
| TC-011 | VER-001 through VER-005 | Give the complete uncommitted implementation diff and validation evidence to an independent Sol High reviewer. | Findings identify a specific defect or report no blocking issue; substantiated findings are resolved and affected checks are rerun before commit. |
