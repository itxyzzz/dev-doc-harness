# Repository Agent Instructions

## Documentation harness

For all development work except very small mechanical edits, use the repository documentation harness:

`.agents/skills/dev-doc-harness/SKILL.md`

Very small mechanical edits may proceed without invoking the harness, but must still preserve existing behavior and tests.

## Active sub-agent model policy

Use the `economy-default` policy from:

`.agents/skills/dev-doc-harness/references/subagent-model-policy.md`

Do not switch to `enterprise-default` unless the operator explicitly changes this instruction.

## Compatibility

If Superpowers is installed and active, use Superpowers for its normal software-development methodology, but apply this repository harness as the required artifact-location and documentation contract.

If spec-kit is installed and active, use the repository spec-kit adapter if present, but treat `.agents/skills/dev-doc-harness/SKILL.md` as the canonical source for artifact and documentation rules.
