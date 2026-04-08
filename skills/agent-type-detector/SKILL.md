---
name: agent-type-detector
description: Detect the most likely agent type for a repository based on capabilities, interfaces, and execution model.
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

Determine whether a project is best described as a coding, research, browser/computer-use, workflow, multimodal, or multi-agent system.

## When to use

- Category assignment is ambiguous.
- A repository spans multiple agent patterns.
- Reviewers disagree on primary project type.

## How it works

1. Identify the main execution surface (code editing, research synthesis, UI actions, etc.).
2. Map that surface to a primary agent type.
3. Capture secondary types only when they materially impact usage.
4. Provide confidence and explain conflicting signals.

## Examples

### Example 1

Input:
- Features: reads codebase, edits files, runs tests, opens PRs

Output:
- primary: `Coding Agents`
- secondary: `Workflow / Automation`
- confidence: high
