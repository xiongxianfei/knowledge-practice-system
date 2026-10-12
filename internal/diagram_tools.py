#!/usr/bin/env python3
"""Build or check a small set of D2 publication images, not a knowledge platform."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import xml.etree.ElementTree as ET
import validate as v

ROOT = Path(__file__).resolve().parents[1]
RELATIONS = ('uses_concepts', 'uses_principles', 'uses_models', 'uses_methods', 'uses_practices')


def local_path(root: Path, name: str) -> Path:
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Diagram path escapes repository: ' + name)
    return path


def knowledge_graph(root: Path, identity: str) -> str:
    """Generate one-hop metadata edges; they are use relations, not causal arrows."""
    docs = {}
    for folder in ('concepts', 'principles', 'models', 'methods', 'practices'):
        for path in sorted((root / folder).glob('*.md')):
            doc = v.parse(path)
            docs[doc.meta['id']] = doc
    if identity not in docs:
        raise ValueError('Unknown graph root: ' + identity)
    edges = [(identity, rel, target) for rel in RELATIONS
             for target in docs[identity].meta.get(rel, [])]
    ids = [identity] + sorted({target for _, _, target in edges} - {identity})
    names = {ident: 'n' + str(i) for i, ident in enumerate(ids)}
    lines = ['# Generated from current YAML metadata by diagram_tools.py.',
             '# Use relations only; not causality, proof, or a complete graph.',
             'direction: right']
    for ident in ids:
        if ident not in docs:
            raise ValueError('Unknown graph target: ' + ident)
        doc = docs[ident]
        title = next(title for level, title in doc.headings if level == 1)
        label = '\n'.join(textwrap.wrap(title, 24)) + '\n[' + doc.meta['type'] + ']'
        lines.append(names[ident] + ': ' + json.dumps(label))
    for source, rel, target in sorted(edges):
        lines.append(f'{names[source]} -> {names[target]}: {rel}')
    return '\n'.join(lines) + '\n'


def svg_check(data: bytes) -> None:
    """Check a parseable, static SVG; this does not judge visual clarity."""
    doc = ET.fromstring(data)
    if doc.tag != '{http://www.w3.org/2000/svg}svg':
        raise ValueError('Not an SVG root')
    for node in doc.iter():
        if node.tag.rsplit('}', 1)[-1] in ('script', 'foreignObject', 'image'):
            raise ValueError('Unexpected active or externally dependent SVG element')
        if any(key.lower().startswith('on') for key in node.attrib):
            raise ValueError('Unexpected SVG event handler')


def run(root: Path, write: bool = False, d2: str = 'd2') -> int:
    root = root.resolve()
    cfg = json.loads((root / 'diagrams/manifest.json').read_text(encoding='utf-8'))
    env = {key: value for key, value in os.environ.items()
           if not key.startswith('D2_') and key not in ('OMIT_VERSION', 'DEBUG')}
    version = subprocess.run([d2, '--version'], check=True, capture_output=True,
                             text=True, timeout=15, env=env).stdout.strip().lstrip('v')
    if version != cfg['d2_version']:
        raise ValueError(f"Expected D2 {cfg['d2_version']}; got {version}")
    registered = {item['source'] for item in cfg['diagrams']}
    actual = {p.relative_to(root).as_posix() for p in (root / 'diagrams').rglob('*.d2')}
    # On first build a generated metadata graph may not yet exist.
    generated = {item['source'] for item in cfg['diagrams'] if item.get('metadata_root')}
    if actual - registered or (registered - actual) - (generated if write else set()):
        raise ValueError('Unregistered or missing D2 sources')
    failures = []
    with tempfile.TemporaryDirectory() as temp:
        for index, item in enumerate(cfg['diagrams']):
            source = local_path(root, item['source'])
            target = source.with_suffix('.svg')
            if not local_path(root, item['owner']).is_file():
                raise ValueError('Missing diagram owner: ' + item['owner'])
            if item.get('metadata_root'):
                expected = knowledge_graph(root, item['metadata_root'])
                if write:
                    source.parent.mkdir(parents=True, exist_ok=True)
                    source.write_text(expected, encoding='utf-8')
                elif source.read_text(encoding='utf-8') != expected:
                    failures.append(item['source'] + ': stale metadata graph')
            output = Path(temp) / f'{index}.svg'
            command = [d2, '--layout', cfg['layout'], '--theme', str(cfg['theme']),
                       '--pad', str(cfg['pad']), '--salt', item['source'],
                       '--bundle=true', str(source), str(output)]
            subprocess.run(command, check=True, capture_output=True, timeout=60,
                           cwd=root, env=env)
            data = output.read_bytes()
            svg_check(data)
            if write:
                target.write_bytes(data)
            elif not target.is_file() or target.read_bytes() != data:
                failures.append(target.relative_to(root).as_posix() + ': missing or stale render')
    if failures:
        raise ValueError('\n'.join(failures))
    return len(cfg['diagrams'])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true', help='Regenerate D2 metadata graph and all SVGs')
    mode.add_argument('--check', action='store_true', help='Render temporarily and compare without writes (default)')
    parser.add_argument('--d2', default='d2', help='Path to D2 0.9.0 executable')
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        count = run(args.root, args.write, args.d2)
    except (OSError, ValueError, ET.ParseError, subprocess.SubprocessError) as exc:
        print('FAIL diagrams:', exc)
        if isinstance(exc, subprocess.CalledProcessError):
            print(exc.stderr.decode() if isinstance(exc.stderr, bytes) else exc.stderr)
        return 1
    print(('BUILT' if args.write else 'PASS'), count, 'D2/SVG pairs; semantic review is separate')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
