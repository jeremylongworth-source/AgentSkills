# Skill Security Review Template

Use this before publishing a new skill, installing a third-party skill, or
adding scripts/resources to an existing skill. This is a review aid, not a
replacement for security tooling or expert review.

```markdown
# Skill Security Review: <skill or bundle>

Date:
Reviewer:
Source:
Version or commit:
Install path:

## Summary

Recommendation: approve | approve with changes | block | defer
Risk level: low | medium | high | high-liability
Reason:

## Scope

Reviewed files:

- <path>

Not reviewed:

- <path or reason>

## Capability Inventory

| Capability | Present? | Notes |
|---|---|---|
| Instruction-only skill |  |  |
| Executable scripts |  |  |
| External dependencies |  |  |
| Network access |  |  |
| File read/write guidance |  |  |
| Secret handling |  |  |
| MCP/tool permissions |  |  |
| Host-specific install steps |  |  |

## Risk Checks

| Check | Result | Evidence |
|---|---|---|
| Prompt injection or instruction override | pass / warn / fail |  |
| Hidden data exfiltration path | pass / warn / fail |  |
| Privilege escalation or broad permissions | pass / warn / fail |  |
| Unsafe script execution | pass / warn / fail |  |
| Unpinned or suspicious dependencies | pass / warn / fail |  |
| Secrets requested or exposed | pass / warn / fail |  |
| Network calls without clear purpose | pass / warn / fail |  |
| Destructive file or git operations | pass / warn / fail |  |
| Legal, financial, medical, or compliance claims | pass / warn / fail |  |
| Host lock-in or hidden install behavior | pass / warn / fail |  |

## Findings

| Severity | Finding | File | Required fix |
|---|---|---|---|
| high |  |  |  |
| medium |  |  |  |
| low |  |  |  |

## Required Mitigations

- <change>
- <change>

## Approval Conditions

- <condition>
- <condition>

## Follow-Up

- Add scenario:
- Add validation:
- Re-review after:
```

## Security Review Rules

- Treat third-party skills like dependencies. Inspect instructions,
  references, scripts, install steps, and requested permissions.
- Default unknown scripts to blocked until reviewed.
- Prefer read-only, draft-first behavior for high-risk domains.
- Require explicit user approval for production writes, account changes,
  outbound messages, financial publication, legal/compliance outputs, and
  destructive filesystem or git operations.
- Keep MCP scopes narrow. Add write permissions only when the workflow needs
  them and the approval path is clear.
- Escalate any instruction that asks the agent to hide activity, bypass policy,
  ignore higher-priority instructions, or access unrelated secrets.
