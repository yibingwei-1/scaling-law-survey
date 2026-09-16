# Variables, Metrics, and Cost Conventions

The equations in this survey explain mechanisms and support experimental comparisons. The same symbol can have different definitions in different papers; the conventions below are reading aids, not replacements for the original definitions.

| Symbol or metric | Convention in this survey | Conditions that comparisons must retain |
|---|---|---|
| $N$ | Number of model parameters | Whether embeddings are included; report both total and active parameters for sparse models |
| $D$ | Total training tokens processed | Tokenizer, unique data, repeated epochs, and context length |
| $U$ | Size of the unique training data | Token, document, and semantic deduplication define different quantities |
| $C$ | Compute budget with a stated accounting boundary | Whether training or inference, forward and backward passes, routing, verifiers, tools, and data generation are included |
| $L$ | Loss under a specified distribution and scoring rule | Cross-entropy, normalized error, and FID cannot directly share fitted parameters |
| $Q$ | Number of requests over the model's lifecycle | Request length, concurrency, target quality, hardware, and latency requirements |
| pass@1 | Probability, or an estimate, that one sample is correct | Sampling temperature, prompt, length limit, and checker |
| pass@k | Probability, or an estimate, that at least one of $k$ candidates is correct | Usually evaluated using a checker; does not imply that a deployed selector can identify the correct candidate |
| maj@k | Accuracy after majority aggregation of candidate answers | Answer normalization, correlated errors, and tie handling |
| best-of-N | A strategy that selects candidates with a scorer | $N$ is a strategy hyperparameter; final accuracy depends on both the generator and scorer |
| GPU-hours | Total time occupying accelerators | Device type, utilization, precision, communication, and waiting overhead |
| Latency / throughput | Waiting time per request / completed work per unit time | Batching can make their optimization objectives diverge |

The common language-model approximation $C_{\mathrm{train}}\approx 6ND$ is a training-cost model for dense Transformers. Estimating inference compute from parameters and generated tokens likewise has conditions. Long-context attention, KV caches, prefill and decode, sparse routing, and hardware utilization require separate examination. Two systems generating the same token count do not necessarily use equal computation, cost, or time. [Chinchilla](https://arxiv.org/abs/2203.15556); [HF experiments on inference compute with open models](https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute).

“Compute-optimal” must specify both the objective and constraints. Minimizing validation loss at fixed training FLOPs, maximizing quality at fixed model size, and minimizing lifecycle cost for a specified serving demand are three different problems. [Beyond Chinchilla-Optimal](https://arxiv.org/abs/2401.00448).

“Overtraining” here means training beyond a particular training-compute-optimal allocation; it does not automatically imply statistical overfitting. “Emergence” describes the shape of change under a measurement procedure; it does not by itself prove a discrete transition in an internal mechanism. Nor does every larger model with a higher score establish a “scaling law”: a meaningful relationship also needs resource definitions, multiple scales, a functional form, a fitting range, and extrapolation tests. [Schaeffer et al.](https://arxiv.org/abs/2304.15004).

“Capability boundaries” are particularly easy to conflate. Failure within a finite sampling budget means success was not observed under that protocol and budget; it does not prove that the probability of a correct solution is exactly zero. Conversely, one success after enormous sampling does not establish reliable delivery within a practical budget. The text therefore discusses candidate coverage, candidate selection, and final reliability separately. [Research on RL capability boundaries](https://arxiv.org/abs/2504.13837); [inference-time compute allocation](https://arxiv.org/abs/2408.03314).
