# Checkpoint

Chronelle's durable primitives record what an organization believes, wants, and
decides, and how that state changed. They are append-only organizational truth.

Agents also need short-term memory: the live working state of an activity in
progress, so the same or another actor can pick up where it left off.

Checkpoint is that working-memory unit.

## What A Checkpoint Is

A Checkpoint is a mutable snapshot of an actor's current working state for an
activity in progress.

It exists to let work resume. It is a resumption aid, not organizational truth.

Where a Transition is an append-only fact about durable change, a Checkpoint is
latest-wins working state that is expected to be overwritten and eventually
discarded.

## What A Checkpoint Records

- id
- status
- actor
- updated time
- related project
- related Episode, if one is open
- focus: what this session is working toward
- progress: what has been done so far this session
- next action: the single most useful step to resume from
- open loops: blockers and unresolved threads
- working context: files, references, commands, and loaded state
- promotion notes: durable memory that should be written when this closes

## Lifecycle

- `active`: a session is currently working against it
- `handed-off`: paused and ready for another actor to resume
- `resumed`: picked up again, by the same or a different actor
- `closed`: the activity ended

Create a Checkpoint when an activity is worth resuming later.

Update it continuously. The latest version replaces the previous one. A
Checkpoint does not keep its own history; if a step is durable memory, record it
as a Transition.

## The Promotion Rule

A Checkpoint is never the source of truth.

When a session ends, promote its durable residue into the long-term layer:
Decisions become Decisions, state changes become Transitions, and a bounded
activity becomes an Episode with outputs.

After promotion, the Checkpoint can be cleared or archived. Nothing of lasting
value is lost, because the lasting value was promoted.

## Relationship To Episode

A Checkpoint is the live working state of an open Episode, or of exploration that
has not yet formed into one.

Episode is the durable narrative of what happened, written when the activity is
bounded and meaningful. Checkpoint is the mutable, in-flight state before then.

When the Episode completes, the Checkpoint's durable residue becomes the
Episode's outputs and Transitions.

## Location

Checkpoints live in each project's own memory under `.memory/checkpoints/`.

A single active session uses `checkpoints/current.md`.

## Multi-Actor Sessions

Multiple actors may work on a project at the same time, so a project may have
more than one active Checkpoint at once: one per track or actor.

The intended shape is one Checkpoint file per track under `.memory/checkpoints/`,
keyed by track or actor.

The coordination model for concurrent Checkpoints is deferred. It is related to
the open ontology question about concurrent Transitions revising the same
primitive.

## Open Questions

How should concurrent Checkpoints on parallel tracks be named, discovered, and
reconciled?

When should a Checkpoint be promoted automatically versus on explicit handoff?

Should a closed Checkpoint be archived for audit, or deleted once promoted?
