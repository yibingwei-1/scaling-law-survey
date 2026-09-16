# 评估与多模态分支：检索及核验日志

- 检索／核验日期：2026-09-16。
- 对应章节：[03-evaluation-multimodal.md](../docs/03-evaluation-multimodal.md)。
- 目的：补足loss预测、能力预测、评分函数、分段规律与多模态迁移之间的逻辑边界，选择少量能解释问题变化的原始工作。
- 方法：web搜索发现 → arXiv或官方论文页确认 → HTML正文定向阅读方法、结果和限制 → 保存版本与实际阅读章节。不是穷尽检索；不根据结果顺序推断重要性或社交热度。
- 结构化查询和记录：[extensions-search-log.json](extensions-search-log.json)；论文元数据：[extensions.json](extensions.json)。`full_text_targeted`表示阅读了所列正文章节，不表示逐字读完全部附录或复现实验。

## 查询批次

2026-09-16，批次一，建立经典测量与跨模态主线：

1. `site.arxiv.org Schaeffer 2023 Are Emergent Abilities Large Language Models Mirage`
2. `site.arxiv.org Broken Neural Scaling Laws Caballero 2022`
3. `site.arxiv.org Scaling Laws Autoregressive Generative Modeling Henighan 2020`
4. `site.arxiv.org Scaling Vision Transformers 2022 Zhai`

批次二，连接数据与寻找2026年新评估工作：

1. `site.arxiv.org/abs/ 2026 scaling laws downstream evaluation prediction benchmark loss`
2. `site.arxiv.org/abs/ 2026 multimodal scaling laws evaluation contamination`
3. `site.arxiv.org DataComp In search next generation multimodal datasets 2023`
4. `site.arxiv.org CLIP Learning Transferable Visual Models Natural Language Supervision`

批次三，补充当年范围：

1. `site.arxiv.org/abs/ "2026" "scaling" "benchmark" "prediction" language model`
2. `site.arxiv.org/abs/ "2026" "multimodal" "evaluation" "scaling"`

另按编辑要求直接访问[GPT-4技术报告](https://arxiv.org/html/2303.08774v6)，定向阅读§2–3，而不是把检索摘要当作预测实验的证据。

## 改变正文表述的核验点

| 主源 | 定向阅读与约束 |
|---|---|
| [GPT-4报告](https://arxiv.org/html/2303.08774v6) | loss预测和HumanEval预测分别拟合；后者有可估计性筛选、最难题排除及分桶偏差。§2明确限制技术披露。 |
| [Schaeffer等](https://arxiv.org/html/2304.15004v2) | 读数学模型、指标实验和讨论；作者没有主张真实涌现不可能。 |
| [BNSL](https://arxiv.org/html/2210.14891) | 读形状表达、外推及§6预测边界；对转折的预测需要接近转折的观测。HTML未显示版本号，摘要页当前版本是v17，元数据分别记录。 |
| [Henighan等](https://arxiv.org/html/2010.14701v2) | 读跨域实验、分类与多模态信息增益；不可把特定图像表示上的规律外推为所有VLM共同指数。 |
| [Scaling Vision Transformers](https://arxiv.org/html/2106.04560v2) | 读联合缩放和附录；分类错误率没有熵的解释。2021首次预印本、2022会议发表，日期分开记录。 |
| [CLIP](https://arxiv.org/html/2103.00020v1) | 读§2和§6；自然语言监督扩展与对比目标效率有直接方法论依据，但计数、细粒度和分布外限制仍存在。 |
| [DataComp](https://arxiv.org/html/2304.14108v5) | 读统一流程与下游相关性；ImageNet与均分相关，不代表与每一个单独任务一致。 |
| [Kearns 2026](https://arxiv.org/html/2602.15532v1) | 读构念效度、结论与限制；探索性、观察性的测量模型不能证明潜在能力的因果机制。 |
| [Sarridis等2026](https://arxiv.org/html/2607.28211v1) | 读194 checkpoint比较、部分控制因素的比较和限制；不能从OpenCLIP、少数群体基准推到所有生成式VLM。论文自报ACM Multimedia 2026接收，未另核会议录，按新近预印本证据处理。 |

本章没有把“问题上的接续”写成论文间未经核实的直接影响。GPT-4、Schaeffer与BNSL是互补的预测／测量视角，不声称三者构成单线历史。

## 暂未纳入的2026线索

[Scaling Native Multimodal Pre-Training From Scratch](https://arxiv.org/abs/2607.22043)只作为待阅读全文候选；[aerial MLLM mission-level evaluation](https://arxiv.org/abs/2607.22014)只读摘要且偏离本章简短主线；[2606.08231](https://arxiv.org/abs/2606.08231)是综述线索，不充当原始技术证据；[Seed2Scale](https://arxiv.org/abs/2603.08260)仅初筛。没有借这些材料补写未核验结论。

## 下次更新的触发条件

优先查证新增事前预测、原始实验复现、测量选择改变结论以及同预算干预结果。对2026两篇前沿材料，跟踪后续版本是否改变结论、公开评测资产及独立复现情况；不要因为检索时间更新而把已有材料改写成新的领域共识。
