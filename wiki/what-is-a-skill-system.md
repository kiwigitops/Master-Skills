# What Is A Skill System

A skill system is a way to package reusable agent capability.

## Core idea

Instead of repeating instructions in every prompt, you store them once in a skill folder.

Each skill contains:
- metadata (name, purpose, inputs, outputs)
- execution instructions
- optional resources (examples, scripts, references)

## Why it matters

- faster onboarding
- more consistent outputs
- easier quality review
- easier reuse across teams

## Skill vs prompt

A single prompt is one-time guidance.
A skill is reusable workflow guidance with structure.

## Good skill characteristics

- explicit trigger conditions
- clear input/output contract
- deterministic steps where possible
- realistic examples
