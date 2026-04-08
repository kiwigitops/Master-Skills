---
name: repo-classifier
description: Classify external AI repositories (including upstream skill repos) into the atlas taxonomy using README intent, architecture clues, and repository metadata.
category: taxonomy
inputs:
  - github repository url
  - readme or docs text
  - optional existing tags
outputs:
  - category
  - subcategory
  - normalized tags
  - confidence notes
tags:
  - classification
  - taxonomy
  - curation
difficulty: intermediate
---

# Repo Classifier

## Description

Classify one external repository into a canonical category and produce consistent metadata for repo-of-repos indexing.

## When to use

- A new external repository needs first classification.
- Existing entries have inconsistent categories.
- A contributor asks where an upstream skill repository belongs in the taxonomy.

## How it works

1. Read repository intent from README, docs, and examples.
2. Identify primary value surface (framework, sdk, coding agent, evaluation tool, etc.).
3. Select one canonical category and a reusable subcategory.
4. For skill-centric repositories, mark them under `Skills Systems` unless another function is clearly primary.
5. Propose normalized tags and explain edge-case tradeoffs.
6. Return confidence notes, including what evidence is missing.

## Output format

```yaml
category: Agent Frameworks
subcategory: graph orchestrator
tags:
  - orchestration
  - stateful-agents
  - workflows
confidence: high
reasoning:
  - Primary value is workflow orchestration.
missing_evidence:
  - No benchmark data in repository docs.
```

## Quality checks

- exactly one canonical category
- subcategory stays reusable across multiple projects
- tags are lowercase kebab-case and non-promotional
- confidence explains uncertainty, not just score labels

## Examples

### Example 1

Input:
- URL: `https://github.com/langchain-ai/langgraph`
- README: graph-based orchestration for agent workflows

Output:
- category: `Agent Frameworks`
- subcategory: `graph orchestrator`
- tags: `orchestration`, `stateful-agents`, `workflows`
- confidence: high
