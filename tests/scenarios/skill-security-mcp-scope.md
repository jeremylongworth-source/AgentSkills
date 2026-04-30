# Scenario: Skill Security MCP Scope

Prompt:

> Review whether this skillset should receive filesystem, browser, network, and
> issue-tracker MCP access. Keep the recommendation least-privilege and identify
> approval gates for any write or production-related scope.

Expected routing:

- skill-threat-model
- data-exfiltration-review
- script-permission-review
- safe-install-checklist

Future bundle:

- skill-security-audit
