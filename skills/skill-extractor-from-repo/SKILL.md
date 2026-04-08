---
name: skill-extractor-from-repo
description: Extract reusable skill metadata from upstream repositories by identifying folder-per-skill structures, SKILL.md files, and repeated workflow patterns.
category: extraction
inputs:
  - repository structure
  - readme and docs
  - scripts and command references
outputs:
  - proposed skill list
  - per-skill scope
  - starter frontmatter
  - implementation notes
tags:
  - skill-design
  - extraction
  - reuse
difficulty: advanced
---

# Skill Extractor From Repo

## Description

Extract structured skill candidates and metadata from external repositories so they can be indexed in a repo-of-repos workflow.

## When to use

- An upstream repository appears to contain skills.
- You need to map external skills into this repository's metadata model.
- Team knowledge is trapped in scattered docs and scripts.

## How it works

1. Detect `SKILL.md` files and likely skill roots in the external repository.
2. Scan docs and scripts for recurring workflows.
3. Group steps into candidate skill boundaries.
4. Define input/output contracts for each candidate.
5. Generate starter metadata suggestions for indexing and local adapters.
6. Flag workflows that should stay as docs instead of skills.

## Output format

```yaml
source_repository: https://github.com/org/repo
detected_skill_files:
  - skills/release-checker/SKILL.md
candidate_skills:
  - name: release-checker
    purpose: pre-release verification workflow
    inputs:
      - target version
    outputs:
      - release readiness report
notes:
  - Keep one candidate as docs-only due to weak repeatability.
```

## Quality checks

- tie each candidate to specific repository evidence
- avoid creating skills from one-off maintenance tasks
- preserve source context so reviewers can verify extraction
- separate executable workflows from narrative documentation

## Examples

### Example 1

Input:
- deployment runbook with repeated staging checks

Output:
- proposed skill: `staging-release-checker`
- required inputs: environment and target release
- outputs: checklist status and blocking risks
