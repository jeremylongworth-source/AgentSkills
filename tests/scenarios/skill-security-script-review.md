# Scenario: Skill Security Script Review

Prompt:

> Audit the scripts bundled with this skill. Review file writes, shell command
> construction, network calls, dependency installs, environment access, secrets
> exposure, and whether any script should be blocked or changed before publish.

Expected routing:

- script-permission-review
- supply-chain-review
- secrets-handling-review
- safe-install-checklist

Future bundle:

- skill-security-audit
