---
title: "Closing the Gap Between Text and Speech Understanding in LLMs"
authors:
  - "Santiago Cuervo"
  - "Skyler Seto"
  - "Maureen de Seyssel"
  - "Richard He Bai"
  - "Zijin Gu"
  - "Tatiana Likhomanenko"
  - "Navdeep Jaitly"
  - "Zakaria Aldeneh"
date: "2025-10-15"
arxiv_id: "2510.13632"
arxiv_url: "https://arxiv.org/abs/2510.13632"
pdf_url: "https://arxiv.org/pdf/2510.13632v2"
categories:
  - "cs.CL"
  - "cs.AI"
  - "eess.AS"
tags:
  - "多模态LLM"
  - "语音理解"
  - "模态对齐"
  - "知识蒸馏"
  - "数据高效学习"
  - "模型适应"
relevance_score: 5.5
---

# Closing the Gap Between Text and Speech Understanding in LLMs

## 原始摘要

Large Language Models (LLMs) can be adapted to extend their text capabilities to speech inputs. However, these speech-adapted LLMs consistently underperform their text-based counterparts--and even cascaded pipelines--on language understanding tasks. We term this shortfall the text-speech understanding gap: the performance drop observed when a speech-adapted LLM processes spoken inputs relative to when the original text-based LLM processes the equivalent text. Recent approaches to narrowing this gap either rely on large-scale speech synthesis of text corpora, which is costly and heavily dependent on synthetic data, or on large-scale proprietary speech datasets, which are not reproducible. As a result, there remains a need for more data-efficient alternatives for closing the text-speech understanding gap. In this work, we analyze the gap as driven by two factors: (i) forgetting of text capabilities during adaptation, and (ii) cross-modal misalignment between speech and text. Based on this analysis, we introduce SALAD--Sample-efficient Alignment with Learning through Active selection and cross-modal Distillation--which combines cross-modal distillation with targeted synthetic data to improve alignment while mitigating forgetting. Applied to 3B and 7B LLMs, SALAD achieves competitive performance with a strong open-weight model across broad-domain benchmarks in knowledge, language understanding, and reasoning, while training on over an order of magnitude less speech data from public corpora.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在扩展至语音输入时出现的“文本-语音理解鸿沟”问题。研究背景是，尽管LLM在文本理解上表现出色，但为了支持更自然的语音交互，研究者尝试将文本LLM直接适配以处理语音输入（端到端方法）。然而，现有方法存在明显不足：这些语音适配的LLM在语言理解任务上的性能持续低于其纯文本版本，甚至不如将自动语音识别（ASR）与文本LLM串联的级联管道。近期缩小该鸿沟的方法要么依赖大规模文本语料的语音合成（成本高昂且严重依赖合成数据），要么需要大规模专有语音数据集（不可复现），导致缺乏数据高效的解决方案。

本文要解决的核心问题正是如何以数据高效的方式弥合这一鸿沟。作者通过分析指出，鸿沟主要由两个因素驱动：一是在适配过程中LLM对原有文本能力的“遗忘”；二是语音与文本模态之间的“跨模态错位”。基于此分析，论文提出了名为SALAD的样本高效方法，该方法结合了跨模态知识蒸馏（以原始文本LLM为教师）和针对性的合成数据选择，旨在改善模态对齐的同时减轻遗忘，从而在仅使用少量公开语音数据的情况下，使语音适配LLM在广泛领域的知识、语言理解和推理任务上达到有竞争力的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕将大型语言模型（LLM）适配到语音输入的方法，可分为以下几类：

**1. 端到端语音适配方法**：近期工作通常通过微调，使LLM能基于语音输入生成中间文本表示。这些方法依赖于在有限语音数据集上进行负对数似然最小化训练。然而，现有语音数据（如LibriHeavy、Emilia）领域覆盖狭窄，与文本语料（如FineWeb-Edu）的广泛分布形成鲜明对比，导致模型在语音理解任务上表现不佳，甚至不如级联语音识别+文本LLM的流水线系统。

**2. 弥补文本-语音理解差距的现有途径**：主要分为两类。一是**大规模语音合成方法**，通过将文本语料合成为语音来扩充数据，但成本高昂且严重依赖合成数据质量。二是**利用大规模专有语音数据集**，但缺乏可复现性。两者均数据效率低下。

**3. 本文的关联与区别**：本文指出，性能差距主要源于两个因素：**微调过程中的文本能力遗忘**和**语音与文本的跨模态未对齐**。与前述依赖海量数据的方法不同，本文提出的SALAD方法结合了**跨模态蒸馏**和**定向合成数据**，旨在以更少的数据（使用公开语料，数据量低一个数量级）实现对齐并减轻遗忘。该方法在3B和7B规模的LLM上，于知识、语言理解和推理的宽领域评测中取得了与强开源模型竞争的性能，凸显了其数据高效性优势。

### Q3: 论文如何解决这个问题？

论文通过提出名为SALAD（基于主动选择和跨模态蒸馏的样本高效对齐）的两阶段方法来解决文本-语音理解差距问题。该方法的核心思想是结合跨模态蒸馏与针对性合成数据，以在提升对齐效果的同时缓解模型在适应过程中对文本能力的遗忘。

整体框架分为两个阶段。第一阶段（在自然语音上进行蒸馏）使用自然语音数据集训练语音适应的大语言模型（P_θ），通过最小化其与原始文本模型（Q_φ）在语音数据上的蒸馏损失（ℒ_DIST）来实现初步对齐。这一阶段利用了蒸馏学习的强扩展性，直到对齐效果达到一个由固有误对齐（E）决定的平台期。

第二阶段（用于领域扩展的主动选择）旨在解决残余的误对齐问题。其创新点在于引入了一种模型引导的主动选择策略，仅合成并引入少量但关键的合成语音数据，而非依赖大规模合成。具体而言，该方法首先将一个大范围文本语料库（𝒟_web）通过句子嵌入和k-means聚类划分为K个簇。关键步骤是让模型自身定义目标分布（P_target）：通过在一个小型探测集上计算每个簇内的蒸馏损失（即误对齐程度M(c)），将误对齐程度高的簇视为“缺失”领域并赋予更高权重。随后，根据此重要性权重（w_γ(c) ∝ M(c)^γ）按比例采样簇，并从被选中的簇中均匀选取文本来合成语音，形成一个主动数据集（𝒟_active）。参数γ控制了对高误对齐簇的关注程度。最后，将主动数据集与第一阶段的自然语音数据结合，继续通过最小化蒸馏损失来训练模型，以防止遗忘。

主要模块包括：1）跨模态蒸馏模块，用于对齐语音和文本表示；2）聚类与重要性采样模块，用于识别和选择信息量最大的文本进行合成；3）合成数据注入与联合训练模块。SALAD的创新点在于：1）将问题根源归结为遗忘和跨模态误对齐；2）提出了数据高效的二阶段方案，显著减少了对大规模合成数据的依赖；3）设计了由模型自身误对齐信号驱动的主动选择机制，实现了对“缺失”领域的精准补充。实验表明，该方法在仅使用公开语料库且训练数据量少一个数量级的情况下，使3B和7B模型在知识、语言理解和推理等广泛领域基准测试中达到了与强开源模型竞争的性能。

### Q4: 论文做了哪些实验？

论文通过一系列实验分析了文本-语音理解差距的成因，并验证了所提方法SALAD的有效性。实验设置方面，研究基于Qwen2.5-3B/7B基础模型，采用包含语音编码器、适配器和语言模型的架构，其中编码器固定，适配器和语言模型可训练。训练目标通过参数α在最大似然损失和跨模态蒸馏损失之间进行插值。数据集使用了两个公开的自然英语语音语料库LibriHeavy（朗读语音）和Emilia的YODAS-EN子集（对话语音），并合成了一个高质量广域文本语料库FineWeb-Edu的10B词符语音版本用于研究领域匹配的影响。评估在多个广域基准测试上进行，包括StoryCloze、MMSU、OpenBookQA、HellaSwag、ARC-Challenge和PIQA，均采用少样本提示和准确率作为指标。

对比方法主要涉及不同训练目标（α取值0、0.25、0.5、0.75、1）和不同训练数据（窄域语音数据 vs. 广域合成语音数据）的组合。关键发现包括：跨模态失准与语音性能显著负相关（留一交叉验证R²=0.75），而遗忘与文本性能显著负相关（R²=0.74）。部分R²分析显示，在控制遗忘后，失准单独解释了约56%的语音性能方差；在控制失准后，遗忘单独解释了约32%的文本性能方差。实验结果表明，纯最大似然训练（α=0）在窄域数据上会导致失准随训练规模增加而上升，性能最差；而跨模态蒸馏（α>0）能有效降低失准，其缩放规律符合典型的对数线性神经缩放定律。例如，当α=1时，在窄域数据上训练，失准可降至0.13，但需要约47.58B词符才能接近其不可约失准E的5%以内；而在广域数据上使用蒸馏（α=1），不可约失准E可低至0.04。此外，即使使用广域数据匹配，最大似然训练也无法获得有意义的缩放收益，而结合领域匹配的蒸馏则能实现最低的失准和最佳的语音理解性能。这些结果为SALAD方法的设计提供了依据，使其能够在仅使用少量公开语音数据的情况下，在知识、语言理解和推理基准上达到与强大开源模型竞争的性能。

### Q5: 有什么可以进一步探索的点？

本文提出的SALAD方法在减少数据依赖方面取得了进展，但仍存在一些局限性和值得深入探索的方向。首先，该方法主要关注通用领域的语言理解任务，对于包含丰富副语言信息（如情感、语调、口音）的对话或交互式场景，其跨模态对齐的有效性尚未验证。其次，主动选择策略依赖于聚类和预合成探针数据，计算开销和合成质量可能影响效率；未来可探索更轻量的不确定性采样或基于梯度的数据选择方法。此外，论文仅评估了3B和7B模型，更大规模LLM的适应过程可能面临不同的遗忘和对齐挑战，值得系统研究。从更广的视角看，文本-语音差距的根源可能超越领域覆盖，涉及模态固有的信息差异（如语音的时序模糊性），未来可结合语音增强或混合模态表示学习来建模这种差异。最后，SALAD依赖文本教师模型进行蒸馏，若教师存在偏见或错误，可能限制性能上限；探索自监督对齐或引入人类反馈或许能进一步提升鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对语音适配大语言模型在语言理解任务上表现不及纯文本模型甚至级联系统的问题，提出了“文本-语音理解差距”的概念。核心贡献在于深入分析了该差距的两个成因：模型适配过程中对文本能力的遗忘，以及语音与文本模态间的错位。为解决此问题，论文提出了一种名为SALAD的数据高效方法，该方法结合了跨模态蒸馏和有针对性的合成数据生成，旨在增强模态对齐并减轻遗忘。实验表明，在仅使用少量公开语音数据的情况下，SALAD方法能使3B和7B参数规模的模型在知识、语言理解和推理等广泛领域的基准测试中，达到与强大开源模型相竞争的性能。这项工作为以数据高效的方式弥合文本与语音理解差距提供了新的思路和可行方案。
