# 社区检索日志

检索日期：2026-09-16。执行方式：网页搜索工具的 `search_query`、`open`、`find` 与作者仓库交叉链接。未登录 X，未使用私人账号数据或付费平台 API。以下保留影响选样的查询、回溯链和失败记录，不保存整篇帖子或视频转录。

## 检索目标与规则

目标不是逐个平台凑“热门论文”，而是寻找能暴露研究分歧的帖子，并回到主源确认技术内容。检索覆盖 Chinchilla、s1、DeepSeek-R1、测试时计算、scaling 边界和 2026 年新增讨论。种子样本不宣称全量覆盖。

计数只按工具返回的字段登记：YouTube `views` / `likes`；Reddit 可见 `score`；未知评论总数保持 `null`。X 未获得可直接核验的计数。检索日期和计数快照时间分开：后者本轮全部未知。本轮筛选阈值由编辑预先明确为 YouTube ≥100,000 观看或 Reddit score ≥100，用于排阅读优先级，不用于推断技术正确性。

## 查询与主要结果

| 阶段 | 实际使用的查询（选录） | 结果与处理 |
|---|---|---|
| 训练最优性 | `site.reddit.com/r/MachineLearning Chinchilla compute optimal large language models` | 找到 Llama / Chinchilla 误读、Cerebras-GPT、推理成本讨论；保留 RD-01 作为目标函数辨析入口 |
| s1 传播 | `site.reddit.com/r/LocalLLaMA s1 simple test time scaling`；`"s1: Simple test-time scaling" "youtube"` | 找到 s1 帖和视频；视频可见 5,544 观看、335 赞；作为技术背景样本，未标热门 |
| s1 作者原帖 | `"s1: Simple test-time scaling" "x.com"`；`"1886405528777073134" "s1"` | 得到原帖 ID，再回溯 [作者仓库](https://github.com/simplescaling/s1) 与 [论文](https://arxiv.org/abs/2501.19393)；X 读取 403 |
| Chinchilla 原帖 | `"Chinchilla" "karpathy/status"`；`"1781033433336262691"` | 得到 Karpathy 相关原帖线索，但直接读取空页；留在备选，不录任何互动数 |
| R1 视频 | `site:youtube.com/watch "DeepSeek-R1" "views"` | 得到 Dave's Garage 与 Fireship 两条百万观看视频；保留 YT-02 / YT-03；只读元数据及说明栏 |
| R1 Reddit | `site.reddit.com "DeepSeek-R1" "votes"` | 得到发布帖 +301 score；回溯仓库链接和 [R1 报告](https://arxiv.org/abs/2501.12948) |
| Lite-Preview | `"DeepSeek-R1-Lite-Preview" "x.com"`；`"DeepSeek-R1-Lite-Preview" site:api-docs.deepseek.com/news/news1120` | 确认官方公告与 X 原帖的引用链；原帖 403，官方域名索引可读但直接 open 超时 |
| 失效边界 | `"The Illusion of Thinking" site:reddit.com/r/MachineLearning` | 找到原研究讨论 +103；回到 Apple 官方研究页 |
| 反驳 | `"Comment on The Illusion of Thinking" site:reddit.com/r/LocalLLaMA/comments/1lbgczn` | 找到反驳讨论 +58；同时核验 [Comment v2](https://arxiv.org/abs/2506.09250v2) 的修订说明 |
| 当年扫描 | `"scaling laws" "2026" site:reddit.com/r/MachineLearning` | 找到 2026 理论观点论文 +263，以及近期 Z.ai 讨论 +519；保留 RD-05 / RD-06 |
| 新 blog 回溯 | `"Thoughts About Scaling Law" "Z.ai"`；`"2089941544581403107"` | 发现 Reddit、二级报道与同一 X 原帖；官方 [GLM-5.3 blog](https://z.ai/blog/glm-5.3) 返回空正文，具体技术主张待核验 |

## 可见计数证据摘记

以下是索引返回的短元数据片段，不是实时抓取的 API 数据；canonical URL 保存在 JSON 中。每个数字只使用一次，未把回复分数叠加到帖子分数。

| 记录 | 返回的计数 | 发表日期信息来源 | 未取得字段 |
|---|---|---|---|
| YT-01 | `5544 views, 335 likes` | YouTube 索引 `Published: 2025-03-23` | 评论、指标采集时间 |
| YT-02 | `2436922 views, 128000 likes` | YouTube 索引 `Published: 2025-01-27` | 评论、指标采集时间 |
| YT-03 | `3884394 views, 152000 likes` | YouTube 索引 `Published: 2025-01-27` | 评论、指标采集时间 |
| RD-01 | `+48 votes` | Reddit 索引 `Monday August 12 2024` | 点赞总数、评论总数、浏览 |
| RD-02 | `+301 votes` | Reddit 索引 `Monday January 20 2025` | 同上 |
| RD-03 | `+103 votes` | Reddit 索引 `Friday June 06 2025` | 同上 |
| RD-04 | `+58 votes` | Reddit 索引 `Saturday June 14 2025` | 同上 |
| RD-05 | `+263 votes` | Reddit 索引 `Friday April 24 2026` | 同上 |
| RD-06 | `+519 votes` | Reddit 索引 `Wednesday August 19 2026` | 同上 |
| X-01 / X-02 / X-03 | 无 | 未直接核验，JSON 日期为 `null` | 所有互动计数 |

## 访问失败及证据降级

- [s1 X 原帖](https://x.com/Muennighoff/status/1886405528777073134)、[DeepSeek X 原帖](https://x.com/deepseek_ai/status/1859200141355536422)、[Jie Tang X 原帖](https://x.com/jietang/status/2089941544581403107)：直接读取均返回 403。保留真实原帖链接及回溯源，证据级别为“交叉链接 / 摘要级”，热度不可核验。
- [Karpathy 原帖线索](https://x.com/karpathy/status/1781033433336262691)：直接读取返回零行。关联 [Reddit 讨论](https://www.reddit.com/r/MachineLearning/comments/1eq95ga) 可提示最优性误读，但不据此重建未读到的完整 X 对话。
- [s1 Reddit 帖](https://www.reddit.com/r/LocalLLaMA/comments/1iipyo2)：检索有链接但直接读取失败，未取得可靠计数；未作为已核验热门条目。
- YT-01 直接视频 URL 抓取失败；各视频只按搜索引擎返回的 YouTube 元数据和说明栏登记，不声称已观看或阅读评论。
- 部分 Reddit 帖 open 失败，而 search index 返回主帖和精选回复。RD-02、RD-06 页面可读，但页面提取未提供当前数值；计数仍明确来自索引。
- X 搜索也返回了第三方镜像中的互动数。因无法确定字段标签、缓存时间和原帖状态，未录入 X 指标。
- [Z.ai 官方 blog](https://z.ai/blog/glm-5.3) 返回零行；即使 Reddit 转述有可见热度，相关具体模型结果也只留待核验，未写成综述技术事实。

## 主源核验与版本差异

| 主源 | 本轮可读层级 | 对综述的约束 |
|---|---|---|
| [Chinchilla](https://arxiv.org/abs/2203.15556) | 页面 / 元数据；全文由综述主线另行核读 | 社区疑问不能被当作论文主张 |
| [Beyond Chinchilla-Optimal](https://arxiv.org/abs/2401.00448) | 摘要及版本历史 | 当前 v3 为 2025-04-14；最初提交为 2023-12-31，arXiv ID 为2401；区分版本与会议年份 |
| [s1](https://arxiv.org/abs/2501.19393) | 摘要、元数据及作者仓库 | 首次提交2025-01-31，v3为2025-03-01；少量SFT不等于从零训练成本 |
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | 摘要和元数据 | arXiv 页面本轮显示 v2 2026-01-04，Nature 2025；不把2024 Lite-Preview混入正式R1实验 |
| [Apple 原研究](https://machinelearning.apple.com/research/illusion-of-thinking) | 官方摘要、研究说明 | 描述所测任务和复杂度范围，不推广成“所有推理都不可能” |
| [Lawsen Comment](https://arxiv.org/abs/2506.09250v2) | 摘要及修订说明 | v2 为2025-06-16，移除Claude作者并更正v1部分章节；社区旧标题不等于当前元数据 |
| [There Will Be a Scientific Theory of Deep Learning](https://arxiv.org/abs/2604.21691) | 摘要和元数据 | 2026-04-23的观点论文；作为研究议程，不当作统一理论的实证完成 |

## 未入主表但可继续追踪的候选

| 线索 | 本轮可见证据 | 本轮处理 |
|---|---|---|
| [Cerebras-GPT Reddit 帖](https://www.reddit.com/r/MachineLearning/comments/12et59x) / [论文](https://arxiv.org/abs/2304.03208) | 索引 +154，2023-04-07；论文页面可读 | 有关注信号；本轮主表限制12条，训练最优性分支已由RD-01覆盖，可作下一轮系统验证分支 |
| [Beyond Chinchilla Reddit 帖](https://www.reddit.com/r/MachineLearning/comments/18yxu0d) | 索引 +5，2024-01-05 | 技术主源重要，但不能称帖子热门 |
| [2026 理论论文作者 X 线程](https://x.com/learning_mech/status/2047723849874330047) | RD-05 作者帖明确给出链接；直接 open 403 | 作者主源入口；未录热度 |
| [Karpathy Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI) | 搜索核验视频链接，但本轮未取得可见原始观看指标 | 有教学价值；不凭作者知名度补写计数 |
| [2026 年9月关于 scaling 极限的泛讨论](https://www.reddit.com/r/AskReddit/comments/1wfmwav/for_people_working_in_mlai_and_mathematicians_how/) | 索引主帖 +6；其中某回复 +55 | 提及 Bitter Lesson；主帖热度与直接技术证据均不足，不纳入热门表 |

## 下轮追加记录方式

后续保留该日期的历史字段，在独立快照或 `observations` 数组中追加新观测；记录查询时间窗、平台、原帖 URL、访问状态、计数来源和真实指标时间。若只有新的搜索摘要，不把它冒充实时平台观测。对同一论文的发布、批评、作者回应与复现分开记事件，并用主源 ID 关联。新的传播事件只有在改变已有研究链或暴露明确缺口时才更新综述正文。


## 2026-09-16 扩展复核

新增6条记录：YT-04–06、RD-07–08、X-04。查询覆盖 YouTube Jared Kaplan / Stanford CS336 scaling laws，Reddit test-time scaling 与 HF 复现，X Chinchilla/s1/test-time compute。保留平台原始链接，不采用二级镜像计数。YouTube元数据含观看、赞、发布日期；未观看全文。RD-07主帖与作者关于验证器/显存/FLOPs的回复可读；score来自检索索引。RD-08直接访问错误但索引文本和score可读。X-04原帖索引正文和明确标注的7,143 Views可读；直接打开返回空正文，其他裸数字不作指标。既有X三帖仍无可核验计数。

HF作者blog完整文本经官方Space链接的hf.space iframe读取：实验设置、BoN、beam search、DVTS、难度分桶、局限、署名均可读；记录到sources/editorial.json。所有计数观测日是检索日，快照采集时刻未知。未发现即未发现，不推断为平台没有讨论。
