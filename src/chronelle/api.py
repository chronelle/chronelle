from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from difflib import unified_diff
from pathlib import Path
import re
from typing import Any


MEMORY_DIR = ".memory"
SUPPORTED_TYPES = {
    "goal": "goals",
    "assumption": "assumptions",
    "decision": "decisions",
    "constraint": "constraints",
    "claim": "claims",
    "experiment": "experiments",
}


@dataclass(frozen=True)
class MemoryRecord:
    path: Path
    metadata: dict[str, str]
    title: str
    body: str

    @property
    def id(self) -> str:
        return self.metadata.get("id", self.path.stem)

    @property
    def type(self) -> str:
        return self.metadata.get("type", self.path.parent.name.rstrip("s"))

    @property
    def status(self) -> str | None:
        return self.metadata.get("status")

    def summary(self) -> dict[str, str | None]:
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "path": self.path.as_posix(),
        }


@dataclass(frozen=True)
class ProposedChange:
    kind: str
    path: Path
    content: str
    title: str

    def as_dict(self) -> dict[str, str]:
        return {
            "kind": self.kind,
            "path": self.path.as_posix(),
            "title": self.title,
        }


@dataclass
class Proposal:
    changes: list[ProposedChange] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {"changes": [change.as_dict() for change in self.changes]}


class Chronelle:
    """Small file-backed Chronelle API.

    The MVP intentionally keeps state in project-owned `.memory/` directories.
    Proposed updates are staged in this Python object only. Calling `commit()`
    is the first operation that writes durable memory.
    """

    def __init__(self, root: str | Path = ".") -> None:
        self.root = Path(root).resolve()
        self.memory_root = self.root / MEMORY_DIR
        self._proposal = Proposal()

    def get_context(
        self,
        project: str | None = None,
        role: str | None = None,
        task: str | None = None,
    ) -> dict[str, Any]:
        records = self._read_all_records()
        checkpoints = self._read_records("checkpoints")
        plans = self._read_records("plans")

        return {
            "project": project or self.root.name,
            "role": role,
            "task": task,
            "goals": _summaries(records["goals"], active_only=True),
            "assumptions": _summaries(records["assumptions"]),
            "decisions": _summaries(records["decisions"]),
            "constraints": _summaries(records["constraints"], active_only=True),
            "open_questions": self._open_questions(records),
            "study_plan": [record.summary() for record in plans],
            "active_experiments": _summaries(records["experiments"], active_only=True),
            "checkpoint": checkpoints[0].summary() if checkpoints else None,
        }

    def propose_updates(self, transcript: str) -> dict[str, Any]:
        self._proposal = Proposal(_infer_changes(transcript, self.memory_root))
        return self._proposal.as_dict()

    def diff(self) -> str:
        if not self._proposal.changes:
            return ""

        hunks: list[str] = []
        for change in self._proposal.changes:
            current = ""
            if change.path.exists():
                current = change.path.read_text(encoding="utf-8")

            hunks.extend(
                unified_diff(
                    current.splitlines(keepends=True),
                    change.content.splitlines(keepends=True),
                    fromfile=f"a/{change.path.relative_to(self.root).as_posix()}",
                    tofile=f"b/{change.path.relative_to(self.root).as_posix()}",
                )
            )
        return "".join(hunks)

    def commit(self) -> list[str]:
        written: list[str] = []
        for change in self._proposal.changes:
            change.path.parent.mkdir(parents=True, exist_ok=True)
            change.path.write_text(change.content, encoding="utf-8")
            written.append(change.path.relative_to(self.root).as_posix())
        self._proposal = Proposal()
        return written

    def _read_all_records(self) -> dict[str, list[MemoryRecord]]:
        return {
            name: self._read_records(name)
            for name in [
                "goals",
                "assumptions",
                "decisions",
                "constraints",
                "claims",
                "experiments",
            ]
        }

    def _read_records(self, category: str) -> list[MemoryRecord]:
        directory = self.memory_root / category
        if not directory.exists():
            return []
        records = []
        for path in sorted(directory.glob("*.md")):
            records.append(_parse_record(path))
        return records

    def _open_questions(self, records: dict[str, list[MemoryRecord]]) -> list[dict[str, str | None]]:
        open_items: list[dict[str, str | None]] = []
        for claim in records["claims"]:
            if claim.status in {None, "unsettled", "open", "proposed"}:
                item = claim.summary()
                item["source"] = "claim"
                open_items.append(item)

        for path in sorted((self.root / "ontology").glob("*.md")):
            text = path.read_text(encoding="utf-8")
            section = _section(text, "Open Questions")
            for question in _bullets(section):
                open_items.append(
                    {
                        "id": _slugify(question[:72]),
                        "title": question,
                        "status": "open",
                        "path": path.relative_to(self.root).as_posix(),
                        "source": "open-questions-section",
                    }
                )
        return open_items


_default = Chronelle()


def get_context(
    project: str | None = None,
    role: str | None = None,
    task: str | None = None,
) -> dict[str, Any]:
    return _default.get_context(project=project, role=role, task=task)


def propose_updates(transcript: str) -> dict[str, Any]:
    return _default.propose_updates(transcript)


def diff() -> str:
    return _default.diff()


def commit() -> list[str]:
    return _default.commit()


def _parse_record(path: Path) -> MemoryRecord:
    text = path.read_text(encoding="utf-8")
    metadata, body = _split_frontmatter(text)
    title = _first_heading(body) or metadata.get("id") or path.stem
    return MemoryRecord(
        path=path,
        metadata=metadata,
        title=title,
        body=body.strip(),
    )


def _split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    raw = text[4:end]
    metadata: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata, text[end + 5 :]


def _first_heading(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def _summaries(records: list[MemoryRecord], active_only: bool = False) -> list[dict[str, str | None]]:
    if active_only:
        records = [record for record in records if record.status in {None, "active"}]
    return [record.summary() for record in records]


def _section(text: str, heading: str) -> str:
    pattern = re.compile(rf"^## {re.escape(heading)}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return ""
    rest = text[match.end() :]
    next_heading = re.search(r"^## ", rest, re.MULTILINE)
    if next_heading:
        return rest[: next_heading.start()]
    return rest


def _bullets(text: str) -> list[str]:
    return [line[2:].strip() for line in text.splitlines() if line.startswith("- ")]


def _infer_changes(transcript: str, memory_root: Path) -> list[ProposedChange]:
    changes: list[ProposedChange] = []
    seen: set[tuple[str, str]] = set()
    for line in transcript.splitlines():
        match = re.match(
            r"\s*(?:[-*]\s*)?(New Decision|Decision|Assumption Updated|Assumption|Constraint|Open Question|Question|Experiment Added|Experiment)\s*:\s*(.+)",
            line,
            flags=re.IGNORECASE,
        )
        if not match:
            continue

        label = match.group(1).lower()
        title = match.group(2).strip()
        primitive_type = _label_to_type(label)
        key = (primitive_type, title.lower())
        if key in seen:
            continue
        seen.add(key)
        changes.append(_new_change(primitive_type, title, memory_root))

    return changes


def _label_to_type(label: str) -> str:
    if "decision" in label:
        return "decision"
    if "assumption" in label:
        return "assumption"
    if "constraint" in label:
        return "constraint"
    if "experiment" in label:
        return "experiment"
    return "claim"


def _new_change(primitive_type: str, title: str, memory_root: Path) -> ProposedChange:
    slug = _slugify(title)
    directory = SUPPORTED_TYPES[primitive_type]
    path = _available_path(memory_root / directory / f"{slug}.md")
    status = _default_status(primitive_type)
    today = datetime.now(timezone.utc).date().isoformat()
    content = (
        "---\n"
        f"id: {path.stem}\n"
        f"type: {primitive_type}\n"
        f"status: {status}\n"
        f"created: {today}\n"
        "---\n\n"
        f"# {_title_case(title)}\n\n"
        "Source: proposed from transcript.\n"
    )
    return ProposedChange(kind=f"create {primitive_type}", path=path, content=content, title=title)


def _default_status(primitive_type: str) -> str:
    if primitive_type == "decision":
        return "proposed"
    if primitive_type == "claim":
        return "unsettled"
    return "active"


def _available_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(2, 1000):
        candidate = path.with_name(f"{path.stem}-{index}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"could not allocate proposal path for {path}")


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "untitled"


def _title_case(value: str) -> str:
    return " ".join(word.capitalize() for word in value.split())
