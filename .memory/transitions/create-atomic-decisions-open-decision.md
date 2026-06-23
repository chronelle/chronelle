---
id: create-atomic-decisions-open-decision
type: transition
episode: dogfood-atomic-decisions
operation: create
target_type: decision
target_id: atomic-vs-bundled-decisions
---

# Create Atomic-vs-Bundled Decisions Open Decision

## Rationale

Applying Chronelle in practice surfaced that bundled Decisions cannot be
partially superseded. The matter is a decision Chronelle has yet to make, so it
is recorded as an open Decision rather than a resolved one.

## Before

The tension existed only implicitly, adjacent to the open question on whether a
Transition should target exactly one primitive.

## After

An explicit open Decision `atomic-vs-bundled-decisions` records the problem,
dogfooding evidence, and candidate resolutions, to be resolved later with an
`accept` Transition.

## Evidence

- `.memory/decisions/atomic-vs-bundled-decisions.md`
