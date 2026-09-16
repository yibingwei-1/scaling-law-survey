#!/usr/bin/env python3
"""Assemble the maintained chapters and verified metadata; no network needed."""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOGS = ['foundations', 'frontier', 'extensions',
            'expansion-foundations', 'expansion-frontier', 'expansion-evaluation', 'editorial']
CHAPTERS = [
    'introduction.md',
    '01-predictability-budget.md', '02-data.md', '03-architecture-deployment.md',
    '04-posttraining.md', '05-inference.md', '06-theory-evaluation.md',
    '07-multimodal.md', '04-community-radar.md', 'conclusion.md',
    'glossary.md', '00-reference-method.md',
]


def canonical_url(url):
    match = re.search(r'arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})', url)
    return f'https://arxiv.org/abs/{match.group(1)}' if match else url.split('#')[0].rstrip('/')


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


def reading_label(paper):
    value = paper.get('reading_depth', '')
    if value in ('abstract', 'abstract_and_metadata') or '全文待精读' in value:
        return '摘要/元数据'
    if value == 'abstract_and_introduction' or '未精读全部方法' in value:
        return '摘要/引言'
    if value == 'full_text' or value.startswith('full primary article'):
        return '全文文字'
    if value == 'official_report_sections':
        return '官方报告选段'
    return '正文定向阅读'


def version_label(paper):
    value = paper.get('version_read') or ''
    match = re.search(r'\bv\d+\b', value)
    return match.group() if match else ('网页观测版' if 'web' in value.lower() else '见元数据')


def bibliography(papers):
    rows = ['# 文献索引', '',
            f'本索引含 {len(papers)} 条去重后的论文与技术报告主源；社区讨论另列。按首发年份排序，不代表质量或热度排名。', '',
            '作者栏若为 et al. 仅记录经核验的首位作者；BibTeX 是轻量引用入口，投稿前应从主源补齐作者与正式出版信息。表中阅读层级是简写，具体章节、局限和版本时间见 [papers.json](data/papers.json)。全文文字阅读不表示复核全部图像、代码或实验。', '',
            '| 年份 | 文献与原始来源 | 阅读深度 | 版本/状态 | 正文位置 |',
            '|---|---|---|---|---|']
    bib = ['% Generated from verified source catalogs. Partial author lists are marked with "and others".', '']
    english = ['# References', '',
               f'{len(papers)} distinct primary-source records, ordered by first-publication year. Community discussions are recorded separately. This is not a quality or popularity ranking.', '',
               'Reading-depth labels are abbreviated; exact sections, limitations, and versions are recorded in [papers.json](data/papers.json). Full-text reading does not mean that every figure, proof, or experiment has been independently verified. Partial author lists are marked in the BibTeX export and should be completed from primary sources before submission.', '',
               '| Year | Work and primary source | Reading depth | Version / type | Chapters |',
               '|---|---|---|---|---|']
    depth_en = {'摘要/元数据': 'Abstract / metadata', '摘要/引言': 'Abstract / introduction',
                '全文文字': 'Full text', '官方报告选段': 'Official report sections',
                '正文定向阅读': 'Selected full-text sections'}
    for p in sorted(papers, key=lambda x: (x['year'], x['title'])):
        locations = '、'.join(f'[{name[:2]}](docs/{name})' for name in p.get('cited_in', [])) or '索引／待深入综合'
        kind = '技术文章' if 'blog' in p['type'] else ('报告' if 'report' in p['type'] else '论文/预印本')
        rows.append(f"| {p['year']} | [{cell(p['title'])}]({p['canonical_url']}) | {reading_label(p)} | {version_label(p)} / {kind} | {locations} |")
        en_locations = ', '.join(f'[{name[:2]}](docs/en/{name})' for name in p.get('cited_in', [])) or 'Catalog only'
        en_kind = 'Technical article' if 'blog' in p['type'] else ('Report' if 'report' in p['type'] else 'Paper / preprint')
        en_version = {'网页观测版': 'Web snapshot', '见元数据': 'See metadata'}.get(version_label(p), version_label(p))
        english.append(f"| {p['year']} | [{cell(p['title'])}]({p['canonical_url']}) | {depth_en[reading_label(p)]} | {en_version} / {en_kind} | {en_locations} |")
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
    (ROOT / 'REFERENCES.en.md').write_text('\n'.join(english) + '\n')
    (ROOT / 'references.bib').write_text('\n'.join(bib))
    (ROOT / 'data' / 'papers.json').write_text(json.dumps(papers, ensure_ascii=False, indent=2) + '\n')


def citation_audit(papers):
    """Measure actual technical-chapter citation coverage, separately from catalog size."""
    lookup = {p['canonical_url']: p for p in papers}
    aliases = {url: url for url in lookup}
    for p in papers:
        for field in ('publication_url', 'fulltext_url', 'full_text_url'):
            if p.get(field):
                aliases[canonical_url(p[field])] = p['canonical_url']
    for p in papers:
        p['cited_in'] = []
    chapters = []
    unmatched = {}
    for name in CHAPTERS[1:8]:
        body = (ROOT / 'docs' / name).read_text()
        urls = {canonical_url(url) for url in re.findall(r'\]\((https?://[^\s)]+)\)', body)}
        matched = sorted({aliases[url] for url in urls if url in aliases})
        for url in matched:
            lookup[url]['cited_in'].append(name)
        unmatched[name] = sorted(urls - aliases.keys())
        chapters.append({'file': name, 'title': body.splitlines()[0].lstrip('# '),
                         'han_characters': len(re.findall(r'[\u4e00-\u9fff]', body)),
                         'catalog_sources_cited': len(matched),
                         'all_external_links': len(urls)})
    audit = {'catalog_count': len(papers), 'cited_in_technical_chapters': sum(bool(p['cited_in']) for p in papers),
             'chapters': chapters, 'external_links_without_catalog_match': unmatched}
    (ROOT / 'data/citation-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
    rows = ['# 正文覆盖与阅读地图', '',
            '由构建脚本按七篇技术章中的实际主源链接计算。引用数量、阅读深度、论证质量是不同维度；表格不把索引收录等同于深度综合。', '',
            '| 问题线 | 正文汉字数 | 已收录主源引用数 |', '|---|---:|---:|']
    for c in chapters:
        rows.append(f"| [{c['title']}]({c['file']}) | {c['han_characters']:,} | {c['catalog_sources_cited']} |")
    rows += ['', f"文献库去重后 {len(papers)} 条，其中 {audit['cited_in_technical_chapters']} 条在七篇技术章中实际引用。共享来源不重复计入总数。", '',
             '逐条阅读深度与版本见[文献索引](../REFERENCES.md)，机器可读的章节映射见[citation-audit.json](../data/citation-audit.json)。', '']
    (ROOT / 'docs/evidence-map.md').write_text('\n'.join(rows))


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
    citation_audit(papers)
    bibliography(papers)
    state = json.loads((ROOT / 'data/state.json').read_text())
    date = state['last_successful_search']
    lead = f'''# Scaling Law：问题驱动的技术演化综述

版本 {state["edition"]} · 检索与核验截至 {date} · 中文持续更新版

从“能否预测规模收益”到“如何联合分配预训练、后训练与推理预算”。本版含 {len(papers)} 条去重主源和独立社区雷达；属于代表性文献的叙事综合，非穷尽性系统综述，未独立复现实验。

![研究问题演化图](figures/evolution-map.png)

图为概念综合，不是实测曲线；箭头不自动意味着已证实的历史因果。

阅读入口：[中文首页](README-zh.md) · [English edition](SURVEY.en.md) · [方法与范围](METHODOLOGY.md) · [文献索引](REFERENCES.md) · [更新日志](CHANGELOG.md)

'''
    parts = [lead]
    for filename in CHAPTERS:
        parts.append(assemble_chapter(ROOT / 'docs' / filename))
    parts.append('## 文献索引\n\n完整元数据保存在 [文献索引](REFERENCES.md)、[BibTeX](references.bib) 和 [结构化文献库](data/papers.json)。正文各项非平凡技术结论均附对应主源链接。\n')
    # Include the title table for offline PDF readers.
    index = (ROOT / 'REFERENCES.md').read_text().split('| 年份 |', 1)[1]
    parts.append('| 年份 |' + index)
    (ROOT / 'SURVEY.zh-CN.md').write_text('\n\n---\n\n'.join(parts))
    en_lead = f'''# Scaling Law: A Problem-Driven Review

Edition {state["edition"]} · Searches and verification through {date} · English living edition

From predicting returns to scale to jointly allocating pretraining, post-training, and inference budgets. This edition contains {len(papers)} distinct primary-source records and a separate community radar. It is a representative narrative review, not an exhaustive systematic review; the cited experiments have not been independently reproduced.

![Research problem evolution map](figures/evolution-map.png)

The figure is a conceptual synthesis, not an experimental curve; arrows do not automatically establish historical causation.

Reading links: [English homepage](README.md) · [Chinese edition](SURVEY.zh-CN.md) · [References](REFERENCES.en.md) · [Translation status](data/translation-status.json)

'''
    english = [en_lead]
    for filename in CHAPTERS:
        english.append(assemble_chapter(ROOT / 'docs/en' / filename))
    english.append('## References\n\nFull metadata are available in the [reference index](REFERENCES.en.md), [BibTeX](references.bib), and [structured catalog](data/papers.json). Technical claims in the text link to their primary sources.\n')
    index_en = (ROOT / 'REFERENCES.en.md').read_text().split('| Year |', 1)[1]
    english.append('| Year |' + index_en)
    (ROOT / 'SURVEY.en.md').write_text('\n\n---\n\n'.join(english))
    print(f'Built Chinese and English surveys and reference indexes, BibTeX, and source metadata; {len(papers)} unique sources.')


if __name__ == '__main__':
    main()
