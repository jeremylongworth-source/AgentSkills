# AgentOps Evaluation Bundle Brief

## Problem

Skill libraries need proof that skills improve outputs, avoid regressions, and
justify their context overhead. Without evaluation, a growing skill library can
become a list of plausible instructions instead of a trusted workflow system.

## Target User

Skill authors, AI engineers, repo maintainers, team leads, and reviewers who
create, install, validate, or publish agent skills.

## Included Skills

- `skill-benchmark-design`: define benchmark scenarios, evidence, and decision
  rules.
- `scenario-test-authoring`: create route scenarios and expected skill routing.
- `before-after-evaluation`: compare baseline and skill-enabled outputs.
- `acceptance-criteria-mapper`: turn broad goals into observable pass/fail
  checks.
- `prompt-regression-testing`: define reusable prompt regression coverage.
- `skill-output-scoring`: apply rubric scoring with evidence and blockers.
- `skill-token-overhead-review`: review context, tool, and process overhead.
- `skill-evaluation-iteration`: improve skills after scenario evidence.
- `concise-technical-writing`: tighten evaluation reports and recommendations.

## Context Files

- `docs/evaluation/evaluation-method.md`: evaluation loop and promotion stages.
- `docs/evaluation/scenario-test-template.md`: route scenario format.
- `docs/evaluation/before-after-report-template.md`: comparison report format.
- `docs/evaluation/skill-quality-rubric.md`: scoring criteria and blockers.
- `docs/evaluation/security-review-template.md`: safety review template.

## MCP Preset Intent

Use documentation research for external benchmark or platform references when
needed. Keep evaluation runnable from local files and review notes without
requiring any single observability, tracing, or LLM-judge vendor.

## Safety Rules

- Do not publish private prompts, customer data, secrets, or sensitive outputs.
- Do not leak expected answers into benchmark prompts.
- Do not promote a skill when safety, correctness, or maintainability regresses
  even if the output looks more polished.
- Do not remove safety, approval, or validation instructions only to reduce
  context overhead.
- Require human review for high-risk legal, financial, security, employment,
  medical, production, or customer-impacting evaluations.

## Pilot Metrics

- Operational: time from skill proposal to evaluation plan.
- Quality: reviewer agreement with score and recommendation.
- Adoption: percent of new bundles with before/after reports.
- Economic: reduction in repeated skill revision cycles.

## Acceptance Criteria

- The bundle installs with a dry run.
- Benchmark, scenario authoring, before/after, regression, and overhead review
  scenarios route to the intended skills.
- Evaluation outputs include acceptance criteria, evidence capture, scoring,
  safety notes, and a keep/revise/split/merge/defer/retire decision.
- No workflow requires a vendor-specific evaluation platform.
