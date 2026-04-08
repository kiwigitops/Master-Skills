# Getting Started

## 1. Clone and install dependencies

```bash
git clone <your-fork-url>
cd Master-Skills
pip install -r requirements.txt
```

## 2. Validate repository entries

```bash
python scripts/validate_repo_entries.py
```

## 3. Generate markdown indexes

```bash
python scripts/generate_indexes.py
```

## 4. Read core docs

- `docs/how-to-use-this-repo.md`
- `docs/classification-system.md`
- `docs/skills-system.md`
- `docs/schema.md`

## 5. Start contributing

- add a new entry with `templates/repo-entry-template.md`
- add a new skill with `templates/skill-template.md`
- submit with the pull request template

## 6. CI behavior

Pull requests run repository validation and index checks via:

- `.github/workflows/validate-repository.yml`
