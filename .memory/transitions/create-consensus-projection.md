---
id: create-consensus-projection
type: transition
episode: define-consensus-and-actor
operation: create
target_type: projection
target_id: consensus
---

# Create Consensus Projection

## Rationale

Consensus needed a shared definition as a projection so every project derives
agreement state the same way.

## Before

Chronelle had only the task-planning projection.

## After

Chronelle has a consensus projection that derives a target's agreement state from
Actors' accept and reject Transitions, with states proposed, agreed, contested,
ratified, and superseded, and the projections README lists it.

## Evidence

- `projections/consensus.md`
- `projections/README.md`
