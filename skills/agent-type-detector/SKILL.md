---
name: agent-type-detector
description: Detect the most likely agent type for an external repository based on capabilities, interfaces, and execution model.
category: classification
inputs:
  - repository description
  - feature list
  - usage examples
outputs:
  - primary agent type
  - secondary types
  - reasoning trace
  - confidence level
tags:
  - agent-types
  - classification
  - analysis
difficulty: intermediate
---

# Agent Type Detector

## Description

Determine whether an external project is best described as coding, research, browser/computer-use, workflow, multimodal, multi-agent, or skills-system infrastructure.

## When to use

- Category assignment is ambiguous.
- A repository spans multiple agent patterns.
- Reviewers disagree on whether a project should be `Skills Systems` versus another agent type.

## How it works

1. Identify the main execution surface (code editing, research synthesis, UI actions, etc.).
2. Map that surface to a primary agent type.
3. Capture secondary types only when they materially impact usage.
4. Provide confidence and explain conflicting signals.

## Output format

```yaml
primary_type: Coding Agents
secondary_types:
  - Workflow / Automation
confidence: high
signals:
  - Includes git-aware code editing loops.
  - Includes automation primitives for CI tasks.
conflicts:
  - Also ships generic framework abstractions.
```

## Quality checks

- pick one primary type only
- secondary types must impact real-world adoption decisions
- include at least one direct signal from docs or examples
- make ambiguity explicit when signals conflict

## Examples

### Example 1

Input:
- Features: reads codebase, edits files, runs tests, opens PRs

Output:
- primary: `Coding Agents`
- secondary: `Workflow / Automation`
- confidence: high
