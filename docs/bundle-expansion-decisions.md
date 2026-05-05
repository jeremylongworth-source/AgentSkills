# Bundle Expansion Decisions

This decision map records how current scope-broadening ideas map to the
portfolio. Use it as the baseline when reviewing the next expansion document.

## Current Decisions

| Proposal | Decision | Canonical target | Reason |
|---|---|---|---|
| Support and customer success | create alpha | `support-success` | High-volume reviewable workflow with clear draft/approval gates |
| Engineering delivery | create alpha | `engineering-delivery` | Strong fit for coding agents and existing QA/release coverage |
| Product research | create alpha | `product-research` | Distinct product-facing evidence-to-spec workflow |
| Revenue growth | compose alpha | `revenue-growth` | Existing sales/marketing skills cover most work; approval framing was missing |
| Analytics and finance | create alpha | `analytics-finance` | High-value read-first reporting workflow with strict review gates |
| Broad sales and marketing | keep existing | `sales-marketing` | Useful broad install target; overlaps with but does not replace `revenue-growth` |
| Broad research validation | keep existing | `research-validation` | General evidence bundle; `product-research` is the product-facing subset |
| Frontend/product delivery | keep existing | `frontend-product` | Implementation-quality bundle rather than research bundle |
| Game development and publishing | keep existing | `game-dev`, `html5-game-publishing` | Already has deep domain coverage |
| Executive operating workflows | create alpha | `executive-command-center` | Best flagship executive bundle: decisions, risk, cadence, and follow-up |
| Founder fundraising and IR | create alpha | `founder-fundraising-ir` | High-leverage founder workflow with visible artifacts and review gates |
| AI transformation governance | create alpha | `ai-transformation-governance` | Timely agent-adoption category with clear governance artifacts |
| AgentOps and skill evaluation | create alpha | `agentops-evaluation` | Signature proof system for scenario tests, before/after reports, scoring, and overhead review |
| Skill security auditing | create alpha | `skill-security-audit` | Signature trust system for prompt-injection, script, secrets, dependency, and install review |
| Creator content operations | create alpha | `creator-content-engine` | Strong non-developer workflow with concrete content artifacts and draft-first safety gates |
| Creator brand deals | create alpha | `creator-brand-deals` | High-value sponsorship workflow with concrete pitches, packages, rights checks, recaps, and review gates |
| Creator analytics reporting | compose alpha | `creator-analytics-reporting` | Reuses existing analytics/reporting skills while adding creator-specific performance and affiliate reporting |
| Creator monetization | compose alpha | `creator-monetization` | Reuses pricing, analytics, owner, content, and sponsor skills while adding offer ladder and owned-product launch planning |
| Creator business operations | compose alpha | `creator-business-ops` | Reuses owner, finance, pipeline, docs, and rights skills while adding invoice readiness and production ops briefs |
| Creator community operations | compose alpha | `creator-community` | Reuses support, research, content, and analytics skills while adding community triage and moderation briefs |
| Creator reputation risk | compose alpha | `creator-reputation-risk` | Reuses publishing, rights, AI governance, community, escalation, risk, and sponsor skills while adding one reputation review skill |
| Creator AI production | compose alpha | `creator-ai-production` | Reuses content, publishing, rights, reputation, production, and AI governance skills while adding media prompt briefs and synthetic character bibles |

## Earlier Suggested Additions

| Suggested area | Current mapping | Decision before adding new bundle |
|---|---|---|
| Backend/API development | `backend-api` | Built as an alpha bundle for API design, contracts, migrations, and service patterns |
| Data/analytics engineering | `analytics-finance` plus `engineering-delivery` | Add only if pipeline, warehouse, dbt, orchestration, and data quality workflows recur |
| DevOps/release engineering | `devops-cloud-release` | Built as an alpha bundle for deployment, CI, rollback, config, cost, and readiness |
| AI app development | `frontend-product`, `engineering-delivery`, `product-research` | Add only if model evals, prompts, RAG, agents, and AI safety become recurring work |
| Documentation/technical writing | `technical-documentation` | Built as an alpha bundle for docs IA, API docs, release docs, and docs QA |
| Business operations | backlog `ops-pmo` | Defer until SOP, project status, meeting, and operating cadence artifacts are clearer |
| Executive command center | `product-research`, `analytics-finance`, `revenue-growth` | Build as a new flagship bundle because the executive artifact set is distinct |
| Founder fundraising/IR | `analytics-finance`, `revenue-growth`, `concise-technical-writing` | Build as a new bundle with financial/legal/investment disclaimers |
| AI transformation governance | `llm-skill-authoring`, `product-research`, `engineering-delivery` | Build as a new bundle with governance, risk, and adoption artifacts |
| AgentOps/evaluation | `llm-skill-authoring`, `skill-evaluation-iteration` | Built as an alpha bundle because proof is now a core differentiator |
| Skill security audit | `llm-skill-authoring`, `qa-test-strategy`, `release-launch-readiness` | Built after `agentops-evaluation`; kept review-only and vendor-neutral |
| Backend/API | `backend-api` | Built after proof/security because API contracts, auth, schema, and backend tests need distinct routing |
| DevOps/cloud/release | `devops-cloud-release` | Built after backend/API for release/deployment scenarios |
| Quality/testing | `quality-testing` | Built as a standalone bundle because test planning deserves first-class routing |
| Data analytics/BI | `data-analytics-bi` | Built as a data-decision bundle distinct from finance close work |
| Customer success/support | `support-success` | Keep as canonical; add success/renewal skills only if new scenarios justify them |
| Customer success/account management | `support-success` | Strengthen support-success with account health, retention, QBR, renewal risk, and adoption workflows before splitting |
| Creator and influencer workflows | `creator-content-engine`, `creator-brand-deals`, `creator-analytics-reporting`, `creator-monetization`, `creator-business-ops`, `creator-community`, `creator-reputation-risk`, and `creator-ai-production` | Build platform expansion or live/event bundles only after real-input validation proves the core loop |

## Deferred Candidates

| Candidate | Decision | Required before alpha |
|---|---|---|
| `agentops-evaluation` | created alpha | before/after report scenarios, rubric scoring, skill overhead review |
| `skill-security-audit` | created alpha | threat model, prompt-injection review, script review, safe install scenarios |
| `technical-documentation` | created alpha | README, API docs, changelog, ADR, migration guide scenarios |
| `backend-api` | created alpha | API contract, auth flow, schema review, backend test scenarios |
| `devops-cloud-release` | created alpha | CI, deployment, rollback, environment, and production readiness scenarios |
| `quality-testing` | created alpha | QA matrix, bug reproduction, unit/integration/E2E test scenarios |
| `data-analytics-bi` | created alpha | metric definition, dashboard, funnel, cohort, experiment readout scenarios |
| `creator-content-engine` | created alpha | content pillar, script, calendar, repurposing, YouTube brief, and publishing checklist scenarios |
| `creator-brand-deals` | created alpha | media kit, brand pitch, rate card, sponsorship package, deliverables, usage rights, campaign recap scenarios |
| `creator-analytics-reporting` | created alpha | sponsor report, watch-time, retention, affiliate performance, content experiment readout scenarios |
| `creator-monetization` | created alpha | creator-owned revenue, pricing, offer ladder, product launch, and affiliate boundaries |
| `creator-business-ops` | created alpha | sponsor pipeline, invoices, production budget, assistant delegation, and contractor brief scenarios |
| `creator-community` | created alpha | comment/DM triage, fan feedback, moderation, audience research, and community event scenarios |
| `creator-reputation-risk` | created alpha | platform policy, disclosure, copyright, AI labeling, brand safety, and controversy response review scenarios |
| `creator-ai-production` | created alpha | AI content workflow, image/video/audio prompt packs, synthetic character bible, and batch production scenarios |
| `systems-automation` | compose first | Internal-tool, dashboard, form, integration, workflow automation, data-access, QA, and release scenarios |
| `ops-pmo` | defer | SOP, project risk, status update, postmortem, and meeting-summary scenarios |
| `owner-operator-os` | create alpha | Cash-flow, pricing, vendor negotiation, delegation, and owner dashboard scenarios |
| `operating-cadence` | composed alpha | Split into new atomic skills only if leadership cadence scenarios reveal gaps |
| `board-governance` | build later | Governance review language, board pack scenarios, and minutes/action follow-up artifacts |
| `finance-strategy` | compose first | Reuse `analytics-finance`; add runway/scenario skills if repeated executive use appears |
| `people-talent` | defer | privacy and policy templates, recruiting/onboarding scenarios, review gates |
| `partnerships-ma` | defer | diligence, negotiation, integration-risk, and announcement review gates |
| `crisis-comms` | defer | legal/compliance review, incident severity rules, stakeholder map scenarios |
| `security-trust` | defer | security governance, read-only posture, prompt-injection handling, strict MCP scopes |
| `legal-compliance` | defer | counsel-reviewed disclaimers, jurisdiction context, review-only posture |
| `vertical-*` | defer | domain expert validation, safety gates, and non-generic artifacts |

## Rules for the Next Expansion Document

Use these rules when mapping new proposals:

- If the proposal is mostly a role-specific install target for existing skills,
  compose a bundle first.
- If the proposal has a distinct task trigger and artifact, add one atomic skill
  before adding a large bundle.
- If the proposal overlaps with an alpha bundle, add scenarios before new
  skills.
- If the proposal is high-liability, add governance and review-only guidance
  before implementation skills.
- If the proposal requires private connectors to be useful, defer connector work
  and define a draft/read-only workflow first.

## Output Format for Future Mapping

For each proposal in the incoming document, record:

- proposal name
- source section or quote summary
- decision: create, compose, alias, merge, or defer
- canonical target bundle
- missing skills or context templates
- route scenarios to add
- risk tier and approval gates
- pilot metric
- next implementation step
