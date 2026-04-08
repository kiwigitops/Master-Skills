# Scripts Hub

Automation scripts for repository maintenance.

- `validate_repo_entries.py`: schema validation for YAML entries
- `generate_indexes.py`: generate markdown indexes from structured data
- `index_upstream_skills.py`: generate deterministic index for external skill repositories

## Local usage

```bash
pip install -r requirements.txt
python scripts/validate_repo_entries.py
python scripts/generate_indexes.py
python scripts/index_upstream_skills.py
```

Optional upstream discovery pass:

```bash
python scripts/index_upstream_skills.py --fetch
```
