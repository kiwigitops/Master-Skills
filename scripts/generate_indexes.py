#!/usr/bin/env python3
"""Generate markdown indexes from repository entry YAML files."""

from __future__ import annotations

import collections
import pathlib
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: Missing dependency 'PyYAML'. Install with: pip install pyyaml")
    raise SystemExit(2)

CATEGORY_ORDER = [
    "Agent Frameworks",
    "Agent SDKs / Libraries",
    "Skills Systems",
    "Memory / Retrieval / RAG",
    "Tool Use / Integrations",
    "Multi-Agent Systems",
    "Coding Agents",
    "Research Agents",
    "Browser / Computer Use Agents",
    "Voice / Multimodal Agents",
    "Evaluation / Benchmarking",
    "Workflow / Automation",
    "Observability / Monitoring",
    "Sandboxing / Execution",
    "Knowledge Bases",
]


def load_entries(root: pathlib.Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.yaml")) + sorted(root.rglob("*.yml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data["_path"] = str(path).replace("\\", "/")
            entries.append(data)
    return entries


def beginner_badge(entry: dict[str, Any]) -> str:
    return "beginner-friendly" if entry.get("beginner_friendly") else "intermediate+"


def line_for(entry: dict[str, Any]) -> str:
    entry_path = entry.get("_path", "")
    return (
        f"- **{entry['name']}** ([repo]({entry['github_url']}), "
        f"[entry](../{entry_path})) - {entry['description']} "
        f"`{entry['language']}` | `{entry['maturity']}` | `{beginner_badge(entry)}`"
    )


def write_by_category(entries: list[dict[str, Any]], out_path: pathlib.Path) -> None:
    groups: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for entry in entries:
        groups[entry["category"]].append(entry)

    ordered = [category for category in CATEGORY_ORDER if category in groups]
    extras = sorted([category for category in groups if category not in CATEGORY_ORDER])
    categories = ordered + extras

    lines = [
        "# Index By Category",
        "",
        "Generated from `data/repositories/`.",
        "Each item includes language, maturity, and beginner-signal metadata.",
        "",
    ]
    for category in categories:
        lines.append(f"## {category}")
        lines.append("")
        for entry in sorted(groups[category], key=lambda e: e["name"].lower()):
            lines.append(line_for(entry))
        lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_by_use_case(entries: list[dict[str, Any]], out_path: pathlib.Path) -> None:
    groups: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for entry in entries:
        for use_case in entry.get("use_cases", []):
            groups[use_case].append(entry)

    lines = [
        "# Index By Use Case",
        "",
        "Generated from `data/repositories/`.",
        "Use-case headings are source-derived and may evolve as entries change.",
        "",
    ]
    for use_case in sorted(groups, key=lambda item: item.lower()):
        lines.append(f"## {use_case}")
        lines.append("")
        seen = set()
        for entry in sorted(groups[use_case], key=lambda e: e["name"].lower()):
            key = entry["github_url"]
            if key in seen:
                continue
            seen.add(key)
            lines.append(line_for(entry))
        lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_by_language(entries: list[dict[str, Any]], out_path: pathlib.Path) -> None:
    groups: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for entry in entries:
        groups[entry["language"]].append(entry)

    lines = [
        "# Index By Language",
        "",
        "Generated from `data/repositories/`.",
        "Language reflects each entry's primary implementation language.",
        "",
    ]
    for language in sorted(groups):
        lines.append(f"## {language}")
        lines.append("")
        for entry in sorted(groups[language], key=lambda e: e["name"].lower()):
            lines.append(line_for(entry))
        lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_beginner_friendly(entries: list[dict[str, Any]], out_path: pathlib.Path) -> None:
    filtered = [entry for entry in entries if entry.get("beginner_friendly") is True]
    filtered.sort(key=lambda e: e["name"].lower())

    lines = [
        "# Beginner-Friendly Index",
        "",
        "Entries with `beginner_friendly: true`.",
        "These are good starting points, not endorsements.",
        "",
    ]

    for entry in filtered:
        lines.append(line_for(entry))

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    data_root = pathlib.Path("data/repositories")
    output_root = pathlib.Path("indexes")
    output_root.mkdir(parents=True, exist_ok=True)

    entries = load_entries(data_root)
    if not entries:
        print("No entries found. Nothing to index.")
        return 1

    write_by_category(entries, output_root / "by-category.md")
    write_by_use_case(entries, output_root / "by-use-case.md")
    write_by_language(entries, output_root / "by-language.md")
    write_beginner_friendly(entries, output_root / "beginner-friendly.md")

    print(f"Generated indexes for {len(entries)} entries in {output_root}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
