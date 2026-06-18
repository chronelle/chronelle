---
id: actor-first-class
type: decision
status: accepted
---

# Make Actor A First-Class Primitive

Chronelle adds Actor as a durable primitive: a participant that authors memory,
human or agent.

Previously `actor` and `participants` were informal string fields on Transitions
and Episodes. There was no well-defined set of participants.

Elevating Actor gives attribution, multi-actor sessions, and consensus a defined
membership. Actors are referenced by Transitions, Episodes, Checkpoints, and the
Consensus projection.

This was decided together with [[consensus-as-projection]], which depends on
Actors being identifiable.
