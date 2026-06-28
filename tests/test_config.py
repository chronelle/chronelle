from pathlib import Path
import json
import tempfile
import unittest

from chronelle.config import default_registry, load_registry


class ConfigTests(unittest.TestCase):
    def test_default_registry_uses_current_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = default_registry(root)
            project = registry.get_project("personal", root.name)

            self.assertEqual(project.root, root.resolve())
            self.assertEqual(project.memory_path, root.resolve() / ".memory")
            self.assertEqual(project.approval_policy, "explicit")

    def test_load_registry_resolves_paths_relative_to_config(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "repos" / "aifund"
            repo.mkdir(parents=True)
            config = root / ".chronelle" / "config.json"
            config.parent.mkdir()
            config.write_text(
                json.dumps(
                    {
                        "orgs": {
                            "personal": {
                                "default_actor": "lxjuly",
                                "projects": {
                                    "aifund": {
                                        "path": "../repos/aifund",
                                        "approval_policy": "explicit",
                                    }
                                },
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )

            registry = load_registry(config)
            project = registry.get_project("personal", "aifund")

            self.assertEqual(project.root, repo.resolve())
            self.assertEqual(project.memory_path, repo.resolve() / ".memory")
            self.assertEqual(project.default_actor, "lxjuly")

    def test_config_example_registers_aifund(self) -> None:
        config = Path(".chronelle/config.example.json")
        if not config.exists():
            self.skipTest("config example not present")

        registry = load_registry(config)
        project = registry.get_project("personal", "aifund")

        self.assertEqual(project.project_id, "aifund")
        self.assertTrue(project.memory_path.as_posix().endswith("aifund/.memory"))


if __name__ == "__main__":
    unittest.main()
