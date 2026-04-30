# Scenario: Skill Security Third-Party Install

Prompt:

> Review this third-party skill before we install it. Identify threat model,
> prompt-injection risk, data exfiltration paths, dependency or install risks,
> and a least-privilege safe-install recommendation.

Expected routing:

- skill-threat-model
- prompt-injection-review
- data-exfiltration-review
- supply-chain-review
- safe-install-checklist

Future bundle:

- skill-security-audit
