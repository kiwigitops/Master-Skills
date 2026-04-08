---
name: framework-comparator
description: Compare two or more external agent frameworks or skill repositories using consistent criteria for architecture, usability, operations, and ecosystem fit.
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

Produce a structured comparison of external repositories so teams can choose frameworks and skill ecosystems based on fit, not hype.

## When to use

- Selecting frameworks or skill repositories for a new build.
- Re-evaluating an existing stack against upstream alternatives.
- Preparing architecture review material for stakeholders.

## How it works

1. Establish decision criteria (developer experience, reliability, extensibility, cost).
2. Score each framework against those criteria with evidence.
3. Highlight scenario-specific tradeoffs.
4. Recommend one primary option and one fallback option.

## Output format

```yaml
comparison_matrix:
  - criterion: extensibility
    option_a: high
    option_b: medium
recommendation:
  primary: LangGraph
  fallback: AutoGen
tradeoffs:
  - AutoGen has stronger multi-agent defaults.
risks:
  - migration complexity
```

## Quality checks

- criteria map to the stated team constraints
- every score includes evidence (docs, architecture, examples)
- recommendation includes at least one material downside
- fallback option remains viable for the same use case

## Examples

### Example 1

Input:
- frameworks: LangGraph, AutoGen
- use case: long-running tool workflows with human approvals

Output:
- matrix with weighted criteria
- recommendation: primary + fallback
- risks: migration complexity and observability gaps
