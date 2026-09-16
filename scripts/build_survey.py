#!/usr/bin/env python3
"""Assemble the maintained chapters and verified metadata; no network needed."""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOGS = ['foundations', 'frontier', 'extensions']
CHAPTERS = [
    'introduction.md', '00-reference-method.md',
    '01-pretraining-data-architecture.md', '02-posttraining-inference.md',
    '03-evaluation-multimodal.md', '04-community-radar.md', 'conclusion.md',
]


def canonical_url(url):
    match = re.search(r'arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})', url)
    return f'https://arxiv.org/abs/{match.group(1)}' if match else url.rstrip('/')


def load_papers():
    merged = {}
    for group in CATALOGS:
        path = ROOT / 'sources' / f'{group}.json'
        for original in json.loads(path.read_text()):
            entry = dict(original)
            key = canonical_url(entry['url'])
            if key in merged:
                merged[key]['catalogs'].append(group)
                continue
            entry['canonical_url'] = key
            entry['catalogs'] = [group]
            merged[key] = entry
    return list(merged.values())


def cell(value):
    if isinstance(value, list):
        value = ', '.join(value)
    return str(value or '未完整记录').replace('|', '\\|').replace('\n', ' ')


def bibliography(papers):
    rows = ['# 文献索引', '',
            f'本索引含 {len(papers)} 条去重后的论文与技术报告主源；社区讨论另列。按首发年份排序，不代表质量或热度排名。', '',
            '作者栏若为 et al. 仅记录经核验的首位作者；BibTeX 是轻量引用入口，投稿前应从主源补齐作者与正式出版信息。阅读深度详见结构化记录。', '',
            '| 年份 | 文献与原始来源 | 阅读深度 | 版本/状态 |',
            '|---|---|---|---|']
    bib = ['% Generated from verified source catalogs. Partial author lists are marked with "and others".', '']
    for p in sorted(papers, key=lambda x: (x['year'], x['title'])):
        rows.append(f"| {p['year']} | [{cell(p['title'])}]({p['canonical_url']}) | {cell(p.get('reading_depth'))} | {cell(p.get('version_read'))} / {cell(p['type'])} |")
        fields = {'title': p['title'], 'year': str(p['year']), 'url': p['canonical_url']}
        authors = p.get('authors')
        if authors:
            if isinstance(authors, str):
                authors = [authors]
            fields['author'] = ' and '.join('others' if a.lower() in ['et al.', 'et al'] else a for a in authors)
        fields['note'] = f"Verified {p['verification_date']}; version read: {p.get('version_read') or 'not recorded'}"
        bib.append('@misc{' + p['id'] + ',')
        for k, v in fields.items():
            v = str(v).replace('\\', '\\textbackslash{}').replace('&', '\\&').replace('%', '\\%').replace('_', '\\_')
            bib.append('  ' + k + ' = {' + v + '},')
        bib += ['}', '']
    (ROOT / 'REFERENCES.md').write_text('\n'.join(rows) + '\n')
    (ROOT / 'references.bib').write_text('\n'.join(bib))
    (ROOT / 'data' / 'papers.json').write_text(json.dumps(papers, ensure_ascii=False, indent=2) + '\n')


def assemble_chapter(path):
    text = path.read_text()
    # A source chapter owns h1; the assembled document owns the outer title.
    text = re.sub(r'^(#{1,5}) ', r'#\1 ', text, flags=re.M)

    def relocate(m):
        label, target = m.group(1), m.group(2)
        if urlparse(target).scheme or target.startswith('#'):
            return m.group(0)
        filepart, sep, anchor = target.partition('#')
        resolved = (path.parent / filepart).resolve()
        try:
            rel = resolved.relative_to(ROOT).as_posix()
        except ValueError:
            raise ValueError(f'Link escapes repository: {path}: {target}')
        return f'[{label}]({rel}{sep}{anchor})'

    return re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', relocate, text)


def main():
    (ROOT / 'data').mkdir(exist_ok=True)
    papers = load_papers()
    bibliography(papers)
    state = json.loads((ROOT / 'data/state.json').read_text())
    date = state['last_successful_search']
    lead = f'''# Scaling Law：问题驱动的技术演化综述

版本 {state["edition"]} · 检索与核验截至 {date} · 中文持续更新版

从“能否预测规模收益”到“如何联合分配预训练、后训练与推理预算”。本版含 {len(papers)} 条去重主源和独立社区雷达；属于代表性文献的叙事综合，非穷尽性系统综述，未独立复现实验。

![研究问题演化图](figures/evolution-map.png)

图为概念综合，不是实测曲线；箭头不自动意味着已证实的历史因果。

阅读入口：[仓库说明](README.md) · [方法与范围](METHODOLOGY.md) · [文献索引](REFERENCES.md) · [更新日志](CHANGELOG.md)

'''
    parts = [lead]
    for filename in CHAPTERS:
        parts.append(assemble_chapter(ROOT / 'docs' / filename))
    parts.append('## 文献索引\n\n完整元数据保存在 [文献索引](REFERENCES.md)、[BibTeX](references.bib) 和 [结构化文献库](data/papers.json)。正文各项非平凡技术结论均附对应主源链接。\n')
    # Include the title table for offline PDF readers.
    index = (ROOT / 'REFERENCES.md').read_text().split('| 年份 |', 1)[1]
    parts.append('| 年份 |' + index)
    (ROOT / 'SURVEY.zh-CN.md').write_text('\n\n---\n\n'.join(parts))
    print(f'Built SURVEY.zh-CN.md, REFERENCES.md, references.bib, data/papers.json; {len(papers)} unique sources.')


if __name__ == '__main__':
    main()
