# Contributing to PoD Localization Engineering

This public repository demonstrates **original engineering code with fictional
data**. It does not contain the production localization or the full private
pipeline. You can run and propose improvements to the demonstration, subject to
the currently unresolved licensing and contribution-rights questions below.

## Start here

1. Read `README.md`, `AGENTS.md`, `docs/architecture.md` and
   `docs/allowlist.md`.
2. Use Python 3.10+ (standard library; no third-party installs).
3. Run:
   ```bash
   python -m unittest discover -s tests -v
   python tools/showcase.py demo --out build
   python tools/showcase.py verify build/demo.zip build/manifest.json
   ```
4. Make your change in a branch or fork; keep the scope narrow.
5. For each behavior change, add tests covering expected and rejected cases.
6. Open a pull request describing the motivation, tests and any new fixture or
   file; do not claim production validation.

## Safe work

Suitable examples: token grammar hardening (within fictional syntax), better
schema validation, reproducible packaging, precise error handling, manifest
integrity tests, synthetic fixtures, documentation and CI.

Never contribute real localization strings, mod/game assets, StrategyTürk text,
private translation memory, raw production logs or private Git history.
Do not upload them to AI coding tools or pull requests. Do not modify or
distribute real-world copyrighted content from this sample project.

## License and contribution status

**No open-source license is currently granted.** GitHub's public/fork
functionality does not confer a general permission to redistribute, sublicense
or use the implementation in another product. The owner must complete
a rights review and choose a license before treating this as a fully open-source
contribution project. Contributors should clarify intended reuse terms with the
owner before investing substantial work; unsolicited patches may not be accepted.

## Review checklist

- [ ] Synthetic-only inputs, no private or third-party game content
- [ ] All added files recorded in `docs/allowlist.md`
- [ ] Tests pass locally (GitHub Actions is disabled due to account quota)
- [ ] No network calls, credentials, local absolute paths or generated ZIPs
- [ ] README/architecture updated when changing the public contract
- [ ] No false production compatibility or game-runtime claims
