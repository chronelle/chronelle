# Chronelle

Chronelle is a shared organizational memory system for mixed human-agent organizations.

Organizations historically relied on human memory to connect goals, constraints, assumptions, decisions, and execution.

As organizations increasingly delegate work to agents, human memory can no longer serve as the sole long-term memory substrate.

Chronelle provides an explicit organizational memory layer that both humans and agents can inhabit.

## MVP API

Chronelle currently exposes a small local Python API over a project-owned
`.memory/` directory.

```python
from chronelle import Chronelle

chronelle = Chronelle(".")

context = chronelle.get_context(
    project="aifund",
    role="researcher",
    task="continue chronelle design",
)

proposal = chronelle.propose_updates(transcript)
print(chronelle.diff())
chronelle.commit()
```

### `get_context(project, role, task)`

Projects current organizational state into an agent-friendly dictionary:

- goals
- assumptions
- decisions
- constraints
- open questions
- study plan
- active experiments
- current checkpoint

### `propose_updates(transcript)`

Infers candidate organizational state changes from explicit transcript lines such
as:

```text
Decision: use project-owned .memory directories
Assumption: research continuity is the first customer problem
Open Question: should proposals be staged in process?
Experiment: dogfood Chronelle across Codex and Claude Code
```

This stages proposed files in memory only. It does not write durable `.memory`
state.

### `diff()`

Returns a unified diff for staged proposal changes, using Git-style `a/` and
`b/` paths.

### `commit()`

Writes staged proposal files into `.memory/` and clears the in-process proposal.

## Run Tests

```sh
PYTHONPATH=src python3 -m unittest discover -s tests
```
