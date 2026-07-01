---
id: choose-long-horizon-memory-structure
type: episode
status: completed
created: 2026-07-01T02:32:12Z
---

# Choose Long Horizon Memory Structure

The user chose the next Chronelle goal: optimize memory structure for
long-horizon tasks.

The discussion compared several alternatives, including primitive folders with a
current projection, task-centric memory, episode journals with projections,
Claim/Commitment simplification, checkpoint stacks, and thread-based memory.

## Outcome

The accepted direction is thread-based memory with per-thread checkpoints while
keeping existing durable primitives as the source of truth.

## Outputs

- decision: thread-checkpoint-memory-for-long-horizon-tasks
- transition: accept-thread-checkpoint-memory-decision
- transition: revise-current-plan-for-thread-memory
