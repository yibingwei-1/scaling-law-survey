# 后训练与推理扩展：检索与阅读记录

核验日期：2026-09-16。新增 40 篇原论文，补齐历史链而非按热度堆砌条目。原有2026前沿另见 frontier-search-log。本文正文的因果连接主要是问题层面的综合，不冒充逐篇直接影响史。

## 检索路径

第 1 批：

- `site:arxiv.org Training Verifiers to Solve Math Word Problems Cobbe`
- `site:arxiv.org STaR Self Taught Reasoner Bootstrapping Reasoning`
- `site:arxiv.org Solving math word problems process outcome based feedback Uesato`
- `site:arxiv.org Reinforced Self Training ReST Gulcehre`

第 2 批：

- `site:arxiv.org Beyond Human Data Scaling Self Training Problem Solving Large Language Models ReST`
- `site:arxiv.org Tree of Thoughts Deliberate Problem Solving`
- `site:arxiv.org Language Agent Tree Search Unifies Reasoning Acting Planning`
- `site:arxiv.org ReST MCTS process reward guided tree search`

第 3 批：

- `site:arxiv.org Math Shepherd Verify Reinforce LLMs Step by step`
- `site:arxiv.org Llemma Open Language Model Mathematics`
- `site:arxiv.org DeepSeekMath Pushing Limits Mathematical Reasoning Open Language Models`
- `site:arxiv.org MetaMath Bootstrap Mathematical Questions`

第 4 批：

- `site:arxiv.org DeepSeek Prover V1.5 Reinforcement Learning Monte Carlo Tree Search`
- `site:arxiv.org rStar Math Small LLMs Master Math Reasoning`
- `site:arxiv.org Mutual Reasoning Makes Smaller LLMs Stronger Problem Solvers rstar`
- `site:arxiv.org WizardMath Empowering Mathematical Reasoning Reinforced Evol Instruct`

第 5 批：

- `site:arxiv.org Tulu 3 Pushing Frontiers Open Language Model Post Training`
- `site:arxiv.org 2 OLMo 2 Furious`
- `site:arxiv.org Open Reasoner Zero Reinforcement Learning Scaling`
- `site:arxiv.org SimpleRL Zoo Investigating Taming Zero Reinforcement Learning Open Base Models`

第 6 批：

- `site:arxiv.org DAPO Open Source LLM Reinforcement Learning System Scale`
- `site:arxiv.org Understanding R1 Zero Like Training Critical Perspective Dr GRPO`
- `site:arxiv.org Group Sequence Policy Optimization`
- `site:arxiv.org VAPO Efficient Reliable Reinforcement Learning Advanced Reasoning Tasks`

第 7 批：

- `site:arxiv.org "Math-Shepherd"`
- `site:arxiv.org "2 OLMo 2 Furious"`
- `site:arxiv.org "Understanding R1-Zero-Like Training"`
- `site:arxiv.org "The Lessons of Developing Process Reward Models"`

第 8 批：

- `site:arxiv.org "Large Language Monkeys"`
- `site:arxiv.org "Scaling of Search and Learning"`
- `site:arxiv.org "Process Reward Models That Think"`
- `site:arxiv.org "LUFFY"`

第 9 批：

- `site:arxiv.org "Universal Transformers"`
- `site:arxiv.org "Quiet-STaR"`
- `site:arxiv.org "Training Large Language Models to Reason in a Continuous Latent Space"`
- `site:arxiv.org "Scaling up Test-Time Compute with Latent Reasoning"`

第 10 批：

- `site:arxiv.org "Stop Overthinking"`
- `site:arxiv.org "ThinkPrune"`
- `site:arxiv.org "Let's Think Dot by Dot"`
- `site:arxiv.org "Self-Rewarding Language Models"`

搜索命中仅作为发现线索；技术结论均回到 arXiv 元数据和原文相关章节核验。WizardMath、Scaling of Search and Learning 等查询未在本批形成新增条目，不能据此认定这些方向没有相关文献；已有来源重复项也不重复入库。未把评论、视频摘要或新闻当作方法证据。

## 阅读深度与版本

`full_text_targeted` 表示打开原文后定向阅读方法／目标及相关实验段落，不表示每篇全部附录与代码已被审阅。下表和 JSON 记录具体范围。版本号无法明确钉住时保留 null；初始日期按 arXiv 页面日历日期记录。OLMo 2 初始提交为 2024-12-31，Coconut 本次使用 2026-08-23 更新的 v4。

| 原文 | 读取版本 | 具体范围 |
|---|---|---|
| [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168) | v2 | §4：生成器与验证器训练、test@1/test@100及过拟合 |
| [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) | v2 | §3–5：算法、训练重置、rationalization及实验限制 |
| [Solving math word problems with process- and outcome-based feedback](https://arxiv.org/abs/2211.14275) | v1 | §2–4：数据、反馈来源、答案与trace错误指标 |
| [Reinforced Self-Training (ReST) for Language Modeling](https://arxiv.org/abs/2308.08998) | v2 | 引言与方法：Grow/Improve、过滤、机器翻译评价 |
| [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](https://arxiv.org/abs/2312.06585) | 未钉住，null | §3–5：EM目标、拒绝采样、PaLM2数学代码实验与限制 |
| [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) | v2 | §3：thought粒度、生成、评价、BFS/DFS；任务设置 |
| [Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models](https://arxiv.org/abs/2310.04406) | v3 | §4：selection/expansion/evaluation/simulation/backpropagation |
| [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://arxiv.org/abs/2406.03816) | v3 | §3：MCTS*、正确路径距离、过程价值及迭代训练 |
| [Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations](https://arxiv.org/abs/2312.08935) | v3 | §3.1–3.5：自动标签、PRM、重排与step-wise PPO |
| [Llemma: An Open Language Model For Mathematics](https://arxiv.org/abs/2310.10631) | 未钉住，null | §2：Proof-Pile-2构建、混合与训练规模 |
| [MetaMath: Bootstrap Your Own Mathematical Questions for Large Language Models](https://arxiv.org/abs/2309.12284) | v4 | §3：问题重构、前后向生成与过滤 |
| [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) | v3 | §2与§4：数据、持续预训练、GRPO目标与训练 |
| [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://arxiv.org/abs/2408.08152) | v1 | §2.3–3：RL、proof截断续写与MCTS/RMaxTS |
| [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solvers](https://arxiv.org/abs/2408.06195) | v1 | §3：动作空间、MCTS与mutual verification |
| [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://arxiv.org/abs/2501.04519) | v1 | §3：policy/PPM、数据生成及四轮自演化 |
| [Tulu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124) | 未钉住，null | §6.1–6.4：RLVR、奖励、数据与底座/奖励消融 |
| [2 OLMo 2 Furious](https://arxiv.org/abs/2501.00656) | v3 | §5：post-training、SFT、DPO与RLVR |
| [Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model](https://arxiv.org/abs/2503.24290) | 未钉住，null | §2–3：PPO设置、critic、数据规模消融 |
| [SimpleRL-Zoo: Investigating and Taming Zero Reinforcement Learning for Open Base Models in the Wild](https://arxiv.org/abs/2503.18892) | v3 | §2.1–2.4：十种底座、数据难度、模板与格式奖励 |
| [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476) | v2 | §3：四项核心设计与对应消融 |
| [Understanding R1-Zero-Like Training: A Critical Perspective](https://arxiv.org/abs/2503.20783) | v2 | §3：response-length及difficulty bias、Dr.GRPO |
| [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071) | v2 | §4–5：目标、MoE路由与稳定性实验 |
| [VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks](https://arxiv.org/abs/2504.05118) | v3 | §3–4：value pretraining、GAE与长度适配 |
| [DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning](https://arxiv.org/abs/2511.22570) | v1 | §2–3：verifier训练、meta-verification、generator及高预算评估 |
| [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) | v1 | §3及结果：SFT/RM/PPO流程、偏好比较与限制 |
| [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) | v3 | §4：RLHF目标、最优策略重参数化与DPO损失 |
| [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) | v3 | §2：IFT/EFT种子、judge提示与迭代DPO |
| [Universal Transformers](https://arxiv.org/abs/1807.03819) | v3 | §2：共享深度、逐位置递归与ACT |
| [Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking](https://arxiv.org/abs/2403.09629) | v2 | §3–4：parallel rationale、mixing head、REINFORCE及teacher forcing |
| [Training Large Language Models to Reason in a Continuous Latent Space](https://arxiv.org/abs/2412.06769) | v4 | v4 §3–5及附录C：课程、计算图、更大模型及限制 |
| [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](https://arxiv.org/abs/2502.05171) | v2 | §3–4：递归架构、深度分布、截断反传与训练稳定 |
| [Let's Think Dot by Dot: Hidden Computation in Transformer Language Models](https://arxiv.org/abs/2404.15758) | v1 | §3–4：2SUM/3SUM、34M模型、训练与测试条件 |
| [Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs](https://arxiv.org/abs/2412.21187) | v2 | §2–3：overthinking测量、正确轨迹与短链偏好 |
| [ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning](https://arxiv.org/abs/2504.01296) | v1 | §3：截断奖励、迭代裁剪与检查点选择 |
| [Learning to Reason under Off-Policy Guidance](https://arxiv.org/abs/2504.14945) | v5 | §3：mixed-policy GRPO及policy shaping |
| [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](https://arxiv.org/abs/2407.21787) | v3 | §3–4：coverage scaling、sample budget与选择饱和 |
| [How Do Large Language Monkeys Get Their Power (Laws)?](https://arxiv.org/abs/2502.17578) | v1 | §2–3：单题失败概率、混合积分与近零密度 |
| [Process Reward Models That Think](https://arxiv.org/abs/2504.16828) | 未钉住，null | §3及附录E：合成检查轨迹、训练、预算与评估样本 |
| [The Lessons of Developing Process Reward Models in Mathematical Reasoning](https://arxiv.org/abs/2501.07301) | v2 | §2–4：自动标签偏差、评价、共识过滤及ProcessBench |
| [CREAM: Consistency Regularized Self-Rewarding Language Models](https://arxiv.org/abs/2410.12735) | v5 | §3.2–3.3：一致性正则项与自奖励循环 |

## 可复查的结论边界

- 自训练用成功轨迹重加权已有分布；答案提示、教师和工具提供额外信息，不能归于纯自发发现。
- Math-Shepherd 的续写标签估计策略相关成功价值；PRM Lessons 检查的是这种标签与步骤真伪之间的错位，两者不可简单排成胜负。
- Dr.GRPO、DAPO 与 GSPO 更改目标的不同部分；本稿不把它们合成一个算法，也不把经验稳定写成普遍数学定理。
- pass@k 是候选覆盖；实际选择成功率和总成本需要另测。重复采样聚合幂律依赖问题成功概率分布。
- 思考压缩可能容许准确率下降；latent 计算也有真实前向与训练成本。
- 所有实验均为原文报告，本批没有独立复现。未知版本与未覆盖分支是透明缺口，不以猜测补齐。

完整查询及逐篇 URL、读取范围的机器可读记录见 [expansion-frontier-search-log.json](expansion-frontier-search-log.json)。

