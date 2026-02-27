---
title: "Generative Agents Navigating Digital Libraries"
authors:
  - "Saber Zerhoudi"
  - "Michael Granitzer"
date: "2026-02-26"
arxiv_id: "2602.22529"
arxiv_url: "https://arxiv.org/abs/2602.22529"
pdf_url: "https://arxiv.org/pdf/2602.22529v1"
categories:
  - "cs.IR"
  - "cs.AI"
  - "cs.DL"
tags:
  - "Agent 仿真"
  - "用户行为模拟"
  - "数字图书馆"
  - "Agent 评测/基准"
  - "LLM 应用于 Agent 场景"
relevance_score: 7.5
---

# Generative Agents Navigating Digital Libraries

## 原始摘要

In the rapidly evolving field of digital libraries, the development of large language models (LLMs) has opened up new possibilities for simulating user behavior. This innovation addresses the longstanding challenge in digital library research: the scarcity of publicly available datasets on user search patterns due to privacy concerns. In this context, we introduce Agent4DL, a user search behavior simulator specifically designed for digital library environments. Agent4DL generates realistic user profiles and dynamic search sessions that closely mimic actual search strategies, including querying, clicking, and stopping behaviors tailored to specific user profiles. Our simulator's accuracy in replicating real user interactions has been validated through comparisons with real user data. Notably, Agent4DL demonstrates competitive performance compared to existing user search simulators such as SimIIR 2.0, particularly in its ability to generate more diverse and context-aware user behaviors.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决数字图书馆研究中因隐私问题导致的真实用户搜索行为数据稀缺的难题。随着大语言模型（LLM）的发展，模拟用户行为成为可能，但现有模拟方法在生成多样化、符合上下文情境的用户行为方面存在不足。研究背景是数字图书馆和搜索引擎的普及使得理解用户搜索行为对系统优化至关重要，而传统依赖真实用户观察的方法成本高、受伦理和隐私限制。因此，本文提出Agent4DL，一个基于LLM的用户搜索行为模拟器，核心目标是生成更真实、动态的用户档案和搜索会话，精准模拟查询、点击和停止等行为，以弥补现有数据缺口和模拟方法的局限性，为数字图书馆研究提供可扩展且可靠的替代方案。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：信息检索领域的用户行为分析与用户模拟方法。

在**用户行为分析**方面，传统研究集中于分析搜索会话中的用户交互，意图演变与行为预测，代表性工作包括会话搜索模型和点击模型。这些模型通过分析查询-点击数据模式来理解用户行为，推动了以用户为中心的数字图书馆发展，为本文提供了理论基础。

在**用户模拟方法**方面，早期方法侧重于简单的查询生成和基于启发式的搜索停止行为模拟。近年来，随着大语言模型（LLMs）的发展，研究开始利用LLMs在网页搜索、推理和社交互动等场景中生成更动态、真实的用户行为模拟。本文提出的Agent4DL正是基于这一前沿方向，专门针对数字图书馆环境进行模拟。与现有模拟器（如SimIIR 2.0）相比，Agent4DL的独特性在于其利用LLM的先进能力，能生成更具多样性、上下文感知且贴合特定用户画像的搜索行为（包括查询、点击和停止），从而更逼真地模拟真实用户交互，并解决了因隐私问题导致的真实用户搜索数据稀缺的长期挑战。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Agent4DL的、基于大语言模型的生成式智能体模拟器来解决数字图书馆中用户搜索行为数据稀缺的问题。其核心方法是利用大语言模型的能力，创建能够逼真模拟学术用户搜索、点击和停止等行为的智能体，从而生成高质量、多样化的模拟数据集。

整体框架围绕智能体与数字图书馆环境的交互展开。核心架构设计包括三个主要模块：用户画像模块、记忆模块和交互模块。用户画像模块负责赋予智能体个性化的学术特征和研究兴趣。它从基准数据集初始化，量化定义了四个关键学术特征：深度（阅读深入程度）、广度（主题多样性）、近因偏好（对新文献的倾向）和跨学科性。每个特征将用户分为三个等级，并结合用户历史交互文档，利用大语言模型提炼出自然语言描述的研究兴趣。记忆模块模拟人类的认知与情感记忆，包含事实记忆（记录查询、浏览等行为）和情感记忆（记录对搜索结果的满意度、对复杂查询的挫败感等）。该模块支持记忆的检索、写入和基于情感的自我反思操作，使智能体能够基于过往经验进行决策。交互模块则定义了智能体在搜索环境中的具体行为，分为搜索驱动行为（如生成查询、评估和点击文档）和情感驱动行为（如评估搜索体验、决定是否停止搜索）。该模块利用ReAct（推理-行动）框架，在每一轮交互中，智能体根据当前上下文进行推理，生成停止、查询或点击等动作。

关键技术体现在多个方面。首先，在行为模拟上，采用任务特定的提示模板和ReAct方法，引导大语言模型进行逐步推理和行动，确保了模拟过程的稳定性和可控性。其次，在个性化建模上，通过精细量化的用户画像和双记忆系统，使智能体能够展现出复杂、一致且个性化的行为模式。第三，在环境构建上，设计了文档相关性生成和搜索结果呈现机制。相关性基于历史交互推断，同时利用大语言模型生成文档主题和摘要，并通过少样本学习对文档进行学科分类以检测和规避大语言模型的幻觉问题，确保模拟的可靠性。搜索结果呈现模拟了真实数字图书馆的分页、排序和过滤功能。最后，其创新点在于首次为数字图书馆场景构建了集成了深度个性化画像、情感记忆和认知推理能力的生成式智能体模拟器。它不仅能模拟表面的搜索动作，还能捕捉内在的研究偏好、情感状态和基于经验的决策过程，从而生成比现有模拟器（如SimIIR 2.0）更多样化、更贴合上下文的行为数据，为评估搜索算法提供了更真实的测试平台。

### Q4: 论文做了哪些实验？

论文实验主要围绕评估Agent4DL模拟数字图书馆用户搜索行为的有效性展开。实验设置包括使用RoBERTa排序模型，训练5个epoch，批次大小为128，学习率为5e-6，输入为历史行为序列、当前查询和候选文档的拼接，输出相关性分数。评估指标为平均倒数排名（MRR）和归一化折损累积增益（nDCG@1, nDCG@3）。

数据集/基准测试采用两个数字图书馆的真实用户数据：Sowiport用户搜索会话数据集（SUSS，含约48.4万会话）和EconBiz数据集（约42万会话）。对比方法包括传统检索模型BM25、基于SUSS和EconBiz训练的RoBERTa模型，以及用户模拟器SimIIR和SimIIR 2.0。在查询生成任务中还比较了Popular Selection、Random Selection和Discriminative Selection等基线策略。

主要结果如下：在偏好预测和相关性预测任务中，使用Agent4DL生成数据训练的模型（即使仅1000个会话）均优于基线。例如，偏好预测任务中，Agent4DL_3000的MRR达41.32，nDCG@1为22.66，nDCG@3为35.19，高于BM25（34.89, 15.12, 26.03）及其他RoBERTa基线。在查询行为评估中，Agent4DL的术语重叠率（τ）达0.87，BLEU为0.40，BERTScore为0.83，显著优于其他方法。点击和停止行为预测方面，Agent4DL在准确率（点击84.14%，停止84.14%）和精确率（停止82.90%）上表现突出，但召回率相对较低。数据增强实验显示，结合学术特征和研究兴趣的Agent4DL生成数据能提升模型性能，如MRR从59.12提升至64.37。这些结果表明Agent4DL能有效模拟多样且上下文感知的用户行为。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于对数字图书馆元数据的强依赖，以及当前模型未能完全模拟学术信息寻求的复杂性。未来研究可探索以下方向：首先，开发元数据增强技术，利用知识图谱或弱监督方法补全稀疏信息，降低对高质量元数据的依赖。其次，扩展智能体的行为空间，纳入引文链追踪、跨会话学习、偶然性浏览等真实学术搜索行为，使模拟更贴近现实。此外，可研究隐私保护下的真实用户行为融合方法，如差分隐私或联邦学习，在保护隐私的同时提升模拟真实性。针对领域知识滞后问题，可构建动态更新的学术知识库，并针对特定学科微调语言模型。最后，将模拟器与强化学习结合，让智能体通过与环境互动自主优化搜索策略，可能催生更自适应、个性化的数字图书馆服务。

### Q6: 总结一下论文的主要内容

该论文针对数字图书馆研究中因隐私问题导致的真实用户搜索行为数据稀缺的挑战，提出了一个名为Agent4DL的新型用户搜索行为模拟器。其核心贡献是利用基于大语言模型（LLM）的智能体来生成大规模、逼真的用户搜索行为数据。方法上，Agent4DL通过设计策略构建详细的用户画像，并模拟出包含查询、点击和停止等动态搜索会话，这些行为能够紧密贴合特定用户画像，生成多样且上下文感知的交互。实验表明，该模拟器能有效生成真实、多样的用户行为，其性能在与真实数据对比及与现有模拟器（如SimIIR 2.0）的比较中具有竞争力。主要结论是，Agent4DL不仅能提升信息检索任务的效果，尤其在稀疏数据集场景下，还能在尊重用户隐私的前提下为相关研究提供支持。此外，研究团队还发布了配套的模拟数据集Agent4DLData，以推动该领域发展，这项工作为探索数字图书馆用户搜索行为提供了新视角，有助于搜索技术和用户体验的优化。
