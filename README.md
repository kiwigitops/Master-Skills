<div align="center">

# Agent Ecosystem Atlas

**A schema-first, contributor-ready map of AI agent frameworks, SDKs, skills systems, and agent tooling.**

<p>
  <a href="https://github.com/kiwigitops/Master-Skills/stargazers"><img src="https://img.shields.io/github/stars/kiwigitops/Master-Skills?style=for-the-badge&logo=github&label=Star%20This%20Repo&color=f59e0b" alt="Star this repository" /></a>
  <a href="https://github.com/sponsors/kiwigitops"><img src="https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor this project" /></a>
</p>

<p>
  <sub>If this repository helps you, starring and sponsoring directly support ongoing curation.</sub>
</p>

<p>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-16a34a?style=flat-square" alt="License" /></a>
  <a href="./docs/schema.md"><img src="https://img.shields.io/badge/Schema-Structured_Data-1d4ed8?style=flat-square" alt="Schema" /></a>
  <a href="./docs/classification-system.md"><img src="https://img.shields.io/badge/Taxonomy-15_Categories-0f766e?style=flat-square" alt="Taxonomy" /></a>
  <a href="./docs/skills-system.md"><img src="https://img.shields.io/badge/Skills-System-7c3aed?style=flat-square" alt="Skills" /></a>
  <a href="./PRINCIPLES.md"><img src="https://img.shields.io/badge/Principles-First-475569?style=flat-square" alt="Principles" /></a>
</p>

<p>
  <a href="./indexes/by-category.md"><img src="https://img.shields.io/badge/Browse-Indexes-334155?style=flat-square" alt="Indexes" /></a>
  <a href="./wiki/beginners-guide.md"><img src="https://img.shields.io/badge/Beginner-Start_Here-0891b2?style=flat-square" alt="Beginner" /></a>
  <a href="./CONTRIBUTING.md"><img src="https://img.shields.io/badge/Contribute-Welcome-2563eb?style=flat-square" alt="Contribute" /></a>
  <a href="./SECURITY.md"><img src="https://img.shields.io/badge/Security-Policy-f59e0b?style=flat-square" alt="Security" /></a>
</p>

<p>
  <a href="#quick-start"><img src="https://img.shields.io/badge/Quick_Start-Run_Now-1f2937?style=flat-square" alt="Quick Start" /></a>
  <a href="./templates/repo-entry-template.md"><img src="https://img.shields.io/badge/Add_Repository-Template-1f2937?style=flat-square" alt="Add Repository" /></a>
  <a href="./templates/skill-template.md"><img src="https://img.shields.io/badge/Add_Skill-Template-1f2937?style=flat-square" alt="Add Skill" /></a>
</p>

</div>

---

## Why This Project

The AI agent ecosystem is moving fast. Decision quality falls when catalogs are inconsistent, promotional, or hard to maintain.

This repository is built to solve that with:

- a stable, explicit classification system
- structured YAML entries with validation
- reproducible generated indexes
- reusable skills for curation workflows
- contributor onboarding for both beginners and advanced maintainers

## At A Glance

| Signal | Value |
| --- | --- |
| Repository entries | 19 validated entries |
| Canonical taxonomy | 15 top-level categories |
| Reusable skills | 5 original skills |
| Generated indexes | 4 browse surfaces |
| Validation status | Script-validated in CI-ready workflow |

## Quick Navigation

- [Quick Start](#quick-start)
- [Who This Is For](#who-this-is-for)
- [Repository Structure](#repository-structure)
- [Classification System](#classification-system)
- [Skills System](#skills-system)
- [Data Schema](#data-schema)
- [Principles](#principles)
- [Indexes](#indexes)
- [Contributing](#contributing)
- [Roadmap](#roadmap)

## Quick Start

### 1. Install dependency

```bash
pip install -r requirements.txt
```

### 2. Validate data

```bash
python scripts/validate_repo_entries.py
```

### 3. Regenerate indexes

```bash
python scripts/generate_indexes.py
```

## Who This Is For

| Role | What You Get |
| --- | --- |
| Tool evaluators | Category-consistent entries with strengths and limitations |
| Engineers | Fast browsing by category, language, and use case |
| Beginners | Guided wiki docs and learning paths |
| Maintainers | Validation scripts, templates, and CI-ready structure |
| Contributors | Clear contribution flow with review checklist |

## Repository Structure

```text
.
|-- README.md
|-- LICENSE
|-- CONTRIBUTING.md
|-- CODE_OF_CONDUCT.md
|-- SECURITY.md
|-- SUPPORT.md
|-- .github/
|-- docs/
|-- wiki/
|-- data/repositories/
|-- skills/
|-- templates/
|-- scripts/
|-- indexes/
`-- examples/
```

### Key Paths

| Path | Purpose |
| --- | --- |
| `data/repositories/` | Canonical YAML catalog entries |
| `skills/` | Reusable skill packages (`SKILL.md` + optional resources) |
| `indexes/` | Generated browse views for discoverability |
| `docs/` | Core standards (taxonomy, schema, system design) |
| `wiki/` | Beginner-friendly conceptual learning content |
| `templates/` | Contributor templates for entries, skills, issues, and PRs |
| `scripts/` | Validation + index generation automation |
| `.github/` | Native GitHub issue/PR UX and CI workflow |

## Classification System

Every entry uses exactly one canonical category from a fixed 15-category taxonomy.

This prevents drift and enables clean comparison over time.

Read: [docs/classification-system.md](./docs/classification-system.md)

## Skills System

Skills are first-class artifacts, each in:

```text
skills/<skill-name>/SKILL.md
```

Required frontmatter fields:

- `name`
- `description`
- `category`
- `inputs`
- `outputs`
- `tags`
- `difficulty`

Read: [docs/skills-system.md](./docs/skills-system.md)

## Data Schema

Repository entries include decision-critical fields:

- identity: `name`, `github_url`, `description`
- classification: `category`, `subcategory`, `tags`
- quality signals: `maturity`, `activity_status`, `docs_quality`, `beginner_friendly`
- comparison support: `use_cases`, `notable_features`, `limitations`
- maintenance: `last_reviewed`

Read: [schema.md](./schema.md)

## Principles

This project is run with explicit quality and stewardship principles.

- Read: [PRINCIPLES.md](./PRINCIPLES.md)
- Release history: [CHANGELOG.md](./CHANGELOG.md)

## Indexes

- [By Category](./indexes/by-category.md)
- [By Use Case](./indexes/by-use-case.md)
- [By Language](./indexes/by-language.md)
- [Beginner-Friendly](./indexes/beginner-friendly.md)

## Beginner Path

Start here:

1. [Beginner's Guide](./wiki/beginners-guide.md)
2. [Agent Types Explained](./wiki/agent-types-explained.md)
3. [Choosing an Agent Framework](./wiki/choosing-an-agent-framework.md)
4. [Learning Paths](./wiki/learning-paths.md)

## Contributing

- Contributor guide: [CONTRIBUTING.md](./CONTRIBUTING.md)
- Repo template: [templates/repo-entry-template.md](./templates/repo-entry-template.md)
- Skill template: [templates/skill-template.md](./templates/skill-template.md)
- Issue template: [templates/issue_template.md](./templates/issue_template.md)
- PR template: [templates/pull_request_template.md](./templates/pull_request_template.md)

## Roadmap

- [x] Structured repository schema and taxonomy
- [x] Reusable skills system
- [x] Beginner wiki docs
- [x] Automated validation and index generation
- [x] GitHub-native issue/PR UX and CI workflow
- [ ] Expand entry volume with quarterly review cadence
- [ ] Add benchmark-backed comparison snapshots

## Quality Principles

- facts over hype
- explicit limitations in every entry
- deterministic generation and validation
- clean separation of production data vs examples
- original content (not direct mirrors/forks of seed repos)
