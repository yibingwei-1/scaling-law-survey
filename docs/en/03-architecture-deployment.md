# T3 Architecture and Deployment: Why Do Parameters, FLOPs, GPU Memory, and Actual Costs Evolve Separately?

> Verification date: 2026-09-16. Scope: sparse experts, training parallelism, exact-attention implementations, KV representations and serving, long context, and lifecycle budgets. This chapter discusses algorithmic cost, hardware performance, and model quality separately; acceleration factors reported in individual papers are not treated as constants that generalize across hardware. See the [foundational sources](../../sources/foundations.json) and [additional sources](../../sources/expansion-foundations.json) for original sources and reading depth. No systems benchmarks were run.

## 1. When Parameters Need Not Be Activated, Scaling Laws Need New Coordinates

In dense models, parameter count usually represents both storage capacity and per-token computation. MoE breaks this coupling: a model can contain many experts while activating only a few for each token. Doubling model size therefore no longer implies doubling computation per step. Architecture comparisons must distinguish at least total parameters, active parameters, data volume, FLOPs, memory, and communication. The relationships below are this survey's accounting distinctions, not a claim that these quantities already share a universal conversion factor.

GShard combined conditional computation with automatic sharding compilation, distributing experts across devices. Its multilingual translation experiments demonstrated the possibility of expanding capacity while increasing computation more slowly. They also showed that parameter sparsity does not eliminate systems complexity: routing, cross-device data movement, and compilation at scale still need to be handled. These results concern multilingual translation and cannot be transferred without qualification into claims about equal-budget gains for general-purpose autoregressive language models. [Lepikhin et al., 2020, §1–3](https://arxiv.org/html/2006.16668v1)

Switch Transformers directly simplified routing: each token selects one expert rather than several, reducing routing and communication, while selective high precision mitigates numerical instability in the router. Expert capacity requires buffer space; too little causes overflow tokens to be dropped, while too much wastes computation and memory. Its T5-style objective, C4 data, and TPU comparisons establish measurable speed–quality trade-offs, rather than proving that per-step cost remains constant no matter how many experts are added. [Fedus et al., 2021/2022, §2](https://arxiv.org/html/2101.03961v3)

### From Runnable Architectures to Predictable Configurations

Clark et al. separated active computation from total capacity to study shared regularities in routed language models, but their main experiments fixed training at 130B tokens and did not jointly optimize data volume. Fine-Grained MoE explicitly identified this limitation and brought tokens, parameters, and expert granularity into joint optimization. Finer experts increase the flexibility of combinations, but also add routing overhead. This chain has evidence of direct inheritance and shows why a sparse-model scaling law cannot be obtained merely by replacing the parameter count in a dense formula with active parameters. [Clark et al., 2022](https://arxiv.org/html/2202.01169); [Scaling Laws for Fine-Grained Mixture of Experts, 2024](https://arxiv.org/html/2402.07871)

Mixtral demonstrated how this architecture could enter open autoregressive models: two of eight experts are selected per layer, with roughly 47B total parameters and 13B active parameters per token. The report explicitly notes that serving memory depends on total parameters, while routing and memory access also affect device utilization; batched workloads more readily achieve higher arithmetic intensity. Describing its deployment cost simply as that of a 13B model therefore omits major constraints. [Jiang et al., 2024, §2 and §3](https://arxiv.org/html/2401.04088v1)

## 2. Landmark: DeepSeekMoE Moves from More Capacity to More Useful Experts

When conventional experts are coarse-grained, one expert may handle unrelated knowledge, while several experts may redundantly learn information needed everywhere. DeepSeekMoE addresses these two issues through fine-grained segmentation and shared experts. It reduces each expert's intermediate dimension to $1/m$ of its original size, increases the number of experts to $mE$, and correspondingly increases the number activated per token to $mk$, aiming to keep total expert parameters and active computation comparable. Of these $mk$ active slots, it then reserves $|S|$ for always-active shared experts handling common knowledge, selecting only $mk-|S|$ non-shared experts each time. Shared experts consume part of the existing activation budget. [Dai et al., 2024, §3](https://arxiv.org/html/2401.06066v1)

Omitting residual connections and normalization, the layer output can be illustrated as

$$
y(x)=\sum_{s\in S}f_s(x)+
\sum_{i\in \mathrm{Top}_{mk-|S|}(g_{\bar{S}}(x))}g_i(x)f_i(x).
$$

$S$ is the shared-expert set, and $\bar{S}$ contains the remaining, non-shared experts; the second term selects $mk-|S|$ paths only from the non-shared set. The idea is not to equate the number of combinations with capability. It is to assign common and specialized content to different paths while allowing specialized paths to combine more flexibly. The original paper conducted architectural ablations in a roughly 2B-parameter, 100B-token setting before scaling to 16B parameters and 2T tokens. Comparisons with dense references trained on the same corpus come closer to isolating the architectural benefit than cross-company model leaderboards do. [§4–5 of the original paper](https://arxiv.org/html/2401.06066v1)

Two limitations remain. First, expert removal and performance ablations can provide evidence of specialization, but cannot prove that every expert has a clear, independent semantic responsibility recognizable to humans. Second, the paper uses a dense model with the same total parameter count as a strong reference; this survey does not call it a strict performance upper bound for every task and training budget. Finer experts can also cause a token to contact more devices, so matching parameters and FLOPs does not eliminate communication differences.

### Direct Successor V2: Once the FFN Becomes Cheaper, KV and Communication Become Bottlenecks

DeepSeek-V2 explicitly inherits this expert structure while addressing two new constraints. Its fine-grained routing controls communication by limiting the number of devices involved in processing a token. On the attention side, it introduces MLA, jointly compressing keys and values into a low-dimensional latent representation. Let the cached latent dimension per layer be $d_c$, the key dimension dedicated to positional encoding be $d_R$, and the number of layers be $\ell$. Its cache contains approximately $(d_c+d_R)\ell$ elements per token, reducing storage relative to the standard multi-head cache of $2h d_h\ell$ elements. [DeepSeek-V2, §2](https://arxiv.org/html/2405.04434v5)

One mechanism deserves close reading. If the up-projections in a low-rank compression can be absorbed into the query/output matrices, the full KV representation need not be reconstructed each time. RoPE's position-dependent transformations, however, disrupt this matrix rearrangement. V2 therefore decouples the position-dependent component rather than merely claiming that low-rank KV is sufficient. This also explains why MLA's benefits should be verified together with its architecture and implementation. The reported cache reductions and throughput gains are not automatically plug-and-play results for arbitrary models. [Ibid., §2.1.2–2.1.3](https://arxiv.org/html/2405.04434v5)

### Direct Successor V3: Load Balancing Itself Can Interfere with the Model Objective

V3 retains MLA and DeepSeekMoE but moves the main expert load-balancing mechanism outside the auxiliary loss. It adjusts routing biases according to expert overload or underload, using those biases to affect selection while retaining the original affinity scores as the weights for expert outputs. It is important to specify that a small sequence-level auxiliary balancing loss remains. “Auxiliary-loss-free” should not be interpreted as the complete absence of balancing terms from the training objective. [DeepSeek-V3, §2.1](https://arxiv.org/html/2412.19437v2)

Its larger-scale implementation also combines FP8, DualPipe, and inter-node communication optimizations. The evidence establishes that the complete recipe can run, supported by local ablations; it does not fully isolate the contribution of every component. The reported 2.788M H800 GPU hours cover the official training stages and correspond to roughly USD 5.576M at the assumed rental price, explicitly excluding preliminary research and ablations. This figure cannot be described as the project's total research and development cost, nor can it be derived solely from the active-parameter ratio. [Ibid., Table 1 and §3](https://arxiv.org/html/2412.19437v2)

## 3. Fitting a Model into Memory Does Not Mean the Cluster Runs It Quickly

The systems branch faces another limitation: even if the algorithmic budget permits a larger model, a single device may lack memory for its parameters, gradients, and optimizer states. Megatron-LM exploits the structure of Transformer layers for tensor parallelism, reducing redundant communication in naive partitioning, and combines it with data parallelism. In its 8.3B-parameter, 512-GPU experiment, approximately 76% refers to scaling efficiency relative to the selected single-GPU baseline, not to achieving 76% of theoretical peak hardware performance. This distinction directly affects how a paper's FLOPs translate into procurement or operating budgets. [Shoeybi et al., 2019/2020](https://arxiv.org/html/1909.08053v4)

ZeRO instead addresses replicated storage in data parallelism. It progressively shards optimizer states, gradients, and parameters, allowing the cluster's aggregate memory to serve one model more efficiently. It does not make all communication free or eliminate every activation and temporary-buffer overhead. A discussion of theoretically accommodating a trillion parameters and evidence of completed training at that scale represent different levels of evidence. ZeRO can be combined with tensor parallelism because they address different memory and communication bottlenecks. [Rajbhandari et al., 2019/2020](https://arxiv.org/html/1910.02054v3)

This survey treats such work as defining the feasible region for scaling experiments. A mathematically better $N,D$ configuration may run more slowly than a FLOPs-suboptimal configuration if it forces the model across low-bandwidth links, into overly small microbatches, or through frequent recomputation. Comparisons of training optima should therefore specify whether they optimize an ideal arithmetic budget or an actual budget for a particular cluster and deadline. The former cannot automatically stand in for the latter.

## 4. Landmark: Why Can FlashAttention Do More Arithmetic Yet Run Faster?

Standard attention computes $QK^\top$, softmax, and multiplication by $V$. Conventional implementations write a quadratically sized intermediate matrix to high-bandwidth memory, or HBM, and then read it back. On GPUs, this data movement can cost more than some arithmetic. FlashAttention therefore begins by reorganizing exact computation rather than changing the model approximation: it places input tiles in faster on-chip SRAM and maintains global normalization with an online softmax. [Dao et al., 2022, §2–3](https://arxiv.org/html/2205.14135v2)

The key to the online computation is that statistics from two blocks can be merged. If the old block's maximum and exponential sum are $m,\ell$, and the new block's are $\tilde m,\tilde\ell$, the merged statistics are

$$
m'=\max(m,\tilde m),\qquad
\ell'=e^{m-m'}\ell+e^{\tilde m-m'}\tilde\ell.
$$

Rescaling the accumulated output accordingly removes the need to store the full attention matrix in HBM. During backpropagation, the necessary intermediate results are recomputed from the input blocks. Arithmetic work can increase, yet reduced reads and writes make execution faster. This remains exact attention with quadratic arithmetic complexity and should not be conflated with linear attention. [Ibid., Algorithm 1 and Theorems 1–2](https://arxiv.org/html/2205.14135v2)

For BERT-large at sequence length 512, the paper reports roughly 15% end-to-end acceleration relative to the then-current MLPerf 1.1 training record. For GPT-2 at length 1K, it reports approximately 3× acceleration relative to its selected implementation. These factors depend on sequence length and baseline; they are not common gains for all Transformers. The analysis explicitly includes SRAM capacity in IO complexity and does not claim identical benefits on every GPU or at every head dimension. [§4.1 of the original paper](https://arxiv.org/html/2205.14135v2)

**This survey's assessment** is that this work changes the interpretation of cost in scaling laws. The same model, tokens, and theoretical FLOPs can incur different wall-clock costs because memory access is organized differently. This must be recorded separately from improvements in the model's statistical efficiency.

### Direct Successor FlashAttention-2: One IO Optimization Does Not Remove Every Bottleneck

The second generation found that the first was still limited by thread-block occupancy, shared-memory communication between warps, and non-matrix operations. It reduces non-matrix FLOPs such as normalization, adds parallelism along the sequence dimension, and redistributes work among warps. Roughly 2× attention-kernel acceleration and higher peak utilization on A100 demonstrate that the same FLOP count still does not imply the same time per FLOP. [Dao, 2023, §3–4](https://arxiv.org/html/2307.08691v1)

This explicit successor chain does not replace an incorrect algorithm with a correct one; it removes successive systems bottlenecks while preserving exact outputs. It also leaves a new boundary: a kernel-level speedup does not directly yield an equally large speedup for the entire training run. Other layers, communication, the optimizer, and data loading still consume time. Survey updates should record hardware, tensor shapes, precision, baseline versions, and whether measurements are kernel-level or end-to-end, rather than retaining only a speedup factor.

## 5. Serving Has Two Memory Bottlenecks: Storage per Token and Wasted Capacity

Autoregressive decoding repeatedly reads the KV states of previous tokens, giving it different resource characteristics from prefill, which can process input tokens in parallel. MQA lets different query heads share one set of keys and values, reducing cache and bandwidth requirements while changing the model's representational capacity. GQA directly extends this approach by grouping query heads and sharing KV within each group. It offers a compromise between standard multi-head attention and a single shared group, and also studies converting existing multi-head checkpoints through mean pooling followed by further training. [Shazeer, 2019](https://arxiv.org/html/1911.02150v1); [Ainslie et al., 2023, §2–3](https://arxiv.org/html/2305.13245v3)

Ignoring buffers and other overheads, for batch size $B$, context length $T$, layer count $\ell$, KV head count $h_{\rm KV}$, head dimension $d_h$, and bytes per element $b$, KV storage can be written as

$$
M_{\rm KV}\approx 2BT\ell h_{\rm KV}d_h b.
$$

This survey derives the expression from tensor shapes to illustrate the interactions among longer context, larger batches, fewer KV heads, and precision changes. GQA's conversion result using 5% additional training compute comes from its particular model settings; it does not guarantee lossless conversion of arbitrary checkpoints. MLA further changes this accounting through the different low-dimensional representation described above.

PagedAttention addresses an orthogonal problem. Even if the KV size per token is unchanged, reserving contiguous space for requests of different lengths creates fragmentation and unused capacity. It divides KV into fixed-size blocks, allocates them on demand, permits noncontiguous storage and prefix sharing, and uses vLLM's scheduling to increase the batch size that can be served. Its benefit is more effective use of space, not compression of each token's representation. [Kwon et al., 2023, §1–4](https://arxiv.org/html/2309.06180v1)

MQA/GQA/MLA can therefore be combined with paged management: the former change representation, while the latter changes allocation. Both must nevertheless be evaluated against the workload. Long requests, diverse generations, shared prefixes, low-latency single requests, and large offline batches benefit differently. Pope et al.'s inference analysis considers parallel layouts, batch size, context, and latency requirements together, studying input processing and token-by-token generation separately. The highest-throughput configuration may fail an interactive latency requirement, and the lowest-latency configuration may not minimize cost per token. [Efficiently Scaling Transformer Inference, 2022](https://arxiv.org/html/2211.05102v1)

## 6. Context Scaling: Fitting the Window Does Not Mean Using the Information Well

Even after improving attention implementations, long context still requires compatible training distributions and positional mechanisms. Xiong et al. continued pretraining from Llama 2 checkpoints for approximately 400B tokens, adjusting positional encoding, long-sequence settings, and data mixtures. Smaller models used a longer training window, while larger models used another length to control costs. This provides empirical evidence for extending short-context models while also showing that enlarging the window is not a free configuration change. [Effective Long-Context Scaling of Foundation Models, §2 and §4](https://arxiv.org/html/2309.16039v3)

In comparing data mixtures, the paper found that text quality and the training recipe could matter more than simply increasing the proportion of long documents. The survey should not compress these results into a claim that adding long documents is sufficient. Different tasks require retrieval, integration, or reasoning across passages and need separate evaluation. The bottleneck has shifted from whether memory can hold the sequence to whether training teaches the model to use the additional information effectively. [Ibid., data and training-curriculum ablations](https://arxiv.org/html/2309.16039v3)

Mamba takes a different architectural branch. Instead of using attention to retain the full history for item-by-item retrieval, it selectively updates a state using input-dependent state-space parameters. Its basic form is $h_t=\bar A_t h_{t-1}+\bar B_t x_t,\ y_t=C_t h_t$; selection makes information retention content-dependent. A hardware-friendly scan addresses the computational problem created when input-dependent parameters invalidate the fixed convolutional form. The trade-off is that history is compressed into a finite state. Linear sequence complexity does not automatically guarantee fine-grained retrieval equivalent to attention. [Gu & Dao, 2023/2024, §2–3 and §5](https://arxiv.org/html/2312.00752v2)

The original report studies sequence modeling across language, DNA, and audio. Results involving million-length sequences cannot be recast as million-token general-purpose language understanding without distinguishing modalities. **This survey's synthesis** is that long-context research should jointly measure at least length, information density, tasks assessing effective use, and execution cost. A model's maximum supported window is only one condition and cannot by itself represent the scale of its capabilities.

## 7. Deployment Objectives Ultimately Feed Back into Pretraining

Sardana et al. add inference demand to a Chinchilla-style objective. If a model will be used extensively, the serving savings of a smaller model can compensate for longer pretraining. At sufficiently high demand, a smaller model trained on more data can minimize total cost. However, curves fitted over conventional tokens-per-parameter ranges may also overestimate the benefit of additional data in the regime of extremely long training. [Beyond Chinchilla-Optimal, 2023/2024](https://arxiv.org/html/2401.00448)

A simplified dense-model accounting expression illustrates this change:

$$
C_{\rm life}\approx6ND_{\rm train}+2ND_{\rm infer}.
$$

It omits attention length, the prefill/decode distinction, memory, communication, and hardware utilization, and serves only to explain why the objective changes. Thus, [overtraining in T1](01-predictability-budget.md) and [data curricula in T2](02-data.md) are not exceptions to scaling laws; they reallocate resources under new demand constraints. If post-training causes a model to generate longer reasoning for each request, the inference budget changes again.

The shared conclusion this survey draws from these lines of work is that systems innovation can make previously infeasible configurations feasible, architectural innovation can change the relationship between capacity and cost, and deployment demand can change what counts as optimal. The most valuable updates from subsequent papers identify which constraint was revised, which controls establish the net benefit, and where the next bottleneck appears. Reporting more total parameters, fewer active parameters, or higher throughput in one experiment is insufficient to establish that argument.
