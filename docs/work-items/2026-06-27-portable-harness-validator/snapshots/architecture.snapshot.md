# Portable Harness Validator Architecture Snapshot

Work ID: `2026-06-27-portable-harness-validator`
Short ID: `portable-harness-validator`
Status: Approved
Harness release: `0.3.0`
Policy references: `module:architecture`, `module:lifecycle`, `module:quality`

## Decision

The harness validator will move from a PowerShell implementation to a Python standard-library implementation. Python becomes the only supported active validator command after implementation; the PowerShell script is retained only long enough to prove parity during the migration and is deleted before completion.

## Validator boundary

The validator remains a lightweight structural check for current harness surfaces. It protects file presence, policy graph ownership, route consistency, duplicate reusable policy blocks, placeholder cleanup, tracked work-item documentation, golden traversal evidence, and release package consistency.

The validator must not become a semantic parser for plan quality, operator judgment, approval state, or policy interpretation. Those responsibilities remain in routed references, approved work-item artifacts, review, and operator approval.

## Portability constraints

- Use Python standard-library modules only.
- Derive the repository root from `Path(__file__).resolve().parents[4]`, matching the current script location under `.agents/skills/dev-doc-harness/scripts/`.
- Normalize repository-relative paths to forward slashes for stable diagnostics.
- Preserve current check IDs and output style.
- Avoid network access, generated files, package installs, and external runtime dependencies.

## Migration sequence

1. Add the Python validator while the PowerShell validator still exists.
2. Run both validators on unchanged current surfaces and compare check IDs and output order.
3. Update current harness guidance to Python.
4. Update validator self-references to require the Python script.
5. Delete the PowerShell script.
6. Run the Python validator as the final canonical validation command.

## Current-surface policy

Current reusable harness surfaces must use the Python command after implementation. Frozen historical work-item artifacts may keep PowerShell examples because they preserve old review evidence and are not current reusable-policy owners.

## Rejected alternatives

- Permanent PowerShell wrapper: rejected because it keeps the non-portable command in the active surface.
- Direct deletion before parity: rejected because it removes the current behavior oracle too early.
- Third-party Python test framework or parser dependency: rejected because the harness package should remain copyable without dependency installation.
