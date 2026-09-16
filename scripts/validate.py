#!/usr/bin/env python3
"""Check source metadata and repository links; does not claim web revalidation."""
import json
import hashlib
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse
from build_survey import CATALOGS, CHAPTERS

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {'id', 'title', 'year', 'url', 'type', 'branch', 'problem',
            'insight', 'limitation', 'reading_depth', 'verification_date'}


def main():
    problems = []
    ids = set()
    for group in CATALOGS:
        path = ROOT / 'sources' / f'{group}.json'
        entries = json.loads(path.read_text())
        for p in entries:
            missing = REQUIRED - p.keys()
            if missing:
                problems.append(f'{path.name}: missing {sorted(missing)}')
            if p['id'] in ids:
                problems.append(f'Duplicate source ID: {p["id"]}')
            ids.add(p['id'])
            if not p['url'].startswith('https://'):
                problems.append(f'Invalid URL: {p["url"]}')
            if p['year'] > date.today().year:
                problems.append(f'Future source: {p["id"]}')
    for name in CHAPTERS:
        for folder in ('docs', 'docs/en'):
            if not (ROOT / folder / name).exists():
                problems.append(f'Missing maintained chapter: {folder}/{name}')
    manifest_path = ROOT / 'data/translation-status.json'
    if not manifest_path.exists():
        problems.append('Missing translation status manifest')
    else:
        translations = json.loads(manifest_path.read_text()).get('chapters', {})
        for name in CHAPTERS:
            zh_path, en_path = ROOT / 'docs' / name, ROOT / 'docs/en' / name
            if not zh_path.exists() or not en_path.exists():
                continue
            zh, en = zh_path.read_text(), en_path.read_text()
            record = translations.get(name, {})
            if record.get('status') != 'reviewed_translation':
                problems.append(f'Translation has not been marked reviewed: {name}')
            if re.search(r'[\u3400-\u4dbf\u4e00-\u9fff]', en):
                problems.append(f'Chinese text remains in English chapter: {name}')
            for key, path in [('source_sha256', zh_path), ('translation_sha256', en_path)]:
                if record.get(key) != hashlib.sha256(path.read_bytes()).hexdigest():
                    problems.append(f'Translation review is stale: {name}/{key}')
            urls = lambda s: Counter(re.findall(r'\]\((https?://[^\s)]+)\)', s))
            if urls(zh) != urls(en):
                problems.append(f'External source links differ between languages: {name}')
            formulas = lambda s: [re.sub(r'\s+', '', f) for f in re.findall(r'\$\$(.*?)\$\$', s, re.S)]
            if formulas(zh) != formulas(en):
                problems.append(f'Display formulas differ between languages: {name}')
            inline_formulas = lambda s: re.findall(r'(?<!\$)\$([^$\n]+)\$(?!\$)', re.sub(r'\$\$.*?\$\$', '', s, flags=re.S))
            if Counter(inline_formulas(zh)) != Counter(inline_formulas(en)):
                problems.append(f'Inline formulas differ between languages: {name}')
    social = json.loads((ROOT / 'sources/community.json').read_text())['entries']
    platforms = {e['platform'] for e in social}
    if not {'X', 'YouTube', 'Reddit'} <= platforms:
        problems.append(f'Missing community platform: {platforms}')
    if len({e['id'] for e in social}) != len(social):
        problems.append('Duplicate community ID')
    for p in social:
        for key, value in p['metrics'].items():
            if value is not None and (not isinstance(value, (int, float)) or value < 0):
                problems.append(f'Invalid metric: {p["id"]}/{key}')
    markdowns = [*ROOT.glob('*.md'), *ROOT.glob('docs/**/*.md')]
    for path in markdowns:
        text = path.read_text()
        if text.count('```') % 2 or text.count('~~~') % 2:
            problems.append(f'Unclosed code fence: {path.name}')
        for target in re.findall(r'\]\(([^\s)]+)\)', text):
            if urlparse(target).scheme or target.startswith('#'):
                continue
            dest = (path.parent / unquote(target.split('#')[0])).resolve()
            if not dest.exists():
                problems.append(f'Broken local link: {path.relative_to(ROOT)} -> {target}')
        if re.search(r'turn\d+(?:search|view)\d+|cite', text):
            problems.append(f'Unresolved tool citation: {path.name}')
    if problems:
        raise SystemExit('\n'.join(problems))
    print(f'PASS: {len(ids)} source records, {len(social)} community records, {len(markdowns)} Markdown files; local links and schemas checked.')
    print('External URLs and scientific claims require primary-source review; this script does not replace it.')


if __name__ == '__main__':
    main()
