# GPT-5.6 Model Taxonomy Evidence Snapshot

- Work ID: `2026-07-11_model-selection-dimensions`
- Captured: `2026-07-11`
- Evidence type: external-source verification summary
- Snapshot policy: verified claims are preserved here; live pages remain the authoritative provider sources and may change.

## Verification summary

Official OpenAI material available during planning supports treating generation, capability tier, reasoning effort, and multi-agent orchestration as distinct dimensions. Additional official material supports treating model transitions and context compaction as execution-continuity concerns. The harness design extrapolates a vendor-neutral policy schema and fresh-task handoff policy from those verified provider facts; the vendor-neutral names, authorization rules, and thread-start protocol are repository decisions, not OpenAI terminology.

## Verified claims

1. GPT-5.6 is a model generation containing Sol, Terra, and Luna tiers.
2. OpenAI describes Sol as the flagship tier, Terra as a balanced/lower-cost tier, and Luna as the fastest/most affordable tier.
3. OpenAI states that the generation number and the Sol/Terra/Luna capability tiers are distinct and that the tiers can advance on their own cadence.
4. Supported GPT-5.6 products allow reasoning effort to be selected independently of Sol/Terra/Luna, including a `max` effort option where available.
5. OpenAI describes `ultra` as a highest-capability setting that coordinates multiple agents, which makes it an orchestration mode rather than merely another reasoning-effort label.
6. Availability varies by product and plan, so a harness plan cannot assume that every selected combination is exposed in every runtime.
7. OpenAI notes that model transitions can disrupt response style or workflows even when prior context is retained for continuity.
8. Changing the target model in a Codex conversation changes model-specific prompt instructions and causes a prompt-cache miss, affecting efficiency.
9. Codex automatically compacts a conversation after an internal context threshold by replacing it with a smaller representative input.
10. The official sources reviewed do not establish that an agent can reliably inspect exact remaining active context or predict the effective compaction threshold from inside a task.

## Repository conclusions derived from the evidence

1. Use vendor-neutral capability tiers in permanent harness policy and keep Sol/Terra/Luna as a current mapping example.
2. Record reasoning effort separately from capability tier.
3. Record platform-managed multi-agent execution separately from harness-managed bounded sub-agents.
4. Require an availability/fallback field instead of silently resolving an unavailable profile.
5. Prefer a fresh task with curated planning artifacts when the main model/profile changes.
6. Treat compaction as runtime/operator managed when exact context telemetry is unavailable.
7. Require artifact rehydration for a same-task model switch and keep fresh-task handoff prompts minimal.

## Sources

1. OpenAI, “GPT-5.6: Frontier intelligence that scales with your ambition,” published 2026-07-09: https://openai.com/index/gpt-5-6/
2. OpenAI, “Previewing GPT-5.6 Sol: a next-generation model,” published 2026-06-26: https://openai.com/index/previewing-gpt-5-6-sol/
3. OpenAI Help Center, “GPT-5.6 in ChatGPT,” accessed 2026-07-11: https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt
4. OpenAI, “Unrolling the Codex agent loop,” accessed 2026-07-11: https://openai.com/index/unrolling-the-codex-agent-loop/
5. OpenAI Help Center, “What to expect when models change,” accessed 2026-07-11: https://help.openai.com/en/articles/20001053-what-to-expect-when-models-change

## Limitations

1. This snapshot does not preserve pricing because pricing is mutable and is outside this work item's policy requirements.
2. The official Codex manual helper failed during planning because the response lacked the expected `x-content-sha256` header. A bounded official-domain search did not establish a universal public rule for manual sub-agent authorization.
3. The active session's explicit runtime instruction remains the controlling evidence that manual sub-agent spawning can require a direct user or applicable repository/skill request.
