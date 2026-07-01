---
id: evaluate-memory-structure-with-resume-harness
type: decision
status: accepted
created: 2026-07-01T02:37:07Z
accepted: 2026-07-01T02:37:07Z
---

# Evaluate Memory Structure With A Resume Harness

Chronelle should add an eval harness before treating the thread/checkpoint memory
structure as successful.

The first eval should measure whether a projected context lets an agent resume a
long-horizon task without rereading broad project history.

## Initial Metrics

- **Resume precision**: required facts present in the projected context.
- **Resume noise**: unrelated facts included in the projected context.
- **Next-action accuracy**: the projected next action matches the expected next
  action for the fixture.
- **Open-loop recall**: expected unresolved questions or risks are present.
- **Decision recall**: relevant accepted/open decisions are present.
- **Context size**: projected context stays within a practical token/character
  budget.

## First Harness Shape

Use deterministic fixtures before adding model-judged evals:

```text
tests/fixtures/resume_eval_cases/
  local_agent_service/
    memory/
    expected.json
  primitive_simplification/
    memory/
    expected.json
```

Each case should run `Chronelle.get_context()` against fixture memory and score
the projection against expected facts, next actions, open loops, and relevant
decisions.

## Rationale

Thread memory is intended to improve long-horizon continuity. Without metrics,
Chronelle cannot tell whether a new memory structure actually helps or merely
adds files.

The first eval should be cheap, local, deterministic, and versioned with the
repository.
