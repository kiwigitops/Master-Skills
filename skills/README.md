# Skills Hub

Reusable skills for repository curation and comparison workflows.

These are **operator skills** for working with external skill repositories.
This project's primary skill implementations are upstream in repository sources listed at:

- `data/upstream/skill-sources.yaml`

## Included skills

| Skill | Primary role | Typical output |
| --- | --- | --- |
| `repo-classifier` | Map external repositories into canonical taxonomy categories | category, subcategory, tags, confidence notes |
| `repo-summarizer` | Create neutral, comparable repository summaries | concise summary, strengths, limitations, suggested tags |
| `agent-type-detector` | Detect primary and secondary agent patterns | primary type, secondary types, reasoning trace |
| `skill-extractor-from-repo` | Extract skill candidates and metadata from upstream repositories | candidate skill list, contracts, extraction notes |
| `framework-comparator` | Compare frameworks/skill repos for decision making | comparison matrix, recommendation, risks |
| `upstream-skill-source-manager` | Maintain and index upstream skill source manifest | refreshed source index, source health notes |

Each skill lives in `skills/<skill-name>/` and includes `SKILL.md` with required frontmatter.

See [docs/skills-system.md](../docs/skills-system.md) for the full contract.
