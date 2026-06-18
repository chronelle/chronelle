---
id: create-checkpoint-decision
type: transition
episode: define-session-memory
operation: create
target_type: decision
target_id: checkpoint-working-memory
---

# Create Checkpoint Decision

## Rationale

Adding a short-term memory layer is a material design choice that needed an
accepted decision with rationale.

## Before

Chronelle had only long-term primitives and projections. There was no recorded
position on session memory.

## After

Chronelle records the decision to add Checkpoint as a short-term working-memory
unit, distinct from durable primitives and projections, never the source of
truth.

## Evidence

- `ontology/checkpoint.md`
- `.memory/decisions/checkpoint-working-memory.md`
