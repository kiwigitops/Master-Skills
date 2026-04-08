---
name: framework-comparator
description: Compare two or more agent frameworks using consistent criteria for architecture, usability, operations, and ecosystem fit.
category: comparison
inputs:
  - framework names
  - target use case
  - team constraints
outputs:
  - comparison matrix
  - recommendation
  - tradeoff notes
  - adoption risks
tags:
  - comparison
  - frameworks
  - decision-support
difficulty: intermediate
---

# Framework Comparator

## Description

Produce a structured comparison of frameworks so teams can choose tools based on fit, not hype.

## When to use

- Selecting a framework for a new build.
- Re-evaluating an existing stack.
- Preparing architecture review material for stakeholders.

## How it works

1. Establish decision criteria (developer experience, reliability, extensibility, cost).
2. Score each framework against those criteria with evidence.
3. Highlight scenario-specific tradeoffs.
4. Recommend one primary option and one fallback option.

## Examples

### Example 1

Input:
- frameworks: LangGraph, AutoGen
- use case: long-running tool workflows with human approvals

Output:
- matrix with weighted criteria
- recommendation: primary + fallback
- risks: migration complexity and observability gaps
