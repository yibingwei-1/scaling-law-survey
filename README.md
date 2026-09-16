# Scaling Law Survey: A Problem-Driven Review

**English** | [**简体中文**](README-zh.md)

**Living survey · Updated September 16, 2026 · [GitHub repository](https://github.com/yibingwei-1/scaling-law-survey)**

Scaling-law research repeatedly uncovers what an existing resource model leaves out, then revisits how resources should be allocated. This survey follows that development from predictable training returns and parameter–data allocation to effective data, sparse architectures, deployment costs, post-training, inference-time computation, and capability measurement.

Each research thread follows **the original problem → the central insight → the mechanism → experimental evidence → remaining limitations → subsequent branches**. Connections distinguish direct responses, parallel approaches, and the survey's own synthesis.

**Edition status:** The Chinese manuscript and PDF are available. The full English manuscript is being translated and checked. This English README is the default repository homepage; a complete LaTeX build is not yet available.

**[Chinese survey](SURVEY.zh-CN.md)** · **[Chinese PDF](output/pdf/scaling-law-survey.zh-CN.pdf)** · [References and versions](REFERENCES.md) · [Research map](docs/research-map.md) · [Coverage audit](docs/evidence-map.md) · [BibTeX](references.bib)

![A conceptual map of scaling-law research](figures/evolution-map.png)

The figure summarizes relationships between research problems; it is not an experimental plot.

## Seven Research Threads

The chapter links below currently open the Chinese edition.

| Chapter | Question driving the research | Main trajectory |
|---|---|---|
| [1. Predictability and budgets](docs/01-predictability-budget.md) | How can we predict returns before training, and why does the optimal allocation change? | Learning curves → Kaplan → Chinchilla → reanalysis, hyperparameter transfer, and training recipes |
| [2. Effective data](docs/02-data.md) | How can scaling continue when data are limited, unequal in value, or drawn from changing distributions? | Repetition → deduplication and selection → DoReMi / RegMix → synthesis and information retention |
| [3. Architecture and deployment](docs/03-architecture-deployment.md) | Why do parameter counts and FLOPs fail to capture practical cost on their own? | Routing and MoE → memory, I/O, and caching → long context → lifecycle optimization |
| [4. Post-training and RL](docs/04-posttraining.md) | How do we turn available candidate solutions into reliable policies, and when do learning signals fail? | Self-training → feedback and verification → GRPO and successors → overoptimization, coverage, and curricula |
| [5. Inference-time computation](docs/05-inference.md) | Should additional computation go to longer reasoning, resampling, search, or verification? | CoT and multiple samples → search and PRMs → difficulty-dependent budgets → distillation and latent depth |
| [6. Theory and capability evaluation](docs/06-theory-evaluation.md) | Where do power laws come from, and how does loss relate to usable capabilities? | Mechanisms → feature learning → emergence and measurement → extrapolation and generalization limits |
| [7. Multimodality and interaction](docs/07-multimodal.md) | Which resource dimensions matter when modalities and feedback change? | Vision scaling → image–text supervision and mixtures → diffusion computation → robotics and environmental coverage |

The survey also includes an [introduction](docs/introduction.md), a [community discussion radar](docs/04-community-radar.md), and a [cross-thread synthesis](docs/conclusion.md). Chapters retain variable definitions, comparison protocols, experimental conditions, and open questions, while separating established foundations from preliminary findings.

## Research Method and Reference Design

The organization draws on [JonnesLin/post-training-survey](https://github.com/JonnesLin/post-training-survey). We read its Chinese preface, introduction, seven chapters, conclusion, and design and implementation documents, and checked its 468 bibliography entries against 440 unique citation keys used in the Chinese chapters. We adopt its problem-driven structure, depth hierarchy, and cross-thread connections while checking technical claims against their primary sources. See the [method analysis](docs/00-reference-method.md) and the [separate review of research organization and repository architecture](docs/reference-repository-analysis.md), both currently in Chinese.

The initial edition contained 45 primary sources and three compressed technical chapters. The expanded edition has seven technical chapters, approximately 36,600 Chinese characters, and 161 distinct primary-source records, of which 151 are cited in the technical chapters. Catalog size, actual citation coverage, and reading depth are reported separately. Abstract-only candidates are not counted as close readings. Exact figures are available in the [coverage map](docs/evidence-map.md) and [machine-readable audit](data/citation-audit.json).

## Community Discovery and Evidence

The repository records 18 traceable items from X, YouTube, and Reddit, including author announcements, research talks, engineering reproductions, and rebuttals. Engagement records retain observation dates and retrieval limitations; unavailable values remain `null`, and search-index snapshots are not presented as live rankings. Discussions identify questions and disagreements; papers, author experiments, and technical reports support technical judgments. See the [community radar](docs/04-community-radar.md).

The main focus is language models, with theory, vision, diffusion, and robotics used to examine assumptions and boundaries. Searches extend through September 16, 2026, without a claim of exhaustive coverage. The survey does not independently reproduce the cited experiments. Individual records retain reading scope, version information, and limitations; selected 2026 results are distinguished from established findings.

## Maintenance

A Codex maintenance task is scheduled for Mondays at 09:00 in `America/Los_Angeles`. It searches papers, author blogs, technical reports, and the three community platforms, then updates the narrative, source records, PDF, and repository after verification. Notifications are reserved for substantive changes, failures, or required user action. Execution depends on the local task environment. See [UPDATING.md](UPDATING.md) for the maintenance procedure, currently documented in Chinese.

- [Research and writing methodology](METHODOLOGY.md)
- [Changelog](CHANGELOG.md) and [publication status](PUBLISHING.md)
- [Source records](sources/) and [maintenance state](data/state.json)

```bash
python3 scripts/build_survey.py
python3 scripts/validate.py
# PDF dependencies: reportlab, Pillow, pypdf; matplotlib for display mathematics
python3 scripts/build_pdf.py --check
```

The technical chapters in `docs/` and verification records in `sources/` are maintained sources. The complete manuscript, reference index, citation audit, and PDF are generated artifacts. Original papers, community posts, and the reference repository remain the work of their respective authors; this repository distributes its own synthesis and links, not third-party full texts.
