#!/usr/bin/env python3
"""Regression tests for publication checks, not scientific/domain validity.
Run: python test_validate.py
Each test mutates a temporary copy, never the published knowledge.
"""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest

HERE=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('publication_validator',HERE/'validate.py')
v=importlib.util.module_from_spec(spec);sys.modules[spec.name]=v;spec.loader.exec_module(v)

class PublicationChecks(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)/'package'
        shutil.copytree(HERE,self.root,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache','*.pyc'))
    def tearDown(self):self.temp.cleanup()
    def find(self,typ):
        return next(p for p in sorted(self.root.rglob('*.md')) if v.parse(p).meta.get('type')==typ)
    def meta(self,p,key,value):
        m,b=v.split_frontmatter(p.read_text());m[key]=value
        p.write_text('---\n'+'\n'.join(k+': '+json.dumps(x,ensure_ascii=False) for k,x in m.items())+'\n---\n\n'+b)
    def expect(self,code,manifest=False):
        r=v.validate(self.root,manifest=manifest)
        self.assertFalse(r['ok']); self.assertIn(code,[x['code'] for x in r['errors']],r['errors'])
    def add(self,p,text):p.write_text(p.read_text()+'\n'+text+'\n')
    def make_manifest(self):
        paths=v.manifest_payload_files(self.root)
        (self.root/'MANIFEST.sha256').write_text(''.join(v.sha(p)+'  '+p.relative_to(self.root).as_posix()+'\n' for p in paths))

    def refresh_and_check(self):
        result = v.validate(self.root, refresh=True)
        self.assertTrue(result['ok'], result['errors'])
        return result

    def test_01_clean_package(self):
        r=v.validate(self.root);self.assertTrue(r['ok'],r['errors'])
    def test_02_missing_summary(self):
        p=self.find('concept');p.write_text(p.read_text().replace('## Summary','## Overview',1));self.expect('local-summary')
    def test_03_empty_summary(self):
        p=self.find('concept');p.write_text(re.sub(r'(## Summary\n).*?(?=\n## )',r'\1\n',p.read_text(),count=1,flags=re.S));self.expect('local-summary')
    def test_04_imperative_principle(self):
        p=self.find('principle');p.write_text(re.sub(r'^# .+$','# Always obey this design',p.read_text(),count=1,flags=re.M));self.expect('imperative-principle')
    def test_05_missing_method_rationale(self):
        ps=[p for p in sorted(self.root.rglob('*.md')) if v.parse(p).meta.get('type')=='method' and '\n## Rationale\n' in p.read_text()]
        p=ps[0];p.write_text(p.read_text().replace('## Rationale','## Explanation',1));self.expect('method-rationale')
    def test_07_nonconsecutive_stage(self):
        p=self.find('practice');p.write_text(p.read_text().replace('## Stage2 ','## Stage99 ',1));self.expect('stage-order')
    def test_08_invented_ti_fragment(self):
        p=self.find('practice');self.add(p,'[Build the model](#ti-03)');self.expect('missing-fragment')
    def test_09_duplicate_heading(self):
        p=self.find('concept');self.add(p,'## Summary\nAnother summary.');self.expect('duplicate-heading')
    def test_10_missing_target(self):
        p=self.root/'README.md';self.add(p,'[Absent](missing-file.md)');self.expect('missing-target')
    def test_11_target_outside_package(self):
        p=self.root/'README.md';self.add(p,'[Sibling](../other-package/README.md)');self.expect('local-link')
    def test_12_duplicate_identity(self):
        a=self.find('concept');b=self.find('model');self.meta(b,'id',v.parse(a).meta['id']);self.expect('duplicate-id')
    def test_13_wrong_relationship_role(self):
        a=self.find('concept');b=self.find('method');self.meta(b,'uses_methods',[v.parse(a).meta['id']]);self.expect('relationship-type')
    def test_14_unknown_identity(self):
        p=self.find('method');self.meta(p,'uses_models',['missing:model']);self.expect('unresolved-id')
    def test_15_wrong_folder_role(self):
        p=self.find('principle');self.meta(p,'type','model');self.expect('type-folder')
    def test_16_recursive_composition_cycle(self):
        p=self.find('practice');self.meta(p,'composes',[v.parse(p).meta['id']]);self.expect('composition-cycle')
    def test_17_metadata_id_is_not_an_anchor(self):
        p=self.find('method');self.add(p,'[Object identity](#'+v.parse(p).meta['id']+')');self.expect('missing-fragment')
    def test_18_changed_dependency_needs_review(self):
        s=json.loads((self.root/'internal/metadata/summary-dependencies.json').read_text())
        target=next(iter(next(iter(s['entries'].values())).keys()))
        self.add(self.root/target,'A changed source condition needs a deliberate review.');self.expect('stale-summary')
    def test_19_exact_version_not_major_line(self):
        p=self.root/'publication.json';d=json.loads(p.read_text());d['kps_language']='9.0.0';p.write_text(json.dumps(d));self.expect('compatibility')
    def test_20_wrong_language_in_file(self):
        self.meta(self.find('concept'),'language','KPS 8.x');self.expect('language')
    def test_21_custom_html_anchor(self):
        self.add(self.find('concept'),'<a id="hidden"></a>');self.expect('html-anchor')
    def test_22_application_wikilink(self):
        self.add(self.find('concept'),'[[A particular application link]]');self.expect('wikilink')
    def test_23_missing_reference_access_extent(self):
        self.meta(self.find('reference'),'access_extent','');self.expect('reference-access')
    def test_24_manifest_detects_tamper(self):
        self.make_manifest();self.add(self.root/'README.md','Changed after packaging.');self.expect('manifest-hash',True)
    def test_25_manifest_detects_unlisted_payload(self):
        self.make_manifest();(self.root/'unexpected.txt').write_text('unlisted');self.expect('manifest-coverage',True)
    def test_26_fenced_demonstration_is_not_live(self):
        self.add(self.root/'README.md','```markdown\n## TI-03\n[Not live](#missing)\n```')
        r=v.validate(self.root);self.assertTrue(r['ok'],r['errors'])
    def test_27_fresh_manifest_verifies(self):
        self.make_manifest();r=v.validate(self.root,manifest=True);self.assertTrue(r['ok'],r['errors'])
    def test_28_duplicate_metadata_key(self):
        p=self.find('concept');p.write_text(p.read_text().replace('---\n','---\ntype: "concept"\n',1));self.expect('parse')
    def test_29_missing_stage_map(self):
        p=self.find('practice');doc=v.parse(p);h=doc.meta['stage_titles'][0]
        p.write_text(p.read_text().replace('](#'+v.slug(h)+')','](../README.md)'));self.expect('stage-navigation')
    def test_30_review_refresh_does_not_hide_broken_links(self):
        self.add(self.root/'README.md','[Missing](does-not-exist.md)')
        old=(self.root/'internal/metadata/summary-dependencies.json').read_bytes();r=v.validate(self.root,refresh=True)
        self.assertFalse(r['ok']);self.assertEqual(old,(self.root/'internal/metadata/summary-dependencies.json').read_bytes())

    def test_31_manifest_ignores_checkout_and_caches(self):
        self.make_manifest()
        for name in ('.git/objects/fixture', '.pytest_cache/fixture', '__pycache__/fixture.pyc'):
            path=self.root/name
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes(b'build tooling, not publication payload')
        result=v.validate(self.root,manifest=True)
        self.assertTrue(result['ok'],result['errors'])


    def test_39_local_image_target(self):
        asset = self.root/'assets'/'sample.svg'
        asset.parent.mkdir(parents=True,exist_ok=True)
        asset.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
        self.add(self.root/'README.md','![Review branches](assets/sample.svg)\nThe procedure separates success from revision.')
        self.refresh_and_check()

    def test_40_missing_local_image(self):
        self.add(self.root/'README.md','![Review branches](assets/missing.svg)')
        self.expect('missing-target')

    def test_41_image_alt_warning(self):
        asset = self.root/'sample.svg';asset.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
        self.add(self.root/'README.md','![](sample.svg)')
        result = self.refresh_and_check()
        self.assertIn('image-alt',[w['code'] for w in result['warnings']])

    def test_42_remote_image_warning(self):
        self.add(self.root/'README.md','![Remote example](https://example.invalid/chart.png)')
        result = self.refresh_and_check()
        self.assertIn('remote-image',[w['code'] for w in result['warnings']])

    def test_43_image_cannot_escape_package(self):
        self.add(self.root/'README.md','![Outside](../outside.svg)')
        self.expect('local-link')

    def test_44_fenced_image_not_live(self):
        self.add(self.root/'README.md','```markdown\n![Not live](missing.svg)\n```')
        self.refresh_and_check()

    def test_47_newer_minimum_validator_rejected(self):
        p=self.root/'publication.json';d=json.loads(p.read_text());d['minimum_validator']='9.99.0';p.write_text(json.dumps(d))
        self.expect('validator-version')

    def test_48_older_minimum_still_accepted(self):
        p=self.root/'publication.json';d=json.loads(p.read_text());d['minimum_validator']='9.0.0';p.write_text(json.dumps(d))
        for practice in (self.root/'practices').glob('*.md'):
            if v.parse(practice).meta.get('type') == 'practice':
                self.meta(practice,'practice_format','staged-inline-stageN-v1')
        self.refresh_and_check()

    def test_49_markdown_in_git_and_cache_not_knowledge(self):
        for name in ('.git/notes.md','.pytest_cache/README.md','__pycache__/sample.md'):
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('not a knowledge document')
        self.refresh_and_check()

    def test_50_missing_image_blocks_review_refresh(self):
        old=(self.root/'internal/metadata/summary-dependencies.json').read_bytes()
        self.add(self.root/'README.md','![Missing](absent.svg)')
        result=v.validate(self.root,refresh=True)
        self.assertFalse(result['ok'])
        self.assertEqual(old,(self.root/'internal/metadata/summary-dependencies.json').read_bytes())

    def test_52_steps_first_requires_declared_tool_floor(self):
        p=self.root/'publication.json';d=json.loads(p.read_text());d.pop('minimum_validator',None);p.write_text(json.dumps(d))
        self.expect('validator-version')

    def flexible_model(self):
        p = self.find('model')
        text = p.read_text()
        text = re.sub(r'## Key takeaway\n.*?(?=## Summary)', '', text, flags=re.S)
        text = text.replace('## Summary\n', '', 1)
        p.write_text(text)
        return p

    def test_model_with_introduction_and_subject_headings(self):
        p = self.flexible_model()
        p.write_text(p.read_text().replace('Representation', 'Entities and relations').replace('#representation', '#entities-and-relations'))
        self.refresh_and_check()

    def test_model_missing_introduction(self):
        p = self.flexible_model()
        p.write_text(re.sub(r'(^# [^\n]+\n).*?(?=^## Contents)', r'\1\n', p.read_text(), flags=re.M|re.S))
        self.expect('model-introduction')

    def test_model_contents_navigation(self):
        p = self.find('model')
        original = p.read_text()
        for contents in ['', '- [Elsewhere](../README.md)', '- [Absent](#absent)', '```markdown\n- [Representation](#representation)\n```', '- [Limits](#assumptions-and-limits)\n- [Representation](#representation)', '- [Representation](#representation)\n- [Again](#representation)']:
            with self.subTest(contents=contents):
                p.write_text(re.sub(r'(^## Contents\n).*?(?=^## )', lambda m: m[1] + '\n' + contents + '\n\n', original, flags=re.M|re.S))
                self.expect('model-contents')

    def test_flexible_model_requires_declared_tool_floor(self):
        self.flexible_model()
        p = self.root/'publication.json'
        data = json.loads(p.read_text()); data['minimum_validator'] = '9.1.0'
        p.write_text(json.dumps(data))
        self.expect('validator-version')

if __name__=='__main__':unittest.main(verbosity=2)
