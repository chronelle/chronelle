---
id: create-checkpoint-ontology
type: transition
episode: define-session-memory
operation: create
target_type: document
target_id: checkpoint-ontology
---

# Create Checkpoint Ontology

## Rationale

The Checkpoint unit needed a shared definition so every project models session
memory the same way.

## Before

Chronelle had no ontology document for working memory.

## After

Chronelle has `ontology/checkpoint.md` defining what a Checkpoint records, its
lifecycle, the promotion rule, its relationship to Episode, its location under
`.memory/checkpoints/`, and the deferred multi-actor model.

## Evidence

- `ontology/checkpoint.md`
