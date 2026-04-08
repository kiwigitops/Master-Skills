# Federated Skills Model

This project is a repo-of-repos.

## Core rule

External repositories are primary skill sources.
Local `skills/` are operator skills used to curate, classify, and index those sources.

## Source of truth

- Upstream source manifest: `data/upstream/skill-sources.yaml`
- Source template: `templates/upstream-skill-source-template.yaml`
- Generated upstream index: `indexes/upstream-skill-sources.md`

## Why this model

- avoids duplicating large upstream skill collections
- keeps this repository focused on mapping and comparison
- supports continuous ingestion as upstream repositories evolve

## Operator workflow

1. Update `data/upstream/skill-sources.yaml`.
2. Run `python scripts/index_upstream_skills.py`.
3. Optionally run `python scripts/index_upstream_skills.py --fetch` for detected skill counts.
4. Validate repository data and regenerate standard indexes.
5. Submit PR with source rationale and review notes.

Before committing, regenerate `indexes/upstream-skill-sources.md` without `--fetch` to keep index output deterministic.
