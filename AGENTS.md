# Coding-agent instructions (Codex, Claude, and similar tools)

## Mission and hard boundaries

- Improve **only this synthetic localization engineering showcase**.
- This repo is not the real Princes of Darkness Turkish translation.
- **Never request, fetch, reconstruct, scrape, clone, copy or submit** production
  PoD/CK3/StrategyTürk files, real localization strings, translation memory,
  private Git repositories, raw reports, release artifacts or credentials.
- Do not use web search, user-supplied personal machine paths or external language
  models to import real game text. The fictional fixtures are enough.
- Keep the public allowlist policy in `docs/allowlist.md`. If adding files,
  extend its list deliberately and describe why each is safe.
- The original showcase code, synthetic fixtures and documents are MIT-licensed
  (see `LICENSE`); preserve copyright/license notices in substantial copies.
  Never infer that this licenses the private PoD translation, game/mod assets,
  third-party trademarks or proprietary data.
- Only submit original or MIT-compatible contributions; do not import code
  with incompatible licensing or unconfirmed ownership.
- No changes to private repositories, Steam Workshop, game installs or upstream mods.
- Do not present synthetic demo output as a working CK3 mod.

## Architecture: read first

1. `README.md` — purpose, quick start, limits.
2. `docs/architecture.md` — accepted syntax and verification contract.
3. `docs/allowlist.md` — explicit publication boundary.
4. `CONTRIBUTING.md` — tests, review and contribution rules.
5. `docs/ROADMAP.md` — optional scoped tasks.

Core implementation: `tools/showcase.py`.
Fixtures: `fixtures/synthetic/`.
Tests: `tests/test_showcase.py`.
Python 3.10+ **standard library only**; no API keys and no network needed.

## Working procedure

- Read the relevant code and tests before editing.
- Keep changes bounded. Prefer one concern per pull request.
- Add a positive test and a negative/adversarial test for new parsing,
  substitution, path or ZIP-handling behavior.
- Preserve deterministic archives, UTF-8 BOM, LF, sorted members and token
  multiplicities unless a task explicitly and safely changes the contract.
- Do not loosen validators merely to make a test pass.
- Explain limits: this is not a general YAML/CK3 parser, translator, or game tester.
- GitHub Actions is disabled; report the exact local test results instead.
- Avoid unnecessary dependencies and large/generated files.

## Verification before finishing

```bash
python -m unittest discover -s tests -v
python tools/showcase.py demo --out build
python tools/showcase.py verify build/demo.zip build/manifest.json
```

The generated `build/` directory is ignored. Ensure no actual game strings,
personal paths, tokens or private data appear in the diff.

## Response / pull request expectations

Report what changed, why, commands run and their exact outcomes, remaining risks,
and whether any public-file scope was expanded. Do not claim game compatibility.
If unsure about content ownership, stop and ask for an owner's decision; do not
invent a permissive license or silently add third-party materials.
