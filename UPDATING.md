# 持续更新流程

## 运行约定

维护目录为当前仓库。默认每周一 09:00 America/Los_Angeles，由已存在的 Codex“更新 Scaling Law 综述”任务继续维护；实际调度配置以应用中的任务卡为准。仅在重要结论变化、明显新分支、失败或需要用户行动时通知。

这是需要研究判断的更新任务，不是自动复制 RSS 标题。机器离线、认证或网络限制可能导致未执行；一次任务成功配置不代表未来每次都已完成。

## 每次运行

1. 读取 README、METHODOLOGY、本文、data/state.json、最近 CHANGELOG 与用户后续要求。以最近一次成功检索日期向前重叠14天，防止索引滞后；首次运行重新核验核心版本。
2. 搜索论文、作者/机构 blog、technical report 与三类社区平台。关键词覆盖 scaling laws / compute-optimal / data-constrained / MoE / reward scaling / test-time compute / inference-time scaling / scaling evaluation / multimodal。
3. 核查标题、作者、首发日期、当前版本、撤稿或重要更正。优先使用稳定 arXiv ID/DOI 去重，blog与社区链接关联论文，不能重复计成多个独立研究。
4. 比较旧问题与新证据。新增项必须写清 problem、insight、method、result、limitation、branch、reading_depth、verification_date；证据不足者进待查队列。
5. 若需要改写正文，同步修改 `docs/` 中文源章节与 `docs/en/` 完整英文对应章节，保留旧结论的历史记录并说明变化原因。同步更新 sources、社区雷达、CHANGELOG 和状态；无变化时只更新必要的检索运行记录，不制造“进展”。
6. 运行 `python3 scripts/build_survey.py` 和 `python3 scripts/validate.py`。正文变化后分别运行 `python3 scripts/build_pdf.py --language zh --check` 与 `python3 scripts/build_pdf.py --language en --check`，检查两种 PDF 渲染；PDF构建失败时标明PDF落后版本，不能把旧PDF冒充最新。
7. 本地内容验证成功后才提交。若 GitHub 已配置并由用户授权正常发布，可提交/推送本仓库更新；有用户未提交修改时只暂存本次修改，不能覆盖或强推。未认证或无远端时维护本地，保留发布阻塞。
8. 只有检索成功才推进 last_successful_search；源站访问失败不算“没有新论文”。部分检索成功时记录失败平台与覆盖限制。每次通知附改变了哪条问题线及对应证据链接。

## 改写正文的门槛

值得改写：可靠反证/复现；旧假设失效；新的可复现成本最优关系；方法解决了先前明确瓶颈；评测口径改变后旧结论需要收缩；重要版本更正。

仅更新索引：小范围基准涨分；同类配方新模型；只存在宣传摘要的新报告。未读主源的热门讨论只进入候选队列。

## 版本与发布

默认 `README.md` 始终为英文；`README-zh.md` 为中文首页，两者互链并分别导向对应语言。源章节和证据是事实来源；SURVEY.zh-CN.md、SURVEY.en.md、REFERENCES.md、REFERENCES.en.md、references.bib、data/papers.json 是生成产物。PDF是阅读版，公式精确表达仍以Markdown为准。文献库不要求一次收齐所有作者，但缺失字段必须保留真实状态；任何后续补全应核对主源。

中英文均包含导论、七篇技术章、社区雷达、结论、术语表与方法附录。更新任一语言后，须逐段复核论证、数字、公式、引用和限制，再更新 `data/translation-status.json` 中该章节的两个 SHA-256 与复核日期；不能为消除报错而直接批量刷新指纹。若翻译或 PDF 落后，明确标记，不能发布成同步版本。

七篇技术章的路径以 `scripts/build_survey.py` 中的 CHAPTERS 为准；旧的合并章节保留导航入口。独立公式使用 `$$`，行内公式使用 `$`，保持 GitHub 可读。新增目录条目后检查 `docs/evidence-map.md`：仅摘要候选、正文实际引用与深度阅读分别报告。每次选取最可能改变已有结论的候选升级阅读，不能仅不断追加待查标题。

GitHub Actions 在提交与 PR 时检查源记录、本地链接和生成产物一致性；文献检索与综合仍由每周 Codex 维护任务完成。PDF排版在有字体与渲染依赖的本地环境检查，不把旧PDF生成成功当作新正文已校验。

远端发布只包括本综述目录中的研究内容与构建文件。不要上传其他项目、凭据、浏览器会话、个人记录、临时第三方全文或环境配置。
