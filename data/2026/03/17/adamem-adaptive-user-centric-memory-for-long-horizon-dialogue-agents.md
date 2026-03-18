---
title: "AdaMem: Adaptive User-Centric Memory for Long-Horizon Dialogue Agents"
authors:
  - "Shannan Yan"
  - "Jingchen Ni"
  - "Leqi Zheng"
  - "Jiajun Zhang"
  - "Peixi Wu"
  - "Dacheng Yin"
  - "Jing Lyu"
  - "Chun Yuan"
  - "Fengyun Rao"
date: "2026-03-17"
arxiv_id: "2603.16496"
arxiv_url: "https://arxiv.org/abs/2603.16496"
pdf_url: "https://arxiv.org/pdf/2603.16496v1"
categories:
  - "cs.CL"
tags:
  - "对话Agent"
  - "记忆系统"
  - "个性化"
  - "长程推理"
  - "检索增强生成"
  - "用户建模"
relevance_score: 8.0
---

# AdaMem: Adaptive User-Centric Memory for Long-Horizon Dialogue Agents

## 原始摘要

Large language model (LLM) agents increasingly rely on external memory to support long-horizon interaction, personalized assistance, and multi-step reasoning. However, existing memory systems still face three core challenges: they often rely too heavily on semantic similarity, which can miss evidence crucial for user-centric understanding; they frequently store related experiences as isolated fragments, weakening temporal and causal coherence; and they typically use static memory granularities that do not adapt well to the requirements of different questions. We propose AdaMem, an adaptive user-centric memory framework for long-horizon dialogue agents. AdaMem organizes dialogue history into working, episodic, persona, and graph memories, enabling the system to preserve recent context, structured long-term experiences, stable user traits, and relation-aware connections within a unified framework. At inference time, AdaMem first resolves the target participant, then builds a question-conditioned retrieval route that combines semantic retrieval with relation-aware graph expansion only when needed, and finally produces the answer through a role-specialized pipeline for evidence synthesis and response generation. We evaluate AdaMem on the LoCoMo and PERSONAMEM benchmarks for long-horizon reasoning and user modeling. Experimental results show that AdaMem achieves state-of-the-art performance on both benchmarks. The code will be released upon acceptance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在长程对话中，其外部记忆系统存在的核心缺陷。随着对话智能体需要处理更开放、更持久的交互，记忆模块变得至关重要。然而，现有方法主要依赖基于语义相似性的检索，这存在三个主要不足：首先，过度依赖语义匹配可能遗漏对理解用户至关重要的非语义证据（如稳定偏好、个人特质）；其次，相关经验常被存储为孤立片段，削弱了事件间的时间与因果连贯性；最后，多数系统采用静态的记忆粒度（如固定长度的文本块），无法根据不同问题的需求自适应地调整检索策略和记忆结构，导致检索结果要么包含过多无关信息，要么割裂了事件间的依赖关系。

因此，本文的核心问题是：如何为长程对话智能体构建一个**以用户为中心、结构自适应**的记忆框架，以克服上述局限性，实现更精准、连贯且个性化的信息检索与响应生成。为此，论文提出了AdaMem框架，通过组织工作记忆、情景记忆、人物记忆和图记忆等多种结构化记忆，并设计一个基于条件检索与多智能体协作的管道，来动态、有针对性地整合证据，从而提升长程推理和用户建模的能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：记忆系统设计、结构化记忆表示以及多智能体协作方法。

在**记忆系统设计**方面，早期工作主要通过分块处理来扩展上下文长度。后续研究如MemGPT引入了分页和分段机制来管理长期记忆，而Mem0则将记忆抽象为独立的层进行管理。这些方法为长程交互提供了基础，但通常依赖静态检索策略或非结构化存储，可能导致信息碎片化。本文提出的AdaMem框架则通过整合工作记忆、情景记忆、人物记忆和图记忆，构建了一个统一的自适应系统，以更好地保持时序和因果连贯性。

在**结构化记忆表示**方面，相关研究探索了基于图的记忆（如A-Mem）和基于事件或时序知识图谱的语义记忆结构（如Zep），旨在提升信息组织能力。然而，这些方法往往过于依赖语义相似性检索，可能忽略以用户为中心的关键证据。AdaMem在此基础上，引入了关系感知的图扩展检索，仅在需要时结合语义检索，从而更灵活地适应不同问题的需求。

在**多智能体协作方法**方面，近期研究利用多智能体LLM通过角色 specialization 和协作来解决复杂任务。例如，MIRIX尝试使用专用智能体进行记忆组织，但缺乏确保长期记忆一致性的显式机制。本文借鉴了角色 specialization 的思想，但专注于以用户为中心的记忆构建和问题条件检索，通过角色专门化的证据合成与响应生成流程，增强了长程对话中的用户建模和推理能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AdaMem的自适应用户中心记忆框架来解决现有记忆系统面临的三大核心挑战：过度依赖语义相似性、记忆片段孤立以及静态记忆粒度。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块：**
AdaMem采用一个端到端的管道，包含四个紧密耦合的组件：记忆构建、问题条件检索规划、证据融合和响应生成。整个系统围绕三个专门的智能体（Agent）进行角色化协作：
1.  **记忆智能体（Memory Agent）**：负责在线处理对话历史。它将每个话语解析为包含摘要、主题、态度、原因、事实片段、属性等信息的规范化记录，并以此为基础更新四种结构化记忆。这四种记忆按参与者（用户和助手）分别组织成记忆束，包括：
    *   **工作记忆**：一个有限容量的先进先出缓冲区，保存近期对话上下文。
    *   **情景记忆**：长期的结构化记录，存储事件、事实、属性和主题摘要。
    *   **人设记忆**：从情景证据中提炼出的、相对稳定的用户偏好和特征概要。
    *   **图记忆**：一个异构知识图，连接消息、主题、事实、属性等节点，支持关系感知的检索。
2.  **研究智能体（Research Agent）**：在问答时负责证据收集与合成。它遵循“规划→搜索→整合→反思”的循环：首先分解回答问题所需的信息，然后通过统一的检索接口发起一轮或多轮检索，整合证据形成研究摘要，并判断是否需要进一步搜索。
3.  **工作智能体（Working Agent）**：负责将研究摘要转化为最终简洁的答案，必要时辅以高置信度的人设属性或事实片段作为补充。

**核心创新点与关键技术：**
1.  **异构、结构化的记忆组织**：通过工作、情景、人设和图记忆的四层设计，系统同时保留了近期上下文、结构化长期经验、稳定用户特征和关系感知连接，解决了记忆片段孤立和缺乏时序/因果连贯性的问题。
2.  **自适应的、问题条件的检索规划**：在推理时，系统首先解析问题的目标参与者。然后，生成一个**问题条件检索路线计划**，该计划动态决定是否以及如何进行图扩展（如传播跳数、激活的种子节点、使用的边类型先验等）。这使得简单的事实性问题主要依赖轻量级语义检索，而涉及时序或因果的复杂问题则触发更广泛的结构化图探索，从而实现了记忆检索粒度的自适应。
3.  **目标感知的混合检索与融合机制**：检索分为基线检索和图检索。基线检索从人设摘要、情景事实和主题链接的消息中聚合语义候选。图检索则在需要时，从图记忆中的种子节点出发，进行有界多跳扩展以发现关系证据。两者通过一个加权公式进行融合，公式综合考虑了基线得分、图得分、时间新近性先验和事实支持奖励，确保了证据的全面性与相关性。
4.  **规范化的写入与记忆巩固流程**：所有记忆更新都基于统一的规范化记录，减少了不同记忆模块间的提示漂移。工作记忆到情景记忆的巩固基于时间顺序而非问题显著性，防止了未来问题对记忆选择产生隐式影响。巩固过程中，路由器模块（预测ADD/UPDATE/IGNORE）和后续的主题重组、人设刷新机制，共同实现了从细粒度证据到高层摘要的自动化提炼与组织。
5.  **角色专门化的流水线协作**：将记忆管理、证据研究、答案生成分离给三个专门的智能体，使每个环节可以针对其角色进行优化，同时通过统一的记忆接口保持紧密耦合，确保了系统在长程推理和用户建模中的高效与准确性。

### Q4: 论文做了哪些实验？

论文在LoCoMo和PERSONAMEM两个基准上进行了实验评估。实验设置方面，使用了闭源模型（GPT-4.1-mini和GPT-4o-mini）和开源模型（Qwen3-4B-Instruct和Qwen3-30B-A3B-Instruct）作为骨干网络，在NVIDIA RTX A800 GPU上运行。关键参数包括：温度固定为0，检索top-k设为10，最大检索迭代次数Li为2，记忆嵌入使用all-MiniLM-L6-v2模型。

对比方法包括五个代表性的开源记忆框架：MemGPT、A-Mem、Mem0、LangMem和Zep。在LoCoMo基准上，主要评估指标为F1和BLEU-1。使用GPT-4.1-mini时，AdaMem取得了44.65%的整体F1分数，相比之前的最佳方法提升了4.4%；在时序问题上提升最大，F1提高了23.4%。使用GPT-4o-mini时，整体F1为41.84%，相对提升达12.8%。在PERSONAMEM基准上（使用准确率评估），AdaMem取得了63.25%的准确率，相对最佳基线提升5.9%，在“泛化到新场景”任务上提升尤为显著（27.3%）。

消融实验表明，移除图记忆、融合模块或多智能体响应管道均会导致性能下降，其中图记忆的影响最大（整体F1从44.65降至42.63）。超参数分析显示，默认设置（K=10，Li=2）在性能与效率间取得了良好平衡。效率分析指出，AdaMem虽非计算成本最低的方法（输入令牌2248，延迟4.722秒），但其在推理质量上具有显著优势（F1比Mem0高7.57）。

### Q5: 有什么可以进一步探索的点？

该论文提出的AdaMem框架在提升长程对话理解方面效果显著，但其局限性也为未来研究提供了明确方向。首先，系统复杂性和延迟问题突出，多级记忆结构与自适应检索虽提升了精度，却增加了计算与通信开销，未来可探索更轻量化的记忆融合机制或动态计算资源分配策略。其次，框架高度依赖上游解析模块（如实体链接、时间归一化），错误易传播且难以纠正，未来可研究端到端的联合训练方案，或引入不确定性感知模块以增强鲁棒性。此外，当前记忆组织仍以文本为中心，未来可整合多模态信息（如用户交互行为、情感变化）以更全面建模用户画像。最后，个性化与通用性的平衡值得深入探索：如何使系统在适应用户长期偏好的同时避免过度拟合，并支持跨领域、跨场景的迁移能力，将是实现更通用对话Agent的关键。

### Q6: 总结一下论文的主要内容

该论文提出了AdaMem，一种面向长程对话代理的自适应用户中心记忆框架。针对现有记忆系统过度依赖语义相似性、存储孤立片段以及使用静态记忆粒度的问题，AdaMem设计了工作记忆、情景记忆、人物记忆和图记忆四种记忆模块，以统一框架保存近期上下文、结构化长期经验、稳定用户特征及关系感知连接。其方法核心在于推理时先确定目标参与者，再构建结合语义检索与按需关系感知图扩展的问题条件检索路径，最后通过角色专精的证据合成与响应生成管道产生答案。实验表明，AdaMem在长程推理和用户建模基准测试中取得了最先进的性能，验证了自适应记忆组织与检索对复杂多轮交互的价值，推动了对话代理记忆系统向更自适应、问题感知和用户中心的设计方向发展。
