#!/usr/bin/env python3
"""Dependency-free release checks for the Symvanta Codex plugin."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SKILL_PHRASES = ("Call `init`", "blast_radius", "ask_codebase")


def read_json(relative_path: str) -> dict:
    with (ROOT / relative_path).open(encoding="utf-8") as file:
        return json.load(file)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> int:
    portable = read_json("plugin.json")
    compatibility = read_json(".codex-plugin/plugin.json")
    mcp = read_json("mcp.json")
    compatibility_mcp = read_json(".mcp.json")
    skill = (ROOT / "skills" / "symvanta" / "SKILL.md").read_text(encoding="utf-8")

    require(portable["name"] == "symvanta", "portable manifest name must be symvanta")
    require(portable["version"] == compatibility["version"], "manifest versions must match")
    require(portable["repository"] == "https://github.com/Symvanta/codex-plugin", "repository URL is incorrect")
    interface = portable["extensions"]["com.openai"]["interface"]
    require(interface["privacyPolicyURL"] == "https://symvanta.com/privacy-policy", "privacy URL is incorrect")
    require(interface["termsOfServiceURL"] == "https://symvanta.com/terms-of-service", "terms URL is incorrect")
    require((ROOT / "LICENSE").is_file(), "LICENSE is missing")
    require((ROOT / "README.md").is_file(), "README is missing")
    require(all(phrase in skill for phrase in REQUIRED_SKILL_PHRASES), "skill is missing a core workflow")

    for config in (mcp, compatibility_mcp):
        server = config["mcpServers"]["symvanta"]
        require(server["type"] == "streamable-http", "MCP transport must be streamable-http")
        require(server["url"] == "https://mcp.symvanta.com/mcp", "MCP endpoint is incorrect")

    print("Symvanta plugin release checks passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"Symvanta plugin release checks failed: {error}", file=sys.stderr)
        raise SystemExit(1)
