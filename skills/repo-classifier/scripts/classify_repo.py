#!/usr/bin/env python3
"""Heuristic classifier for draft repository entries.

This script is intentionally simple. It suggests a category from README-like text
using keyword matches. Maintainers should review all outputs manually.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass


@dataclass
class Rule:
    category: str
    keywords: tuple[str, ...]


RULES = [
    Rule("Coding Agents", ("code", "pull request", "repository editing", "developer")),
    Rule("Research Agents", ("research", "literature", "sources", "report")),
    Rule("Browser / Computer Use Agents", ("browser", "ui automation", "computer use", "playwright")),
    Rule("Evaluation / Benchmarking", ("evaluation", "benchmark", "metric", "judge")),
    Rule("Memory / Retrieval / RAG", ("memory", "retrieval", "rag", "vector")),
    Rule("Skills Systems", ("skill", "skill.md", "skills catalog", "agent skills")),
    Rule("Multi-Agent Systems", ("multi-agent", "agent team", "coordinator")),
    Rule("Tool Use / Integrations", ("tool calling", "integration", "mcp", "connector")),
    Rule("Workflow / Automation", ("workflow", "automation", "trigger", "orchestration")),
    Rule("Voice / Multimodal Agents", ("voice", "audio", "multimodal", "realtime")),
    Rule("Observability / Monitoring", ("observability", "tracing", "monitoring", "telemetry")),
    Rule("Sandboxing / Execution", ("sandbox", "isolated execution", "runtime security")),
    Rule("Knowledge Bases", ("knowledge base", "document workspace", "enterprise search")),
    Rule("Agent SDKs / Libraries", ("sdk", "library", "api client", "developer toolkit")),
    Rule("Agent Frameworks", ("framework", "agent graph", "state machine", "runtime")),
]


def classify(text: str) -> tuple[str, int]:
    lowered = text.lower()
    best_category = "Agent Frameworks"
    best_score = 0

    for rule in RULES:
        score = sum(1 for kw in rule.keywords if re.search(re.escape(kw), lowered))
        if score > best_score:
            best_score = score
            best_category = rule.category

    return best_category, best_score


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest a taxonomy category from text.")
    parser.add_argument("text", help="README snippet or repository description")
    args = parser.parse_args()

    category, score = classify(args.text)
    print(f"category={category}")
    print(f"match_score={score}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
