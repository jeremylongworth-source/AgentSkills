# Creator Skillsets Roadmap

AgentSkills should support creators as operators, not just posters. A modern
creator often runs a small media company: content studio, audience community,
sales channel, brand partner, product launcher, and analytics function.

Sources reviewed on 2026-04-30:

- [Goldman Sachs creator economy outlook](https://www.goldmansachs.com/insights/articles/the-creator-economy-could-approach-half-a-trillion-dollars-by-2027)
- [Collabstr 2025 influencer marketing report](https://collabstr.com/2025-influencer-marketing-report)
- [IAB 2025 creator economy ad spend report](https://www.iab.com/news/creator-economy-ad-spend-to-reach-37-billion-in-2025-growing-4x-faster-than-total-media-industry-according-to-iab/)
- [Influencer definition and transparency context](https://en.wikipedia.org/wiki/Influencer)
- [Vogue AI consumer perception survey](https://www.vogue.com/article/you-cannot-trust-a-machine-the-ai-consumer-perception-survey)
- [Time reporting on AI influencers](https://time.com/7329699/ai-influencers-tiktok-granny-spills/)

## Strategic Read

Creator workflows fit AgentSkills because they are repetitive, artifact-heavy,
and reviewable:

- idea -> hook -> script -> production -> publishing
- publishing -> engagement -> analytics -> sponsor report
- attention -> monetization -> operations -> reputation protection

This category expands AgentSkills beyond developer and executive workflows
without abandoning the current portable, artifact-first model.

## Planned Creator Bundles

| Bundle | Status | Main job | Best output |
|---|---|---|---|
| `creator-content-engine` | alpha | Turn ideas into publishable content | 30-day content calendar |
| `creator-brand-deals` | alpha | Win and manage sponsorships | media kit and campaign proposal |
| `creator-analytics-reporting` | alpha | Prove what worked | sponsor campaign report |
| `creator-community` | alpha | Manage audience relationships | community engagement plan |
| `creator-monetization` | alpha | Build owned revenue | offer ladder |
| `creator-business-ops` | alpha | Run the creator business | weekly creator ops dashboard |
| `creator-reputation-risk` | alpha | Protect trust | reputation risk checklist |
| `creator-ai-production` | alpha | Use AI safely in production | AI content workflow |
| `creator-platform-expansion` | defer | Expand across channels | platform expansion plan |
| `creator-live-events` | defer | Move into events and IRL formats | event launch plan |

## Build Order

### Phase 1: Core Creator Loop

1. `creator-content-engine` - alpha
2. `creator-brand-deals` - alpha
3. `creator-analytics-reporting` - alpha

Reason: these cover create, sell, and prove.

### Phase 2: Business Maturity

4. `creator-monetization` - alpha
5. `creator-business-ops` - alpha
6. `creator-community` - alpha

Reason: these turn attention into a repeatable business.

### Phase 3: Trust and Advanced Production

7. `creator-reputation-risk` - alpha
8. `creator-ai-production` - alpha
9. `creator-platform-expansion`
10. `creator-live-events`

Reason: these need stronger platform-specific freshness, disclosure, copyright,
and reputation boundaries.

## Safety Rules

- Do not promise virality, reach, revenue, sponsor acceptance, or algorithmic
  outcomes.
- Verify current platform requirements, ad disclosure rules, format limits, and
  monetization rules when tactical details matter.
- Require human approval before publishing posts, sending sponsor pitches,
  making public apology/crisis statements, or changing monetization offers.
- Avoid copyright infringement, undisclosed sponsorships, deceptive AI content,
  fake scarcity, fake audience metrics, and fabricated testimonials.
- Treat legal, tax, accounting, employment, platform policy, and contract
  outputs as workflow support only, requiring professional review.

## Reuse Map

| Existing bundle | Creator use |
|---|---|
| `sales-marketing` and `revenue-growth` | brand deals, offers, campaigns |
| `data-analytics-bi` | creator analytics and sponsor reporting |
| `owner-operator-os` | creator business operations |
| `technical-documentation` | media kits, briefs, creator docs |
| `skill-security-audit` | AI and platform trust review |
| `quality-testing` | publishing checklists and content QA |
| `ai-transformation-governance` | AI production governance |

## Immediate Next Step

Forward-test `creator-content-engine`, `creator-brand-deals`, and
`creator-analytics-reporting`, and `creator-monetization` with anonymized real
creator inputs. Forward-test `creator-business-ops` with anonymized sponsor
pipeline, invoice readiness, production handoff, asset checklist, and weekly ops
inputs, forward-test `creator-community` with anonymized comment/DM queues,
moderation notes, poll results, and event inputs, and forward-test
`creator-reputation-risk` with anonymized sponsored posts, AI content plans,
asset rights notes, sponsor campaign briefs, and backlash packets, and
forward-test `creator-ai-production` with anonymized AI content plans, prompt
packs, source asset notes, synthetic character concepts, and voiceover
workflows before building platform-expansion or live/event bundles.
