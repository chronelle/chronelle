# Ontology

Chronelle primitives fall into layers.

## Durable Primitives

Long-term organizational memory. Append-only.

- Actor
- Goal
- Constraint
- Assumption
- Question
- Alternative
- Decision

Actor represents a participant in the organization, human or agent. See
[Actor](actor.md).

## Temporal Primitives

- Episode
- Transition

Episode and Transition describe how organizational state changes over time.

See [Episode and Transition](episode-transition.md).

## Working Memory

Short-term, mutable session memory. Not organizational truth.

- Checkpoint

Checkpoint is an actor's live working state for an activity in progress, so work
can resume. Its durable residue is promoted into the layers above when a session
ends.

See [Checkpoint](checkpoint.md).
