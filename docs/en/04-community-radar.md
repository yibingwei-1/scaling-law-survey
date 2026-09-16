# Community Radar: Which Debates Should Change the Scaling-Law Survey?

Search date: **September 16, 2026**. This round established **18 traceable records: 4 from X, 6 from YouTube, and 8 from Reddit**. Eight meet the screening threshold, seven provide instructional or contrasting context, and engagement counts remain unverified for three X posts. The date identifies this search round; **it does not mean that views or votes in the search index are live counts from that day**.

Community discussion exposes unresolved questions among researchers and practitioners. Technical conclusions still require papers, author code, and official reports: high view counts indicate reach, not correctness, and vigorous debate is not independent replication. Full fields appear in [community.json](../../sources/community.json); searches and leads not included appear in [community-search-log.md](../../sources/community-search-log.md).

## 1. Operationalizing “High Attention”

The initial round uses explicit, conservative editorial thresholds: a YouTube search-index view count of at least 100,000 or a Reddit post score of at least 100 receives the label `high_attention_proxy`. This is a signal for reading priority, not a statistical definition of popularity or an exhaustive platform ranking. For X, an explicitly labeled view count of at least 100,000 provides the same priority signal. Only X-04 currently has an indexed original-post view count, below that threshold; the other three remain unverified. Counts claimed by third-party mirrors are not entered as X metrics.

`context_below_screening_threshold` is retained for items that clarify technical disagreements, such as misunderstandings of Chinchilla optimality and rebuttals to the Apple paper. This captures broadly circulated topics while preserving less prominent but necessary counterarguments. The threshold controls search priority, not scientific value.

Missing counts are recorded as `null`, not zero. Reddit scores differ from total likes and comment counts, and an upvoted reply cannot supply the parent post's metrics. Reliable total comment counts are unavailable in this round, so “visible attention signals” is more accurate than a claim to have measured the full intensity of discussion. Views, likes, and scores are neither summed across platforms nor combined into a universal ranking.

## 2. Observed Examples of Circulation

All counts below are **index snapshots returned during searches on September 16, 2026**; the time when the counts themselves were collected is unknown. YouTube inspection covered metadata and descriptions, not complete video viewing or comment analysis.

| ID / platform | Post or video | Visible attention signal | Status and role in the survey |
|---|---|---:|---|
| YT-02 / YouTube | [Dave Plummer explains Deepseek R1](https://www.youtube.com/watch?v=r3TpcHebtxM), 2025-01-27 | 2,436,922 views; 128,000 likes | Meets threshold; a lead into R1 efficiency narratives |
| YT-03 / YouTube | [Fireship: Did DeepSeek R1 just pop the AI bubble?](https://www.youtube.com/watch?v=Nl7aCUsWykg), 2025-01-27 | 3,884,394 views; 152,000 likes | Meets threshold; distinguish efficiency gains from claims that scaling has failed |
| YT-01 / YouTube | [AI Coffee Break: s1 / “wait…”](https://www.youtube.com/watch?v=XuH2QTAC5yI), 2025-03-23 | 5,544 views; 335 likes | Below threshold; a technical explanation example |
| RD-02 / Reddit | [DeepSeek R1 has been officially released!](https://www.reddit.com/r/LocalLLaMA/comments/1i5p549/deepseek_r1_has_been_officially_released/), 2025-01-20 | Score +301 | Meets threshold; benchmarks, practical coding, and distillation |
| RD-03 / Reddit | [Discussion of Apple's The Illusion of Thinking](https://www.reddit.com/r/MachineLearning/comments/1l4nk5s), 2025-06-06 | Score +103 | Meets threshold; reasoning boundaries and evaluation confounds |
| RD-04 / Reddit | [Discussion of the rebuttal to The Illusion of Thinking](https://www.reddit.com/r/LocalLLaMA/comments/1lbgczn), 2025-06-14 | Score +58 | Below threshold; a necessary alternative interpretation |
| RD-01 / Reddit | [New Llama scaling laws?](https://www.reddit.com/r/MachineLearning/comments/1eq95ga), 2024-08-12 | Score +48 | Below threshold; common misunderstandings of Chinchilla |
| RD-05 / Reddit | [There Will Be a Scientific Theory of Deep Learning](https://www.reddit.com/r/MachineLearning/comments/1sun588/there_will_be_a_scientific_theory_of_deep/), 2026-04-24 | Score +263 | Meets threshold; empirical regularities versus mechanistic theory |
| RD-06 / Reddit | [Thoughts About Scaling Law - Z.ai](https://www.reddit.com/r/LocalLLaMA/comments/1vsf9eg/thoughts_about_scaling_law_zai/), 2026-08-19 | Score +519 | Meets threshold; new claims await primary-source verification |

Additional records cover research talks and engineering reproduction discussions directly relevant to scaling laws. The value of a lecture does not depend on crossing an attention threshold; only metadata and descriptions were verified for all videos.

| ID / platform | Post or video | Indexed attention signal | Research connection |
|---|---|---:|---|
| YT-04 / YouTube | [Jared Kaplan's scaling talk at YC](https://www.youtube.com/watch?v=p8Jx4qvDoSo), published 2025-07-29 | 60,347 views; 965 likes | How a researcher connects pretraining, RL, and compute efficiency; the talk took place on 2025-06-16 |
| YT-05 / YouTube | [Stanford CS336 2026 Lecture 9](https://www.youtube.com/watch?v=Q15rhEWZPQ4), 2026-04-30 | 12,604 views; 173 likes | An entry point into foundational course material |
| YT-06 / YouTube | [Stanford CS336 2026 Lecture 11](https://www.youtube.com/watch?v=vTfEyOyzV9E), 2026-05-19 | 8,699 views; 128 likes | A later lecture in the same course |
| RD-07 / Reddit | [HF authors share search reproduction and DVTS](https://www.reddit.com/r/LocalLLaMA/comments/1hfw14v/), 2024-12-16 | Score +507 | High attention; compare generators, verifiers, and costs together |
| RD-08 / Reddit | [Discussion of o3 and test-time scaling](https://www.reddit.com/r/LocalLLaMA/comments/1hirf2f/), 2024-12-20 | Score +142 | High attention; returns to budget and local deployment constraints |

X posts are listed separately so that author authority is not confused with engagement:

| ID | Original post and associated primary source | Scope verified in this round |
|---|---|---|
| X-01 | [Niklas Muennighoff announces s1](https://x.com/Muennighoff/status/1886405528777073134); [author repository](https://github.com/simplescaling/s1), [paper](https://arxiv.org/abs/2501.19393) | The author repository links directly to the post; the original returned 403; publication time, likes, replies, reposts, and views remain `null` |
| X-02 | [DeepSeek announces R1-Lite-Preview](https://x.com/deepseek_ai/status/1859200141355536422); [official announcement](https://api-docs.deepseek.com/news/news1120/) | The post URL is cited by s1; the official announcement was readable in the search index; the post returned 403; all counts remain `null` |
| X-03 | [Jie Tang: Thoughts About Scaling Law](https://x.com/jietang/status/2089941544581403107); [associated official blog](https://z.ai/blog/glm-5.3) | Reddit and secondary coverage trace back to the same post; X returned 403 and the official blog did not return readable body text; all counts remain `null` |
| X-04 | [A post circulating the HF search results](https://x.com/kimmonismus/status/1869337064740938145), 2024-12-18 | The original-post index shows 7,143 Views; the direct page returned no body text; unlabeled numbers are not interpreted as likes or reposts. This is the same research event as RD-07 |

## 3. Turn Discussion into a Problem-Driven Research Narrative

### 3.1 Does Continued Training of Smaller Models Overturn Chinchilla?

RD-01 is useful because it exposes a confusion between objectives: fixed FLOPs for one training run and a fixed deployment size serving many requests define different optimization problems. The survey should move naturally from allocating parameters and data under a training budget to allocating resources across training and serving. [Chinchilla](https://arxiv.org/abs/2203.15556) provides an empirical model for the former; [Beyond Chinchilla-Optimal](https://arxiv.org/abs/2401.00448) incorporates inference demand and examines extrapolation errors at very high tokens-per-parameter ratios.

The resulting connection is **an objective that omits deployment cost → a revised cost objective → longer training of smaller models becomes reasonable → fits require recalibration in extreme regimes**. It is not simply a small-model counterexample overturning an old law. The primary sources support this chain; Reddit identifies an accessible entry point into the confusion.

### 3.2 If R1 or s1 Is Inexpensive, Does More Compute Stop Mattering?

The two R1 videos with millions of indexed views and the release discussion show how rapidly methodological efficiency and cost narratives circulate. They do not independently establish that scaling has failed. The [DeepSeek-R1 report](https://arxiv.org/abs/2501.12948) connects RL training, inference behavior, and capability transfer to smaller models. [s1](https://arxiv.org/abs/2501.19393) offers another route to controlled test-time computation through an existing Qwen base, selected reasoning trajectories, and budget forcing.

The next question worth integrating is: **should an additional budget go to base-model pretraining, RL, teacher-trajectory generation, or extra computation on each test request?** A small count of SFT examples is not a substitute for full-pipeline cost accounting. R1-Lite-Preview and the released R1 also cannot be treated as the same experiment. This radar does not extract training-cost figures or leaderboard conclusions from news videos.

### 3.3 Under What Conditions Does More Thinking Stop Helping?

[Apple's original study](https://machinelearning.apple.com/research/illusion-of-thinking) distinguishes low-, medium-, and high-complexity behavior in controlled puzzles. [Lawsen's Comment v2](https://arxiv.org/abs/2506.09250v2) raises confounds involving output length, scoring, and unsolvable instances. The RD-03/RD-04 debate should become a set of verifiable questions: are budgets comparable, are instances solvable, does the answer representation require exponentially long outputs, and does tool use change the task definition?

This branch cannot be compressed into either “LLMs cannot reason” or “the rebuttal proves there are no boundaries.” The experiment and response constrain the scope of their respective evidence; the response's second version also notes corrections to its earlier version. A review must retain versions and distinguish **the return curve for more computation** from **a failure point under one evaluation protocol**.

### 3.4 A Question Added in 2026: Can Empirical Regularities Become Mechanistic Explanations?

The [2026 position paper](https://arxiv.org/abs/2604.21691) linked by RD-05 advocates connecting solvable models, tractable limits, macroscopic empirical regularities, hyperparameter theory, and universal phenomena. It motivates a theoretical branch asking why particular exponents arise and when they transfer. It is a research agenda, not evidence that a unified theory is complete.

RD-06 and X-03 are recent candidates connecting deployment conditions, MoE, and post-training budgets. The associated official blog did not provide readable body text in this search round, so **we record the questions without adopting specific claims about new-model performance or architectural mechanisms**. Appearance on two platforms indicates cross-platform circulation, not two independent technical validations.

### 3.5 What Exactly Does “3B Beats 70B” Compare?

RD-07 provides a more useful research conversation than a repeated headline. After the authors shared open-model search experiments, readers asked how large the verifier was and whether 256 candidates actually saved compute relative to one generation from a larger model. The author replied that a strict FLOPs comparison had not been completed and suggested that extensive sampling with the 3B system might be less compute-efficient than 70B, while its memory requirements made deployment more accessible. This is an author's clarification of their own experiment and should still be read alongside the technical material. [Original post and author replies](https://www.reddit.com/r/LocalLLaMA/comments/1hfw14v/).

In the [authors' technical article](https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute), the generator, verifier, and search algorithm together constitute the evaluated system. The case raises the question of **how to combine generation and verification within memory and acceptable-latency constraints**, rather than demonstrating that parameters no longer matter. It shares the cost-accounting issue in [architecture and deployment](03-architecture-deployment.md) and directly connects to search allocation in [inference-time budgets](05-inference.md).

RD-08 connects these changes to public discussion of o3, but community speculation about undisclosed training procedures lacks sufficient evidence. The survey retains the explicit budget questions, not inferences such as “pretraining has stopped improving.” X-04's headline similarly compresses experimental conditions. A complete update should therefore connect **headline → author experiment → reader questions → author qualifications → survey revision**, rather than merely adding a popular link.

## 4. Preserve Comparability Across Updates

Each update begins with searches over the preceding 7–30 days, followed by author responses, corrections, and independent reproductions. Merge records of the same event using DOI, arXiv ID, and canonical URL. Preserve earlier observations and append new counts, access status, and evidence timestamps; do not overwrite historical observations with current values.

Once stable counts are available, medians, quantiles, and growth rates could be reported within a platform, time window, and comparable set of channels or communities. The current selective seed sample does not support reliable “top 10%” rankings or engagement-growth estimates. Platform APIs or readable pages authorized by the user may later fill gaps in comments, reposts, and views. Failed access continues to produce `null`, not guessed values.

A candidate enters the technical narrative only after the primary source establishes which earlier limitation it addresses, what the experiment controls, and which trade-offs remain. Updates prioritize counterevidence and corrections that change existing conclusions, then independent reproduction, then new allocation evidence, and only afterward high-exposure opinion. Reposts that do not change understanding update the radar rather than repeatedly expanding the prose.

## 5. Limitations of This Round

This is a purposive seed search concentrated on English-speaking communities, language models, and selected turning points. Search visibility, channel size, community population, emotionally framed headlines, and accumulated attention all affect counts. X login restrictions and missing YouTube comments make platform coverage uneven. Chinese and other non-English discussions, negative results, smaller research groups, and work outside social media may be underrepresented. The table supports decisions about what to verify next, not a ranking of the most popular papers across the field or a claim of community consensus.
