---
id: local-agent-implementation-plan
type: decision
status: accepted
created: 2026-06-28
accepted: 2026-06-28
---

# Build The Local Agent As A Local HTTP Service

Chronelle will build the local agent as a **local HTTP agent service**.

Chronelle has accepted local agent service first as the MVP product shape. The
next implementation question is how to build it without losing the file-backed
trust layer or overbuilding orchestration.

## Accepted Resolution

Implement Plan B: Local HTTP agent service.

The service should run locally:

```sh
chronelle-agent run
```

and expose local endpoints for context, transcript ingestion, proposed diffs,
and approved commits. This satisfies the user's target workflow: work on AIFund
while Chronelle runs alongside the work and automatically maintains pending
organizational memory updates.

## Candidate Resolutions

### Plan A: Command-driven agent workflow

Add an executable `chronelle-agent` command that wraps the existing core API:

```sh
chronelle-agent context --org personal --project aifund --task "continue research"
chronelle-agent ingest transcript.md --org personal --project aifund
chronelle-agent diff --org personal --project aifund
chronelle-agent commit --org personal --project aifund
```

Pros:

- Smallest implementation step from the current Python API.
- Easy to test in Codex and Claude Code sessions.
- No long-running process or HTTP server yet.
- Keeps review and approval explicit.
- Establishes org/project config without service complexity.

Cons:

- Still depends on the user or calling agent to invoke commands.
- Does not feel much like a standing memory steward yet.
- ChatGPT direct integration still needs Codex or another bridge.
- Does not satisfy the user's clarified goal of working on AIFund while an agent
  automatically updates organizational memory.

### Plan B: Local HTTP agent service

Add a local long-running service:

```sh
chronelle-agent run
```

Expose local endpoints:

```http
GET  /orgs/{org}/projects/{project}/context
POST /orgs/{org}/projects/{project}/ingest
GET  /orgs/{org}/projects/{project}/diff
POST /orgs/{org}/projects/{project}/commit
```

Pros:

- More accurately models an agent service.
- Gives Codex, Claude Code, scripts, and future UIs a stable API.
- Can later sit behind a tunnel or deployed relay for ChatGPT.
- Forces clearer auth, approval, and process boundaries.

Cons:

- Requires service lifecycle, ports, logs, request validation, and local auth.
- More complexity before the basic agent loop is proven.
- Commit permissions need careful handling even locally.

### Plan C: Workspace-local MCP server

Expose Chronelle as an MCP server with tools:

```text
chronelle.get_context
chronelle.propose_updates
chronelle.diff
chronelle.commit
```

Pros:

- Tool protocol maps naturally to agent clients.
- Better long-term fit for Codex, Claude Code, and ChatGPT-style integrations.
- Keeps the agent/tool boundary explicit.
- May reduce custom integration code later.

Cons:

- Requires MCP packaging and client configuration.
- May be premature before Chronelle's core workflow stabilizes.
- Still needs an agent policy layer that decides when to call tools.

## Architecture Direction

The user wants to work on AIFund while an agent automatically updates
organizational memory. That requires a running local service or tool server, not
only a command-driven workflow.

Plan B should still reuse a clear core:

```text
chronelle.core       file-backed memory API
chronelle.config     org/project registry
chronelle.agent      policy and workflow
chronelle.cli        command entrypoints
chronelle.server     local HTTP service
```

This creates a standing local memory steward while leaving a path to MCP and
later deployed services.

## Related Memory

- goal: speed-up-other-project-development
- decision: mvp-agent-service-vs-cli-tool
- decision: project-owned-memory-directory
- ontology: checkpoint
