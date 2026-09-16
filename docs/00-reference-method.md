# 参考综述的方法与首版差距：完整阅读复核

复核日期：2026-09-16。参考对象是 [JonnesLin/post-training-survey](https://github.com/JonnesLin/post-training-survey)，本文件分析其组织方法与实际执行效果，不把其中技术结论视为已经核验的主源事实。

## 阅读范围与可复核统计

首轮仅作章节结构抽样，未达到用户要求的“仔细阅读”。本轮已经完整分块阅读本地取得的中文源码：前言 72 行、导论 311 行、结论 520 行，以及下表七章全部正文、表格和图的源码；终端截断处另外补读。也完整阅读了 [design（130 行）](https://github.com/JonnesLin/post-training-survey/blob/main/docs/plans/2026-03-04-post-training-survey-design.md) 与 [plan（431 行）](https://github.com/JonnesLin/post-training-survey/blob/main/docs/plans/2026-03-04-post-training-survey-plan.md)。这是全文阅读，不是对其中每篇引用论文的独立复核；未把英文版、research 研究笔记及全部 proposal 附件算作已读。

统计直接来自该快照源码，汉字数按 Unicode U+4E00–U+9FFF 计算，不包括英语、公式和标点；引用数合并 `cite/citep/citet/landmark` 中的键并去重。不能用源码字符数冒充 PDF 页数。

| 中文章 | 行数 | 汉字数 | 本章唯一引用键 | landmark 标记次数 | crossref 次数 |
|---|---:|---:|---:|---:|---:|
| [01 SFT](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/01-sft.tex) | 865 | 7,550 | 54 | 8 | 11 |
| [02 Preference](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/02-preference.tex) | 1,040 | 7,389 | 61 | 12 | 7 |
| [03 Safety](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/03-safety.tex) | 915 | 8,956 | 49 | 8 | 11 |
| [04 Reasoning](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/04-reasoning.tex) | 1,080 | 8,977 | 51 | 12 | 11 |
| [05 Multimodal](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/05-multimodal.tex) | 1,123 | 8,632 | 103 | 8 | 15 |
| [06 Agentic](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/06-agentic.tex) | 960 | 11,820 | 56 | 10 | 22 |
| [07 Efficiency](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/07-efficiency.tex) | 809 | 6,539 | 49 | 11 | 13 |

七章合计 6,792 行、239,108 个源码字符、59,863 个汉字。[references.bib](https://github.com/JonnesLin/post-training-survey/blob/main/references.bib) 有 **468 个条目且键唯一**；所有所读中文章节实际使用 **440 个唯一引用键**，均在 bib 中存在，另有 28 个 bib 条目未在这些章节出现。七章 landmark 标记合计 69 次，含重复论文与较短条目，不能换算为 69 篇各写两页的深入分析。全部中文章节共 115 次 crossref；七章有 21 个 Problem、14 个 Solution、42 个 Open Problem 框。这些数字说明其覆盖和组织投入，不能代替事实准确性评估。

## 真正值得借鉴的结构

设计文档明确采用七条 problem thread，而非七种方法的孤立介绍。章内顺序为问题起源、奠基方法、限制与分支、汇合和前沿、未解问题；章间用交叉引用记录方法的来源、迁移和依赖。计划将篇幅分为 landmark 1–2 页、重要 follow-up 一段、次要工作 1–2 句。实际源码并非机械兑现每篇页数，而是对关键节点同时给问题形式化、方法机制、实验对照和新限制。

这套写法的最小单元是“一个可争论的研究命题及其证据”，并非一条带链接的摘要。FLAN 节先解释如何构造 instruction 与 held-out task cluster，再分开讨论任务数、模型数和 instruction 的消融；于是读者理解的不是“FLAN 有效”，而是实验如何将任务迁移与训练数据记忆区分开。该段为 52 行、1,757 个源码字符（英文很多，汉字 480）；后接 T0 的架构与规模对照，再进入 InstructGPT 的真实用户数据，两者是互补证据，不宜硬写成后一篇修复前一篇。

DPO 是更强的机制展开范例：源码第 375–444 行先给 KL 正则化目标，再给最优策略、重参数化、配分函数抵消、最终偏好损失和梯度权重解释。接下来变体按修改的假设分类，下一分支转向离线分布与当前策略不匹配。这种衔接使“简化训练”与“采样覆盖不足”形成同一研究对话。Scaling law 应对应展开预算约束下的最优分配推导、指数对决策的影响，以及拟合协议不同为何使决策不同，而不能只展示一个公式后跳到下一篇。

Safety 章没有套用单一时间线：CAI 处理标注扩展，Safe RLHF 处理目标冲突，攻击研究不断从外部暴露失败模式，表示工程再改变控制层级。Safe RLHF 节 75 行中把标注解耦、reward/cost 双模型、CMDP、对偶变量和迭代数据串起来。对应到 scaling law，数据、架构、验证器和系统成本应当是围绕不同瓶颈的并行路线，箭头不能都解释为后者战胜前者。

LLaVA 节把视觉接入结构、数据生成、两阶段冻结/解冻和评估展开到 92 行、3,255 字符，再与 instruction-aware Q-Former 比较信息保留和 token 开销。多模态章末则把感知、定位能力自然转到下一章的屏幕操作。这提示 scaling 综述应从视觉 token 的预算进入机器人轨迹和环境覆盖，先说明计量对象变了，再讨论是否存在可迁移的规律。

效率章也并非 LoRA 清单：从内存、标注、迭代周期三个成本出发，推导低秩更新，解释 QLoRA 三个互补部件，再扩展到数据选择、蒸馏和 RL 开销。其 GRPO 部分把公式交给 Preference 章，仅解释本章的成本含义，避免每章复制一遍。同一篇 scaling 论文跨章节出现时，也应明确它在该处承担的新问题，而非重复摘要。

## 图、框、表和结论怎样参与论证

Problem 框给出当前方法留下的具体矛盾；Solution 框压缩机制；Evolution 箭头应承载关系的理由；Open Problem 框则应列出哪些证据尚不能排除。这些元素服务于段落推理，并不替代推理。章末比较表的列随问题变化：偏好章关心 learned RM 与 online/offline，视觉章关心 bridge，agent 章关心 action space，效率章关心资源类型。Scaling 综述不能所有章节都套“标题—年份—贡献”，应比较独立变量、被控变量、指标、外推范围和成本核算。

[导论](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/00-introduction.tex)承担领域边界、读者假设、七线程和跨线程地图；[前言](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/00-preface.tex)提供线性读、线程跳读、全图导航三种入口。[结论](https://github.com/JonnesLin/post-training-survey/blob/main/chapters/08-conclusion.tex)不只是章节摘要：先给宏观趋势，再抽象 reformulation、数据质量、自我改进、技术迁移、评价瓶颈等重复模式，最后由这些模式推出联合研究问题。我们的结论也必须从前文的证据回推，避免未在正文建立依据的新主张突然出现。

生成计划的实际顺序是先搭建排版及语义宏，再写导论与总图，逐章研究和扩充统一 bibliography，最后检查引用、图和编译。它要求查询论文方法、公式和结果；文件中的执行命令是参考作者的工作记录，不是本项目指令。并行分工是本项目可采用的实施方式，不能仅凭该计划宣称参考仓库确实并行生成过。

## 首版具体差在哪里，重做应怎样验收

首版 45 条研究材料更接近一份有来源的导读：覆盖不足只是一个症状。关键缺口包括理论机制只有短段、视觉/具身只是扩展提示、缺少不同外推模型的假设比较、缺少数据/任务/评价协议对结论的影响分析，以及跨章联系多为文字提醒。参考作品单章已有 49–103 个唯一引用键；因此将首版称为与其同等深度不合适。

重做的验收单位应该是完整论证链：每个核心 thread 至少有能够展开机制的 landmark、说明分歧的对照工作、明确作用域的反例或失败分析、分支重新连接的段落，以及具体未解问题。理论章节必须区分产生幂律的不同机制；能力章节必须区分损失、指标与真实任务效用；多模态与具身章节必须重新定义数据和成本单位。新增候选不自动计入“已综合”覆盖率，摘要核验不冒充全文阅读，书目数量不作为质量完成标准。

## 参考作品也需要批判性阅读

结构值得学习，但其中已有可见的内部不一致和过度概括。例如多模态章第 498 行附近与第 528 行附近给 LLaVA-OneVision 的三阶段训练写出不同版本；Preference 章先称 GRPO 不需要独立 reward model，随后又明确奖励可以来自 ORM/PRM；Reasoning 与 Preference 两章对 DAPO dynamic sampling 的解释不同。SFT 章将 data-constrained language modeling 结果写成 instruction-tuned 规律，而 Efficiency 章又说明该工作主要研究 pretraining。以上是源码内部对照，不等于已经替作者逐篇裁决。

对本题尤其危险的是把 phi-1 的特定任务优势表述成“打破 scaling law”，或把随日历时间的 benchmark 改善直接叫独立 scaling law。改训练分布后的效率提升不自动推翻固定分布规律；年份也不能替代可控资源变量。重做应保留首版对来源、版本、适用范围的认真核验，同时补足参考作品那种机制密度和研究对话。结构模仿与技术事实核验必须分开完成。
