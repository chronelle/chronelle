---
id: chronelle-current-checkpoint
type: checkpoint
status: active
actor: Claude
updated: 2026-06-18
episode: define-session-memory
---

# Current Checkpoint

## Focus

Add short-term session memory to Chronelle as the Checkpoint working-memory unit.

## Progress

- Decided to model session memory as a Checkpoint in a distinct working-memory
  layer, not as a durable primitive or a projection.
- Defined `ontology/checkpoint.md` and restructured `ontology/README.md` into
  layers.
- Recorded the decision, the `define-session-memory` episode, and its
  transitions.
- Created this checkpoint as the first instance.

## Next Action

Decide whether to apply Checkpoint to AIfund by promoting `SESSION_HANDOFF.md`
into `aifund/.memory/checkpoints/current.md`.

## Open Loops

- Multi-actor, multi-track concurrency model for Checkpoints is deferred.
- Whether closed Checkpoints are archived or deleted after promotion is open.

## Working Context

- `ontology/checkpoint.md`
- `ontology/README.md`
- `.memory/decisions/checkpoint-working-memory.md`
- prior art: `aifund/SESSION_HANDOFF.md`

## Promotion Notes

When this session closes, no further durable memory is pending: the decision,
episode, and transitions are already written. This checkpoint can then be cleared
or set to `closed`.
