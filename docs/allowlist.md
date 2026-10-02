# Public material allowlist and provenance

Decision recorded before implementation creation, 2026-10-02.
Default deny: no private repository file is approved for verbatim copying.
No private Git objects, branches, tags or history may be imported.

## Exact allowed files (all newly written)

- `.gitignore`
- `.gitattributes`
- `README.md`
- `docs/allowlist.md`
- `docs/architecture.md`
- `docs/production-evidence.md`
- `docs/validation.md`
- `tools/showcase.py`
- `tests/test_showcase.py`
- `fixtures/synthetic/catalog.json`
- `fixtures/synthetic/terms.json`
- `fixtures/synthetic/invalid.json`

Only these paths may enter the initial Git tree. Generated demonstration
archives, bytecode, local audit output and credentials are excluded.

## Private material read for conceptual evidence only

- `AGENTS.md`: workflow constraints and context review policy.
- `README.md`: recorded scope and Steam Workshop distribution statement.
- `progress.json`: aggregate counts and historical completion flags.
- `tools/pod_tr_pipeline.py`: selected parser, token protection, terminology
  substitution and pair-validation functions. Also contains real text tables;
  the entire file is excluded from copying.
- `scripts/release/release_core.py`: selected deterministic ZIP and release-gate
  functions. Contains production constants and machine paths; excluded.
- `scripts/release/build_release_candidate.py`: release entry point.
- `scripts/integration/build_full_yml_tree.py`: production integration entry point.
- `scripts/terminology/verify_terminology_convergence.py`: verification contract.
- `reports/release/final_release_quality_gates.md`: aggregate historical results;
  rewritten as a short evidence summary, never copied as a raw report.
- `translation_memory.csv`: local row count and local text-overlap audit only.
- `source/pod/localization/`: local file counts and local text-overlap audit only.
- `terminology.csv`, `source/strategyturk/`, `baseline/`, `output/`: local
  text-overlap audit only; no contents exported.
- Git remote/status/HEAD metadata: verify account and unchanged private state;
  no existing Git history imported.

## Explicit exclusions

All production English, Chinese and Turkish localization; translation memory;
StrategyTurk-derived data; terminology datasets; baseline and working corpora;
raw reports, logs and archives; copyrighted game/mod assets; local machine
identifiers; credentials; all existing Git history. Only aggregate counts and
high-level engineering descriptions cross the boundary.

## Ownership and licensing

Every included implementation file was written specifically for this showcase.
No implementation file or source sentence was copied from the private project.
This is a conceptual demonstration, not an export of its production pipeline.
That establishes creation provenance, not legal ownership: contributor,
employment and contractual rights remain for the repository owner to confirm.
No license is applied. After rights review, MIT would be a reasonable option
for the original demonstration code and synthetic fixtures; separately decide
how to license the documentation. Project/game/mod names identify context and
do not imply affiliation or permission to redistribute production content.
