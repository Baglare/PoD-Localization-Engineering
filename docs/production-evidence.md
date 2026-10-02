# Private production evidence, summarized

Verified locally on 2026-10-02. Private files were read only. No underlying
corpus, raw log, production manifest or report is distributed here.

| Claim | Private evidence and verification |
| --- | --- |
| 87,865 memory rows | `progress.json` agrees with a local CSV row count |
| 965 upstream YML files | Local count under `source/pod/localization/`: 460 English, 498 Chinese, seven other-language files |
| 460 active source and output files | `progress.json` and production README record this release scope |
| Token/escape protection and terminology | Selected functions in `tools/pod_tr_pipeline.py` |
| Deterministic ZIP and SHA-256/CRC checks | `deterministic_zip` and `package_rc` in `scripts/release/release_core.py` |
| Terminology verification | `scripts/terminology/verify_terminology_convergence.py` |
| Steam Workshop distribution | Production README; distribution also specified by repository owner |

Historical release results are recorded in
`reports/release/final_release_quality_gates.md`: 12/12 required RC2 manual smoke
checks, 25/25 runtime static checks, 462/462 package member hashes and CRC checks,
a matching deterministic stable rebuild, and all 460 localization files identical
between RC2 and stable (two descriptor members differ).

These are **historical recorded results**, not tests rerun for the showcase.
The manual game results are private project acceptance records, not independent
runtime verification performed here. Compatibility is recorded for PoD 1.19.0.6
and the supported CK3 1.19.* profile, not guaranteed for future builds.
Keys include preserved/technical values; row coverage is not linguistic quality.
