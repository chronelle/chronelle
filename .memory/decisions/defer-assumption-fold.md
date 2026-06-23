---
id: defer-assumption-fold
type: decision
status: accepted
---

# Keep Assumption Distinct From Claim For Now

Assumption is *not* folded into Claim as an `assumed` status. It stays a distinct
primitive.

An Assumption is a proposition relied upon without settling it — formally close to
a Claim held as if `settled` but unverified. Folding it in would be more
parsimonious, but writing "Assumption" is a speech act that signals "proceed as if
this holds, and challenge it." That pragmatic signal is load-bearing for
legibility, which is Chronelle's actual success criterion (a future actor must
reconstruct what happened), not elegance.

The fold is deferred, not rejected. It is recorded as an open question in
`ontology/claim.md` to revisit once Claim has been used in practice.
