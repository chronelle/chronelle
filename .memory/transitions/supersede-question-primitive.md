---
id: supersede-question-primitive
type: transition
episode: refactor-proposition-primitives
operation: supersede
target_type: primitive
target_id: question
---

# Supersede The Question Primitive

## Rationale

The accepted remove-question decision is realized by removing Question from the
ontology and projections, superseded by Decision (deliberative half) and Claim
(empirical half).

## Before

Question appeared in the durable-primitives list, in the Episode "related" fields
and examples of `episode-transition.md`, and as a task target in the task-planning
projection.

## After

Question is removed from `ontology/README.md`, `ontology/episode-transition.md`,
and `projections/task-planning.md`; those references now point to Claim or
Decision. Historical memory records that mention Question are left intact as
append-only history.

## Evidence

- `ontology/README.md`
- `ontology/episode-transition.md`
- `projections/task-planning.md`
