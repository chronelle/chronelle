---
id: consensus-as-projection
type: decision
status: accepted
---

# Model Consensus As A Projection, Not A Primitive

Chronelle models consensus as a projection over project memory, not as a new
durable primitive.

Consensus is the agreement state of a target primitive. It is derived from the
`accept` and `reject` Transitions that Actors apply to the target. Because those
Transitions are append-only and carry an Actor, the agreement state is replayable.

This follows Chronelle's discipline of preferring a projection when a concept is
derivable, the same path taken for task planning.

Consensus requirements, namely who must agree and what quorum is needed, are not
part of consensus itself. They are expressed as Constraints. See
[[ontology-change-consensus]] for an example.

This decision depends on [[actor-first-class]], which gives consensus a defined
set of members.
