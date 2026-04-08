---
name: skill-extractor-from-repo
description: Extract reusable skill candidates from a repository by identifying repeated workflows, scripts, and domain-specific procedures.
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

Convert repeated repository workflows into candidate skills that can be packaged under `skills/<skill-name>/`.

## When to use

- A project has repeatable command sequences.
- Team knowledge is trapped in scattered docs.
- You want to create skills from existing operational playbooks.

## How it works

1. Scan docs and scripts for recurring workflows.
2. Group steps into candidate skill boundaries.
3. Define input/output contracts for each candidate.
4. Generate starter `SKILL.md` metadata suggestions.
5. Flag workflows that should stay as docs instead of skills.

## Examples

### Example 1

Input:
- deployment runbook with repeated staging checks

Output:
- proposed skill: `staging-release-checker`
- required inputs: environment and target release
- outputs: checklist status and blocking risks
