# Repository Agent Instructions

## Documentation harness

For all development work except very small mechanical edits, use the repository documentation harness entrypoint and operation router:

`.agents/skills/dev-doc-harness/SKILL.md`

The router points to the canonical modules for work sizing, artifact lifecycle, planning freeze gates, variance, changelog, documentation matrices, quality bars, compatibility, and model/sub-agent notation. Very small mechanical edits may proceed without durable artifacts only when the router's `module:lifecycle` sizing rules allow it, and they must still preserve existing behavior and relevant checks.

## Release branch creation

When the operator asks an agent in chat to create the next release branch, follow the repository-local process in:

`docs/release-branch-process.md`

That process defines the agent-executed release flow, including the `master` preflight, remote release-branch version derivation, package-local release notes under `.agents/skills/dev-doc-harness/docs/releases/`, the release branch push, and the post-release `master` reset.

## Active sub-agent model policy

This section is the single repository-local selection point for the active model policy.
Other current harness docs and templates should refer to the active repository policy
instead of hard-coding this selected policy as their own default.

Use the `economy-default` policy from:

`.agents/skills/dev-doc-harness/references/subagent-model-policy.md`

Do not switch to `enterprise-default` unless the operator explicitly changes this instruction.

## Compatibility

If Superpowers is installed and active, use Superpowers for its normal software-development methodology, but apply this repository harness as the required artifact-location and lifecycle contract.

If spec-kit is installed and active, use the repository spec-kit adapter if present, but treat `.agents/skills/dev-doc-harness/SKILL.md` and its routed canonical modules as the source for artifact and documentation rules.
