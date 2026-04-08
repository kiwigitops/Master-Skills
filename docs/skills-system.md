# Skills System

This repository includes a reusable skill packaging system for agent workflows.

## Skill directory contract

Each skill lives in:

`skills/<skill-name>/`

Required:
- `SKILL.md`

Optional:
- `examples.md`
- `scripts/`
- `references/`
- `assets/`

## Required frontmatter

`SKILL.md` must start with YAML frontmatter containing:

- `name`
- `description`
- `category`
- `inputs`
- `outputs`
- `tags`
- `difficulty`

Example:

```yaml
---
name: repo-classifier
description: Classify AI repositories into the atlas taxonomy.
category: taxonomy
inputs:
  - repository url
  - readme text
outputs:
  - category
  - subcategory
  - confidence notes
tags:
  - classification
  - curation
  - metadata
difficulty: intermediate
---
```

## Required content sections

After frontmatter, each skill must include these sections:

1. Description
2. When to use
3. How it works
4. Examples

## Skill quality checklist

A good skill should:
- define clear trigger conditions
- specify input assumptions
- produce structured outputs
- include at least one realistic example
- avoid vague universal instructions

## Naming rules

- lowercase letters, digits, and hyphens only
- keep names under 64 characters
- use purpose-driven names (`framework-comparator`, not `framework-helper-v2`)

## Versioning and updates

- update frontmatter and examples together
- keep instructions concise and task-specific
- if behavior changes, document changes in the skill body

## Boundary between skills and docs

- docs explain concepts for humans
- skills encode repeatable workflows for agents

Use docs for tutorials. Use skills for execution patterns.
