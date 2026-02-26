---
title: "Understanding Artificial Theory of Mind: Perturbed Tasks and Reasoning in Large Language Models"
authors:
  - "Christian Nickel"
  - "Laura Schrewe"
  - "Florian Mai"
  - "Lucie Flek"
date: "2026-02-25"
arxiv_id: "2602.22072"
arxiv_url: "https://arxiv.org/abs/2602.22072"
pdf_url: "https://arxiv.org/pdf/2602.22072v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Theory of Mind"
  - "Agent Reasoning"
  - "LLM Evaluation"
  - "Chain-of-Thought"
  - "False-Belief Tasks"
  - "Agent Capabilities"
relevance_score: 7.5
---

# Understanding Artificial Theory of Mind: Perturbed Tasks and Reasoning in Large Language Models

## 原始摘要

Theory of Mind (ToM) refers to an agent's ability to model the internal states of others. Contributing to the debate whether large language models (LLMs) exhibit genuine ToM capabilities, our study investigates their ToM robustness using perturbations on false-belief tasks and examines the potential of Chain-of-Thought prompting (CoT) to enhance performance and explain the LLM's decision. We introduce a handcrafted, richly annotated ToM dataset, including classic and perturbed false belief tasks, the corresponding spaces of valid reasoning chains for correct task completion, subsequent reasoning faithfulness, task solutions, and propose metrics to evaluate reasoning chain correctness and to what extent final answers are faithful to reasoning traces of the generated CoT. We show a steep drop in ToM capabilities under task perturbation for all evaluated LLMs, questioning the notion of any robust form of ToM being present. While CoT prompting improves the ToM performance overall in a faithful manner, it surprisingly degrades accuracy for some perturbation classes, indicating that selective application is necessary.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究大语言模型是否真正具备心智理论能力，以及如何系统评估和提升其在此类任务上的鲁棒性与可解释性。研究背景在于，心智理论作为人类认知与社交互动的核心，对于实现可靠的人机交互至关重要，而现有研究对大语言模型是否拥有真正的心智理论能力存在争议。现有方法的不足主要体现在：先前研究多依赖于狭窄的基准测试，这些测试在面临微小扰动时性能会大幅下降，从而无法证明模型具有泛化且稳健的心智理论能力；同时，现有基准缺乏系统结构来评估扰动效应或不同提示策略的影响，也难以分析模型内部推理过程的可信度。因此，本文要解决的核心问题是：通过构建一个包含经典及扰动版错误信念任务的、手工精细标注的数据集，并设计相应评估指标，来系统检验大语言模型在心智理论任务上的鲁棒性，并探究思维链提示能否以可信的方式提升其性能与推理可解释性，从而更深入地理解大语言模型心智理论能力的本质与局限。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：心智理论（ToM）在大型语言模型（LLMs）中的研究、思维链（CoT）提示技术，以及思维链的忠实性评估。

在**ToM评估研究**方面，已有工作探讨了LLMs是否展现真正的心智理论能力。例如，有研究认为GPT-4等先进模型能像人类一样解决经典错误信念任务，但另一些研究指出轻微扰动就会破坏性能，表明模型可能依赖统计线索而非真正推理心理状态。为此，研究者开发了多种评估基准（如ToMBench、FANToM、OpenToM、ToMATO），这些基准覆盖了不同社交场景和多模态环境，但普遍发现LLMs仍落后于人类，且可能仅测量了“字面心智理论”而非“功能心智理论”。**本文与这些工作的区别在于**：通过系统引入多种扰动类别，并构建包含扰动/非扰动任务对、附带黄金标准CoT注释的数据集，从而能精确分析扰动类型如何影响推理质量和最终预测，这是现有基准所缺乏的。

在**CoT提示技术**方面，CoT被广泛用于提升LLMs在推理任务上的表现，但其在ToM任务中的效果尚不明确且研究不足。已有报告显示CoT对不同任务类型的性能影响不一，而一项元分析指出CoT主要在数学或逻辑任务上带来显著收益。**本文聚焦于错误信念类ToM任务**，探究CoT提示对性能的影响，并特别关注其应用的选择性。

在**CoT忠实性评估**方面，先前研究指出CoT推理轨迹可能并不忠实于最终答案，其因果关联性存疑。相关工作常使用近似度量（如ROUGE分数）来评估忠实性。**本文的贡献在于**：采用基于推理链实际正确性的相关性方法来更精确地度量忠实性，同时与基于ROUGE的近似方法进行比较，从而更可靠地评估CoT在ToM推理中的信息价值。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统性的评估框架来解决大语言模型（LLM）是否具备稳健心理理论（ToM）能力的问题。其核心方法是创建一个精心设计、带有丰富标注的ToM数据集，并在此基础上结合链式思维（CoT）提示，对多种LLM进行全面的性能与推理忠实度评估。

**整体框架与主要模块**：
1.  **数据集构建**：研究构建了一个新颖的人工标注数据集，包含经典和扰动版错误信念任务。数据集基于7个基本场景（4个“意外内容”和3个“意外转移”），并通过引入10类扰动（其中5类是已有，5类是新提出的）来生成变体任务。每项任务要求模型追踪主角随着情景展开而变化的信念状态。数据集最终包含1088个问题，并提供了每个句子后主角正确信念状态的黄金标注（以集合形式，允许歧义），这为评估推理链的正确性奠定了基础。
2.  **实验设计与评估**：对六个开源LLM（如Llama 2/3-70B, Vicuna-33B等）进行测试，采用两种提示策略：直接回答的“普通提示”（V-P）和分步推理的“链式思维提示”（CoT-P）。模型被要求以结构化JSON格式输出每一步的心理状态更新和最终答案，便于自动化评估。
3.  **多层次评估指标**：
    *   **性能与稳健性**：计算模型在各类任务上的准确率，并使用平均处理效应（ATE）量化扰动和CoT提示的影响。定义了“表面ToM”（OToM）、“稳健ToM”（RToM）和“有限稳健ToM”的阈值标准，以区分不同层次的ToM能力。
    *   **推理链正确性**：核心创新在于严格评估CoT的质量。主要指标是判断模型生成的推理链是否是黄金标注推理链的一个“真子序列”。这要求模型输出的中间信念状态必须与黄金链中的某个有效序列逐步匹配，并最终到达正确状态。此外，还引入了基于最长公共子序列（ROUGE-LCS）、最长公共“准真子序列”（ROUGE-LCPS）和状态转移重叠度（Transition Overlap）的连续度量作为近似评估。
    *   **推理忠实度**：通过计算CoT正确性与最终答案正确性之间的相关性（如Φ系数和点二列相关系数）来评估模型的“忠实度”。高正相关表明模型的推理步骤对其最终答案有因果贡献，而非“安慰剂效应”。

**创新点**：
1.  **系统化的扰动评估**：不仅应用了已知扰动，还新引入了五类需要整合不同推理模式（如空间推理、历史知识、情感推断、信息过滤等）的扰动，从而更全面、更严格地测试ToM能力的鲁棒性。
2.  **精细的推理链评估方法**：提出了基于“真子序列”匹配的严格二进制评估标准，这是对CoT推理质量进行深入、精确分析的关键创新。同时辅以多种连续度量，提供了多角度的评估视角。
3.  **忠实度与安慰剂效应分析**：明确地将CoT提示的收益分解为源于正确推理的部分和可能源于提示形式本身的“安慰剂效应”，这为了解CoT如何以及为何影响ToM任务表现提供了更细致的洞察。
4.  **综合评估框架**：将数据集构建、多模型测试、多维度指标（准确率、稳健性、推理正确性、忠实度）有机结合，形成了一个能够深入质疑和检验LLM是否拥有真正、稳健ToM能力的完整方法论体系。

### Q4: 论文做了哪些实验？

论文实验围绕评估大语言模型在扰动任务下的心智理论能力展开。实验设置上，研究者使用两种提示策略：直接回答的普通提示和生成中间推理步骤的思维链提示，对六个开源大语言模型进行推理，包括Llama-2-70B-Chat、Llama-3-70B-Instruct、Vicuna-33B-v1.3、Yi-34B-Chat、Mixtral-8x7B-Instruct-v0.1和DBRX-Instruct，参数规模从33B到132B。模型通过HuggingFace的transformers库访问，在A100计算节点上运行，温度设为0，并采用一次性提示以提高输出一致性。

数据集为研究者手工构建的丰富标注心智理论数据集，包含经典和扰动的错误信念任务，以及对应的有效推理链空间。评估指标包括最终答案准确率、思维链正确性以及模型忠实度（即推理正确性与最终预测之间的统计对齐）。主要结果发现：在无扰动任务中，使用普通提示时，四个模型表现出类似心智理论的行为；但在任务扰动下，所有模型性能均大幅下降，仅Llama-3-70B和DBRX在五个扰动类别中保持有限鲁棒性（准确率≥50%），其中空间推理扰动对所有模型均构成挑战。思维链提示总体上能忠实提升心智理论性能，但对某些扰动类别（如结论来自情感和自动改变知识）反而降低了准确率，表明需选择性应用。此外，思维链正确性与最终答案正确性在大多数模型中呈强相关，模型总体忠实，但Mixtral出现安慰剂效应，即即使生成错误推理链，性能仍有所提升。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度展开。首先，数据集仅聚焦于错误信念任务，未涵盖愿望推理、失言检测等其他心理理论维度，未来可扩展任务类型以全面评估LLMs的社会认知能力。其次，当前评估主要基于开源模型，未来需纳入GPT、Claude等闭源模型进行横向对比，并收集人类在扰动任务上的表现数据以建立更可靠的基线。此外，研究指出思维链提示在某些扰动类型中反而降低性能，这启示未来需探索更精细的提示策略（如基于代理的架构或符号推理方法），避免思维链引入噪声。从方法学角度，当前依赖结构化推理输出评估思维链正确性，对小型模型适用性有限；未来可开发更灵活的评估框架，并探索利用LLMs自动生成合成数据以降低标注成本。最后，论文强调模型失败源于推理步骤缺陷而非“编造”推理，这提示通过改进训练数据或引导式推理增强中间步骤的可靠性，可能是实现稳健心理理论的有效路径。

### Q6: 总结一下论文的主要内容

该论文主要研究大语言模型是否具备真正的心智理论能力。作者通过构建一个包含经典及扰动错误信念任务的手工标注数据集，系统评估了LLMs在ToM任务上的鲁棒性。核心贡献在于提出了一个包含10类扰动、1088个样本的新基准，并设计了基于结构化思维链的忠实性评估框架。研究发现，尽管多数模型在未扰动任务上表现出表面ToM能力，但在任务扰动下性能急剧下降，仅个别模型保持有限鲁棒性，空间推理任务尤为困难。思维链提示虽能整体提升性能且推理过程基本忠实，但在某些扰动类别中反而降低准确率，表明需选择性使用。论文结论指出，LLMs的ToM能力仍很脆弱，但针对性提示和结构化评估为未来发展提供了路径。
