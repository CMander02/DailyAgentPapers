---
title: "ParamMem: Augmenting Language Agents with Parametric Reflective Memory"
authors:
  - "Tianjun Yao"
  - "Yongqiang Chen"
  - "Yujia Zheng"
  - "Pan Li"
  - "Zhiqiang Shen"
  - "Kun Zhang"
date: "2026-02-26"
arxiv_id: "2602.23320"
arxiv_url: "https://arxiv.org/abs/2602.23320"
pdf_url: "https://arxiv.org/pdf/2602.23320v1"
categories:
  - "cs.LG"
  - "cs.MA"
tags:
  - "Agent 架构"
  - "记忆模块"
  - "自我反思"
  - "推理"
  - "参数化记忆"
  - "Agent 自演化"
  - "代码生成"
  - "数学推理"
  - "问答"
relevance_score: 9.5
---

# ParamMem: Augmenting Language Agents with Parametric Reflective Memory

## 原始摘要

Self-reflection enables language agents to iteratively refine solutions, yet often produces repetitive outputs that limit reasoning performance. Recent studies have attempted to address this limitation through various approaches, among which increasing reflective diversity has shown promise. Our empirical analysis reveals a strong positive correlation between reflective diversity and task success, further motivating the need for diverse reflection signals. We introduce ParamMem, a parametric memory module that encodes cross-sample reflection patterns into model parameters, enabling diverse reflection generation through temperature-controlled sampling. Building on this module, we propose ParamAgent, a reflection-based agent framework that integrates parametric memory with episodic and cross-sample memory. Extensive experiments on code generation, mathematical reasoning, and multi-hop question answering demonstrate consistent improvements over state-of-the-art baselines. Further analysis reveals that ParamMem is sample-efficient, enables weak-to-strong transfer across model scales, and supports self-improvement without reliance on stronger external model, highlighting the potential of ParamMem as an effective component for enhancing language agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于自反思的语言智能体在迭代优化解决方案时，其反思输出往往重复且缺乏多样性，从而限制推理性能提升的问题。研究背景是，大型语言模型在复杂推理任务中展现出显著进步，其中基于反思的框架通过在推理时进行自我反思并积累到情景记忆中来指导后续尝试，已被证明是有效的。然而，现有方法（如Reflexion、DoT和DoT-bank）存在明显不足：它们主要通过提示层面的修改或基于检索的方式引入跨样本轨迹来增加反思多样性，但提示方法改进有限，而检索方法（如DoT-bank）依赖嵌入相似性，捕捉组合模式的能力有限，且学习到的嵌入容易坍缩到低秩子空间，从而降低了检索的多样性。

本文的核心问题是：如何进一步扩展反思的多样性以实现更强的推理性能？为此，论文提出了ParamMem，一个参数化记忆模块，它通过将跨样本的反思模式编码到模型参数中，从根本上提供多样性。与依赖提示变化或显式检索相似样本的方法不同，ParamMem通过对辅助反思数据集进行轻量级微调，在推理时通过从学习到的模式中泛化来生成反思，从而克服了现有方法的局限性。在此基础上构建的ParamAgent框架，整合了参数化记忆与情景记忆和跨样本记忆，旨在通过增强反思多样性来持续提升语言智能体的推理能力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升语言智能体自反思能力的多样性展开，可分为方法类和应用类。

在方法类研究中，**基于提示的反思增强**（如DoT）通过修改提示词来增加反思的多样性，但改进有限。**基于检索的反思增强**（如DoT-bank）则通过检索相似样本的推理轨迹来引入多样性，取得了初步成功，但其依赖嵌入相似性检索，捕捉组合模式的能力有限，且检索多样性易受嵌入坍缩影响。本文提出的ParamMem与这些工作有直接关联，但采用了根本不同的机制：它通过微调一个轻量级参数化模块，将跨样本的反思模式编码到参数中，在推理时通过温度控制采样生成多样化反思，而非依赖提示修改或显式检索。

在应用类研究中，**反思型智能体框架**（如Reflexion）已成功应用于编程、数学推理和决策等任务，其核心是让智能体在情节记忆中积累自我反思以指导后续尝试。本文的ParamAgent框架正是在此基础上，创新性地将参数化反思记忆（ParamMem）与情节记忆、跨样本记忆相集成，从而构建了一个更强大的反思型智能体。

本文与这些相关工作的核心区别在于，它首次引入了参数化记忆模块来内部化并生成跨样本反思模式，提供了一种样本高效、可自我改进且支持弱到强知识迁移的新范式，从而在根本上扩展了反思多样性，提升了推理性能。

### Q3: 论文如何解决这个问题？

论文通过引入一个名为ParamMem的参数化记忆模块，并结合一个名为ParamAgent的反思型智能体框架来解决自我反思过程中输出重复、多样性不足的问题。核心方法是利用参数化学习来编码跨样本的反思模式，从而生成多样化的反思信号，以增强语言智能体的推理能力。

整体框架分为两个主要阶段。首先，构建ParamMem模块：通过收集一个辅助数据集，其中每个样本包含输入任务（如编程问题）和由大型语言模型生成的反思反馈（如潜在错误枚举）或分解后的语义单元（针对多跳问答）。然后，使用LoRA技术对预训练语言模型进行微调，得到一个参数化模块，该模块能够学习跨样本的反思规律，并通过温度控制采样生成新颖的反思，避免了基于提示或检索方法的局限性。

其次，将ParamMem集成到反思型智能体框架ParamAgent中。在每次迭代中，智能体不仅基于历史自我反思，还从ParamMem中采样一个全局级反思信号，共同作为条件生成新的解决方案。此外，论文还提出了一个增强变体ParamAgent-plus，它额外检索记忆库中已解决任务的推理轨迹，结合参数化和跨样本信号进行生成。

关键技术包括：1）利用训练动态隐式捕获跨样本规律，使模块能泛化到未见示例；2）温度控制采样调节反思多样性；3）结合参数化记忆、情景记忆和跨样本记忆的多源记忆机制。创新点在于首次将参数化记忆用于反思生成，通过模型参数编码反思模式，提供了一种样本高效、支持弱到强迁移且不依赖外部强模型的自改进方法，从而显著提升了任务成功率。

### Q4: 论文做了哪些实验？

论文在代码生成、数学推理和多跳问答三个领域进行了广泛的实验。实验设置方面，所有方法（包括基线）均固定迭代次数为5次。对于ParamAgent及其变体，首次迭代采样温度设为T=0.2，后续迭代设为T=1.0以促进多样性。参数化模型使用Llama3.1-8B-Instruct实例化，并通过LoRA进行微调（秩r=128，缩放因子α=32，学习率2e-5，训练3轮）。

使用的数据集/基准测试包括：代码生成任务使用HumanEval和MBPP，以及更具挑战性的LiveCodeBench进行额外评估；数学推理使用涵盖七个学科竞赛级问题的MATH数据集；多跳问答使用HotpotQA和2WikiMultiHopQA。评估指标上，代码任务报告Pass@1，数学和QA任务报告0-1准确率。

对比方法包括：(1) Base（无反思的基础LLM代理）；(2) Reflexion（使用情景自反思）；(3) Retroformer（同样使用参数化反思模块，但通过策略梯度优化训练以提高反思准确性）；(4) DoT（在Reflexion基础上增加提示级多样性）；(5) DoT-bank（进一步结合记忆库丰富反思反馈）。实验在三个不同推理能力的骨干LLM上进行：Llama-3.1-8B、Mistral-7B-v0.2和Qwen2-1.5B-instruct。

主要结果显示，ParamAgent在多个数据集上超越了所有基线方法。关键数据指标如下：在HumanEval上，ParamAgent使用Llama-3.1-8B达到82.93% Pass@1，显著优于Base的59.15%和最佳基线DoT-bank的79.56%；在MBPP上达到67.00%，优于Base的47.61%和DoT-bank的64.82%。在MATH上，ParamAgent-plus（增强版）使用Llama-3.1-8B达到75.45%准确率，优于Base的48.20%和DoT-bank的73.02%。在多跳QA任务中，ParamAgent在HotpotQA（Llama-3.1-8B）上达到78.33%准确率，优于Base的57.67%和Retroformer的73.00%；在2WikiMultiHopQA上达到88.67%，优于Base的40.33%和DoT-bank的80.33%。分析表明，ParamMem通过训练动态引入了额外的反思多样性层（如聚类分析显示其最优聚类数K*=39，显著高于其他方法），且多样化的反思扩大了错误诊断的假设空间，从而提升了性能。此外，研究还验证了方法在不依赖更强外部模型下的自我改进能力、小参数模块对强LLM代理的增强（弱到强迁移）以及ParamMem的样本效率优势。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来可探索的方向包括：首先，ParamMem 在数学推理任务上表现相对较弱，这表明其参数化记忆模块可能对需要精确逻辑推导和固定模式的问题适应性不足，未来可研究如何结合符号推理或结构化知识来增强其在数学领域的表现。其次，方法依赖于高质量的反思数据生成，若初始数据存在偏差或噪声，可能影响训练效果，未来可探索更鲁棒的数据合成或去噪策略。此外，实验主要基于特定规模的模型（如8B、7B），虽然提到了弱到强的迁移，但参数化模块与不同架构、更大规模基座模型的适配性及效率仍需系统评估。从改进思路看，可以探索动态温度调度策略，而非固定的两阶段温度设置，以更精细地平衡反思的多样性与准确性。另外，ParamMem 目前主要编码跨样本模式，未来可考虑引入任务或领域特定的元学习，使模块能快速适应新任务。最后，其与外部工具（如代码执行器、数学求解器）的协同机制尚未深入探讨，结合工具使用可能进一步提升复杂任务的解决能力。

### Q6: 总结一下论文的主要内容

该论文提出了一种增强语言智能体自我反思能力的新方法。针对现有反思机制容易产生重复输出、限制推理性能的问题，作者通过实证分析发现反思多样性与任务成功率呈强正相关。为此，论文核心贡献是引入了**ParamMem**，一个参数化记忆模块，它将跨样本的反思模式编码到模型参数中，并通过温度控制采样来生成多样化的反思信号。基于此模块构建的**ParamAgent**框架，整合了参数化记忆、情景记忆和跨样本记忆。在代码生成、数学推理和多跳问答任务上的实验表明，该方法显著超越了现有基线。分析进一步指出，ParamMem具有样本高效性，支持不同模型规模间的弱到强知识迁移，并能不依赖更强外部模型实现自我改进，这凸显了其作为增强语言智能体有效组件的潜力。
