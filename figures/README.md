# 图示来源与维护

`evolution-map.png` 是为本用户同一综述请求的先前中断任务使用内置 image generation 工具生成的概念图，已检查文字与关系后复用。它不是论文原图，不包含实验数值。生成日期：2026-09-16。

生成规格：白色背景，海军蓝字体，青/橙/紫/蓝分支；主轴是 Predict loss from scale → Allocate model + data → Which constraint is binding；分支分别是数据、部署、推理、能力评估；底部汇合为 pretraining + post-training + inference 联合优化。箭头表示问题关系，不声称历史因果。

图中“Smaller models, MoE”只表示针对部署成本的两类研究路线，不能理解为MoE必然降低实际延迟；“Search, verification, RL”将相互影响的推理与后训练机制合并展示，RL本身仍属于训练阶段。正文对这些条件分别解释。多模态支线未单独画出，见技术章。

精确、可编辑的关系图保存在 Markdown 的 Mermaid 代码中。若主线发生改变，应同步更新图与说明；不能只刷新文稿日期而沿用不再准确的图。
