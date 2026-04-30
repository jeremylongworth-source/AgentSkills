# Data Analytics BI Bundle Brief

## Problem

Teams need agents to turn messy business questions into trustworthy analysis
plans, metric definitions, dashboard specs, SQL outlines, and decision memos.
This is distinct from qualitative research: the central question is what the
data says, how reliable it is, and what decision it can support.

## Target User

Founders, operators, analysts, product managers, growth teams, finance partners,
and engineering teams working with product, customer, revenue, and operational
data.

## Included Skills

- `metric-definition`: define KPIs, formulas, grains, caveats, and owners.
- `dashboard-design`: create decision-oriented dashboard specs.
- `cohort-analysis`: plan or interpret cohort comparisons.
- `funnel-analysis`: define funnel steps, conversion, drop-off, and
  instrumentation gaps.
- `retention-analysis`: define retention, churn, renewal, and engagement
  analysis.
- `sql-analysis-plan`: outline read-only SQL analyses and validation checks.
- `experiment-readout`: summarize tests, guardrails, decisions, and learnings.
- `analytics-instrumentation-plan`: define event taxonomy, identity, privacy,
  and QA.
- `metric-narrative`: turn metric movement into reviewed decision narratives.
- `product-analytics-instrumentation`: support product telemetry and event
  taxonomy.
- `marketing-analytics-attribution`: support marketing and acquisition
  measurement.
- `experiment-design-validation`: support experiment design and decision rules.
- `concise-technical-writing`: tighten analysis memos and dashboard specs.

## Context Files

- `METRIC_DEFINITIONS.md`: formulas, grains, source-of-truth rules, and owners.
- `DATA_CATALOG.md`: tables, fields, event names, and data quality notes.
- `DASHBOARD_GUIDELINES.md`: chart, filter, refresh, and publication standards.
- `EXPERIMENT_LOG.md`: hypotheses, metrics, guardrails, and decisions.
- `TRACKING_PLAN.md`: events, properties, identity model, privacy rules, and QA.

## MCP Preset Intent

Use documentation research for analytics platform or warehouse behavior when
needed. Keep database, warehouse, analytics, and BI tools read-only unless the
user explicitly approves a write action.

## Safety Rules

- Do not invent data, formulas, baselines, table names, event names, or causal
  explanations.
- Do not run write queries, alter tracking, publish external figures, or change
  dashboards without approval.
- Escalate finance, investor, compensation, compliance, regulated, or customer
  commitment reporting.
- Separate observed facts, assumptions, caveats, confidence, and
  recommendations.

## Pilot Metrics

- Operational: time from business question to analysis plan.
- Quality: reviewer correction rate on definitions, SQL logic, and caveats.
- Adoption: percent of analysis plans used by analysts or operators.
- Economic: reduced ad hoc analysis rework and decision delay.

## Acceptance Criteria

- The bundle installs with a dry run.
- Metric definition, dashboard, cohort/funnel/retention, SQL, experiment, and
  instrumentation scenarios route to the intended skills.
- Outputs include concrete artifacts: metrics dictionary entry, dashboard spec,
  analysis plan, SQL outline, experiment readout, or tracking plan.
- High-risk reporting remains read-only and reviewed before publication.
