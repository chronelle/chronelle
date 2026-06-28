---
id: commitment-as-fundamental-primitive
type: decision
status: open
---

# Should Goal/Constraint/Decision/Alternative Unify Under A Commitment Primitive?

A decision Chronelle has not yet made.

Given [[commitment-family-is-real]], the will-apt primitives could collapse into a
single **Commitment** primitive — a proposition plus a stance — exactly as Claim
unified the truth-apt side:

- Goal = Commitment{mode: achieve}
- Constraint = Commitment{mode: maintain}
- Decision = Commitment{mode: select, accepted}
- Alternative = Commitment{mode: select, proposed}

This would give Chronelle a clean two-primitive core: **Claim** (truth-apt) and
**Commitment** (will-apt), each a proposition under a stance.

## Why It Is Held Open

The modes are structurally different, not just labels: Goals are evaluated at
completion, Constraints continuously, Decisions resolve a deliberation. The
ends / bounds / means trichotomy is load-bearing for legibility, and legibility —
not minimal primitive count — is Chronelle's success criterion.

This is the same legibility-vs-parsimony tension as [[defer-assumption-fold]] and a
sibling of [[atomic-vs-bundled-decisions]]. For now Chronelle **keeps the named
variants** (Goal, Constraint, Decision, Alternative) and continues using them.

## Candidate Resolutions

- Unify into `Commitment{mode, status}`; named primitives become views.
- Keep named variants permanently (reject unification on legibility grounds).
- Hybrid: `Commitment` as a base type with named variants as legible specializations.

When decided, resolve with an `accept` Transition recording the chosen resolution.

## Current Lean

The user is increasingly interested in simplifying Chronelle's durable
primitives to **Claim** and **Commitment**.

The attraction is that Claim and Commitment may express the core distinction more
cleanly:

- Claim tracks what the organization believes or is trying to settle.
- Commitment tracks what the organization wants, requires, chooses, proposes, or
  intends to maintain.

This would reduce the ontology's primitive count while preserving the ability to
project legible views such as Goals, Constraints, Decisions, and Alternatives.

The decision remains open because Chronelle still needs to prove that the named
views remain legible and operationally useful if they become views over
Commitment rather than first-class primitives.
