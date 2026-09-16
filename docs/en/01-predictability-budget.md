# T1 Predictability, Budgets, and Training Recipes: What Is the Same Curve Actually Comparing?

> Verification date: 2026-09-16. Scope: empirical pretraining laws, budget allocation, optimization across scales, overtraining, and capability extrapolation. Evidence comes from the original papers; this chapter does not claim exhaustive coverage through the verification date. Core methods, experiments, and limitations were checked in targeted readings of the full texts; experiments were not rerun, nor were all appendices independently recalculated. See the [foundational sources](../../sources/foundations.json) and [additional sources](../../sources/expansion-foundations.json) for sources and reading depth. Direct lines of inheritance are identified in the text; other connections are this survey's synthesis of how the research problems evolved.

## 1. The Initial Prediction Target Was the Marginal Return on Additional Resources

The early engineering problem was not a lack of awareness that larger models and more data might help. It was uncertainty about how much another order of magnitude of resources would improve performance, and whether a plateau reflected the task's limits or a problem with the implementation. Across translation, language, image, and speech tasks, Hestness et al. adjusted both model capacity and optimization settings to measure the relationship between dataset size and generalization error. They distinguished a small-data region resembling guessing, a region of power-law improvement, and eventual saturation. This made learning curves a planning tool, without proving that every task could improve indefinitely at the same slope. [Hestness et al., 2017](https://arxiv.org/html/1712.00409v1)

Measuring data scaling alone was still insufficient: with a fixed budget, increasing the parameter count reduces the number of training tokens that can be processed. Kaplan et al. placed parameters, data, and training compute within one empirical framework, emphasizing that the greater sample efficiency of large models could allow an early-stopped large model to outperform a smaller model trained more fully. Their compute-optimal estimate was approximately $N_{\rm opt}\propto C^{0.73}$, but it primarily counted non-embedding parameters and used compute adjusted for batch size. This exponent cannot be detached from those definitions and compared directly with any later FLOPs curve. [Kaplan et al., 2020, §1 and §6](https://arxiv.org/html/2001.08361v1)

### From Loss Prediction to Practical Capabilities: GPT-3 and Gopher Exposed Another Layer of the Problem

GPT-3 was an important step in putting this resource perspective into practice: models ranging from 125M to 175B parameters received task examples without weight updates, demonstrating the potential for in-context learning to change with scale. It shifted attention from how much cross-entropy decreased to whether a single pretrained model could handle more tasks. These results could not, however, simultaneously establish optimal training budgets, the causal origins of each capability, and the absence of data contamination; the original report also disclosed shortcomings in its contamination filtering. Evaluation with a few prompt examples does not imply that the model never encountered relevant knowledge during pretraining. [Brown et al., 2020, §2–4](https://arxiv.org/html/2005.14165v4)

Gopher extended comparisons across model sizes to a broad range of tasks. Knowledge and reading comprehension improved more clearly, whereas some logic and mathematics tasks benefited less, and performance on some tasks even worsened with scale. Pretraining loss is therefore a compressed measure of model behavior, while capabilities emerge from the interaction of the model with task distributions, prompts, and evaluation. The point is not that average loss is useless, but that an average cannot by itself identify which capabilities have entered a regime of predictable improvement. [Rae et al., 2021/2022, §4.3](https://arxiv.org/html/2112.11446v2)

## 2. Chinchilla Revised Resource Allocation, Not Predictability Itself

Chinchilla directly revisited parameter/token allocation under a fixed compute budget. It estimated optimal configurations through three approaches: training-curve envelopes, IsoFLOP curves, and a parametric loss model. A 70B-parameter model trained on 1.4T tokens demonstrated the benefits of training a smaller model for longer, using a training compute budget comparable to Gopher's. One commonly used fit is

$$
L(N,D)=E+A N^{-\alpha}+B D^{-\beta},\qquad C\approx6ND.
$$

Here, $D$ counts processed tokens, $L$ is defined on a specified validation distribution, and the constants and exponents come from a particular training recipe. The expression $6ND$ is only an approximation for training dense Transformers; it does not include every context-related or systems overhead. [Hoffmann et al., 2022, §3–5](https://arxiv.org/html/2203.15556v1)

**This survey's algebraic explanation** substitutes $D=C/(6N)$ and sets the derivative to zero, yielding

$$
\alpha A N^{-\alpha}=\beta B D^{-\beta},\qquad
N_{\rm opt}\propto C^{\beta/(\alpha+\beta)},\quad
D_{\rm opt}\propto C^{\alpha/(\alpha+\beta)}.
$$

The optimal allocation balances the marginal returns from two reducible error terms. Only when their exponents are similar do the budget exponents for parameters and data both approach one-half. Roughly 20 tokens per parameter is thus an empirical approximation for a particular training objective and recipe, not an upper bound beyond which additional data becomes useless. The original paper's three fitting methods did not produce identical results either. [Tables 2 and 3 of the original paper](https://arxiv.org/html/2203.15556v1)

### Why Can Smooth Curves Produce Different “Optima”?

Porian et al. directly investigated the differences between Kaplan and Chinchilla, examining output-layer costs, warmup, and how learning rate and batch size change with scale. After adjustments, their allocation trends on two datasets were closer to Chinchilla's. Observed scaling effects can therefore be entangled with insufficient optimization of small models or inconsistent cost accounting; they cannot all be interpreted as physical properties of model capacity. [Porian et al., 2024; revised version consulted](https://arxiv.org/html/2406.19146)

The fitting procedure itself also needs auditing. Besiroglu et al. reconstructed Chinchilla's data from figures and repeated its third, parametric fitting approach, identifying issues with the parameters and confidence intervals. Their new fit was closer to the trends from the paper's first two methods. This was a check based on limited available material, not a full replication using complete original training logs. The relatively robust conclusion that models and data should grow together should be distinguished from the more fragile claim that a particular set of constants can extrapolate precisely across four orders of magnitude. [Chinchilla Scaling: A replication attempt, 2024](https://arxiv.org/html/2404.10102)

## 3. Optimization Is Also a Scaling Variable: Tensor Programs and μP

These disagreements raise a deeper question. If the best learning rate and update magnitude change with width, a curve connecting models trained with uncalibrated hyperparameters may be measuring the quality of tuning. Yet searching for hyperparameters from scratch for every large model consumes budget that could otherwise support the final training run. **What needs to transfer is not only model capability, but also the training recipe.**

Tensor Programs IV approached this issue through infinite-width parameterizations. Some limits turn a network into a kernel model with approximately fixed features; other parameterizations preserve feature learning. This distinction provides a theoretical foundation for the subsequent μP work, but does not directly imply the loss exponents of real language models. It addresses how networks can maintain nontrivial learning dynamics as width changes. [Yang & Hu, 2020/2022](https://arxiv.org/html/2011.14522v3)

Tensor Programs V turned this idea into μTransfer: tune a narrow model, then transfer suitable base hyperparameters to a wider model. The mechanism is not simply to multiply the global learning rate by a constant. It coordinates initialization, learning rates, and readout scaling across different tensors so that updates have an appropriately sized effect on activations. For example, under its Adam recipe, if a hidden matrix's width multiplier is $m$, its learning rate is $\eta_{\rm base}/m$; vectors and input and output layers follow different rules. Extracting just one of these scaling formulas while retaining the other settings of standard parameterization does not implement μP. [Yang et al., 2022, Table 3 and Appendix B](https://arxiv.org/html/2203.03466v2)

The paper used a roughly 40M-parameter proxy to search for hyperparameters for a 6.7B GPT-3-style model, reporting a tuning budget of approximately 7% of the large model's pretraining FLOPs. This suggests that small models can help choose the optimization settings behind a loss curve, as well as estimate the curve itself. Experimental details matter, however: the large-model comparison used different positional encodings, and numerical issues led the μP run to use FP32 while the baseline used FP16. Consequently, the full downstream difference cannot be attributed solely to parameterization. The theoretical basis for width transfer is also stronger than for transfer across depth, batch size, or sequence length; regularization hyperparameters do not have the same guarantees. [§6.1 and §7.4 of the original paper](https://arxiv.org/html/2203.03466v2)

This survey therefore separates the cost of a scaling experiment into finding a recipe and executing it. The primary value of μP is to reduce the former and reduce optimization mismatch across scales, rather than to claim that changing parameterization improves every power-law exponent. This also explains why new scaling papers should report tuning budgets and failed runs: these costs determine whether a method can genuinely guide the next expensive training run.

## 4. Checking a Curve Requires More Than Final Weights

One of OPT's contributions was to document restarts, loss anomalies, and hardware problems that are difficult to infer from a final curve. Real training budgets include recovery and the work required to keep runs operating; they are not determined solely by successfully processed tokens. Its open models support external analysis, but data, implementations, and recipes still differ between OPT, GPT-3, and other families. Matching nominal parameter counts does not fully control these variables. [Zhang et al., 2022, §2.5](https://arxiv.org/html/2205.01068v4)

Pythia made the ability to study scaling a more explicit design objective: eight sizes, each trained on both the original and a deduplicated version of the data, for 16 models in total. It controlled data order within each data version and provided 154 checkpoints per model. This lets researchers ask when a behavior emerges and whether it changes consistently with training time and model size. The trade-off is that a uniform schedule does not automatically provide compute-optimal training for every size. A suite suited to studying dynamics has not necessarily solved the optimal budget-allocation problem. [Biderman et al., 2023, §2](https://arxiv.org/html/2304.01373v2)

OLMo extended openness to data, training code, logs, checkpoints, and evaluation. Its connection to the problem addressed by Pythia is clear: testing an empirical law requires allowing others to reconstruct the process that generated its data points. **This survey's assessment** is that open model suites are part of the measurement infrastructure for scaling laws. Their scientific value should not be judged solely by their leaderboard positions at release. [Groeneveld et al., 2024](https://arxiv.org/html/2402.00838v4)

## 5. Beyond the Training Optimum: LLaMA and the New Problem of Overtraining

Chinchilla optimizes the training cost of reaching a given loss. LLaMA explicitly included inference cost in its design motivation: a smaller model may be better suited to extensive subsequent use even if it requires more pretraining tokens. Its results made training beyond Chinchilla-style ratios a practical requirement. However, cross-family performance comparisons also change data and recipes, so they are not ablations of parameter count alone. [Touvron et al., 2023, Introduction](https://arxiv.org/html/2302.13971v1)

Here, overtraining means exceeding the tokens-per-parameter ratio that is optimal for training compute. It does not mean that validation performance has already deteriorated from overfitting. Gadre et al. therefore asked whether loss retains a stable structure away from the optimal frontier. They measured 104 models with 11M–6.9B parameters across three types of corpora, covering token multipliers $M=D/N$ from 5 to 640. Setting $\alpha=\beta=2\eta$ in the base model and substituting $M$ and $C\approx6ND$ gives

$$
L(C,M)=E+\left(aM^\eta+bM^{-\eta}\right)C^{-\eta}.
$$

This expression separates scaling compute from choosing training duration. Within the range where the fit holds, changing $M$ may primarily shift the curve's position without disrupting a common compute exponent. This is not an a priori guarantee: the approximate exponents, data recipes, and optimization settings in the experiments all require examination. [Gadre et al., 2024, §2–3](https://arxiv.org/html/2403.08540v2)

The authors also mapped validation loss to average error across a set of downstream tasks. Two boundaries matter: the task set was selected using small-model performance, and an average relationship cannot replace predictions for individual tasks, let alone automatically cover post-training. The experiments were also preceded by a hyperparameter search, so the small-model budget needed for prediction should not be described as the total cost of the study. This survey interprets the result as providing useful interpolation and extrapolation tools for deployment-oriented training, rather than establishing that arbitrarily long training yields the same returns. [Experimental setup and §6 of the original paper](https://arxiv.org/html/2403.08540v2)

## 6. Llama 3: Separating Budget Prediction from Task Prediction

The Llama 3 report illustrates how scaling laws can become a decision procedure for a large training run. The researchers trained smaller models of roughly 40M–16B parameters, spanning approximately $6\times10^{18}$ to $10^{22}$ FLOPs, found minimum losses along IsoFLOP curves, and estimated how the optimal token count changed with compute. Extrapolation suggested a configuration of about 402B parameters and 16.55T tokens; considering the flat region around the minimum, they ultimately selected 405B. This is closer to the engineering purpose of scaling laws than fitting a line after the fact: identifying candidate configurations and the basis for choosing between them before training the target model. [The Llama 3 Herd of Models, §3.2.1](https://arxiv.org/html/2407.21783v3)

Capability prediction is a separate layer. The first step fits the relationship between training compute and the negative log-likelihood of correct answers on the target task; the second maps that NLL to accuracy. The second step uses not only small models but also larger Llama 2 models as anchors, despite differences in data and tokenizers. Successful extrapolation in the report therefore validates a particular pipeline. It does not prove that all large-model tasks can be predicted precisely using only small models trained on the same distribution. [Ibid., §3.2.1](https://arxiv.org/html/2407.21783v3)

The report also exposes a hidden variable in token accounting: tokenizer improvements increased the number of characters represented by each token. Two models trained on a trillion tokens need not have processed the same amount of text. Loss comparisons must also respect their units: per-token cross-entropy over different vocabularies cannot be treated directly as the same quantity. Large-model technical reports should therefore be broken into separately testable claims, examining the controls for configuration selection, validation-loss prediction, task mapping, and systems implementation, rather than compressing the success of an entire model into “scaling works.” [Ibid., §3.1–3.3](https://arxiv.org/html/2407.21783v3)

## 7. Which Cost Should Be Optimized Next?

This line of work has advanced from a single learning curve to a conditional experimental procedure: specify the data distribution and evaluation objective, ensure comparable optimization quality across scales, fit under an explicit cost definition, and finally test on scales or tasks excluded from fitting. This procedure also explains why apparently contradictory optimal ratios may both be valid: they may optimize different training recipes or serve different deployment requirements.

For a model that will provide a long-running service, the objective must also include request volume, generation length, and hardware constraints. [T3 Architecture and Deployment](03-architecture-deployment.md) develops this topic. When training tokens no longer correspond to new useful information, the analysis must incorporate unique data volume, mixture proportions, filtering, and generation mechanisms, as discussed in [T2 Data](02-data.md). Tasks that have not yet entered a reliable extrapolation regime should retain their uncertainty, rather than having it replaced by a smoother average curve.
