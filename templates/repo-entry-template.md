# Repository Entry Template

Use this template when adding a new file under `data/repositories/`.

```yaml
name: <Project name>
github_url: <https://github.com/org/repo>
description: <Short, factual summary>
category: <One canonical category from docs/classification-system.md>
subcategory: <Narrow reusable label>
tags:
  - <tag-one>
  - <tag-two>
  - <tag-three>
language: <python|typescript|go|rust|multi|...>
license: <MIT|Apache-2.0|...>
maturity: <experimental|beta|production>
activity_status: <active|maintenance|inactive>
docs_quality: <low|medium|high>
beginner_friendly: <true|false>
use_cases:
  - <use case one>
  - <use case two>
deployment_type:
  - <local|cloud|hybrid|api|self-hosted|managed>
notable_features:
  - <feature one>
  - <feature two>
limitations:
  - <limitation one>
  - <limitation two>
related_projects:
  - <https://github.com/org/related-repo>
last_reviewed: <YYYY-MM-DD>
```

Notes:
- Keep descriptions neutral and specific.
- Do not leave `limitations` empty.
- Use one canonical `category` only.
