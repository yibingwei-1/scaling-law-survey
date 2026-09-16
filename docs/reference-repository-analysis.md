# 参考仓库的两层设计：文献研究与双语学术出版

核验日期：2026-09-16。参考仓库为 [JonnesLin/post-training-survey](https://github.com/JonnesLin/post-training-survey)。本次通过 GitHub API 核对当前 `main` 为 [e00571cb](https://github.com/JonnesLin/post-training-survey/commit/e00571cb25ac11f29867766a35bcb8ee6e806050)，提交日期 2026-04-02；本地阅读快照的全部56个文件逐一与远端 Git blob 哈希一致。目录包含30个 `.tex`、19个 `.md`、5个 `.bib`、`CITATION.cff` 和 `.gitignore`。这里分析的是仓库设计及其可见实现，没有重新裁决其中全部论文结论，也没有在本轮编译它的 LaTeX。

**这份参考应从两个方面学习：研究内容如何形成，以及研究成果如何维护、阅读和引用。** 前者决定综述有没有解释力，后者决定解释能否以可靠、可复用的形式交付。此前 scaling-law 仓库主要补充了中文内容，没有完整实现第二方面；中文 PDF 和一个 BibTeX 导出文件不足以满足双语 LaTeX 出版要求。

> 后续实施状态（v0.3）：已完成默认英文首页、中文首页、完整中英文 Markdown 与 PDF，以及翻译同步校验。下文的差距对照保留原审查时点；LaTeX 出版等其余目标仍未全部实现。

## 1. 内容组织：从材料集合到研究对话

参考的[设计文档](https://github.com/JonnesLin/post-training-survey/blob/main/docs/plans/2026-03-04-post-training-survey-design.md)最初把目标定位为支持博士研究的个人综述。当前导论进一步面向研究者、研究生和从业者。由这些明确目标，以及仓库中的 gap analysis 与 proposals，可以看出它希望兼顾系统学习、技术理解与研究选题；“支持选题”是对这些材料用途的归纳，不表示其中方案已经通过实验。

### 1.1 先确定问题线，再让文献进入合适的位置

七条 thread 各自对应一个持续存在的问题，例如如何表达偏好、如何提供可靠推理反馈、如何使方法的成本可接受。论文是回答这些问题的节点；时间顺序帮助解释演化，但不是唯一的分类依据。

这种划分的作用是稳定章节边界。某个新算法出现时，编辑先判断它改变了哪一个问题的解法、假设或证据，再决定放到哪里。读者也能以问题进入，而不必先知道算法名字。对应到 scaling law，章节应该围绕收益预测、资源分配、有效数据、实际成本、反馈、推理和能力测量展开。

### 1.2 研究笔记是候选和编辑判断的中间层

[`research/thread2-preference.md`](https://github.com/JonnesLin/post-training-survey/blob/main/research/thread2-preference.md)先按子问题整理论文，再记录标题、作者、年份、标识和重要性。它本身是一份候选清单，不等于完成了逐篇方法审查。

更深入的 [`thread5-multimodal-deep-research.md`](https://github.com/JonnesLin/post-training-survey/blob/main/research/thread5-multimodal-deep-research.md)进一步写出应补充哪个小节、什么证据改变了已有认识、哪些方向优先整合。其价值在于把“找到新论文”转换为“这篇论文要求我们改哪一段论证”。部分建议尚未进入正式章节，不能把研究笔记中的计划当作已完成正文。

因此，我们需要保留三个不同状态：发现候选、核验与阅读、进入正文综合。X、YouTube、Reddit 可以补充第一步；后续技术判断仍要回到论文、作者实验和报告。

### 1.3 深度分配围绕研究转折

设计给关键转折论文更大篇幅，重要跟进集中解释改动，次要工作简短定位。目的不是平均介绍每篇论文，而是把读者的注意力投入最能解释研究分叉的位置。

以[偏好章 DPO 部分](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/02-preference.tex)为例，正文连接优化目标、策略表达、重参数化、损失和梯度，再讨论变体与离线分布问题。它回答了方法为什么有效、依赖什么条件，以及下一类工作为什么需要出现。scaling law 的相应要求是展开最优预算推导、资源定义、实验设计和外推边界，而不是只列一个幂律公式。

### 1.4 章内是演化链，章间是关系图

每章从起点和基础方法进入限制、分支、阶段性汇合与开放问题。跨章引用则解释一种思想在其他场景承担了什么新角色：例如偏好建模与推理验证共享评分思想，但目标与正确性条件不同。

这种结构支持两种阅读：连续读懂一条问题线，或者沿引用跳到所需背景。它也减少了同一方法在多章重复推导。对我们的综述，每条跨章关系应标明是直接回应、方法迁移、共同瓶颈还是编辑归纳；不能把相邻年代自动写成因果关系。

### 1.5 补文献依靠缺口分析，不能只依靠热度

[`research/related-work-gap-analysis.md`](https://github.com/JonnesLin/post-training-survey/blob/main/research/related-work-gap-analysis.md)从关键论文的 Related Work 返回更早的来源，并与现有覆盖对照，标记已覆盖和遗漏节点。它使补充工作针对前驱、分支和反证，而不仅追逐最近发布的材料。

这一方法特别适合修补 scaling law 中“直接从 Kaplan 跳到 Chinchilla”、忽略学习曲线理论或训练协议复核的问题。社区讨论能够发现新的争议，引用追踪则帮助恢复争议的研究背景。

### 1.6 结论将章节压缩为研究判断，再发展成选题

[结论](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/08-conclusion.tex)重新整理跨方向的变化与反复出现的限制。仓库另有 [proposal 笔记](https://github.com/JonnesLin/post-training-survey/blob/main/research/vlm-first-principles-project-proposals.md)和独立 LaTeX proposal，把其中问题进一步展开为假设、方案、最小实验和风险。

这样，综述的用途从“了解过去”延伸到“选择下一步实验”。但 proposal 是待检验的研究设想，应与综述中已经建立的证据分开呈现。

### 1.7 内容审阅与引用审阅分开保存

[`docs/full-review-report.md`](https://github.com/JonnesLin/post-training-survey/blob/main/docs/full-review-report.md)讨论定位、结构、可读性、交叉引用和编译问题；[`citation-verification-report.md`](https://github.com/JonnesLin/post-training-survey/blob/main/docs/citation-verification-report.md)集中讨论书目准确性。它们服务不同质量目标：论证是否成立，与来源是否存在、元数据是否正确，不能互相替代。

这些文件是带日期的历史记录，不应把其中旧的缺陷数量或自评分当作当前仓库的独立审计结论。参考的价值是把研究和审阅过程保留下来，而不是仅展示一份看似完成的 PDF。

## 2. 仓库组织：各层分别服务什么目标

下面为实际结构的功能摘要，不把所有文件展开：

```text
post-training-survey/
├── README.md / README-zh.md          英文、中文门户
├── main.tex / main-en.tex            两种语言的装配与编译入口
├── preamble.tex / preamble-en.tex    语言设置、版式、语义宏
├── chapters/ / chapters-en/          完整双语 LaTeX 章节
├── references.bib                    两种语言共用的正式书目
├── bib_parts/                        部分书目分片
├── figures/overview.tex              可编辑 TikZ 演化图
├── research/                        候选材料、深研、缺口与选题笔记
├── docs/                            设计、计划、审阅及独立研究提案
├── CITATION.cff                      别人如何引用这份综述
└── .gitignore                       排除编译中间文件和下载论文
```

### 2.1 双语 README 是读者门户

[英文首页](https://github.com/JonnesLin/post-training-survey/blob/main/README.md)和[中文首页](https://github.com/JonnesLin/post-training-survey/blob/main/README-zh.md)互相链接，解释选题、七条问题线、主要特色、目录、构建和引用方法。读者进入首页即可判断内容是否相关、从哪里读、如何取得学术排版版本。

README 的目标是降低进入成本，不承担全篇正文。只翻译 README，也不能构成双语综述。

### 2.2 双语章节与双语入口分开

`chapters/` 和 `chapters-en/` 分别保存完整中英内容；`main.tex` 与 `main-en.tex` 指定语言设置、章节顺序、目录和书目。共同章节结构便于逐章对应和审阅，独立入口允许中文字体与英文页面布局分别设置。

这说明“中英文版”的单位是整篇文稿，包括图注、表格、开放问题和引用，而不仅是标题或摘要。两种语言共用书目能避免同一论文出现两套元数据，但它本身不能保证两份正文语义一致。

### 2.3 preamble 把内容角色变成统一呈现

参考[导言区](https://github.com/JonnesLin/post-training-survey/blob/main/preamble.tex)定义线程颜色、跨章引用、关键论文、演化关系和四类信息框。尤其演化宏有“起点、终点、原因”三个参数：它表达的关系比一根没有解释的箭头更明确。

这层设计有两个作用。对作者，固定语义角色使章节写法更一致；对读者，统一颜色、框和链接让长文可以扫描和跳读。改变版式也只需集中修改。宏提供表达规范，并不会自动验证逻辑或证据。

### 2.4 图是维护中的研究地图

[`figures/overview.tex`](https://github.com/JonnesLin/post-training-survey/blob/main/figures/overview.tex)使用共同时间轴、问题线、关键节点和跨线连接。TikZ 源码可随研究更新修改并重建，也适合与论文版式一起生成。

它服务全局定位、跨章理解与长期维护。静态概念图片可以辅助阅读，但不能替代可维护的节点、年份、关系与图注。我们还应区分实证关系与编辑归纳，避免图比正文作出更强的主张。

### 2.5 Citation 实际包含三个不同功能

| 功能 | 参考如何实现 | 服务的目标 |
|---|---|---|
| 本综述引用原论文 | 正文引用键加共享 `references.bib`，由 BibTeX/natbib 排版 | 把论断连接到来源，统一作者、年份和出版信息 |
| 本综述内部互相定位 | section label、crossref、hyperref/cleveref | 在论证、公式、图和背景章节之间导航 |
| 别人引用本综述 | `CITATION.cff` 和 README 的引用示例 | 将仓库成果变成可明确归属和引用的研究产物 |

[英文导言区](https://github.com/JonnesLin/post-training-survey/blob/main/preamble-en.tex)还启用了书目到正文引用页的反向链接，便于从一篇论文回查它在哪些论证中使用。`CITATION.cff` 则是另一条链：GitHub 可据它显示 “Cite this repository”，并提供引用格式；它不负责管理正文的几百篇参考文献。[GitHub 官方说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)。

### 2.6 研究过程与正式文稿分层

`research/` 保存尚在生长的材料与判断；章节保存经过选择、组织的论证；`docs/` 保存设计、审阅和延伸产物。读者不需要先理解研究者的全部工作记录，维护者又能回溯一个结论怎样形成。

当前参考的 `docs/` 仍混有不同类型文件，不能视为唯一正确的目录划分。应借鉴的是职责分离；我们可以进一步将审阅、设计和 proposal 分目录保存。当前 scaling-law PDF 收入了参考方法拆解，也宜在重构时区分正文读者与编辑维护者的需要。

### 2.7 编译和发布使源稿成为学术交付物

README 给出 XeLaTeX、BibTeX 和 latexmk 构建方式；两种语言分别编译。版本库主要保存源文件，`.gitignore` 排除了 PDF 和编译中间文件。

本轮核验 [v1.0 Release](https://github.com/JonnesLin/post-training-survey/releases/tag/v1.0)只有 `arxiv-submission.tar.gz` 附件。展开列表显示它包含英文主入口、英文章节、导言区、共享书目和图，没有双语 PDF。由此可以确认参考偏向可编译源码与投稿交付，不能说它已经提供所有形式的即点即读下载。归档存在也不等于投稿已被接受。

## 3. 必须分清参考已有的能力与我们要补的能力

| 能力 | 参考仓库的当前事实 | 对 scaling-law 的要求 |
|---|---|---|
| 双语首页 | 已有 | 补齐并提供语言切换与格式入口 |
| 双语完整正文 | 已有两套 LaTeX 章节 | 补齐英文，连同公式解释、表图和边界一起审校 |
| 完整双语 Markdown | 未发现；现有 Markdown 为门户、笔记、报告等 | 作为用户新增要求实现两种语言的网页阅读版 |
| LaTeX | 已有入口、章节、宏、引用和图源码 | 提供实际可编译文稿，而非只有 PDF |
| 双语自动同步 | 未发现自动机制 | 用稳定章节 ID、版本关联和审校状态追踪 |
| CI | 当前树没有 `.github/workflows` | 扩展我们的现有 CI，验证双语、引用和构建 |
| 正式发行 | 有 v1.0 英文投稿源包；无 PDF 附件 | 同一版本发布两语 Markdown、PDF、LaTeX 源包 |

参考也有值得避免的维护缺口。例如，中文前言文件存在，但中文 `main.tex` 没有引入；英文入口引入了前言。两语共用的 overview 文件含中文图注，而英文导言区未声明中文支持。后者存在英文呈现与字体覆盖风险，本轮没有编译，故不将其写为已观察到的渲染故障。

`bib_parts/` 四份分片合计241个引用键，均是主库468键的子集；当前编译入口直接读取主库，未发现自动合并分片的脚本。因此不能把分片误认成已经实现的完整书目生成流程。

## 4. 我们当前的差距

当前仓库已有中文 Markdown 正文、来源核验、阅读深度、社区线索、构建脚本和基础 CI。这些可保留。差距主要在完整出版链，而不只是文件夹名称：

- **语言**：没有英文完整正文和双语门户，尚不能向英文读者交付同一篇综述。
- **LaTeX**：现有 PDF 通过 ReportLab 生成，没有可编译 `.tex` 主稿；行内数学还使用简化记号。PDF 可读不等于 LaTeX 可复用。
- **引用**：现有正文使用 URL 链接，`references.bib` 是导出附件，没有作为正文引用的统一驱动。部分作者和出版信息仍待补齐。
- **分层**：`docs/` 同时承载正文、方法拆解和核验日志，正式内容与维护材料的边界不够明确。
- **导航与图**：已有章节链接、Mermaid 地图和概念图，但没有贯穿全部语言与格式的稳定 section ID、语义框和统一图源。
- **质量与版本**：当前 CI 检查元数据、本地链接和生成物一致性，未检查双语同步、LaTeX 编译与正式 citation。每周更新也需在新架构落地后覆盖这些环节。

## 5. 建议的目标架构：沿用参考呈现，明确维护来源

下列是**建议的重构目标，尚未实施**。它保留参考易于辨认的双语入口、双语章节、书目、图、研究笔记和学术构建，同时增加用户要求的完整双语 Markdown。

```text
scaling-law-survey/
├── README.md / README-zh.md         英文、中文门户
├── CITATION.cff                    引用本综述
├── content/
│   ├── zh-CN/                      中文章节维护源
│   ├── en/                         经审校的英文对应源
│   ├── manifest.yml                章节顺序与稳定 ID
│   └── translation-status.json     对应版本、待同步与审校状态
├── main.tex / main-en.tex          生成的可编译入口
├── chapters/ / chapters-en/        生成的双语 LaTeX 章节
├── preamble.tex / preamble-en.tex  维护的语言设置与语义宏
├── references.bib                  由统一书目生成，两语共用
├── sources/                        书目事实、阅读与主张证据、社区记录
├── research/                       缺口分析、线程研究与选题笔记
├── figures/                        可编辑图源和网页/PDF导出
├── docs/                           方法、审阅、贡献与构建说明
├── SURVEY.zh-CN.md / SURVEY.en.md  生成的完整 GitHub 阅读版
├── output/pdf/                     双语 PDF
├── scripts/                        多格式构建和一致性验证
└── .github/workflows/              校验与版本发布
```

推荐保留 Markdown 作为每种语言的维护源，再生成 LaTeX、PDF 与适合 GitHub 的 Markdown。理由是现有正文和持续更新以 Markdown 为基础，新增文献和审阅差异更方便；同时生成的 `main.tex`、章节、图和书目必须组成完整可编译工程。若采用 LaTeX 主稿，精细排版更直接，但回到 GitHub Markdown 时需要额外处理复杂宏；无论选哪种，都不应该手工维护四份彼此独立的正文。

转换并非一个命令就能保证正确。问题框、演化关系、跨章链接、引用和 TikZ 图需要明确的导出规则与验证。Pandoc 支持这些格式及过滤器，但官方也明确说明复杂格式之间可能丢失信息；实现时应先验证一个包含公式、表格、框、引用和图的完整样例。[Pandoc 官方说明](https://pandoc.org/MANUAL.html#description)。

内容结构与发布结构应通过同一组稳定标识连接：一篇论文有一个引用键，一节论证有一个 section ID；中英文共享它们，不必共享完全相同的句子。中文更新后，关联的英文版本标成待同步。结构、数值、公式和引用可以自动核对，语义等价仍需审校。

完整流程应为：发现材料 → 核验与研究笔记 → 改写问题链 → 审校英文 → 校验共用引用与章节映射 → 生成两语三种格式 → 以同一版本发布。每周维护不再仅追加条目，而要说明改变了哪项判断、影响哪些章节，以及英文与各格式是否已同步。

## 6. 后续重构的验收标准

1. 英文与中文首页各自能直接进入本语言的完整 Markdown、PDF 和 LaTeX 源码。
2. 两语覆盖相同的实质章节与证据边界；摘要不能代替英文正文，翻译滞后必须可见。
3. 一份正式书目驱动两语、各格式的引用；引用键、section ID、图表引用均能解析。
4. 从干净环境可构建两语 PDF，保留正确数学、图表和导航；源码下载后能够独立编译。
5. 研究笔记、核验记录和 proposal 不冒充已经进入正文的结论；读者入口与编辑材料分开。
6. 一次实质更新只修改权威源，再生成交付物；CI 能识别未同步语言、缺失引用、损坏链接和过期生成物。
7. 保留原有来源审计与更新历史，迁移旧链接，确保持续维护任务使用新的路径与发布规则。

本次完成的是两方面的证据分析与架构建议；英文正文、LaTeX 构建和新目录迁移不在此被标记为已完成。
