#!/usr/bin/env python3
"""Core curation checks; these do not evaluate scientific truth or source authority."""
from pathlib import Path
import json
import shutil
import tempfile
import unittest
import validate as v

ROOT = Path(__file__).resolve().parent
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
    trans = json.loads((root / 'transition.json').read_text())
    for path, item in trans['retired'].items():
        if (root / path).exists() or item['id'] in by_id:
            errors.append('retired-object-retained')
        name, frag = item['destination'].split('#', 1)
        dest = (root / name).resolve()
        if not dest.is_relative_to(root.resolve()) or not dest.is_file():
            errors.append('migration-target'); continue
        d = v.parse(dest)
        if d.meta.get('type') != 'practice' or frag not in d.fragments:
            errors.append('migration-target')
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
    def test_07_retired_paths_stay_retired(self):
        trans=json.loads((self.root/'transition.json').read_text());path=next(iter(trans['retired']))
        (self.root/path).write_text('retained by accident');self.assertIn('retired-object-retained',check_alignment(self.root))
    def test_08_wrong_migration_fragment_is_rejected(self):
        p=self.root/'transition.json';t=json.loads(p.read_text());first=next(iter(t['retired'].values()));first['destination']='practices/use-kps.md#absent';p.write_text(json.dumps(t));self.assertIn('migration-target',check_alignment(self.root))
    def test_09_all_previous_objects_accounted_for(self):
        t=json.loads((self.root/'transition.json').read_text());self.assertEqual(41,len(t['retired']));self.assertEqual(41,len({d['id'] for d in t['retired'].values()}))
    def test_10_practice_stages_preserved(self):
        counts={'use-kps.md':4,'build-domain-knowledge.md':5,'improve-kps.md':4,'review-and-learn.md':4}
        for file,count in counts.items():self.assertEqual(count,len(v.parse(self.root/'practices'/file).meta['stage_titles']))
    def test_11_only_practices_are_local_workflow_objects(self):
        self.assertEqual(20,sum(1 for folder in ['concepts','principles','models','methods','practices'] for _ in (self.root/folder).glob('*.md')))
        self.assertEqual(16,sum(1 for folder in ALLOWED for _ in (self.root/(folder+'s')).glob('*.md')))
    def test_12_existing_content_language_remains_explicit(self):
        p=json.loads((self.root/'publication.json').read_text());self.assertEqual('10.2.0',p['version']);self.assertEqual('9.x',p['kps_language']);self.assertEqual('9.1.0',p['validated_with'])

if __name__ == '__main__': unittest.main(verbosity=2)
