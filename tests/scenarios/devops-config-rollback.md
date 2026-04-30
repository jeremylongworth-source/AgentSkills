# Scenario: DevOps Config Rollback

Prompt:

> Review the environment configuration and rollback path for enabling a feature
> flag in staging and production. Identify config drift, secrets risks,
> approval gates, rollback steps, and post-rollback validation.

Expected routing:

- environment-config-review
- rollback-plan
- production-readiness-review
- secrets-handling-review

Future bundle:

- devops-cloud-release
