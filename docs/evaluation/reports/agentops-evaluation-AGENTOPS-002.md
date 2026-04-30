# Before/After Report: agentops-evaluation AGENTOPS-002

Date: 2026-04-30
Reviewer: Codex
Skill or bundle: `agentops-evaluation`
Packet: `AGENTOPS-002`

Source material:

- `docs/evaluation/packets/AGENTOPS-002-skill-security-audit.md`
- `docs/evaluation/packets/SECURITY-001-ai-media-prompt-brief.md`
- `docs/evaluation/packets/SECURITY-002-local-install-mcp.md`
- `docs/evaluation/reports/skill-security-audit-SECURITY-001.md`
- `docs/evaluation/reports/skill-security-audit-SECURITY-002.md`
- `docs/bundles/skill-security-audit.md`
- `docs/evaluation/security-review-template.md`
- `docs/evaluation/skill-quality-rubric.md`

## Decision

Decision: keep as alpha

Reason: `skill-security-audit` produced usable approval decisions for both an
instruction-only skill and a higher-risk installer/MCP layer. The bundle caught
script, file-write, MCP package-execution, host-adapter, and overclaim risks
without requiring a vendor-specific security platform. It still needs third-
party and scripted-skill evidence before promotion beyond alpha.

## Target Artifact

Artifact expected: before/after evaluation of `skill-security-audit` across
`SECURITY-001` and `SECURITY-002`.
Audience: skill authors, maintainers, security reviewers, and users installing
third-party skills.
High-risk boundaries: do not claim third-party packages, live MCP behavior,
private environments, or future installer changes are safe from local file
review alone.

## Acceptance Criteria

- Compare instruction-only security review and installer/MCP security review.
- Score whether the bundle catches hidden instruction, script, install, MCP,
  secrets, host lock-in, and approval-boundary risks.
- Separate mitigated findings from residual risks.
- Require at least one third-party or scripted-skill packet before promotion.

## Baseline Result

Setup: ad hoc manual review of the two security packets without the
`skill-security-audit` workflow.

Output summary: likely to notice that `ai-media-prompt-brief` has no scripts
and that the installer writes files. Less likely to produce a capability
inventory, risk matrix, approval conditions, residual-risk list, and mitigation
status.

What worked: obvious script presence and dry-run behavior are visible from the
source files.

What failed: baseline review can miss that MCP snippets are later package
execution, that "no scripts" does not mean "no risk", and that Codex installer
behavior should be framed as an adapter rather than the portable contract.

Safety issues: medium risk of over-approving local installers or MCP snippets
without naming package-review and pinning conditions.

Reviewer edits required: moderate to high for release-facing decisions.

## Skill-Enabled Result

Setup: security packets reviewed with `skill-security-audit`, then evaluated
with the AgentOps report structure.

Output summary: `SECURITY-001` approved the instruction-only AI media skill for
alpha while preserving rights/disclosure/platform caveats. `SECURITY-002`
approved the installer/MCP layer with changes, documented the `npx` package
execution risk, and replaced a stale setup-guide skillset list.

What improved: the audit workflow produced capability inventories, risk checks,
findings, mitigations, approval conditions, and follow-up packets. It also
separated actual findings from residual risks that require live package,
platform, or private-environment review.

What regressed: no regression found. The workflow adds review overhead, but
that overhead is appropriate for install, script, and MCP trust decisions.

Safety issues: no blocker found after the SECURITY-002 docs mitigation. The
remaining risk is intentionally deferred to future third-party/scripted-skill
packets.

Reviewer edits required: low to moderate.

## Score

| Criterion | Baseline | Skill-enabled | Notes |
|---|---:|---:|---|
| Trigger fit | 2 | 3 | The security packets map cleanly to threat, script, supply-chain, and safe-install review. |
| Artifact usefulness | 2 | 3 | Skill-enabled output gives approve/approve-with-changes decisions and mitigations. |
| Correctness and evidence | 1 | 3 | Reports separate reviewed files, unreviewed live systems, findings, and residual risk. |
| Procedural value | 1 | 3 | Adds inventory, risk matrix, conditions, and follow-up evidence. |
| Safety boundaries | 1 | 3 | Avoids launching MCP servers or claiming package safety from config review. |
| Context efficiency | 2 | 2 | Requires several local files but no external platform. |
| Validation behavior | 1 | 3 | Names release checks and future third-party/scripted-skill packets. |
| Vendor neutrality | 2 | 3 | Keeps Codex installer as adapter and portable content as Markdown/YAML/TOML. |
| Maintainability | 2 | 3 | Produces concise reports and small docs mitigation instead of a new system. |

## Overhead

Extra files loaded: two security packets, two security reports, one bundle
brief, one security template, and one quality rubric.

Extra tools/scripts used: local validation and release check.

Approximate extra turns or time: one proof-pass review.

Token or trace link if available: not applicable.

## Follow-Up Changes

- Keep `skill-security-audit` in v0.2 alpha.
- Add one third-party skill folder packet with scripts or install hooks.
- Add one MCP-scope packet that includes credentials, write scopes, or private
  workspace access before considering beta.
- Consider a later installer guardrail that prints target paths before deleting
  an existing installed skill folder in non-dry-run mode.

## Evidence Links

- `docs/evaluation/reports/skill-security-audit-SECURITY-001.md`
- `docs/evaluation/reports/skill-security-audit-SECURITY-002.md`
- `docs/bundles/skill-security-audit.md`
- `docs/evaluation/security-review-template.md`
