---
id: mvp-agent-service-vs-cli-tool
type: decision
status: accepted
created: 2026-06-28
accepted: 2026-06-28
---

# The MVP Product Shape Is Local Agent Service First

Chronelle will implement a **local agent service first**.

The main goal is now to speed up development of other projects by preserving
continuity across AI work sessions. That shifts the MVP question from "what is
the smallest API?" to "what product shape best proves that Chronelle accelerates
real work?"

The accepted direction is to build a local agent service over the core
file-backed API/CLI:

```text
project-owned .memory
        ^
Chronelle core API / CLI
        ^
Chronelle local agent service
```

This keeps the business ambition pointed at an agent service while preserving
the simplest trustworthy persistence layer.

## Accepted Resolution

Build the local agent service first.

The service has a standing job: maintain project memory, produce restart
context, ingest transcripts, propose updates, show diffs, and commit only after
approval.

This best matches the user's immediate goal: accelerate development across
Chronelle, AIFund, and other projects by preserving continuity across ChatGPT,
Codex, Claude Code, and other agent sessions.

## Candidate Resolutions

### Build a simple CLI/tool first

Chronelle remains primarily a local CLI and Python library over project-owned
`.memory/` files.

This is the smallest and most inspectable implementation. It keeps memory close
to Git, makes diffs reviewable, and avoids hosted service surface area.

Pros:

- Smallest implementation surface.
- Easy to test, debug, and trust.
- Keeps memory close to Git and project files.
- Avoids auth, background processes, hosting, tenancy, and billing.
- Good foundation for every later deployment model.

Cons:

- The user still has to remember to run Chronelle.
- It may feel like another developer tool rather than a memory steward.
- It weakly validates the agent-service business model.
- It does not naturally observe work across sessions or tools.
- It may under-test the real promise: speeding up work without manual
  bookkeeping.

### Build a local agent service first

Chronelle runs as a local agent service over the same core CLI/API and
project-owned `.memory/` files.

The service has a standing job: maintain project memory, produce restart
context, ingest transcripts, propose updates, show diffs, and commit only after
approval.

This best matches the goal of accelerating the user's own multi-agent
development workflow while preserving the trust and auditability of local files.

Pros:

- Best fit for the user's current preference.
- Tests the agent-service product shape without hosted SaaS complexity.
- Gives Chronelle a standing job: maintain project memory.
- Can support multiple local organizations through local org/project config.
- Keeps durable memory repo-owned, inspectable, and reviewable.
- Provides a direct migration path to self-hosted and hosted deployments.
- Better dogfoods the core value: restart context, transcript intake, proposed
  updates, diffs, and approved commits.

Cons:

- More moving parts than a simple CLI.
- Needs process lifecycle, config, logs, and probably an HTTP API.
- Still requires local setup by each user or organization.
- Does not prove hosted distribution, billing, or enterprise administration.
- Could blur the boundary between "agent reasoning" and "memory persistence" if
  not designed carefully.

### Build a hosted vendable agent service first

Chronelle is built immediately as a hosted service that vends a memory steward
agent to an organization.

This most directly tests the business model suggested by agent-service examples
such as Harvey and Sierra.

Pros:

- Most directly aligned with the long-term agent-service business model.
- Easier for customers to adopt if they do not want local setup.
- Enables managed integrations, billing, admin controls, and support.
- Makes "vend an agent to an organization" literal.
- Can create stronger product feedback from external users.

Cons:

- Introduces auth, tenancy, billing, security, data retention, and support
  burden immediately.
- Raises trust issues before the memory loop is proven.
- Requires careful isolation between organizations.
- Makes mistakes more expensive because customer data leaves local control.
- Could distract from validating the first-customer workflow.
- Requires deployment and operational work before Chronelle has earned it.

### Build a deployed personal service first

Chronelle runs as a deployed service for the first customer, but does not yet
become a full multi-tenant SaaS product.

This service can expose an HTTPS API that ChatGPT, Codex, Claude Code, and other
clients can call without relying on local tunneling.

Pros:

- Better fit for ChatGPT integration, because ChatGPT tools need a reachable
  HTTPS endpoint.
- Still allows a single-customer deployment before full SaaS tenancy.
- Makes Chronelle feel like an agent service rather than a local developer tool.
- Can later evolve into a hosted vendable service if the workflow proves useful.
- Avoids asking every client to reach into a laptop-local process.

Cons:

- Adds deployment, secrets, authentication, backups, and monitoring earlier.
- Requires a stronger permission model before `commit` can be exposed remotely.
- Creates a risk that `.memory` ownership drifts away from project repositories.
- Still does not fully validate multi-tenant enterprise concerns.
- May slow core memory-loop iteration compared with local-only dogfooding.

## Architecture Direction

Keep the core file-backed CLI/API underneath the local agent service:

```text
project-owned .memory
        ^
Chronelle core API / CLI
        ^
Chronelle local agent service
```

ChatGPT integration creates pressure toward a deployed service because ChatGPT
cannot reliably call a laptop-local agent without a tunnel or relay. A deployed
personal service may be the smallest product-shaped bridge between local
dogfooding and hosted SaaS.

Local agent service also preserves a path to multiple organizations without
hosted tenancy by modeling each organization as local config:

```text
org id
  project id
    repo path
    .memory path
    actors
    approval policy
```

## Related Memory

- goal: speed-up-other-project-development
- decision: project-owned-memory-directory
- decision: use-task-planning-projection
- ontology: checkpoint
