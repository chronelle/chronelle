---
id: migrate-chronelle-memory-to-dot-memory
type: transition
episode: define-project-memory-directory
operation: revise
target_type: memory-location
target_id: chronelle-own-memory
---

# Migrate Chronelle Memory To .memory

## Rationale

Chronelle should follow its own convention so its memory layout matches every
other project's.

## Before

Chronelle's own memory lived under `projects/chronelle/`, while the accepted
convention placed project memory in `.memory/`.

## After

Chronelle's own memory lives in `.memory/`, and the `projects/` directory is
removed. Evidence references inside relocated records were updated to the new
paths.

## Evidence

- `workspace.md`
- `.memory/decisions/project-owned-memory-directory.md`
