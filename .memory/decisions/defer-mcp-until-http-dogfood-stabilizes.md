---
id: defer-mcp-until-http-dogfood-stabilizes
type: decision
status: accepted
created: 2026-06-28
accepted: 2026-06-28
---

# Defer MCP Until HTTP Dogfood Stabilizes

Chronelle will defer a workspace-local MCP server until the local HTTP agent
workflow has been dogfooded on AIFund.

The local HTTP service is now the primary MVP integration surface. MCP remains a
strong candidate for Codex, Claude Code, and ChatGPT-style clients, but adding it
before the context/ingest/diff/commit loop is proven would increase integration
surface area too early.

## Rationale

The accepted implementation plan is Plan B: local HTTP agent service. The next
learning should come from running that service during real AIFund work, not from
adding another protocol.

## Revisit Trigger

Revisit MCP after the HTTP service has successfully supported at least one real
AIFund work session from restart context through approved memory update.
