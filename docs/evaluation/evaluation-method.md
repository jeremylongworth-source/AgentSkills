# Skill Evaluation Method

Use this method before promoting a skill or bundle from draft to alpha, and
again before release. The question is not whether the skill sounds useful. The
question is whether it changes agent behavior in a measurable, reviewable way.

## Why This Exists

Current ecosystem signals support a proof-first approach:

- SWE-Skills-Bench reports that many public software-engineering skills showed
  little or no pass-rate improvement, while a smaller set of specialized skills
  produced meaningful gains.
- Skill security research found common risks across public skill ecosystems,
  including prompt injection, data exfiltration, privilege escalation, and
  supply-chain risks.
- Public skill collections and product-specific repos show that the ecosystem
  is already crowded; AgentSkills should differentiate on curated bundles,
  output contracts, scenario tests, and reviewable safety boundaries.

Sources reviewed on 2026-04-30:

- [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401)
- [Agent Skills in the Wild](https://arxiv.org/abs/2601.10338)
- [AgentSkillOS](https://arxiv.org/abs/2603.02176)
- [Langfuse skill evaluation example](https://langfuse.com/blog/2026-02-26-evaluate-ai-agent-skills)
- [VoltAgent awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- [Supabase agent-skills](https://github.com/supabase/agent-skills)
- [Addy Osmani agent-skills](https://github.com/addyosmani/agent-skills)

## Evaluation Loop

1. Define the target artifact.

   Name the concrete output the skill should improve: memo, checklist,
   runbook, review report, scenario plan, scorecard, risk register, or code
   change.

2. Write realistic scenarios.

   Use prompts that resemble real user work. Do not leak the expected answer
   into the prompt. Include incomplete context when that is realistic, and make
   expected routing explicit.

3. Run a baseline.

   Capture what the agent produces without the new skill or bundle active. If a
   true baseline is impractical, use the closest existing bundle or current
   production behavior.

4. Run the skill-enabled path.

   Use the same prompt, same source material, and same acceptance criteria.
   Record any extra context, scripts, tools, or references the skill required.

5. Score the outputs.

   Use the [skill quality rubric](skill-quality-rubric.md). Compare artifact
   usefulness, correctness, evidence handling, safety, validation, concision,
   context overhead, and reviewer trust.

6. Decide.

   Keep, revise, split, merge, defer, or retire the skill. Do not add more
   instructions unless the evaluation reveals a concrete trigger, workflow,
   output, validation, or safety gap.

7. Publish lightweight proof.

   Summarize the result with the
   [before/after report template](before-after-report-template.md). Link the
   scenario, acceptance criteria, reviewer notes, and any follow-up patch.

## Minimum Proof By Stage

| Stage | Required proof |
|---|---|
| Draft | One realistic scenario and one clear output contract |
| Alpha | Three scenarios, one before/after report, rubric score, safety review |
| Beta | Five or more scenarios across common edge cases, reviewer notes, regression checks |
| Release | Passing repo validation, documented limitations, no unresolved high-risk security findings |

## Evaluation Metrics

Track only metrics that can change a decision:

- task success against acceptance criteria
- reviewer edit burden
- missing-step rate
- unsafe assumption rate
- evidence citation or source-grounding quality
- time to useful draft
- output retained after human review
- tool or token overhead when available

## Decision Rules

- Promote when the skill produces a better artifact with acceptable overhead
  and clear safety boundaries.
- Revise when the trigger, workflow, or output is unclear but the use case is
  still valuable.
- Split when one skill is trying to serve multiple unrelated jobs.
- Merge when the skill is only a minor variant of an existing workflow.
- Retire or defer when the skill adds overhead, stale guidance, or risky
  instructions without measurable benefit.
