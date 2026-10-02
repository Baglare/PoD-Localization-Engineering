"""Offline, synthetic-only localization engineering demonstration."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile


class ValidationError(ValueError):
    """Input or artifact violates the demonstration contract."""


KEY = re.compile(r"demo_[a-z0-9_]+\Z")
# Intentionally narrow lexical subset; no game expression evaluation.
TOKEN = re.compile(
    r"\$[A-Za-z_][A-Za-z0-9_]*\$|\[[A-Za-z_][A-Za-z0-9_.]*(?:\|E)?\]"
    r"|\{[A-Za-z_][A-Za-z0-9_]*\}|#[A-Za-z_][A-Za-z0-9_]*|#!"
    r"|@[A-Za-z_][A-Za-z0-9_]*!|\\[nrt\"\\]"
)
RESERVED = set('$[]{}#@\\"')


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError('duplicate JSON field')
        result[key] = value
    return result


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
    except (ValueError, UnicodeError) as exc:
        raise ValidationError('invalid JSON input') from exc


def spans(text: str):
    if not isinstance(text, str) or not text.strip():
        raise ValidationError('empty or non-string text')
    if any(ord(c) < 32 or 0xD800 <= ord(c) <= 0xDFFF for c in text):
        raise ValidationError('use literal escapes instead of control characters')
    cursor = 0
    depth = 0
    found = []
    for match in TOKEN.finditer(text):
        if any(c in RESERVED for c in text[cursor:match.start()]):
            raise ValidationError('unsupported or malformed token')
        token = match.group()
        if token == '#!':
            depth -= 1
            if depth < 0:
                raise ValidationError('unmatched formatting close')
        elif token.startswith('#'):
            depth += 1
        found.append(match)
        cursor = match.end()
    if any(c in RESERVED for c in text[cursor:]) or depth:
        raise ValidationError('unsupported or unclosed token')
    return found


def tokens(text: str) -> Counter:
    return Counter(m.group() for m in spans(text))


def validate_terms(terms):
    if not isinstance(terms, dict):
        raise ValidationError('terms must be an object')
    for source, target in terms.items():
        if not isinstance(source, str) or not isinstance(target, str):
            raise ValidationError('term strings required')
        if tokens(source) or tokens(target):
            raise ValidationError('terms must contain plain display text')
    return terms


def replace_terms(text: str, terms: dict[str, str]) -> str:
    """One deterministic longest-first pass over visible spans only."""
    validate_terms(terms)
    ordered = sorted(terms, key=lambda term: (-len(term), term))
    pattern = re.compile(r'(?<!\w)(?:' + '|'.join(re.escape(t) for t in ordered) + r')(?!\w)') if ordered else None
    def replace(segment):
        return pattern.sub(lambda m: terms[m.group()], segment) if pattern else segment
    pieces = []
    cursor = 0
    for match in spans(text):
        pieces.extend((replace(text[cursor:match.start()]), match.group()))
        cursor = match.end()
    pieces.append(replace(text[cursor:]))
    result = ''.join(pieces)
    if tokens(result) != tokens(text):
        raise ValidationError('terminology changed protected syntax')
    return result


def normalize(rows, terms):
    if not isinstance(rows, list) or not rows:
        raise ValidationError('nonempty catalog list required')
    validate_terms(terms)
    seen = set()
    normalized = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != {'key', 'source', 'target'}:
            raise ValidationError('catalog row schema mismatch')
        key = row['key']
        if not isinstance(key, str) or not KEY.fullmatch(key) or key in seen:
            raise ValidationError('invalid or duplicate demo key')
        seen.add(key)
        target = replace_terms(row['target'], terms)
        if tokens(row['source']) != tokens(target):
            raise ValidationError(f'{key}: protected token mismatch')
        normalized.append({'key': key, 'source': row['source'], 'target': target})
    return sorted(normalized, key=lambda row: row['key'])


def canonical(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n').encode('utf-8')


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def build(rows, terms):
    normalized = normalize(rows, terms)
    # The fictitious header prevents this example being mistaken for a game mod.
    text = 'l_demo:\n' + ''.join(f' {r["key"]}:0 "{r["target"]}"\n' for r in normalized)
    members = {'localization/demo.yml': b'\xef\xbb\xbf' + text.encode('utf-8')}
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, payload in sorted(members.items()):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, payload)
    payload = stream.getvalue()
    manifest = {
        'schema_version': 1,
        'catalog_sha256': sha256(canonical(normalized)),
        'archive_sha256': sha256(payload),
        'members': [{'path': name, 'bytes': len(data), 'sha256': sha256(data)} for name, data in sorted(members.items())],
    }
    verify(payload, manifest)
    return payload, manifest


def verify(payload: bytes, manifest):
    """Compare with a separately retained manifest; no signature/authenticity claim."""
    if not isinstance(manifest, dict) or set(manifest) != {'schema_version', 'catalog_sha256', 'archive_sha256', 'members'}:
        raise ValidationError('manifest schema mismatch')
    if type(manifest['schema_version']) is not int or manifest['schema_version'] != 1:
        raise ValidationError('unsupported manifest version')
    for key in ('catalog_sha256', 'archive_sha256'):
        if not isinstance(manifest[key], str) or not re.fullmatch(r'[0-9a-f]{64}', manifest[key]):
            raise ValidationError('invalid digest')
    records = manifest['members']
    if not isinstance(records, list) or len(records) != 1:
        raise ValidationError('unexpected manifest members')
    row = records[0]
    if not isinstance(row, dict) or set(row) != {'path', 'bytes', 'sha256'} or row['path'] != 'localization/demo.yml':
        raise ValidationError('unexpected member path')
    if type(row['bytes']) is not int or row['bytes'] < 0 or not isinstance(row['sha256'], str) or not re.fullmatch(r'[0-9a-f]{64}', row['sha256']):
        raise ValidationError('invalid member metadata')
    if sha256(payload) != manifest['archive_sha256']:
        raise ValidationError('archive SHA-256 mismatch')
    try:
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            if archive.namelist() != [row['path']] or archive.testzip() is not None:
                raise ValidationError('archive member or CRC mismatch')
            data = archive.read(row['path'])
            if len(data) != row['bytes'] or sha256(data) != row['sha256']:
                raise ValidationError('member SHA-256 or size mismatch')
    except (zipfile.BadZipFile, RuntimeError, EOFError) as exc:
        raise ValidationError('invalid ZIP') from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    demo = sub.add_parser('demo')
    demo.add_argument('--out', type=Path, default=Path('build'))
    check = sub.add_parser('verify')
    check.add_argument('archive', type=Path)
    check.add_argument('manifest', type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'demo':
            fixture = Path(__file__).resolve().parents[1] / 'fixtures/synthetic'
            payload, manifest = build(read_json(fixture/'catalog.json'), read_json(fixture/'terms.json'))
            args.out.mkdir(parents=True, exist_ok=True)
            (args.out/'demo.zip').write_bytes(payload)
            (args.out/'manifest.json').write_bytes(canonical(manifest))
            print(f'Synthetic artifact verified: {len(payload)} bytes, SHA-256 {sha256(payload)}')
        else:
            verify(args.archive.read_bytes(), read_json(args.manifest))
            print('Archive, member hashes and CRC verified.')
    except (ValidationError, OSError) as exc:
        # OS exceptions can contain machine paths: keep the CLI error portable.
        parser.exit(1, f'Validation failed: {exc if isinstance(exc, ValidationError) else "file I/O error"}\n')


if __name__ == '__main__':
    main()
