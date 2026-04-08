---
name: repo-classifier
description: Classify AI repositories into the atlas taxonomy using README intent, architecture clues, and repository metadata.
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

Classify one repository into a canonical category and produce a consistent metadata recommendation that matches this atlas.

## When to use

- A new repository needs a first classification.
- Existing entries have inconsistent categories.
- A contributor asks where a project belongs in the taxonomy.

## How it works

1. Read repository intent from README, docs, and examples.
2. Identify primary value surface (framework, sdk, coding agent, evaluation tool, etc.).
3. Select one canonical category and a reusable subcategory.
4. Propose normalized tags and explain edge-case tradeoffs.
5. Return confidence notes, including what evidence is missing.

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
