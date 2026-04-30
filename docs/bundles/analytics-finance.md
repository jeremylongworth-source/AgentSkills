# Analytics Finance Bundle Brief

## Problem

Analytics and finance teams need agents to explain metrics, draft variance
commentary, and prepare close/reporting checklists without inventing numbers,
changing systems, or publishing figures without review.

## Target User

Analysts, founders, finance operators, growth analysts, product analysts,
marketing analysts, and operators preparing reviewed reporting.

## Included Skills

- `metric-narrative`: write KPI and dashboard narratives from supplied data.
- `variance-commentary`: explain actuals versus target, forecast, prior period,
  or cohort changes.
- `finance-close-checklist`: prepare finance close and reporting checklists.
- `product-analytics-instrumentation`: define product metrics and data quality
  checks.
- `marketing-analytics-attribution`: define funnel, attribution, and campaign
  measurement.
- `experiment-design-validation`: interpret experiments and decision rules.
- `pricing-packaging-strategy`: support monetization and pricing metric
  interpretation.
- `concise-technical-writing`: tighten reporting notes and summaries.

## Context Files

- `METRIC_DEFINITIONS.md`: approved metric names, formulas, sources, filters,
  and owners.
- `DATA_QUALITY_RULES.md`: freshness, completeness, validation, and confidence
  rules.
- `FINANCE_CLOSE.md`: close calendar, workstreams, reconciliations, and
  approvals.
- `REPORTING_GLOSSARY.md`: approved reporting terms and audience-specific
  language.

## MCP Preset Intent

Use documentation research for public docs and platform behavior. Keep
warehouses, BI tools, finance systems, spreadsheets, billing systems, and CRM
systems read-only unless a finance or data owner approves a write action.

## Safety Rules

- Never invent numbers, definitions, sources, baselines, or drivers.
- Never publish figures, approve close, change dashboards, or write to finance
  systems automatically.
- Do not provide accounting, tax, legal, audit, or investment advice.
- Require reviewer confirmation for external, board, investor, compensation,
  compliance, or customer-facing reporting.

## Pilot Metrics

- Operational: time-to-answer for ad hoc metric questions.
- Quality: reviewer edit rate and data-quality correction rate.
- Adoption: reviewer confidence rating.
- Economic: analyst or finance-operator hours saved.

## Acceptance Criteria

- The bundle installs with a dry run.
- KPI narrative and close checklist scenarios route to the intended skills.
- Outputs separate facts, assumptions, drivers, caveats, and follow-up checks.
- External or finance-sensitive reporting requires human review.
