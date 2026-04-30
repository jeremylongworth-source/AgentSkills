# Engineering Delivery Bundle Brief

## Problem

Engineering teams need agents to turn issues into scoped plans, review code
changes, define regression coverage, and assess release risk without taking
production actions automatically.

## Target User

Software engineers, engineering managers, QA leads, release owners, and small
teams using coding agents for delivery work.

## Included Skills

- `issue-to-plan`: convert issues, bugs, and requests into implementation
  plans.
- `pr-review`: review code changes for correctness, risk, and missing tests.
- `regression-check`: define verification coverage for changed behavior.
- `release-risk`: assess release readiness, rollout, rollback, and monitoring.
- `qa-test-strategy`: broaden risk-based test strategy.
- `release-launch-readiness`: cover launch operations and support readiness.
- `product-brainstorming-planning`: clarify broad or ambiguous requirements.
- `concise-technical-writing`: tighten plans, reviews, and release notes.

## Context Files

- `ENGINEERING_WORKFLOW.md`: branch, review, ownership, and delivery rules.
- `TESTING_STANDARDS.md`: required test layers, fixtures, environments, and
  gates.
- `RELEASE_POLICY.md`: deployment, approval, rollback, monitoring, and incident
  expectations.
- `ARCHITECTURE_NOTES.md`: module boundaries, service ownership, invariants, and
  dependencies.

## MCP Preset Intent

Use documentation research for framework, API, and platform behavior. Keep
repository, CI, deployment, and production tools read-first unless the user
explicitly approves a write action.

## Safety Rules

- Never merge, deploy, release, close issues, or approve production changes
  automatically.
- Do not claim tests passed unless output or evidence is available.
- Escalate changes involving auth, billing, customer data, security, migrations,
  broad availability, or production operations.
- Prefer small scoped plans over broad rewrites unless evidence justifies a
  larger change.

## Pilot Metrics

- Operational: issue-to-plan time and PR review turnaround.
- Quality: escaped defect rate, reopen rate, and reviewer correction rate.
- Adoption: accepted-plan rate and retained-test rate.
- Economic: cycle-time reduction and reduced release follow-up work.

## Acceptance Criteria

- The bundle installs with a dry run.
- Issue planning, PR review, regression, and release-risk scenarios route to the
  intended skills.
- Plans include acceptance criteria, test coverage, and open questions.
- Reviews put findings before summaries and call out missing validation.
- Release risk outputs include gates, rollout, rollback, monitoring, and owner
  approval needs.
