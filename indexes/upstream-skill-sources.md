# Upstream Skill Sources

Generated from `data/upstream/skill-sources.yaml`.
This index reflects the repo-of-repos model: external repositories are primary skill sources.

| Source | Repository | Skill roots | Detected SKILL.md files | Notes |
| --- | --- | --- | --- | --- |
| OpenAI Skills | [https://github.com/openai/skills](https://github.com/openai/skills) | skills/.curated<br />skills/.system | not fetched (run --fetch) | Use folder-per-skill and read frontmatter first. |
| Anthropic Skills | [https://github.com/anthropics/skills](https://github.com/anthropics/skills) | skills<br />template | not fetched (run --fetch) | Prioritize skills/ for practical examples and template/ for bootstrapping. |
| Awesome Copilot | [https://github.com/github/awesome-copilot](https://github.com/github/awesome-copilot) | skills | not fetched (run --fetch) | Treat skills as one primitive among agents, instructions, hooks, and workflows. |

## Usage

- Preview only (no network fetch):
  - `python scripts/index_upstream_skills.py`
- Fetch/update all configured sources and refresh counts:
  - `python scripts/index_upstream_skills.py --fetch`
