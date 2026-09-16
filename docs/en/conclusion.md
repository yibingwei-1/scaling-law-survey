# Synthesis: How Has the Research Focus Shifted, and What Evidence Matters Next?

Reducing scaling laws to “larger models perform better” cannot explain why identical compute budgets produce models of different quality, why smaller models may warrant longer training, or why longer thinking sometimes reduces accuracy. The preceding chapters show several overlapping shifts in the field's focus.

First, **from observed improvements to predictable returns**. Early learning curves made the benefits of larger experiments estimable, allowing smaller experiments to inform larger investments. The remaining issues concern functional form and extrapolation range: low fitting error alone cannot guarantee reliable predictions across orders of magnitude. Second, **from increasing one resource to allocating resources jointly**. Kaplan, Chinchilla, and reanalysis studies examined the relationship between parameters, data, and training computation, showing that the optimal configuration depends on experimental design and cost conventions. [Hestness](https://arxiv.org/abs/1712.00409); [Kaplan](https://arxiv.org/abs/2001.08361); [Chinchilla](https://arxiv.org/abs/2203.15556); [Porian](https://arxiv.org/abs/2406.19146).

Third, **from nominal resources to effective resources**. Repeated tokens are not new information; selected data need not be more valuable for every task; total MoE parameters do not equal active computation per step; and FLOPs are not latency or monetary cost. Resource optimization must therefore specify the data distribution, architecture, hardware, and model lifecycle. [Data-constrained scaling](https://arxiv.org/abs/2305.16264); [DataComp-LM](https://arxiv.org/abs/2406.11794); [Routed LMs](https://arxiv.org/abs/2202.01169); [Beyond Chinchilla](https://arxiv.org/abs/2401.00448).

Fourth, **from predicting average loss to optimizing task systems**. Inference-time sampling and search expand the candidate pool, verifiers turn that potential into selectable answers, and post-training changes how models explore and use their budgets. These approaches complement one another, while verifiable rewards, selector reliability, and task difficulty become new bottlenecks. Existing results support conditional cost frontiers, not a fixed universal exchange rate among pretraining, RL, and inference compute. [Snell](https://arxiv.org/abs/2408.03314); [DeepSeek-R1](https://arxiv.org/abs/2501.12948); [s1](https://arxiv.org/abs/2501.19393).

These shifts do not imply that earlier approaches have been completely replaced. Better base models can increase the probability of successful RL exploration; better data can improve both pretraining and verification; and reliable inference trajectories can feed into distillation. These cross-branch relationships explain more than a straight narrative in which pretraining ends and inference takes over.

## Turn Debates into Testable Questions

| Common debate | A testable formulation | Evidence that would change the narrative |
|---|---|---|
| Has scaling hit a wall? | For which objective, budget range, data distribution, and system configuration do returns diminish? | Reproduction across scales with consistent accounting, plus counterfactual comparisons after changing constraints |
| What happens when data run out? | At fixed unique data, total compute, and target distribution, what gains come from repetition, selection, and synthesis? | Accounting for generation and selection costs, real-data controls, and tail evaluation |
| Can smaller models replace larger ones by thinking longer? | Which problems permit such substitution at equal end-to-end budget and latency? | Complete compute accounting, difficulty stratification, realistic selectors, and reproduction across tasks |
| Does RL create new capabilities? | How does the solvable set change after matching prompts, sampling, length, and checkers? | Full pass@k curves, disclosure of external information, and replication across base models |
| Does long CoT establish reasoning? | Does increasing the budget causally improve delivered outcomes, and does the conclusion survive interface changes? | Randomized budget interventions, separation of action execution from algorithmic representation, and tool-cost accounting |
| Do multimodal models inherit language-model laws? | How do optimal proportions of visual data, encoders, and language backbones change with the objective? | Independent variation of each axis, with distribution-specific and worst-group results |

This table is a research agenda, not a claim that every question has been answered. It also sets a threshold for maintenance: a new benchmark point can first enter the reference index; evidence that changes an assumption, supplies a counterexample, establishes a new cost convention, or repairs a critical failure should alter the corresponding connection in the survey.

## What Remains Missing

This edition extends the discussion to diffusion models and robotics under their distinct data and feedback constraints. Scientific foundation models, long-horizon agents, hardware energy use, and economic scaling still need fuller synthesis. Limited disclosure of data and costs in industrial training often prevents direct comparison across organizations. Much of the 2026 literature awaits further replication, and community search indexes have temporal lags and visibility biases.

Future maintenance should first upgrade verified abstract-only candidates into reviews of methods and evidence, track publicly reproducible post-training and inference cost frontiers, and expand tool-use and cross-distribution evaluation. The result should be an increasingly accurate map of research questions, not merely a longer list of papers.

## Cross-Chapter Relationships Matter More Than a Single Optimal Exponent

At least four interactions connect data, architecture, feedback, and evaluation. Data selection changes the training distribution and therefore the regions a verifier can judge reliably. Architecture and caching change how many candidates fit within an inference budget, moving the practical cost frontier of search. Reliable search trajectories can enter post-training, converting a one-time inference expense into policy capabilities that can subsequently be amortized. Changes in evaluation protocol may then reduce or erase those gains on new tasks. These relationships organize the evidence reviewed above; they are not a single precise dynamical model shared by all the papers.

This yields a more concrete way to judge new work: does it reach a larger scale on an existing curve, change the curve itself, change the price of available resources, or change the objective being measured? All four can matter, but they require different controlled comparisons. Updates should first revise the affected question and assumptions, then add the relevant papers. Later readers can then understand why a conclusion held, why its scope subsequently narrowed, and which branches remain worth pursuing.
