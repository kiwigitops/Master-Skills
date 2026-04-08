# Repository Entry Schema

This document specifies the required fields for every repository entry in `data/repositories/`.

## Required fields

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Project name |
| `github_url` | string | Canonical GitHub URL |
| `description` | string | One-paragraph summary |
| `category` | string | Canonical taxonomy category |
| `subcategory` | string | Narrow category label |
| `tags` | list[string] | Search and filtering tags |
| `language` | string | Primary language (`multi` allowed) |
| `license` | string | SPDX-style or common license name |
| `maturity` | string | `experimental`, `beta`, or `production` |
| `activity_status` | string | `active`, `maintenance`, or `inactive` |
| `docs_quality` | string | `low`, `medium`, or `high` |
| `beginner_friendly` | boolean | Beginner onboarding signal |
| `use_cases` | list[string] | Real-world usage intents |
| `deployment_type` | list[string] | Deployment styles |
| `notable_features` | list[string] | Key capabilities |
| `limitations` | list[string] | Known constraints |
| `related_projects` | list[string] | Related repositories or tools |
| `last_reviewed` | date string | `YYYY-MM-DD` |

## Optional fields

- `notes`: free-form reviewer notes
- `example_only`: set to `true` for non-production sample entries

## YAML example

```yaml
name: Example Agent Framework
github_url: https://github.com/example/agent-framework
description: Example entry showing expected schema structure.
category: Agent Frameworks
subcategory: graph orchestrator
tags:
  - orchestration
  - agents
  - workflow
language: python
license: MIT
maturity: production
activity_status: active
docs_quality: high
beginner_friendly: true
use_cases:
  - multi-step tool workflows
  - long-running agent tasks
deployment_type:
  - local
  - cloud
notable_features:
  - graph-based orchestration
  - retry-aware execution
limitations:
  - advanced setup for large teams
related_projects:
  - https://github.com/example/agent-sdk
last_reviewed: 2026-04-08
example_only: true
```

## Validation behavior

`python scripts/validate_repo_entries.py` checks:
- field presence
- type correctness
- allowed value constraints
- basic URL and date format rules
