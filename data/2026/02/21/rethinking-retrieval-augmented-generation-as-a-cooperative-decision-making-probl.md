---
title: "Rethinking Retrieval-Augmented Generation as a Cooperative Decision-Making Problem"
authors:
  - "Lichang Song"
  - "Ting Long"
  - "Yi Chang"
date: "2026-02-21"
arxiv_id: "2602.18734"
arxiv_url: "https://arxiv.org/abs/2602.18734"
pdf_url: "https://arxiv.org/pdf/2602.18734v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "检索增强生成"
  - "协同决策"
  - "Agent 架构"
  - "任务规划"
relevance_score: 8.5
---

# Rethinking Retrieval-Augmented Generation as a Cooperative Decision-Making Problem

## 原始摘要

Retrieval-Augmented Generation (RAG) has demonstrated strong effectiveness in knowledge-intensive tasks by grounding language generation in external evidence. Despite its success, many existing RAG systems are built based on a ranking-centric, asymmetric dependency paradigm, where the generation quality of the generator is highly dependent on reranking results of the reranker. To overcome this limitation, we reformulate RAG as a cooperative multi-agent decision-making problem and propose Cooperative Retrieval-Augmented Generation (CoRAG), a framework in which the reranker and the generator act as peer decision-makers rather than being connected through an asymmetric dependency pipeline. By jointly optimizing their behaviors toward a shared task objective, the reranker and generator are encouraged to cooperate, ensuring that document reranking and generation work in concert to improve the final response. Experimental results demonstrate good generalization and improved generation stability of CoRAG, even when the model is trained on only around 10K PopQA samples. Our model released in https://anonymous.4open.science/r/CoRAG-D63F

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统检索增强生成（RAG）系统中存在的“排名中心化、非对称依赖”范式问题。在该范式中，生成器的输出质量高度依赖于重排序器提供的精确文档排名顺序。这种紧密耦合导致生成器对重排序结果异常敏感：一旦重排序器出现微小失误（例如将相关文档错误地排在稍后位置），即使正确答案仍在候选文档集中，生成器也可能产生错误响应。此外，论文指出，让重排序器学习一个精确的文档总排序（例如严格区分第1、2、3名）本身非常困难，而生成器却恰恰需要这种精细排序，这种优化目标与模型能力之间的不匹配严重影响了RAG系统的稳定性和泛化能力。

为此，论文将RAG重新定义为一个协作式多智能体决策问题，提出了协作式检索增强生成（CoRAG）框架。该框架不再将重排序器和生成器视为具有单向依赖的流水线组件，而是将它们视为平等的、协作的智能体。通过在多智能体强化学习框架下，使用一个共享的、面向最终任务目标的奖励函数对两者进行联合优化，鼓励重排序器学习更准确的排序，同时训练生成器能够更鲁棒地利用候选文档中的信息，而不是僵化地依赖某个严格的排名顺序。这种方法旨在缓解生成器对精细排名的非对称依赖，从而提升整个系统在生成稳定性、鲁棒性和跨数据集泛化能力方面的表现。

### Q2: 有哪些相关研究？

相关研究主要分为三类：数据驱动、模型驱动和策略驱动（即Agentic RAG）方法。数据驱动方法关注查询或文档层面的信息挖掘与重构，如Decomposition Prompting通过提示工程分解复杂任务，EviNoteRAG采用笔记优先方式标注文档中的不确定信息，HtmlRAG则利用HTML保留语义结构。模型驱动方法通过微调提升模型对检索文档的解读、过滤和利用能力，代表工作包括通过正负样本对比训练增强鲁棒性的RetRobust、通过自合成推理显式学习去噪过程的InstructRAG，以及利用生成器反馈优化文档使用顺序和数量来训练重排序器的DynamicRAG。策略驱动方法引入智能体行为动态调整检索与生成策略，例如FLARE在生成遇到不确定标记时触发前瞻检索，SelfRAG通过反思模块同步动态调整检索与生成，MA-RAG通过思维链将工作流分解为子智能体，ComposeRAG支持模块化智能体组合。

本文提出的CoRAG在高层面上与Agentic RAG相似，都将重排序器和生成器建模为协作智能体。然而，与许多现有Agentic RAG方法将检索器（重排序器）和生成器视为需要单独训练或复杂提示协作的模块化智能体不同，CoRAG将其框架化为一个统一策略，无需手工协调机制，并使两个模块能够以任务感知的方式自适应专业化，从而克服了传统RAG系统中生成器高度依赖重排序结果的不对称依赖局限。

### Q3: 论文如何解决这个问题？

论文通过将检索增强生成（RAG）重构为一个协作的多智能体决策问题，提出了协作式检索增强生成（CoRAG）框架来解决传统RAG中生成器对重排序器结果的单向依赖问题。核心方法是将重排序器和生成器视为两个对等的决策智能体，通过共享的任务导向奖励进行联合优化，促使它们协同工作以提升最终响应质量。

在架构设计上，系统包含两个关键组件：重排序器（Reranker）和生成器（Generator）。重排序器负责对检索到的候选文档集进行重排序，根据相关性分数选择Top-K文档子集提供给生成器。生成器则基于查询和选定的文档子集生成最终响应。两者不再是传统的管道式依赖，而是作为协作的智能体，共同决策。

关键技术在于联合优化机制。优化基于一个共享的任务导向奖励函数（例如，生成响应是否包含真实答案）。对于重排序器，由于缺乏文档级直接监督，论文创新地将任务级奖励转化为文档级的随机偏好信号。通过历史迭代中文档是否参与成功生成的经验，计算每个文档的期望任务成功概率，并采样得到二元偏好标签。随后，采用基于群组相对偏好的优化（GRPO）思想，但为了降低方差，将其转化为一个确定性的排序学习问题，使用边际成对排序损失函数进行优化，确保高成功率的文档获得更高排名。

对于生成器，则直接应用标准的GRPO进行优化，其优势函数同样基于同一任务奖励计算，并与批次内其他响应比较得出。通过这种共享奖励的耦合，重排序器和生成器的行为得以协调，共同朝向提升任务性能的目标优化。实验表明，即使仅用约1万样本训练，该框架也表现出良好的泛化能力和生成稳定性。

### Q4: 论文做了哪些实验？

论文在五个知识密集型问答基准上进行了实验：PopQA、TriviaQA、Natural Questions (NQ)、ASQA 和 2WikiMultiHopQA。实验设置采用 BGE-reranker-v2-m3 作为重排序器，Llama-3-Instruct-8B 作为生成器，并使用 LoRA 进行微调。模型仅在约 1.3 万条 PopQA 样本上训练，其他数据集仅用于评估。

基准测试对比了三大类方法：无检索的基线（如 ChatGPT、Llama-3）、无训练的 RAG（如 In-Context RALM、InstructRAG-ICL）和有训练的 RAG（如 Self-RAG、RetRobust、InstructRAG-FT）。评估指标主要为准确率（ASQA 额外使用精确匹配、引用精确率和召回率）。

主要结果显示，CoRAG 在 PopQA、TriviaQA、NQ 和 2WikiMultiHopQA 上取得了最优性能（准确率分别为 71.2%、81.0%、72.4% 和 58.2%），显著超越了现有方法，但在需要合成多答案的 ASQA 上表现稍逊。消融研究表明，联合优化重排序器和生成器对性能提升至关重要，且生成器贡献更大。Top-N 分析表明 CoRAG 在不同文档数量下均表现稳健且性能随文档数增加而提升。跨任务评估（代码生成和表格问答）进一步证明了 CoRAG 生成器的良好泛化能力。

### Q5: 有什么可以进一步探索的点？

本文提出的CoRAG框架将RAG重构为协同决策问题，其核心局限在于联合优化可能削弱检索器进一步改进对生成质量的提升效果，这揭示了检索有效性与生成敏感性之间的内在张力。未来可从以下几个方向深入探索：首先，研究更精细的协同机制，如在训练中引入动态权重或对抗性目标，以平衡检索与生成模块的贡献，避免一方改进被另一方“吸收”而无法体现。其次，可将框架扩展至更复杂的多智能体场景，例如引入查询重写或事实核查等额外智能体，研究它们之间的协同与竞争关系。再者，探索在不同领域（如长文本生成、多轮对话）中应用此协同范式，并评估其泛化性与稳定性。最后，从理论层面分析这种协同决策框架的收敛性与最优解特性，为设计更高效的联合训练算法提供指导。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献是将检索增强生成（RAG）重新构想为一个协作式多智能体决策问题，并提出了相应的框架CoRAG。传统RAG系统通常采用以排序为中心、非对称依赖的范式，即生成器的输出质量高度依赖于重排序器的结果，这导致生成过程对排序的细微错误非常敏感，影响系统稳定性。CoRAG的创新在于将重排序器和生成器视为对等的协作智能体，通过多智能体强化学习框架，让两者共同优化一个共享的任务目标（如生成答案的准确性），而非单向依赖。这种方法放松了生成器对精确文档排序的严格依赖，鼓励重排序器学习更准确的排序，同时训练生成器更鲁棒地利用检索到的信息。实验表明，即使仅用约1万条PopQA数据训练，CoRAG也表现出良好的泛化能力和更强的生成稳定性，显著超越了基线模型。这一工作为RAG系统的设计提供了新视角，通过促进组件间的协同合作，提升了整体性能与鲁棒性。
