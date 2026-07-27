# Testing Guide Delta — Execution Flow Clarity

Work ID: `2026-07-27_harness-execution-flow-clarity`

Validate execution routing with `python .agents/skills/dev-doc-harness/scripts/test_harness_policy.py`. The validator protects the ordered method cascade, mandatory route-specific review, the native no-review stop, fresh method-only and model-only overrides, and the grouped next-stage summary. The summary distinguishes current planning facts from the draft recommendation or frozen approval, validates Method/Run in/Plan Task reviewers and Model/Reasoning, rejects context speculation, and checks the matching draft-review, freeze, and handoff chat projection.
