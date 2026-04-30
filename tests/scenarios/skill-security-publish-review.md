# Scenario: Skill Security Publish Review

Prompt:

> Before publishing this skill, produce a security review with risk matrix,
> unsafe instruction list, secrets-handling notes, data movement concerns,
> required mitigations, and approve/block/defer recommendation.

Expected routing:

- skill-threat-model
- prompt-injection-review
- data-exfiltration-review
- secrets-handling-review
- safe-install-checklist

Future bundle:

- skill-security-audit
