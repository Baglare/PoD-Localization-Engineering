# Contributing to PoD Localization Engineering

This public repository demonstrates **original engineering code with fictional
data**. It does not contain the production localization or the full private
pipeline. You can run and propose improvements to this MIT-licensed showcase,
without importing private or third-party game material.

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
integrity tests, synthetic fixtures, documentation and local test automation.
GitHub Actions is intentionally disabled to conserve account quota.

Never contribute real localization strings, mod/game assets, StrategyTürk text,
private translation memory, raw production logs or private Git history.
Do not upload them to AI coding tools or pull requests. Do not modify or
distribute real-world copyrighted content from this sample project.

## Reporting and proposing work

For bugs or enhancements to the synthetic demo, use GitHub Issues and select
the appropriate issue template. Describe a minimal repro with **fictional**
inputs and exact commands, not a real game localization sample.
For suspected infringement, licensing or privacy complaints, avoid public
Issues: email **bparilti123123@gmail.com** privately with a reference to the
affected file/URL and your concern. See [SECURITY.md](SECURITY.md).

## License and contribution terms

This repository is published under the [MIT License](LICENSE).
You may use, adapt and redistribute the original showcase material under
its terms. Preserve the license and copyright notice in copies or substantial
portions.

By opening a pull request, you confirm that you are entitled to submit the
contribution (your own work or material compatible with MIT) and intend it
to be distributed under the MIT License, without additional restrictions.
You retain copyright in your contribution. Do not submit copied game/mod
content, private repository data, proprietary examples or work that violates
third-party licenses, confidentiality or contractual duties.

MIT licensing of this sample does **not** grant access to the actual PoD
Turkish localization, or rights over third-party games, translations,
trademarks or artwork.

## Review checklist

- [ ] Synthetic-only inputs, no private or third-party game content
- [ ] All added files recorded in `docs/allowlist.md`
- [ ] Tests pass locally (GitHub Actions is disabled due to account quota)
- [ ] No network calls, credentials, local absolute paths or generated ZIPs
- [ ] README/architecture updated when changing the public contract
- [ ] No false production compatibility or game-runtime claims
