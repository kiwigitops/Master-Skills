#!/usr/bin/env python3
"""Index upstream skill repositories.

This script supports a repo-of-repos model by treating external repositories as
primary skill sources and generating a local markdown index.
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
from dataclasses import dataclass

try:
    import yaml
except ImportError:
    print("ERROR: Missing dependency 'PyYAML'. Install with: pip install pyyaml")
    raise SystemExit(2)


@dataclass
class Source:
    source_id: str
    name: str
    github_url: str
    description: str
    skills_roots: list[str]
    skill_file: str
    discovery_hint: str


def load_sources(path: pathlib.Path) -> tuple[list[Source], list[str]]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        return [], [f"{path}: root must be a mapping with a 'sources' key"]

    raw_sources = payload.get("sources", [])
    if not isinstance(raw_sources, list):
        return [], [f"{path}: 'sources' must be a list"]

    results: list[Source] = []
    warnings: list[str] = []
    seen_ids: set[str] = set()

    for idx, item in enumerate(raw_sources, start=1):
        if not isinstance(item, dict):
            warnings.append(f"{path}: sources[{idx}] skipped (expected mapping)")
            continue

        source_id = str(item.get("id", "")).strip()
        name = str(item.get("name", "")).strip()
        github_url = str(item.get("github_url", "")).strip()
        description = str(item.get("description", "")).strip()

        raw_roots = item.get("skills_roots", [])
        roots: list[str] = []
        if isinstance(raw_roots, list):
            for root in raw_roots:
                if isinstance(root, str) and root.strip():
                    roots.append(root.strip())
                else:
                    warnings.append(
                        f"{path}: source '{source_id or f'index {idx}'}' has non-string skills_roots entry"
                    )
        else:
            warnings.append(f"{path}: sources[{idx}] has non-list skills_roots")

        skill_file = str(item.get("skill_file", "SKILL.md")).strip() or "SKILL.md"
        discovery_hint = str(item.get("discovery_hint", "")).strip()

        if not source_id:
            warnings.append(f"{path}: sources[{idx}] skipped (missing id)")
            continue
        if source_id in seen_ids:
            warnings.append(f"{path}: duplicate source id '{source_id}' skipped")
            continue
        if not github_url.startswith("https://github.com/"):
            warnings.append(f"{path}: source '{source_id}' skipped (invalid github_url)")
            continue
        if not roots:
            warnings.append(
                f"{path}: source '{source_id}' has no skills_roots; discovery may be incomplete"
            )

        seen_ids.add(source_id)
        results.append(
            Source(
                source_id=source_id,
                name=name or source_id,
                github_url=github_url,
                description=description,
                skills_roots=roots,
                skill_file=skill_file,
                discovery_hint=discovery_hint,
            )
        )

    return results, warnings


def run_git(*args: str, cwd: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else None,
        text=True,
        capture_output=True,
        check=False,
    )


def ensure_repo(source: Source, cache_root: pathlib.Path, fetch: bool) -> pathlib.Path | None:
    if not fetch:
        return None

    repo_dir = cache_root / source.source_id

    cache_root.mkdir(parents=True, exist_ok=True)

    if repo_dir.exists():
        result = run_git("pull", "--ff-only", cwd=repo_dir)
        if result.returncode != 0:
            print(f"WARN: failed to update {source.source_id}: {result.stderr.strip()}")
    else:
        result = run_git("clone", "--depth", "1", source.github_url, str(repo_dir))
        if result.returncode != 0:
            print(f"WARN: failed to clone {source.source_id}: {result.stderr.strip()}")
            return None

    return repo_dir


def count_skills(repo_dir: pathlib.Path, source: Source) -> int:
    total = 0
    for root in source.skills_roots:
        skill_root = repo_dir / root
        if not skill_root.exists() or not skill_root.is_dir():
            continue
        for skill_file in skill_root.rglob(source.skill_file):
            if skill_file.is_file():
                total += 1
    return total


def write_index(sources: list[Source], counts: dict[str, int | None], out_path: pathlib.Path) -> None:
    lines: list[str] = [
        "# Upstream Skill Sources",
        "",
        "Generated from `data/upstream/skill-sources.yaml`.",
        "This index reflects the repo-of-repos model: external repositories are primary skill sources.",
        "",
        "| Source | Repository | Skill roots | Detected SKILL.md files | Notes |",
        "| --- | --- | --- | --- | --- |",
    ]

    for source in sources:
        detected = counts.get(source.source_id)
        detected_str = str(detected) if detected is not None else "not fetched (run --fetch)"
        roots = "<br />".join(source.skills_roots) if source.skills_roots else "-"
        lines.append(
            "| "
            f"{source.name} | "
            f"[{source.github_url}]({source.github_url}) | "
            f"{roots} | "
            f"{detected_str} | "
            f"{source.discovery_hint} |"
        )

    lines.extend(
        [
            "",
            "## Usage",
            "",
            "- Preview only (no network fetch):",
            "  - `python scripts/index_upstream_skills.py`",
            "- Fetch/update all configured sources and refresh counts:",
            "  - `python scripts/index_upstream_skills.py --fetch`",
        ]
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate index for upstream skill repositories.")
    parser.add_argument(
        "--sources",
        default="data/upstream/skill-sources.yaml",
        help="Path to upstream source manifest",
    )
    parser.add_argument(
        "--output",
        default="indexes/upstream-skill-sources.md",
        help="Output markdown path",
    )
    parser.add_argument(
        "--cache-dir",
        default=".cache/upstream-skill-sources",
        help="Local cache directory for cloned upstream repositories",
    )
    parser.add_argument(
        "--fetch",
        action="store_true",
        help="Clone/update upstream repositories before counting skills",
    )
    args = parser.parse_args()

    sources, warnings = load_sources(pathlib.Path(args.sources))
    for warning in warnings:
        print(f"WARN: {warning}")

    if not sources:
        print("ERROR: no valid upstream sources found")
        return 1
    counts: dict[str, int | None] = {}

    cache_root = pathlib.Path(args.cache_dir)

    for source in sources:
        repo_dir = ensure_repo(source, cache_root=cache_root, fetch=args.fetch)
        if repo_dir and repo_dir.exists():
            counts[source.source_id] = count_skills(repo_dir, source)
        else:
            counts[source.source_id] = None

    write_index(sources=sources, counts=counts, out_path=pathlib.Path(args.output))
    print(f"Generated {args.output} for {len(sources)} source(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
