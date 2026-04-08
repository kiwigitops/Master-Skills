---
name: repo-summarizer
description: Produce concise, comparable summaries of external AI repositories for catalog entries, including upstream skill repositories.
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

Generate neutral, decision-focused summaries so maintainers can compare external repositories without marketing noise.

## When to use

- A new external repository entry needs a one-paragraph description.
- Existing entries are too verbose or promotional.
- A reviewer wants consistent summaries for upstream skill source repos.

## How it works

1. Extract project intent, primary users, and core capability.
2. Separate objective features from claims.
3. Write a concise summary using plain language.
4. Return strengths, limitations, and beginner-fit notes.
5. Suggest 3-6 taxonomy-friendly tags.

## Output format

```yaml
summary: Framework for...
audience_fit:
  - platform engineers
  - applied ML teams
strengths:
  - explicit state management
  - strong docs
limitations:
  - migration overhead for existing stacks
suggested_tags:
  - orchestration
  - workflows
```

## Quality checks

- summary is factual and does not include marketing language
- strengths and limitations are evidence-backed
- output can be compared side-by-side with other entries
- tags are useful for filtering, not vanity keywords

## Examples

### Example 1

Input:
- README sections: Overview, Quickstart, Architecture

Output:
- summary: 2-4 sentences
- strengths: 3 bullets
- limitations: 2 bullets
- suggested tags: 4 normalized tags
