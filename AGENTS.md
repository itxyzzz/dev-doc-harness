# Repository Agent Instructions

## Documentation harness

For substantial development work, use the repository documentation harness:

`.agents/skills/dev-doc-harness/SKILL.md`

Substantial work includes new features, medium or large refactors, API or interface changes, persistence or schema changes, security-sensitive work, multi-step implementation, and work where tests, operator notes, API docs, or architecture notes may need to be created or updated.

Small mechanical edits may proceed without invoking the harness, but must still preserve existing behavior and tests.

## Active sub-agent model policy

Use the `economy-default` policy from:

`.agents/skills/dev-doc-harness/references/subagent-model-policy.md`

Do not switch to `enterprise-default` unless the operator explicitly changes this instruction.

## Compatibility

If Superpowers is installed and active, use Superpowers for its normal software-development methodology, but apply this repository harness as the required artifact-location and documentation contract.

If spec-kit is installed and active, use the repository spec-kit adapter if present, but treat `.agents/skills/dev-doc-harness/SKILL.md` as the canonical source for artifact and documentation rules.
