# Bundle Expansion Map

Use this map when reviewing a new bundle expansion document. The goal is to
decide whether each proposed workflow should become a new bundle, an alias for
an existing bundle, a new atomic skill, or a deferred idea.

For the current baseline decisions, see
[bundle expansion decisions](bundle-expansion-decisions.md).

## Current Canonical Bundles

| Bundle | Role | Current status | Notes |
|---|---|---|---|
| `support-success` | Support and customer success | alpha | Ticket triage, safe replies, escalation, KB |
| `engineering-delivery` | Software engineering delivery | alpha | Issue planning, PR review, regression, release risk |
| `product-research` | Product management and research | alpha | Feedback synthesis, PRDs, validation, analytics |
| `business-analysis` | Business analysis and requirements | alpha | Guided discovery, BRDs, stakeholder requirements, traceability |
| `revenue-growth` | Revenue, GTM, sales, and marketing | alpha | Composed from existing sales/marketing skills |
| `analytics-finance` | Analytics and finance operations | alpha | Read-first narratives, variance, close checklists |
| `executive-command-center` | Executive operating system | alpha | Executive briefs, decisions, risks, and action tracking |
| `founder-fundraising-ir` | Founder fundraising and investor relations | alpha | Investor updates, fundraising narrative, data rooms, diligence |
| `ai-transformation-governance` | AI transformation and governance | alpha | AI use cases, pilots, risks, vendors, adoption, scale |
| `owner-operator-os` | Small business owner operations | alpha | Owner dashboards, cash-flow triage, pricing, vendors, bottlenecks |
| `operating-cadence` | Leadership operating rhythm | composed alpha | Weekly meetings, OKRs, decisions, escalations, MBRs |
| `creator-content-engine` | Creator content operations | alpha | Content pillars, hooks, scripts, calendars, captions, repurposing |
| `creator-brand-deals` | Creator sponsorship operations | alpha | Media kits, pitches, packages, rate cards, rights checks, recaps |
| `creator-analytics-reporting` | Creator analytics operations | alpha | Sponsor reports, content performance, affiliates, dashboards, experiments |
| `creator-monetization` | Creator owned-revenue operations | alpha | Offer ladders, owned-product launches, pricing, affiliates, dashboards |
| `creator-business-ops` | Creator business operations | alpha | Weekly ops, sponsor pipeline, invoice readiness, production handoffs, asset checks |
| `creator-community` | Creator community operations | alpha | Comment/DM triage, moderation briefs, feedback, polls, engagement plans |
| `creator-reputation-risk` | Creator trust and reputation review | alpha | Disclosure, rights, AI-labeling, brand safety, platform-policy, response risk |
| `creator-ai-production` | Creator AI production planning | alpha | AI media prompt briefs, synthetic characters, provenance, disclosure, review gates |
| `game-dev` | Game development | existing | Domain-specific creative/software bundle |
| `html5-game-publishing` | Browser game publishing | existing | Focused game publishing workflow |
| `frontend-product` | Frontend product delivery | existing | Product/frontend/UX implementation quality |
| `research-validation` | Evidence and validation | existing | Broad research and validation utility bundle |
| `sales-marketing` | Sales and marketing | existing | Broad predecessor to `revenue-growth` |
| `llm-skill-authoring` | Skill creation | existing | Skill authoring and evaluation |

## Planned Proof and Engineering Bundles

| Bundle | Role | Default decision | Notes |
|---|---|---|---|
| `agentops-evaluation` | Skill authors and maintainers | created alpha | Scenario tests, before/after reports, rubric scoring, overhead review |
| `skill-security-audit` | Skill authors, reviewers, and teams installing skills | created alpha | Threat model, prompt-injection review, scripts, dependencies, safe install |
| `technical-documentation` | Maintainers, DevRel, and developers | created alpha | README, API docs, changelogs, ADRs, migration and onboarding docs |
| `backend-api` | Backend and full-stack developers | created alpha | API contracts, auth flows, database review, error contracts, backend tests |
| `devops-cloud-release` | Developers and release owners | created alpha | Deployment plan, CI/CD, containerization, env config, rollback, readiness |
| `quality-testing` | Developers and QA leads | created alpha | Unit, integration, E2E, bug reproduction, QA matrix, accessibility and performance tests |
| `data-analytics-bi` | Analysts, founders, operators, product managers | created alpha | Metrics dictionary, dashboards, cohorts, funnels, retention, experiment readouts |
| `customer-success-support` | Support and success teams | alias or merge | Already covered by `support-success`; add renewal/customer health later if scenarios justify split |

## Alias and Overlap Decisions

| Proposed area | Default mapping | Rationale |
|---|---|---|
| Sales enablement, GTM, outbound, campaigns | `revenue-growth` | More precise approval-aware revenue workflow |
| Broad sales and marketing | `sales-marketing` or `revenue-growth` | Keep `sales-marketing` for broad legacy use |
| Product discovery, feedback, PRDs | `product-research` | Product-facing evidence-to-spec workflow |
| BRDs, stakeholder requirements, business scope | `business-analysis` | Business-facing requirements before solution design |
| General customer/market validation | `research-validation` | Broader evidence utility outside product work |
| QA, release, PR review, issue planning | `engineering-delivery` | Delivery workflow rather than standalone QA bundle |
| Support operations and success handoffs | `support-success` | Clear reviewable workflow with safety gates |
| KPI reporting and finance close | `analytics-finance` | Read-first reporting and review workflow |
| Executive decisions, CEO briefs, risk registers | `executive-command-center` | New flagship executive bundle |
| Fundraising and investor relations | `founder-fundraising-ir` | New founder-facing workflow with legal/financial review gates |
| AI use-case portfolio and governance | `ai-transformation-governance` | New strategic bundle tied to agent adoption and governance |
| Skill benchmarking and before/after proof | `agentops-evaluation` | New signature proof bundle |
| Skill install and publish security review | `skill-security-audit` | New signature trust bundle |
| README, API docs, release notes, onboarding | `technical-documentation` | New docs-focused workflow bundle |
| API contracts, database schemas, auth, backend tests | `backend-api` | New engineering bundle distinct from general delivery |
| CI/CD, deployment, rollback, cloud readiness | `devops-cloud-release` | New release and platform bundle |
| Test strategy, QA matrix, bug reproduction | `quality-testing` | New testing bundle |
| Dashboards, funnels, cohorts, metrics, SQL plans | `data-analytics-bi` | New data decision bundle |
| Creator content pillars, hooks, scripts, calendars, captions | `creator-content-engine` | New creator workflow bundle |
| Creator sponsorships, media kits, rate cards, campaign recaps | `creator-brand-deals` | New creator sponsorship workflow after content engine validation |
| Creator performance, sponsor reports, retention analysis | `creator-analytics-reporting` | New composed creator proof and reporting workflow |
| Creator community, comments, DMs, moderation, polls | `creator-community` | New composed creator audience workflow |
| Creator reputation, disclosure, copyright, AI labeling, brand safety | `creator-reputation-risk` | New composed review-only creator trust workflow |
| Creator AI production, synthetic personas, prompt briefs | `creator-ai-production` | New composed provider-neutral AI production planning workflow |
| Creator-owned products, affiliates, merch, courses, memberships | `creator-monetization` | New composed creator owned-revenue workflow |
| Creator sponsor pipeline, invoices, budgets, contractors, assets | `creator-business-ops` | New composed creator operations workflow |

## Backlog Candidates

| Candidate | Default decision | Required before build |
|---|---|---|
| `agentops-evaluation` | Created alpha | Scenario templates, before/after report, scoring rubric, overhead review |
| `skill-security-audit` | Created alpha | Security review template, threat model, prompt-injection and script review scenarios |
| `technical-documentation` | Created alpha | README, API docs, release notes, architecture docs, migration guide scenarios |
| `backend-api` | Created alpha | API contract, schema review, auth flow, backend test plan scenarios |
| `devops-cloud-release` | Created alpha | Deployment, CI, rollback, env config, production readiness scenarios |
| `quality-testing` | Created alpha | Unit, integration, E2E, bug reproduction, QA matrix scenarios |
| `data-analytics-bi` | Created alpha | Metric definition, dashboard, funnel, cohort, experiment readout scenarios |
| `creator-content-engine` | Created alpha | Content pillar, script, calendar, repurposing, YouTube brief, and publishing checklist scenarios |
| `creator-brand-deals` | Created alpha | Media kit, brand pitch, rate card, deliverables, campaign recap, usage-rights scenarios |
| `creator-analytics-reporting` | Created alpha | Sponsor report, watch-time review, audience growth, affiliate performance, experiment readout scenarios |
| `creator-monetization` | Created alpha | Offer ladder, owned-product launch, membership/community pricing, merch margin, affiliate, dashboard scenarios |
| `creator-business-ops` | Created alpha | Weekly dashboard, sponsor pipeline, invoice readiness, production budget, contractor handoff, asset checklist scenarios |
| `creator-community` | Created alpha | Comment/DM triage, moderation, feedback synthesis, poll, engagement, and event scenarios |
| `creator-reputation-risk` | Created alpha | Sponsored disclosure, AI labeling, rights, brand-safety, controversy, and platform-policy scenarios |
| `creator-ai-production` | Created alpha | AI content workflow, prompt pack, synthetic character, voiceover, and batch production scenarios |
| `executive-command-center` | Created alpha | Brief, decision memo, risk register, leadership agenda scenarios |
| `founder-fundraising-ir` | Created alpha | Investor update, data room, diligence, and fundraising disclaimer templates |
| `ai-transformation-governance` | Created alpha | AI use-case portfolio, pilot scorecard, risk register, governance checklist |
| `owner-operator-os` | Created alpha | Cash-flow, pricing, vendor, delegation, and owner dashboard scenarios |
| `operating-cadence` | Composed alpha | Uses `executive-command-center` skills before adding cadence-specific skills |
| `board-governance` | Create later | Board memo, board pack, minutes, and governance review gates |
| `finance-strategy` | Compose first | Reuse `analytics-finance`; add executive scenario planning only if needed |
| `observability-debugging` | Compose first | Reuse engineering delivery and support escalation until traces/log scenarios justify split |
| `data-engineering` | Compose first | Reuse `backend-api`, `data-analytics-bi`, and `engineering-delivery` until pipeline work recurs |
| `knowledge-management` | Compose first | Reuse `technical-documentation` and support KB skills before creating a separate bundle |
| `revops-pipeline` | Compose first | Reuse `revenue-growth` and `analytics-finance`; add forecast/CRM scenarios first |
| `ops-pmo` | Defer or compose | Clear recurring artifacts: SOP, postmortem, status update, project risk review |
| `people-talent` | Defer | Policy/privacy gates and strong context templates |
| `partnerships-ma` | Defer | Diligence, negotiation, and integration-risk review gates |
| `crisis-comms` | Defer | Legal, compliance, reputation, and incident review gates |
| `security-trust` | Defer | Security review gates, prompt-injection handling, and strict MCP scope model |
| `legal-compliance` | Defer | Legal disclaimers, jurisdiction/counsel context, and review-only posture |
| `vertical-*` bundles | Defer | Domain validation, high-risk safety rules, and external expert review |

## Mapping Process

For each proposed bundle in an expansion document:

1. Name the target role and recurring job.
2. Identify the reviewable artifact the bundle should produce.
3. Map the proposal to an existing bundle, new skill, new bundle, alias, or
   deferred candidate.
4. Check risk tier and required approval gates.
5. Prefer composition from existing skills before creating new atomic skills.
6. Add route coverage scenarios before adding many skills.
7. Add a bundle brief before adding a manifest.
8. Validate with the release gate.

## Decision Rules

Create a new bundle only when:

- the workflow is recurring and role-specific
- at least three skills need to work together
- the bundle produces reviewable artifacts
- existing bundles would be misleading or too noisy
- safety rules and context templates are clear
- at least one route coverage scenario can be written without private data

Create a new atomic skill only when:

- no existing skill has the workflow as its main job
- the workflow has a distinct trigger
- the skill changes the agent's process, not just wording
- a concise `SKILL.md` and one useful reference checklist are enough

Defer a proposal when:

- it depends on high-liability legal, medical, financial, or security judgment
- it requires private connectors before a draft-first workflow is useful
- domain validation is weak
- the workflow is mostly an alias for an existing bundle

## Risk Tiers

| Tier | Examples | Default posture |
|---|---|---|
| Low | Drafting internal docs, planning, summarizing public docs | Draft-first |
| Medium | Customer replies, product specs, PR review, outbound drafts | Draft-first plus reviewer approval |
| High | Billing, account changes, production releases, finance reporting | Read-first plus explicit approval for writes |
| High-liability | Legal, compliance, security, regulated verticals | Review-only until governance is stronger |

## Expansion Review Output

When mapping a supplied expansion document, produce:

- proposed bundle
- decision: create, compose, alias, merge, or defer
- mapped existing bundle or skill
- missing atomic skills
- context templates needed
- route scenarios needed
- risk tier and approval gates
- pilot metric
- next implementation step
