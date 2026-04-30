# Before and After Agent Behavior

These examples show how AgentSkills should change agent behavior.

## Browser Game Build

Prompt:

```text
Build a small Phaser browser game and prepare it for itch.io.
```

Without AgentSkills, the agent may jump straight to implementation and miss
publishing, browser QA, accessibility, pricing, or release checks.

With the `game-dev` or `html5-game-publishing` skillset, expected routing is:

- `game-skill-orchestration` frames the player-facing goal and deliverables
- `game-phaser-development` handles Phaser implementation
- `game-sprite-design` covers 2D asset needs
- `game-ui-design` covers HUD and menu flow
- `itch-html5-game-publishing` covers packaging and itch.io readiness
- `qa-test-strategy` and `release-launch-readiness` cover release checks

Expected output starts with a brief plan, then implements and verifies the game.

## Executive Weekly Brief

Prompt:

```text
Create a one-page weekly CEO brief from these metrics, customer issues, delivery risks, and open actions.
```

Without AgentSkills, the agent may produce generic leadership advice or blend
facts, assumptions, risks, and actions together.

With `executive-command-center`, expected routing is:

- `executive-briefing` creates the brief structure and priority narrative
- `metric-narrative` explains metric movement without inventing figures
- `risk-register` identifies risks, owners, mitigations, and escalation paths
- `action-tracker` converts open items into owner follow-up

Expected output is a concrete executive artifact with facts, assumptions,
decisions, risks, and owner actions separated.

## Founder Investor Update

Prompt:

```text
Draft a monthly investor update from these traction notes, runway notes, product progress, risks, and asks.
```

Without AgentSkills, the agent may overstate progress, blur internal notes into
sendable copy, or miss financial and legal review needs.

With `founder-fundraising-ir`, expected routing is:

- `investor-update` drafts the update and investor asks
- `metric-narrative` explains supplied metrics without inventing numbers
- `executive-briefing` keeps the update concise and decision-ready
- `risk-register` flags risks requiring review
- `concise-technical-writing` tightens investor-facing language

Expected output separates sendable text, internal notes, missing evidence, and
required founder, finance, or counsel review.

## AI Use Case Portfolio

Prompt:

```text
Build an AI use-case portfolio and choose the safest pilots to run first.
```

Without AgentSkills, the agent may suggest generic AI ideas without risk,
governance, owner, or measurement discipline.

With `ai-transformation-governance`, expected routing is:

- `ai-use-case-portfolio` maps and scores use cases
- `ai-pilot-selection` selects pilots with hypotheses and decision rules
- `ai-risk-register` identifies risks, controls, and owners
- `ai-governance-checklist` defines gates before scale

Expected output separates opportunity, evidence, assumptions, governance gaps,
pilot metrics, and approvals.

## Owner Dashboard

Prompt:

```text
Create a monthly owner dashboard and cash action list from these business notes.
```

Without AgentSkills, the agent may provide generic small-business advice or
make unsupported finance assumptions.

With `owner-operator-os`, expected routing is:

- `owner-dashboard` creates the practical business snapshot
- `cash-flow-triage` identifies cash pressure and missing data
- `variance-commentary` explains supplied changes and caveats
- `action-tracker` turns decisions into owner follow-up

Expected output separates confirmed data, assumptions, missing inputs, review
needs, and owner actions.

## Operating Cadence

Prompt:

```text
Turn these leadership updates into a weekly agenda with OKR status, decisions, risks, and owner actions.
```

Without AgentSkills, the agent may summarize notes without preserving decision
ownership or follow-through.

With `operating-cadence`, expected routing is:

- `executive-briefing` prepares the agenda and operating narrative
- `decision-memo` captures decisions and tradeoffs
- `risk-register` tracks escalations and dependencies
- `action-tracker` assigns owners and follow-up

Expected output separates metrics, OKRs, decisions, risks, escalations, and
actions.

## React Performance Audit

Prompt:

```text
Audit this Next.js app for slow interactions and production readiness.
```

Without AgentSkills, the agent may give generic performance advice.

With `frontend-product`, expected routing is:

- `react-next-performance-optimization` checks rendering, bundle, caching, and
  Core Web Vitals risk
- `visual-ui-ux-audit` uses screenshots when UI evidence is needed
- `tailwind-design-system` checks utility consistency when Tailwind is present
- `qa-test-strategy` defines verification coverage

Expected output includes concrete file references, measurable risks, and a
verification plan.

## Engineering Issue Plan

Prompt:

```text
Turn this bug report into an implementation plan and identify regression risk.
```

Without AgentSkills, the agent may jump into code changes before clarifying
scope, acceptance criteria, or the release gate.

With `engineering-delivery`, expected routing is:

- `issue-to-plan` scopes the task and defines acceptance criteria
- `regression-check` maps changed behavior to verification coverage
- `qa-test-strategy` broadens risk-based test planning
- `release-risk` flags rollout, rollback, and production readiness concerns

Expected output separates facts, assumptions, implementation steps, tests,
release risk, and approval needs.

## Product Feedback to PRD

Prompt:

```text
Synthesize this feedback corpus into a PRD and propose how we should validate it.
```

Without AgentSkills, the agent may blend evidence, assumptions, and
recommendations into one generic product brief.

With `product-research`, expected routing is:

- `feedback-synthesis` clusters raw feedback into themes and confidence
- `write-spec` turns the decision into requirements and acceptance criteria
- `customer-research-validation` identifies evidence gaps
- `experiment-design-validation` defines validation and decision rules
- `product-analytics-instrumentation` adds measurement needs

Expected output separates evidence from assumptions, then produces a reviewed
spec with validation and analytics coverage.

## KPI Narrative

Prompt:

```text
Explain why activation dropped this week and draft a metric narrative for review.
```

Without AgentSkills, the agent may invent causes or blur data caveats into a
confident executive summary.

With `analytics-finance`, expected routing is:

- `metric-narrative` explains the metric movement with confidence and caveats
- `variance-commentary` separates actuals, baselines, and drivers
- `product-analytics-instrumentation` checks metric definitions and tracking
- `marketing-analytics-attribution` checks funnel or channel context when needed

Expected output separates observed facts, likely drivers, assumptions, data
quality caveats, and follow-up checks.

## GTM Plan

Prompt:

```text
Create a launch plan for a B2B SaaS analytics product.
```

Without AgentSkills, the agent may produce a generic marketing checklist.

With `sales-marketing` or `revenue-growth`, expected routing is:

- `growth-strategy-orchestration` frames the GTM system
- `marketing-positioning-strategy` defines ICP, category, and value props
- `customer-research-validation` identifies evidence gaps
- `competitive-market-research` handles market and competitor evidence
- `content-seo-strategy`, `paid-media-growth`, and
  `lifecycle-crm-email` shape channel execution when relevant

Expected output separates strategy, assumptions, validation needs, and execution
steps.

## Support Ticket Triage

Prompt:

```text
Triage this customer ticket, decide whether to escalate, and draft a reply for review.
```

Without AgentSkills, the agent may answer directly, miss escalation evidence,
or blur internal assumptions into customer-facing copy.

With `support-success`, expected routing is:

- `ticket-triage` classifies issue type, severity, impact, and missing facts
- `escalation-pack` prepares owner handoff when the issue needs review
- `reply-drafting` writes a customer-safe draft without sending it
- `concise-technical-writing` tightens the final reply or handoff

Expected output separates triage notes, internal assumptions, escalation needs,
and the customer-facing draft.

## Skill Authoring

Prompt:

```text
Improve this skill so it triggers reliably and is easier to validate.
```

Without AgentSkills, the agent may edit wording without testing trigger
behavior.

With `llm-skill-authoring`, expected routing is:

- `skill-evaluation-iteration` defines realistic test scenarios
- `concise-technical-writing` tightens instructions
- local validation confirms required skill structure

Expected output includes the changed files and the validation commands run.
