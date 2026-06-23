# Claim

Chronelle needs to record not only what an organization intends, bounds, and
decides, but what it holds to be *true* — and how that truth-state changes as
evidence arrives.

Claim is the truth-apt primitive.

## What A Claim Is

A Claim is a proposition whose truth the organization tracks: something that can
be true or false, and whose standing is moved by evidence rather than by
decision.

Where a Decision is *will-apt* (chosen, not true or false), a Claim is
*truth-apt* (settled by evidence, not by preference). "We will use SvelteKit" is
a Decision; "the JSearch API paginates" is a Claim.

Claims are durable. A Claim persists across sessions and is referenced wherever
memory depends on something being the case.

## What A Claim Records

- id
- statement: the proposition itself, stated independently of the activity that
  found it
- status: `unsettled`, `settled`, or `refuted`
- evidence: what moved it to its current status
- actor: who settled or refuted it
- description

## Status And Lifecycle

- `unsettled`: the proposition is posed but its truth is not yet known. This is
  the home for an empirical inquiry — the kind of open question that is answered
  by finding out, not by choosing.
- `settled`: evidence established the proposition as true. A settled Claim is
  what is informally called a "fact."
- `refuted`: evidence established the proposition as false.

Settling a Claim — moving it from `unsettled` to `settled` — is the act of
*discovery*. It is an operation on a Claim, not a separate primitive.

A `settled` or `refuted` Claim may be **reopened** when new evidence destabilizes
it. Findings can be wrong, and that history matters.

## Relationship To Other Primitives

Claim is the affirmative counterpart of the former Question primitive. Question
conflated two jobs — *what we don't know* and *what we haven't decided*. Its
empirical half is now an `unsettled` Claim; its deliberative half is a Decision
that has not yet been accepted. See [Decision] in the durable layer.

Assumption is, for now, kept distinct from Claim. An Assumption is a proposition
relied upon *without* settling it — closest to a Claim held as if `settled` but
unverified. Whether Assumption should fold into Claim as an `assumed` status is
deferred on legibility grounds: writing "Assumption" is a speech act that signals
"proceed as if this holds, and challenge it," which a bare status flag may lose.

## How Claims Are Referenced

- a Transition records a Claim in its target when it creates, settles, refutes,
  revises, or reopens the Claim
- an Episode may record Claims among its outputs (what was learned)
- a Transition that changes another primitive may cite a Claim as evidence
  (a settled Claim is durable, linkable evidence, not just a string)

## Open Questions

Should Assumption fold into Claim as an `assumed` status, or stay a distinct
speech-act primitive?

Should `settle` and `refute` be first-class Transition operations, or specializations
of `revise`?

Should a refuted Claim be archived, or retained as standing memory that the
organization once believed it?
