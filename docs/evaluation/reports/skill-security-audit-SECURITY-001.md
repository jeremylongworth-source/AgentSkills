# Skill Security Review: ai-media-prompt-brief SECURITY-001

Date: 2026-04-30
Reviewer: Codex
Source: `skills/ai-media-prompt-brief`
Version or commit: current workspace
Install path: local repo skill folder

## Summary

Recommendation: approve
Risk level: medium
Reason: `ai-media-prompt-brief` is instruction-only, has no scripts or external
dependencies, and contains explicit gates for rights, consent, provenance,
disclosure, platform policy, sponsor review, generation, and publishing. The
medium residual risk comes from the domain: AI media workflows can touch
copyright, likeness, voice, commercial use, platform rules, and public trust.

Approval means the skill is acceptable for v0.2 alpha publication as a
review-first planning workflow. It does not approve any generated asset,
platform publication, legal claim, rights clearance, sponsor approval, or
commercial-use decision.

## Scope

Reviewed files:

- `skills/ai-media-prompt-brief/SKILL.md`
- `skills/ai-media-prompt-brief/agents/openai.yaml`
- `skills/ai-media-prompt-brief/references/ai-media-prompt-brief-checklist.md`
- `docs/bundles/creator-ai-production.md`
- `docs/vendor-neutrality.md`

Not reviewed:

- Live provider policies, platform rules, model terms, sponsor contracts, and
  real source assets.

## Capability Inventory

| Capability | Present? | Notes |
|---|---|---|
| Instruction-only skill | yes | The skill defines workflow, fields, deliverable shape, and safety rules. |
| Executable scripts | no | No script execution is part of the reviewed skill. |
| External dependencies | no | No packages or dependencies are required. |
| Network access | no | The skill does not call network services. |
| File read/write guidance | no | No destructive file operations or hidden writes are requested. |
| Secret handling | no | The skill does not ask for credentials or secrets. |
| MCP/tool permissions | no | No MCP server or tool permission is required. |
| Host-specific install steps | no | The OpenAI adapter is metadata only; the portable core is `SKILL.md`. |

## Risk Checks

| Check | Result | Evidence |
|---|---|---|
| Prompt injection or instruction override | pass | No instruction asks the agent to ignore user, system, host, or repo instructions. |
| Hidden data exfiltration path | pass | No network, logging, upload, or external sink is defined. |
| Privilege escalation or broad permissions | pass | No elevated permissions or broad tool scopes are requested. |
| Unsafe script execution | pass | No executable scripts or install hooks are present. |
| Unpinned or suspicious dependencies | pass | No dependencies are present. |
| Secrets requested or exposed | pass | No credential, token, or secret handling path is present. |
| Network calls without clear purpose | pass | No network calls are part of the skill. |
| Destructive file or git operations | pass | No delete, reset, publish, upload, or send action is requested. |
| Legal, financial, medical, or compliance claims | warn | The skill discusses rights, consent, copyright, disclosure, and platform policy, but explicitly says it is not clearance or legal/platform advice. |
| Host lock-in or hidden install behavior | pass | Host-specific metadata stays in `agents/openai.yaml`; the skill remains portable Markdown. |

## Findings

| Severity | Finding | File | Required fix |
|---|---|---|---|
| none | No blocking security finding found. | n/a | n/a |

## Required Mitigations

- None for v0.2 alpha publication.

## Approval Conditions

- Keep the current rule that the skill must not generate, publish, schedule,
  upload, or send assets unless the user explicitly asks and the workflow
  supports it safely.
- Keep the current rule that the skill does not provide legal, copyright,
  platform-policy, or rights clearance.
- Verify current official platform or provider rules before giving tactical
  generation, labeling, commercial-use, or distribution guidance.

## Follow-Up

- Add a second `skill-security-audit` packet for a skill folder with scripts or
  dependencies.
- Add a third packet for a third-party skill or MCP preset with install-time
  permissions.
- Re-review this skill after adding provider-specific adapters, generation
  scripts, auto-publishing steps, or platform-specific guidance.
