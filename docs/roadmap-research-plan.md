# Roadmap Research Plan

This plan turns `deep-research-report (1).md` and current ecosystem checks into
an execution path for broadening AgentSkills.

## Research Goal

Decide which business workflow bundles to build first, what each bundle must
prove, and what safety/governance rules must ship with it.

The current working thesis is:

- build role-based, vendor-neutral workflow bundles
- start with reviewable, horizontal desk workflows
- keep actions draft-first and read-first by default
- require approval for outbound, financial, legal, production, or account
  changes
- use pilot metrics to decide whether a bundle deserves deeper investment

## Current Evidence Snapshot

Reviewed sources:

- deep research report supplied by the project owner, reviewed 2026-04-30
- [GitHub CLI `gh skill install`](https://cli.github.com/manual/gh_skill_install), reviewed 2026-04-30
- [GitHub Copilot agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), reviewed 2026-04-30
- [OpenAI Codex skills](https://developers.openai.com/codex/skills), reviewed 2026-04-30
- [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices), reviewed 2026-04-30
- [Claude Code plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), reviewed 2026-04-30
- [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401), reviewed 2026-04-30
- [Agent Skills in the Wild](https://arxiv.org/abs/2601.10338), reviewed 2026-04-30
- [AgentSkillOS](https://arxiv.org/abs/2603.02176), reviewed 2026-04-30
- [Langfuse skill evaluation example](https://langfuse.com/blog/2026-02-26-evaluate-ai-agent-skills), reviewed 2026-04-30
- [VoltAgent awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills), reviewed 2026-04-30
- [Supabase agent-skills](https://github.com/supabase/agent-skills), reviewed 2026-04-30
- [Addy Osmani agent-skills](https://github.com/addyosmani/agent-skills), reviewed 2026-04-30
- [McKinsey State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai/), reviewed 2026-04-30
- [IBM 2025 CEO Study](https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles), reviewed 2026-04-30
- [U.S. Chamber 2025 small business AI report](https://www.uschamber.com/technology/empowering-small-business-the-impact-of-technology-on-u-s-small-business), reviewed 2026-04-30
- creator and influencer expansion report supplied by the project owner,
  reviewed 2026-04-30
- [Goldman Sachs creator economy outlook](https://www.goldmansachs.com/insights/articles/the-creator-economy-could-approach-half-a-trillion-dollars-by-2027), reviewed 2026-04-30
- [Collabstr 2025 influencer marketing report](https://collabstr.com/2025-influencer-marketing-report), reviewed 2026-04-30
- [IAB 2025 creator economy ad spend report](https://www.iab.com/news/creator-economy-ad-spend-to-reach-37-billion-in-2025-growing-4x-faster-than-total-media-industry-according-to-iab/), reviewed 2026-04-30

Current source implications:

- Agent skills are converging on portable folders with `SKILL.md`, scripts,
  references, and optional resources.
- `gh skill install` is useful for distribution and supports many agent hosts,
  but it remains an adapter path, not the portable contract.
- Copilot docs reinforce that skills are selected by description and may carry
  scripts/resources.
- Public skill distribution requires preview and inspection because skills can
  contain hidden instructions or scripts.
- MCP scope and permissioning should start narrow and expand only when a task
  needs elevated access.
- Plugin marketplaces create another distribution path, but packaging should
  remain modular because host behavior is still evolving.
- Public benchmark research suggests many skills may not improve outputs unless
  they are specific, compatible with context, and tested against acceptance
  criteria.
- Public skill security research supports treating skills like dependencies,
  especially when they include scripts, permissions, network access, or
  third-party install steps.
- Ecosystem examples support workflow-based bundles with verification gates,
  product-specific expertise, and lightweight evaluation datasets.
- Executive and small-business adoption signals support business/operator
  bundles, but those bundles should come after proof and trust tracks are in
  place.
- Creator and influencer workflows are a strong vertical because they are
  repetitive, artifact-heavy, and can start with draft-first content planning
  before adding platform connectors or sponsorship workflows.

## Research Questions

### Bundle Portfolio

- Which proposed bundles are new, and which are better handled as aliases or
  refinements of existing bundles?
- Should `sales-marketing` remain a broad bundle while `revenue-growth` becomes
  the sharper launch bundle?
- Should `research-validation` stay broad, or should `product-research` become
  the product-facing bundle?
- Is `engineering-delivery` one bundle, or should `qa-release` remain separate?

### Buyer and Use Case

- Who is the first buyer or champion for each bundle?
- What recurring task does the bundle help them complete?
- What artifact does the bundle produce that a reviewer can inspect?
- What metric would make the buyer care after one pilot?

### Safety and Governance

- Which actions must always require approval?
- Which MCP categories are read-only by default?
- What context files are required to avoid hallucinated policy, pricing,
  commitments, or numbers?
- What should the bundle refuse or escalate?

### Distribution

- Which host should be the first non-Codex setup target for each bundle?
- Which bundles need marketplace/plugin packaging later?
- Which README snippets or social previews are needed for discovery?

## Workstreams

| Workstream | Purpose | Output |
|---|---|---|
| Portfolio taxonomy | Decide canonical bundle names and aliases | updated `docs/scope-broadening-roadmap.md` and skillset manifests |
| Bundle design | Define skills, context files, safety rules, and routing | bundle brief per skillset |
| Pilot validation | Define metrics, control flow, and decision rules | validation plan per bundle |
| Host packaging | Keep portable core stable while supporting hosts | setup docs and templates only where behavior differs |
| Distribution proof | Show why a bundle is worth trying | examples, before/after flows, README snippets |

Mapping artifacts:

- [bundle expansion map](bundle-expansion-map.md)
- [bundle expansion decisions](bundle-expansion-decisions.md)
- [executive skillsets roadmap](executive-skillsets-roadmap.md)
- [creator skillsets roadmap](creator-skillsets-roadmap.md)
- [evaluation proof layer](evaluation/README.md)

## First Development Backlog

### 0. Evaluation Proof Layer

Status: implemented under `docs/evaluation/`.

Add reusable templates for proving whether skills and bundles improve outputs.

Artifacts:

- `evaluation-method.md`
- `scenario-test-template.md`
- `before-after-report-template.md`
- `skill-quality-rubric.md`
- `security-review-template.md`

Acceptance criteria:

- templates stay host-neutral and tool-optional
- quality and security reviews produce concrete pass/revise/block decisions
- future bundles can link to these templates without adding manifest schema

### 0.1 AgentOps Evaluation Bundle

Status: alpha bundle added as `agentops-evaluation`.

Create a bundle for maintainers who need to test, compare, and improve skills.

Candidate skills:

- `skill-benchmark-design`
- `scenario-test-authoring`
- `before-after-evaluation`
- `acceptance-criteria-mapper`
- `prompt-regression-testing`
- `skill-output-scoring`
- `skill-token-overhead-review`

Acceptance criteria:

- at least three scenarios route to the bundle
- output includes a benchmark plan, before/after report, and improvement memo
- no vendor-specific tracing or evaluation platform is required

### 0.2 Skill Security Audit Bundle

Status: alpha bundle added as `skill-security-audit`.

Create a review-only bundle for auditing skills before install or publish.

Candidate skills:

- `skill-threat-model`
- `prompt-injection-review`
- `data-exfiltration-review`
- `script-permission-review`
- `supply-chain-review`
- `secrets-handling-review`
- `safe-install-checklist`

Acceptance criteria:

- at least three scenarios route to the bundle
- output includes a security report, risk matrix, unsafe instruction list, and
  safe-install recommendation
- scripts, dependencies, MCP scopes, and host-specific install steps are
  reviewed before approval

### 0.3 Creator Content Engine Bundle

Status: alpha bundle added as `creator-content-engine`.

Create a creator workflow bundle for turning ideas into publishable content
artifacts without requiring live social account access.

Candidate skills:

- `content-pillars`
- `short-form-hooks`
- `video-script`
- `thumbnail-title-brief`
- `caption-writer`
- `content-calendar`
- `longform-to-shorts`
- `newsletter-repurpose`
- `podcast-outline`
- `publishing-checklist`

Acceptance criteria:

- at least five scenarios route to the bundle
- output includes a pillar map, hook pack, video script, content calendar,
  repurposing plan, or publishing checklist
- publishing, scheduling, sponsor claims, disclosures, and platform-specific
  tactics remain human-reviewed and current-source verified when needed

### 0.4 Creator Brand Deals Bundle

Status: alpha bundle added as `creator-brand-deals`.

Create a creator sponsorship workflow bundle for media kits, pitches, packages,
rate-card drafts, campaign proposals, usage-rights review, negotiation prep,
deliverable tracking, recaps, and renewals.

Candidate skills:

- `brand-pitch`
- `media-kit-builder`
- `sponsorship-package`
- `rate-card-builder`
- `campaign-proposal`
- `usage-rights-checklist`
- `deal-negotiation-prep`
- `deliverables-tracker`
- `campaign-recap`
- `renewal-pitch`

Acceptance criteria:

- at least five scenarios route to the bundle
- output includes a sponsor pitch, media kit section, package table, rate-card
  draft, campaign proposal, rights checklist, negotiation plan, tracker, recap,
  or renewal pitch
- sponsor sends, contract terms, pricing commitments, rights approvals, and
  sponsored publishing remain human-reviewed

### 0.5 Creator Analytics Reporting Bundle

Status: alpha bundle added as `creator-analytics-reporting`.

Create a creator reporting workflow bundle for source-backed sponsor reports,
content performance reviews, audience growth reviews, affiliate reporting,
content experiment readouts, dashboards, attribution, and instrumentation.

New creator-specific skills:

- `creator-content-performance-review`
- `affiliate-performance-report`

Existing skills to reuse:

- `campaign-recap`
- `renewal-pitch`
- `deliverables-tracker`
- `metric-definition`
- `metric-narrative`
- `dashboard-design`
- `retention-analysis`
- `cohort-analysis`
- `funnel-analysis`
- `experiment-readout`
- `experiment-design-validation`
- `marketing-analytics-attribution`
- `analytics-instrumentation-plan`

Acceptance criteria:

- at least six scenarios route to the bundle
- output includes a sponsor report, content performance memo, audience growth
  review, affiliate report, experiment readout, dashboard spec, or tracking plan
- platform, sponsor, affiliate, CRM, payment, analytics, and social tools stay
  read-only unless the user approves a specific write, send, or publish action

### 0.6 Creator Monetization Bundle

Status: alpha bundle added as `creator-monetization`.

Create a composed creator-owned revenue workflow for offer ladders, owned-product
launches, pricing, affiliate review, membership/community pricing, merch margin
review, and monetization dashboards.

New creator-specific skills:

- `creator-offer-ladder`
- `creator-owned-product-launch-plan`

Existing skills to reuse:

- `pricing-packaging-strategy`
- `pricing-margin-review`
- `affiliate-performance-report`
- `marketing-analytics-attribution`
- `metric-definition`
- `metric-narrative`
- `dashboard-design`
- `funnel-analysis`
- `retention-analysis`
- `content-calendar`
- `caption-writer`
- `publishing-checklist`
- `content-seo-strategy`
- `owner-dashboard`
- `cash-flow-triage`
- `rate-card-builder`
- `sponsorship-package`
- `campaign-recap`
- `renewal-pitch`
- `experiment-design-validation`
- `experiment-readout`

Acceptance criteria:

- at least six scenarios route to the bundle
- output includes an offer ladder, owned-product launch plan, membership or
  community pricing model, merch margin review, affiliate review, dashboard
  spec, or validation plan
- checkout, pricing, payment, email, platform, affiliate, refund, and financial
  reporting actions remain human-reviewed

### 0.7 Creator Business Ops Bundle

Status: alpha bundle added as `creator-business-ops`.

Create a composed creator operations workflow for weekly reviews, sponsor
pipeline hygiene, invoice readiness, production ops, contractor/assistant
handoffs, asset-system checklists, lightweight SOPs, and operating dashboards.

New creator-specific skills:

- `creator-invoice-readiness`
- `creator-production-ops-brief`

Existing skills to reuse:

- `owner-dashboard`
- `cash-flow-triage`
- `finance-close-checklist`
- `pricing-margin-review`
- `ops-bottleneck-review`
- `vendor-negotiation-prep`
- `action-tracker`
- `deliverables-tracker`
- `sales-pipeline-management`
- `dashboard-design`
- `metric-definition`
- `metric-narrative`
- `variance-commentary`
- `kb-from-resolution`
- `tutorial-writing`
- `usage-rights-checklist`
- `brand-pitch`

Acceptance criteria:

- at least six scenarios route to the bundle
- output includes a weekly ops dashboard, sponsor pipeline review, invoice
  readiness checklist, production ops brief, assistant/contractor handoff,
  asset checklist, SOP, or action tracker
- accounting, banking, payroll, CRM, payment, project-management, social,
  storage, publishing, and contractor systems stay read-only unless the user
  approves a specific action

### 0.8 Creator Community Bundle

Status: alpha bundle added as `creator-community`.

Create a composed creator audience workflow for comment and DM triage,
moderation review, feedback synthesis, polls, engagement planning, and
community event prompts.

New creator-specific skills:

- `community-triage`
- `community-moderation-brief`

Existing skills to reuse:

- `reply-drafting`
- `ticket-triage`
- `escalation-pack`
- `feedback-synthesis`
- `customer-research-validation`
- `experiment-design-validation`
- `content-pillars`
- `caption-writer`
- `content-calendar`
- `publishing-checklist`
- `metric-definition`
- `metric-narrative`
- `creator-content-performance-review`

Acceptance criteria:

- at least six scenarios route to the bundle
- output includes a triage table, moderation brief, feedback synthesis, poll
  plan, engagement calendar, event plan, reviewed reply queue, or escalation
  packet
- social, community, support, CRM, publishing, moderation, and member systems
  stay read-only unless the user approves a specific action

### 0.9 Creator Reputation Risk Bundle

Status: alpha bundle added as `creator-reputation-risk`.

Create a composed creator trust workflow for sponsored disclosure checks, AI
labeling, rights/copyright risk, platform-policy uncertainty, brand-safety
review, controversy response briefs, and hold/revise/go recommendations.

New creator-specific skill:

- `creator-reputation-risk-review`

Existing skills to reuse:

- `publishing-checklist`
- `caption-writer`
- `usage-rights-checklist`
- `community-triage`
- `community-moderation-brief`
- `reply-drafting`
- `escalation-pack`
- `risk-register`
- `ai-risk-register`
- `ai-governance-checklist`
- `campaign-proposal`
- `sponsorship-package`

Acceptance criteria:

- at least six scenarios route to the bundle
- output includes a reputation risk memo, disclosure checklist, rights risk
  list, AI-labeling review, brand-safety memo, controversy response brief,
  escalation packet, or hold/revise/go recommendation
- legal, compliance, copyright, platform-policy, crisis, moderation, sponsor,
  and public-response decisions remain human-reviewed

### 0.10 Creator AI Production Bundle

Status: alpha bundle added as `creator-ai-production`.

Create a composed, provider-neutral AI production planning workflow for media
prompt packs, synthetic character bibles, source-asset provenance, disclosure,
rights, likeness/voice boundaries, batch production handoffs, and human-review
gates.

New creator-specific skills:

- `ai-media-prompt-brief`
- `synthetic-character-bible`

Existing skills to reuse:

- `content-calendar`
- `creator-production-ops-brief`
- `video-script`
- `podcast-outline`
- `thumbnail-title-brief`
- `caption-writer`
- `publishing-checklist`
- `usage-rights-checklist`
- `creator-reputation-risk-review`
- `ai-risk-register`
- `ai-governance-checklist`

Acceptance criteria:

- at least six scenarios route to the bundle
- output includes an AI content workflow, image/video/audio prompt pack,
  synthetic character bible, voiceover plan, batch production plan, source
  provenance notes, or human-review checklist
- generation, publishing, rights, legal, platform-policy, sponsor, likeness,
  voice, and disclosure decisions remain human-reviewed

### 1. Bundle Brief Template

Status: implemented in `templates/bundles/bundle-brief.md`.

Create a reusable brief format for new bundles.

Fields:

- problem
- target user
- included skills
- context files
- MCP preset intent
- safety rules
- pilot metrics
- acceptance criteria
- install notes

Acceptance criteria:

- brief is small enough to copy for every new bundle
- no host-specific fields are required
- links to bundle authoring and vendor-neutrality docs

### 2. Route Coverage Scenarios

Status: initial scenarios added under `tests/scenarios/`.

Add scenario files for the top five bundles before adding many skills.

Initial scenarios:

- support ticket triage and draft reply
- issue to implementation plan and regression risk
- feedback corpus to PRD
- account research to approved outreach draft
- KPI question to reviewed metric narrative

Acceptance criteria:

- every top-five bundle has at least one scenario
- expected routing names existing or planned skills
- scenarios avoid requiring private data or live systems

### 3. Support and Success Alpha

Status: alpha bundle added as `support-success`.

Build the first new bundle after the brief and scenario structure exist.

Minimum viable skills:

- `ticket-triage`
- `reply-drafting`
- `escalation-pack`
- `kb-from-resolution`

Minimum context templates:

- `SUPPORT_POLICY.md`
- `ESCALATION_RULES.md`
- `KB_STYLE_GUIDE.md`
- `PRODUCT_GLOSSARY.md`

Pilot decision:

- Continue if draft acceptance and QA scores are strong enough to justify
  deeper connector work.

### 4. Engineering Delivery Alpha

Status: alpha bundle added as `engineering-delivery`.

Build or compose an engineering workflow bundle using current QA/release
strengths.

Minimum viable skills:

- `issue-to-plan`
- `pr-review`
- `regression-check`
- `release-risk`

Pilot decision:

- Continue if accepted-plan rate and retained-test rate are strong, and if
  reviewer trust does not degrade.

### 5. Bundle Metadata Decision

Wait for the incoming expansion document before changing manifest schema.

Candidate optional fields:

- `category`
- `aliases`
- `recommended_for`
- `pilot_metrics`
- `governance`
- `context_templates`

Decision rule:

- Add a field only when at least two bundles need it and one script or doc uses
  it.

## Pilot Design Pattern

For each bundle, use one operational metric, one quality metric, one adoption
metric, and one economic metric.

| Bundle | Operational | Quality | Adoption | Economic |
|---|---|---|---|---|
| `support-success` | first-response time | QA score | draft acceptance | resolutions/hour |
| `engineering-delivery` | issue-to-plan time | reopen or defect rate | accepted-plan rate | cycle-time reduction |
| `product-research` | time-to-draft-spec | revision rounds | PM acceptance | backlog grooming time |
| `revenue-growth` | call-prep time | rewrite rate | approved drafts | meetings booked |
| `analytics-finance` | time-to-answer | reviewer edit rate | confidence rating | analyst hours saved |
| `creator-content-engine` | idea-to-calendar time | creator edit rate | retained asset rate | planning hours saved |
| `creator-brand-deals` | inbound-to-proposal time | manager edit rate | approved sponsor asset rate | deal-prep hours saved |
| `creator-analytics-reporting` | export-to-report time | metric caveat edit rate | approved report rate | reporting hours saved |
| `creator-monetization` | idea-to-offer-plan time | pricing/review edit rate | approved test rate | launch planning hours saved |
| `creator-business-ops` | scattered-ops-to-review time | handoff edit rate | weekly artifact use rate | admin hours saved |
| `creator-community` | raw-queue-to-triage time | reply/moderation edit rate | weekly community review use | reduced missed escalations |
| `creator-reputation-risk` | risky-packet-to-memo time | legal/manager edit rate | hold/revise/go memo use | fewer missed risk checks |
| `creator-ai-production` | concept-to-prompt-pack time | editor/creator edit rate | provenance/review checklist use | fewer missed AI-risk checks |

## Near-Term Decisions

Make these decisions before building more than one new bundle:

1. Canonical names versus legacy bundle aliases.
2. Whether `support-success` starts with four atomic skills or composes larger
   existing skills first.
3. Whether route coverage lives in `tests/scenarios/` only, or also in bundle
   docs.
4. Whether context templates live under `templates/context/` or inside each
   skill reference folder.
5. Which non-Codex host gets the first full setup example.

## Next Implementation Step

Forward-test `agentops-evaluation`, `skill-security-audit`,
`technical-documentation`, `backend-api`, `devops-cloud-release`,
`quality-testing`, `data-analytics-bi`, `creator-content-engine`, and
`creator-brand-deals`, `creator-analytics-reporting`, and
`creator-monetization`, `creator-business-ops`, `creator-community`,
`creator-reputation-risk`, and `creator-ai-production` with anonymized real
inputs before selecting the next executive, customer success, creator, or
vertical expansion.
