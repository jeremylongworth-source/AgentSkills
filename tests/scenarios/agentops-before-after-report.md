# Scenario: AgentOps Before/After Report

Prompt:

> Compare these baseline and skill-enabled outputs for a proposed decision-memo
> skill. Score the outputs, call out regressions or unsafe assumptions, note any
> extra context overhead, and recommend whether to keep, revise, split, merge,
> defer, or retire the skill.

Expected routing:

- before-after-evaluation
- skill-output-scoring
- skill-token-overhead-review
- concise-technical-writing

Future bundle:

- agentops-evaluation
