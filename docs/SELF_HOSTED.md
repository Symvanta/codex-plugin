# Self-hosted and staging Symvanta

The published plugin connects to Symvanta Cloud at
`https://mcp.symvanta.com/mcp`. The Agent Plugins format requires a fixed remote
MCP endpoint in a published package, so it cannot safely expose an arbitrary
per-user URL as a plugin setting.

To use a self-hosted or staging endpoint, add it as a normal Codex MCP server:

```powershell
codex mcp add symvanta-self-hosted --url https://mcp.example.com/mcp
codex mcp login symvanta-self-hosted
```

Use the full `/mcp` endpoint with no trailing slash. Start a new Codex task
after signing in. The Symvanta plugin skill remains available and applies to
the self-hosted server too.

If your environment uses bearer-token authentication instead of OAuth, use
Codex's `--bearer-token-env-var` option with `codex mcp add`; do not put a token
in this repository or the plugin manifest.
