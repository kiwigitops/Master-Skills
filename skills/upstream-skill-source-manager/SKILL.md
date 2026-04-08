---
name: upstream-skill-source-manager
description: Manage and index upstream skill repositories defined in data/upstream/skill-sources.yaml for this repo-of-repos project.
category: federation
inputs:
  - upstream source manifest
  - optional fetch flag
outputs:
  - refreshed upstream source index
  - detected skill counts
  - source health notes
tags:
  - upstream
  - skills
  - indexing
  - repo-of-repos
difficulty: intermediate
---

# Upstream Skill Source Manager

## Description

Use this skill when maintaining external skill repository integrations. It treats external repositories as primary skill sources and keeps local indexes in sync.

## When to use

- A new upstream skill repository should be tracked.
- Existing upstream sources need re-indexing.
- You want fresh counts of detected `SKILL.md` files.

## How it works

1. Update `data/upstream/skill-sources.yaml` with source metadata.
2. Run `python scripts/index_upstream_skills.py` for manifest-only index generation.
3. Run `python scripts/index_upstream_skills.py --fetch` to clone/update sources and count discovered skills.
4. Review `indexes/upstream-skill-sources.md` and commit changes.

## Output format

```yaml
updated_sources:
  - id: openai-skills
index_path: indexes/upstream-skill-sources.md
fetch_mode: false
health_notes:
  - all github_url values are valid
  - no duplicate source ids detected
```

## Quality checks

- each source has a unique `id`
- `github_url` points to GitHub repository roots
- `skills_roots` are explicit and non-empty
- manifest updates do not mirror upstream content into local `skills/`

## Examples

### Example 1

Input:
- add a new source repo with a `skills/` root

Output:
- source appears in `indexes/upstream-skill-sources.md`
- detected `SKILL.md` count is reported after `--fetch`
