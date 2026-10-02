"""Contract tests against fictional fixtures only; no production inputs."""
import copy
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import showcase as s

FIXTURE = Path(__file__).resolve().parents[1] / 'fixtures/synthetic'


class ShowcaseTests(unittest.TestCase):
    def setUp(self):
        self.rows = s.read_json(FIXTURE/'catalog.json')
        self.terms = s.read_json(FIXTURE/'terms.json')

    def artifact(self):
        return s.build(self.rows, self.terms)

    def test_reordered_inputs_produce_identical_archive_and_manifest(self):
        first = self.artifact()
        other = s.build(list(reversed(self.rows)), dict(reversed(list(self.terms.items()))))
        self.assertEqual(first, other)
        self.assertEqual(first, self.artifact())

    def test_output_order_encoding_escapes_and_terminology(self):
        payload, manifest = self.artifact()
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            data = archive.read('localization/demo.yml')
            self.assertTrue(data.startswith(b'\xef\xbb\xbfl_demo:\n'))
            self.assertNotIn(b'\r', data)
            text = data.decode('utf-8-sig')
            self.assertIn('ay pulu', text)
            self.assertIn('bulut rozeti', text)
            self.assertNotIn('moon token', text)
            self.assertIn(r'\"Yumuşakça dön\".\nİki kez katla.', text)
            keys = [line.split(':', 1)[0].strip() for line in text.splitlines()[1:]]
            self.assertEqual(keys, sorted(row['key'] for row in self.rows))
            info = archive.infolist()[0]
            self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))
            self.assertEqual(info.compress_type, zipfile.ZIP_STORED)
        s.verify(payload, manifest)

    def test_terminology_never_changes_protected_spans(self):
        text = '[Pilot.DisplayName] Pilot {count} $DEMO_BADGE$ #gold gold#! @spark!'
        terms = {'Pilot':'Kılavuz', 'count':'sayı', 'DEMO_BADGE':'rozet', 'gold':'altın', 'spark':'ışık'}
        result = s.replace_terms(text, terms)
        self.assertIn('Kılavuz', result)
        self.assertIn('#gold altın#!', result)
        self.assertEqual(s.tokens(text), s.tokens(result))

    def test_longest_match_whole_word_and_non_cascading_terms(self):
        self.assertEqual(s.replace_terms('cloud badge badges badge', {'cloud badge':'rozet', 'badge':'işaret', 'rozet':'other'}), 'rozet badges işaret')

    def test_token_reordering_allowed(self):
        s.normalize([{'key':'demo_order','source':'{first} before {second}.','target':'{second}, sonra {first}.'}], {})

    def test_token_loss_and_duplication_rejected(self):
        for target in ('Bir pul.', '{count} ve {count} pul.'):
            with self.subTest(target=target), self.assertRaises(s.ValidationError):
                s.normalize([{'key':'demo_count','source':'{count} token.','target':target}], {})

    def test_malformed_fixture_rejected(self):
        with self.assertRaises(s.ValidationError):
            s.build(s.read_json(FIXTURE/'invalid.json'), self.terms)

    def test_unsupported_syntax_and_unbalanced_markup_rejected(self):
        for text in ('[Pilot(', '$UNCLOSED', r'bad\x', '"raw quote"', '#gold unclosed', 'close #!', 'actual\nnewline', '{count', '\ud800'):
            with self.subTest(text=text), self.assertRaises(s.ValidationError):
                s.tokens(text)

    def test_duplicate_key_rejected(self):
        with self.assertRaises(s.ValidationError):
            s.build(self.rows + [self.rows[0]], self.terms)

    def test_schema_errors_rejected(self):
        for rows in ([], {}, [{'key':'../escape','source':'plain','target':'düz'}], [{'key':'demo_x','source':'plain','target':'düz','extra':1}], [{'key':'demo_x','source':'plain','target':''}], [{'key':'demo_x','source':42,'target':'düz'}]):
            with self.subTest(rows=rows), self.assertRaises(s.ValidationError):
                s.build(rows, {})

    def test_duplicate_json_fields_and_invalid_json_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'input.json'
            for text in ('{"a":1,"a":2}', '{broken'):
                path.write_text(text, encoding='utf-8')
                with self.assertRaises(s.ValidationError):
                    s.read_json(path)

    def test_terms_cannot_insert_tokens_or_controls(self):
        for terms in ({'plain':'{added}'}, {'plain':'new\nline'}, {'plain':''}, {'plain':5}, []):
            with self.subTest(terms=terms), self.assertRaises(s.ValidationError):
                s.build(self.rows, terms)

    def test_archive_sha_detects_changes(self):
        payload, manifest = self.artifact()
        with self.assertRaisesRegex(s.ValidationError, 'archive SHA'):
            s.verify(payload + b'changed', manifest)

    def test_member_digest_and_size_independently_checked(self):
        payload, manifest = self.artifact()
        for field, value in (('sha256', '0'*64), ('bytes', 0)):
            changed = copy.deepcopy(manifest)
            changed['members'][0][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(s.ValidationError, 'member SHA'):
                s.verify(payload, changed)

    def test_crc_checked_even_if_outer_digest_is_updated(self):
        payload, manifest = self.artifact()
        corrupt = bytearray(payload)
        index = payload.index(b'\xef\xbb\xbf')
        corrupt[index] ^= 1
        manifest['archive_sha256'] = s.sha256(corrupt)
        with self.assertRaises(s.ValidationError):
            s.verify(bytes(corrupt), manifest)

    def test_extra_and_duplicate_archive_members_rejected(self):
        payload, manifest = self.artifact()
        with zipfile.ZipFile(io.BytesIO(payload)) as original:
            data = original.read('localization/demo.yml')
        for name in ('unexpected.txt', 'localization/demo.yml'):
            stream = io.BytesIO()
            import warnings
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', UserWarning)
                with zipfile.ZipFile(stream, 'w') as archive:
                    archive.writestr('localization/demo.yml', data)
                    archive.writestr(name, b'extra')
            changed = copy.deepcopy(manifest)
            changed['archive_sha256'] = s.sha256(stream.getvalue())
            with self.subTest(name=name), self.assertRaises(s.ValidationError):
                s.verify(stream.getvalue(), changed)

    def test_manifest_paths_and_schema_rejected(self):
        payload, manifest = self.artifact()
        for change in ({'schema_version':2}, {'members':[]}, {'extra':True}):
            changed = dict(manifest, **change)
            with self.assertRaises(s.ValidationError):
                s.verify(payload, changed)
        manifest['members'][0]['path'] = '../outside'
        with self.assertRaises(s.ValidationError):
            s.verify(payload, manifest)

    def test_cli_build_verify_and_failure_exit_status(self):
        script = Path(s.__file__)
        with tempfile.TemporaryDirectory() as directory:
            def run(*args):
                return subprocess.run([sys.executable, str(script), *map(str, args)], capture_output=True, text=True)
            out = Path(directory)/'build'
            self.assertEqual(run('demo', '--out', out).returncode, 0)
            self.assertEqual(run('verify', out/'demo.zip', out/'manifest.json').returncode, 0)
            (out/'demo.zip').write_bytes(b'changed')
            result = run('verify', out/'demo.zip', out/'manifest.json')
            self.assertEqual(result.returncode, 1)
            self.assertIn('SHA-256 mismatch', result.stderr)
            self.assertNotIn(directory, result.stderr)


if __name__ == '__main__':
    unittest.main()
