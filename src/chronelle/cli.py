from __future__ import annotations

import argparse

from .agent import AgentService
from .config import load_registry
from .server import make_server


def main() -> None:
    parser = argparse.ArgumentParser(prog="chronelle-agent")
    subcommands = parser.add_subparsers(dest="command", required=True)

    run = subcommands.add_parser("run", help="run the local Chronelle agent service")
    run.add_argument("--config", help="path to .chronelle/config.json")
    run.add_argument("--host", default="127.0.0.1")
    run.add_argument("--port", type=int, default=8765)

    args = parser.parse_args()
    if args.command == "run":
        registry = load_registry(args.config)
        server = make_server(args.host, args.port, AgentService(registry))
        host, port = server.server_address
        print(f"chronelle-agent listening on http://{host}:{port}", flush=True)
        server.serve_forever()


if __name__ == "__main__":
    main()
