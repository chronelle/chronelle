---
id: create-consensus-decision
type: transition
episode: define-consensus-and-actor
operation: create
target_type: decision
target_id: consensus-as-projection
---

# Create Consensus Decision

## Rationale

How to model consensus is a material design choice that needed an accepted
decision with rationale.

## Before

Chronelle had no recorded position on consensus.

## After

Chronelle records the decision to model consensus as a projection over Actors'
accept and reject Transitions, with requirements expressed as Constraints, rather
than as a new primitive.

## Evidence

- `projections/consensus.md`
- `.memory/decisions/consensus-as-projection.md`
