---
id: define-project-memory-directory
type: episode
status: completed
---

# Define Project-Owned Memory Directory

This Episode records defining where project memory lives.

## Context

The first external project, AIfund, needed to be managed with the Chronelle
ontology. The question was where its memory should live. The steward clarified
that each project should own its memory in a `.memory/` directory in its own
repository, and that Chronelle should hold only the ontology, its own memory, and
shared tools.

## Participants

- project steward
- Claude

## Inputs

- request to manage AIfund with the Chronelle ontology
- steward clarification on the `.memory/` convention

## Outputs

- revised workspace model
- accepted decision that projects own their memory in `.memory/`
- AIfund memory established in the AIfund repository under `.memory/`
- Chronelle's own memory migrated from `projects/chronelle/` to `.memory/`

## Transitions

- create-project-memory-directory-decision
- revise-workspace-model
- migrate-chronelle-memory-to-dot-memory
