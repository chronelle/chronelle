# Actor

Chronelle is memory for a mixed human-agent organization. Work is done by many
participants, and memory needs to say who believed, decided, changed, and agreed.

Actor is the participant primitive.

## What An Actor Is

An Actor is a participant in the organization that can author memory: a human or
an agent.

Actors are durable. They persist across sessions and are referenced wherever
memory records who did something.

## What An Actor Records

- id
- name
- kind: `human` or `agent`
- roles, if any (for example `steward`, `researcher`, `executor`)
- status: `active` or `inactive`
- description
- for an agent: the model or system it runs as, if useful

## How Actors Are Referenced

- a Transition records the Actor in its `actor` field
- an Episode records Actors in its participants
- a Checkpoint records the Actor that holds the session
- the Consensus projection aggregates Actors' `accept` and `reject` Transitions

Until now `actor` and `participants` were informal strings. Making Actor
first-class gives consensus, attribution, and multi-actor sessions a well-defined
set of members.

## Lifecycle

Create an Actor when a new participant begins authoring memory.

Change an Actor with a `revise` Transition, for example to change roles or to set
status `inactive`. Actor history is tracked through Transitions like any other
primitive.

## Open Questions

How should an agent Actor's identity relate to its model version over time?

Should roles be free-form or a controlled vocabulary?
