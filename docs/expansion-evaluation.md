# T6／T7 扩展文献核验与阅读日志

观测日期：2026-09-16。目标是补齐理论机制、能力测量、视觉多模态、扩散与机器人分支，而非把文献数量当作完成度。

## 本轮完成范围

- 新增 37 条主源书目；以原始 arXiv 摘要页核对标题、全部作者、首次提交日期及版本历史，按实际读取版本保存链接。年份使用首次公开提交年份，会议年份在正文需要时另注。
- 6 篇读完 PDF 提取的全部正文及附录文字、表格与图注；跳过参考文献列表，不声称逐张审查全部图像、逐行验证证明或复现实验。
- 5 篇进行正文定向阅读；其中 feature-learning 一文已读全部主文，证明附录未逐项阅读。具体章节逐条保存在 JSON。
- 26 篇只完成摘要及书目核验，保留为候选；正文中偶有用于定位历史或后续问题的简短提及，不把它们计入精读或完整综合完成量。
- 已综合 11 篇、候选 26 篇；这一状态描述本轮新增研究深度，并不表示被引用的候选已经通过全部机制、消融或统计审查。

本轮正文分为 [T6 理论与能力评估](06-theory-evaluation.md) 和 [T7 视觉、多模态、扩散与机器人](07-multimodal.md)。吸收了旧评估多模态章与旧预训练篇理论节，原文件保留；既有来源的阅读深度沿用 foundations.json／extensions.json，未冒充本轮重新通读。

## 检索及选择过程

本轮以此前主线暴露的缺口为入口，搜索主题包括：neural scaling law learning curve theory、kernel spectrum、feature learning、observational scaling、emergence loss perspective、downstream task scaling、mixed-modal scaling、diffusion inference-time scaling、robot imitation data scaling。先用网页检索发现候选，再回到 arXiv 作者提交页与论文 PDF；不使用转载、新闻或社区热度来支持技术结论。

对照当前 sources/foundations.json、frontier.json 和 extensions.json，排除了已有 Bahri、Michaud、GPT-4、Schaeffer、BNSL、Henighan、Scaling ViT、CLIP 与 DataComp 等条目的重复计数。新增条目的摘要页于本轮批量读取，核心 PDF 使用固定版本；临时下载与提取文本留在 tmp/research/evaluation，不属于可发布的论文再分发材料。

优先全文阅读的标准是它是否能改变章节中的问题链：长尾机制；loss 对能力的代理边界；多模态干扰；推理搜索的评价器限制；机器人采集与闭环泛化。其他工作保留为明确候选，而不因有 DOI、arXiv ID 或摘要就升级为深度综述证据。

此次补充不声称系统综述意义上的穷尽检索，没有双人独立筛选、完整数据库覆盖或统一质量评分。2026 新稿尤其保留探索性状态。曾尝试补取六篇视觉／机器人候选全文，工具等待被中止；没有因此提高任何条目的阅读深度。

## 已核验条目

| 主源 | 首发年份／读取版本 | 分支 | 本轮状态 |
|---|---|---|---|
| [A Constructive Prediction of the Generalization Error Across Scales](https://arxiv.org/abs/1909.12673v2) | 2019／v2 | T6 | 仅摘要；候选 |
| [Deep Double Descent: Where Bigger Models and More Data Hurt](https://arxiv.org/abs/1912.02292v1) | 2019／v1 | T6 | 仅摘要；候选 |
| [Spectrum Dependent Learning Curves in Kernel Regression and Wide Neural Networks](https://arxiv.org/abs/2002.02561v7) | 2020／v7 | T6 | 仅摘要；候选 |
| [A Neural Scaling Law from the Dimension of the Data Manifold](https://arxiv.org/abs/2004.10802v1) | 2020／v1 | T6 | 仅摘要；候选 |
| [Learning Curve Theory](https://arxiv.org/abs/2102.04074v1) | 2021／v1 | T6 | 全文文字与附录；已综合 |
| [Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models](https://arxiv.org/abs/2206.04615v3) | 2022／v3 | T6 | 仅摘要；候选 |
| [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682v2) | 2022／v2 | T6 | 仅摘要；候选 |
| [Revisiting Neural Scaling Laws in Language and Vision](https://arxiv.org/abs/2209.06640v2) | 2022／v2 | T6 | 正文定向；已综合 |
| [A Solvable Model of Neural Scaling Laws](https://arxiv.org/abs/2210.16859v1) | 2022／v1 | T6 | 仅摘要；候选 |
| [Inverse scaling can become U-shaped](https://arxiv.org/abs/2211.02011v5) | 2022／v5 | T6 | 仅摘要；候选 |
| [Inverse Scaling: When Bigger Isn't Better](https://arxiv.org/abs/2306.09479v2) | 2023／v2 | T6 | 仅摘要；候选 |
| [How predictable is language model benchmark performance?](https://arxiv.org/abs/2401.04757v1) | 2024／v1 | T6 | 仅摘要；候选 |
| [A Dynamical Model of Neural Scaling Laws](https://arxiv.org/abs/2402.01092v4) | 2024／v4 | T6 | 正文定向；已综合 |
| [Scaling Laws for Downstream Task Performance of Large Language Models](https://arxiv.org/abs/2402.04177v3) | 2024／v3 | T6 | 全文文字与附录；已综合 |
| [Understanding Emergent Abilities of Language Models from the Loss Perspective](https://arxiv.org/abs/2403.15796v3) | 2024／v3 | T6 | 全文文字与附录；已综合 |
| [Observational Scaling Laws and the Predictability of Language Model Performance](https://arxiv.org/abs/2405.10938v3) | 2024／v3 | T6 | 正文定向；已综合 |
| [How Feature Learning Can Improve Neural Scaling Laws](https://arxiv.org/abs/2409.17858v2) | 2024／v2 | T6 | 正文定向；已综合 |
| [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929v2) | 2020／v2 | T7 | 仅摘要；候选 |
| [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377v3) | 2021／v3 | T7 | 仅摘要；候选 |
| [Reproducible scaling laws for contrastive language-image learning](https://arxiv.org/abs/2212.07143v2) | 2022／v2 | T7 | 正文定向；已综合 |
| [Scaling Vision Transformers to 22 Billion Parameters](https://arxiv.org/abs/2302.05442v1) | 2023／v1 | T7 | 仅摘要；候选 |
| [Sigmoid Loss for Language Image Pre-Training](https://arxiv.org/abs/2303.15343v4) | 2023／v4 | T7 | 仅摘要；候选 |
| [Scaling Laws for Generative Mixed-Modal Language Models](https://arxiv.org/abs/2301.03728v1) | 2023／v1 | T7 | 全文文字与附录；已综合 |
| [MM1: Methods, Analysis & Insights from Multimodal LLM Pre-training](https://arxiv.org/abs/2403.09611v4) | 2024／v4 | T7 | 仅摘要；候选 |
| [Data curation via joint example selection further accelerates multimodal learning](https://arxiv.org/abs/2406.17711v1) | 2024／v1 | T7 | 仅摘要；候选 |
| [Improved Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2102.09672v1) | 2021／v1 | T7 | 仅摘要；候选 |
| [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752v2) | 2021／v2 | T7 | 仅摘要；候选 |
| [Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748v2) | 2022／v2 | T7 | 仅摘要；候选 |
| [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2403.03206v1) | 2024／v1 | T7 | 仅摘要；候选 |
| [Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps](https://arxiv.org/abs/2501.09732v1) | 2025／v1 | T7 | 全文文字与附录；已综合 |
| [Inference-time Scaling of Diffusion Models through Classical Search](https://arxiv.org/abs/2505.23614v2) | 2025／v2 | T7 | 仅摘要；候选 |
| [Inference-Time Scaling in Diffusion Models through Iterative Partial Refinement](https://arxiv.org/abs/2605.19317v1) | 2026／v1 | T7 | 仅摘要；候选 |
| [RT-1: Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817v2) | 2022／v2 | T7 | 仅摘要；候选 |
| [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818v1) | 2023／v1 | T7 | 仅摘要；候选 |
| [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864v9) | 2023／v9 | T7 | 仅摘要；候选 |
| [Data Scaling Laws in Imitation Learning for Robotic Manipulation](https://arxiv.org/abs/2410.18647v4) | 2024／v4 | T7 | 全文文字与附录；已综合 |
| [AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation](https://arxiv.org/abs/2607.21588v1) | 2026／v1 | T7 | 仅摘要；候选 |

## 综合时保留的关键修正

1. 不把初始核理论直接视为特征学习理论；后者在受控模型中的指数提升有任务难度、损失和优化器条件。
2. 不把低 loss 等同任务成功；区分固定配方下的共同曲线、跨语料改变后的任务错配，以及微调和提示两种评价设置。
3. 不把“连续指标”当作消除涌现争论的充分手段；同时检查机会基线、正确与错误选项概率以及事前预测。
4. Mixed-modal 的 45.12B token 是边界附近拟合预测，检验 run 使用 50B token；不能混写为同一实验数值。
5. 扩散搜索可能提高单样本代理分数却损害总体多样性；NFE、FLOPs、verifier 费用与实际延迟需要分别记录。
6. 机器人文中的幂律拟合基于六个规模点，1191 个环境—物体组合的外推未验证；评分、成功率与动作 MSE 不可互换，任务协议的限制必须保留。

## 后续更新优先级

第一优先是候选中的基础方法与边界复核：ViT／MAE／DiT／rectified flow、SigLIP／JEST、RT-1／RT-2／Open X-Embodiment 的方法、消融、成本和局限；同时补充核谱与随机特征推导。第二优先是检查 2026 IPR 与 AXIS 的全文、评价协议及后续复现。新增工作只有在能修复当前问题、揭示失败边界或提供更可靠外推验证时，才进入主线而非仅追加目录。
