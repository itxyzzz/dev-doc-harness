# Dev Doc Harness Instructions

## Using Dev Doc Harness

### Harness Purpose

For all development work except very small mechanical edits, use the documentation harness entrypoint and operation router:

`.agents/skills/dev-doc-harness/SKILL.md`

The router points to the canonical modules for work sizing, artifact lifecycle, planning freeze gates, variance, changelog, documentation matrices, quality bars, compatibility, and model/sub-agent notation. Very small mechanical edits may proceed without durable artifacts only when the router's `module:lifecycle` sizing rules allow it, and they must still preserve existing behavior and relevant checks.

### Active sub-agent model policy

These instructions select the `economy-default` policy for work within their scope. A more-specific applicable `AGENTS.md` may replace this selection.

Use the `economy-default` policy from:

`.agents/skills/dev-doc-harness/references/subagent-model-policy.md`

Do not switch to `enterprise-default` unless the operator or a more-specific applicable `AGENTS.md` explicitly selects it.

### Compatibility

If Superpowers is installed and active, use Superpowers for its normal software-development methodology, but apply this harness as the artifact-location and lifecycle contract. These instructions override Superpowers' defaults for work governed by this harness.

Canonical durable planning artifacts still live under `docs/work-items/<work-id>/` and pass the harness freeze gates before implementation. Add `docs/superpowers` documents only when the directory already exists and contains previous documentation packages from before the current work; never create or seed it to satisfy this compatibility condition. When allowed for continuity, every new file must be a minimal pointer stub to the canonical harness work item package rather than a duplicate spec or plan.

For normal substantial small/medium work, draft and freeze the combined small/medium package: both canonical spec and plan files. A spec-only package is allowed only when the operator requested or approved staged planning, with the reason and `plan drafting` as the next activity.

If spec-kit is installed and active, use the repository spec-kit adapter if present, but treat `.agents/skills/dev-doc-harness/SKILL.md` and its routed canonical modules as the source for artifact and documentation rules.

### Execution defaults

After a frozen package receives fresh start authorization, use its planned method without another generic method question: prefer `superpowers:subagent-driven-development`, then `superpowers:executing-plans` while Superpowers is available. Native Codex is the default only when Superpowers is unavailable and an independent reviewer sub-agent can run; otherwise stop and report the blocker. A fresh explicit operator start instruction may select another available method, model/profile, reasoning effort, or Codex-task continuity without an amendment solely for that runtime choice.

## Dev Doc Harness distribution maintenance

### Use only for harness maintenance

This section applies only when the operator explicitly asks to maintain, package, or release the Dev Doc Harness distribution in its source repository. Do not use this section for downstream application, package, or service releases merely because they use a copy of this harness.

### Release branch creation

When the operator asks an agent in chat to create the next release branch, follow the repository-local process in:

`.agents/skills/dev-doc-harness/docs/release-branch-process.md`

That process defines the agent-executed release flow, including the `master` preflight, remote release-branch version derivation, package-local release notes under `.agents/skills/dev-doc-harness/docs/releases/`, the release branch push, and protected post-release PR synchronization with remote verification before later development branches.
