---
id: chronelle-current-checkpoint
type: checkpoint
status: active
actor: Claude
updated: 2026-06-23
episode: refactor-proposition-primitives
---

# Current Checkpoint

## Focus

Refine the durable primitives: add the truth-apt primitive and prune redundancy.

## Progress

- Added **Claim** — a truth-apt proposition with status `unsettled`/`settled`/`refuted`.
  Discovery is modeled as the `settle` operation, not a primitive.
- Removed **Question**: empirical half → `unsettled` Claim, deliberative half →
  unaccepted Decision.
- Kept **Assumption** distinct for now (fold deferred on legibility grounds).
- Authored the change recursively: settled Claims justify it, three Decisions
  commit it, one Episode and six Transitions record it; ontology docs are the
  Episode's outputs.

## Next Action

Decide the Claim follow-ups now tracked in `ontology/claim.md` open questions:
whether Assumption folds into Claim, whether `settle`/`refute` are first-class
operations or specializations of `revise`, and whether refuted Claims are archived
or retained.

## Open Loops

- Assumption-fold into Claim: deferred, not rejected.
- `settle`/`refute` operations: added to the vocabulary, but the controlled-vocab
  question remains open.
- Multi-threaded checkpoints and the concurrent-Transition conflict model are
  still deferred (related to contested consensus).
- `atomic-vs-bundled-decisions` remains open; the multi-target
  `settle-proposition-claims` Transition is a first datapoint that combination
  targets are workable.

## Working Context

- `ontology/claim.md`, `ontology/README.md`, `ontology/episode-transition.md`
- `projections/task-planning.md`
- `.memory/claims/`, `.memory/decisions/`, `.memory/episodes/refactor-proposition-primitives.md`

## Promotion Notes

Durable residue is already written (claims, decisions, episode, transitions). This
checkpoint can close once the Claim follow-up questions are picked up.
