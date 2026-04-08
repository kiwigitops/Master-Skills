# Skill Template

Create a folder `skills/<skill-name>/` and place this file as `SKILL.md`.

```markdown
---
name: <skill-name>
description: <What this skill does and when it should be used>
category: <taxonomy|analysis|comparison|...>
inputs:
  - <input one>
  - <input two>
outputs:
  - <output one>
  - <output two>
tags:
  - <tag-one>
  - <tag-two>
difficulty: <beginner|intermediate|advanced>
---

# <Skill Title>

## Description

<Explain the purpose and boundaries of the skill.>

## When to use

- <Trigger condition one>
- <Trigger condition two>

## How it works

1. <Step one>
2. <Step two>
3. <Step three>

## Examples

### Example 1

Input:
- <input>

Output:
- <expected output>
```

Optional additions:
- `examples.md`
- `scripts/`
- `references/`
