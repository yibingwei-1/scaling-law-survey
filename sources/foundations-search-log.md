# 经典预训练、数据、架构与理论分支：检索与阅读日志

- 检索/核验日：2026-09-16。
- 执行方式：web 工具的公开网页检索，以及 arXiv 原始摘要页和全文 HTML；也尝试 Nature 正式论文页面。
- 检索性质：围绕预先选定的问题进行定向检索和引用追踪，不是穷尽性系统综述；没有记录可复现的数据库全集数量，也不使用 PRISMA 数量叙述。
- 纳入依据：能核验主源，能够解释关键问题转变、限制、反证或方法扩展；不按搜索排序推定影响力，不把社交媒体热度作为真实性证据。
- 日期口径：元数据 `year` 原则上为首次预印本年；若阅读的是后来版本，单独写明。`verification_date` 只代表本次打开核查，不代表搜尽当日全部文献。

## 检索式与纳入决定

| 查询或追踪入口 | 核验并纳入的主源 | 处理说明 |
|---|---|---|
| `Hestness 2017 Deep Learning Scaling is Predictable Empirically arxiv` | [1712.00409](https://arxiv.org/abs/1712.00409) | 核查方法与早期问题背景。 |
| `Kaplan 2020 Scaling Laws for Neural Language Models arxiv` | [2001.08361](https://arxiv.org/abs/2001.08361) | 核查参数口径、批量调整和最优分配指数。 |
| `Hoffmann 2022 Training Compute Optimal Large Language Models arxiv` | [2203.15556](https://arxiv.org/abs/2203.15556) | 核查三种方法、公式、实验对比和不足一epoch限制。 |
| `Revisiting Scaling Laws Language Models 2024 Kaplan Chinchilla learning rate warmup`；`Resolving Discrepancies in Compute-Optimal Scaling arxiv` | [2406.19146](https://arxiv.org/abs/2406.19146) | 直接复核历史分歧，避免仅用二手“Kaplan被推翻”的解释。 |
| `Chinchilla Scaling: A replication attempt` | [2404.10102](https://arxiv.org/abs/2404.10102) | 区分曲线趋势与具体拟合系数的可靠程度。 |
| `Scaling Data-Constrained Language Models arxiv` | [2305.16264](https://arxiv.org/abs/2305.16264) | 核查唯一token/重复token区分及重复收益的条件。 |
| `Scaling Laws data pruning Sorscher 2022 arxiv` | [2206.14486](https://arxiv.org/abs/2206.14486) | 阅读原始摘要及主文限制，避免将视觉剪枝外推为通用LLM指数改善。 |
| `site:arxiv.org DataComp-LM` | [2406.11794](https://arxiv.org/abs/2406.11794) | 作为受控数据研究框架，不冒充普遍幂律系数研究。 |
| `site:arxiv.org Data Mixture Scaling Laws 2024` | [2403.16952](https://arxiv.org/abs/2403.16952)、[2507.09404](https://arxiv.org/abs/2507.09404) | 前者摘要/引言级阅读；后者仅原始摘要，列待精读。 |
| `AI models collapse training nature 2024 accumulation data`；`site:arxiv.org The Curse of Recursion 2023` | [2305.17493](https://arxiv.org/abs/2305.17493) | Nature 页面未成功读取，使用明确标识版本的原始预印本；不声称正式版全文已读。 |
| `site:arxiv.org Accumulating Model Collapse 2024` | [2404.01413](https://arxiv.org/abs/2404.01413) | 对照替换与累积条件，并检查累积增加计算的限制。 |
| `Scaling Laws mixture expert Clark 2022 arxiv` | [2202.01169](https://arxiv.org/abs/2202.01169) | 核查活动/总参数以及固定130B token训练设置。 |
| 引用追踪 Fine-Grained MoE 对 Clark 的讨论 | [2402.07871](https://arxiv.org/abs/2402.07871) | 核查专家粒度、训练数据联合优化及路由开销。 |
| `Beyond Chinchilla-Optimal arxiv` | [2401.00448](https://arxiv.org/abs/2401.00448) | 核查生命周期目标、6ND/2ND近似及高token比例外推局限。 |
| `site:arxiv.org Explaining Neural Scaling Laws Bahri` | [2102.06701](https://arxiv.org/abs/2102.06701) | 机制分类与假设层面的阅读，未重算证明。 |
| `site:arxiv.org The Quantization Model of Neural Scaling` | [2303.13506](https://arxiv.org/abs/2303.13506) | 核查知识单元假设及作者自述限制。 |

## 全文访问与证据深度

所有已纳入条目的 URL、阅读层级和局限见 [foundations.json](foundations.json)。核心篇目的“全文 HTML”指进入原论文全文并阅读正文相关章节，不表示每个附录、证明、图像和实验日志都经独立复核。具体章节在 `reading_depth` 中记录。

本次访问到了 Hestness、Kaplan、Chinchilla、Porian、Muennighoff、Sardana、Sorscher、DCLM、Ye、Shumailov、Gerstgrasser、Clark、Fine-Grained MoE、Besiroglu、Bahri 与 Michaud 的原论文 HTML。Shukor 2025 仅核验原始摘要，保持待精读状态。

## 排除和暂缓

- 搜索返回的百科、聚合摘要、自动化论文解读和 Reddit 帖子未作为技术论断主证据。
- 检索中出现的 2026 年视觉扩展（如 *Abra: Scaling Diffusion Image Training*）不在本章定向范围，未据摘要加入经典语言预训练结论。
- 搜索曾返回一个二手页面，把 Beyond Chinchilla 的方向描述为高推理需求下应训练更大、更短；原论文恰好主张更小、更久。该二手解读被排除，这也是全文主源核验必要性的实际例子。
- 未核查社会平台实时热度；该项由综述的社区讨论部分单独记录，不能从本日志推定。

## 后续增量更新时的优先问题

1. 新模型/新配方是否改变最优指数，还是只改变截距？是否控制优化器与计算口径？
2. 数据混合规律的跨规模外推是否在未参与拟合的大模型上验证？
3. MoE 结果是否同时报告活动参数、总参数、训练token、路由开销和真实吞吐？
4. 合成数据结果是否说明原数据保留方式、生成与过滤预算、独立评测及尾部性能？
5. 生命周期优化是否计入新的 test-time compute 分配，且明确请求量假设？
