from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


DEFAULT_ORG_ID = "personal"


@dataclass(frozen=True)
class ProjectConfig:
    org_id: str
    project_id: str
    root: Path
    memory_path: Path
    default_actor: str = "user"
    approval_policy: str = "explicit"


@dataclass(frozen=True)
class OrgConfig:
    org_id: str
    name: str
    projects: dict[str, ProjectConfig]
    default_actor: str = "user"


class Registry:
    def __init__(self, orgs: dict[str, OrgConfig]) -> None:
        self.orgs = orgs

    def get_project(self, org_id: str, project_id: str) -> ProjectConfig:
        try:
            org = self.orgs[org_id]
        except KeyError as exc:
            raise KeyError(f"unknown org: {org_id}") from exc

        try:
            return org.projects[project_id]
        except KeyError as exc:
            raise KeyError(f"unknown project for org {org_id}: {project_id}") from exc

    def as_dict(self) -> dict[str, Any]:
        return {
            "orgs": {
                org_id: {
                    "name": org.name,
                    "default_actor": org.default_actor,
                    "projects": {
                        project_id: {
                            "path": project.root.as_posix(),
                            "memory_path": project.memory_path.as_posix(),
                            "default_actor": project.default_actor,
                            "approval_policy": project.approval_policy,
                        }
                        for project_id, project in org.projects.items()
                    },
                }
                for org_id, org in self.orgs.items()
            }
        }


def load_registry(config_path: str | Path | None = None, cwd: str | Path = ".") -> Registry:
    cwd_path = Path(cwd).resolve()
    if config_path is None:
        default_path = cwd_path / ".chronelle" / "config.json"
        if default_path.exists():
            config_path = default_path
        else:
            return default_registry(cwd_path)

    path = Path(config_path).expanduser().resolve()
    data = json.loads(path.read_text(encoding="utf-8"))
    return registry_from_dict(data, base_path=path.parent)


def default_registry(root: str | Path = ".") -> Registry:
    root_path = Path(root).resolve()
    project_id = root_path.name
    project = ProjectConfig(
        org_id=DEFAULT_ORG_ID,
        project_id=project_id,
        root=root_path,
        memory_path=root_path / ".memory",
    )
    org = OrgConfig(
        org_id=DEFAULT_ORG_ID,
        name="Personal",
        projects={project_id: project},
    )
    return Registry({DEFAULT_ORG_ID: org})


def registry_from_dict(data: dict[str, Any], base_path: str | Path = ".") -> Registry:
    base = Path(base_path).resolve()
    orgs: dict[str, OrgConfig] = {}
    for org_id, org_data in data.get("orgs", {}).items():
        default_actor = org_data.get("default_actor", "user")
        projects: dict[str, ProjectConfig] = {}
        for project_id, project_data in org_data.get("projects", {}).items():
            root = _resolve_path(project_data["path"], base)
            memory_path = _resolve_path(project_data.get("memory_path", root / ".memory"), base)
            projects[project_id] = ProjectConfig(
                org_id=org_id,
                project_id=project_id,
                root=root,
                memory_path=memory_path,
                default_actor=project_data.get("default_actor", default_actor),
                approval_policy=project_data.get("approval_policy", "explicit"),
            )

        orgs[org_id] = OrgConfig(
            org_id=org_id,
            name=org_data.get("name", org_id),
            projects=projects,
            default_actor=default_actor,
        )

    return Registry(orgs)


def _resolve_path(value: str | Path, base: Path) -> Path:
    path = Path(value).expanduser()
    if path.is_absolute():
        return path.resolve()
    return (base / path).resolve()
