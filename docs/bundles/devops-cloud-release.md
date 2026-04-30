# DevOps Cloud Release Bundle Brief

## Problem

Teams need agents to help ship software without taking unsafe production
actions. Deployment, CI, containers, config, rollback, cost, and readiness work
should produce runbooks and review artifacts before any live change.

## Target User

Developers, release owners, DevOps engineers, platform engineers, indie
hackers, and teams preparing apps or services for production.

## Included Skills

- `deployment-plan`: create deployment runbooks, rollout steps, smoke tests,
  and go/no-go criteria.
- `ci-workflow-plan`: design CI jobs, quality gates, permissions, and required
  checks.
- `containerization-plan`: plan container images, runtime config, healthchecks,
  and container security.
- `environment-config-review`: review env vars, config, secrets, feature flags,
  validation, and drift.
- `rollback-plan`: define rollback triggers, recovery steps, validation, and
  communication.
- `cloud-cost-review`: review cloud, hosting, CI, logging, storage, and
  database cost risk.
- `production-readiness-review`: assess readiness, blockers, evidence, and
  release recommendation.
- `release-risk`: assess release risk and rollout/rollback tradeoffs.
- `release-launch-readiness`: support launch, support, and communication
  readiness.
- `skill-threat-model`: support high-risk tool and permission review.
- `concise-technical-writing`: tighten runbooks and release summaries.

## Context Files

- `DEPLOYMENT_RUNBOOK.md`: deployment steps, owners, windows, and smoke tests.
- `CI_POLICY.md`: required checks, branches, permissions, and release gates.
- `ENVIRONMENT_CONFIG.md`: environments, config schema, secrets, and flags.
- `ROLLBACK_PLAN.md`: rollback triggers, data restore, fallback, and contacts.
- `COST_GUARDRAILS.md`: budgets, alerts, quotas, and retention policies.

## MCP Preset Intent

Use documentation research for current host, CI, container, and cloud-provider
facts. Keep cloud, CI, deployment, secret, and production tools read-only unless
the user explicitly approves writes.

## Safety Rules

- Do not deploy, change production config, run migrations, rotate secrets,
  delete resources, push images, or modify live infrastructure automatically.
- Do not invent test results, current spend, provider pricing, traffic levels,
  or production readiness evidence.
- Verify provider-specific commands and pricing from current official docs when
  exact facts matter.
- Escalate changes involving customer data, auth, billing, migrations,
  regulated workloads, high traffic, or broad availability.

## Pilot Metrics

- Operational: time from release candidate to reviewed runbook.
- Quality: reviewer correction rate on deployment and rollback plans.
- Adoption: percent of releases using generated readiness artifacts.
- Economic: avoided release rework and cost surprises identified before launch.

## Acceptance Criteria

- The bundle installs with a dry run.
- Deployment, CI, container, config, rollback, cost, and readiness scenarios
  route to the intended skills.
- Outputs include concrete artifacts: deployment runbook, CI workflow plan,
  container review, config review, rollback plan, cost risk memo, or readiness
  report.
- High-risk production actions remain review-only until explicitly approved.
