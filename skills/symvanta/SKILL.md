---
name: symvanta
description: Navigate an indexed codebase with Symvanta before editing. Use for codebase behavior questions, finding symbols or routes, tracing callers and dependencies, estimating change scope, and blast-radius checks.
---

# Symvanta for Codex

Symvanta is the codebase-intelligence layer for Codex. Use its MCP tools for
code discovery and relationship questions; use local file reads only after the
graph identifies a relevant file.

## Start here

Call `init` once at the start of a repository task. It confirms the attached
project and returns the current tool-routing guidance.

If no repository is attached or indexed, tell the user. You can then use local
search as a fallback, but say that cross-repository dependency information is
unavailable.

## Choose the smallest correct tool

| Need | Use |
| --- | --- |
| Explain how or why a behavior happens | `ask_codebase` |
| Find a known symbol | `find_node` |
| Find a literal string or identifier | `locate` with `mode: "text"` |
| Search by approximate symbol or file name | `locate` with `mode: "symbol"` or `mode: "file"` |
| Find an HTTP handler | `find_http_route` |
| Find callers or dependencies | `relate` with `kind: "callers"` or `"dependencies"` |
| Understand an impact surface | `relate` with `kind: "blast_radius"` |
| Map repository architecture | `map` with `view: "architecture"` |
| Locate tests for a symbol | `list_tests_for` |
| Assess a multi-file change | `estimate_scope` |

Use `ask_codebase` directly for real “how does this work?”, “why?”, or “walk
me through it” questions. It returns a synthesized answer with source
citations, so do not manually trace several files first.

## Safe editing workflow

Before editing an existing symbol, call `relate` with `kind: "blast_radius"`.
If the change reaches more than roughly five files, crosses layers, or includes
cross-repository edges, show the impact summary and confirm scope with the
user before editing.

Do not edit additional symbols merely because they appear in a caller,
dependency, or blast-radius result. Those results are for comprehension unless
the user explicitly includes them in the requested scope.

## Source policy

Symvanta returns locations and signatures rather than source text. Open local
files only at locations it identified when you need verbatim code to edit or
quote. When the live checkout disagrees with the index, trust the live file.

## Branches and uncommitted work

Use `ref` to read an indexed feature branch. Use `ref` with
`op: "index_working_tree"` to temporarily overlay uncommitted edits before
running graph queries or `diff_impact`.
