#!/usr/bin/env python3
"""Validate repository entry YAML files.

Checks required fields, basic types, and controlled vocabulary constraints.
"""

from __future__ import annotations

import datetime as dt
import pathlib
import re
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: Missing dependency 'PyYAML'. Install with: pip install pyyaml")
    raise SystemExit(2)


REQUIRED_FIELDS = {
    "name",
    "github_url",
    "description",
    "category",
    "subcategory",
    "tags",
    "language",
    "license",
    "maturity",
    "activity_status",
    "docs_quality",
    "beginner_friendly",
    "use_cases",
    "deployment_type",
    "notable_features",
    "limitations",
    "related_projects",
    "last_reviewed",
}

CATEGORIES = {
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
}

MATURITY_VALUES = {"experimental", "beta", "production"}
ACTIVITY_VALUES = {"active", "maintenance", "inactive"}
DOCS_QUALITY_VALUES = {"low", "medium", "high"}
DEPLOYMENT_VALUES = {"local", "cloud", "hybrid", "api", "self-hosted", "managed"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ALLOWED_DATA_FOLDERS = {
    "agent-frameworks",
    "agent-sdks-libraries",
    "skills-systems",
    "coding-agents",
    "browser-agents",
    "research-agents",
    "multimodal",
    "multi-agent",
    "evaluation",
    "memory",
    "tooling",
    "automation",
}


def is_string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) and item.strip() for item in value)


def normalize_review_date(value: Any) -> tuple[str | None, str | None]:
    """Normalize last_reviewed to an ISO date string or return an error.

    YAML may parse unquoted dates as datetime.date. This helper keeps validation
    strict while supporting both canonical input forms.
    """
    if isinstance(value, dt.datetime):
        return value.date().isoformat(), None

    if isinstance(value, dt.date):
        return value.isoformat(), None

    if isinstance(value, str) and value.strip():
        return value, None

    return None, "last_reviewed must be a non-empty string or date"


def validate_entry(path: pathlib.Path, entry: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    missing = sorted(REQUIRED_FIELDS - set(entry.keys()))
    if missing:
        errors.append(f"missing fields: {', '.join(missing)}")
        return errors

    str_fields = [
        "name",
        "github_url",
        "description",
        "category",
        "subcategory",
        "language",
        "license",
        "maturity",
        "activity_status",
        "docs_quality",
    ]
    for field in str_fields:
        value = entry.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field} must be a non-empty string")

    reviewed_value, reviewed_type_error = normalize_review_date(entry.get("last_reviewed"))
    if reviewed_type_error:
        errors.append(reviewed_type_error)

    list_fields = ["tags", "use_cases", "deployment_type", "notable_features", "limitations", "related_projects"]
    for field in list_fields:
        if not is_string_list(entry.get(field)):
            errors.append(f"{field} must be a non-empty list of strings")

    if not isinstance(entry.get("beginner_friendly"), bool):
        errors.append("beginner_friendly must be boolean")

    category = entry.get("category")
    if category not in CATEGORIES:
        errors.append(f"category must be one of the canonical taxonomy values: {category!r}")

    if entry.get("maturity") not in MATURITY_VALUES:
        errors.append("maturity must be one of: experimental, beta, production")

    if entry.get("activity_status") not in ACTIVITY_VALUES:
        errors.append("activity_status must be one of: active, maintenance, inactive")

    if entry.get("docs_quality") not in DOCS_QUALITY_VALUES:
        errors.append("docs_quality must be one of: low, medium, high")

    deployment = entry.get("deployment_type", [])
    invalid_deployment = sorted(set(deployment) - DEPLOYMENT_VALUES) if isinstance(deployment, list) else []
    if invalid_deployment:
        errors.append(f"deployment_type contains invalid values: {', '.join(invalid_deployment)}")

    url = str(entry.get("github_url", ""))
    if not url.startswith("https://github.com/"):
        errors.append("github_url must start with https://github.com/")

    reviewed = reviewed_value or ""
    if reviewed and not DATE_RE.match(reviewed):
        errors.append("last_reviewed must match YYYY-MM-DD")
    elif reviewed:
        try:
            dt.datetime.strptime(reviewed, "%Y-%m-%d")
        except ValueError:
            errors.append("last_reviewed has an invalid calendar date")

    for idx, tag in enumerate(entry.get("tags", []), start=1):
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", tag):
            errors.append(f"tags[{idx}] must be lowercase kebab-case: {tag!r}")

    return errors


def load_entries(root: pathlib.Path) -> list[tuple[pathlib.Path, dict[str, Any]]]:
    files = sorted(root.rglob("*.yaml")) + sorted(root.rglob("*.yml"))
    results: list[tuple[pathlib.Path, dict[str, Any]]] = []

    for path in files:
        relative = path.relative_to(root)
        if len(relative.parts) < 2:
            raise ValueError(f"{path}: entry must be in data/repositories/<folder>/")
        folder = relative.parts[0]
        if folder not in ALLOWED_DATA_FOLDERS:
            raise ValueError(
                f"{path}: unknown data folder '{folder}'. "
                f"Allowed: {', '.join(sorted(ALLOWED_DATA_FOLDERS))}"
            )

        text = path.read_text(encoding="utf-8")
        parsed = yaml.safe_load(text)
        if not isinstance(parsed, dict):
            raise ValueError(f"{path}: root object must be a mapping")
        results.append((path, parsed))

    return results


def main() -> int:
    root = pathlib.Path("data/repositories")
    if not root.exists():
        print("ERROR: data/repositories directory not found")
        return 2

    try:
        entries = load_entries(root)
    except Exception as exc:  # pylint: disable=broad-except
        print(f"ERROR: failed to parse YAML files: {exc}")
        return 2

    if not entries:
        print("ERROR: no YAML entries found in data/repositories")
        return 2

    total_errors = 0
    for path, entry in entries:
        errors = validate_entry(path, entry)
        if errors:
            total_errors += len(errors)
            print(f"\n{path}:")
            for err in errors:
                print(f"  - {err}")

    if total_errors:
        print(f"\nValidation failed: {total_errors} issue(s) found across {len(entries)} file(s).")
        return 1

    print(f"Validation passed: {len(entries)} repository entries are schema-compliant.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
