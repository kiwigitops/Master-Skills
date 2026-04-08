# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog and this project follows semantic versioning principles.

## [1.1.0] - 2026-04-08

### Added

- Federated upstream skill source model:
  - `data/upstream/skill-sources.yaml`
  - `indexes/upstream-skill-sources.md`
  - `scripts/index_upstream_skills.py`
- New `Skills Systems` repository entry:
  - `Awesome Copilot`
- New local operator skill:
  - `upstream-skill-source-manager`
- Contributor template for upstream skill sources:
  - `templates/upstream-skill-source-template.yaml`
- New docs:
  - `docs/federated-skills.md`
  - `docs/adoption-prompt.md`
  - `docs/releases/v1.1.0.md`
- Native GitHub Sponsors metadata:
  - `.github/FUNDING.yml`

### Changed

- Skills system documentation now enforces an upstream-first repo-of-repos model.
- Core skills upgraded with clearer output contracts and quality checks.
- README improved for trust and conversion with CI + update badges and clearer star-value framing.
- CI workflow now installs dependencies from `requirements.txt`.

## [1.0.0] - 2026-04-08

### Added

- Complete repository architecture for cataloging AI agent ecosystem projects.
- Canonical 15-category classification system and schema documentation.
- Reusable skills system with five original skills:
  - `repo-classifier`
  - `repo-summarizer`
  - `agent-type-detector`
  - `skill-extractor-from-repo`
  - `framework-comparator`
- Structured repository entries across major ecosystem segments.
- Beginner wiki guides and learning paths.
- Contributor templates and contributor workflow documentation.
- GitHub-native community and workflow files:
  - issue templates
  - pull request template
  - CI validation workflow
  - security and support policies
- Validation and index generation automation scripts.
- Principles-first governance document (`PRINCIPLES.md`).

### Changed

- README redesigned with professional navigation and contributor UX.
- Index generation improved with deterministic ordering and richer metadata display.
- Validator hardened for YAML date parsing and data-folder integrity checks.

### Security

- Added a dedicated `SECURITY.md` for private vulnerability reporting flow.
