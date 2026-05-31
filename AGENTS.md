# AGENTS.md

Guidance for agents working in this repository.

## Project

Chronelle is a shared organizational memory system for mixed human-agent
organizations.

When changing Chronelle, prefer updating Chronelle's own project memory before
or alongside code and ontology changes.

## Commits

Use Conventional Commits for all commit messages.

Follow the Conventional Commits 1.0.0 specification:

https://www.conventionalcommits.org/en/v1.0.0/#specification

Commit messages must use this form:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Use `feat:` for new features and `fix:` for bug fixes.

Other useful types include `docs:`, `chore:`, `refactor:`, `test:`, `ci:`,
`build:`, `style:`, and `perf:`.

Use `!` after the type or scope, or a `BREAKING CHANGE:` footer, for breaking
changes.

Examples:

```text
docs: add agent contribution guidance
feat(ontology): define episode and transition primitives
fix(projections): handle empty project state
```
