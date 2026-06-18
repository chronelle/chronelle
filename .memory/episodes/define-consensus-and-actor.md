---
id: define-consensus-and-actor
type: episode
status: completed
---

# Define Consensus And Actor

This Episode records adding consensus and elevating Actor in Chronelle.

## Context

Chronelle had no model for consensus among participants. The steward asked
whether consensus should be a new primitive. Analysis showed consensus is
derivable from per-Actor `accept` and `reject` Transitions, so it fits a
projection rather than a primitive. The analysis also exposed that Actor was not
first-class, which consensus needs.

## Participants

- project steward
- Claude

## Inputs

- Chronelle ontology, especially the `accept` and `reject` Transition operations
- the open question on the conflict model for concurrent Transitions

## Outputs

- Actor defined as a first-class durable primitive
- Consensus defined as a projection over Actors' accept and reject Transitions
- consensus requirements modeled as Constraints, with an example Constraint
- ontology and projections indexes updated

## Transitions

- create-actor-decision
- create-actor-ontology
- create-consensus-decision
- create-consensus-projection
- create-ontology-change-consensus-constraint
