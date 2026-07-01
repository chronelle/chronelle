---
id: chronelle-current-plan
type: plan
status: active
projection: task-planning
---

# Chronelle Current Plan

This plan is a projection over Chronelle project memory.

## Done

### Run full AIFund dogfood session

- id: run-full-aifund-dogfood-session
- status: done
- why: The local HTTP service needed a real AIFund work session to validate
  whether the loop speeds up development.
- related memory:
  - goal: speed-up-other-project-development
  - decision: local-agent-implementation-plan
  - decision: defer-mcp-until-http-dogfood-stabilizes

### Define local org and project registry

- id: define-local-org-project-registry
- status: done
- why: Chronelle's first-customer goal is to speed up development of other
  projects, which requires addressing AIFund and Chronelle as distinct projects
  under a local organization.
- related memory:
  - goal: speed-up-other-project-development
  - decision: mvp-agent-service-vs-cli-tool
  - decision: local-agent-implementation-plan
  - transition: revise-current-plan-with-local-agent-tasks

### Add local HTTP service skeleton

- id: add-local-http-service-skeleton
- status: done
- why: Plan B requires `chronelle-agent run` as a standing local service.
- related memory:
  - decision: local-agent-implementation-plan
  - goal: speed-up-other-project-development

### Implement context endpoint

- id: implement-context-endpoint
- status: done
- why: AIFund work sessions need restart context at the beginning of work.
- related memory:
  - decision: local-agent-implementation-plan
  - ontology: checkpoint

### Implement transcript ingest and proposal staging

- id: implement-transcript-ingest-proposal-staging
- status: done
- why: The agent must automatically maintain pending organizational memory
  updates while the user works on AIFund.
- related memory:
  - decision: local-agent-implementation-plan
  - decision: mvp-agent-service-vs-cli-tool

### Implement diff and approval-gated commit endpoints

- id: implement-diff-and-approval-gated-commit
- status: done
- why: Chronelle's trust boundary is review before durable writes to `.memory`.
- related memory:
  - decision: local-agent-implementation-plan
  - decision: project-owned-memory-directory

### Dogfood local agent on AIFund

- id: dogfood-local-agent-on-aifund
- status: done
- why: Chronelle's first customer is the user's own AIFund and Chronelle work.
- related memory:
  - goal: speed-up-other-project-development
  - decision: local-agent-implementation-plan

### Define automatic observation source

- id: define-automatic-observation-source
- status: done
- why: The agent cannot automatically update memory unless it knows where
  session evidence enters the system.
- related memory:
  - decision: local-agent-implementation-plan
  - ontology: episode-transition

### Evaluate MCP after HTTP workflow stabilizes

- id: evaluate-mcp-after-http-workflow-stabilizes
- status: done
- why: MCP may become the cleaner integration path for Codex, Claude Code, and
  ChatGPT-style clients, but should not precede the core memory loop.
- related memory:
  - decision: local-agent-implementation-plan
  - decision: defer-mcp-until-http-dogfood-stabilizes

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

### Implement thread checkpoint memory

- id: implement-thread-checkpoint-memory
- status: active
- why: Chronelle's next goal is to optimize memory structure for long-horizon
  tasks, and the accepted structure is thread-based memory with per-thread
  checkpoints.
- next action: Define the `.memory/threads/` file shapes, create initial threads
  for local-agent-service and primitive-simplification, and teach context
  projection to surface active thread context.
- related memory:
  - decision: thread-checkpoint-memory-for-long-horizon-tasks
  - episode: choose-long-horizon-memory-structure

## Proposed

### Define thread memory file shapes

- id: define-thread-memory-file-shapes
- status: proposed
- why: Thread memory needs repeatable conventions before implementation.
- next action: Specify `index.md`, `checkpoint.md`, `plan.md`, and
  `open-loops.md` fields and linking rules.
- related memory:
  - decision: thread-checkpoint-memory-for-long-horizon-tasks

### Create initial Chronelle threads

- id: create-initial-chronelle-threads
- status: proposed
- why: Chronelle needs live examples to dogfood thread memory.
- next action: Create `local-agent-service` and `primitive-simplification`
  threads under `.memory/threads/`.
- related memory:
  - decision: thread-checkpoint-memory-for-long-horizon-tasks
  - decision: commitment-as-fundamental-primitive

### Project active thread context

- id: project-active-thread-context
- status: proposed
- why: Long-horizon task memory only helps if `get_context()` can surface the
  relevant thread checkpoint and open loops.
- next action: Extend the Chronelle context projection to include active threads.
- related memory:
  - decision: thread-checkpoint-memory-for-long-horizon-tasks
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
