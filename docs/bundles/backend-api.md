# Backend API Bundle Brief

## Problem

Frontend and product work often creates backend needs: contracts, schemas, auth,
service boundaries, errors, limits, docs, and tests. Agents need a backend/API
workflow that produces reviewable design artifacts before implementation or
production changes.

## Target User

Backend developers, full-stack developers, SaaS builders, tech leads, and teams
using agents to plan or review API and service work.

## Included Skills

- `api-contract-design`: define endpoints, schemas, status codes, versioning,
  and examples.
- `database-schema-review`: review tables, migrations, constraints, indexes,
  and data integrity.
- `auth-flow-design`: plan authentication, authorization, sessions, tokens,
  permissions, and tenant access.
- `service-boundary-design`: define service/module responsibilities,
  dependencies, and data ownership.
- `error-handling-contracts`: design error envelopes, status mappings, retry
  guidance, and logging behavior.
- `rate-limit-design`: define API limits, quotas, throttling, headers, and
  monitoring.
- `api-doc-writing`: turn reviewed contracts into API documentation.
- `backend-test-plan`: define backend verification and release gates.
- `skill-threat-model`: support high-risk backend security review.
- `qa-test-strategy`: broaden test strategy when risk extends beyond backend.
- `concise-technical-writing`: tighten API design memos and review summaries.

## Context Files

- `API_CONTRACTS.md`: current public/internal API contracts and compatibility
  rules.
- `DATABASE_SCHEMA.md`: schema notes, migrations, ownership, and access
  patterns.
- `AUTH_POLICY.md`: auth provider, permission model, token/session rules, and
  tenant boundaries.
- `SERVICE_BOUNDARIES.md`: module/service ownership and dependencies.
- `TESTING_STANDARDS.md`: backend test layers and release gates.

## MCP Preset Intent

Use documentation research for current framework, database, API, and auth
provider behavior. Keep database, cloud, deployment, and production tools
read-only unless the user explicitly approves a write action.

## Safety Rules

- Do not apply migrations, deploy services, rotate credentials, change auth
  policy, alter production data, or change live rate limits automatically.
- Do not invent production traffic, customer entitlements, auth scopes, schema
  guarantees, or API behavior.
- Escalate work involving auth, billing, payments, customer data, regulated
  data, multi-tenant isolation, public APIs, or backward compatibility.
- Separate design recommendations from implementation steps and release gates.

## Pilot Metrics

- Operational: time from backend request to reviewed API design.
- Quality: reviewer correction rate on contracts, schemas, and auth plans.
- Adoption: percent of backend design artifacts accepted without major rewrite.
- Economic: reduction in implementation rework caused by unclear contracts.

## Acceptance Criteria

- The bundle installs with a dry run.
- API contract, schema review, auth flow, and backend test scenarios route to
  the intended skills.
- Outputs include concrete artifacts: API contract, schema critique, auth flow
  plan, service boundary memo, error contract, rate-limit plan, or test plan.
- High-risk backend changes include review gates and do not perform production
  writes.
