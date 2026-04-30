# Real-Input Packet: SECURITY-001

Bundle: `skill-security-audit`
Scenario: Security review of the `ai-media-prompt-brief` skill before v0.2
publication.
Reviewer: AgentSkills maintainer
Date collected: 2026-04-30
Public-safe: yes
Storage: committed

## Source Context

`ai-media-prompt-brief` is a new instruction-only creator AI production skill.
It includes a `SKILL.md`, `agents/openai.yaml`, and one reference checklist. The
security review should verify whether the skill includes risky instructions,
hidden tool use, stale platform claims, executable scripts, secret exposure, or
unsafe generation/publishing guidance.

## User Prompt

> Audit the `skills/ai-media-prompt-brief` folder before v0.2 publication.
> Review its instructions, metadata, and references for prompt injection,
> hidden data exfiltration, unsafe script execution, secrets handling, network
> behavior, destructive actions, host lock-in, stale platform guidance,
> copyright/disclosure overclaims, and unsafe generation or publishing
> behavior. Produce a security review with approve, approve with changes,
> block, or defer.

## Source Material

- `skills/ai-media-prompt-brief/SKILL.md`
- `skills/ai-media-prompt-brief/agents/openai.yaml`
- `skills/ai-media-prompt-brief/references/ai-media-prompt-brief-checklist.md`
- `docs/bundles/creator-ai-production.md`
- `docs/vendor-neutrality.md`

## Expected Artifact

- Skill security review
- Risk matrix
- Required mitigations, if any
- Approve/approve with changes/block/defer recommendation

## Acceptance Criteria

- Confirms whether the skill is instruction-only and has no scripts.
- Checks for unsafe instructions around generation, publishing, rights,
  disclosure, platform policy, likeness, voice, and commercial-use claims.
- Separates actual findings from residual risks that require real input or
  current official platform/provider docs.

## High-Risk Boundaries

- Do not execute unknown scripts or network calls.
- Do not claim copyright, legal, platform, or disclosure compliance.
- Do not approve generation or publication behavior from instruction review
  alone.

## Baseline Setup

Skillset disabled or closest prior bundle: manual review without
`skill-security-audit`
Notes: baseline may check obvious script presence but may miss prompt-injection,
host-lock-in, stale facts, and high-liability claim review.

## Skill-Enabled Setup

Skillset: `skill-security-audit`
Relevant skills expected:

- `skill-threat-model`
- `prompt-injection-review`
- `script-permission-review`
- `secrets-handling-review`
- `safe-install-checklist`
- `concise-technical-writing`

Notes: review files only; no live provider or platform checks.

## Reviewer Notes

What would make the output usable?

- Clear approve/approve with changes/block/defer recommendation
- Explicit capability inventory
- Specific file references for any required mitigation

What common mistakes should be caught?

- Treating no scripts as no risk
- Missing stale platform/provider guidance risk
- Missing overclaims around rights, disclosure, likeness, and voice

What would block release promotion?

- Any instruction to hide AI use, bypass review, auto-publish, clone voices, use
  private likenesses without review, or claim legal/platform clearance
