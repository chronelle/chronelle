---
id: revise-deployed-personal-service-alternative
type: transition
episode: define-mvp-agent-service-strategy
operation: revise
target: decision:mvp-agent-service-vs-cli-tool
actor: Codex
created: 2026-06-28
---

# Revise Deployed Personal Service Alternative

Added a fourth candidate MVP product shape: a deployed personal Chronelle
service for the first customer, positioned between a local agent service and a
full hosted multi-tenant agent service.

## Rationale

The user noted that, for ChatGPT integration, they might prefer a deployed
service. ChatGPT tool calls need a reachable HTTPS endpoint, so local-only agent
deployment may introduce tunnel or relay friction.
