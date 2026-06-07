# Operator Manual Delta: Work-Item History And Required Model Route

Work ID: `2026-06-07-followup-hardening`
Status: Final

## Work-item history

Planning, implementation, snapshot, delta, and variance artifacts under `docs/work-items` are tracked repository history for this harness repository. They should be committed with the harness changes that they justify or validate.

Do not use a nested `docs/work-items/AGENTS.md` file to make work-item artifacts local-only. The repository-level harness and canonical references define the lifecycle contract for current work; historical work-item artifacts preserve past decisions and evidence.

## Model and sub-agent strategy

Small, medium, and large durable planning routes now load `module:models` as a required module. This makes model choice, sub-agent policy, context strategy, and fresh authorization explicit for every substantial durable plan, even when the selected strategy is a compact statement such as `enterprise-default; no sub-agents`.

Repository-local policy selection still comes from `AGENTS.md` unless the operator explicitly overrides it for the work item.

## Operator impact

The implementation should reduce implicit policy discovery. Agents should find the required model/sub-agent strategy through the router, validate the graph with the policy script, and preserve historical docs without treating them as mutable current policy.
