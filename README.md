# PoD Localization Engineering

A compact public engineering showcase, conceptually extracted from
**Princes-of-Darkness-Turkce**, a real Turkish localization project distributed
through **Steam Workshop**. The production repository remains private.

This repository contains newly written engineering demonstrations and a tiny
fictional dataset. It does **not** contain or redistribute the actual PoD
localization corpus, upstream source material, production Turkish output,
translation memory, StrategyTurk-derived data or game/mod assets.

## The engineering problem

Large-scale localization needs reliable processing around translation:
per-key traceability, protected runtime syntax, consistent terminology,
bounded review, repeatable outputs and verifiable release artifacts. A natural
translation can still break a placeholder, reference or runtime lookup.

## Verified production workflow and scale

The private project uses CSV translation memory and terminology, bounded batches
(up to 1,000 entries / 20,000 source words), a second context pass for ambiguity,
structural and semantic QA, integration and runtime-key recovery, static release
gates, deterministic ZIP assembly, SHA-256 manifests, CRC/member checks and
manual game smoke before release. This demonstration implements a small subset;
it does not reproduce the production pipeline or its language review system.

| Private production metric, verified 2026-10-02 | Count |
| --- | ---: |
| Translation-memory rows | 87,865 |
| Upstream localization files across all language folders | 965 |
| Active English source / generated Turkish localization files | 460 / 460 |

These are production metrics, **not this repository's dataset** or counts of
newly translated sentences. The 965 total includes 498 Chinese files and seven
other-language files in addition to the 460 English files.
[Evidence and historical QA](docs/production-evidence.md) distinguish recorded
release results from checks run on this showcase.

## Run the synthetic demonstration

Python 3.10+; standard library only; no downloads, APIs or game installation.
From the repository root:

```sh
python -m unittest discover -s tests -v
python tools/showcase.py demo --out build
python tools/showcase.py verify build/demo.zip build/manifest.json
```

Four fictional entries demonstrate placeholders, references, icons, formatting,
literal escapes, protected terminology replacement and sorted output. Negative
tests exercise malformed input, token loss, duplicate keys and artifact changes.
The demo emits a BOM-prefixed `l_demo` localization file in a deterministic ZIP,
plus a separate SHA-256 manifest. `l_demo` is fictional and is not a playable mod.

[Architecture and limitations](docs/architecture.md) explain the contracts.
[The strict allowlist](docs/allowlist.md) records the publication boundary.
[Validation](docs/validation.md) records this repository's checks.

## Contributing and AI-assisted development

This is an **independently runnable synthetic demonstration**, not the playable
Turkish translation and not a mirror of the private production repository.
See [CONTRIBUTING.md](CONTRIBUTING.md) for a safe local workflow,
[AGENTS.md](AGENTS.md) for Codex/Claude/other coding agents,
[docs/ROADMAP.md](docs/ROADMAP.md) for scoped enhancements and
[SECURITY.md](SECURITY.md) for disclosure and data-handling rules.

Please use **only fictional test data**. Never upload, paste or copy real PoD,
CK3, StrategyTürk or private translation-memory material into issues, prompts,
commits or pull requests. Public AI-assistance must remain synthetic-only.
Test each contribution locally with the documented commands. Automated GitHub
Actions is intentionally disabled to avoid consuming the owner's unavailable quota.

**License: [MIT](LICENSE).** The original showcase code, synthetic fixtures,
tests, and documentation in **this public repository** may be reused, modified,
and redistributed under MIT, including commercially, while retaining the
license and copyright notice. Contributions are welcome via pull requests;
see [CONTRIBUTING.md](CONTRIBUTING.md).

## Issues and private rights reports

Issues are open for [bugs](https://github.com/Baglare/PoD-Localization-Engineering/issues/new/choose)
and improvement ideas **about this fictional engineering showcase**.
Use the issue templates and include only fictional repro data; please do not
paste real PoD, CK3, StrategyTürk, private translation-memory or Workshop
content into a public issue or pull request.

If you suspect copyright infringement, a license conflict, missing attribution,
trademark misuse, exposed private data or another rights issue, contact
**bparilti123123@gmail.com** privately, preferably with the affected
file/URL, the relevant right or work, and requested action. Do not publish
confidential evidence in an Issue. Reports can be evaluated for correction,
restriction or removal where warranted. [Security and disclosure](SECURITY.md).

## Distribution, boundary and licensing

The actual localization is distributed through Steam Workshop. No GitHub Release
is claimed. Production data stays private; this repository is intentionally
limited to original demonstrations, synthetic fixtures and aggregate evidence.
It was created with fresh Git history. Production localization data remains
private; this repository contains only the public engineering showcase.

The MIT grant covers only original material included in this public showcase.
It **does not** license the third-party Crusader Kings III game, Princes of
Darkness mod, StrategyTürk translations, private production repository,
Workshop package, upstream assets or trademarks. Referencing their names
describes project context and does not imply affiliation or endorsement.

Contributor submissions must contain original or appropriately licensed work;
contributors retain their own copyrights and agree that contributions will
be distributed under the repository's MIT license. See
[licensing boundaries](docs/allowlist.md#ownership-and-licensing).
