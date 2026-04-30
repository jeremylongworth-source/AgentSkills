# Before/After Report: creator-community

Date: 2026-04-30
Reviewer: Codex
Skill or bundle: `creator-community`
Scenarios:

- `creator-comment-dm-triage`
- `creator-community-feedback-synthesis`
- `creator-community-poll-plan`
- `creator-moderation-escalation`
- `creator-community-engagement-plan`
- `creator-community-event-plan`

Source material:

- `tests/scenarios/creator-comment-dm-triage.md`
- `tests/scenarios/creator-community-feedback-synthesis.md`
- `tests/scenarios/creator-community-poll-plan.md`
- `tests/scenarios/creator-moderation-escalation.md`
- `tests/scenarios/creator-community-engagement-plan.md`
- `tests/scenarios/creator-community-event-plan.md`
- `skillsets/creator-community.yaml`
- `docs/bundles/creator-community.md`

## Decision

Decision: keep as alpha

Reason: the bundle adds only two creator-specific community skills and composes
existing support, research, content, and analytics skills. It supports
reviewable community work without becoming a social inbox, moderation bot, or
platform-specific community manager.

## Target Artifact

Artifact expected: creator community operating artifacts
Audience: creators, creator-founders, community managers, creator teams,
agencies, assistants, editors, and managers
High-risk boundaries: social sends, DMs, moderation actions, bans, member role
changes, support/account actions, platform policy, privacy, safety, minors,
sponsor conflicts, legal claims, and crisis/reputation issues

## Acceptance Criteria

- Produces reviewable community artifacts rather than generic engagement advice.
- Routes triage, feedback synthesis, poll, moderation, engagement, and event
  scenarios to intended skills.
- Separates confirmed facts, assumptions, missing context, proposed replies,
  internal notes, moderation rationale, and approval owners.
- Keeps external systems read-only unless the user approves a specific action.
- Requires approval before replies, deletes, bans, mutes, member approvals,
  role changes, reports, rule updates, posts, or sponsor-facing statements.

## Baseline Result

Setup: scenario prompt treated as a generic creator community request without
community-specific routing.

Output summary: likely to produce useful reply ideas or engagement prompts, but
may blur public replies with internal notes and may miss moderation, safety,
support, sponsor, or platform-policy escalation gates.

What worked: can summarize comments and propose generic responses.

What failed: less likely to classify intent, urgency, sentiment, risk, owner,
missing context, moderation rationale, and approval requirements consistently.

Safety issues: higher risk of implying automatic replies, deletions, bans,
policy decisions, or public statements.

Reviewer edits required: moderate to high for high-emotion threads,
moderation-sensitive posts, support/account issues, and sponsor-visible
contexts.

## Skill-Enabled Result

Setup: scenario prompt routed through `creator-community` with two new
community-specific skills and reused support, research, content, and analytics
skills.

Output summary: each scenario has a clear primary artifact:

- comment and DM triage queue
- community feedback synthesis
- poll and learning plan
- moderation escalation brief
- engagement calendar and prompt set
- live event and follow-up plan

What improved: skills add classification fields, review owners, read-only
posture, escalation triggers, separation of public/private notes, and concrete
community artifacts.

What regressed: the bundle is more cautious than a simple response generator.
That is appropriate because community workflows can involve safety, reputation,
privacy, support, and platform-policy risk.

Safety issues: no blocker found. Real community policy, platform context,
thread evidence, and reviewer ownership are still needed before external
action.

Reviewer edits required: moderate; users must provide actual comments, DMs,
policy, sponsor/customer context, platform context, and desired voice.

## Score

| Criterion | Baseline | Skill-enabled | Notes |
|---|---:|---:|---|
| Trigger fit | 2 | 3 | Scenarios route cleanly to community, support, research, content, and analytics workflows. |
| Artifact usefulness | 2 | 3 | Bundle outputs triage queues, moderation briefs, feedback synthesis, polls, engagement plans, and event plans. |
| Correctness and evidence | 1 | 2 | Strong assumption marking; quality depends on supplied community evidence and policies. |
| Procedural value | 1 | 3 | Adds classification, escalation, reviewer ownership, and no-write checks generic advice may skip. |
| Safety boundaries | 1 | 3 | Strong read-only and approval gates for replies, moderation actions, and platform changes. |
| Context efficiency | 2 | 3 | Only two new skills; most community work reuses existing skills. |
| Validation behavior | 1 | 2 | Scenario routing is validated; anonymized real community packets should be used later. |
| Vendor neutrality | 2 | 3 | No required social, Discord, Patreon, Circle, Slack, Reddit, CRM, or support platform. |
| Maintainability | 2 | 3 | Composed bundle avoids unnecessary poll, event, sentiment, and platform micro-skills. |

## Overhead

Extra files loaded: bundle manifest, bundle brief, six scenario files, two new
creator community `SKILL.md` files, and reused support/research/content skill
metadata

Extra tools/scripts used: repo validation and release check

Approximate extra turns or time: one evaluation pass

Token or trace link if available: not applicable

## Follow-Up Changes

- Keep `creator-community` as alpha.
- Forward-test with anonymized real comment/DM queues, moderator notes, poll
  results, and community event inputs before promotion.
- Build `creator-reputation-risk` next only after platform policy, disclosure,
  copyright, brand-safety, AI-labeling, and crisis boundaries are explicit.

## Evidence Links

- `tests/scenarios/creator-comment-dm-triage.md`
- `tests/scenarios/creator-community-feedback-synthesis.md`
- `tests/scenarios/creator-community-poll-plan.md`
- `tests/scenarios/creator-moderation-escalation.md`
- `tests/scenarios/creator-community-engagement-plan.md`
- `tests/scenarios/creator-community-event-plan.md`
- `docs/bundles/creator-community.md`
- `skillsets/creator-community.yaml`
