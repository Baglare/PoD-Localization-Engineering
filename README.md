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

## Distribution, boundary and licensing

The actual localization is distributed through Steam Workshop. No GitHub Release
is claimed. Production data stays private; this repository is intentionally
limited to original demonstrations, synthetic fixtures and aggregate evidence.
It starts with fresh Git history and remains private pending human review.

No license has been applied. All implementation files were newly written for
this showcase; the owner must confirm contributor and contractual rights before
choosing a license. MIT is a possible next decision for code and synthetic
fixtures after that review. No ownership is claimed over the game/mod or names.
