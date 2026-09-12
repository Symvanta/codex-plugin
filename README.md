# Symvanta for Codex

Symvanta gives Codex a live codebase graph: it can locate symbols and routes,
explain behavior with cited files, map architecture, identify tests, and assess
the blast radius of a change before touching code.

## What it adds

- A connection to the Symvanta Cloud MCP server at
  `https://mcp.symvanta.com/mcp`.
- A `symvanta` skill that routes behavior questions to `ask_codebase`, lookup
  questions to graph tools, and edit-risk questions to `blast_radius`.
- Portable Agent Plugins packaging for public distribution, plus a Codex
  compatibility manifest for local testing.

## Install and test locally

1. In Codex, refresh Plugins and install **Symvanta** from your local personal
   marketplace.
2. Start a new task. Sign in through the Symvanta OAuth flow when prompted.
3. Try one of these prompts:
   - `Explain how authentication works in this repository using Symvanta.`
   - `What breaks if I change <symbol>? Use a blast-radius check first.`
   - `Map this repository's architecture with Symvanta.`

The skill begins with `init`, which confirms that a Symvanta project and its
repositories are attached. If none are attached, add the repository in the
Symvanta dashboard and start a new task.

## Self-hosted or staging

The published package intentionally points to the Cloud endpoint. For a custom
MCP endpoint, use Codex's normal MCP configuration. See
[self-hosted setup](docs/SELF_HOSTED.md).

## Development

Run the repository validation before a release:

```powershell
python scripts/validate_plugin.py
```

GitHub Actions runs the dependency-free release checks on pull requests and
pushes to `main`.

## Release

The repository is ready for the OpenAI universal plugin directory submission.
Before submitting, install it from a local marketplace, authenticate to the MCP
server, and complete the representative smoke tests documented above.
