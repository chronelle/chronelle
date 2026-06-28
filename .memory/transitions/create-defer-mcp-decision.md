---
id: create-defer-mcp-decision
type: transition
episode: define-mvp-agent-service-strategy
operation: create
target: decision:defer-mcp-until-http-dogfood-stabilizes
actor: Codex
created: 2026-06-28
---

# Create Defer MCP Decision

Created an accepted Decision to defer MCP until the local HTTP agent workflow
has been dogfooded on AIFund.

## Rationale

The concrete local-agent tasks implemented the HTTP workflow. MCP should remain
a follow-up integration path rather than part of the first service build.
