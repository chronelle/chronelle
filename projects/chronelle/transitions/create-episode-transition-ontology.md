---
id: create-episode-transition-ontology
type: transition
episode: define-episode-transition-primitives
operation: create
target_type: ontology
target_id: episode-transition
---

# Create Episode and Transition Ontology

Chronelle added Episode and Transition as ontology primitives.

## Rationale

Chronelle needs to reconstruct how organizational state evolves over time, not
only what state currently exists.

## Before

The ontology listed:

- Goal
- Constraint
- Assumption
- Question
- Alternative
- Decision

## After

The ontology also lists:

- Episode
- Transition

The new ontology note defines Episode as meaningful organizational activity and
Transition as organizational state change.

## Evidence

- GitHub issue #1
- `ontology/README.md`
- `ontology/episode-transition.md`
