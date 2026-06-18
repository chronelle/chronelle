---
id: define-session-memory
type: episode
status: completed
---

# Define Session Memory

This Episode records adding short-term session memory to Chronelle.

## Context

Chronelle's primitives were all long-term. Agents lacked a way to capture the
live working state of an activity in progress so work could resume across
sessions and actors. The steward asked whether this should be a new primitive or
something else.

## Participants

- project steward
- Claude

## Inputs

- Chronelle ontology and its append-only discipline
- AIfund's informal `SESSION_HANDOFF.md` as prior art

## Outputs

- Checkpoint defined as a working-memory unit in a distinct short-term layer
- ontology README restructured into durable, temporal, and working-memory layers
- decision to add Checkpoint
- first Chronelle checkpoint instance

## Transitions

- create-checkpoint-decision
- create-checkpoint-ontology
- revise-ontology-readme
