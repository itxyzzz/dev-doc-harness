# Dev Doc Harness Instructions

## Using Dev Doc Harness

For all repository development work except very small mechanical edits, use `.agents/skills/dev-doc-harness/SKILL.md` as the harness entrypoint and operation router. Very small mechanical edits may skip durable artifacts only when the router's `module:lifecycle` sizing rules allow it; they must still preserve existing behavior and relevant checks.

This repository selects the `economy-default` policy from `.agents/skills/dev-doc-harness/references/subagent-model-policy.md`. A more-specific applicable `AGENTS.md` or the operator may replace that selection. Do not switch to `enterprise-default` otherwise.

When Superpowers is installed and active, use it for normal software-development methodology and use the Dev Doc Harness for the artifact-location and lifecycle contract. Canonical durable planning artifacts live under `docs/work-items/<work-id>/` and pass the harness freeze gates before implementation. For substantial small work, draft and freeze the combined small package; for substantial medium work, draft and freeze the combined medium package. Each package contains both the canonical spec and plan.

Add `docs/superpowers` documents only when that directory already exists and contains previous documentation packages from before the current work. Do not create or seed it for compatibility. Any allowed new file must be a minimal pointer stub to the canonical harness work item rather than a duplicate spec or plan.

After a frozen package receives fresh start authorization, follow its planned method and the execution and reviewer routes in the active skill without another generic method question. A fresh explicit operator start instruction may select another available method, model/profile, reasoning effort, or next-stage continuity without an amendment solely for that runtime choice. Record the actual selection, and use the canonical variance route if the instruction also changes scope or another material boundary.

## Dev Doc Harness distribution maintenance

Use this section only when the operator explicitly asks to maintain, package, or release the Dev Doc Harness distribution in its source repository. Do not use it for downstream application, package, or service releases merely because they include the harness.

For a requested release branch, follow `.agents/skills/dev-doc-harness/docs/release-branch-process.md`.
