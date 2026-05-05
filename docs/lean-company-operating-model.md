# Lean Company Operating Model

This note maps the first-five-hires research into AgentSkills portfolio
decisions. The point is to strengthen role leverage without turning every job
title into a separate bundle.

## Product Thesis

AgentSkills should help a lean company operate with five high-leverage humans:
revenue, operations, product/business delivery, systems automation, and customer
success. The system should make each hire faster at artifact-heavy work while
keeping relationship-building, prioritization, judgment, and approval with the
human operator.

## Five-Hire Coverage Map

| Hire | Current coverage | Gap found | Decision |
|---|---|---|---|
| Revenue Operator / Sales Lead | `revenue-growth`, `sales-marketing`, ABM, positioning, prospecting, conversion, lifecycle, paid, pricing, attribution | `sales-pipeline-management` existed but was missing from `revenue-growth`, leaving qualification and forecast hygiene underweighted | Add pipeline management to `revenue-growth` and add a pipeline review scenario |
| Operations Manager / Chief of Staff | `owner-operator-os`, `operating-cadence`, `executive-command-center`, analytics/finance | Follow-through exists through `action-tracker`, but owner bundle docs did not call it out clearly | Sync owner docs/routing around action tracking; keep `ops-pmo` as compose-first backlog |
| Product / Business Analyst / Delivery Lead | `product-research`, `business-analysis`, acceptance criteria, analytics, decision memos | Handoff from business requirements to implementation is a cross-bundle workflow, not a standalone skill yet | Compose from business-analysis, product-research, engineering-delivery, and QA before adding a new skill |
| Technical Builder / Systems Automation Lead | `frontend-product`, `backend-api`, `engineering-delivery`, `devops-cloud-release`, `quality-testing`, `data-analytics-bi` | No role-level bundle for internal tools, forms, dashboards, integrations, and workflow automation in non-software companies | Treat `systems-automation` as a compose-first candidate; add scenarios before a manifest |
| Customer Success / Account Manager | `support-success`, support triage, replies, escalation, KB, customer evidence, support metrics | Bundle was too reactive for account health, adoption, renewal risk, QBRs, and success plans | Add `customer-health-review`, include `retention-analysis`, and add an account-health scenario |

## Strengthening Changes

- `revenue-growth` now includes `sales-pipeline-management` for stage design,
  qualification, CRM hygiene, deal reviews, and forecast cadence.
- `support-success` now includes `customer-health-review` and
  `retention-analysis` for account health, renewal risk, adoption, and QBR
  preparation.
- `owner-operator-os` docs now call out `action-tracker` explicitly for owner
  follow-through.
- New route scenarios cover pipeline review and customer health review.

## Compose-First Candidates

### `systems-automation`

Default decision: compose first.

Use existing skills before creating a new bundle:

- `product-brainstorming-planning`
- `business-requirements-document`
- `write-spec`
- `dashboard-design`
- `product-analytics-instrumentation`
- `api-contract-design`
- `database-schema-review`
- `auth-flow-design`
- `qa-test-strategy`
- `deployment-plan`
- `release-launch-readiness`

Route scenarios to add before a manifest:

- internal tool request to scoped build brief
- spreadsheet or form workflow to dashboard and automation plan
- integration request to API contract, auth, data, and release checklist

Context templates likely needed:

- `SYSTEMS_INVENTORY.md`
- `AUTOMATION_BACKLOG.md`
- `INTEGRATION_RULES.md`
- `DATA_ACCESS_RULES.md`

### Product / Business Delivery Handoff

Default decision: compose first.

The recurring artifact should be an implementation handoff packet, not a new
role bundle yet. It should combine business requirements, acceptance criteria,
implementation plan, QA coverage, risks, and owner approvals.

Route scenario to add before a new skill:

- stakeholder notes and BRD to engineering/operations handoff packet

## Acceptance Criteria

- Revenue operator scenarios route to pipeline, ABM, research, outreach,
  conversion, analytics, and writing skills as appropriate.
- Customer success scenarios route to account health, retention, customer
  evidence, analytics, support, and writing skills.
- Operations scenarios keep decisions, risks, metrics, and actions separate.
- Product/business delivery scenarios separate business requirements from
  solution design and include implementation handoff gates.
- Systems automation work stays review-first for customer data, auth, billing,
  production, and operational writes.

## Validation Plan

- Keep new role insights in docs until at least one route scenario proves a
  concrete gap.
- Add an atomic skill only when an existing skill cannot own the trigger and
  artifact cleanly.
- Add a bundle only after at least three existing skills need to work together
  for a recurring role-specific job.
- Run skill, skillset, scenario, and release validators after each expansion.
