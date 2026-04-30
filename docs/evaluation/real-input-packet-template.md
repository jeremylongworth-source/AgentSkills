# Real-Input Packet Template

Use this template when collecting anonymized source material for v0.2 alpha
validation. Keep private customer, sponsor, employee, financial, legal,
credential, and platform data out of public commits. If a packet cannot be
safely public, store it outside the repo and reference only a local packet ID in
the validation tracker.

```markdown
# Real-Input Packet: <packet-id>

Bundle:
Scenario:
Reviewer:
Date collected:
Public-safe: yes | no
Storage: committed | private local | external review only

## Source Context

Describe the real task, role, and artifact needed.

## User Prompt

> Paste the exact anonymized prompt the agent should receive.

## Source Material

- <sanitized excerpt, file summary, screenshot description, or data table>
- <remove names, emails, account IDs, private links, secrets, and exact financials unless public>

## Expected Artifact

- <memo, checklist, runbook, brief, report, scorecard, draft, or code review>

## Acceptance Criteria

- <criterion>
- <criterion>
- <criterion>

## High-Risk Boundaries

- <approval gate>
- <legal/financial/platform/security/privacy caveat>
- <system writes or sends that must not happen automatically>

## Baseline Setup

Skillset disabled or closest prior bundle:
Notes:

## Skill-Enabled Setup

Skillset:
Relevant skills expected:
Notes:

## Reviewer Notes

What would make the output usable?
What common mistakes should be caught?
What would block release promotion?
```

## Sanitization Checklist

- Remove names, emails, phone numbers, addresses, account IDs, and private URLs.
- Remove credentials, tokens, secrets, keys, cookies, and private env values.
- Redact exact revenue, payroll, legal, customer, medical, and platform
  enforcement details unless explicitly public.
- Replace company, sponsor, creator, customer, and employee names with stable
  placeholders.
- Preserve enough structure for the workflow to remain realistic.
- Mark whether the packet is safe to commit.
