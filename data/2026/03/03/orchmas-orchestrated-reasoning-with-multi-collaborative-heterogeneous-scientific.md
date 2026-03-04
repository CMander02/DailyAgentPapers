---
title: "OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents"
authors:
  - "Yichao Feng"
  - "Haoran Luo"
  - "Zhenghong Lin"
  - "Yiqun Sun"
  - "Pengfei Wei"
  - "Lawrence B. Hsieh"
  - "Anh Tuan Luu"
date: "2026-03-03"
arxiv_id: "2603.03005"
arxiv_url: "https://arxiv.org/abs/2603.03005"
pdf_url: "https://arxiv.org/pdf/2603.03005v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "Agent架构"
  - "规划与推理"
  - "工具使用"
  - "科学推理"
  - "动态协作"
  - "异构模型集成"
relevance_score: 9.0
---

# OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents

## 原始摘要

Multi-agent large language model frameworks are promising for complex multi step reasoning, yet existing systems remain weak for scientific and knowledge intensive domains due to static prompts and agent roles, rigid workflows, and homogeneous model reliance, leading to poor domain adaptation, limited reasoning flexibility, and high latency on heterogeneous or long-horizon scientific tasks. They also struggle to revise earlier decisions when intermediate reasoning diverges, reducing reliability in structured and calculation heavy settings. To address these limitations, we propose a scientific domain oriented interactive two tier multi model orchestration framework. A dedicated orchestration model analyzes each task, dynamically constructs a domain aware reasoning pipeline, and instantiates specialized expert agents with tailored prompts, while an execution model performs each step under generated role and instruction specifications. The orchestrator iteratively updates the pipeline based on intermediate feedback, enabling dynamic replanning, role reallocation, and prompt refinement across multi turn interactions, strengthening robustness and specialization for scientific reasoning through structured heterogeneous model collaboration. The framework is model agnostic and supports heterogeneous LLM integration with different capacities or costs, enabling flexible performance efficiency trade offs in practical scientific deployments. Experiments show consistent improvements over existing multi agent systems and strong baselines across diverse reasoning and scientific style benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有基于大语言模型的多智能体系统在科学和知识密集型领域进行复杂推理时存在的关键局限性。研究背景是，尽管多智能体系统通过角色分工和协作来分解复杂任务，被视为一种有前景的范式，但现有方法在应对科学任务时表现不佳。现有方法的不足主要体现在三个方面：一是采用静态的角色模板和提示词，导致与具体任务的对齐度差，领域适应性弱；二是依赖人工设计、顺序固定的刚性工作流，不仅工程和维护成本高，而且缺乏灵活性，无法动态调整步骤，容易导致错误累积和传播；三是通常使用同质化的大模型来实例化所有智能体，这限制了真正的专业化，如果基础模型在某个科学领域存在偏差或知识不足，用其同时进行生成和验证会放大错误。

针对这些不足，本文要解决的核心问题是：如何构建一个能够动态适应、灵活协作且具备高度专业化的多智能体框架，以有效应对异构、多步、计算密集型的科学推理任务。为此，论文提出了OrchMAS框架，其核心创新在于引入了一个交互式的双层异构模型编排机制。该框架通过一个专用的编排模型来分析任务，动态构建领域感知的推理流水线，并为专门化的专家智能体生成定制化的提示词；执行模型则在生成的指令下执行具体步骤。编排器能够根据中间结果的反馈迭代更新流水线，实现动态重规划、角色重分配和提示词优化，从而增强科学推理的鲁棒性和专业性。该框架是模型无关的，支持集成不同能力或成本的大模型，以实现性能与效率的灵活权衡。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为多智能体系统（MAS）和推理增强技术两大类。

在多智能体系统方面，早期工作如AgentVerse提出了面向流水线的多智能体框架，通过智能体间的协调交互提升性能；后续研究如Self-Adaptive MAS进一步引入了自适应行为与动态协调策略。近期工作则训练专用控制器模型来管理智能体选择与流程执行，以提升跨领域任务的编排效率。本文提出的OrchMAS框架与这些工作一脉相承，但关键区别在于其针对科学领域进行了专门设计，通过双层编排架构（编排模型与执行模型）实现了动态的、领域感知的推理流水线构建，并能根据中间反馈进行迭代更新（如重新规划、角色重分配和提示词优化），从而克服了现有系统在提示词和角色静态、工作流僵化、模型同质化依赖等方面的局限。

在推理增强技术方面，思维链（CoT）推理和强化学习（RL）已被广泛用于提升多步推理和决策质量，例如在KBQA-o1和Search-R1等工作中用于增强复杂问答和搜索任务。这些方法将逐步推理与环境交互结合，允许模型迭代检索证据、修订计划并验证中间结论。本文框架吸收了这类迭代、反馈驱动的思想，但其核心创新在于将这种动态调整机制系统性地融入了异构专家智能体的结构化协作流程中，专注于解决计算密集、结构化的科学领域任务中早期决策难以修正的可靠性问题。此外，本文框架是模型无关的，支持集成不同能力或成本的异构大语言模型，以实现性能与效率的灵活权衡。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为OrchMAS的两层多模型编排框架来解决现有多智能体系统在科学领域适应性差、推理僵化、决策难以修正等问题。其核心方法围绕动态编排、异构专家协作和迭代反馈优化展开。

整体框架采用“协调器-工作者”范式，包含两个核心模块：**协调器模块（Coordinator Module）** 和**交互基底（Interaction Substrate）**。协调器（通常是一个LLM）作为中枢，负责分析任务、动态规划推理流程，并从角色库中为每一步选择最合适的专家角色（如研究员、数学求解器、验证者等）。交互基底则作为中介层，根据协调器指定的角色，将带有结构化指令的请求分派给相应的专家智能体（可以是不同能力或成本的异构LLM），并收集反馈。

关键技术体现在以下几个方面：
1.  **动态角色编排与流程构建**：协调器并非使用静态提示或固定工作流，而是根据任务内容和历史交互，在每一轮动态生成角色指派（σ_t）、推理思路（u_t^{reason}）和具体请求（u_t^{msg}）。这构成了一个可动态调整的“领域感知推理管道”。
2.  **结构化状态管理与迭代优化**：系统维护一个**协作状态流形（Collaborative State Manifold）**，编码了整个多轮交互的历史，包括所有角色分配、请求、反馈和协调决策。协调器基于此完整上下文进行后续规划和行动决策。关键在于，系统能根据中间步骤的反馈，对推理管道进行动态重规划、角色重分配和提示词优化，从而修正早期错误或偏离的推理路径。
3.  **双层提示架构与强化学习驱动**：操作上采用双层提示机制。策略模型（π_φ）遵循“思考→交互（指定agent_role）→观察”的多轮协议来驱动流程。外部LLM（M_ext）则接收动态构建的系统提示，其中由RL学习生成的自由格式的`agent_role`字符串决定其专业人设。协调器的策略通过**分层奖励的端到端强化学习**进行优化，奖励函数整合了**格式奖励（R_fmt）** 和**精度奖励（R_prec）**。格式奖励确保每一步的思考和请求结构良好、边界令牌正确；精度奖励则评估最终答案与标准答案的匹配度。两者通过门控聚合，确保只有在结构完全正确时才激活精度奖励，从而鼓励模型同时保证流程规范性和结果准确性。

创新点在于：1) 提出了一个面向科学领域的、支持动态重规划和迭代修正的交互式两层编排架构；2) 实现了完全由学习驱动的自由格式角色动态分配，而非预定义集合选择，增强了灵活性和领域适应性；3) 设计了结合结构合规性与答案准确性的分层奖励机制，并通过门控聚合和GRPO风格的目标函数进行整体优化，提升了训练稳定性和最终性能；4) 框架是模型无关的，支持集成不同能力或成本的异构LLM，实现了性能与效率的灵活权衡。

### Q4: 论文做了哪些实验？

实验设置方面，论文采用了两层架构：编排器基于Qwen3-4B模型，使用GRPO方法训练；执行器则部署了GPT-OSS-120B大模型。训练和推理分别在两个配备4块RTX A6000 GPU的节点上进行，最大提示长度设为8192个token，每次交互最多允许5轮代理交互。

数据集与基准测试涵盖了多种科学推理任务，包括分布内数据集（2WikiMultiHopQA、HotpotQA、GSM8K、DAPO、MusiQue、PopQA、BookSum、WritingPrompts）和分布外数据集（TriviaQA、MathQA、SQuAD v2、XSum），以评估多跳推理、数值计算、知识问答和长文本摘要等能力。

对比方法包括：直接提示基线（Qwen3-4B、GPT-4o-mini）、监督微调（SFT）、思维链提示（CoT）、基于GRPO的强化学习，以及先前的多代理系统优化方法（OPRO、TextGrad、GEPA）。

主要结果与关键指标显示，所提出的OrchMAS框架在各项基准上均一致优于所有基线方法。在分布内问答任务中，例如在2WikiMultiHopQA上，OrchMAS的F1和EM分别达到67.25和60.42，相比最佳多代理基线GEPA（F1 41.24，EM 37.50）有显著提升。在HotpotQA上，F1从47.13提升至61.99，EM从39.58提升至53.13。在更具挑战性的DAPO基准上，OrchMAS的F1/EM达到56.64/56.64，远高于GEPA的15.16/13.54。在摘要任务中，OrchMAS在BookSum、WritingPrompts和XSum上的余弦相似度得分分别为59.09、36.42和65.48，均领先于其他方法。消融分析进一步证实，动态代理角色、多轮推理和环境引导执行这三个关键组件都对最终性能有重要贡献，移除任一组件都会导致性能大幅下降。

### Q5: 有什么可以进一步探索的点？

该论文提出的OrchMAS框架在动态编排异构专家Agent方面有显著创新，但仍存在一些局限和可深入探索的方向。首先，其核心依赖一个“编排模型”来动态规划流程，该模型本身的决策能力与泛化性可能成为瓶颈；未来可研究如何引入更复杂的元认知机制或强化学习，使编排过程能基于历史任务表现进行自我优化。其次，框架虽支持异构模型，但未深入探讨不同模型在特定科学子领域（如符号计算、实验设计）的特化集成策略；可探索基于能力评估的模型自动匹配与组合机制，以进一步提升效率与精度。此外，系统在“修订早期决策”方面依赖于中间反馈，但未明确处理科学任务中常见的证据冲突或不确定性推理；未来可引入概率推理或辩论协商机制，使多Agent在分歧时能进行证据加权与共识形成。最后，实验评估集中于现有基准，未来需在真实长期科研工作流中验证其可持续协作能力，并考虑计算成本与延迟的平衡优化。

### Q6: 总结一下论文的主要内容

该论文提出了一种面向科学领域的交互式双层多模型编排框架OrchMAS，旨在解决现有多智能体大语言模型框架在科学和知识密集型任务中的局限性。核心问题是现有系统因静态提示与角色、僵化工作流及同质化模型依赖，导致领域适应性差、推理灵活性不足、延迟高，且在中间推理偏离时难以修正决策。

方法上，框架包含一个编排模型和一个执行模型。编排模型分析任务，动态构建领域感知的推理管道，实例化具有定制提示的专家智能体；执行模型则在生成的角色和指令规范下执行各步骤。关键创新在于编排器能基于中间反馈迭代更新管道，实现动态重规划、角色重分配和提示优化，通过结构化异构模型协作增强科学推理的鲁棒性和专业化。该框架与模型无关，支持集成不同能力或成本的异构大语言模型，以平衡性能与效率。

主要结论显示，实验在多种推理和科学风格基准测试中，该框架相比现有多智能体系统和强基线均取得持续改进。其意义在于提升了复杂科学任务中的动态适应性、推理可靠性和资源利用灵活性，为知识密集型领域的多智能体系统部署提供了实用解决方案。
