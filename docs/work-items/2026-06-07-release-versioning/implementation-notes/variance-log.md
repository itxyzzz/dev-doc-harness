# Variance Log

Work ID: `2026-06-07-release-versioning`

## Entries

### 2026-06-07 - Include release policy in validation surfaces

- Variance class: Local technical
- Original plan reference: `plan-phase-02-release-package-release-versioning.md` Step 14
- What changed: Updated `.agents/skills/dev-doc-harness/scripts/Test-HarnessPolicy.ps1` to include `.agents/skills/dev-doc-harness/references/release-policy.md` in the canonical reference and required-file lists.
- Why it changed: The existing graph validation only scans its fixed current-surface lists. Without the new reference in those lists, `module:release` appeared as a dangling reference even though the owner file existed.
- Impact on scope: No package-boundary, release-identity, compatibility, or adoption behavior changed. This is the smallest validation-surface adjustment needed for the existing graph check to see the new owner.
- Impact on tests: Existing harness validation should pass once the new reference is tracked.
- Impact on documentation: Variance recorded here; no amendment required.
- Risk: Low. The script change broadens the existing owner graph input set and does not add new release-specific checks.
- Approval required: No
- Approval status: Not required
