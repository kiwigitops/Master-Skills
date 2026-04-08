#!/usr/bin/env python3
"""Find repeated shell command patterns to suggest skill candidates.

The goal is to assist maintainers by identifying clusters of repeated commands.
It does not modify files and should be treated as a drafting helper.
"""

from __future__ import annotations

import argparse
import collections
import pathlib
import re

COMMAND_RE = re.compile(r"`([^`]+)`")


def collect_commands(path: pathlib.Path) -> collections.Counter[str]:
    counter: collections.Counter[str] = collections.Counter()
    for file in path.rglob("*.md"):
        text = file.read_text(encoding="utf-8", errors="ignore")
        for match in COMMAND_RE.findall(text):
            head = match.strip().split()[0] if match.strip() else ""
            if head and len(head) <= 40:
                counter[head] += 1
    return counter


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest skill candidates from repeated commands.")
    parser.add_argument("path", nargs="?", default=".", help="Repository root")
    parser.add_argument("--min-frequency", type=int, default=5, help="Minimum command frequency")
    args = parser.parse_args()

    root = pathlib.Path(args.path)
    counter = collect_commands(root)

    print("# Candidate command clusters")
    for command, count in counter.most_common():
        if count < args.min_frequency:
            break
        print(f"- {command}: {count} occurrences")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
