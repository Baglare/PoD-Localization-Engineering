# Public showcase roadmap (synthetic-only)

This is a backlog for voluntary improvements, **not** a roadmap for the private
production translation. Tasks must use original fictional text only.

## Good first contributions

- Improve CLI error categories while preserving path redaction.
- Add tests for duplicate / malformed fields and nested-looking synthetic syntax.
- Expand the README with an example of the fictional input-to-output flow.
- Make fixture naming and negative cases clearer to new contributors.

## Medium tasks

- Design a versioned manifest migration example while rejecting unknown versions
  by default.
- Support an optional input fixture path only with strict path checks and bounded
  input size; never use production inputs for tests.
- Add property-based tests **without** introducing mandatory runtime dependencies,
  or implement reproducible random fixture generation with standard library.
- Add a documented checksum-based regression fixture for deterministic output.

## Explicit non-goals

- Releasing a playable PoD mod or actual Turkish localization.
- Importing production CSV, game assets, raw PoD texts or private history.
- Building a broad CK3 syntax parser from proprietary examples.
- Integrating external translation or AI services.
- Claiming source authentication from an unauthenticated hash manifest.

## Acceptance

Each change should include tests, documented limits, no data-boundary violation,
and green GitHub Actions. Legal licensing and contributions remain an owner
decision before promoting the project as fully open source.
