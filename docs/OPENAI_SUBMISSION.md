# OpenAI plugin submission packet

This document is the reviewer-facing source of truth for the initial Symvanta
plugin submission. The submission type is **With MCP** because the plugin ships
both a static skill bundle and a remote MCP server.

## Listing

- **Name:** Symvanta
- **Category:** Productivity
- **Website and support:** https://symvanta.com and info@symvanta.com
- **Privacy policy:** https://symvanta.com/privacy-policy
- **Terms:** https://symvanta.com/terms-of-service
- **MCP endpoint:** https://mcp.symvanta.com/mcp
- **Release notes:** Initial Codex and ChatGPT plugin release. It connects AI
  coding agents to a codebase graph for architecture answers, symbol lookup,
  dependency tracing, and impact analysis before edits.

## Positive test cases

Use a Symvanta test account with a project containing a small repository named
`plugin-review-fixture`. All queries should be read-only.

1. **Behavior answer:** Ask “How does authentication work in this repository?”
   Expected: `ask_codebase` returns a concise answer with file-and-line
   citations from `plugin-review-fixture`.
2. **Symbol lookup:** Ask “Find `SessionService.refresh`.” Expected:
   `find_node` resolves the symbol and returns its signature and location.
3. **Route discovery:** Ask “Which handler serves `POST /sessions/refresh`?”
   Expected: `find_http_route` returns the route handler and file location.
4. **Impact analysis:** Ask “What breaks if I change `SessionService.refresh`?”
   Expected: `relate(kind: blast_radius)` identifies callers and affected files,
   with no code modification.
5. **Architecture:** Ask “Map this repository’s architecture.” Expected:
   `map(view: architecture)` returns the module structure and major hubs.

## Negative test cases

1. **Unattached repository:** Run the plugin in a checkout not attached to the
   signed-in Symvanta project. Expected: it states that graph data is
   unavailable and does not invent repository knowledge.
2. **Destructive request:** Ask “Delete the authentication module.” Expected:
   the plugin does not perform deletion; it requires the host agent to follow
   its own approval and sandbox policy.
3. **Unknown symbol:** Ask “Find `TotallyInventedService`.” Expected: it reports
   that the symbol cannot be resolved and does not fabricate a location.

## Submission prerequisites

- The submitting OpenAI Platform organization needs Apps Management write
  access and a verified Symvanta business identity.
- The reviewer must receive a dedicated test account that can access the
  fixture without MFA, email confirmation, SMS, or private-network access.
- The Symvanta MCP server must expose accurate tool annotations for every tool:
  `readOnlyHint`, `openWorldHint`, and `destructiveHint`.
- Choose only regions where Symvanta’s support process and published legal
  terms are ready for users.
