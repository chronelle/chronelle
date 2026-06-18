---
id: project-owned-memory-directory
type: decision
status: accepted
---

# Projects Own Their Memory In A .memory Directory

Each project keeps its own organizational memory in a `.memory/` directory inside
its own repository, the way `.git` keeps version history.

Chronelle defines only the shared ontology, its own memory, and shared tooling.
Chronelle does not store other projects' state.

A project's `.memory/` uses the Chronelle ontology and the same primitive file
shapes, but is owned, versioned, and stored by that project.

This keeps project memory close to the code it describes, lets each repository
travel with its own memory, and keeps Chronelle focused on shared concerns.

This refines [[workspace-project-separation]]: state belongs to projects, and now
physically lives with them.
