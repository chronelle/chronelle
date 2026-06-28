from pathlib import Path
import tempfile
import unittest

from chronelle import Chronelle


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ChronelleApiTests(unittest.TestCase):
    def test_get_context_projects_memory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(
                root / ".memory/goals/validate.md",
                "---\nid: validate\ntype: goal\nstatus: active\n---\n\n# Validate Memory\n",
            )
            write(
                root / ".memory/claims/question.md",
                "---\nid: question\ntype: claim\nstatus: unsettled\n---\n\n# Is State Useful?\n",
            )
            write(
                root / ".memory/checkpoints/current.md",
                "---\nid: current\ntype: checkpoint\nstatus: active\n---\n\n# Current Checkpoint\n",
            )

            context = Chronelle(root).get_context(
                project="aifund",
                role="researcher",
                task="continue chronelle design",
            )

            self.assertEqual(context["project"], "aifund")
            self.assertEqual(context["role"], "researcher")
            self.assertEqual(context["task"], "continue chronelle design")
            self.assertEqual(context["goals"][0]["title"], "Validate Memory")
            self.assertEqual(context["open_questions"][0]["id"], "question")
            self.assertEqual(context["checkpoint"]["id"], "current")

    def test_propose_diff_commit_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            chronelle = Chronelle(root)

            proposal = chronelle.propose_updates(
                """
                Decision: use project-owned .memory directories
                Assumption: research continuity is the first customer problem
                Open Question: should propose_updates stage pending changes?
                """
            )

            self.assertEqual(
                [change["kind"] for change in proposal["changes"]],
                ["create decision", "create assumption", "create claim"],
            )

            diff = chronelle.diff()
            self.assertIn("+++ b/.memory/decisions/use-project-owned-memory-directories.md", diff)
            self.assertIn("+status: proposed", diff)
            self.assertIn("+status: unsettled", diff)

            written = chronelle.commit()

            self.assertEqual(
                written,
                [
                    ".memory/decisions/use-project-owned-memory-directories.md",
                    ".memory/assumptions/research-continuity-is-the-first-customer-problem.md",
                    ".memory/claims/should-propose-updates-stage-pending-changes.md",
                ],
            )
            self.assertEqual(chronelle.diff(), "")
            self.assertTrue((root / written[0]).exists())


if __name__ == "__main__":
    unittest.main()
