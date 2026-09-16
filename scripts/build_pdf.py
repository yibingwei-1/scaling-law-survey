#!/usr/bin/env python3
"""Build a readable Chinese PDF from the maintained Markdown survey.

Usage: python scripts/build_pdf.py [--input SURVEY.zh-CN.md] [--output PATH]
Dependencies: reportlab, Pillow. Optional: matplotlib for display mathematics,
pypdf for --check. An existing separate Python environment may provide mathtext
via --math-python; this script never installs packages.
"""
from __future__ import annotations

import argparse
from datetime import date
import hashlib
from html import escape
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import quote

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Flowable, Frame, HRFlowable, Image, KeepTogether,
    LongTable, PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
NAVY = colors.HexColor('#142F46')
TEAL = colors.HexColor('#007F86')
TEXT = colors.HexColor('#253541')
MUTED = colors.HexColor('#5C6E7B')
PALE = colors.HexColor('#EEF5F6')
LINE = colors.HexColor('#D4E0E4')
FORMULA_DIR = ROOT / 'tmp' / 'pdfs' / 'formulas'
FORMULA_DPI = 240
FORMULA_FONT_SIZE = 13
FORMULA_STATS = {'rendered': 0, 'fallback': 0}
MATH_PYTHON = None
_MATH_BACKEND_CHECKED = False


def register_fonts():
    paths = [('/System/Library/Fonts/STHeiti Light.ttc', 'CJK'),
             ('/System/Library/Fonts/STHeiti Medium.ttc', 'CJKBold')]
    try:
        for path, name in paths:
            pdfmetrics.registerFont(TTFont(name, path, subfontIndex=0))
    except Exception:
        pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
        return 'STSong-Light', 'STSong-Light'
    pdfmetrics.registerFontFamily('CJK', normal='CJK', bold='CJKBold',
                                 italic='CJK', boldItalic='CJKBold')
    return 'CJK', 'CJKBold'


FONT, BOLD = register_fonts()


def notation(text):
    """Readable fallback; retain unknown commands rather than losing symbols."""
    text = text.strip()
    text = re.sub(r'\\(?:begin|end)\{(?:aligned|gathered|split)\}', '', text)
    text = re.sub(r'\\label\{[^}]+\}', '', text)
    text = re.sub(r'\\tag\{([^}]+)\}', r' (\1)', text)
    for _ in range(5):
        text = re.sub(r'\\(?:text|mathrm|mathbf|mathcal|operatorname|textbf|textrm)\{([^{}]*)\}', r'\1', text)
        text = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', r'(\1)/(\2)', text)
        text = re.sub(r'\\sqrt\{([^{}]*)\}', r'sqrt(\1)', text)
        text = re.sub(r'([_^])\{([^{}]*)\}', r'\1(\2)', text)
    replacements = {
        'alpha': 'alpha', 'beta': 'beta', 'gamma': 'gamma', 'delta': 'delta',
        'theta': 'theta', 'lambda': 'lambda', 'epsilon': 'epsilon', 'pi': 'pi',
        'eta': 'eta', 'sigma': 'sigma', 'mu': 'mu', 'rho': 'rho', 'phi': 'phi',
        'approx': ' ~= ', 'simeq': ' ~= ', 'sim': ' ~ ', 'propto': ' proportional to ',
        'times': ' x ', 'cdot': ' * ', 'leq': ' <= ', 'geq': ' >= ', 'le': ' <= ',
        'ge': ' >= ', 'neq': ' != ', 'infty': 'infinity', 'to': ' -> ',
        'rightarrow': ' -> ', 'Rightarrow': ' => ', 'in': ' in ',
        'sum': 'sum', 'prod': 'prod', 'min': 'min', 'max': 'max',
        'argmin': 'argmin', 'argmax': 'argmax', 'log': 'log', 'exp': 'exp',
        'left': '', 'right': '', 'qquad': '    ', 'quad': '  ',
        'mid': ' | ', 'vert': '|',
    }
    for key in sorted(replacements, key=len, reverse=True):
        text = re.sub(r'\\' + key + r'(?![A-Za-z])', lambda m: replacements[key], text)
    text = re.sub(r'\\([,;:! ])', ' ', text)
    text = text.replace('\\\\', '\n').replace('\\%', '%').replace('\\_', '_')
    text = text.replace('\\{', '{').replace('\\}', '}')
    # Only alignment markers are removable; escaped ampersands remain literal.
    text = re.sub(r'(?<!\\)&', ' ', text).replace(r'\&', '&')
    text = text.translate(str.maketrans({'α': 'alpha', 'β': 'beta', '∝': ' proportional to ',
        '≈': ' ~= ', '∞': 'infinity', '≤': '<=', '≥': '>=', '×': ' x ', '−': '-'}))
    return text.strip()


def safe_text(text):
    return text.translate(str.maketrans({'\u2011': '-', '\u2013': '-', '\u2014': '-',
                                        '\u2212': '-', '\u00a0': ' '}))


def plain(text):
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'[*`]', '', text)
    return safe_text(text)


def inline(text):
    text = safe_text(text)
    text = re.sub(r'\\\((.*?)\\\)', lambda m: notation(m.group(1)), text)
    text = re.sub(r'(?<!\\)\$([^$\n]+)\$', lambda m: notation(m.group(1)), text)
    placeholders = []

    def protect(value):
        placeholders.append(value)
        return f'ZZPROTECTEDTOKEN{len(placeholders)-1}ZZ'

    def link(m):
        label, url = m.group(1), m.group(2).strip().strip('<>')
        if url.startswith(('http://', 'https://', 'mailto:')):
            return protect(f'<link href="{escape(url, quote=True)}" color="#007F86">{escape(plain(label))}</link>')
        # Relative repository links need not become invalid local hyperlinks.
        return protect(f'<font color="#007F86">{escape(plain(label))}</font>')

    text = re.sub(r'\[([^\]]+)\]\(([^\s]+)(?:\s+"[^"]*")?\)', link, text)
    text = re.sub(r'`([^`]+)`', lambda m: protect(f'<font name="{FONT}" color="#355169">{escape(m.group(1))}</font>'), text)
    text = escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', rf'<font name="{BOLD}">\1</font>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'(?<![="\w])(https?://[^\s<>]+)',
                  lambda m: f'<link href="{m.group(1)}" color="#007F86">{m.group(1)}</link>', text)
    for i, fragment in enumerate(placeholders):
        text = text.replace(f'ZZPROTECTEDTOKEN{i}ZZ', fragment)
    return text


def make_styles():
    base = dict(fontName=FONT, fontSize=10, leading=16.4, textColor=TEXT,
                wordWrap='CJK', splitLongWords=True, allowWidows=0, allowOrphans=0)
    styles = {'body': ParagraphStyle('body', spaceAfter=7.5, **base)}
    styles['small'] = ParagraphStyle('small', **{**base, 'fontSize': 8.7, 'leading': 13.4}, textTransform=None, spaceAfter=6)
    styles['quote'] = ParagraphStyle('quote', **base, leftIndent=11, rightIndent=8,
                                     borderColor=LINE, borderWidth=0.5, borderPadding=9,
                                     backColor=PALE, spaceBefore=5, spaceAfter=11)
    styles['list'] = ParagraphStyle('list', **base, leftIndent=13, firstLineIndent=-10,
                                    spaceAfter=5, bulletIndent=0)
    for level, size, lead, before, after in [(1, 23, 31, 8, 16), (2, 17, 25, 19, 11),
                                           (3, 12.5, 19.5, 13, 7), (4, 10.6, 17, 10, 5)]:
        styles[f'h{level}'] = ParagraphStyle(f'h{level}', fontName=BOLD, fontSize=size,
            leading=lead, textColor=NAVY if level < 3 else TEAL, wordWrap='CJK',
            spaceBefore=before, spaceAfter=after, keepWithNext=True)
    styles['table'] = ParagraphStyle('table', fontName=FONT, fontSize=8.2, leading=12.5,
        textColor=TEXT, wordWrap='CJK', splitLongWords=True, allowWidows=1, allowOrphans=1)
    styles['thead'] = ParagraphStyle('thead', parent=styles['table'], fontName=BOLD, textColor=colors.white)
    styles['code'] = ParagraphStyle('code', fontName=FONT, fontSize=8.4, leading=13.3,
        textColor=NAVY, wordWrap='CJK', splitLongWords=True, borderColor=LINE,
        borderWidth=0.4, borderPadding=9, backColor=PALE, spaceBefore=4, spaceAfter=10)
    return styles


STYLES = make_styles()


class SurveyDoc(BaseDocTemplate):
    def __init__(self, filename, edition, **kwargs):
        self.edition = edition
        self.heading_serial = 0
        super().__init__(filename, pagesize=A4, leftMargin=23*mm, rightMargin=23*mm,
                         topMargin=22*mm, bottomMargin=21*mm, **kwargs)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height,
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate('survey', [frame], onPage=self.decorate)])

    def beforeDocument(self):
        self.canv.setTitle('Scaling Law：问题驱动的技术演化综述')
        self.canv.setAuthor('Scaling Law Survey')
        self.canv.setSubject('训练资源分配、数据、推理与后训练 scaling 的问题驱动综述')
        self.heading_serial = 0

    def decorate(self, canvas, doc):
        if doc.page == 1:
            return
        canvas.saveState()
        w, h = A4
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(.5)
        canvas.line(doc.leftMargin, h-16.5*mm, w-doc.rightMargin, h-16.5*mm)
        canvas.setFillColor(MUTED)
        canvas.setFont(FONT, 8)
        canvas.drawString(doc.leftMargin, h-13*mm, 'SCALING LAW  /  问题驱动综述')
        canvas.drawRightString(w-doc.rightMargin, h-13*mm, self.edition)
        canvas.line(doc.leftMargin, 16.5*mm, w-doc.rightMargin, 16.5*mm)
        canvas.drawString(doc.leftMargin, 12*mm, '来源链接可点击  ·  经验结论保留适用范围')
        canvas.drawRightString(w-doc.rightMargin, 12*mm, f'{doc.page:02d}')
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and hasattr(flowable, '_toc_level'):
            level, title = flowable._toc_level, flowable.getPlainText()
            key = f'heading-{self.heading_serial}'
            self.heading_serial += 1
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, level=level, closed=False)
            if level == 0:
                self.notify('TOCEntry', (level, title, self.page, key))


def heading(text, level):
    p = Paragraph(inline(text), STYLES[f'h{min(level,4)}'])
    if level in (2,3):
        p._toc_level = level-2
    return p


def split_cells(line):
    cells = re.split(r'(?<!\\)\|', line.strip().strip('|'))
    return [c.strip().replace('\\|', '|').replace('<br>', '<br/>') for c in cells]


def markdown_table(lines, width):
    rows = [split_cells(line) for line in lines]
    rows = [r for r in rows if not all(re.fullmatch(r'\s*:?-{3,}:?\s*', c) for c in r)]
    n = max(map(len, rows))
    for row in rows:
        row += ['']*(n-len(row))
    # A clipped long row is worse than using a smaller, wrapped table style.
    style = STYLES['table'] if n < 6 else ParagraphStyle('dense-table', parent=STYLES['table'], fontSize=7.5, leading=11.5)
    scores = []
    for col in range(n):
        lengths = sorted(len(plain(r[col])) for r in rows)
        # Capping limits the effect of a single long URL or discussion cell.
        scores.append(max(5, min(32, lengths[len(lengths)//2]))**.65)
    if n == 2:
        ratio = max(.23, min(.40, scores[0]/sum(scores)))
        widths = [width*ratio, width*(1-ratio)]
    else:
        minimum = width*(.115 if n <= 5 else .10)
        remainder = width-minimum*n
        widths = [minimum + remainder*s/sum(scores) for s in scores]
    data = [[Paragraph(inline(c), STYLES['thead'] if i == 0 else style)
             for c in row] for i, row in enumerate(rows)]
    table = LongTable(data, colWidths=widths, repeatRows=1, hAlign='LEFT',
                      splitByRow=1, splitInRow=0, spaceBefore=6, spaceAfter=13)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F4F7F8')]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 6), ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LINEBELOW', (0,0), (-1,0), .7, NAVY),
        ('LINEBELOW', (0,1), (-1,-1), .35, LINE),
    ]))
    return table


def math_environment():
    """Keep both Matplotlib and fontconfig caches inside the workspace."""
    cache = ROOT / 'tmp' / 'pdfs' / 'cache'
    cache.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env['MPLBACKEND'] = 'Agg'
    env['MPLCONFIGDIR'] = str(cache / 'matplotlib')
    env['XDG_CACHE_HOME'] = str(cache)
    return env


def math_python():
    """Locate an existing renderer once; no package installation or downloads."""
    global MATH_PYTHON, _MATH_BACKEND_CHECKED
    if _MATH_BACKEND_CHECKED:
        return MATH_PYTHON
    _MATH_BACKEND_CHECKED = True
    requested = MATH_PYTHON or os.environ.get('SCALING_LAW_MATH_PYTHON')
    candidates = [requested] if requested else [
        sys.executable,
        str(Path.home() / 'anaconda3' / 'bin' / 'python'),
        str(Path.home() / 'miniforge3' / 'bin' / 'python'),
        str(Path.home() / 'miniconda3' / 'bin' / 'python'),
        shutil.which('python3'),
    ]
    MATH_PYTHON = None
    for candidate in dict.fromkeys(c for c in candidates if c):
        executable = shutil.which(candidate) or candidate
        if not Path(executable).is_file():
            continue
        try:
            check = subprocess.run(
                [executable, '-c', 'from matplotlib.mathtext import math_to_image; from PIL import Image'],
                capture_output=True, text=True, timeout=30, env=math_environment())
            if check.returncode == 0:
                MATH_PYTHON = executable
                break
        except (OSError, subprocess.TimeoutExpired):
            continue
    return MATH_PYTHON


def normalize_mathtext(source):
    """Normalize only presentation macros; keep all mathematical content.

    Mathtext does not implement LaTeX environments. For aligned/split/gathered,
    render complete rows in their original order, removing only alignment marks.
    Unknown environments/commands are left intact so a failed parse is explicit.
    """
    source = source.strip()
    # A source newline is TeX whitespace, not a displayed line break (\\\\).
    # Mathtext rejects embedded literal newlines inside a single math span.
    source = re.sub(r'\s*\n\s*', ' ', source)
    source = re.sub(r'\\(?:begin|end)\{(?:aligned|gathered|split)\}', '', source)
    source = re.sub(r'\\label\{[^}]+\}', '', source)
    source = re.sub(r'\\tag\{([^}]+)\}', r'\\qquad(\1)', source)
    source = re.sub(r'\\(?:displaystyle|textstyle|limits)(?![A-Za-z])', '', source)
    source = re.sub(r'\\(?:big|Big|bigg|Bigg)[lr]?(?![A-Za-z])', '', source)
    source = re.sub(r'\\(?:dfrac|tfrac)(?![A-Za-z])', r'\\frac', source)
    source = re.sub(r'\\operatorname\*', r'\\operatorname', source)
    source = re.sub(r'\\(argmin|argmax)(?![A-Za-z])', r'\\operatorname{\1}', source)
    # Matplotlib 3.7 has no \\text. Preserve word separation in roman labels.
    source = re.sub(r'\\(?:text|textrm|textnormal)\{([^{}]*)\}',
                    lambda m: r'\mathrm{' + m.group(1).replace(' ', r'\ ') + '}', source)
    if re.search(r'[\u3400-\u9fff]', source):
        raise ValueError('Chinese formula annotations require text fallback')
    rows, current, depth, index = [], [], 0, 0
    while index < len(source):
        if source[index:index+2] == r'\\' and depth == 0:
            row = ''.join(current).strip()
            if row:
                rows.append(row)
            current = []
            index += 2
            spacing = re.match(r'\[[^\]]*\]', source[index:])
            if spacing:
                index += len(spacing.group())
            continue
        char = source[index]
        escaped = index > 0 and source[index-1] == '\\'
        if char == '{' and not escaped:
            depth += 1
        elif char == '}' and not escaped:
            depth -= 1
        if char != '&' or escaped:
            current.append(char)
        index += 1
    if ''.join(current).strip():
        rows.append(''.join(current).strip())
    if not rows:
        raise ValueError('Empty formula')
    return rows


MATH_RENDER_WORKER = r'''
import io, json, sys, warnings
import matplotlib
matplotlib.use('Agg')
from matplotlib.font_manager import FontProperties
from matplotlib.mathtext import math_to_image
from PIL import Image
job = json.load(sys.stdin)
warnings.filterwarnings('error', message='.*[Gg]lyph.*missing.*')
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
rows = []
for expression in job['rows']:
    buffer = io.BytesIO()
    math_to_image('$' + expression + '$', buffer,
                  prop=FontProperties(size=job['font_size']),
                  dpi=job['dpi'], format='png', color='#142F46')
    buffer.seek(0)
    image = Image.open(buffer).convert('RGBA')
    rows.append(image.copy())
padding = round(job['dpi'] * 5 / 72)
gap = round(job['dpi'] * 6 / 72)
width = max(image.width for image in rows) + padding * 2
height = sum(image.height for image in rows) + gap * (len(rows)-1) + padding * 2
canvas = Image.new('RGBA', (width, height), (255, 255, 255, 255))
y = padding
for image in rows:
    canvas.alpha_composite(image, ((width-image.width)//2, y))
    y += image.height + gap
canvas.convert('RGB').save(job['output'], dpi=(job['dpi'], job['dpi']))
'''


def formula_block(lines, is_math=True, width=None):
    source = '\n'.join(lines)
    if not is_math:
        rendered = '<br/>'.join(escape(safe_text(line)) for line in source.splitlines())
        return Paragraph(rendered or ' ', STYLES['code'])
    width = width or A4[0] - 46*mm
    try:
        rows = normalize_mathtext(source)
        backend = math_python()
        if not backend:
            raise ValueError('No existing Python environment provides matplotlib')
        FORMULA_DIR.mkdir(parents=True, exist_ok=True)
        digest = hashlib.sha256(json.dumps(
            [rows, FORMULA_DPI, FORMULA_FONT_SIZE, 'stix-v1'], ensure_ascii=False
        ).encode('utf-8')).hexdigest()[:20]
        output = FORMULA_DIR / f'{digest}.png'
        if not output.exists():
            job = {'rows': rows, 'output': str(output),
                   'dpi': FORMULA_DPI, 'font_size': FORMULA_FONT_SIZE}
            result = subprocess.run([backend, '-c', MATH_RENDER_WORKER],
                input=json.dumps(job), text=True, capture_output=True,
                timeout=45, env=math_environment())
            if result.returncode:
                error = result.stderr.strip().splitlines()
                raise ValueError(error[-1] if error else 'mathtext renderer failed')
        with PILImage.open(output) as image:
            image_width, image_height = image.size
        scale = min(72 / FORMULA_DPI, width / image_width)
        if FORMULA_FONT_SIZE * scale * FORMULA_DPI / 72 < 8:
            raise ValueError('Formula too wide to remain legible at page width')
        rendered = Image(str(output), width=image_width*scale,
                         height=image_height*scale, hAlign='CENTER')
        rendered.spaceBefore = 5
        rendered.spaceAfter = 10
        FORMULA_STATS['rendered'] += 1
        return rendered
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        FORMULA_STATS['fallback'] += 1
        print(f'Formula fallback: {error}; source={source[:100]!r}', file=sys.stderr)
        # Unknown TeX remains visible instead of being guessed or silently dropped.
        text = notation(source)
        rendered = '<br/>'.join(escape(safe_text(line)) for line in text.splitlines())
        return KeepTogether([
            Paragraph('公式文本回退：未能完整排版；未识别的 LaTeX 记号保留如下。', STYLES['small']),
            Paragraph(rendered or ' ', STYLES['code']),
        ])


def parse_markdown(text, width, source_dir):
    lines, story, i = text.splitlines(), [], 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line in ('---', '***', '___'):
            i += 1
            continue
        if line.startswith('<!--'):
            while i < len(lines) and '-->' not in lines[i]:
                i += 1
            i += 1
            continue
        m = re.match(r'^(#{1,6})\s+(.+)', line)
        if m:
            level = len(m.group(1))
            if level != 1:  # Cover owns the document title.
                story.append(heading(m.group(2), level))
            i += 1
            continue
        if line.startswith('```'):
            language = line[3:].lower()
            block, i = [], i+1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                block.append(lines[i])
                i += 1
            if language == 'mermaid':
                story.append(Paragraph('本处 Mermaid 图未在 PDF 中渲染；可编辑图及对应关系见 Markdown 正文。', STYLES['small']))
            else:
                story.append(formula_block(block, language in ('math', 'latex', 'tex'), width))
            i += 1
            continue
        if line.startswith('$$') or line.startswith(r'\['):
            closing = '$$' if line.startswith('$$') else r'\]'
            opening = '$$' if closing == '$$' else r'\['
            remainder = line[len(opening):]
            block=[]
            if remainder.endswith(closing) and remainder:
                block.append(remainder[:-len(closing)])
            else:
                if remainder:
                    block.append(remainder)
                i += 1
                while i < len(lines) and closing not in lines[i]:
                    block.append(lines[i])
                    i += 1
                if i < len(lines):
                    block.append(lines[i].split(closing)[0])
            story.append(formula_block(block, width=width))
            i += 1
            continue
        if '|' in line and i+1 < len(lines) and re.search(r'\|?\s*:?-{3,}', lines[i+1]):
            block=[]
            while i < len(lines) and '|' in lines[i]:
                block.append(lines[i]); i += 1
            story.append(markdown_table(block, width))
            continue
        im = re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)', line)
        if im:
            path=(source_dir/im.group(2)).resolve()
            if path.exists():
                with PILImage.open(path) as img: iw, ih=img.size
                scale=min(width/iw, 195*mm/ih)
                story.append(Image(str(path), width=iw*scale, height=ih*scale))
                if im.group(1): story.append(Paragraph(inline(im.group(1)), STYLES['small']))
            i += 1; continue
        if line.startswith('>'):
            block=[]
            while i < len(lines) and lines[i].strip().startswith('>'):
                block.append(lines[i].strip().lstrip('>').strip()); i+=1
            story.append(Paragraph(inline(' '.join(block)), STYLES['quote']))
            continue
        lm=re.match(r'^([-*+]\s+|\d+[.)]\s+)(.+)', line)
        if lm:
            marker='• ' if not lm.group(1)[0].isdigit() else lm.group(1)
            story.append(Paragraph(inline(marker+lm.group(2)), STYLES['list']))
            i+=1; continue
        block=[line]; i+=1
        while i < len(lines) and lines[i].strip():
            s=lines[i].strip()
            if re.match(r'^(#{1,6}\s|>|```|\$\$|\\\[|[-*+]\s|\d+[.)]\s|!\[)',s): break
            if '|' in s and i+1 < len(lines) and re.search(r'\|?\s*:?-{3,}',lines[i+1]): break
            block.append(s); i+=1
        story.append(Paragraph(inline(' '.join(block)), STYLES['body']))
    return story


def cover(doc, edition, diagram):
    title=ParagraphStyle('cover-title', fontName=BOLD, fontSize=42, leading=50, textColor=NAVY)
    subtitle=ParagraphStyle('cover-subtitle', fontName=BOLD, fontSize=20, leading=31, textColor=NAVY, wordWrap='CJK')
    kicker=ParagraphStyle('cover-kicker', fontName=BOLD, fontSize=10, leading=16, textColor=TEAL, charSpace=1)
    story=[Spacer(1, 19*mm), Paragraph('RESEARCH REVIEW  /  持续更新',kicker), Spacer(1,10*mm),
           Paragraph('Scaling Law',title), Spacer(1,5*mm),
           Paragraph('问题驱动的技术演化综述',subtitle), Spacer(1,10*mm),
           HRFlowable(width='100%', thickness=2, color=TEAL), Spacer(1,8*mm),
           Paragraph('从资源配置到数据、推理与后训练的边界',STYLES['h3']),
           Paragraph('沿着问题、方法、局限与下一步的关系，重建研究对话。',STYLES['body']),
           Spacer(1,14*mm), Paragraph(f'版本日期  {edition}',STYLES['body']),
           Paragraph('中文阅读版 · 原始论文、技术报告与社区讨论分层呈现',STYLES['small']),
           Paragraph('本文包含可点击来源与导航书签。独立公式优先以数学排版呈现；不支持的公式明确标记文本回退。行内公式采用可读记号，持续修订以 Markdown 源文件为准。',STYLES['small']),
           Spacer(1,12*mm), Paragraph('问题 → 核心洞察 → 方法 → 实验证据 → 限制 → 后续分支', STYLES['quote']),
           PageBreak()]
    story.append(Paragraph('阅读导航',STYLES['h1']))
    story.append(Paragraph('目录页码与 PDF 页码一致。点击标题可跳转；侧边栏书签提供同样的章节导航。',STYLES['small']))
    toc=TableOfContents()
    toc.levelStyles=[ParagraphStyle('toc-main',fontName=BOLD,fontSize=10.3,leading=16,
        textColor=NAVY,wordWrap='CJK',spaceBefore=7,leftIndent=0,rightIndent=28),
        ParagraphStyle('toc-sub',fontName=FONT,fontSize=9.1,leading=14,
        textColor=TEXT,wordWrap='CJK',spaceBefore=3,leftIndent=14,rightIndent=28)]
    toc.dotsMinLevel=0
    story += [toc,PageBreak()]
    if diagram and diagram.exists():
        story.append(Paragraph('研究问题的演化图',STYLES['h1']))
        with PILImage.open(diagram) as im: iw,ih=im.size
        scale=min(doc.width/iw, 208*mm/ih)
        story.append(Image(str(diagram),width=iw*scale,height=ih*scale))
        story.append(Spacer(1,5*mm))
        story.append(Paragraph('图示作为阅读索引。正文区分直接回应、共同瓶颈与并行路线；箭头不自动意味着已被证明的历史因果。',STYLES['small']))
        story.append(PageBreak())
    return story


def main():
    global MATH_PYTHON
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=ROOT/'SURVEY.zh-CN.md')
    parser.add_argument('--output',type=Path,default=ROOT/'output/pdf/scaling-law-survey.zh-CN.pdf')
    parser.add_argument('--diagram',type=Path,default=ROOT/'figures/evolution-map.png')
    parser.add_argument('--edition',default=None)
    parser.add_argument('--math-python',help='Existing Python executable with matplotlib; no installation is performed')
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    MATH_PYTHON = args.math_python
    text=args.input.read_text(encoding='utf-8')
    found=re.search(r'20\d{2}-\d{2}-\d{2}',text[:2500])
    edition=args.edition or (found.group() if found else date.today().isoformat())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    doc=SurveyDoc(str(args.output),edition=edition)
    story=cover(doc,edition,args.diagram)
    # The opening overview already has its own page after the contents.
    if args.diagram and args.diagram.exists():
        text = text.replace('![研究问题演化图](figures/evolution-map.png)\n', '', 1)
    story += parse_markdown(text,doc.width,args.input.parent)
    doc.multiBuild(story)
    print(f'Created {args.output} ({args.output.stat().st_size:,} bytes; font={FONT})')
    print(f'Display formulas: {FORMULA_STATS}; math_python={MATH_PYTHON or "unavailable"}')
    if args.check:
        from pypdf import PdfReader
        reader=PdfReader(args.output)
        links=sum(1 for page in reader.pages for a in page.get('/Annots',[]) if a.get_object().get('/Subtype')=='/Link')
        print(f'Pages={len(reader.pages)}; link_annotations={links}; top_level_outline_items={len(reader.outline)}')


if __name__=='__main__':
    main()
