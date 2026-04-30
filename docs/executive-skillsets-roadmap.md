# Executive Skillsets Roadmap

This roadmap captures the next executive-oriented expansion after the first
business alpha bundles. The direction is to serve CEOs, founders, owners,
chiefs of staff, and leadership teams with artifact-first workflows.

## Positioning

Reusable AI-agent workflows for builders, operators, and executive teams.

For executive users, AgentSkills should help leaders turn messy context into
clear reviewable artifacts:

- brief
- memo
- dashboard
- risk register
- decision log
- agenda
- scorecard
- roadmap
- checklist
- scenario plan
- stakeholder message

Do not make these generic CEO advice bundles. Every skill should produce one
concrete executive artifact.

## Evidence and Timing

The executive expansion is timely because AI adoption is moving from isolated
experiments into governed operating systems. Deloitte's 2025 TMT Predictions
forecast that enterprise AI agent deployment among enterprises using GenAI
would rise from 25% in 2025 to 50% by 2027. Deloitte's 2026 State of AI in the
Enterprise report also highlights an agentic AI governance gap: only one in
five companies has a mature governance model for autonomous AI agents.

Sources reviewed on 2026-04-30:

- [Deloitte 2025 TMT Predictions](https://www.deloitte.com/us/en/about/press-room/deloitte-technology-media-telecom-2025-predictions.html)
- [Deloitte State of AI in the Enterprise](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html)

## Executive Use-Case Map

| Executive user | Core pressure | High-value use cases | Best new bundle |
|---|---|---|---|
| CEO / founder | Too many ambiguous decisions | weekly CEO brief, strategic options memo, decision log, risk register | `executive-command-center` |
| Startup founder | Fundraising and investor narrative | investor updates, data room checklist, diligence responses, deck story | `founder-fundraising-ir` |
| Small business owner | Cash, operations, local growth, hiring | cash-flow triage, pricing review, vendor negotiation, monthly owner dashboard | `owner-operator-os` |
| COO / chief of staff | Execution across teams | OKRs, operating cadence, meeting system, escalation tracking | `operating-cadence` |
| CFO / finance lead | Runway, margin, unit economics | budget variance, scenario planning, runway model review, pricing sensitivity | `finance-strategy` |
| Board-facing CEO | Governance and board prep | board pack, board questions, risk oversight, action follow-up | `board-governance` |
| AI transformation lead | Turning AI experiments into ROI | AI use-case portfolio, pilot selection, governance, adoption plan | `ai-transformation-governance` |
| Founder hiring team | Hiring and org design | role scorecards, interview loops, org design, performance memos | `people-leadership` |
| CEO / BD lead | Partnerships and M&A | partner thesis, target screen, negotiation prep, integration risks | `partnerships-ma` |
| CEO in incident mode | Crisis and reputation | incident brief, stakeholder updates, customer apology, postmortem | `crisis-comms` |

## Recommended Build Order

### 1. `executive-command-center`

Status: alpha added.

Primary user: CEO, founder, owner, chief of staff.

Why first: this is the flagship executive bundle. It is broad enough for CEOs,
founders, and owners, but concrete enough to produce useful artifacts.

Core use cases:

- weekly executive briefing
- strategic options memo
- decision log
- risk register
- priority filter
- leadership meeting prep
- follow-up action tracker

Suggested skills:

- `executive-briefing`
- `decision-memo`
- `strategic-options`
- `risk-register`
- `priority-filter`
- `leadership-meeting-prep`
- `action-tracker`

Outputs:

- 1-page executive brief
- decision memo
- risk and opportunity register
- weekly leadership agenda
- action owner list

Positioning:

Reusable CEO operating workflows for turning messy context into clear decisions.

### 2. `founder-fundraising-ir`

Status: alpha added.

Primary user: startup founder, CEO, investor-facing operator.

Why second: fundraising is repeated, painful, high-leverage, and visible to
startup audiences.

Core use cases:

- investor update
- fundraising narrative
- pitch deck outline
- data room checklist
- due diligence response prep
- investor target list structure
- term sheet question list

Suggested skills:

- `investor-update`
- `fundraising-narrative`
- `pitch-deck-structure`
- `data-room-checklist`
- `diligence-response-prep`
- `investor-targeting`
- `term-sheet-questions`

Outputs:

- monthly investor update
- seed or Series A narrative
- pitch deck skeleton
- data room readiness checklist
- diligence FAQ
- investor CRM schema

Safety:

- analysis support only
- not legal, tax, investment, or financial advice
- human review required before investor sends, diligence responses, financial
  claims, fundraising claims, or term-sheet decisions

Positioning:

Founder-ready workflows for investor updates, fundraising prep, and diligence.

### 3. `ai-transformation-governance`

Status: alpha added.

Primary user: CEO, CIO, CTO, AI lead, transformation lead.

Why third: it connects AgentSkills directly to the current AI-agent adoption
conversation and gives the repo a timely strategic category.

Core use cases:

- AI use-case portfolio
- pilot selection
- AI risk register
- vendor evaluation
- model/data governance checklist
- adoption training plan
- pilot-to-scale roadmap

Suggested skills:

- `ai-use-case-portfolio`
- `ai-pilot-selection`
- `ai-risk-register`
- `ai-vendor-evaluation`
- `ai-governance-checklist`
- `ai-adoption-plan`
- `pilot-to-scale-roadmap`

Outputs:

- AI opportunity map
- pilot scorecard
- risk register
- vendor evaluation matrix
- governance checklist
- adoption roadmap

Safety:

- distinguish strategy, policy, security, privacy, and compliance assumptions
- require human approval before vendor commitments, policy changes, production
  AI rollout, employee-impacting decisions, or sensitive data access

Positioning:

Executive workflows for moving AI from experiments to governed business value.

## Later Executive Bundles

| Priority | Bundle | Decision | Notes |
|---|---|---|---|
| 4 | `owner-operator-os` | alpha added | Opens AgentSkills to small business and non-enterprise operators |
| 5 | `operating-cadence` | composed alpha added | Uses executive artifact skills before adding cadence-specific skills |
| 6 | `board-governance` | create later | High-value, document-heavy, and reviewable; requires governance language |
| 7 | `finance-strategy` | compose first | Reuse `analytics-finance`; add only if executive scenario planning needs distinct skills |
| 8 | `people-leadership` | defer | Employment-law and privacy review gates needed |
| 9 | `partnerships-ma` | defer | Strategic and document-heavy, but diligence and negotiation risks are higher |
| 10 | `crisis-comms` | defer | Useful but legal, compliance, reputation, and incident risks require strong review gates |

## v0.2 Roadmap Language

The next AgentSkills expansion focuses on executive operators: CEOs, founders,
owners, chiefs of staff, and top-level business leaders.

Planned skillset bundles:

- `executive-command-center`: weekly executive briefs, decision memos, risk
  registers, and leadership cadence
- `founder-fundraising-ir`: investor updates, fundraising narrative, data room
  prep, and diligence response workflows
- `ai-transformation-governance`: AI use-case portfolio, pilot selection,
  governance, vendor evaluation, and adoption roadmap
- `owner-operator-os`: cash-flow triage, pricing review, vendor negotiation,
  delegation, and owner dashboards
- `operating-cadence`: OKRs, leadership meetings, monthly business reviews,
  decision logs, and escalation memos
- `board-governance`: board packs, board questions, risk oversight, minutes,
  and board follow-up
- `finance-strategy`: runway, unit economics, budget variance, pricing
  sensitivity, and scenario planning
- `people-leadership`: hiring plans, role scorecards, interview loops, org
  design, and performance communication
- `partnerships-ma`: partner thesis, target screening, negotiation prep,
  diligence, and integration risk
- `crisis-comms`: incident briefs, stakeholder updates, customer messages,
  employee FAQs, and postmortems

## Design Rules

- Build artifact-producing skills, not advice-only skills.
- Reuse existing alpha bundles where possible:
  - `analytics-finance` for numbers, variance, and runway context
  - `revenue-growth` for market, customer, and pipeline context
  - `product-research` for evidence and decision framing
  - `engineering-delivery` for delivery, release, and technical risk
  - `support-success` for customer impact and incident signals
- Keep executive bundles draft-first and review-first.
- Add route scenarios before adding many skills.
- Avoid private connectors until a read-only or draft-first workflow is useful.
- Add disclaimers for finance, fundraising, legal, people, M&A, and crisis
  communication workflows.

## Next Implementation Step

Forward-test `operating-cadence` against realistic weekly leadership, OKR
review, and monthly business review samples. Then decide whether
`board-governance` or `finance-strategy` should be next based on pilot evidence.
