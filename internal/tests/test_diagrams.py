#!/usr/bin/env python3
"""Diagram policy and failure-path tests. CLI mocks are not real rendering tests."""
from pathlib import Path
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from internal import diagram_tools as d


class DiagramTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'package'
        shutil.copytree(d.ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', '.pytest_cache'))
        self.cfg = json.loads((self.root / 'diagrams/manifest.json').read_text())
        self.original = {x['source']: (d.ROOT / x['source']).with_suffix('.svg').read_bytes()
                         for x in self.cfg['diagrams']}

    def tearDown(self):
        self.temp.cleanup()

    def save_config(self):
        (self.root / 'diagrams/manifest.json').write_text(json.dumps(self.cfg))

    def fake_cli(self, command, **kwargs):
        if command[-1] == '--version':
            return subprocess.CompletedProcess(command, 0, stdout='v0.9.0\n')
        source = Path(command[-2]).relative_to(self.root).as_posix()
        Path(command[-1]).write_bytes(self.original[source])
        return subprocess.CompletedProcess(command, 0, stdout=b'', stderr=b'')

    def run_check(self, write=False):
        with patch.object(d.subprocess, 'run', side_effect=self.fake_cli):
            return d.run(self.root, write=write)

    def test_01_inventory_and_owners(self):
        self.assertGreater(len(self.cfg['diagrams']), 0)
        self.assertEqual(len(self.cfg['diagrams']), len({x['source'] for x in self.cfg['diagrams']}))
        for item in self.cfg['diagrams']:
            self.assertTrue((self.root / item['owner']).is_file())
            self.assertTrue(item['reason'].strip())
            d.svg_check((self.root / item['source']).with_suffix('.svg').read_bytes())

    def test_02_metadata_graph_matches(self):
        item = next(x for x in self.cfg['diagrams'] if x.get('metadata_root'))
        self.assertEqual(d.knowledge_graph(self.root, item['metadata_root']),
                         (self.root / item['source']).read_text())

    def test_03_changed_metadata_is_stale(self):
        path = self.root / 'practices/use-kps.md'
        path.write_text(path.read_text().replace('"kps:method:retrieval-practice"', '', 1))
        with self.assertRaisesRegex(ValueError, 'stale metadata graph'):
            self.run_check()

    def test_04_unknown_graph_target(self):
        path = self.root / 'practices/use-kps.md'
        path.write_text(path.read_text().replace('kps:method:retrieval-practice', 'missing:method', 1))
        with self.assertRaisesRegex(ValueError, 'Unknown graph target'):
            d.knowledge_graph(self.root, 'kps:pr:use-kps')

    def test_05_check_is_read_only(self):
        paths = list((self.root / 'diagrams').rglob('*'))
        before = {p: p.read_bytes() for p in paths if p.is_file()}
        self.assertEqual(len(self.cfg['diagrams']), self.run_check())
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_06_modified_svg_is_rejected(self):
        path = (self.root / self.cfg['diagrams'][0]['source']).with_suffix('.svg')
        path.write_bytes(path.read_bytes() + b'\n<!-- stale -->')
        with self.assertRaisesRegex(ValueError, 'stale render'):
            self.run_check()

    def test_07_missing_svg_is_rejected(self):
        (self.root / self.cfg['diagrams'][0]['source']).with_suffix('.svg').unlink()
        with self.assertRaisesRegex(ValueError, 'missing or stale render'):
            self.run_check()

    def test_08_wrong_renderer_version(self):
        with patch.object(d.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, stdout='v0.8.0')):
            with self.assertRaisesRegex(ValueError, 'Expected D2'):
                d.run(self.root)

    def test_09_failed_compile_is_not_accepted(self):
        def fail(command, **kwargs):
            if command[-1] == '--version':
                return self.fake_cli(command, **kwargs)
            raise subprocess.CalledProcessError(1, command, stderr=b'invalid D2')
        with patch.object(d.subprocess, 'run', side_effect=fail):
            with self.assertRaises(subprocess.CalledProcessError):
                d.run(self.root)

    def test_10_paths_cannot_escape(self):
        with self.assertRaisesRegex(ValueError, 'escapes'):
            d.local_path(self.root, '../outside.svg')

    def test_11_missing_owner_is_rejected(self):
        self.cfg['diagrams'][0]['owner'] = 'absent.md'
        self.save_config()
        with self.assertRaisesRegex(ValueError, 'Missing diagram owner'):
            self.run_check()

    def test_12_active_svg_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Unexpected'):
            d.svg_check(b'<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script></svg>')

    def test_13_missing_renderer_is_not_success(self):
        with patch.object(d.subprocess, 'run', side_effect=FileNotFoundError('d2')):
            with self.assertRaises(FileNotFoundError):
                d.run(self.root)

    def test_14_write_restores_render(self):
        path = (self.root / self.cfg['diagrams'][0]['source']).with_suffix('.svg')
        path.write_bytes(b'stale')
        self.assertEqual(len(self.cfg['diagrams']), self.run_check(write=True))
        self.assertEqual(self.original[self.cfg['diagrams'][0]['source']], path.read_bytes())

    def test_15_unregistered_source_is_rejected(self):
        (self.root / 'diagrams/unused.d2').write_text('a -> b\n')
        with self.assertRaisesRegex(ValueError, 'Unregistered'):
            self.run_check()

    def test_16_each_owner_embeds_and_explains(self):
        for item in self.cfg['diagrams']:
            owner = self.root / item['owner']
            text = owner.read_text()
            target = Path(item['source']).with_suffix('.svg').name
            self.assertRegex(text, r'!\[[^\]\n]+\]\([^\n)]*' + re.escape(target) + r'\)')
            self.assertIn(Path(item['source']).name, text)
            self.assertIn('## Summary', text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
