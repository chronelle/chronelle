---
id: settle-proposition-claims
type: transition
episode: refactor-proposition-primitives
operation: create
target_type: claim
target_ids:
  - question-conflates-two-jobs
  - proposition-is-durable-unit
---

# Settle The Proposition-Model Claims

## Rationale

The design analysis established two propositions as true at once, and they share a
single rationale, so they are recorded as one multi-target Transition rather than
two — exercising the position that a Transition may encode a change to any
combination of primitives.

## Before

The truth-apt observations existed only as prose in a design discussion.

## After

Two settled Claims exist: `question-conflates-two-jobs` and
`proposition-is-durable-unit`. They are the evidence the proposition-primitive
decisions are grounded in.

## Evidence

- `.memory/claims/question-conflates-two-jobs.md`
- `.memory/claims/proposition-is-durable-unit.md`
