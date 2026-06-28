from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .api import Chronelle
from .config import ProjectConfig, Registry


@dataclass(frozen=True)
class CommitApproval:
    approved: bool
    actor: str | None = None


class AgentService:
    def __init__(self, registry: Registry) -> None:
        self.registry = registry
        self._chronelles: dict[tuple[str, str], Chronelle] = {}

    def context(
        self,
        org_id: str,
        project_id: str,
        role: str | None = None,
        task: str | None = None,
    ) -> dict[str, Any]:
        project = self._project(org_id, project_id)
        context = self._chronelle(project).get_context(
            project=project.project_id,
            role=role,
            task=task,
        )
        context["org"] = project.org_id
        context["project_root"] = project.root.as_posix()
        context["memory_path"] = project.memory_path.as_posix()
        return context

    def ingest(
        self,
        org_id: str,
        project_id: str,
        transcript: str,
        source: str | None = None,
        task: str | None = None,
    ) -> dict[str, Any]:
        project = self._project(org_id, project_id)
        proposal = self._chronelle(project).propose_updates(transcript)
        proposal["org"] = org_id
        proposal["project"] = project_id
        proposal["source"] = source
        proposal["task"] = task
        proposal["observation_source"] = "explicit_transcript_post"
        return proposal

    def diff(self, org_id: str, project_id: str) -> dict[str, Any]:
        project = self._project(org_id, project_id)
        return {
            "org": org_id,
            "project": project_id,
            "diff": self._chronelle(project).diff(),
        }

    def commit(self, org_id: str, project_id: str, approval: CommitApproval) -> dict[str, Any]:
        project = self._project(org_id, project_id)
        if project.approval_policy == "explicit" and not approval.approved:
            return {
                "org": org_id,
                "project": project_id,
                "committed": False,
                "error": "commit requires explicit approval",
                "written": [],
            }

        written = self._chronelle(project).commit()
        return {
            "org": org_id,
            "project": project_id,
            "committed": True,
            "actor": approval.actor,
            "written": written,
        }

    def _project(self, org_id: str, project_id: str) -> ProjectConfig:
        return self.registry.get_project(org_id, project_id)

    def _chronelle(self, project: ProjectConfig) -> Chronelle:
        key = (project.org_id, project.project_id)
        if key not in self._chronelles:
            self._chronelles[key] = Chronelle(project.root, memory_root=project.memory_path)
        return self._chronelles[key]
