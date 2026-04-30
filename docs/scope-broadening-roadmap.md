# Scope Broadening Roadmap

This roadmap turns the deep research report into an implementation path for
AgentSkills. The direction is to broaden from a portable skill library into a
governed library of role-based workflow bundles, while keeping the core
vendor-neutral and file-based.

The latest scope-broadening memo adds a stronger priority: AgentSkills should
differentiate on trusted, tested bundles rather than volume. The next expansion
therefore moves `agentops-evaluation` and `skill-security-audit` ahead of more
vertical or executive variants.

For the executive expansion, see
[executive skillsets roadmap](executive-skillsets-roadmap.md).
For the creator and influencer expansion, see
[creator skillsets roadmap](creator-skillsets-roadmap.md).

## Product Thesis

AgentSkills should be positioned as reusable workflow bundles for high-value
business work, not as a prompt collection. Each bundle should package:

- portable skills
- references and operating context files
- routing guidance
- MCP preset intent
- measurable pilot outcomes
- host-specific setup only at the adapter layer
- scenario tests and before/after proof
- security review boundaries for skills, scripts, and MCP/tool access

The first wave should favor horizontal, reviewable, desk-based workflows. These
are easier to validate, easier to inspect, and safer than high-liability
vertical automation.

## Guiding Principles

- Keep the portable core in Markdown, YAML, TOML, JSON, and scripts.
- Keep host-specific paths and commands in setup guides, templates, and adapter
  scripts.
- Default to draft-first and read-first behavior.
- Require human approval before customer sends, system writes, financial
  publication, legal outputs, production deployments, or other high-risk acts.
- Track pilot metrics that buyers already understand: turnaround time,
  acceptance rate, error reduction, cycle time, revenue conversion, and
  speed-to-market.
- Add vertical and high-liability bundles only after governance and validation
  are stronger.
- Treat third-party skills like dependencies: inspect instructions, scripts,
  install steps, and permissions before use.
- Promote skills based on output quality, safety, and scenario evidence, not
  package count.

## Current Foundation

Already in place:

- vendor-neutrality guidance
- host setup guides
- examples for skill, skillset, MCP, and before/after behavior
- bundle authoring guide
- bundle brief template
- skillset listing utility
- skillset manifest validation
- release check script
- Codex skillset dry-run mode
- evaluation proof templates under `docs/evaluation/`
- v0.2 alpha validation plan under `docs/evaluation/`
- dynamic MCP preset parsing from `mcp/presets/*.toml`
- route coverage scenarios for the top-five expansion bundles
- bundle expansion map for reviewing new bundle proposals

This gives us enough foundation to add new bundles without creating a larger
platform layer.

## Priority Bundle Waves

| Wave | Bundle | Status | Why now |
|---|---|---|---|
| 0 | `agentops-evaluation` | alpha | Signature proof track for testing whether skills improve outputs |
| 0 | `skill-security-audit` | alpha | Signature trust track for reviewing skills before install or publish |
| 1 | `technical-documentation` | alpha | Strong GitHub audience fit and easy to demonstrate on this repo |
| 1 | `backend-api` | alpha | Fills the largest technical gap after frontend/product coverage |
| 1 | `devops-cloud-release` | alpha | Complements engineering delivery with deployment, CI, rollback, and readiness artifacts |
| 1 | `quality-testing` | alpha | Makes testing a first-class bundle instead of only embedded QA guidance |
| 1 | `data-analytics-bi` | alpha | Adds data-backed decision workflows separate from qualitative research |
| 1 | `creator-content-engine` | alpha | Opens a creator operating workflow with content pillars, hooks, scripts, calendars, and repurposing |
| 1 | `creator-brand-deals` | alpha | Adds creator sponsorship workflows for pitches, media kits, packages, rights review, recaps, and renewals |
| 1 | `creator-analytics-reporting` | alpha | Adds source-backed creator reporting for content performance, sponsors, affiliates, experiments, and dashboards |
| 1 | `creator-monetization` | alpha | Adds creator-owned revenue workflows for offer ladders, product launches, pricing, affiliates, and dashboards |
| 1 | `creator-business-ops` | alpha | Adds weekly ops, sponsor pipeline, invoice readiness, production handoff, and asset checklist workflows |
| 1 | `creator-community` | alpha | Adds comment/DM triage, moderation briefs, feedback synthesis, polls, engagement plans, and event prompts |
| 1 | `creator-reputation-risk` | alpha | Adds disclosure, rights, AI-labeling, brand-safety, platform-policy, and response risk reviews |
| 1 | `creator-ai-production` | alpha | Adds provider-neutral AI media prompt briefs, synthetic character bibles, provenance, disclosure, and review gates |
| 1 | `support-success` | alpha | Highest business evidence and clear reviewable workflow: triage, draft, escalate, KB |
| 1 | `engineering-delivery` | alpha | Strong fit with repo-aware agents, issue triage, PR review, QA, release planning |
| 2 | `product-research` | alpha | Converts feedback and evidence into PRDs, roadmap briefs, and market scans |
| 2 | `revenue-growth` | alpha | Existing skills already map well; needs approval-aware outbound framing |
| 3 | `analytics-finance` | alpha | High value but needs stronger read-only data assumptions and financial review gates |
| 4 | `executive-command-center` | alpha | Flagship executive bundle for briefs, decisions, risks, priorities, and follow-through |
| 4 | `founder-fundraising-ir` | alpha | High-leverage founder workflow with investor, data room, and diligence artifacts |
| 4 | `ai-transformation-governance` | alpha | Timely AI-agent governance workflow tied to pilot selection and adoption |
| 5 | `owner-operator-os` | alpha | Opens AgentSkills to small business and non-enterprise operators |
| 5 | `operating-cadence` | composed alpha | Uses executive artifact skills before adding cadence-specific skills |
| 5 | `board-governance` | planned later | High-value board work with governance review gates |
| 6 | `finance-strategy` | compose first | Reuse analytics-finance before adding executive finance strategy skills |
| 6 | `people-leadership` | later | Recruiting, org, and performance workflows need employment-law caution |
| 6 | `partnerships-ma` | later | Strategic but higher-risk diligence and negotiation workflows |
| 6 | `crisis-comms` | later | Useful but legal, compliance, incident, and reputation risks are high |
| 7 | `security-trust` | later | Valuable but higher blast radius; needs strong governance |
| 7 | `legal-compliance` | later | High value but high liability; should follow mature approval and evidence patterns |
| 8 | `vertical-*` bundles | later | Manufacturing, life sciences, and sector overlays need domain validation and stricter review |

## Creator and Influencer Expansion

The creator report adds a new non-developer but artifact-heavy category:
creators as small media, sales, analytics, and community operators. The first
eight feasible implementations are `creator-content-engine`,
`creator-brand-deals`, `creator-analytics-reporting`, and
`creator-monetization`, plus `creator-business-ops` and `creator-community`,
plus `creator-reputation-risk` and `creator-ai-production`, because they can be
useful without private platform connectors and produce concrete artifacts:
pillar maps, hook packs, scripts, captions, calendars, repurposing plans,
publishing checks, media kits, pitch emails, sponsorship packages, rights
checklists, sponsor reports, affiliate reports, dashboard specs, offer ladders,
owned-product launch plans, invoice readiness checklists, production ops
briefs, renewal pitches, triage queues, moderation briefs, poll plans, feedback
syntheses, engagement calendars, event prompt plans, reputation risk memos, and
hold/revise/go recommendations, AI media prompt packs, synthetic character
bibles, source provenance notes, and human-review checklists.

Planned follow-on bundles:

- `creator-platform-expansion` and `creator-live-events`: defer until the core
  creator operating loop has stronger real-input validation.

## Recommended 12-Week Path

Roadmap adjustment from the latest memo: the next development loop should add
proof and trust tracks before adding many more role bundles. The existing alpha
bundles remain useful, but future expansion should now pass through evaluation
and security review templates.

### Weeks 1-2: Portfolio Foundation

Goal: make the next bundle expansion predictable.

Deliverables:

- confirm bundle naming and taxonomy
- decide whether to extend `skillsets/*.yaml` with optional metadata
- add lightweight operating-context templates
- define pilot metric fields for bundle docs
- add route coverage scenarios for new bundles

Acceptance criteria:

- new bundle template is documented
- validator still passes with old and new manifests
- release check remains the standard gate

### Weeks 3-4: Support and Success Alpha

Goal: create the first new business bundle with the clearest evidence base.

Initial atomic skills:

- `ticket-triage`
- `reply-drafting`
- `escalation-pack`
- `kb-from-resolution`
- optional later: `qbr-renewal-brief`

Portable context templates:

- `SUPPORT_POLICY.md`
- `ESCALATION_RULES.md`
- `KB_STYLE_GUIDE.md`
- `PRODUCT_GLOSSARY.md`

Pilot metrics:

- median first-response time
- resolutions per hour
- QA review score
- percent of drafts accepted with light edits
- KB article reuse

Safety baseline:

- never send customer replies automatically
- never invent refunds, SLAs, commitments, or policy exceptions
- require approval before account changes or outbound messages

### Weeks 3-5: Engineering Delivery Alpha

Goal: turn existing QA and release strengths into an engineering workflow bundle.

Initial atomic skills:

- `issue-to-plan`
- `pr-review`
- `regression-check`
- `release-risk`
- optional later: `secure-fix-review`

Existing skills to reuse:

- `qa-test-strategy`
- `release-launch-readiness`
- `concise-technical-writing`
- `product-brainstorming-planning`

Pilot metrics:

- time from issue to implementation plan
- accepted-plan rate
- PR review turnaround
- generated tests retained
- escaped defect rate

Safety baseline:

- read repo context first
- do not merge, deploy, or edit protected branches without approval
- flag incomplete logs, tests, or reproduction steps

### Weeks 5-7: Product Research Alpha

Goal: formalize product and research workflows already partly covered.

Initial atomic skills:

- `feedback-synthesis`
- `write-spec`
- reuse `product-brainstorming-planning` for roadmap briefs
- reuse `competitive-market-research` for market scans

Existing skills to reuse:

- `product-brainstorming-planning`
- `customer-research-validation`
- `competitive-market-research`
- `experiment-design-validation`
- `product-analytics-instrumentation`
- `concise-technical-writing`

Pilot metrics:

- time from feedback corpus to draft spec
- PM acceptance rate
- stakeholder revision rounds
- backlog grooming time

Safety baseline:

- separate evidence from recommendation
- do not auto-change roadmap artifacts
- make assumptions and evidence gaps explicit

### Weeks 6-8: Revenue Growth Refinement

Goal: adapt the existing sales-marketing coverage into a sharper
approval-aware growth bundle.

Initial approach:

- compose existing sales, marketing, ABM, pricing, analytics, and experiment
  skills first
- add new atomic skills only after pilot scenarios reveal a concrete gap

Existing skills to reuse:

- `sales-prospecting-outreach`
- `sales-conversion-enablement`
- `marketing-positioning-strategy`
- `content-seo-strategy`
- `paid-media-growth`
- `lifecycle-crm-email`
- `account-based-marketing`

Pilot metrics:

- call-prep time
- approval-to-send time
- reply or meeting-book rate
- percent of drafts approved without rewrite

Safety baseline:

- human approval before outbound sends
- honor consent and compliance constraints
- separate strategic recommendations from platform-specific current facts

### Weeks 8-10: Analytics and Finance Alpha

Goal: add a high-value read-first bundle for analytics, KPI narratives, and
finance close support.

Initial atomic skills:

- `metric-narrative`
- `variance-commentary`
- `finance-close-checklist`

Portable context templates:

- `METRIC_DEFINITIONS.md`
- `DATA_QUALITY_RULES.md`
- `FINANCE_CLOSE.md`
- `REPORTING_GLOSSARY.md`

Pilot metrics:

- time-to-answer for ad hoc questions
- analyst review edits
- commentary turnaround
- reviewer confidence rating

Safety baseline:

- read-only warehouse assumptions by default
- never publish figures externally without reviewer confirmation
- surface data quality assumptions and confidence level

### Weeks 10-12: Hardening and Release Packaging

Goal: make the expanded portfolio usable, measurable, and publishable.

Deliverables:

- route coverage scenarios for each new bundle
- example prompts and before/after examples
- host setup notes for each new bundle where behavior differs
- release notes and README tables generated from `list-skillsets.ps1`
- social preview concepts or screenshots for the top bundles

Acceptance criteria:

- `release-check.ps1` passes
- `gh skill publish --dry-run` passes
- every new bundle has pilot metrics, safety rules, and a dry-run install path
- no new host lock-in in skill or bundle manifests

## Backlog After the First Waves

| Bundle | Reason to wait |
|---|---|
| `owner-operator-os` | Build after the first executive flagship unless small-business demand becomes primary |
| `operating-cadence` | May be a sub-bundle of `executive-command-center` first |
| `board-governance` | Needs board-specific review language and governance examples |
| `finance-strategy` | Should reuse `analytics-finance` until runway/scenario workflows justify a split |
| `people-leadership` | Needs careful policy, privacy, and employment-law boundaries |
| `partnerships-ma` | Needs diligence, negotiation, and integration-risk review gates |
| `crisis-comms` | Needs legal/compliance review requirements for regulated incidents |
| `security-trust` | Higher blast radius and prompt-injection risk |
| `legal-compliance` | Requires jurisdiction and counsel-specific playbooks |
| `vertical-manufacturing` | Physical-world operational risk and domain validation burden |
| `vertical-bio-research` | Specialist validation and connector burden are high |

## Immediate Next Steps

1. Use `docs/evaluation/` to forward-test existing alpha bundles with
   before/after reports.
2. Use `docs/evaluation/v0.2-alpha-validation-plan.md` to collect anonymized
   real-input packets before promoting any alpha bundle.
3. Forward-test `agentops-evaluation` with benchmark, scenario authoring,
   before/after evaluation, prompt regression, and overhead review samples.
4. Forward-test `skill-security-audit` with third-party install, script review,
   publish review, and MCP scope samples.
5. Forward-test `technical-documentation` with README, API docs, release notes,
   changelog, migration, onboarding, and tutorial samples.
6. Forward-test `backend-api` with API contract, schema review, auth flow,
   service boundary, and rate-limit samples.
7. Forward-test `devops-cloud-release` with deployment, CI/container, config,
   rollback, cloud cost, and production readiness samples.
8. Forward-test `quality-testing` with unit/integration, E2E matrix, bug
   reproduction, accessibility/performance, and release-risk samples.
9. Forward-test `data-analytics-bi` with metric/dashboard, funnel/cohort,
   retention, experiment readout, and instrumentation samples.
10. Forward-test `creator-content-engine` with anonymized real creator inputs
   after the initial pillar/calendar, short-form script, repurposing, YouTube
   brief, and publishing checklist scenario pass.
11. Forward-test `creator-brand-deals` with anonymized media kit, rate/package,
   sponsor proposal, negotiation, and recap/renewal inputs after the initial
   scenario pass.
12. Forward-test `creator-analytics-reporting` with anonymized sponsor report,
   watch-time review, audience growth, affiliate performance, experiment
   readout, and dashboard inputs after the initial scenario pass.
13. Forward-test `creator-monetization` with anonymized offer ladder,
   owned-product launch, membership/community pricing, merch margin, affiliate,
   and monetization dashboard inputs after the initial scenario pass.
14. Forward-test `creator-business-ops` with anonymized weekly dashboard,
   sponsor pipeline, invoice readiness, production budget, contractor handoff,
   and asset checklist inputs after the initial scenario pass.
15. Forward-test `creator-community` with anonymized comment/DM queues,
   moderation notes, audience feedback, poll results, engagement plans, and
   event prompts after the initial scenario pass.
16. Forward-test `creator-reputation-risk` with anonymized sponsored posts, AI
   content plans, asset rights notes, sponsor campaign briefs, platform-policy
   questions, and backlash packets after the initial scenario pass.
17. Forward-test `creator-ai-production` with anonymized AI content plans,
   prompt packs, source asset notes, synthetic character concepts, voiceover
   workflows, and batch production briefs after the initial scenario pass.
18. Continue executive and vertical expansion only after the proof and trust
   tracks are working.
19. Keep optional manifest metadata deferred until at least two bundles need the
   same field and one script or doc uses it.

## Open Questions

- Should `sales-marketing` remain as-is, or should it become `revenue-growth`
  with `sales-marketing` kept as an alias or legacy bundle?
- Should `research-validation` become `product-research`, or stay as a broader
  evidence bundle?
- Should `engineering-delivery` and `qa-release` be separate bundles or one
  bundle for the first release?
- Which host should be the first pilot target after Codex: Copilot, Cursor,
  Claude Code, or Gemini CLI?
- Do we want optional manifest metadata now, or only after the next bundle
  document defines the real fields?
