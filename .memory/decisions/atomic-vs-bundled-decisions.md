---
id: atomic-vs-bundled-decisions
type: decision
status: open
---

# Should Decisions Be Atomic, Or May They Bundle Several Choices?

A decision Chronelle has not yet made.

When a Decision records several distinct choices at once, later revising just
one of them has no clean Transition. `supersede` targets a whole primitive, so
superseding a bundled Decision to change one element wrongly discards the
elements still in force.

## Evidence From Practice

Applying the ontology surfaced a concrete case: a Decision bundled four choices
(a stack: backend, database, frontend, LLM). Later only the frontend choice
changed. There was no faithful way to supersede only that one element:

- Superseding the bundled Decision wholesale would discard the still-valid
  remaining choices.
- A standalone new Decision coexisting with the old one leaves the bundled
  Decision stale and the relationship informal.

The interim workaround was to record the new Decision standalone and defer the
supersede relationship — exactly the gap this open decision names.

## Relationship To Existing Open Questions

This sharpens the open question in [Episode and Transition](../../ontology/episode-transition.md):
"Should a Transition target exactly one primitive?" Atomic Decisions would make
single-target supersede Transitions sufficient; bundled Decisions would require
either element-level targets or a decomposition operation.

## Candidate Resolutions

- Constrain Decisions to be atomic (one choice per Decision).
- Allow bundled Decisions but add a `decompose` (or `split`) operation that
  replaces a bundled Decision with atomic ones, preserving provenance.
- Allow Transitions to target a named element within a primitive.

When this is decided, resolve it with an `accept` Transition recording the
chosen resolution.

## Evidence

- `ontology/episode-transition.md` (the related open question)
