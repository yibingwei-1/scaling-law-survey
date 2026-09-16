#!/usr/bin/env python3
"""Check source metadata and repository links; does not claim web revalidation."""
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {'id', 'title', 'year', 'url', 'type', 'branch', 'problem',
            'insight', 'limitation', 'reading_depth', 'verification_date'}


def main():
    problems = []
    ids = set()
    for group in ['foundations', 'frontier', 'extensions']:
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
    markdowns = [*ROOT.glob('*.md'), *ROOT.glob('docs/*.md')]
    for path in markdowns:
        text = path.read_text()
        if text.count('```') % 2:
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
