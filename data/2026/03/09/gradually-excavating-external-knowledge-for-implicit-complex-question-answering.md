---
title: "Gradually Excavating External Knowledge for Implicit Complex Question Answering"
authors:
  - "Chang Liu"
  - "Xiaoguang Li"
  - "Lifeng Shang"
  - "Xin Jiang"
  - "Qun Liu"
  - "Edmund Y. Lam"
  - "Ngai Wong"
date: "2026-03-09"
arxiv_id: "2603.08148"
arxiv_url: "https://arxiv.org/abs/2603.08148"
pdf_url: "https://arxiv.org/pdf/2603.08148v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "知识增强"
  - "迭代推理"
  - "工具使用"
  - "问答系统"
  - "外部知识检索"
  - "规划与执行"
relevance_score: 7.5
---

# Gradually Excavating External Knowledge for Implicit Complex Question Answering

## 原始摘要

Recently, large language models (LLMs) have gained much attention for the emergence of human-comparable capabilities and huge potential. However, for open-domain implicit question-answering problems, LLMs may not be the ultimate solution due to the reasons of: 1) uncovered or out-of-date domain knowledge, 2) one-shot generation and hence restricted comprehensiveness. To this end, this work proposes a gradual knowledge excavation framework for open-domain complex question answering, where LLMs iteratively and actively acquire external information, and then reason based on acquired historical knowledge. Specifically, during each step of the solving process, the model selects an action to execute, such as querying external knowledge or performing a single logical reasoning step, to gradually progress toward a final answer. Our method can effectively leverage plug-and-play external knowledge and dynamically adjust the strategy for solving complex questions. Evaluated on the StrategyQA dataset, our method achieves 78.17% accuracy with less than 6% parameters of its competitors, setting new SOTA for ~10B-scale LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在应对开放域隐含复杂问答任务时存在的两个核心缺陷：一是模型参数中可能缺乏特定领域或最新的知识，导致无法回答涉及未知或时效性强的实体的问题；二是模型通常采用一次性生成答案的方式，缺乏对多步骤、隐含逻辑问题的渐进式推理和策略规划能力，导致答案的全面性和准确性受限。

研究背景在于，尽管以ChatGPT、GPT-4等为代表的大语言模型在对话和知识记忆方面展现出类人能力，但在处理开放域、多步骤且逻辑隐含的复杂问题时仍面临挑战。例如，用户可能提出涉及冷门实体或需要分解为多个子问题并通过逻辑推理才能形成解答策略的问题，而现有方法往往依赖手动设计提示词或一次性检索外部知识，难以动态适应问题求解过程中逐步显现的知识需求和策略调整。

现有方法的不足主要体现在：一方面，大语言模型本身的知识覆盖存在盲区且可能过时，无法可靠回答所有开放域问题；另一方面，传统方法通常将问题视为单步任务，缺乏对隐含逻辑的主动挖掘和分步推理能力，导致在策略形成和知识综合利用上受限。

因此，本文的核心问题是：如何设计一个能够**迭代式主动获取外部知识**、并**基于逐步积累的知识动态规划和调整推理策略**的框架，以有效解决开放域、多步骤、逻辑隐含的复杂问答任务。为此，论文提出了GEEK框架，通过核心模型、检索器和提取器模块的协同，在每一步选择执行查询外部知识或进行逻辑推理等动作，逐步推进问题求解，并在过程中探索不同的解决策略空间，最终提升此类复杂问答的准确性和鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为外部信息检索和多步隐式问答两类方法。

在外部信息检索方面，现有工作通过检索器（如BM25、DPR）获取相关文本片段，并将其融合到解码过程中生成答案。例如，AISO采用多轮检索，综合不同检索模型的结果；HopRetriever则以多跳方式，利用前序检索中的实体进行递进查询。这些方法侧重于增强知识覆盖，但通常依赖静态检索策略。

在多步隐式问答领域，StrategyQA数据集推动了针对复杂隐式问题的研究。先前工作如IRGR通过迭代检索寻找前提；ReAct让模型动态选择行动（如调用API）；Maieutic Prompting构建逻辑树并验证每一步；RR结合思维链与检索，在StrategyQA上达到77.73%的准确率，曾是较小规模LLM的SOTA。然而，这些方法多基于HotpotQA等显式多步数据集，假设步骤间存在直接关联（如IRCoT直接以上一步结果作为查询），难以处理隐式问题中策略无法仅从问题文本推导的挑战。

本文提出的GEEK框架与上述工作的核心区别在于：它模拟主动挖掘外部知识的过程，通过组合子问题逐步构建完整解答策略，而非依赖预设的检索或推理路径。相比仅提升检索质量或分解策略的方法，GEEK能动态调整解决复杂问题的策略，在StrategyQA上以更少参数量（<6%）达到78.17%的准确率，实现了新的性能突破。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为GEEK的渐进式知识挖掘框架来解决开放域隐式复杂问答问题。该框架的核心思想是让大型语言模型（LLM）迭代地、主动地获取外部知识，并基于已积累的历史知识进行推理，从而动态地构建解答策略。

**整体框架与主要模块**：GEEK由三个核心组件构成：核心模型、检索器和提取器模型。整个工作流程是一个迭代循环：在每一步，核心模型根据当前问题状态Q_t，从一个预定义的动作空间A中选择一个动作执行，然后更新问题状态，逐步积累外部知识，直至得出最终答案。动作空间包括：1) **FinalAnswer**：当知识足够时，核心模型总结事实并生成最终答案；2) **AddDecomp**：核心模型生成下一个分解子问题；3) **Retrieve & Extract**：调用检索器获取相关外部文本，再由提取器从中提炼出事实答案；4) **SelfAnswer**：对于纯逻辑推理或已有知识的问题，核心模型直接回答。

**架构设计与关键技术**：
1.  **核心模型**：作为一个序列到序列的预训练LLM（如Flan-T5），它充当整个系统的控制器。它不仅负责选择动作，还负责执行AddDecomp、FinalAnswer和SelfAnswer这几类动作。在生成分解问题时，论文采用了“预回答技巧”，即提示模型生成后续所有分解问题及其伪答案，以确保策略的连贯性和可解性，生成的伪答案仅作为辅助，不加入问题状态。
2.  **检索器**：采用双编码器模型DPR进行高效检索。为了应对海量语料，设计了两级嵌套检索：先通过文档检索器（基于标题和首段）将搜索范围缩小至100个文档，再由段落检索器在这些文档中检索出最相关的k个段落。
3.  **提取器**：采用FiD架构，能够同时感知所有检索到的段落，并生成针对分解问题的简洁事实答案。为了提升提取的针对性，会将AddDecomp动作中生成的伪答案作为参考提示给提取器，引导其关注相关信息方面。

**创新点**：
*   **渐进式迭代推理**：将复杂问题求解建模为一个逐步选择动作、执行动作、更新状态的迭代过程，允许模型动态调整推理策略。
*   **主动知识获取与利用**：模型能主动判断何时需要检索外部知识，实现了外部知识的即插即用和与内部推理的有机结合。
*   **策略空间探索**：通过束搜索在AddDecomp步骤生成多个可能的分解问题，创建独立的分支进行后续求解，形成潜在的解决方案树，最后通过多数投票得出最终答案。这不同于一次性生成多个推理链的Self-Consistency方法，是对策略空间的主动探索。

### Q4: 论文做了哪些实验？

论文在StrategyQA数据集上进行了实验，该数据集包含2061个训练样本、229个开发样本和490个无标签测试样本。实验设置方面，作者使用DPR作为检索器（基于BERT-base-uncased），抽取器基于Flan-T5-3B构建，核心模型为Flan-T5-11B，并在8块V100 GPU上使用deepspeed进行训练。对比方法包括ChatGPT、FaithfulCoT、Visconde、RR以及PaLM等不同规模的模型。主要结果显示，GEEK方法在StrategyQA上达到了78.17%的准确率，相比仅使用思维链（CoT）的版本（75.98%）有所提升，且显著优于同等规模（约100亿参数）的模型，成为该规模下的新SOTA。关键数据指标包括：零样本Flan-T5准确率为62.01%，仅使用CoT的准确率为70.74%，而完整GEEK框架（包含分解、检索抽取和策略探索）达到78.17%。此外，通过GPT-4模拟的人工评估表明，GEEK生成的分解-事实对在62.45%的情况下比人类标注更受偏好。

### Q5: 有什么可以进一步探索的点？

该论文提出的GEEK框架在提升隐式复杂问答性能方面表现突出，但仍存在若干局限性和可进一步探索的方向。首先，尽管通过检索器和提取器缓解了幻觉问题，但神经网络的黑盒特性使得完全避免幻觉仍具挑战，未来可研究更透明的推理机制或引入可验证的推理链约束。其次，框架的逻辑正确性无法保证，可能出现步骤错误但答案正确、或步骤正确但答案错误的情况，未来可探索结合形式化验证或强化学习来优化推理过程的逻辑一致性。此外，当前依赖StrategyQA等稀缺数据集限制了泛化能力，未来需构建更多元、跨领域的复杂问答数据集，以评估模型在不同任务设置下的鲁棒性。结合领域见解，可能的改进包括：引入动态知识图谱更新机制以处理实时信息；设计多智能体协作框架，让不同模块专注于知识检索、逻辑推理等子任务，提升整体效率；或探索小规模模型与符号推理的结合，进一步降低参数量的同时增强可解释性。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在开放域隐式复杂问答任务中的局限性（如知识覆盖不全、生成方式单一）提出了GEEK框架。其核心贡献在于设计了一种渐进式知识挖掘方法，通过迭代执行外部知识查询和单步逻辑推理等动作，动态获取并积累外部知识，从而逐步推导出最终答案。该方法将隐式问题分解为显式子问题以检索相关知识，并利用积累的知识优化解决策略，同时通过搜索探索增强策略多样性。实验表明，GEEK在StrategyQA数据集上以不足竞争对手6%的参数量实现了78.17%的准确率，刷新了约100亿参数规模模型的性能记录。这项工作为通过有机整合外部知识而非单纯扩大模型规模来解决复杂问答问题提供了新的思路。
