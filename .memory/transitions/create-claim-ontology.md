---
id: create-claim-ontology
type: transition
episode: refactor-proposition-primitives
operation: create
target_type: primitive
target_id: claim
---

# Create Claim Ontology Definition

## Rationale

The accepted add-claim decision is realized by defining the primitive in the
ontology.

## Before

No Claim definition existed.

## After

`ontology/claim.md` defines Claim: a truth-apt proposition with status
`unsettled`, `settled`, or `refuted`, settled by evidence, with discovery modeled
as the settle operation.

## Evidence

- `ontology/claim.md`
