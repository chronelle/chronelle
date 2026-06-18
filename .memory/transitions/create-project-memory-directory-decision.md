---
id: create-project-memory-directory-decision
type: transition
episode: define-project-memory-directory
operation: create
target_type: decision
target_id: project-owned-memory-directory
---

# Create Project Memory Directory Decision

## Rationale

Managing an external project required a clear, shared rule for where project
memory lives.

## Before

Chronelle stated that state belongs to projects, but did not define where a
project physically stores its memory.

## After

Chronelle records that each project owns its memory in a `.memory/` directory in
its own repository, with Chronelle holding only ontology, its own memory, and
shared tools.

## Evidence

- `workspace.md`
- `.memory/decisions/project-owned-memory-directory.md`
