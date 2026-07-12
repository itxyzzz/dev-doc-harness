## Check execution and completion records

For every Plan Check execution, record the `CHECK` ID, a unique execution instance, stage or environment, actual result, evidence location or inline evidence, and `pass`, `fail`, or `blocker` status. Repeated executions of an unchanged procedure produce distinct records. A material procedure change follows approved variance or amendment rather than silently reusing the ID.

Completion reports cite executed Plan Checks, resulting Verification Criterion status, remaining task or disposition status, variance, and residual risk. Task completion alone does not establish conformance.

## Plan variance handling

Use `rule:lifecycle.variance-policy`. Before freeze, edit this draft directly for operator feedback. After freeze, record nontrivial implementation variance in `implementation-notes/variance-log.md`; use a plan amendment for high-impact architecture, API, data, security, privacy, compliance, scope, Verification Criterion, Plan Check, or feasibility changes.

## Planning artifact freeze gate

Use `module:freeze-gate`, `rule:freeze.draft-review`, `rule:freeze.approval-freeze`, and `rule:freeze.stop-before-implementation`.

Record the draft review, approval commit, and post-freeze implementation authorization status for this plan.
