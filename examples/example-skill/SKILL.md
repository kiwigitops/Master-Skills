---
name: example-entry-auditor
description: Demonstrate how to audit a repository entry for schema and taxonomy quality.
category: validation
inputs:
  - repository entry yaml
  - classification rules
outputs:
  - validation notes
  - suggested fixes
tags:
  - example
  - validation
  - schema
difficulty: beginner
---

# Example Entry Auditor

## Description

This example skill shows how to review one repository entry and return actionable quality feedback.

## When to use

- You are onboarding a new contributor.
- You need a lightweight quality check before a pull request.
- You want consistent review language across maintainers.

## How it works

1. Parse the entry and confirm all required fields exist.
2. Check category and subcategory consistency against taxonomy docs.
3. Verify `limitations`, `use_cases`, and `last_reviewed` are meaningful.
4. Return findings grouped by severity: blocking, warning, suggestion.

## Examples

### Example 1

Input:
- `data/repositories/agent-frameworks/langgraph.yaml`

Output:
- Blocking: none
- Warning: `subcategory` could be more specific
- Suggestion: add one more limitation focused on enterprise operation
