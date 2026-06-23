---
id: dogfood-atomic-decisions
type: episode
status: completed
---

# Practice Surfaces The Atomic-vs-Bundled Decisions Question

This Episode records an ontology finding from applying Chronelle in practice.

## Context

A Decision that bundled several distinct choices needed only one of those
choices changed. There was no faithful Transition to supersede a single element
of a bundled Decision, surfacing a real gap in the ontology.

## Participants

- project steward
- Claude (claude-opus-4-8)

## Inputs

- A bundled stack Decision and a later single-element change to it
- Existing open question in `ontology/episode-transition.md`: "Should a
  Transition target exactly one primitive?"

## Outputs

- An open Decision `atomic-vs-bundled-decisions` capturing the unresolved
  question with evidence and candidate resolutions

## Transitions

- create-atomic-decisions-open-decision
