---
id: chronelle-current-checkpoint
type: checkpoint
status: active
actor: Claude
updated: 2026-06-18
episode: define-consensus-and-actor
---

# Current Checkpoint

## Focus

Extend the Chronelle ontology for a mixed human-agent org: session memory, then
consensus and participants.

## Progress

- Added the Checkpoint working-memory unit and aifund's first checkpoint.
- Decided consensus is a projection (not a primitive) over Actors' accept/reject
  Transitions, with requirements as Constraints.
- Elevated Actor to a first-class durable primitive.
- Defined `ontology/actor.md` and `projections/consensus.md`, indexed both, and
  recorded the decisions, episode, transitions, and an example Constraint.

## Next Action

Decide whether to define the concurrency model for multi-actor work: per-track
Checkpoint naming and the conflict model for concurrent Transitions and contested
consensus.

## Open Loops

- Multi-threaded checkpoints and the concurrent-Transition conflict model are
  still deferred (related to contested consensus).
- Consensus quorum defaults absent a Constraint are intentionally minimal; may
  need tightening.
- Agent-Actor identity vs model version over time is open.

## Working Context

- `ontology/actor.md`, `ontology/README.md`
- `projections/consensus.md`, `projections/README.md`
- `.memory/decisions/consensus-as-projection.md`, `actor-first-class.md`
- `.memory/constraints/ontology-change-consensus.md`

## Promotion Notes

Durable residue for this session is already written (decisions, episode,
transitions). This checkpoint can move to `closed` once consensus and Actor are
committed.
