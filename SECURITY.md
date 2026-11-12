# Security and responsible disclosure

This is a synthetic, offline demonstration, **not** an official CK3/PoD tool.
Do not submit secrets, private localization data or third-party source material
in a public issue or pull request. The repository has no active bug bounty.

For a vulnerability, use GitHub's private vulnerability reporting feature if
enabled. If unavailable, contact the repository owner through a private channel
rather than posting an exploit or confidential data publicly.

The demo verifier checks SHA-256/CRC relative to a separate manifest; it is not
a signature scheme. An attacker who can replace both archive and manifest can
make a consistent forged pair. Never treat it as source authentication.
