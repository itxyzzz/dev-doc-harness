# Portable Harness Validator Variance Log

Work ID: `2026-06-27-portable-harness-validator`
Short ID: `portable-harness-validator`
Status: Current
Harness release: `0.3.0`
Policy references: `module:lifecycle`, `rule:lifecycle.variance-policy`

## Variance Entries

### 2026-06-27: Enterprise-default execution policy

- Class: Local technical
- Planned behavior: The approved plan recorded the active repository `economy-default` policy before implementation authorization.
- Actual behavior: The operator explicitly selected `enterprise-default` before authorizing implementation.
- Rationale: Operator instruction after the freeze gate overrides the earlier default policy note and increases review conservatism for the validator migration.
- Impact: No artifact, interface, or acceptance-criteria change.

### 2026-06-27: Pass-line count wording

- Class: Mechanical documentation correction
- Planned behavior: Some plan text says the current pass contract has 17 `PASS` lines.
- Actual behavior: The approved spec and snapshot enumerate 18 concrete `PASS` lines, and both the PowerShell oracle and Python validator emit those 18 lines.
- Rationale: Implementation follows the enumerated check IDs and observed validator output rather than the mistaken count word.
- Impact: No validator behavior change.
