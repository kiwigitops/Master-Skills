# Adoption Prompt For Existing Repositories

Use this prompt with another AI assistant when you want to retrofit an existing project to this repository's repo-of-repos model.

## Prompt

```text
You are upgrading an existing GitHub repository to align with the Agent Ecosystem Atlas model.

Goals:
1) Keep current project functionality intact.
2) Add a repo-of-repos curation layer for AI agent ecosystems.
3) Treat external skill repositories as primary sources (do not mirror or fork their content).
4) Add local operator skills for classification, summarization, extraction, comparison, and upstream source management.

Required outputs:
- docs updates:
  - docs/classification-system.md
  - docs/skills-system.md
  - docs/federated-skills.md
- data updates:
  - data/repositories/ (schema-compliant YAML entries)
  - data/upstream/skill-sources.yaml
- skills updates:
  - skills/repo-classifier/SKILL.md
  - skills/repo-summarizer/SKILL.md
  - skills/agent-type-detector/SKILL.md
  - skills/skill-extractor-from-repo/SKILL.md
  - skills/framework-comparator/SKILL.md
  - skills/upstream-skill-source-manager/SKILL.md
- scripts:
  - scripts/validate_repo_entries.py
  - scripts/generate_indexes.py
  - scripts/index_upstream_skills.py
- generated indexes:
  - indexes/by-category.md
  - indexes/by-use-case.md
  - indexes/by-language.md
  - indexes/beginner-friendly.md
  - indexes/upstream-skill-sources.md

Constraints:
- Keep everything original and project-specific.
- Use deterministic generation for committed index files.
- Enforce schema quality (required fields, controlled values, date format).
- Maintain beginner-friendly docs and contributor templates.
- Do not remove existing project features unrelated to this migration.

Process:
1) Audit current repository structure.
2) Map existing files to the target structure with minimal disruption.
3) Implement missing docs/data/skills/scripts.
4) Regenerate indexes.
5) Validate all entries.
6) Produce a concise migration summary with file-by-file changes and rationale.
```

## How to use it

1. Paste the prompt into your AI coding tool.
2. Add your repository-specific constraints (language, CI, existing folders).
3. Ask for a branch-safe migration (no destructive refactors).
