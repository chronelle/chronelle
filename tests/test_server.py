from pathlib import Path
from threading import Thread
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import tempfile
import unittest

from chronelle.agent import AgentService
from chronelle.config import registry_from_dict
from chronelle.server import make_server


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ServerTests(unittest.TestCase):
    def test_context_ingest_diff_and_approval_gated_commit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(
                root / "aifund/.memory/goals/reliable.md",
                "---\nid: reliable\ntype: goal\nstatus: active\n---\n\n# Reliable Paper Trading\n",
            )
            registry = registry_from_dict(
                {
                    "orgs": {
                        "personal": {
                            "projects": {
                                "aifund": {
                                    "path": "aifund",
                                    "approval_policy": "explicit",
                                }
                            }
                        }
                    }
                },
                base_path=root,
            )
            server = make_server("127.0.0.1", 0, AgentService(registry))
            thread = Thread(target=server.serve_forever, daemon=True)
            thread.start()
            base = f"http://127.0.0.1:{server.server_address[1]}"
            try:
                context = get_json(
                    f"{base}/orgs/personal/projects/aifund/context?{urlencode({'task': 'continue aifund'})}"
                )
                self.assertEqual(context["org"], "personal")
                self.assertEqual(context["project"], "aifund")
                self.assertEqual(context["goals"][0]["title"], "Reliable Paper Trading")

                proposal = post_json(
                    f"{base}/orgs/personal/projects/aifund/ingest",
                    {
                        "source": "test",
                        "task": "continue aifund",
                        "transcript": "Decision: keep commits approval gated",
                    },
                )
                self.assertEqual(proposal["observation_source"], "explicit_transcript_post")
                self.assertEqual(proposal["changes"][0]["kind"], "create decision")

                diff = get_json(f"{base}/orgs/personal/projects/aifund/diff")
                self.assertIn("keep-commits-approval-gated.md", diff["diff"])

                rejected = post_json(f"{base}/orgs/personal/projects/aifund/commit", {})
                self.assertFalse(rejected["committed"])
                self.assertFalse((root / "aifund/.memory/decisions/keep-commits-approval-gated.md").exists())

                committed = post_json(
                    f"{base}/orgs/personal/projects/aifund/commit",
                    {"approval": True, "actor": "tester"},
                )
                self.assertTrue(committed["committed"])
                self.assertEqual(committed["actor"], "tester")
                self.assertTrue((root / "aifund/.memory/decisions/keep-commits-approval-gated.md").exists())
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=2)


def get_json(url: str) -> dict:
    with urlopen(url, timeout=5) as response:
        return json.loads(response.read().decode("utf-8"))


def post_json(url: str, body: dict) -> dict:
    request = Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"content-type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=5) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        return json.loads(exc.read().decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
