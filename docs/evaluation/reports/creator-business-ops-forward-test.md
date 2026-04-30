# Before/After Report: creator-business-ops

Date: 2026-04-30
Reviewer: Codex
Skill or bundle: `creator-business-ops`
Scenarios:

- `creator-weekly-ops-dashboard`
- `creator-sponsor-pipeline-review`
- `creator-invoice-readiness`
- `creator-production-budget-review`
- `creator-assistant-contractor-handoff`
- `creator-asset-library-checklist`

Source material:

- `tests/scenarios/creator-weekly-ops-dashboard.md`
- `tests/scenarios/creator-sponsor-pipeline-review.md`
- `tests/scenarios/creator-invoice-readiness.md`
- `tests/scenarios/creator-production-budget-review.md`
- `tests/scenarios/creator-assistant-contractor-handoff.md`
- `tests/scenarios/creator-asset-library-checklist.md`
- `skillsets/creator-business-ops.yaml`
- `docs/bundles/creator-business-ops.md`

## Decision

Decision: keep as alpha

Reason: the bundle adds only two creator-specific skills and composes existing
owner, finance, pipeline, deliverables, docs, rights, and metric skills. It
supports practical creator operations without becoming a CRM, accounting,
storage, project-management, payment, or payroll system.

## Target Artifact

Artifact expected: creator business operations artifacts
Audience: creators, creator-founders, managers, assistants, agencies, editors,
and small creator teams
High-risk boundaries: invoices, accounting, banking, payroll, CRM, payment,
project-management, social, storage, publishing, contractor messages, rights,
employment, contracts, tax, and payment disputes

## Acceptance Criteria

- Produces reviewable ops artifacts rather than generic business advice.
- Routes weekly dashboard, sponsor pipeline, invoice readiness, production
  budget, assistant/contractor handoff, and asset checklist scenarios to
  intended skills.
- Separates confirmed facts, assumptions, missing data, risks, and suggested
  next actions.
- Keeps external systems read-only unless the user approves a specific action.
- Requires approval before invoice sends, sponsor updates, payment reminders,
  contractor messages, task changes, payment actions, asset moves, or system
  writes.

## Baseline Result

Setup: scenario prompt treated as a generic creator operations request without
creator-specific routing.

Output summary: likely to produce a useful checklist, but may miss invoice
handoff readiness, deliverable proof, asset rights, accounting owner, production
capacity, sponsor pipeline hygiene, and explicit no-write boundaries.

What worked: can summarize tasks and create general operating lists.

What failed: less likely to tie operations to sponsor deliverables, cash,
invoice readiness, contractor handoffs, rights-aware asset systems, and weekly
owner actions.

Safety issues: higher risk of inventing invoice/payment status or implying that
system updates, invoice sends, or contractor messages can happen automatically.

Reviewer edits required: moderate to high for invoices, rights, contract terms,
and payment/cash status.

## Skill-Enabled Result

Setup: scenario prompt routed through `creator-business-ops` with two new
creator-specific skills and reused owner, finance, pipeline, docs, and rights
skills.

Output summary: each scenario has a clear primary artifact:

- weekly ops dashboard with metrics, blockers, and actions
- sponsor pipeline review with follow-up and deliverable risks
- invoice readiness checklist with proof and missing fields
- production ops budget review with variance and cash notes
- assistant/contractor handoff brief with acceptance criteria
- asset-library checklist with rights and restricted-asset notes

What improved: skills add source/evidence checks, read-only posture, review
owners, invoice handoff fields, production dependencies, and asset/rights
boundaries.

What regressed: the bundle is more procedural than a simple task list. That is
appropriate because creator ops involves invoices, rights, contractors, and
external systems.

Safety issues: no blocker found. Real ops data and reviewer ownership are still
needed before external action.

Reviewer edits required: moderate; users must provide source records, links,
approval state, terms, rights data, contractor details, and cash context.

## Score

| Criterion | Baseline | Skill-enabled | Notes |
|---|---:|---:|---|
| Trigger fit | 2 | 3 | Scenarios route cleanly to ops, invoice, production, pipeline, and asset workflows. |
| Artifact usefulness | 2 | 3 | Bundle outputs dashboards, pipeline reviews, readiness checks, handoffs, and asset checklists. |
| Correctness and evidence | 1 | 2 | Strong assumption marking; quality depends on supplied operational records. |
| Procedural value | 1 | 3 | Adds handoff, proof, rights, finance, and no-write checks generic task lists may skip. |
| Safety boundaries | 1 | 3 | Strong read-only and approval gates for invoices, systems, payments, contractors, and assets. |
| Context efficiency | 2 | 3 | Only two new skills; most operations work reuses existing skills. |
| Validation behavior | 1 | 2 | Scenario routing is validated; real ops packets should be used later. |
| Vendor neutrality | 2 | 3 | No required CRM, accounting, storage, payment, project-management, or social platform. |
| Maintainability | 2 | 3 | Composed bundle avoids unnecessary CRM, invoice, asset, and contractor micro-skills. |

## Overhead

Extra files loaded: bundle manifest, bundle brief, six scenario files, two new
creator ops `SKILL.md` files, and reused owner/finance/pipeline/docs skill
metadata

Extra tools/scripts used: repo validation and release check

Approximate extra turns or time: one evaluation pass

Token or trace link if available: not applicable

## Follow-Up Changes

- Keep `creator-business-ops` as alpha.
- Forward-test with anonymized real sponsor pipeline, invoice packet,
  production budget, asset folder, and contractor handoff inputs before
  promotion.
- Build `creator-community` next only after audience comments, DMs, moderation,
  polls, events, and feedback workflows recur.

## Evidence Links

- `tests/scenarios/creator-weekly-ops-dashboard.md`
- `tests/scenarios/creator-sponsor-pipeline-review.md`
- `tests/scenarios/creator-invoice-readiness.md`
- `tests/scenarios/creator-production-budget-review.md`
- `tests/scenarios/creator-assistant-contractor-handoff.md`
- `tests/scenarios/creator-asset-library-checklist.md`
- `docs/bundles/creator-business-ops.md`
- `skillsets/creator-business-ops.yaml`
