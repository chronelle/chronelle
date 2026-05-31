# Episode and Transition

Chronelle needs memory that can answer not only what an organization currently
believes, wants, asks, considers, and decides, but how that state came to be.

Episode and Transition are the temporal primitives.

Episode is the unit of meaningful organizational activity.

Transition is the unit of organizational state change.

## Episode

An Episode is a bounded activity that is meaningful enough to become
organizational memory.

It is not every message, edit, or tool call. It is the smallest durable narrative
unit that helps a future human or agent reconstruct what happened.

An Episode records:

- id
- title
- summary
- start time
- end time, if known
- participants
- related project
- related Goals, Constraints, Assumptions, Questions, Alternatives, and Decisions
- inputs
- outputs
- Transitions produced or observed

Create an Episode when activity has a coherent intent and later reconstruction
would benefit from preserving its context.

Split an Episode when the intent changes, the participating actors materially
change, or the resulting state changes need separate provenance.

## Transition

A Transition is an explicit change to organizational state.

Where an Episode says what happened, a Transition says what changed.

A Transition records:

- id
- episode id
- time
- actor
- operation
- target primitive
- previous state or reference
- resulting state or reference
- rationale
- evidence

Initial operations:

- create
- revise
- accept
- reject
- supersede
- resolve
- reopen
- archive

A Transition should be small enough that its rationale is clear. If one activity
changes several primitives for different reasons, model those changes as several
Transitions in the same Episode.

## Relationship to Existing Primitives

Goal describes intended state.

Constraint describes a boundary on possible action.

Assumption describes a belief being relied upon.

Question describes an unresolved inquiry.

Alternative describes an option under consideration.

Decision describes a chosen direction.

Episode describes the activity through which those primitives are created,
tested, revised, accepted, rejected, or superseded.

Transition describes the exact state change applied to those primitives.

## Relationship to Event Sourcing

Chronelle should adopt the useful discipline of event sourcing without making
raw system events part of the ontology.

Transitions should be append-only facts whenever possible.

Current project state should be derivable by replaying Transitions.

Episodes should group Transitions into human-legible organizational memory.

Operational events, logs, messages, and edits can become evidence, but they
should become Transitions only when they represent meaningful organizational
state change.

## Examples from Chronelle

### Defining Episode and Transition

Episode:

- title: Define Episode and Transition ontology primitives
- project: Chronelle
- participants: issue author, design agent
- inputs: GitHub issue #1
- outputs: this ontology note

Transitions:

- create Question: What unit represents meaningful organizational activity?
- create Alternative: Use Episode as the activity primitive.
- create Alternative: Use raw event-sourcing events as the activity primitive.
- accept Alternative: Use Episode as the activity primitive.
- create Decision: Model activity as Episodes and state change as Transitions.

### Revising a Goal

Episode:

- title: Refine shared memory validation goal
- project: Chronelle
- inputs: new evidence from a collaboration trial
- outputs: revised Goal and new Assumption

Transitions:

- revise Goal `validate-shared-memory`
- create Assumption that shared memory is most valuable in long-horizon work
- resolve Question about whether short tasks need persistent memory

### Superseding a Decision

Episode:

- title: Revisit workspace and project separation
- project: Chronelle
- inputs: implementation experience
- outputs: superseding Decision

Transitions:

- supersede Decision `workspace-project-separation`
- create Decision describing the replacement model
- archive Alternative that was rejected by the new model

## Implementation Recommendations

Start with an append-only Transition log.

Store Episodes as first-class records that group related Transitions.

Use stable ids for every primitive.

Reference targets by type and id.

Allow current state to be materialized as a projection over Transitions.

Keep project state separate from ontology definitions.

Keep low-level operational telemetry outside the ontology unless it changes
organizational state.

## Open Questions

Should Episode boundaries be manual, agent-suggested, or inferred?

Should a Transition target exactly one primitive?

What conflict model should Chronelle use when concurrent Transitions revise the
same primitive?

Which Transition operations belong in the first controlled vocabulary?

## Success Criteria

Chronelle satisfies this model when a future human or agent can reconstruct:

- what state existed at a given time
- which Episode caused a state change
- who or what applied the change
- what rationale and evidence supported the change
- which memory was created, revised, resolved, superseded, or archived
