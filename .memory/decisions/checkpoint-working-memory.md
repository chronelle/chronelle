---
id: checkpoint-working-memory
type: decision
status: accepted
---

# Add Checkpoint As Short-Term Working Memory

Chronelle adds a working-memory layer with one unit: Checkpoint.

A Checkpoint is an actor's mutable, latest-wins working state for an activity in
progress, so the same or another actor can resume it.

It is a distinct layer from the durable primitives and from projections. It is
not derived like a projection, and it is not append-only truth like the durable
primitives.

The governing rule is that a Checkpoint is never the source of truth. Durable
residue is promoted into Decisions, Transitions, and Episodes when a session
ends.

Checkpoints live in each project's `.memory/checkpoints/`. Multi-actor,
multi-track sessions are supported in shape by one Checkpoint per track, with the
concurrency model deferred.

This refines [[project-owned-memory-directory]] by adding a short-term layer to
the memory each project owns.
