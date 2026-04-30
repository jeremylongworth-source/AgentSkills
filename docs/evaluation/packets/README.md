# Validation Packets

This folder holds public-safe validation packets for v0.2 alpha testing.

Use `../real-input-packet-template.md` for new packets. Commit only packets that
are safe to publish. Store private customer, sponsor, creator, financial,
legal, security, or platform data outside the repo and reference the local
packet ID in `../v0.2-validation-tracker.md`.

## Packet Types

- `public-safe`: based on public repository material and safe to commit.
- `private-local`: real input stored outside the repo.
- `synthetic-calibration`: useful for dry runs, but does not count as real-input
  promotion evidence.

## Current Packets

| Packet | Bundle | Type | Status |
|---|---|---|---|
| `AGENTOPS-001` | `agentops-evaluation` | public-safe | ready |
| `AGENTOPS-002` | `agentops-evaluation` | public-safe | ready |
| `AGENTOPS-003` | `agentops-evaluation` | public-safe | ready |
| `SECURITY-001` | `skill-security-audit` | public-safe | ready |
| `SECURITY-002` | `skill-security-audit` | public-safe | ready |
| `DOCS-001` | `technical-documentation` | public-safe | ready |
| `QUALITY-001` | `quality-testing` | public-safe | ready |
| `DEVOPS-001` | `devops-cloud-release` | public-safe | ready |
| `BACKEND-001` | `backend-api` | public-safe | ready |
