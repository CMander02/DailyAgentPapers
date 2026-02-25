---
title: "Context Shapes LLMs Retrieval-Augmented Fact-Checking Effectiveness"
authors:
  - "Pietro Bernardelle"
  - "Stefano Civelli"
  - "Kevin Roitero"
  - "Gianluca Demartini"
date: "2026-02-15"
arxiv_id: "2602.14044"
arxiv_url: "https://arxiv.org/abs/2602.14044"
pdf_url: "https://arxiv.org/pdf/2602.14044v2"
categories:
  - "cs.CL"
tags:
  - "LLM 能力评估"
  - "检索增强生成 (RAG)"
  - "事实核查"
  - "上下文处理"
  - "提示工程"
relevance_score: 5.5
---

# Context Shapes LLMs Retrieval-Augmented Fact-Checking Effectiveness

## 原始摘要

Large language models (LLMs) show strong reasoning abilities across diverse tasks, yet their performance on extended contexts remains inconsistent. While prior research has emphasized mid-context degradation in question answering, this study examines the impact of context in LLM-based fact verification. Using three datasets (HOVER, FEVEROUS, and ClimateFEVER) and five open-source models accross different parameters sizes (7B, 32B and 70B parameters) and model families (Llama-3.1, Qwen2.5 and Qwen3), we evaluate both parametric factual knowledge and the impact of evidence placement across varying context lengths. We find that LLMs exhibit non-trivial parametric knowledge of factual claims and that their verification accuracy generally declines as context length increases. Similarly to what has been shown in previous works, in-context evidence placement plays a critical role with accuracy being consistently higher when relevant evidence appears near the beginning or end of the prompt and lower when placed mid-context. These results underscore the importance of prompt structure in retrieval-augmented fact-checking systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究大型语言模型在基于检索增强的事实核查任务中，上下文结构如何影响其性能。研究背景是虚假信息泛滥带来的社会挑战，传统人工核查方式难以应对，而具备强大推理能力的LLMs为自动化事实核查提供了新机遇。然而，现有方法存在明显不足：尽管LLMs在多种任务上表现出色，但其在处理长上下文时性能并不稳定，先前研究多关注问答任务中的“中间上下文退化”现象，而在事实核查这一更复杂的任务中（常需综合或调和冲突信息），上下文长度和证据位置的具体影响尚未得到充分探索。

本文要解决的核心问题是：在检索增强的事实核查系统中，当LLMs需要处理包含外部证据的长文本提示时，上下文的结构性因素（如总长度和关键证据在提示中的位置）如何塑造模型的核查准确性。具体通过三个研究问题展开：1）仅凭参数知识（无外部证据），LLMs能多大程度上独立验证事实声明；2）上下文长度如何影响事实核查的准确率；3）相关证据在提示中的位置（开头、中间或结尾）对准确率有何影响。研究发现，模型虽具备一定的参数化事实知识，但准确率普遍随上下文增长而下降，且证据置于提示开头或结尾时性能显著优于置于中间，这凸显了提示结构在构建高效检索增强事实核查系统中的关键作用。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**自动化事实核查系统**和**大语言模型的长上下文处理能力**。

在**自动化事实核查**方面，早期研究确立了“声明识别、证据检索、裁决生成”的三步框架。该领域经历了从基于规则的系统到深度学习（如使用双向LSTM的DeClarE模型），再到基于Transformer的模型（如BERT）的演进，后续的GEAR、KGAT等框架进一步增强了多证据推理能力。本文的研究建立在此基础之上，但聚焦于LLM如何利用其先验知识和处理长上下文的能力来支持裁决生成，特别是探讨如何有效引导和约束LLM的推理以产生可靠结论，这与近期旨在通过检索增强架构或参数化知识来减少幻觉的研究方向一致。

在**大语言模型的长上下文处理**方面，先前研究指出LLM存在“中间上下文退化”现象，即模型对出现在输入中间位置的信息利用效率较低，而在开头或结尾附近性能更佳（“迷失在中间”效应）。现有评测基准多关注检索而非复杂推理任务。本文的工作将这一研究方向延伸至事实核查领域，专门评估上下文长度和证据位置对模型验证准确性的影响，从而补充了现有对长上下文推理能力评估的不足。

### Q3: 论文如何解决这个问题？

论文通过设计一套严谨的控制实验来系统性地研究上下文长度和证据位置对LLM事实核查性能的影响。其核心方法是隔离不同变量，以量化每个因素的具体效应。

整体框架基于三个常用的事实核查数据集（HOVER、FEVEROUS、ClimateFEVER），并选取了不同规模和家族的指令微调开源模型（如Llama-3.1、Qwen2.5、Qwen3）作为评估对象。实验流程主要分为三个关键阶段，构成了方法的主要模块：

首先，建立**参数知识基线**。模型仅接收待核查的声明文本，不提供任何检索证据，直接进行分类。此模块用于评估模型依赖内部记忆知识的程度，并为后续实验提供比较基准。

其次，引入**证据访问实验**。将与声明相关的所有证据句子拼接成一个证据块，与声明一同提供给模型。此模块旨在量化显式提供证据相对于仅依赖参数知识的整体性能增益。

最后，进行系统的**上下文效应分析**。这是方法的核心创新部分，通过控制两个变量来分离影响：(i) **总上下文长度**，设置了2K、4K、8K、16K四种长度；(ii) **证据块在提示中的相对位置**，将其放置在从0%（开头）到100%（结尾）之间均匀分布的11个位置上。为了精确控制输入大小效应并隔离位置影响，证据块被嵌入到由无关填充文本（如维基百科的虚拟段落）构成的上下文中。这样，任何性能差异都主要由证据的相对深度（位置）驱动，而非内容变化。对每个模型评估所有长度和位置的组合（共44种配置），从而能够清晰辨别长上下文是否导致准确性下降，以及证据有效性是否依赖于其在提示中的位置。

关键技术在于通过引入中性填充文本来构建受控的上下文环境，使得研究者能够纯粹地分析“上下文长度”和“证据位置”这两个结构变量的影响，而非证据内容本身的质量或相关性。这种实验设计创新性地揭示了在检索增强的事实核查系统中，提示的结构（特别是证据放置于开头、中间还是末尾）对模型性能起着至关重要的作用，准确率在证据位于上下文两端时较高，在中部时则显著降低。

### Q4: 论文做了哪些实验？

本论文围绕检索增强的事实核查任务，设计了一系列实验来探究上下文长度和证据位置对大型语言模型（LLM）性能的影响。

**实验设置与数据集**：研究使用了三个事实核查数据集：HOVER、FEVEROUS 和 ClimateFEVER。评估了五个不同参数规模和架构的开源模型，包括 Llama-3.1-8B、Qwen2.5-7B、Qwen3-8B、Qwen3-32B 和 Llama-3.1-70B。实验主要分为两部分：一是评估模型仅依赖参数知识（仅提供声明）和提供黄金证据集（无额外上下文）时的性能；二是系统地改变输入上下文的总长度（2k, 4k, 8k, 16k tokens）以及证据块在上下文中的相对位置（从0%到100%），使用填充文本来控制总长度。

**对比方法与主要结果**：
1.  **参数知识评估**：所有模型在仅依赖参数知识时，其准确率（Acc.）均高于随机猜测，表明模型自身具备相当的事实知识。其中，ClimateFEVER 数据集上的表现最好（例如 Qwen3-32B 达 0.82），HOVER 最具挑战性。当提供黄金证据后，所有模型的性能均有系统性提升，提升幅度因数据集而异，FEVEROUS 上增益最大（最高达 +0.20 准确率）。Qwen3-32B 在几乎所有数据集和条件下都取得了最佳准确率。
2.  **上下文长度影响**：随着上下文长度从 2k 增加到 16k tokens，模型的平均验证准确率普遍呈现下降趋势。例如，图表显示平均性能在 8k 和 16k 时通常低于 2k。Qwen3 系列模型（8B和32B）表现出非单调模式，在 4k 处出现局部最低点。Qwen3-32B 在不同上下文长度下的表现最为稳定。
3.  **证据位置影响**：证据在提示词中的位置至关重要。当相关证据出现在提示的开头（0%）或结尾（100%）附近时，准确率 consistently 更高；而当证据位于上下文中间（例如 40%-60%）时，准确率最低，出现了明显的“中间上下文退化”现象。具体数据指标体现在一个大型表格中，例如对于 Llama-3.1-8B 在 FEVEROUS 数据集上，证据在开头（0%）时，最佳准确率（在2k上下文）为 0.70，最差（在8k上下文）为 0.56；而在中间位置（如50%），准确率可低至 0.46（8k上下文）。

**关键数据指标**：主要评估指标为分类准确率（Accuracy）。在参数知识评估中，也报告了宏平均 F1 分数（F1）、精确度（Precision）和召回率（Recall），并区分了支持（SUP）和反驳（REF）标签。在分析上下文影响时，核心指标是不同长度和证据位置配置下的准确率。

### Q5: 有什么可以进一步探索的点？

基于论文结论，未来研究可从多个维度深入。在机制层面，需探究不同模型架构（如注意力机制、位置编码）和训练策略（如长文本优化）如何影响证据位置鲁棒性，这有助于设计更抗干扰的模型。其次，研究应扩展到真实、嘈杂的检索增强生成（RAG）场景，考察部分相关或冲突证据对验证准确性的影响，从而提升端到端事实核查系统的实用性。此外，通过注意力模式分析和令牌级归因等可控实验，可深入解析模型在长上下文中分配注意力的具体方式，为提示工程提供理论依据。结合个人见解，未来可探索动态证据排序或分层处理机制，让模型能自适应地加权关键信息，以缓解中间位置性能下降问题。同时，跨任务泛化性也值得关注，如在摘要、推理等任务中验证上下文形状效应的普遍性。

### Q6: 总结一下论文的主要内容

该论文研究了上下文如何影响大语言模型在检索增强事实核查任务中的表现。核心问题是探究不同上下文长度和证据位置对LLM事实核查准确性的影响。研究使用HOVER、FEVEROUS和ClimateFEVER三个数据集，并评估了Llama-3.1、Qwen2.5和Qwen3等不同参数规模（7B至70B）的开源模型。

论文的主要发现包括：首先，LLM本身具备显著的参数化事实知识，能在无外部证据的情况下解决相当一部分事实核查任务。其次，当提供证据时，随着上下文长度的增加，模型的核查准确性普遍下降。第三，证据在提示词中的位置至关重要，当相关证据出现在提示的开头或结尾时，准确性较高，而放在中间位置则会导致准确性降低。其中，Qwen3-32B模型表现出最强的整体性能和跨上下文长度的相对稳定性。

这些结论表明，在构建检索增强事实核查系统时，盲目增加上下文长度未必能提升推理效果，而精心设计提示中证据的排列顺序对结果有实质性影响。这为优化事实核查系统的提示工程提供了重要指导。未来工作可深入探索位置鲁棒性的内在机制，并在更真实的检索场景中验证这些发现。
