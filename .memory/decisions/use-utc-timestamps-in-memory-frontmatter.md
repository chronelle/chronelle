---
id: use-utc-timestamps-in-memory-frontmatter
type: decision
status: accepted
created: 2026-06-30T03:15:07Z
accepted: 2026-06-30T03:15:07Z
---

# Use UTC Timestamps In Memory Frontmatter

Chronelle-generated memory records should use full UTC timestamps in frontmatter
instead of date-only values.

The timestamp shape is:

```text
YYYY-MM-DDTHH:MM:SSZ
```

## Rationale

Date-only values are insufficient once Chronelle is used by multiple agents and
tools during the same day. Full UTC timestamps preserve ordering across sessions,
machines, and time zones without relying on local clock interpretation.

## Scope

New generated memory records should use full UTC timestamps. Existing historical
date-only records can remain unchanged until Chronelle has an explicit migration
task.
