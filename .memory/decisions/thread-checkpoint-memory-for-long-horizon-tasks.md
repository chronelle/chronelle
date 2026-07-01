---
id: thread-checkpoint-memory-for-long-horizon-tasks
type: decision
status: accepted
created: 2026-07-01T02:32:12Z
accepted: 2026-07-01T02:32:12Z
---

# Use Thread Checkpoint Memory For Long Horizon Tasks

Chronelle will optimize long-horizon task continuity by adding thread-based
memory with per-thread checkpoints, while keeping existing durable primitives as
the source of truth.

The accepted structure is:

```text
.memory/threads/
  local-agent-service/
    index.md
    checkpoint.md
    plan.md
    open-loops.md

  primitive-simplification/
    index.md
    checkpoint.md
    plan.md
    open-loops.md
```

Durable truth remains in:

```text
.memory/goals/
.memory/assumptions/
.memory/claims/
.memory/decisions/
.memory/episodes/
.memory/transitions/
```

## Rationale

Long-horizon work needs a stable resumability surface that is more focused than
the global project plan and less transient than a single current checkpoint.

Threads give each long-running workstream a durable home for:

- current focus
- next action
- open loops
- related goals, claims, decisions, episodes, and transitions
- restart context for agents

This avoids prematurely adding Task as a first-class ontology primitive while
still making long-running work easy to resume.

## Alternatives Considered

- Keep primitive folders plus global current projection only.
- Make Task a first-class primitive.
- Use Episode/Transition journal plus generated projections only.
- Collapse will-apt primitives into Commitment immediately.
- Use only a checkpoint stack.

## Decision

Use a hybrid:

```text
Thread-Based Memory
+ Per-thread Checkpoints
+ Existing Durable Primitives
```

Do not migrate the ontology to Claim + Commitment as part of this change. Keep
that as a separate open ontology decision.
