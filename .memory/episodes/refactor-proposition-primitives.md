---
id: refactor-proposition-primitives
type: episode
status: completed
---

# Refactor The Proposition Primitives

This Episode records adding Claim, removing Question, and keeping Assumption
distinct. It is a recursive change: Chronelle authored this change through its own
ontology, and the new Claim primitive's first use is justifying its own
introduction.

## Context

A design discussion observed that the durable primitives split into truth-apt
(propositions, settled by evidence) and will-apt (commitments, chosen). The
truth-apt side had no home: findings were smeared into prose. Question, meanwhile,
was doing two jobs and could be removed once a proposition primitive existed.

## Participants

- project steward
- Claude (claude-opus-4-8)

## Inputs

- The existing durable primitives and the open `atomic-vs-bundled-decisions`
  decision (which had already pushed a "Question" into an open Decision)
- Findings from dogfooding Chronelle on another project

## Outputs

- Claims: `question-conflates-two-jobs`, `proposition-is-durable-unit` (both settled)
- Decisions: `add-claim-primitive`, `remove-question-primitive`, `defer-assumption-fold`
- Ontology: `ontology/claim.md` added; `ontology/README.md`,
  `ontology/episode-transition.md`, and `projections/task-planning.md` revised to
  drop Question and reference Claim

## Transitions

- settle-proposition-claims
- create-claim-decision
- create-claim-ontology
- create-remove-question-decision
- supersede-question-primitive
- create-defer-assumption-decision
