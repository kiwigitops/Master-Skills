---
name: repo-summarizer
description: Produce concise, comparable summaries of AI repositories for catalog entries and review notes.
category: analysis
inputs:
  - repository readme
  - docs snippets
  - optional release notes
outputs:
  - short summary
  - audience fit
  - strengths and limitations
  - suggested tags
tags:
  - summarization
  - curation
  - documentation
difficulty: beginner
---

# Repo Summarizer

## Description

Generate neutral, decision-focused summaries so maintainers can compare repositories without marketing noise.

## When to use

- A new entry needs a one-paragraph description.
- Existing entries are too verbose or promotional.
- A reviewer wants consistent project summaries across categories.

## How it works

1. Extract project intent, primary users, and core capability.
2. Separate objective features from claims.
3. Write a concise summary using plain language.
4. Return strengths, limitations, and beginner-fit notes.
5. Suggest 3-6 taxonomy-friendly tags.

## Examples

### Example 1

Input:
- README sections: Overview, Quickstart, Architecture

Output:
- summary: 2-4 sentences
- strengths: 3 bullets
- limitations: 2 bullets
- suggested tags: 4 normalized tags
