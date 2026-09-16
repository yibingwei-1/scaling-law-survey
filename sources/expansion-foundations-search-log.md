# 扩展预训练、数据、架构分支：检索与证据审计

- 核验日期：2026-09-16；日期是本次访问日，不是文献发表日。
- 目的：补齐从经典损失预测到训练配方、数据混合、稀疏计算和实际服务成本的技术链；不是按名称填充条目。
- 去重基准：sources/foundations.json、frontier.json、extensions.json 中的 arXiv 标识及标题；新增 38 条不与这三库重复。社区链接不算额外技术论文。
- 访问方式：web 工具直接打开各论文 arXiv abs 页，核验标题、作者、首次提交与修订历史；再打开指定版本 HTML，以节标题和关键词定位相关正文。以下表格记录访问目标，不声称完成跨数据库系统检索。
- 阅读层级：A 为全文内核心方法、实验与限制的定向精读，未独立复现；B 为相关正文段落核查；C 为摘要/引言核验，只入库。没有把“HTML 可以打开”等同于“全文已逐页阅读”。
- 元数据日期依据 arXiv 首发/修订记录；无修订的 v1 用 null 表示 last_revised_date。作者数组可能仅首位 + et al.。Llama 3 的 v3 首位作者为 Aaron Grattafiori，不沿用早期版本的首位作者。
- 本次扩展文献首发年份覆盖 2019–2025；没有为了补“最新”而写入未经核验的 2026 条目。根任务提供的 Skaling: Chinchilla's Exponents Meet Kaplan's Coupling（2608.07222）尚未由本分支核验，未计数、未作正文证据。

## 检索路径与阅读记录

全部链接均为原始论文来源。新增内容已与原经典链整合为三章：[T1](../docs/01-predictability-budget.md)、[T2](../docs/02-data.md)、[T3](../docs/03-architecture-deployment.md)，不另保留重复的扩展长稿。

| ID | 主源元数据 | 所读版本 | 级别 | 重点正文 |
|---|---|---|---|---|
| brown2020gpt3 | [arXiv](https://arxiv.org/abs/2005.14165) | [v4](https://arxiv.org/html/2005.14165v4) | B | §2训练设置、§3任务结果相关段、§4污染分析 |
| rae2021gopher | [arXiv](https://arxiv.org/abs/2112.11446) | [v2](https://arxiv.org/html/2112.11446v2) | B | §4.3规模与任务分析及引言 |
| zhang2022opt | [arXiv](https://arxiv.org/abs/2205.01068) | [v4](https://arxiv.org/html/2205.01068v4) | B | §2.5训练日志及模型设置 |
| biderman2023pythia | [arXiv](https://arxiv.org/abs/2304.01373) | [v2](https://arxiv.org/html/2304.01373v2) | B | 引言、§2套件设计与检查点 |
| touvron2023llama | [arXiv](https://arxiv.org/abs/2302.13971) | [v1](https://arxiv.org/html/2302.13971v1) | B | 引言、训练设置和推理成本动机 |
| dubey2024llama3 | [arXiv](https://arxiv.org/abs/2407.21783) | [v3](https://arxiv.org/html/2407.21783v3) | A | §3.1–3.3，重点§3.2.1与系统设置 |
| groeneveld2024olmo | [arXiv](https://arxiv.org/abs/2402.00838) | [v4](https://arxiv.org/html/2402.00838v4) | B | 引言与§2开放组成 |
| chowdhery2022palm | [arXiv](https://arxiv.org/abs/2204.02311) | [v5](https://arxiv.org/html/2204.02311v5) | C | 摘要、引言 |
| yang2020tensor4 | [arXiv](https://arxiv.org/abs/2011.14522) | [v3](https://arxiv.org/html/2011.14522v3) | B | 摘要、引言及参数化动机；未精读证明 |
| yang2022tensor5 | [arXiv](https://arxiv.org/abs/2203.03466) | [v2](https://arxiv.org/html/2203.03466v2) | A | §1–7，重点Table 3、§6.1、§7.4、Appendix B |
| xie2023doremi | [arXiv](https://arxiv.org/abs/2305.10429) | [v4](https://arxiv.org/html/2305.10429v4) | A | §1–4、§6、Algorithm 1及实验配置 |
| liu2024regmix | [arXiv](https://arxiv.org/abs/2407.01492) | [v2](https://arxiv.org/html/2407.01492v2) | A | 引言、§3方法、§5实验和比较限制 |
| penedo2024fineweb | [arXiv](https://arxiv.org/abs/2406.17557) | [v2](https://arxiv.org/html/2406.17557v2) | A | §4.1–4.2、§6、数据构造与教育筛选实验 |
| allal2025smollm2 | [arXiv](https://arxiv.org/abs/2502.02737) | [v1](https://arxiv.org/html/2502.02737v1) | A | 引言、§3、§4.3–4.7 |
| soldaini2024dolma | [arXiv](https://arxiv.org/abs/2402.00159) | [v2](https://arxiv.org/html/2402.00159v2) | B | 引言与§5过滤、去重相关片段 |
| villalobos2022data | [arXiv](https://arxiv.org/abs/2211.04325) | [v2](https://arxiv.org/html/2211.04325v2) | A | §1–3，数据存量、需求预测及替代来源 |
| gadre2024overtraining | [arXiv](https://arxiv.org/abs/2403.08540) | [v2](https://arxiv.org/html/2403.08540v2) | A | §2–3、§6、实验范围与任务筛选 |
| hernandez2021transfer | [arXiv](https://arxiv.org/abs/2102.01293) | [v1](https://arxiv.org/html/2102.01293v1) | C | 摘要、元数据 |
| lee2021dedup | [arXiv](https://arxiv.org/abs/2107.06499) | [v2](https://arxiv.org/html/2107.06499v2) | B | 引言、方法概述与1.5B C4结果片段 |
| eldan2023tinystories | [arXiv](https://arxiv.org/abs/2305.07759) | [v2](https://arxiv.org/html/2305.07759v2) | C | 摘要、引言 |
| xie2023dsir | [arXiv](https://arxiv.org/abs/2302.03169) | [v3](https://arxiv.org/html/2302.03169v3) | B | 引言、§4–5实验与效率；方法公式未完整复算 |
| fedus2021switch | [arXiv](https://arxiv.org/abs/2101.03961) | [v3](https://arxiv.org/html/2101.03961v3) | A | §2.1–2.4及Table 1–2 |
| lepikhin2020gshard | [arXiv](https://arxiv.org/abs/2006.16668) | [v1](https://arxiv.org/html/2006.16668v1) | B | §1动机、系统设计概述及实验范围 |
| jiang2024mixtral | [arXiv](https://arxiv.org/abs/2401.04088) | [v1](https://arxiv.org/html/2401.04088v1) | B | §2架构、性能分析、§3部署成本说明 |
| dai2024deepseekmoe | [arXiv](https://arxiv.org/abs/2401.06066) | [v1](https://arxiv.org/html/2401.06066v1) | A | §2–4方法、负载平衡、验证设置与§5规模扩展 |
| deepseek2024v2 | [arXiv](https://arxiv.org/abs/2405.04434) | [v5](https://arxiv.org/html/2405.04434v5) | A | §2.1–2.2、§3.2.3及相关消融表 |
| deepseek2024v3 | [arXiv](https://arxiv.org/abs/2412.19437) | [v2](https://arxiv.org/html/2412.19437v2) | A | §1成本表、§2.1–2.2、§3系统概述 |
| dao2022flash | [arXiv](https://arxiv.org/abs/2205.14135) | [v2](https://arxiv.org/html/2205.14135v2) | A | §2–4、Algorithm 1、Theorem 1–2及限制；未复算全部证明 |
| dao2023flash2 | [arXiv](https://arxiv.org/abs/2307.08691) | [v1](https://arxiv.org/html/2307.08691v1) | A | §2–4，尤其§3.1算法与§3.2–3.3并行机制 |
| kwon2023paged | [arXiv](https://arxiv.org/abs/2309.06180) | [v1](https://arxiv.org/html/2309.06180v1) | B | §1–4问题、分页机制和共享设计 |
| pope2022inference | [arXiv](https://arxiv.org/abs/2211.05102) | [v1](https://arxiv.org/html/2211.05102v1) | B | §1–2分析动机及部署结果；未复算全部分片模型 |
| shazeer2019mqa | [arXiv](https://arxiv.org/abs/1911.02150) | [v1](https://arxiv.org/html/1911.02150v1) | B | §2–4、性能分析和等参数实验 |
| ainslie2023gqa | [arXiv](https://arxiv.org/abs/2305.13245) | [v3](https://arxiv.org/html/2305.13245v3) | B | §1–3方法、设置、转换实验 |
| rajbhandari2019zero | [arXiv](https://arxiv.org/abs/1910.02054) | [v3](https://arxiv.org/html/1910.02054v3) | B | §1与模型状态/残余状态内存分析、三阶段设计 |
| shoeybi2019megatron | [arXiv](https://arxiv.org/abs/1909.08053) | [v4](https://arxiv.org/html/1909.08053v4) | B | §1、§3模型并行与性能实验概述 |
| gu2023mamba | [arXiv](https://arxiv.org/abs/2312.00752) | [v2](https://arxiv.org/html/2312.00752v2) | B | §2–3、§4.2相关设置、§5限制 |
| xiong2023longcontext | [arXiv](https://arxiv.org/abs/2309.16039) | [v3](https://arxiv.org/html/2309.16039v3) | B | §2训练配置、§4消融相关片段 |
| abdin2024phi3 | [arXiv](https://arxiv.org/abs/2404.14219) | [v4](https://arxiv.org/html/2404.14219v4) | C | 摘要、元数据 |

## 支撑三条直接后继链的证据

1. **DoReMi → RegMix**：RegMix 引言直接讨论 DoReMi 与代理模型方案。DoReMi 精读 §3 的参考模型/超额损失/DRO、Algorithm 1 的截断与权重处理、§4 代理/目标模型及额外计算。RegMix 精读回归方法和比较设置；正文保留领域重归一化可能削弱 DoReMi 基线的限制。
2. **FlashAttention → FlashAttention-2**：后者明确以第一代为起点，指出线程占用、非矩阵 FLOPs 和共享内存访问限制。核查第一代 Algorithm 1、Theorem 1–2 的准确性、二次计算与 IO 条件；核查第二代 §3 的在线归一化调整、并行和工作分配。
3. **DeepSeekMoE → V2 → V3**：V2 §2.2 明确沿用细粒度/共享专家；V3 §2 明确沿用 MLA/DeepSeekMoE，并修改负载均衡。核查 MoE 公式、验证数据规模及主要消融，V2 低秩 KV 与 RoPE 解耦，V3 路由偏置、仍保留的序列级损失、正式训练成本与排除项。

## 发现并落实到正文的限制

- TP V 的 6.7B GPT 类实验有位置编码与精度差异；不把所有结果差异纯归因于 μP。宽度迁移与深度/正则化迁移的证据不同。
- Gadre 等人的 104 模型实验有明确参数、语料和 token multiplier 范围；下游聚合经过任务筛选，不支持任意单任务外推，也不含后训练。
- Llama 3 的能力映射纳入 Llama 2 锚点，其数据/tokenizer 不完全相同；不能写成仅同分布小模型的全面预测验证。
- RegMix 的 1M 是非 embedding 参数口径；搜索目标 Pile-CC 与通用下游质量不等价。
- FineWeb-Edu 在教育/学术指标上的收益伴随域覆盖变化；不将教育分数视为普适质量。
- SmolLM2 后期同时改混合、训练量和学习率，不能分配全部增益给单个数据源。中间检查点数据消融与从随机初始化代理不等价。
- Villalobos v2 的 2026–2032 是条件预测区间，不是 2026 年已经耗尽数据的观测。
- DeepSeekMoE 文中的 dense “upper bound”在本稿作为实验参照，未写成全局严格性能定理。
- V3 的 auxiliary-loss-free 仍搭配小的序列级辅助损失；约 5.576M 美元不包括前期研究与消融。
- Mixtral 激活参数不决定服务内存；内存按总参数与 KV 计算，路由影响实际利用率。
- Megatron 76% 是对单卡基准的 scaling efficiency，不是硬件峰值利用率。
- FlashAttention 内核、模型端到端与完整训练运行的加速倍数不同；精确注意力仍有二次算术工作。
- PagedAttention 减少 KV 分配碎片，MQA/GQA/MLA 改变 KV 表示；两层机制正交。
- Mamba 的百万序列结果涉及 DNA/音频，未泛化为百万 token 通用语言理解；固定状态也不能保证等同 attention 检索。
- Phi-3 v4 含后续版本内容；当前仅入库，不追溯为 v1 结果。PaLM、TinyStories、Transfer 也未用浅读证据支撑正文结论。

## 工件与计数

三章整合稿约 11,719 个中文字符（汉字计数，英文、公式与链接另计），其中新增内容约 8,500 字。这些数量是内容规模记录，不代表证据质量。38 条技术来源中 34 条进行了相关正文核查，4 条为摘要/引言级待精读记录。源库的 evidence_strength 与 narrative_use 明确区分两者。

复核包括 JSON 可解析、必填字段、arXiv 去重、文内本地链接存在、三章标题/字数；不新增镜像实现的测试，也未宣称运行论文实验。
