# Workspace Model

Chronelle repository
├── ontology/      (shared primitives and conventions)
├── projections/   (shared view definitions)
├── tools/         (shared tooling, as needed)
└── .memory/       (Chronelle's own organizational memory)

Project repository
└── .memory/       (that project's organizational memory)

Ontology is shared.
State belongs to projects.
Views are projections.

Each project keeps its own organizational memory in a `.memory/` directory inside
its own repository, the way `.git` keeps version history. Chronelle itself follows
this rule: its own memory lives in Chronelle's `.memory/`. Chronelle additionally
defines the shared ontology, projections, and tooling that every project's
`.memory/` uses.
