# How To Use This Repo

## For tool evaluators

1. Start in `indexes/by-category.md`.
2. Pick candidate repositories.
3. Open YAML entries under `data/repositories/`.
4. Compare `notable_features`, `limitations`, and `maturity`.
5. Use `indexes/by-use-case.md` for scenario-first shortlisting.
6. Use `indexes/upstream-skill-sources.md` to review external skill ecosystems.

## For beginners

1. Read `wiki/beginners-guide.md`.
2. Use `indexes/beginner-friendly.md`.
3. Follow one path in `wiki/learning-paths.md`.

## For contributors

1. Copy the repo entry template.
2. Place the YAML file in a matching data folder.
3. Run validation and index generation scripts.
4. Update `data/upstream/skill-sources.yaml` when adding external skill sources.
5. Submit a pull request with evidence and review notes.
6. Check `.github/workflows/validate-repository.yml` for CI parity.

## For maintainers

- review taxonomy consistency first
- check claims against source docs
- ensure `last_reviewed` is current
- reject entries without limitations or concrete use cases
