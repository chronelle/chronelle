---
id: automatic-observation-source
type: decision
status: open
created: 2026-06-28
---

# Which Observation Source Should Let Chronelle Update Memory Automatically?

A decision Chronelle has not yet made.

Chronelle can now ingest transcript text through the local HTTP agent service,
stage proposed memory changes, show diffs, and commit after approval. The next
automation question is how session evidence should enter Chronelle without the
user explicitly asking every time.

## Candidate Resolutions

### Watched transcript inbox

Chronelle watches a local directory for new transcript or session-summary files:

```text
.chronelle/inbox/{org}/{project}/
```

Pros:

- Simple and tool-agnostic.
- Works with ChatGPT, Codex, Claude Code, and manual notes.
- Keeps the first observation source local and inspectable.
- Easy to test with real AIFund sessions.

Cons:

- Still requires something to write session material into the inbox.
- File watching and duplicate ingestion need state tracking.
- Raw transcripts may be noisy and may require summarization first.

### Codex session wrapper

Chronelle provides a command that starts or frames a Codex/AIFund session, emits
context at the beginning, and captures a handoff or transcript at the end.

Pros:

- Strong fit for the user's remote Codex workflow.
- Can make context retrieval and session closeout feel automatic.
- Produces cleaner session evidence than arbitrary file watching.

Cons:

- Depends on available Codex session hooks and transcript access.
- May not generalize cleanly to ChatGPT and Claude Code.
- Risks coupling Chronelle too tightly to one client.

### Filesystem and Git change watcher

Chronelle watches project file changes and Git diffs, then proposes memory
updates when meaningful code or document changes occur.

Pros:

- Requires less explicit transcript handling.
- Can notice real project changes even when session text is unavailable.
- Useful for drift detection between work and memory.

Cons:

- Code diffs often omit rationale, assumptions, and rejected alternatives.
- Higher false-positive risk.
- Needs careful filtering to avoid noisy proposals.

### MCP or client tool integration

Codex, Claude Code, ChatGPT, or other clients call Chronelle tools directly at
session start, during work, and at session close.

Pros:

- Clean long-term agent integration model.
- Makes Chronelle a tool clients can call without parsing files.
- Aligns with the separation between Chronelle Skill reasoning and Chronelle
  Tool persistence.

Cons:

- Requires client configuration and protocol work.
- MCP has already been deferred until the HTTP workflow is dogfooded.
- Does not solve clients that cannot call local tools directly.

## Current Lean

Start with a **watched transcript inbox** as the first automatic observation
source.

This best matches the current local HTTP service and is the smallest step from
explicit transcript POST to automatic ingestion. It also keeps AIFund dogfooding
tool-agnostic: any client can write a transcript or closeout note into the inbox.

## Related Memory

- goal: speed-up-other-project-development
- decision: local-agent-implementation-plan
- decision: defer-mcp-until-http-dogfood-stabilizes
- ontology: episode-transition
