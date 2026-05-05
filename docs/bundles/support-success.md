# Support Success Bundle Brief

## Problem

Support and customer success teams need agents to help triage tickets, draft
safe replies, prepare escalations, turn resolutions into reusable knowledge, and
review account health without sending messages or changing accounts
automatically.

## Target User

Support managers, support engineers, customer success managers, founders, and
small teams handling customer issues.

## Included Skills

- `ticket-triage`: classify support requests, severity, customer impact, and
  next owner.
- `reply-drafting`: draft customer-safe replies using supplied policy and
  product context.
- `escalation-pack`: prepare concise escalation handoffs for engineering,
  billing, security, or leadership review.
- `kb-from-resolution`: turn resolved issues into reviewable knowledge base
  articles.
- `customer-health-review`: prepare account health reviews, QBR briefs,
  adoption plans, renewal risk summaries, and customer success action plans.
- `customer-research-validation`: synthesize recurring ticket themes into
  customer evidence.
- `retention-analysis`: define or interpret retention, churn, renewal, and
  account engagement signals.
- `product-analytics-instrumentation`: define support telemetry and quality
  signals.
- `concise-technical-writing`: tighten replies, summaries, and KB articles.

## Context Files

- `SUPPORT_POLICY.md`: support scope, SLAs, refund rules, account-change rules,
  and promises the agent may or may not make.
- `ESCALATION_RULES.md`: severity levels, owners, paging rules, and required
  escalation evidence.
- `KB_STYLE_GUIDE.md`: article style, structure, audience, and review process.
- `PRODUCT_GLOSSARY.md`: product names, feature names, plan names, and approved
  terminology.
- `CUSTOMER_HEALTH_CONTEXT.md`: account health inputs, promised outcomes,
  review rules, and approval owners.

## MCP Preset Intent

Use documentation research when product docs or public API behavior need to be
verified. Keep customer systems read-only by default.

## Safety Rules

- Draft-first: never send a customer reply automatically.
- Read-first: never change accounts, billing, entitlements, subscriptions, or
  support records without approval.
- Do not invent refunds, SLAs, policy exceptions, commitments, incident status,
  security claims, or product behavior.
- Do not invent usage, renewal terms, contract facts, customer quotes, health
  scores, or account outcomes.
- Escalate when policy is missing, customer impact is unclear, legal/security
  risk appears, or the requested action affects money, access, or data.

## Pilot Metrics

- Operational: median first-response draft time.
- Quality: reviewer QA score and correction rate.
- Adoption: percentage of drafts, health reviews, or KB articles accepted with
  light edits.
- Economic: resolved conversations, reusable KB articles, or account-review
  prep time saved per support/success hour.

## Acceptance Criteria

- The bundle installs with a dry run.
- A support ticket scenario routes to triage, reply drafting, escalation, and
  KB skills.
- Account health scenarios route to customer health, retention, customer
  evidence, analytics, and writing skills.
- Reply drafts separate customer-facing copy from internal assumptions.
- Escalation packs include severity, impact, evidence, owner, and requested
  decision.
- KB drafts include audience, symptoms, cause, resolution, and verification.
- Account reviews include health signals, missing evidence, risks, next actions,
  and customer-facing review gates.
