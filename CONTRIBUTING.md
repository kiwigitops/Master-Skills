# Contributing

Thank you for helping improve the Agent Ecosystem Atlas.

## Contribution flow

1. Open an issue or choose an existing one.
2. Create a focused branch.
3. Make one logical change set.
4. Run validation scripts locally.
5. Open a pull request using the project template.

## Before you start

- read `docs/classification-system.md`
- read `docs/schema.md`
- read `PRINCIPLES.md`
- run local validation before opening a PR

## How to add a repository entry

1. Copy `templates/repo-entry-template.md`.
2. Fill every required field with concrete, verifiable information.
3. Place the YAML file under the best matching folder in `data/repositories/`.
4. Run:
   - `python scripts/validate_repo_entries.py`
   - `python scripts/generate_indexes.py`
5. Include rationale for category and beginner-friendly status in your PR.

## How to add a skill

1. Copy `templates/skill-template.md` into `skills/<new-skill-name>/SKILL.md`.
2. Keep frontmatter complete and accurate.
3. Include required sections: Description, When to use, How it works, Examples.
4. Add `examples.md` or `scripts/` only when they add practical value.

## Review checklist

- schema fields are complete and correctly typed
- category and subcategory are consistent with taxonomy
- limitations are realistic and non-empty
- no promotional wording
- dates are in `YYYY-MM-DD`
- links resolve

## Tagging rules

- lowercase kebab-case only
- 3-10 tags per entry
- avoid generic tags like `ai` unless needed

## Naming rules

Repository entry filenames:
- lowercase kebab-case
- include project name only (for example `langgraph.yaml`)

Skill folder names:
- lowercase kebab-case
- verb- or purpose-oriented (for example `framework-comparator`)

## Pull request expectations

- one logical change set per PR
- explain source references used for classification decisions
- mention any fields that required estimation
- keep discussion factual and neutral (no promotional language)
- align changes with `PRINCIPLES.md`

## Branch and commit naming

Branch naming examples:

- `feat/add-new-research-agent-entry`
- `fix/schema-validation-date-normalization`
- `docs/improve-beginners-guide`

Commit style examples:

- `feat(data): add new coding-agents entry for project-x`
- `fix(scripts): enforce allowed data folders in validator`
- `docs(readme): improve quick navigation and contribution UX`
