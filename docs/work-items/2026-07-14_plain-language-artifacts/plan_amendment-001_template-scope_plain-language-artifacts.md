# Plan Amendment 001: Template Scope

Work ID: `2026-07-14_plain-language-artifacts`
Short ID: `plain-language-artifacts`
Status: Approved
Harness release: `0.6+`
Schema: `schema:plan.amendment`
Policy references: `module:lifecycle`, `module:naming`, `module:freeze-gate`, `rule:lifecycle.commit-message-format`, `rule:lifecycle.variance-policy`, `rule:naming.derived-patterns`, `rule:naming.work-item-paths`, `rule:naming.commit-messages`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, `rule:freeze.stop-before-implementation`

## Original plan reference

- Amendment ID: `AMD-001`
- File: `plan_plain-language-artifacts.md`
- Section or task: `TASK-001`, `TASK-003`, `TASK-004`, `CHECK-001`, and `CHECK-003`
- Original instruction: Add a narrow active-path validator, prompt only the shared commitment source block and its two generated specification consumers, then validate and review the resulting diff.

## Discovered issue

The review found that the current template set still contains optional
style-loading cues outside the approved two-consumer set, and the planned
active-path implementation does not inspect those current templates. The
validator also permits, but does not require, the exact canonical
definition-only exception and treats a non-Markdown fixture as a broad
out-of-scope case rather than a narrow documented boundary.

## Proposed change

1. Expand the template-consumer scope to the complete current reusable template
   set. Modify only their source blocks, then use the established assembler to
   regenerate every affected output; do not edit generated templates directly.
2. Update the affected source-block guidance so small/medium planning no
   longer presents artifact-style loading as optional, then regenerate the
   affected templates through the assembler.
3. Expand the active-path validator to the declared current authoring Markdown
   surfaces: root `AGENTS.md`, the harness router and canonical references, all
   template source blocks, and all generated templates. Keep frozen work items,
   legal text, and non-authoring fixtures outside that set.
4. Require exactly one canonical definition-only exception in the style rule and
   test the fixture boundary without treating the entire validator source as an
   exception.
5. Re-run the full validator, assembly freshness check, modal-scope scan,
   whitespace check, read-only review, and staged work-item tracking check.

## Reason this change is necessary

The existing frozen plan limits generated-template work to two specification
outputs. The review shows that completing the intended policy across current
authoring guidance requires additional template consumers and a broader active
validation set. Continuing without approval would violate the frozen
template-consumer and validation-scope boundaries.

## Impact assessment

| Area | Impact |
|---|---|
| Scope | Expands current template consumers and declared active authoring Markdown paths. |
| Verification Criteria and Plan Checks | Retains `VER-001` through `VER-003`; strengthens `CHECK-001` and `CHECK-003` with complete-template and exact-exception evidence. |
| API/interface | None. |
| Data model/migration | None. |
| Security/privacy/compliance | None. |
| Tests | Adds focused fixture and active-path coverage. |
| Documentation | Updates affected source blocks, regenerated templates, testing guidance, review evidence, and changelog records. |
| Rollout/operations | None. |

## Approval

- Required: Yes
- Status: Approved
- Approval evidence: Operator approval in the current Codex task on 2026-07-14.
- Superseded by: None

## Planned commits

| Stage | Planned subject | Changelog title or snippet | Notes |
|---|---|---|---|
| Amendment approval | `amendment 001: plain-language-artifacts -- expand template and validation scope` | `2026-07-14_plain-language-artifacts -- approve template and validation scope` | Approval commit for this amendment. |
| Amended implementation | `docs: plain-language-artifacts -- require ordinary modal wording` | `2026-07-14_plain-language-artifacts -- require ordinary modal wording` | Supersedes the blocked implementation checkpoint after amendment approval. |

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`. Implementation remains paused until this approved amendment is committed and a fresh operator instruction authorizes the amended work.
