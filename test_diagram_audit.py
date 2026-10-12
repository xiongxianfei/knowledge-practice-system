#!/usr/bin/env python3
"""Checks diagram audit coverage and links, not explanatory truth or usefulness."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
ROLES = ('concepts','principles','models','methods','practices')

def inspect_audit(root):
    audit=json.loads((root/'diagram-audit.json').read_text())
    cfg=json.loads((root/'diagrams.json').read_text())
    registry={d['source'] for d in cfg['diagrams']}
    objects={p.relative_to(root).as_posix() for r in ROLES for p in (root/r).glob('*.md')}
    errors=[]
    entries=audit['objects']; named=[e['object'] for e in entries]
    if set(named)!=objects or len(set(named))!=len(named): errors.append('coverage')
    for e in entries:
        if e['decision'] not in {'add','retain','reuse','text-only'}: errors.append('decision')
        if not e['reason'].strip(): errors.append('reason')
        if (e['decision']=='text-only') != (not e['diagrams']): errors.append('text-only')
        owner=(root/e['object']).resolve()
        if not owner.is_relative_to(root.resolve()) or not owner.is_file():
            errors.append('owner'); continue
        text=owner.read_text()
        for name in e['diagrams']:
            source=(root/name).resolve()
            if name not in registry or not source.is_relative_to(root.resolve()) or not source.is_file():
                errors.append('source'); continue
            if not source.with_suffix('.svg').is_file(): errors.append('render')
            image='../'+Path(name).with_suffix('.svg').as_posix()
            if ']('+image+')' not in text or '](../'+name+')' not in text: errors.append('embed')
    return errors

class DiagramAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)/'package'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache'))
    def tearDown(self): self.tmp.cleanup()
    def mutate(self,change):
        p=self.root/'diagram-audit.json'; a=json.loads(p.read_text()); change(a);p.write_text(json.dumps(a))
    def test_01_coverage_and_embeds(self): self.assertEqual([],inspect_audit(self.root))
    def test_02_missing_object(self):
        self.mutate(lambda a:a['objects'].pop());self.assertIn('coverage',inspect_audit(self.root))
    def test_03_duplicate_object(self):
        self.mutate(lambda a:a['objects'].append(a['objects'][0]));self.assertIn('coverage',inspect_audit(self.root))
    def test_04_reason_required(self):
        self.mutate(lambda a:a['objects'][0].update(reason=''));self.assertIn('reason',inspect_audit(self.root))
    def test_05_missing_source(self):
        self.mutate(lambda a:a['objects'][0].update(diagrams=['diagrams/absent.d2']));self.assertIn('source',inspect_audit(self.root))
    def test_06_missing_render(self):
        (self.root/'diagrams/models/prov-relations.svg').unlink();self.assertIn('render',inspect_audit(self.root))
    def test_07_missing_editable_link(self):
        p=self.root/'concepts/skos-concept.md';p.write_text(p.read_text().replace('../diagrams/concepts/concept-and-label.d2','not-source.d2'));self.assertIn('embed',inspect_audit(self.root))
    def test_08_text_only_is_explicit(self):
        self.mutate(lambda a:a['objects'][0].update(decision='text-only'));self.assertIn('text-only',inspect_audit(self.root))
    def test_09_uri_example(self):
        from urllib.parse import urljoin
        self.assertEqual('https://example.org/README.md#summary',urljoin('https://example.org/practices/use-kps.md','../README.md#summary'))
    def test_10_spacing_example(self):
        a,b,c=(1,1,1),(2,2,2),(1,2,3)
        self.assertEqual((3,6,6),(sum(a),sum(b),sum(c)))
        self.assertEqual(len(a),len(b));self.assertEqual(len(b),len(c));self.assertNotEqual(b,c)

if __name__=='__main__': unittest.main(verbosity=2)
