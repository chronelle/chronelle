from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from typing import Any
from urllib.parse import parse_qs, urlparse

from .agent import AgentService, CommitApproval


class ChronelleHTTPServer(ThreadingHTTPServer):
    def __init__(self, server_address: tuple[str, int], agent: AgentService) -> None:
        super().__init__(server_address, ChronelleRequestHandler)
        self.agent = agent


class ChronelleRequestHandler(BaseHTTPRequestHandler):
    server: ChronelleHTTPServer

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/health":
            self._json(200, {"status": "ok"})
            return
        if parsed.path == "/version":
            self._json(200, {"name": "chronelle", "version": "0.1.0"})
            return

        route = _project_route(parsed.path)
        if route and route["action"] == "context":
            query = parse_qs(parsed.query)
            self._call(
                lambda: self.server.agent.context(
                    route["org"],
                    route["project"],
                    role=_first(query.get("role")),
                    task=_first(query.get("task")),
                )
            )
            return

        route = _project_route(parsed.path)
        if route and route["action"] == "diff":
            self._call(lambda: self.server.agent.diff(route["org"], route["project"]))
            return

        self._json(404, {"error": "not found"})

    def do_POST(self) -> None:
        route = _project_route(urlparse(self.path).path)
        if not route:
            self._json(404, {"error": "not found"})
            return

        body = self._body()
        if route["action"] == "ingest":
            transcript = body.get("transcript")
            if not isinstance(transcript, str):
                self._json(400, {"error": "body.transcript must be a string"})
                return
            self._call(
                lambda: self.server.agent.ingest(
                    route["org"],
                    route["project"],
                    transcript=transcript,
                    source=_string_or_none(body.get("source")),
                    task=_string_or_none(body.get("task")),
                )
            )
            return

        if route["action"] == "commit":
            self._call(
                lambda: self.server.agent.commit(
                    route["org"],
                    route["project"],
                    CommitApproval(
                        approved=body.get("approval") is True,
                        actor=_string_or_none(body.get("actor")),
                    ),
                )
            )
            return

        self._json(404, {"error": "not found"})

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _body(self) -> dict[str, Any]:
        length = int(self.headers.get("content-length", "0"))
        if length == 0:
            return {}
        raw = self.rfile.read(length)
        try:
            body = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            return {}
        return body if isinstance(body, dict) else {}

    def _call(self, fn: Any) -> None:
        try:
            self._json(200, fn())
        except KeyError as exc:
            self._json(404, {"error": str(exc)})

    def _json(self, status: int, body: dict[str, Any]) -> None:
        payload = json.dumps(body, indent=2, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("content-type", "application/json; charset=utf-8")
        self.send_header("content-length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def make_server(host: str, port: int, agent: AgentService) -> ChronelleHTTPServer:
    return ChronelleHTTPServer((host, port), agent)


def _project_route(path: str) -> dict[str, str] | None:
    parts = [part for part in path.split("/") if part]
    if len(parts) != 5:
        return None
    if parts[0] != "orgs" or parts[2] != "projects":
        return None
    action = parts[4]
    if action not in {"context", "ingest", "diff", "commit"}:
        return None
    return {"org": parts[1], "project": parts[3], "action": action}


def _first(values: list[str] | None) -> str | None:
    if not values:
        return None
    return values[0]


def _string_or_none(value: Any) -> str | None:
    return value if isinstance(value, str) else None
