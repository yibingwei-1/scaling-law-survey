# Scaling Law Survey · 问题驱动的技术演化综述

[**English**](README.md) | **简体中文**

**中文持续更新版 · 2026-09-16 · [GitHub 仓库](https://github.com/yibingwei-1/scaling-law-survey)**

Scaling law 的历史，是不断发现旧资源模型遗漏了什么、再重新求解最优分配的过程：从预测训练收益，到联合分配参数与数据，再到有效数据、稀疏架构、部署成本、后训练、推理时计算与能力测量。

每条主线按 **原始问题 → 核心洞见 → 方法机制 → 实验证据 → 剩余限制 → 后继分支** 展开。论文之间的连接区分直接回应、并行路线和综述归纳。

**[中文完整综述](SURVEY.zh-CN.md)** · **[中文 PDF](output/pdf/scaling-law-survey.zh-CN.pdf)** · [English survey](SURVEY.en.md) · [English PDF](output/pdf/scaling-law-survey.en.pdf) · [文献与版本索引](REFERENCES.md) · [研究对话地图](docs/research-map.md) · [正文覆盖统计](docs/evidence-map.md) · [BibTeX](references.bib)

![Scaling law 的问题演化图](figures/evolution-map.png)

图为问题关系的概念综合，不是实验曲线。

## 七条研究对话

| 章节 | 推动研究演化的问题 | 主要路径 |
|---|---|---|
| [1. 可预测性与预算](docs/01-predictability-budget.md) | 投入前怎样预测收益？为什么最优配比会改变？ | 学习曲线 → Kaplan → Chinchilla → 复核、超参数迁移与训练配方 |
| [2. 有效数据](docs/02-data.md) | 数据不够、价值不等、分布变化时如何继续扩展？ | 重复收益 → 去重筛选 → DoReMi / RegMix → 合成与信息保留 |
| [3. 架构与部署](docs/03-architecture-deployment.md) | 总参数和 FLOPs 为什么不能独立代表成本？ | 路由与 MoE → 内存/IO/缓存 → 长上下文 → 生命周期优化 |
| [4. 后训练与 RL](docs/04-posttraining.md) | 怎样把候选能力变成可靠策略，学习信号何时失效？ | 自训练 → 反馈与验证 → GRPO及后继 → 过优化、覆盖与课程 |
| [5. 推理时计算](docs/05-inference.md) | 多算一次应该用来延长、重采样、搜索还是检查？ | CoT与多样本 → 搜索与PRM → 难度自适应 → 蒸馏与隐式深度 |
| [6. 理论与能力评估](docs/06-theory-evaluation.md) | 幂律从何而来？loss 如何映射到可交付能力？ | 理论机制 → 特征学习 → 涌现/评分 → 外推、泛化与评测边界 |
| [7. 多模态与交互](docs/07-multimodal.md) | 改变模态和反馈方式后，应该沿哪些资源轴扩展？ | 视觉规模 → 图文监督与混合 → 扩散计算 → 机器人与环境覆盖 |

另有[导论](docs/introduction.md)、[社区雷达](docs/04-community-radar.md)和[跨分支综合](docs/conclusion.md)。各章保留公式的变量定义、比较口径、关键实验条件与开放问题；基础阅读与前沿结果分层处理。

## 参考范例的方法，怎样落实到本仓库

完整阅读了 [JonnesLin/post-training-survey](https://github.com/JonnesLin/post-training-survey/tree/main) 的中文前言、导论、七章、结论及 design/plan 文档，并核对其 468 条书目与正文 440 个唯一引用键。借鉴其问题演化图、分层展开和跨章联系；技术结论回到各自主源核验。[详细结构与生成方法拆解](docs/00-reference-method.md)。

新增[两方面分析：文献研究与仓库出版结构](docs/reference-repository-analysis.md)，核对参考的双语章节、Markdown 用途、LaTeX、引用、研究笔记及发行方式，并列出本仓库的重构目标。当前已提供完整中英文 Markdown 正文与 PDF，默认首页为英文；LaTeX 构建仍未实现。分析文档保留当时的结构审查与后续目标，不代表所有目标都已完成。

v0.1 只有45条主源、三篇压缩技术章，深度与覆盖不足。本次重构为七篇独立技术章，约3.7万正文汉字；文献库含161条去重主源，其中151条在技术章节实际引用。文献库规模、正文引用量和阅读深度分别报告。最新精确统计见[覆盖地图](docs/evidence-map.md)及[机器可读审计](data/citation-audit.json)；候选条目不冒充已精读论文。

## 社区发现与证据

X、YouTube、Reddit 目前有18条可回溯记录，包含作者发布、研究者讲座、工程复现与反驳讨论。指标有观测日期，缺失值保留为 `null`；索引快照不当作实时热榜。讨论帮助发现争议，论文、作者实验和报告支撑技术判断。[社区雷达](docs/04-community-radar.md)。

以 LLM 为主线，理论、视觉、扩散、机器人作为条件与边界的比较。检索截至2026-09-16，不宣称无遗漏；原始实验未由本综述独立重跑。每条文献记录阅读范围、版本和限制，2026年的代表性结果与成熟基础工作区别呈现。

## 持续维护

已启用每周一 09:00（America/Los_Angeles）的 Codex 维护任务，检索论文、作者 blog、technical report 与三类社区，核验后同步更新中英文问题链、文献、两种语言的 PDF 与本仓库。只有实质变化、失败或需要用户操作时通知。调度依赖本地任务运行环境，具体流程见[UPDATING.md](UPDATING.md)。

- [检索与写作方法](METHODOLOGY.md)
- [更新日志](CHANGELOG.md)与[发布状态](PUBLISHING.md)
- [逐条证据](sources/)与[维护状态](data/state.json)

```bash
python3 scripts/build_survey.py
python3 scripts/validate.py
# PDF: reportlab、Pillow、pypdf；matplotlib用于数学排版
python3 scripts/build_pdf.py --language zh --check
python3 scripts/build_pdf.py --language en --check
```

`docs/` 的中文源章节、`docs/en/` 的完整英文对应章节与 `sources/` 的核验记录是维护源；两种语言的完整综述、索引、正文覆盖审计与 PDF 由脚本构建。[翻译复核记录](data/translation-status.json)检测任一语言的变化，复核后才更新文件指纹。文中原论文、社区内容及参考仓库归原作者所有；本仓库只分发原创综合和链接，不分发第三方全文。
