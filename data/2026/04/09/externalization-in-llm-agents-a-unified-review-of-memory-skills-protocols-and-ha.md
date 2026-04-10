---
title: "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"
authors:
  - "Chenyu Zhou"
  - "Huacan Chai"
  - "Wenteng Chen"
  - "Zihan Guo"
  - "Rong Shan"
  - "Yuanyi Song"
  - "Tianyi Xu"
  - "Yingxuan Yang"
  - "Aofan Yu"
  - "Weiming Zhang"
  - "Congming Zheng"
  - "Jiachen Zhu"
  - "Zeyu Zheng"
  - "Zhuosheng Zhang"
  - "Xingyu Lou"
  - "Changwang Zhang"
  - "Zhihui Fu"
  - "Jun Wang"
  - "Weiwen Liu"
  - "Jianghao Lin"
date: "2026-04-09"
arxiv_id: "2604.08224"
arxiv_url: "https://arxiv.org/abs/2604.08224"
pdf_url: "https://arxiv.org/pdf/2604.08224v1"
categories:
  - "cs.SE"
  - "cs.MA"
tags:
  - "Agent Architecture"
  - "Agent Memory"
  - "Agent Skills"
  - "Interaction Protocols"
  - "Agent Infrastructure"
  - "Agent Harness"
  - "Survey"
  - "Cognitive Artifacts"
  - "Externalization"
  - "Agent Systems"
relevance_score: 9.5
---

# Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

## 原始摘要

Large language model (LLM) agents are increasingly built less by changing model weights than by reorganizing the runtime around them. Capabilities that earlier systems expected the model to recover internally are now externalized into memory stores, reusable skills, interaction protocols, and the surrounding harness that makes these modules reliable in practice. This paper reviews that shift through the lens of externalization. Drawing on the idea of cognitive artifacts, we argue that agent infrastructure matters not merely because it adds auxiliary components, but because it transforms hard cognitive burdens into forms that the model can solve more reliably. Under this view, memory externalizes state across time, skills externalize procedural expertise, protocols externalize interaction structure, and harness engineering serves as the unification layer that coordinates them into governed execution. We trace a historical progression from weights to context to harness, analyze memory, skills, and protocols as three distinct but coupled forms of externalization, and examine how they interact inside a larger agent system. We further discuss the trade-off between parametric and externalized capability, identify emerging directions such as self-evolving harnesses and shared agent infrastructure, and discuss open challenges in evaluation, governance, and the long-term co-evolution of models and external infrastructure. The result is a systems-level framework for explaining why practical agent progress increasingly depends not only on stronger models, but on better external cognitive infrastructure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大型语言模型（LLM）智能体（Agent）研究与实践中的一个核心问题：如何系统性地理解和解释智能体设计从依赖模型内部参数（权重）转向依赖外部化基础设施（如记忆存储、技能库、交互协议和运行时管理框架）这一根本性转变。研究背景是，随着LLM能力的提升，构建实用智能体的关键已不再仅仅是增大模型规模或改进训练方法，而是如何重组模型运行时的环境，将原本期望模型内部处理的各种认知负担外部化。

现有方法通常孤立地关注智能体的某个组件，例如检索增强生成（RAG）、工具学习或特定交互协议，缺乏一个统一的理论框架来解释这些分散的技术进步为何共同推动了智能体可靠性的提升。这些方法未能阐明，将状态、程序性知识和交互结构外部化，本质上是一种“表征转换”，它改变了任务呈现给模型的形式，从而让模型能够更可靠地利用其现有能力解决问题。

因此，本文要解决的核心问题是：提供一个系统级的分析框架，以“外部化”为核心组织原则，统一审视和解释智能体在记忆、技能和协议这三个维度上的设计演进，并强调“驾驭层工程”（Harness Engineering）作为协调这些外部化模块的统一运行时环境的关键作用。论文试图论证，可靠智能体的实现不仅依赖于更强大的模型，更取决于构建更好的外部认知基础设施，这一过程与人类文明通过语言、文字、印刷术和数字计算进行认知外部化的历史逻辑相呼应。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕LLM Agent能力外部化的三个核心维度展开，即记忆、技能和协议，并置于从“权重”到“上下文”再到“治理框架”的历史演进脉络中。相关研究可按类别梳理如下：

**1. 权重层相关研究：**
此阶段的研究聚焦于模型参数本身，认为能力主要内化于权重中。代表性工作包括基于大规模语料预训练的大模型（如GPT-4、Gemini），以及通过监督微调（SFT）和偏好优化（如DPO）来对齐模型行为的研究。本文认为，尽管权重层提供了强大的通用能力和快速推理优势，但其知识更新、模块化管理和个性化服务方面存在固有局限，这推动了能力外部化的需求。

**2. 上下文层相关研究：**
此阶段研究重心转向通过设计输入（提示）来改变模型行为，而无需修改权重。关键工作包括：提示工程、思维链（Chain-of-Thought）、ReAct（将推理与工具使用交织）、思维树（Tree of Thoughts）、自优化（Self-Refine）以及检索增强生成（RAG）。本文指出，这些方法将部分认知负担（如知识检索）转移到上下文，实现了从“回忆”到“识别”的转换。但其受限于上下文长度、信息管理成本和状态的短暂性。

**3. 治理框架层相关研究：**
这是当前阶段的核心，研究重点转向构建围绕模型的持久化外部基础设施以提升可靠性。本文系统性地将相关研究归纳为三类外部化形式：
*   **记忆外部化**：涉及将状态跨时间持久化的工作，如Reflexion跨回合持久化反馈，以及各类外部记忆存储系统。
*   **技能外部化**：涉及将程序性专业知识封装为可重用模块的工作，例如在编码代理（如SWE-agent、OpenHands）和研究代理中使用的可复用技能工件。
*   **协议外部化**：涉及规范交互结构的工作，例如AutoGen形式化了多智能体消息交换，MetaGPT引入了基于角色的协作和显式流程，CAMEL探索了任务分解的结构化对话。

此外，像Auto-GPT、BabyAGI这样的早期项目，以及Voyager、LangGraph、CrewAI、OS-Copilot等体现工作流和具身系统的框架，都展示了通过治理框架（而非仅靠提示）来解决可靠性问题的共同模式。

**本文与这些工作的关系和区别：**
本文并非提出新的具体技术，而是提供了一个统一的**系统级框架**，用以理解和整合上述分散的研究进展。它将记忆、技能和协议明确归纳为治理框架下三种相互关联但不同的外部化维度，并强调“治理框架工程”是当前智能体工程的核心。本文的贡献在于从“认知外化”的理论视角，阐释了LLM智能体能力演进的内在逻辑——即通过构建外部认知基础设施，将模型不擅长的负担（如长期状态保持、过程一致性、交互协调）转化为其更擅长处理的形式，从而形成一个更大的认知系统。

### Q3: 论文如何解决这个问题？

论文通过“外部化”这一核心框架来解决LLM智能体能力构建的难题，即不再主要依赖改变模型权重，而是将运行时环境重组，把原本期望模型内部恢复的能力外置到记忆存储、可复用技能、交互协议以及确保这些模块可靠运行的“治理框架”中。

**核心方法与架构设计：**
论文提出一个系统级的框架，将外部化分为四个相互关联但概念独立的层面，并由治理框架统一协调：
1.  **记忆**：外部化状态，解决时间连续性负担。它将代理的状态从瞬态上下文中解耦，具体化为四个持久化维度：**工作上下文**（当前任务的实时中间状态）、**情景经验**（过往运行记录）、**语义知识**（跨情景的抽象知识）和**个性化记忆**（用户/环境特定信息）。其架构演进经历了从**单体上下文**、**带检索的上下文存储**、**分层记忆与编排**（引入提取、巩固、遗忘等主动管理生命周期），到**自适应记忆系统**（动态模块、基于反馈的策略优化）的历程，核心是从被动存储转向主动控制。
2.  **技能**：外部化程序性专业知识。它将重复性的操作模式从具体的执行轨迹中抽象出来，封装为可复用的过程性指导。技能层依赖于记忆层提供的证据基础（如成功轨迹），并反过来将新的执行痕迹写回记忆。
3.  **协议**：外部化交互结构。它定义了智能体与工具、环境或其他智能体之间标准化、受治理的交互规则（如工具调用格式、审批流程、委托机制），将复杂的协调逻辑从模型的推理负担中剥离。
4.  **治理框架**：作为统一层，它协调上述三者，确保可靠、受控的执行。它管理记忆的读写与权限、技能的调用与组合、协议的遵循与路由，并将运行时的状态（如工具输出、审批结果）规范化后写入持久化记忆。

**关键技术要点与创新点：**
*   **认知负担的转化**：核心创新在于将外部化视为一种**认知负担的转化**，而非简单的功能附加。它将模型内部难以可靠解决的“硬认知负担”（如长期状态保持、复杂程序执行、结构化交互）转化为外部基础设施可以更有效处理的形式（如数据库查询、代码函数调用、API协议）。
*   **分层解耦与协同**：清晰定义了记忆、技能、协议三者的角色与边界，并强调它们在治理框架下的协同。记忆是持久化证据库，技能是抽象化的程序，协议是交互的规则，三者通过治理框架形成读写与控制的闭环。
*   **从容量管理到策略优化**：在记忆方面，论文指出演进方向是从解决信息“存在”和“容量”问题，转向解决“组织”和“访问策略”问题。自适应记忆系统利用混合专家、强化学习等技术动态优化检索与存储策略，体现了这一趋势。
*   **治理框架作为新核心**：论文强调，在“治理框架时代”，智能体的进步不仅依赖于更强的模型，更依赖于更好的外部认知基础设施。治理框架成为协调一切、确保可靠执行的“操作系统”，记忆则成为其管理下的状态基础设施。

总之，论文通过构建一个以“外部化”和“治理框架”为中心的系统框架，为解决LLM智能体的长期连续性、复杂技能复用和可靠交互问题提供了一条清晰的工程化与系统化路径。

### Q4: 论文做了哪些实验？

该论文是一篇综述性研究，并未设计具体的实验。因此，它不包含传统意义上的实验设置、数据集或对比方法。其主要工作是对LLM智能体领域“外部化”趋势的系统性回顾与分析。

论文的核心内容是构建一个理论框架，将智能体的关键组件——记忆、技能、协议和治理工程——统一视为“外部化认知”的不同形式。作者通过历史追溯（从权重到上下文再到治理层）和概念分析，论证了基础设施如何将复杂的认知负担转化为模型能更可靠处理的形式，从而驱动智能体的实际进展。

文中讨论的主要“结果”是提出的系统性观点和识别出的未来方向。关键论点包括：智能体的进步日益依赖于外部认知基础设施而不仅是模型本身；记忆、技能、协议三者是相互耦合的外部化形式；在参数化能力与外部化能力之间存在权衡。论文最后指出了评估、治理、模型与基础设施协同进化等开放挑战，以及自我进化治理层、共享智能体基础设施等新兴方向。

### Q5: 有什么可以进一步探索的点？

这篇论文虽然系统性地阐述了外部化在LLM智能体中的关键作用，但仍有几个方向值得深入探索。首先，论文指出了评估、治理和长期协同演化的开放挑战，这暗示着当前缺乏一个统一的框架来衡量外部化组件（如记忆、技能）对智能体整体性能的真实贡献，以及它们如何影响系统的可解释性和安全性。其次，关于“自我演化的治理框架”这一新兴方向，论文提及但未深入，这为未来研究提供了空间：如何设计智能体使其能动态评估并优化自身的外部化结构，例如自动管理记忆的存储与遗忘，或根据任务需求组合技能。此外，论文强调了外部化与参数化能力之间的权衡，但未详细探讨在资源受限场景（如边缘计算）下如何实现最优平衡，这可以结合轻量化架构或选择性外部化来研究。最后，从系统整合角度看，不同外部化模块（如记忆与协议）间的耦合机制仍不明确，未来可探索更高效的协调策略，以提升智能体的鲁棒性和适应性。

### Q6: 总结一下论文的主要内容

这篇论文以“外部化”为核心视角，系统性地回顾和分析了LLM智能体设计范式的转变。论文的核心论点是：当前LLM智能体能力的提升，主要不是通过改变模型权重，而是通过将认知负担从模型内部计算转移到持久、可检查、可重用的外部结构中实现的，这一过程即“外部化”。这构成了理解智能体在记忆、技能、协议和系统工程方面进展的统一框架。

论文将外部化具体分为三个维度：**记忆系统**将状态跨越时间外部化，解决了连续性难题，将回忆任务转化为更可靠的识别任务；**技能系统**将程序性专业知识外部化，将隐性的操作指南转化为显性、可重用的组件，解决了执行方差问题；**协议**将交互结构外部化，为工具、服务及多智能体间的交互定义了明确的机器可读合约，解决了协调难题。而**系统工程**则是将这些外部化模块整合成连贯运行时环境的统一层，提供编排、约束和可观测性。

论文的主要结论是，可靠智能体的实现不仅依赖于更强大的基础模型，更取决于能否通过外部认知基础设施系统地重构任务需求。这种从权重到上下文，再到系统工程的演进路径，与人类认知外部化的历史（从语言、文字到数字计算）形成了递归类比。论文最后探讨了参数化能力与外部化能力之间的权衡，并指出了自演进系统、共享基础设施以及评估与治理等未来挑战。
