---
id: chronelle-current-plan
type: plan
status: active
projection: task-planning
---

# Chronelle Current Plan

This plan is a projection over Chronelle project memory.

## Done

### Refactor proposition primitives

- id: refactor-proposition-primitives
- status: done
- why: The truth-apt side of the ontology had no home, and Question was doing two
  jobs. Added Claim, removed Question, kept Assumption distinct for now.
- related memory:
  - claim: question-conflates-two-jobs
  - claim: proposition-is-durable-unit
  - decision: add-claim-primitive
  - decision: remove-question-primitive
  - decision: defer-assumption-fold
  - episode: refactor-proposition-primitives
  - ontology: claim

## Active

### Define local org and project registry

- id: define-local-org-project-registry
- status: active
- why: Chronelle's first-customer goal is to speed up development of other
  projects, which requires addressing AIFund and Chronelle as distinct projects
  under a local organization.
- next action: Add a config module and file shape for local org/project
  registration, including repo path, `.memory` path, default actor, and approval
  policy.
- related memory:
  - goal: speed-up-other-project-development
  - decision: mvp-agent-service-vs-cli-tool
  - decision: local-agent-implementation-plan
  - episode: define-mvp-agent-service-strategy

## Proposed

### Add local HTTP service skeleton

- id: add-local-http-service-skeleton
- status: proposed
- why: Plan B requires `chronelle-agent run` as a standing local service.
- next action: Add `chronelle.server` and a `chronelle-agent run` entrypoint
  that starts a localhost HTTP server with health and version endpoints.
- related memory:
  - decision: local-agent-implementation-plan
  - goal: speed-up-other-project-development

### Implement context endpoint

- id: implement-context-endpoint
- status: proposed
- why: AIFund work sessions need restart context at the beginning of work.
- next action: Expose `GET /orgs/{org}/projects/{project}/context` over the
  existing `Chronelle.get_context()` projection.
- related memory:
  - decision: local-agent-implementation-plan
  - ontology: checkpoint

### Implement transcript ingest and proposal staging

- id: implement-transcript-ingest-proposal-staging
- status: proposed
- why: The agent must automatically maintain pending organizational memory
  updates while the user works on AIFund.
- next action: Expose `POST /orgs/{org}/projects/{project}/ingest` that accepts
  transcript/session text and stages proposed memory updates without persistence.
- related memory:
  - decision: local-agent-implementation-plan
  - decision: mvp-agent-service-vs-cli-tool

### Implement diff and approval-gated commit endpoints

- id: implement-diff-and-approval-gated-commit
- status: proposed
- why: Chronelle's trust boundary is review before durable writes to `.memory`.
- next action: Expose diff retrieval and commit endpoints, requiring explicit
  approval for commit.
- related memory:
  - decision: local-agent-implementation-plan
  - decision: project-owned-memory-directory

### Dogfood local agent on AIFund

- id: dogfood-local-agent-on-aifund
- status: proposed
- why: Chronelle's first customer is the user's own AIFund and Chronelle work.
- next action: Register AIFund as a local project, run the local agent during an
  AIFund work session, and verify it produces useful context and proposed memory
  updates.
- related memory:
  - goal: speed-up-other-project-development
  - decision: local-agent-implementation-plan

### Define automatic observation source

- id: define-automatic-observation-source
- status: proposed
- why: The agent cannot automatically update memory unless it knows where
  session evidence enters the system.
- next action: Decide the first observation source: explicit transcript POST,
  watched transcript directory, Codex handoff file, or editor/terminal
  integration.
- related memory:
  - decision: local-agent-implementation-plan
  - ontology: episode-transition

### Evaluate MCP after HTTP workflow stabilizes

- id: evaluate-mcp-after-http-workflow-stabilizes
- status: proposed
- why: MCP may become the cleaner integration path for Codex, Claude Code, and
  ChatGPT-style clients, but should not precede the core memory loop.
- next action: After the local HTTP workflow works for AIFund, decide whether to
  add a workspace-local MCP server.
- related memory:
  - decision: local-agent-implementation-plan

### Define project memory templates

- id: define-project-memory-templates
- status: proposed
- why: Future Chronelle work needs repeatable file shapes for Episodes,
  Transitions, and plans.
- next action: Add templates for Episode and Transition records.
- related memory:
  - decision: episode-transition-primitives
  - episode: define-episode-transition-primitives
  - projection: task-planning

### Support multi-threaded checkpoints

- id: support-multi-threaded-checkpoints
- status: proposed
- why: Multiple actors can work on a project at once, so a project may have more
  than one active Checkpoint, and they need naming, discovery, and reconciliation.
- next action: Design per-track Checkpoint naming under `.memory/checkpoints/` and
  a concurrency model, related to the open question on concurrent Transitions.
- related memory:
  - decision: checkpoint-working-memory
  - ontology: checkpoint

### Apply checkpoints to AIfund

- id: apply-checkpoints-to-aifund
- status: proposed
- why: AIfund already keeps an informal `SESSION_HANDOFF.md`, which is exactly a
  Checkpoint and should adopt the formal shape.
- next action: Promote `aifund/SESSION_HANDOFF.md` into
  `aifund/.memory/checkpoints/current.md`.
- related memory:
  - decision: checkpoint-working-memory
  - ontology: checkpoint

### Define task planning conventions

- id: define-task-planning-conventions
- status: proposed
- why: Chronelle needs a clear way to plan work without prematurely adding Task
  as an ontology primitive.
- next action: Use this plan through several work episodes, then decide whether
  Task should become a primitive or remain a projection.
- related memory:
  - projection: task-planning

### Reconcile local and remote history

- id: reconcile-local-remote-history
- status: proposed
- why: Clean repository history makes Chronelle easier for agents and humans to
  trust.
- next action: Confirm local and remote commits are aligned after pushes.
- related memory:
  - AGENTS.md

## Done

### Define consensus and Actor

- id: define-consensus-and-actor
- status: done
- why: A mixed human-agent org needs to represent agreement among participants,
  and consensus needs a defined set of members.
- related memory:
  - decision: actor-first-class
  - decision: consensus-as-projection
  - episode: define-consensus-and-actor
  - projection: consensus
  - ontology: actor

### Define session memory

- id: define-session-memory
- status: done
- why: Chronelle's primitives were all long-term; agents needed short-term memory
  to resume work in progress.
- related memory:
  - ontology: checkpoint
  - decision: checkpoint-working-memory
  - episode: define-session-memory

### Define Episode and Transition primitives

- id: define-episode-transition-primitives
- status: done
- why: Chronelle needed temporal primitives for reconstructing organizational
  state changes.
- related memory:
  - ontology: episode-transition
  - decision: episode-transition-primitives
  - episode: define-episode-transition-primitives
