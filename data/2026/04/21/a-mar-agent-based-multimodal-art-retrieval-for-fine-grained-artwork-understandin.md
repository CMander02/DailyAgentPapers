---
title: "A-MAR: Agent-based Multimodal Art Retrieval for Fine-Grained Artwork Understanding"
authors:
  - "Shuai Wang"
  - "Hongyi Zhu"
  - "Jia-Hong Huang"
  - "Yixian Shen"
  - "Chengxi Zeng"
  - "Stevan Rudinac"
  - "Monika Kackovic"
  - "Nachoem Wijnberg"
  - "Marcel Worring"
date: "2026-04-21"
arxiv_id: "2604.19689"
arxiv_url: "https://arxiv.org/abs/2604.19689"
pdf_url: "https://arxiv.org/pdf/2604.19689v1"
github_url: "https://github.com/ShuaiWang97/A-MAR"
categories:
  - "cs.AI"
tags:
  - "Agent架构"
  - "多模态推理"
  - "检索增强"
  - "规划"
  - "可解释性"
  - "艺术领域"
  - "基准评测"
relevance_score: 7.5
---

# A-MAR: Agent-based Multimodal Art Retrieval for Fine-Grained Artwork Understanding

## 原始摘要

Understanding artworks requires multi-step reasoning over visual content and cultural, historical, and stylistic context. While recent multimodal large language models show promise in artwork explanation, they rely on implicit reasoning and internalized knowl- edge, limiting interpretability and explicit evidence grounding. We propose A-MAR, an Agent-based Multimodal Art Retrieval framework that explicitly conditions retrieval on structured reasoning plans. Given an artwork and a user query, A-MAR first decomposes the task into a structured reasoning plan that specifies the goals and evidence requirements for each step. Retrieval is then conditionedon this plan, enabling targeted evidence selection and supporting step-wise, grounded explanations. To evaluate agent-based multi- modal reasoning within the art domain, we introduce ArtCoT-QA. This diagnostic benchmark features multi-step reasoning chains for diverse art-related queries, enabling a granular analysis that extends beyond simple final answer accuracy. Experiments on SemArt and Artpedia show that A-MAR consistently outperforms static, non planned retrieval and strong MLLM baselines in final explanation quality, while evaluations on ArtCoT-QA further demonstrate its advantages in evidence grounding and multi-step reasoning ability. These results highlight the importance of reasoning-conditioned retrieval for knowledge-intensive multimodal understanding and position A-MAR as a step toward interpretable, goal-driven AI systems, with particular relevance to cultural industries. The code and data are available at: https://github.com/ShuaiWang97/A-MAR.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在细粒度艺术品理解任务中，现有方法难以进行可解释、证据可靠的多模态推理的问题。研究背景是，理解艺术品需要结合视觉内容与文化、历史、风格等多模态上下文进行多步推理。尽管当前的多模态大语言模型在艺术品解释方面展现出潜力，但它们依赖隐式推理和内部知识，导致可解释性差、证据缺乏显式依据，且容易产生幻觉。现有检索增强生成方法虽引入外部知识，但大多采用静态、单次检索策略，仅根据用户查询返回一组无序的上下文文档，无法适应多步推理中不同步骤需要不同类型证据（如视觉特征、历史背景）的需求。因此，本文的核心问题是：如何设计一个能够显式规划推理过程、并根据规划进行针对性多模态检索的框架，以实现更可靠、可解释且证据充分的多步骤艺术品理解与解释。

### Q2: 有哪些相关研究？

相关研究主要可分为两大类：**多模态艺术理解**和**推理感知的多模态检索**。

在**多模态艺术理解**方面，相关工作主要探索绘画分类、检索、描述，以及针对艺术领域微调多模态大语言模型（MLLMs），以进行形式、情感和一般性分析。然而，现有方法（如通过异构图注入结构化元数据）通常依赖于非结构化检索或预定义模式，导致推理过程隐含且与支撑证据的关联性弱，限制了可解释性。本文的A-MAR框架则通过引入显式的结构化推理计划来指导检索，旨在实现更可控、证据更充分的解释。

在**推理感知的多模态检索**方面，大多数现有检索增强系统采用静态、单次检索策略，检索内容由初始查询直接决定，难以支持多步推理或适应不同推理需求。艺术领域的特定方法（如KALE和ArtRAG）展示了整合艺术家、风格等结构化知识的优势，但其检索过程仍是静态的。近期基于智能体和规划的检索增强生成（RAG）方法引入了显式推理来指导检索，但它们主要关注纯文本任务，未解决多模态、特定领域推理的挑战。A-MAR填补了这一空白，首次将显式的多模态规划引入结构化艺术知识检索，实现了针对艺术领域、可控且基于证据的协调推理。

### Q3: 论文如何解决这个问题？

论文通过提出一个基于智能体的多模态艺术检索框架（A-MAR）来解决艺术理解中需要多步推理和显式证据支撑的问题。其核心方法是**将检索过程显式地建立在结构化推理计划之上**，从而实现对细粒度、可解释的多模态理解的支持。

整体框架包含三个主要模块。首先，**规划生成模块**接收用户查询和艺术品图像，利用大型语言模型（如GPT-4）将复杂的艺术理解任务分解为一个结构化的推理计划。该计划明确了每一步推理的子目标以及所需的证据类型（例如，识别视觉元素、查询艺术运动背景、分析风格影响等）。其次，**计划驱动的检索模块**是架构的关键创新。它并非一次性检索所有相关信息，而是根据推理计划中每一步的具体需求，动态地、有目标地从多模态知识库（如SemArt、Artpedia）中检索最相关的文本和视觉证据。这种“按需检索”机制确保了证据的精准性和支撑性。最后，**解释生成模块**整合每一步检索到的证据，生成最终的可视化解释（如带注释的图像）和文本解释，形成完整、可追溯的推理链。

关键技术在于**“推理计划作为检索条件”** 这一创新设计。它改变了传统检索或现有MLLM（多模态大语言模型）中检索与推理脱节或隐式进行的模式，使整个系统变得目标驱动和可解释。此外，论文引入的**ArtCoT-QA诊断基准**也是一个重要贡献，它通过包含多步推理链的艺术问答，使得能够超越最终答案准确率，对模型的证据支撑能力和多步推理能力进行细粒度评估。实验表明，这种计划引导的检索方式在解释质量、证据相关性和多步推理能力上均优于静态检索和强大的MLLM基线。

### Q4: 论文做了哪些实验？

论文在三个数据集上进行了实验：SemArt和Artpedia用于评估整体艺术品解释质量，ArtCoT-QA（本文新引入）用于诊断多步推理能力。实验设置固定了多模态大语言模型（MLLM）主干（主要使用Claude 4.5 Haiku，并用Mistral-3 Large验证鲁棒性），所有检索方法使用相同的结构化艺术上下文知识图（ACKG）和检索预算（粗粒度k=10节点，细粒度m=5节点）。

对比方法包括：1) MLLM-CoT（无外部检索的思维链生成）；2) 静态检索（无规划器）；3) 仅文本规划器（无视觉信息）；4) A-MAR（完整多模态规划器）；以及5) 先前艺术领域特定方法（如Wu 2022、Bai、KALE、ArtRAG）。

主要结果：在Artpedia和SemArt上，A-MAR在自动指标上全面优于基线。例如在Artpedia上（使用Mistral-3主干），A-MAR的BLEU-1/2/3/4分别达到43.3/22.2/15.2/12.4，METEOR为16.3，SPICE为12.3，ROUGE-L为29.4，均超过最佳基线。在ArtCoT-QA上，采用LLM-as-a-Judge评估（从答案质量、推理质量、检索质量三个维度1-5分打分），A-MAR在推理忠实性和步骤完整性上显著优于静态检索和仅文本规划器，证明了其基于规划的检索能实现更好的证据关联和多步推理。消融实验进一步表明，完整多模态规划器相比静态检索和仅文本规划器，在所有指标上带来一致提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的A-MAR框架虽然通过显式结构化推理计划提升了检索的针对性和可解释性，但仍存在一些局限性，为未来研究提供了多个探索方向。首先，其推理计划的生成依赖于预设的分解策略，而艺术理解本身具有主观性和多样性，单一的分解方式可能无法覆盖所有合理的推理路径（如对比式、类比式或主题优先等不同风格）。未来可系统研究不同推理风格对性能的影响，并开发能动态选择或融合多种推理策略的自适应机制。其次，当前框架侧重于检索增强，但未深入探索多模态大模型本身在艺术领域知识内部化与外部证据间的协同优化；未来可研究如何让模型学会在隐含知识与显式检索间动态权衡，以处理模糊或冲突信息。此外，评估方面，ArtCoT-QA提供了细粒度分析基础，但尚未涵盖艺术情感、文化偏见等深层维度；需建立更全面的评估协议，包括对推理链的因果性检验和跨文化泛化能力测试。最后，该框架在实时性、计算成本以及扩展到动态艺术形式（如视频、表演）方面仍有挑战，未来可探索轻量化代理设计与流式多模态推理机制。

### Q6: 总结一下论文的主要内容

该论文提出了A-MAR框架，旨在解决艺术品理解中多模态、多步骤推理的挑战。核心问题是现有大型多模态模型依赖隐式推理和内部知识，导致解释性差且缺乏显式证据支撑。为此，作者设计了一种基于智能体的多模态艺术检索方法，其核心贡献在于将推理过程显式化为结构化计划，并以此指导检索。

方法上，A-MAR首先将用户查询和艺术品图像分解为结构化推理计划，明确每一步的目标和所需证据类型。随后，系统根据该计划进行条件化检索，精准获取相关文本或视觉证据，从而支持逐步的、有据可依的解释。为评估该方法，论文还引入了诊断性基准ArtCoT-QA，专注于分析多步推理链。

实验表明，在SemArt和Artpedia数据集上，A-MAR在最终解释质量上优于静态检索和强大的多模态大模型基线。在ArtCoT-QA上的评估进一步证实了其在证据支撑和多步推理能力上的优势。该研究的意义在于强调了推理条件化检索对于知识密集型多模态理解的重要性，推动了可解释、目标驱动AI系统的发展，尤其在文化产业具有应用潜力。
