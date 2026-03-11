---
title: "Latent-DARM: Bridging Discrete Diffusion And Autoregressive Models For Reasoning"
authors:
  - "Lina Berrayana"
  - "Ahmed Heakl"
  - "Abdullah Sohail"
  - "Thomas Hofmann"
  - "Salman Khan"
  - "Wei Chen"
date: "2026-03-10"
arxiv_id: "2603.09184"
arxiv_url: "https://arxiv.org/abs/2603.09184"
pdf_url: "https://arxiv.org/pdf/2603.09184v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "多智能体协作"
  - "规划与推理"
  - "模型异构性"
  - "通信框架"
  - "数学推理"
  - "常识推理"
relevance_score: 8.0
---

# Latent-DARM: Bridging Discrete Diffusion And Autoregressive Models For Reasoning

## 原始摘要

Most multi-agent systems rely exclusively on autoregressive language models (ARMs) that are based on sequential generation. Although effective for fluent text, ARMs limit global reasoning and plan revision. On the other hand, Discrete Diffusion Language Models (DDLMs) enable non-sequential, globally revisable generation and have shown strong planning capabilities, but their limited text fluency hinders direct collaboration with ARMs. We introduce Latent-DARM, a latent-space communication framework bridging DDLM (planners) and ARM (executors), maximizing collaborative benefits. Across mathematical, scientific, and commonsense reasoning benchmarks, Latent-DARM outperforms text-based interfaces on average, improving accuracy from 27.0% to 36.0% on DART-5 and from 0.0% to 14.0% on AIME2024. Latent-DARM approaches the results of state-of-the-art reasoning models while using less than 2.2% of its token budget. This work advances multi-agent collaboration among agents with heterogeneous models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统中，不同架构的语言模型之间如何有效协作的问题。研究背景是，当前大多数多智能体系统（MAS）完全依赖自回归语言模型（ARMs），这类模型虽然能流畅地生成文本，但其顺序生成的特性限制了全局推理和计划修订的能力。另一方面，离散扩散语言模型（DDLMs）支持非顺序、可全局修订的生成方式，在复杂规划和推理任务上表现出色，但其文本流畅性较差，难以与ARMs直接协作。现有方法的不足在于，ARMs和DDLMs各有优势，但缺乏有效的沟通机制，导致系统无法充分利用两者的互补特性。本文要解决的核心问题是：如何设计一种通信框架，既能发挥DDLMs在规划和全局推理上的优势，又能利用ARMs的文本流畅性来执行任务，从而提升多智能体系统的整体性能。为此，论文提出了Latent-DARM，一种在潜在空间中进行通信的框架，通过DDLM作为规划者生成解决方案计划，再由ARM作为执行者输出最终答案，以优化两者间的协作效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类与评测类。

在方法类工作中，核心是两类语言模型：自回归模型（ARMs）和离散扩散语言模型（DDLMs）。ARMs是当前主流，通过顺序生成保证文本流畅性，但其全局推理和计划修订能力受限。DDLMs则通过迭代去噪实现非顺序、可全局修订的生成，在规划任务上表现出优势，但其文本流畅性不足。近期研究探索了二者的结合，例如Block Diffusion模型，通过混合自回归与扩散生成机制来取长补短。本文的Latent-DARM框架与这类混合方法目标一致，但采取了不同的技术路径：它不试图统一或改造单一模型，而是构建一个多智能体协作系统，让DDLM和ARM分别专注于规划与执行，通过潜在空间通信桥接二者。

在应用类工作中，多智能体协作与潜在空间推理是重要方向。现有工作如“Chain of Continuous Thought”框架，展示了在连续隐藏状态空间中进行多步推理能提升准确性，这启发了本文采用潜在表征作为智能体间的通信媒介。然而，直接将一个模型的隐藏状态传递给另一个模型会因嵌入空间不匹配而失败。本文的创新点在于设计了一个专用的投影网络来解决这一异构潜在空间的对齐问题，从而实现了有效的跨模型协作。

在评测类工作中，研究通常关注于数学、科学和常识推理基准。本文在DART-5、AIME2024等基准上评估了Latent-DARM，其性能提升（例如准确率从27.0%到36.0%）证明了该框架的有效性。与最先进的推理模型相比，本文方法在消耗极少token预算（<2.2%）的情况下接近了其效果，突出了其在效率与性能上的优势。

综上，本文与相关工作的关系是继承并整合了DDLMs的规划优势、ARMs的执行流畅性以及潜在空间通信的思想，其核心区别在于提出了一个专门解决异构模型嵌入空间不匹配问题的多智能体协作框架，而非改进单一模型或简单的输出拼接。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Latent-DARM的潜在空间通信框架来解决离散扩散模型（DDLM）与自回归模型（ARM）在协作中面临的挑战。核心方法是绕过传统的文本空间接口，直接在潜在表示空间建立桥梁，使擅长全局规划和修订的DDLM（规划器）与擅长流畅文本生成和执行的ARM（执行器）能够高效协作。

整体框架包含三个主要模块：DDLM规划器、ARM执行器以及一个关键的学习投影模块。DDLM首先处理问题输入，在最终去噪步骤后生成一个潜在规划表示 \( h_{DDLM} \)。该表示不经过解码为文本，而是通过一个可训练的投影模块 \( f_\theta \) 直接映射到ARM的嵌入空间，得到 \( h_{proj} \)。这个投影后的表示随后与问题本身的ARM嵌入进行拼接，形成ARM的最终输入条件，ARM基于此生成最终答案。

架构设计的关键创新点在于这个投影模块及其训练目标。投影模块是一个简单的Linear–GELU–Linear网络，是系统中唯一可训练的组件，而DDLM和ARM的参数在训练过程中保持冻结。其训练目标并非传统的基于距离的嵌入对齐（因为“正确”的ARM目标嵌入难以定义），而是采用基于下游任务的间接优化。具体而言，目标是最小化ARM在给定投影潜在表示和问题条件下，生成正确答案的负对数似然。这种任务驱动的损失函数鼓励投影模块将DDLM的潜在表示映射到ARM表示空间中那些能引发正确下游行为的区域，实现了功能等价而非几何相似的优化。

这种方法避免了传统文本接口中必须经历的“潜在→文本→潜在”的转换瓶颈，减少了信息损失和计算开销。实验表明，这种潜在空间协作在多个推理基准上显著优于基于文本的接口，并且能以极低的token预算接近最先进推理模型的性能，实现了异构模型智能体之间的高效协同。

### Q4: 论文做了哪些实验？

论文在数学、科学和常识推理等多个基准上进行了实验评估。实验设置上，研究者构建了Latent-DARM框架，其中规划器（Planner）采用离散扩散语言模型（DDLM），包括LLaDA-8B-Instruct和Dream-v0-Instruct-7B；执行器（Executor）采用自回归语言模型（ARM），包括非推理模型（如Qwen2.5-7B-Instruct、Llama-3.1-8B-Instruct及其更小变体）和专用推理模型（如Qwen3-1.7B和DeepSeek-R1蒸馏版）。核心组件是一个定制的潜在投影器（含三个线性层和GELU激活），用于将DDLM的潜在表示映射到ARM的隐藏空间，该投影器使用从LLaDA-8B-Instruct提取的35,000个样本进行训练。

使用的数据集/基准测试包括：ARC-Easy和ARC-Challenge（科学考试问题）、MMLU（涵盖数学、历史等多学科）、AIME 2024（高中数学竞赛）以及DART-1至DART-5（大规模数学推理基准，涵盖五个难度等级）。评估时采用了200个样本或完整基准。

对比方法主要涉及基于文本的接口（即规划器与执行器通过文本通信的基线）以及先进的专用推理模型（如DeepSeek-R1）。主要结果显示，Latent-DARM显著优于文本接口：在DART-5上准确率从27.0%提升至36.0%，在AIME 2024上从0.0%提升至14.0%。同时，Latent-DARM在使用不到最先进推理模型2.2%的token预算的情况下，达到了与之接近的性能，证明了其高效性。关键数据指标包括准确率提升和token预算的极大节省。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度展开。首先，**潜空间投影器的泛化能力有限**，论文指出其在MMLU等需要广泛事实性知识的任务上表现不佳，因为投影器仅在推理任务上训练，未能有效保留细粒度知识。未来可探索**多任务或领域自适应训练**，使投影器能同时编码推理结构和事实细节。其次，**规划长度与性能的权衡**尚不明确，实验显示64个token的规划效果最佳，但更复杂的任务可能需要更动态、结构化的规划表示。未来可研究**自适应规划长度机制**或**分层潜变量表示**，以提升规划的灵活性和信息密度。再者，**执行器瓶颈凸显**，诊断表明潜空间协作后执行器成为主要错误来源。未来可探索**增强执行器能力的方法**，例如通过知识蒸馏将规划器的全局推理能力迁移给执行器，或设计**迭代式精炼机制**，允许执行器与规划器进行多轮潜空间交互以修正错误。此外，**框架目前仅整合了DDLM和ARM**，未来可扩展至其他异构模型（如基于检索的模型或符号推理器），并研究**更通用的潜空间通信协议**。最后，**效率与性能的平衡**值得深入，尽管token使用量极低，但规划器的扩散过程计算开销仍较大，未来可优化扩散采样效率或探索**非自回归模型与潜空间结合的轻量级替代方案**。

### Q6: 总结一下论文的主要内容

该论文提出了Latent-DARM框架，旨在解决多智能体系统中自回归语言模型（ARM）与离散扩散语言模型（DDLM）协作的难题。核心问题是：ARM虽能生成流畅文本，但缺乏全局推理和计划修订能力；DDLM擅长非顺序的全局规划，但文本流畅性差，阻碍了与ARM的直接协作。为此，论文引入了一种潜在空间通信框架，通过学习到的潜在投影替代基于文本的接口，使DDLM规划器能将结构化规划信息高效传递给ARM执行器，从而结合两者优势。

方法上，Latent-DARM通过潜在空间桥接异构模型，允许扩散模型专注于高层次规划，而自回归模型负责流畅执行，避免了文本解码导致的信息损失。实验表明，该方法在数学、科学和常识推理基准上平均优于基于文本的协作，如在DART-5上准确率从27.0%提升至36.0%，在AIME2024上从0.0%提升至14.0%。主要结论是：潜在空间通信能显著减少规划失败，保留推理结构，同时以极低的计算成本（仅需最先进模型2.2%的token预算）达到竞争性性能。这挑战了自然语言作为智能体间唯一通信介质的传统假设，为高效、可扩展的异构模型协作系统开辟了新方向。
