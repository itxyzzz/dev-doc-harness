# Operator Manual Delta — New-Task Handoff Visibility

Work ID: `2026-07-12_new-task-handoff-visibility`
Status: Implemented

## Durable operator-facing changes

1. Describe combined spec-and-plan drafting as the default small/medium planning shape. Treat a small/medium spec-only freeze as an explicit staged exception with a recorded reason and plan drafting as its named next activity.
2. Preserve the large/phased anchor route to later phase-plan drafting and require every freeze result to identify its planning shape, exact frozen package, and documented next activity before continuity routing.
3. For `new task with curated-artifact handoff`, display the copy-ready handoff and proposed model configuration in the conversation. When exact supported task creation is available, ask explicit approval before creating the configured task.
4. When task creation or the recorded model/reasoning configuration is unavailable, report the limitation and keep the same visible copy-ready handoff as the manual fallback without silent substitution.
5. Keep same-task start authorization and justified alternatives separate. An operator may explicitly request current-task continuation, but the new-task route does not recommend it as a competing question.

## Applied surfaces

1. `README.md`.
2. `.agents/skills/dev-doc-harness/docs/operator-note.md`.
