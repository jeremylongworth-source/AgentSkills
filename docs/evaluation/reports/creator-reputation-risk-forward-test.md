# Before/After Report: creator-reputation-risk

Date: 2026-04-30
Reviewer: Codex
Skill or bundle: `creator-reputation-risk`
Scenarios:

- `creator-sponsored-post-disclosure-review`
- `creator-ai-content-labeling-review`
- `creator-copyright-rights-risk-review`
- `creator-brand-safety-campaign-review`
- `creator-controversy-response-brief`
- `creator-platform-policy-risk-check`

Source material:

- `tests/scenarios/creator-sponsored-post-disclosure-review.md`
- `tests/scenarios/creator-ai-content-labeling-review.md`
- `tests/scenarios/creator-copyright-rights-risk-review.md`
- `tests/scenarios/creator-brand-safety-campaign-review.md`
- `tests/scenarios/creator-controversy-response-brief.md`
- `tests/scenarios/creator-platform-policy-risk-check.md`
- `skillsets/creator-reputation-risk.yaml`
- `docs/bundles/creator-reputation-risk.md`

## Decision

Decision: keep as alpha

Reason: the bundle adds one creator-specific review skill and composes existing
publishing, rights, AI governance, community, escalation, risk, and sponsor
skills. It produces review-only risk memos without becoming legal advice,
crisis automation, platform monitoring, or trust-and-safety enforcement.

## Target Artifact

Artifact expected: creator reputation risk review artifacts
Audience: creators, creator-founders, managers, community managers, agencies,
brand-partnership leads, assistants, editors, and creator teams
High-risk boundaries: legal, compliance, copyright, platform policy, public
apologies, crisis response, moderation actions, sponsor conflict, privacy,
minors, harassment, doxxing, threats, AI likeness/voice, public backlash, and
publishing decisions

## Acceptance Criteria

- Produces reviewable risk artifacts rather than legal or crisis advice.
- Routes disclosure, AI-labeling, copyright/rights, brand-safety, controversy,
  and platform-policy scenarios to intended skills.
- Separates confirmed facts, assumptions, missing evidence, public copy,
  internal notes, risk rationale, escalation notes, and approval owners.
- Keeps external systems read-only unless the user approves a specific action.
- Requires approval before publishing, replies, deletes, bans, reports, apology
  statements, sponsor contacts, platform contacts, or rule/settings changes.

## Baseline Result

Setup: scenario prompt treated as a generic creator risk request without
reputation-specific routing.

Output summary: likely to produce general cautions and copy suggestions, but
may miss the structured separation between disclosure, rights, AI labeling,
platform policy, brand safety, public response, escalation, and missing facts.

What worked: can identify obvious reputation concerns and suggest softer
language.

What failed: less likely to preserve review-only posture, avoid legal/platform
conclusions, name approval owners, or route to rights, AI, community, and
escalation skills.

Safety issues: higher risk of implying legal clearance, fair use, sufficient
disclosure, platform compliance, or public apology readiness.

Reviewer edits required: high for legal, disclosure, copyright, platform,
sponsor, AI-likeness, or crisis-sensitive content.

## Skill-Enabled Result

Setup: scenario prompt routed through `creator-reputation-risk` with one new
review skill and reused publishing, rights, AI governance, community,
escalation, risk, and sponsor skills.

Output summary: each scenario has a clear primary artifact:

- sponsored post disclosure review
- AI content labeling risk memo
- copyright and usage-rights risk list
- brand-safety campaign review
- controversy response brief
- platform-policy risk check

What improved: skills add risk checklists, hold/revise/go recommendations,
review owners, escalation triggers, and explicit disclaimers against legal,
copyright, disclosure, platform, or brand-safety conclusions.

What regressed: the bundle is cautious and may ask for current platform or legal
review before giving tactical advice. That is appropriate for reputation and
compliance-sensitive creator work.

Safety issues: no blocker found. Real policies, sponsor terms, platform context,
asset ownership, AI provenance, community evidence, and reviewer ownership are
still needed before external action.

Reviewer edits required: moderate to high; users must provide source assets,
contracts or rights notes, platform context, sponsor terms, community evidence,
and the desired public voice.

## Score

| Criterion | Baseline | Skill-enabled | Notes |
|---|---:|---:|---|
| Trigger fit | 2 | 3 | Scenarios route cleanly to reputation, publishing, rights, AI, community, sponsor, and escalation workflows. |
| Artifact usefulness | 2 | 3 | Bundle outputs risk memos, checklists, response briefs, and hold/revise/go recommendations. |
| Correctness and evidence | 1 | 2 | Strong assumption marking; quality depends on supplied policies, rights, and evidence. |
| Procedural value | 1 | 3 | Adds disclosure, rights, AI, policy, brand-safety, escalation, and no-write checks. |
| Safety boundaries | 1 | 3 | Strong review-only gates for legal, platform, copyright, public response, and publishing decisions. |
| Context efficiency | 2 | 3 | Only one new skill; most reputation work reuses existing skills. |
| Validation behavior | 1 | 2 | Scenario routing is validated; anonymized real risk packets should be used later. |
| Vendor neutrality | 2 | 3 | No required social, platform, monitoring, legal, CRM, or sponsor connector. |
| Maintainability | 2 | 3 | Composed bundle avoids stale platform-specific micro-skills. |

## Overhead

Extra files loaded: bundle manifest, bundle brief, six scenario files, one new
creator reputation `SKILL.md` file, and reused publishing/rights/community/AI
skill metadata

Extra tools/scripts used: repo validation and release check

Approximate extra turns or time: one evaluation pass

Token or trace link if available: not applicable

## Follow-Up Changes

- Keep `creator-reputation-risk` as alpha.
- Forward-test with anonymized real sponsored posts, AI content plans, asset
  rights notes, sponsor campaign briefs, and comment backlash packets before
  promotion.
- Build `creator-ai-production` next only as a draft-first production planning
  bundle with strong disclosure, likeness, voice, provenance, and rights
  boundaries.

## Evidence Links

- `tests/scenarios/creator-sponsored-post-disclosure-review.md`
- `tests/scenarios/creator-ai-content-labeling-review.md`
- `tests/scenarios/creator-copyright-rights-risk-review.md`
- `tests/scenarios/creator-brand-safety-campaign-review.md`
- `tests/scenarios/creator-controversy-response-brief.md`
- `tests/scenarios/creator-platform-policy-risk-check.md`
- `docs/bundles/creator-reputation-risk.md`
- `skillsets/creator-reputation-risk.yaml`
