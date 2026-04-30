# Real-Input Packet: AGENTOPS-001

Bundle: `agentops-evaluation`
Scenario: Evaluate the creator AI production bundle after the prompt-brief
rename and routing refinement.
Reviewer: AgentSkills maintainer
Date collected: 2026-04-30
Public-safe: yes
Storage: committed

## Source Context

The repo added `creator-ai-production` as an alpha bundle and then tightened the
new production skill from a broad production brief into `ai-media-prompt-brief`.
The validation task is to check whether the AgentOps bundle can compare the
before/after behavior, name the decision, and identify any remaining evidence
needed before promotion.

## User Prompt

> Evaluate the `creator-ai-production` alpha bundle after the provider-neutral
> prompt-brief rename. Compare the original broad production-brief shape to the
> current `ai-media-prompt-brief` plus `synthetic-character-bible` shape. Use
> the scenario files and bundle brief to produce a before/after evaluation,
> score the change with the skill quality rubric, and recommend keep, revise,
> split, merge, defer, or retire.

## Source Material

- `docs/bundles/creator-ai-production.md`
- `skillsets/creator-ai-production.yaml`
- `skills/ai-media-prompt-brief/SKILL.md`
- `skills/synthetic-character-bible/SKILL.md`
- `tests/scenarios/creator-ai-content-workflow.md`
- `tests/scenarios/creator-ai-image-prompt-pack.md`
- `tests/scenarios/creator-ai-video-prompt-brief.md`
- `tests/scenarios/creator-ai-audio-voiceover-plan.md`
- `tests/scenarios/creator-synthetic-character-bible.md`
- `tests/scenarios/creator-ai-batch-production-plan.md`
- `docs/evaluation/reports/creator-ai-production-forward-test.md`

## Expected Artifact

- Before/after evaluation report
- Skill quality score table
- Promotion decision and required follow-up evidence

## Acceptance Criteria

- Compares broad production planning against provider-neutral media prompt
  briefs without inventing private inputs.
- Scores trigger fit, artifact usefulness, safety boundaries, vendor
  neutrality, and maintainability.
- Identifies that real source-asset, rights, platform, sponsor, and reviewer
  packets are still needed before promotion.

## High-Risk Boundaries

- Do not claim the AI production bundle proves legal, platform, copyright,
  likeness, voice, disclosure, or commercial-use readiness.
- Do not run generation tools or publish assets.
- Do not treat scenario-only evidence as beta or release-level proof.

## Baseline Setup

Skillset disabled or closest prior bundle: current repo context without
`agentops-evaluation`
Notes: baseline may produce a qualitative summary but may miss scoring,
overhead, and promotion decision structure.

## Skill-Enabled Setup

Skillset: `agentops-evaluation`
Relevant skills expected:

- `before-after-evaluation`
- `skill-output-scoring`
- `acceptance-criteria-mapper`
- `skill-token-overhead-review`
- `concise-technical-writing`

Notes: use existing docs and scenario files only.

## Reviewer Notes

What would make the output usable?

- Clear keep/revise/defer decision
- Specific evidence gaps before promotion
- No overclaiming from scenario-only validation

What common mistakes should be caught?

- Treating the rename as only cosmetic
- Ignoring provider neutrality and rights/disclosure boundaries
- Counting synthetic or scenario evidence as real-input validation

What would block release promotion?

- Claims that prompt packs are safe for publication without rights, platform,
  disclosure, and human review evidence
