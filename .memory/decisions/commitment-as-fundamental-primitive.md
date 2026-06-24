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
