---
id: chronelle-current-plan
type: plan
status: active
projection: task-planning
---

# Chronelle Current Plan

This plan is a projection over Chronelle project memory.

## Active

### Define project memory templates

- id: define-project-memory-templates
- status: active
- why: Future Chronelle work needs repeatable file shapes for Episodes,
  Transitions, and plans.
- next action: Add templates for Episode and Transition records.
- related memory:
  - decision: episode-transition-primitives
  - episode: define-episode-transition-primitives
  - projection: task-planning

## Proposed

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
