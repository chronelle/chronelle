# Task Planning

Task Planning is a projection over project memory.

It is not a new ontology primitive yet.

A task is a proposed next action derived from Goals, Constraints, Assumptions,
Claims, Alternatives, Decisions, Episodes, and Transitions.

## Task Record

A task record should include:

- id
- status
- title
- why
- next action
- related memory
- owner, if known

## Statuses

- proposed
- active
- blocked
- done
- dropped

## Rules

Tasks should be grounded in project memory.

Every active task should point to the Goal, Claim, Decision, Episode, or
Transition that makes it relevant.

When a task changes project state, record the work as an Episode and record the
state change as one or more Transitions.

Use tasks to coordinate work.

Use Episodes and Transitions to preserve memory.
