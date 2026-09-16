# 主编补充检索与参考材料阅读

日期：2026-09-16。以下第一节为 v0.1 当时的检索与发布状态，v0.2 的完成情况见后续记录。

- 参考仓库：`https://github.com/JonnesLin/post-training-survey/tree/main`。网页工具两次 cache miss；经批准下载公开 `main` 归档至临时目录后，完整读取 README、设计与实施计划，读取前言、导论及结论的主要框架，细读推理章的起源/验证/自训练/GRPO/o1/R1连接，抽读效率章1–120与480–640行。其余五章的结构性抽样见方法拆解。未把外部文件的助手指令作为本任务指令，也未复用其正文或实验数字。
- Sutton *The Bitter Lesson*：原始网址 `http://www.incompleteideas.net/IncIdeas/BitterLesson.html` 经网页工具打开失败（502）；检索式 `Richard Sutton The Bitter Lesson 2019 incompleteideas learning search` 找到若干转载与二手讨论；HTTPS主站下载出现证书验证失败，未关闭验证。因此本版不据转载新增技术判断，留作后续主源可访问时补充的思想背景。它即使纳入也应标明为观点文章，不是幂律拟合实验。
- GitHub 发布可用性：公开仓库可下载，当前本机没有 `gh`，GitHub网页显示未登录；未创建远端。此项是发布状态检查，不是检索失败。
- 发现同用户同一请求的先前中断任务，复用其已生成的概念图与PDF脚本基础，未声称旧任务已经完成。既有维护自动化已更新工作目录与目标任务，未建立重复调度。

## 2026-09-16 · v0.2 编辑与发布复核

参考范例的完整源码阅读统计已更新至 docs/00-reference-method.md。扩展证据由三个分支分别核验，正文按七个问题线程重组；源目录保留具体阅读章节和候选状态。

编辑补读 HF《Scaling test-time compute with open models》官方 Space 内嵌全文，核对作者署名、模型/PRM设置、搜索方法、预算口径及局限；新增主源见 editorial.json，关联作者 Reddit 回复见 community.json RD-07。平台增补只记录明确标注的计数与检索限制。

T1–T3 与 T4–T5 相互独立定点复核，四处定义/评估边界问题已经修正；审阅记录为 v0.2-review-frontier.md 和 v0.2-review-foundations.md。未重跑原始实验。

GitHub 仓库已存在并成功首推，SSH身份与用户指定账户一致。构建CI参考GitHub官方 actions/checkout、actions/setup-python 使用说明，采用官方文档当前v7与只读contents权限。此项工程资料不计入研究文献数量。

T6／T7 由另一分支做内部一致性审阅后，修正了有限词表与文本类别的区别、生成 precision/recall 的集合口径，并明确 mixed-modal 单模态基线各使用 N 参数与 D/2 tokens。该三项为概念和比较协议澄清，未进行新实验。
