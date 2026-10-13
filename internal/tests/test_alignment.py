#!/usr/bin/env python3
"""Core curation checks; these do not evaluate scientific truth or source authority."""
from pathlib import Path
import json
import shutil
import tempfile
import unittest
import validate as v

ROOT = Path(__file__).resolve().parents[2]
ALLOWED = {
    'concept': {'definition-paraphrase'},
    'principle': {'scoped-empirical-finding', 'methodological-relationship'},
    'model': {'standard-model-subset'},
    'method': {'published-procedure-summary'},
}

def check_alignment(root):
    """Return structural curation errors without assessing substantive faithfulness."""
    errors = []
    docs = [v.parse(p) for p in sorted(root.rglob('*.md'))
            if not {'.git', '.github', '__pycache__', '.pytest_cache'}.intersection(p.relative_to(root).parts)]
    by_id = {d.meta.get('id'): d for d in docs if d.meta.get('id')}
    for d in docs:
        typ = d.meta.get('type')
        if typ not in ALLOWED:
            continue
        align = d.meta.get('source_alignment')
        if not isinstance(align, list) or not align:
            errors.append('missing-alignment'); continue
        for a in align:
            if not isinstance(a, dict):
                errors.append('invalid-alignment'); continue
            ident = a.get('reference')
            source = by_id.get(ident)
            if source is None or source.meta.get('type') != 'reference':
                errors.append('alignment-source')
            if ident not in d.meta.get('references', []):
                errors.append('alignment-dependency')
            if a.get('relation') not in ALLOWED[typ]:
                errors.append('alignment-relation')
            if not isinstance(a.get('locator'), str) or not a['locator'].strip():
                errors.append('alignment-locator')
    return errors

class CoreAlignmentTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)/'package'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache'))
    def tearDown(self): self.tmp.cleanup()
    def object_path(self): return self.root/'concepts/skos-concept.md'
    def edit(self, mutate):
        path = self.object_path(); m,b=v.split_frontmatter(path.read_text());mutate(m)
        path.write_text('---\n'+'\n'.join(k+': '+json.dumps(x) for k,x in m.items())+'\n---\n'+b)
    def test_01_current_alignment(self): self.assertEqual([], check_alignment(self.root))
    def test_02_missing_alignment_is_rejected(self):
        self.edit(lambda m:m.pop('source_alignment'));self.assertIn('missing-alignment',check_alignment(self.root))
    def test_03_missing_source_is_rejected(self):
        self.edit(lambda m:m['source_alignment'][0].update(reference='unknown'));self.assertIn('alignment-source',check_alignment(self.root))
    def test_04_missing_locator_is_rejected(self):
        self.edit(lambda m:m['source_alignment'][0].update(locator=''));self.assertIn('alignment-locator',check_alignment(self.root))
    def test_05_wrong_relation_is_rejected(self):
        self.edit(lambda m:m['source_alignment'][0].update(relation='institutional-endorsement'));self.assertIn('alignment-relation',check_alignment(self.root))
    def test_06_missing_dependency_is_rejected(self):
        self.edit(lambda m:m.update(references=[]));self.assertIn('alignment-dependency',check_alignment(self.root))

if __name__ == '__main__': unittest.main(verbosity=2)
