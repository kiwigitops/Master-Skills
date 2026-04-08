# Classification System

This document defines the canonical taxonomy for repository entries.

## Design goals

- keep categories stable over time
- separate what a project is from how it is deployed
- support both quick browsing and structured querying
- keep contributor decisions consistent

## Canonical categories

Every entry must use exactly one `category` from this list:

1. Agent Frameworks
2. Agent SDKs / Libraries
3. Skills Systems
4. Memory / Retrieval / RAG
5. Tool Use / Integrations
6. Multi-Agent Systems
7. Coding Agents
8. Research Agents
9. Browser / Computer Use Agents
10. Voice / Multimodal Agents
11. Evaluation / Benchmarking
12. Workflow / Automation
13. Observability / Monitoring
14. Sandboxing / Execution
15. Knowledge Bases

## Subcategory guidance

Use `subcategory` for narrower placement. Examples:
- Agent Frameworks -> graph orchestrators, role-based orchestrators
- Agent SDKs / Libraries -> Python SDK, TypeScript SDK
- Tool Use / Integrations -> MCP, plugin runtime, tool routers
- Evaluation / Benchmarking -> online evals, offline eval harnesses
- Knowledge Bases -> enterprise knowledge hub, semantic indexers

Keep subcategories short (2-5 words) and reusable.

## Supporting dimensions

These fields refine comparison without creating category sprawl:

- `maturity`: `experimental`, `beta`, `production`
- `activity_status`: `active`, `maintenance`, `inactive`
- `docs_quality`: `low`, `medium`, `high`
- `beginner_friendly`: `true` or `false`
- `deployment_type`: one or more of `local`, `cloud`, `hybrid`, `api`, `self-hosted`, `managed`

## Tagging rules

- use lowercase kebab-case tags
- prefer specific tags over broad tags (`browser-automation` over `automation`)
- use 3-10 tags per entry
- avoid duplicating category names as tags

## Language rules

- choose the dominant implementation language
- use `multi` when no single language dominates
- use lowercase names (`python`, `typescript`, `go`, `rust`, `multi`)

## Beginner-friendly criteria

Mark `beginner_friendly: true` only when all are true:
- setup instructions are clear
- docs include runnable example
- core concepts are explained
- common errors are documented

## Review cadence

- every entry should be reviewed periodically
- update `last_reviewed` in `YYYY-MM-DD`
- archive or downgrade stale entries instead of deleting immediately

## Folder mapping

Data is stored in practical browsing folders under `data/repositories/`.
Those folders help navigation and do not replace canonical `category` values.

Current allowed data folders:

- `agent-frameworks`
- `agent-sdks-libraries`
- `skills-systems`
- `coding-agents`
- `browser-agents`
- `research-agents`
- `multimodal`
- `multi-agent`
- `evaluation`
- `memory`
- `tooling`
- `automation`
