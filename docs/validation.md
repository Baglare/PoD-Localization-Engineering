# Showcase validation

Checks performed locally on 2026-10-02 using Python 3.14:

- 18 synthetic-only unittest tests passed, including CLI success/failure,
  malformed JSON/syntax, token loss/repetition, terminology boundaries,
  deterministic rebuilds, BOM/LF/sorted output, archive/member SHA-256, CRC,
  extra/duplicate members and invalid manifest paths.
- Both implementation/test modules passed Python syntax compilation.
- Demo build and independent CLI archive verification passed.
- Exact 12-file allowlist enforced; no production file copied.
- All allowlisted text scanned for absolute machine paths, local usernames,
  credential patterns and private-key material: no findings.
- Local overlap search against upstream localization, production memory,
  terminology, baseline, Turkish output and StrategyTurk source found no
  substantial source sentence in the public material. Fixture values were also
  checked for exact collisions. Only aggregate audit results leave the machine.
- Fresh Git root commit; staged whitespace check passed.
- Private production tracked-file hashes, HEAD and status unchanged after reads.

Secret-pattern and text-overlap searches are bounded static checks, not legal
clearance or a guarantee against every possible secret. The source-sentence
search considers strings of at least 24 characters with four or more words;
fixture fields are additionally compared exactly, including short values.
The local audit examined 1,466,459 text values across 2,635 private data files;
all 7,488 tracked private files retained their recorded SHA-256 hashes.
No raw audit output, source sentences or runtime logs are committed.

Production tests, full builds, browser automation and game runtime tests were
not run. Historical production smoke results remain explicitly historical.
The small showcase test suite and demonstration are the only executed builds.

Human publication review must confirm the file boundary, rights and licensing.
No license is applied and the GitHub repository must remain private until the
owner separately reviews and changes visibility. This repository creates no
GitHub Release, Workshop upload or production mutation.
