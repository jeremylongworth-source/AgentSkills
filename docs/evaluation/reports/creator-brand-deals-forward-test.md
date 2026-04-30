# Before/After Report: creator-brand-deals

Date: 2026-04-30
Reviewer: Codex
Skill or bundle: `creator-brand-deals`
Scenarios:

- `creator-brand-pitch-media-kit`
- `creator-rate-card-package`
- `creator-sponsor-proposal`
- `creator-negotiation-prep`
- `creator-campaign-recap-renewal`

Source material:

- `tests/scenarios/creator-brand-pitch-media-kit.md`
- `tests/scenarios/creator-rate-card-package.md`
- `tests/scenarios/creator-sponsor-proposal.md`
- `tests/scenarios/creator-negotiation-prep.md`
- `tests/scenarios/creator-campaign-recap-renewal.md`
- `skillsets/creator-brand-deals.yaml`
- `docs/bundles/creator-brand-deals.md`

## Decision

Decision: keep as alpha

Reason: the bundle produces concrete sponsor-facing artifacts while keeping
sends, contract terms, pricing commitments, usage rights, and campaign metrics
under explicit human review. It fills the creator sponsorship gap without
requiring platform connectors or a larger CRM system.

## Target Artifact

Artifact expected: creator sponsorship operating assets
Audience: creators, creator managers, agencies, assistants, and creator-led
businesses
High-risk boundaries: sponsor sends, pricing commitments, contract terms,
usage rights, paid usage, whitelisting, exclusivity, affiliate terms,
performance reporting, invoices, and sponsored publishing

## Acceptance Criteria

- Produces reviewable brand-deal artifacts rather than generic sales advice.
- Routes media kit, rate/package, proposal, negotiation, and recap/renewal
  scenarios to the intended skills.
- Separates verified metrics from assumptions, estimates, and placeholders.
- Flags legal, tax, accounting, contract, rights, disclosure, and platform
  policy review needs.
- Requires approval before external sends, sponsor commitments, or system
  updates.

## Baseline Result

Setup: scenario prompt treated as a generic sponsorship or sales request without
creator-specific routing.

Output summary: likely to generate usable sales copy, but often misses creator
deal mechanics such as usage rights, whitelisting, exclusivity, deliverable
tracking, disclosure notes, and sourced campaign reporting.

What worked: can draft outreach, summarize sponsor fit, and create broad
proposal language.

What failed: less likely to separate content creation fees from usage rights,
avoid unsupported audience claims, include manager/counsel review gates, or
tie renewal pitches to source-backed recap data.

Safety issues: higher risk of inflated metrics, implied legal conclusions,
unsupported ROI claims, and premature commitments.

Reviewer edits required: high for rate cards, rights terms, negotiation prep,
and campaign recaps.

## Skill-Enabled Result

Setup: scenario prompt routed through `creator-brand-deals` with the listed
skills and bundle safety rules.

Output summary: each scenario has a clear primary artifact:

- sponsor pitch plus media kit copy and missing assets
- package and rate-card structure with rights assumptions
- campaign proposal with tracker fields and measurement plan
- negotiation plan with counteroffer points and red flags
- recap report plus renewal pitch from supplied metrics

What improved: skills add creator-specific proof rules, usage-rights questions,
pricing assumptions, approval owners, deliverable statuses, metrics caveats,
and no-send gates.

What regressed: sponsorship workflows become more cautious and review-heavy.
That is the intended posture for alpha because the bundle touches contracts,
rates, public claims, and sponsor relationships.

Safety issues: no blocker found. The bundle should keep verifying current
platform, disclosure, affiliate, paid-media, and monetization rules when exact
tactical guidance matters.

Reviewer edits required: moderate; the creator or manager must supply source
metrics, sponsor goals, contract terms, approved rates, and actual campaign
data.

## Score

| Criterion | Baseline | Skill-enabled | Notes |
|---|---:|---:|---|
| Trigger fit | 2 | 3 | Scenarios route cleanly to sponsor-specific artifacts. |
| Artifact usefulness | 2 | 3 | Bundle covers pitches, kits, packages, proposals, trackers, recaps, and renewals. |
| Correctness and evidence | 1 | 2 | Strong placeholder/evidence separation, but real quality depends on supplied creator metrics and campaign data. |
| Procedural value | 1 | 3 | Adds rights, pricing, tracking, negotiation, and recap steps that generic sales writing may miss. |
| Safety boundaries | 1 | 3 | Strong review gates for legal, financial, contract, rights, sends, and performance claims. |
| Context efficiency | 2 | 2 | Ten atomic skills are justified; references stay short and conditional. |
| Validation behavior | 1 | 2 | Scenario routing is validated; future measured sponsor examples would improve confidence. |
| Vendor neutrality | 2 | 3 | No required CRM, marketplace, payment provider, or social platform. |
| Maintainability | 2 | 3 | Follows current repo structure and concise skill format. |

## Overhead

Extra files loaded: bundle manifest, bundle brief, five scenario files, ten
brand-deal `SKILL.md` files

Extra tools/scripts used: repo validation and release check

Approximate extra turns or time: one evaluation pass

Token or trace link if available: not applicable

## Follow-Up Changes

- Keep `creator-brand-deals` as alpha.
- Forward-test with anonymized real creator media kit and campaign recap inputs
  before promoting beyond alpha.
- Build `creator-analytics-reporting` next if sponsor reports, watch-time
  reviews, affiliate performance, and experiment readouts recur.
- Keep contracts, rights, taxes, accounting, and paid usage review out of final
  advice and inside reviewer-gated checklists.

## Evidence Links

- `tests/scenarios/creator-brand-pitch-media-kit.md`
- `tests/scenarios/creator-rate-card-package.md`
- `tests/scenarios/creator-sponsor-proposal.md`
- `tests/scenarios/creator-negotiation-prep.md`
- `tests/scenarios/creator-campaign-recap-renewal.md`
- `docs/bundles/creator-brand-deals.md`
- `skillsets/creator-brand-deals.yaml`
