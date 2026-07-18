# Operator Manual Delta: Superpowers Adapter Contract

Work ID: `2026-07-18_superpowers-adapter-contract`
Short ID: `superpowers-adapter-contract`
Status: Proposed
Harness release: `0.7+`

## Proposed Update

For harness-managed work, project-level or merged global `AGENTS.md` guidance
overrides Superpowers' default spec and plan locations. Durable specs, plans,
snapshots, handoffs, and changelog sources belong in
`docs/work-items/<work-id>/` and the harness freeze route remains the only
durable approval boundary.

After the package freezes and a fresh instruction authorizes execution,
Superpowers may use the conditional execution meta-header, pre-flight, and
task-specific aids inside the recorded strategy. Those aids are ephemeral; they
do not become a second planning package or approval route. Every Superpowers
dispatch records its policy-relative allocation instead of silently inheriting
an unknown session allocation. When Superpowers is unavailable, agents keep
each task independently executable and verifiable with its recorded checks.
