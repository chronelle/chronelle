# Ontology

Chronelle primitives fall into layers.

## Durable Primitives

Long-term organizational memory. Append-only.

- Actor
- Goal
- Constraint
- Assumption
- Claim
- Alternative
- Decision

Actor represents a participant in the organization, human or agent. See
[Actor](actor.md).

Claim is a truth-apt proposition the organization tracks, with status
`unsettled`, `settled`, or `refuted`. See [Claim](claim.md). It replaces the
former Question primitive, whose empirical half is an `unsettled` Claim and whose
deliberative half is an unaccepted Decision.

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
