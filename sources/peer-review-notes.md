# 独立交叉审查记录

审查日期：2026-09-16。审查对象：`docs/02-posttraining-inference.md`、`docs/04-community-radar.md` 及其来源元数据和检索日志。由预训练章节作者独立检查后训练及社区章节；未复现实验，也未把所有社交指标重新抓取一遍。

## 2026 主源核验

| 原始来源 | 独立核验结果 | 对综述的影响 |
|---|---|---|
| [Min-Seek / Thinking Long, but Short](https://arxiv.org/abs/2601.09855) | 2026-01-14 首次提交；标题与作者匹配。阅读 v1 方法、实验及单次生成限制。另由 [ACL Anthology](https://aclanthology.org/2026.findings-eacl.153/) 核验 2026-03 正式发表于 Findings of EACL，页 2942–2951，DOI 10.18653/v1/2026.findings-eacl.153。 | 已补正式发表链接和元数据，`type` 改为 `conference_paper`；技术阅读版本仍明确为 arXiv v1，不冒充已逐项比较正式版。 |
| [Adaptive Test-Time Compute Allocation](https://arxiv.org/abs/2604.14853) | 2026-04-16 首次提交，标题和作者匹配。v1 §5.1 明确每基准 200 题、48 次生成、离散采样预算，路由特征含单次 LLM 调用产生的归一化熵；§E.2 说明 80/20 划分。 | 已把“较小测试集”改为抽样与划分的准确描述，并提示完整路由成本不能等同于轻量分类器成本。主要预算按采样次数计量；本次没有证据断言作者一定漏算了某项，因此采用需要端到端核算的限定表述。 |
| [Curriculum Reinforcement Learning](https://arxiv.org/abs/2606.22317) | 2026-06-21 首次提交，标题和作者匹配。v1 方法明确教师指导、课程与 RL 的混合流程，报告 pass@1 和 pass@256 改善。 | 原文已经保留教师监督条件，没有把它写成纯 RL 获得新能力的证明，无需实质修改。全失败组的零信号严格指奖励驱动的组内策略梯度项，不代表任意其他正则项都为零。 |
| [Test-Time Scaling: Inference Regimes, Evaluation, and Reproducibility](https://arxiv.org/abs/2608.04001) | 首次提交 2026-08-04，最新 v2 修订于 2026-08-31。成功读取 [v2 全文](https://arxiv.org/html/2608.04001v2) 的 §2–3，核查三种推理形态、完整搜索成本、候选库诊断与在线停止。 | 已将正文两处链接及元数据升级为 v2。综述只采用框架，不引用版本间容易混淆的 trace 总数。 |
| [There Will Be a Scientific Theory of Deep Learning](https://arxiv.org/abs/2604.21691) | 2026-04-23 首次提交，Jamie Simon 等，标题与研究纲领内容匹配。此次核验摘要和元数据。 | 社区章节将其作为理论研究观点文章而非统一定理，措辞适当。 |

没有发现这五条 2026 主源的标题、日期或核心内容为虚构。此结论仅涉及本次核验范围，不代表实验结果已经得到独立重复或学界共识。

## 社区指标的语义与可追溯性

现有章节正确区分 YouTube views/likes、Reddit score、评论内容和 X 无法读取的指标；阈值是编辑筛选代理，未冒充跨平台热度排行。缺失指标保留 `null`，搜索索引快照未写成实时计数。X 上 GLM 相关帖子关联的技术正文无法读取时，具体技术主张没有进入综述结论，处理恰当。

本次独立搜索复现了 [Reddit 的 Z.ai 讨论](https://www.reddit.com/r/LocalLLaMA/comments/1vsf9eg/thoughts_about_scaling_law_zai/) 的索引日期 2026-08-19 与 score 519，以及 [Dave's Garage 视频](https://www.youtube.com/watch?v=r3TpcHebtxM) 的 2025-01-27 发布日期、2,436,922 views 和 128,000 likes。复核查询包括 `"Thoughts About Scaling Law - Z.ai" "519"` 和视频标题/ID。

另成功打开 [理论文章 Reddit 讨论](https://www.reddit.com/r/MachineLearning/comments/1sun588/there_will_be_a_scientific_theory_of_deep/)，核实帖子链接到上述原论文；这次页面没有可用的计数，因此没有独立复现原记录的 score 263。该数字继续依赖原检索日志，未擅自覆盖为其他时刻的计数。其余社区数字也不能声称本次全部二次核验。

## 基础章节元数据补充

17 条 `foundations.json` 记录均重新打开各自 arXiv 摘要页，补充经核验的首位作者加 `et al.`、首次公开日期、最近修订日期与最新版本。日期指 arXiv 公开/修订日期，不自动等于会议发表日期。只有 v1 的记录，其 `last_revised_date` 为 `null`，表示没有独立修订版本。

`version_read` 与 `latest_version_verified` 分开保存：此前仅使用无版本 HTML 地址且没有保留确切版本的六条记录，阅读版本保持 `null`，不把最新元数据偷换成全文阅读证明。Hestness、Kaplan、Chinchilla、Porian、Besiroglu 等核心记录均有明确阅读版本；Shukor 的 v2 仍只表示摘要/元数据已读。

本次已按任务协调授权，直接修订 `docs/02-posttraining-inference.md`、`sources/frontier.json` 与 `sources/foundations.json`；社区章节没有修改。未新增关于论文有效性或平台热度的强结论。
