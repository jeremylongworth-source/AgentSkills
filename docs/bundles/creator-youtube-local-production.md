# Creator YouTube Local Production Bundle Brief

## Problem

Creators need a repeatable way to turn a curated topic backlog into YouTube
video packages without relying on cloud editing or automatic publishing. The
workflow has to produce scripts, assets, render manifests, local FFMPEG exports,
validation notes, metadata drafts, and publishing checks while keeping factual
claims, rights, AI disclosure, and upload approval human-reviewed.

## Target User

Creator-founders, YouTube operators, editors, channel producers, technical
creators, educators, solo builders, and small creator teams producing recurring
narrated explainer videos from a topic backlog.

## Included Skills

- `content-pillars`: define channel promise, topic lanes, recurring series, and
  what not to cover.
- `content-calendar`: plan weekly batches, backlog status, review gates, and
  production cadence.
- `video-script`: create scripts, voiceover, storyboard beats, visual notes,
  CTAs, and cutdown opportunities.
- `thumbnail-title-brief`: produce truthful title packs and thumbnail concepts.
- `ai-media-prompt-brief`, `ai-video-prompt-pack`, and
  `social-asset-production`: plan generated or assembled visuals, b-roll,
  thumbnail assets, prompt briefs, and source-asset constraints.
- `local-video-assembly`: create FFMPEG render manifests, assemble local
  video/audio/caption packages, export MP4 drafts, and validate with `ffprobe`.
- `creator-production-ops-brief`: organize owners, source assets, dependencies,
  batch handoffs, and weekly capacity.
- `publishing-checklist`, `usage-rights-checklist`, and
  `creator-reputation-risk-review`: review metadata, captions, rights,
  provenance, AI labeling, brand safety, and hold/revise/go decisions.
- `concise-technical-writing`: tighten briefs, metadata drafts, reviewer notes,
  and handoff summaries.

## Context Files

- `TOPIC_BACKLOG.md` or `TOPIC_BACKLOG.csv`: `id`, `topic`, `audience`,
  `promise`, `angle`, `source_notes`, `target_length`, `status`, `risk_flags`,
  and `review_owner`.
- `CHANNEL_PILLARS.md`: audience promise, topic lanes, recurring formats,
  proof points, boundaries, and avoid list.
- `EPISODE_PACKAGE.md`: script, storyboard, voiceover, asset list, title and
  thumbnail brief, metadata draft, review status, and open issues.
- `RENDER_MANIFEST.json`: scene order, durations, source files, captions,
  audio, output profile, and validation expectations.
- `RIGHTS_AND_DISCLOSURE.md`: source provenance, license notes, AI assistance,
  synthetic-media questions, sponsor/affiliate flags, and reviewer decisions.
- `FFPROBE.txt` and `REVIEW_NOTES.md`: export validation, quality issues,
  missing assets, and go/revise/hold recommendation.

## MCP Preset Intent

Use documentation research for current YouTube, platform, disclosure, caption,
upload, encoding, or provider rules when exact tactical guidance materially
affects a package. Keep YouTube Studio, publishing tools, social accounts,
storage, analytics, sponsor systems, and generation providers read-only unless
the user explicitly approves a specific action.

## Safety Rules

- Do not publish, upload, schedule, mark approved, contact sponsors, or change
  channel settings without explicit human approval.
- Do not claim YouTube compliance, disclosure sufficiency, copyright clearance,
  sponsor approval, platform safety, or commercial-use permission.
- Do not fabricate facts, source notes, audience metrics, personal experience,
  provenance, licenses, captions, transcripts, or AI/tool settings.
- Hold videos with unclear rights, missing source review, unresolved claim
  checks, synthetic-media disclosure questions, broken audio/captions, or
  misleading title-thumbnail packaging.
- Require human review for sponsored, affiliate, AI-generated, regulated,
  legal, medical, financial, political, crisis, or reputation-sensitive videos.

## Pilot Metrics

- Operational: time from backlog topic to complete local episode package.
- Quality: creator/editor revision rate on scripts, manifests, captions, and
  final MP4 exports.
- Reliability: percent of exports passing `ffprobe`, caption, and audio-sync
  checks on the first reviewed render.
- Trust: percent of packages with complete rights, provenance, disclosure, and
  factual-claim review notes before upload.

## Acceptance Criteria

- The bundle installs with a dry run.
- Given one backlog topic, the workflow produces a complete episode package
  with script, storyboard, voiceover text, render manifest, captions, title and
  thumbnail brief, publishing checklist, `final.mp4`, `FFPROBE.txt`, and review
  notes.
- `ffprobe` confirms video stream, audio stream, duration, resolution, frame
  rate, and expected codecs; captions are readable and synced.
- Publishing review returns `go`, `revise`, or `hold`.
- Upload, scheduling, sponsor, rights, synthetic-media disclosure, and
  platform-policy decisions remain human-reviewed.
