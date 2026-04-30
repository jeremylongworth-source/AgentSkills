# Quality Testing Bundle Brief

## Problem

Testing work often gets scattered across implementation, release, and support
workflows. Teams need a focused bundle that turns risk into concrete test
artifacts: unit cases, integration plans, E2E flows, bug reproductions, QA
matrices, accessibility checks, performance tests, and release gates.

## Target User

Developers, QA leads, test engineers, release owners, product engineers, and
teams using agents to improve confidence before merge or release.

## Included Skills

- `unit-test-generation`: create focused unit cases and regression guards.
- `integration-test-plan`: plan cross-module, API, database, service, and
  dependency tests.
- `e2e-test-plan`: plan end-to-end smoke and regression flows.
- `bug-reproduction`: convert bug reports into minimal reproduction and
  diagnostic plans.
- `qa-matrix`: organize risk-based coverage across roles, platforms, and
  scenarios.
- `accessibility-test-plan`: define keyboard, screen reader, contrast, motion,
  form, and WCAG-oriented checks.
- `performance-test-plan`: define latency, load, throughput, Core Web Vitals,
  and regression gates.
- `qa-test-strategy`: broaden test strategy across a product or release.
- `regression-check`: define targeted regression coverage.
- `backend-test-plan`: cover backend services, APIs, migrations, auth, and jobs.
- `accessibility-inclusive-design`: support accessibility-specific review.
- `release-launch-readiness`: connect test gates to release readiness.
- `concise-technical-writing`: tighten QA reports and release recommendations.

## Context Files

- `TESTING_STANDARDS.md`: required test layers, naming, fixtures, and CI gates.
- `SUPPORTED_PLATFORMS.md`: browsers, devices, OS versions, and accessibility
  targets.
- `RELEASE_POLICY.md`: release gates, approvers, and risk tolerance.
- `BUG_REPORT_TEMPLATE.md`: required reproduction fields.
- `PERFORMANCE_BUDGETS.md`: latency, throughput, and frontend performance
  thresholds.

## MCP Preset Intent

Use browser QA tools for local browser validation when available. Use
documentation research for current framework, accessibility, browser, and test
tool facts. Keep production systems and customer data out of tests unless the
user explicitly approves a safe path.

## Safety Rules

- Do not claim tests passed without command output or reviewer evidence.
- Do not use production data, customer credentials, real payment methods, or
  destructive test actions.
- Do not run load tests against production without explicit approval.
- Do not claim accessibility compliance from automated checks alone.
- Escalate uncovered high-risk rows before release.

## Pilot Metrics

- Operational: time from change summary to reviewed test plan.
- Quality: escaped defect rate, reopened bug rate, and reviewer correction rate.
- Adoption: percent of generated tests retained or plans accepted.
- Economic: reduced release delay from clearer test gates.

## Acceptance Criteria

- The bundle installs with a dry run.
- Unit, integration, E2E, bug reproduction, QA matrix, accessibility, and
  performance scenarios route to the intended skills.
- Outputs include concrete artifacts: test case list, integration plan, E2E
  flow, reproduction steps, QA matrix, accessibility plan, or performance test
  plan.
- High-risk testing uses safe environments and explicit approval gates.
