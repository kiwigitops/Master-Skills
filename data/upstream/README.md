# Upstream Source Manifests

This folder tracks external repositories that act as primary skill sources.

## Files

- `skill-sources.yaml`: list of upstream repositories, skill roots, and discovery hints.
- `templates/upstream-skill-source-template.yaml`: snippet for adding new sources.

## Typical workflow

1. Update `skill-sources.yaml`.
2. Run `python scripts/index_upstream_skills.py`.
3. Optionally run `python scripts/index_upstream_skills.py --fetch` for local discovery checks.
4. Commit updated `indexes/upstream-skill-sources.md` generated without `--fetch`.
