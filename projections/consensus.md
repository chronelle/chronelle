# Consensus

Consensus is a projection over project memory. It is not a new ontology
primitive.

In a mixed human-agent organization, a primitive such as a Decision is not always
settled when one Actor writes it. Consensus is the agreement state of a target
primitive, derived from how Actors have responded to it.

## Derived, Not Authored

Consensus is computed, never written directly.

It is derived from the `accept` and `reject` Transitions that Actors apply to a
target primitive. Because Transitions are append-only and carry an Actor, the
agreement state at any time is replayable.

To change consensus, an Actor emits an `accept` or `reject` Transition. Dissent is
simply a `reject`.

## Consensus Record

For a target primitive, the projection reports:

- target: type and id
- members: the Actors whose agreement is required
- accepts: Actors who accepted, with the Transition that records it
- dissents: Actors who rejected, with the Transition that records it
- state
- as-of time

## States

- `proposed`: written but not yet agreed by the required members
- `agreed`: the required members accepted and no blocking dissent stands
- `contested`: dissent stands, or members disagree
- `ratified`: agreed and any required sign-off is present
- `superseded`: the target was superseded, so its consensus no longer applies

## Requirements Are Constraints

Who must agree, and what quorum is needed, are not part of consensus itself. They
are Constraints.

For example, a Constraint may require human-steward agreement for ontology changes
or for enabling live trading. The Consensus projection reads such Constraints to
know the members and the quorum for a target.

Absent any Constraint, a primitive is treated as proposed by its author and is not
consensus-bound.

## Rules

Consensus is grounded in Transitions and Actors.

Record agreement and dissent as `accept` and `reject` Transitions by Actors.

Group the activity of reaching consensus as an Episode when it is worth
remembering.

This projection relates to the open ontology question about the conflict model for
concurrent Transitions revising the same primitive.
