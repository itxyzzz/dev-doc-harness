## Source and Intent

Source input:

1. Summarize the operator request, issue, review comment, incident, prior artifact, or external source that started this work.

Desired operator/user outcome:

1. Name the result the operator, user, maintainer, or reviewer should see after the work.

Success summary:

1. State the smallest useful outcome in one or two sentences.
2. While drafting, use value and scope tradeoffs to split, defer, re-scope, or phase candidate requirements before approval.

## Scope Boundary

### In scope

1. List the behavior, files, interfaces, workflows, docs, validation surfaces, or decisions covered by this work item.
2. Keep the boundary clear enough that later implementation can preserve scope without hidden chat context.

### Non-scope

1. List nearby work intentionally excluded, deferred, or left unchanged.
2. Name tempting follow-ups that would make this package too broad.

### Assumptions

1. Record assumptions that are safe to rely on during planning.
2. Use `None identified after repository-context review` only after checking the relevant local context.

### Open questions

1. Record unresolved decisions, missing operator input, or repo facts that need confirmation.
2. For each question, name the owner or later event needed to resolve it.
3. Use `None identified after repository-context review` only when there are no known open questions.

## Repository Context

### Current state

1. Summarize the relevant repository behavior, architecture, documentation, tests, operational behavior, or process before implementation.

### Evidence read

1. List only repository files, docs, tests, prior artifacts, logs, review comments, or external references actually inspected while drafting.

### Constraints and compatibility

1. Record compatibility, lifecycle, naming, release, testing, operator-workflow, platform, security, privacy, migration, or context-window constraints that shape the work.
