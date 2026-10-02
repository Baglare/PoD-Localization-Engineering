# Architecture and contracts

## Private production workflow (verified concepts)

Read-only upstream inputs -> inventory and per-key memory -> bounded translation
batches -> ambiguity context pass -> terminology and structural checks ->
integration / semantic review / runtime-key recovery -> static release gates ->
deterministic packaging -> manual game smoke -> Steam Workshop distribution.

The production parser records malformed source findings, and the token validator
compares token categories and multiplicities with explicit production exceptions.
Terms have contextual/preservation policies; the production system is more complex
than a global replacement table. Review and runtime checks remain separate gates.
Recorded candidate-to-stable comparisons preserve localization bytes while
allowing release metadata to change in descriptors.

## Showcase implementation

`tools/showcase.py` reads only bundled synthetic JSON in its demo command.

1. Reject duplicate JSON fields, unknown row fields, non-demo keys, duplicate
   keys, empty values, unsupported delimiters and control characters.
2. Recognize a narrow lexical syntax: `{count}`, `[Pilot.DisplayName]`,
   `$DEMO_BADGE$`, `#gold ... #!`, `@spark!` and literal backslash escapes.
3. Apply case-sensitive, longest-first, whole-word fictional terms in visible
   text only. Protected spans are never substituted. Replacements are one pass;
   they do not cascade, and term insertion order cannot change the result.
4. Compare exact source/target token multisets after terminology replacement;
   permit grammatical reordering but reject token loss or repetition.
5. Sort keys, emit UTF-8 BOM and LF with a fictional `l_demo` header, and package
   sorted members with fixed ZIP timestamps, permissions and platform metadata.
   ZIP_STORED deliberately avoids compressor-version variation in this demo.
6. Retain a separate manifest with canonical catalog, archive and member SHA-256
   digests; verify exact member inventory, CRC, byte sizes and member hashes.

This is not a general YAML parser, full CK3 parser, translator, linguistic QA
engine or runtime simulator. Complex expressions are rejected rather than
interpreted. The catalog digest records canonical normalized input provenance;
the standalone verifier checks archive/member integrity, not the source catalog.
Hashes detect changes relative to a trusted manifest; they do not authenticate
an attacker-controlled archive and manifest together. No signature is claimed.
The CLI writes only demonstration artifacts and performs no upload.
