---
title: "CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments"
authors:
  - "Jiaju Chen"
  - "Bo Sun"
  - "Yuxuan Lu"
  - "Yun Wang"
  - "Dakuo Wang"
  - "Bingsheng Yao"
date: "2026-06-04"
arxiv_id: "2606.06399"
arxiv_url: "https://arxiv.org/abs/2606.06399"
pdf_url: "https://arxiv.org/pdf/2606.06399v1"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "协作能力评估"
  - "CSCW"
  - "LLM Agent仿真框架"
  - "受控实验"
  - "协作智能体"
relevance_score: 7.5
---

# CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments

## 原始摘要

Multi-agent systems (MAS) built on large language models have shown growing promise, with their effectiveness resting on agents' ability to coordinate through text-based channels much as human teams do. Yet recent study suggests that MAS often falter not because agents lack individual task-solving ability, but because they lack collaborative competence: the capacity to establish common ground, maintain shared task understanding, balance individual and collective incentives, and repair misalignment as interaction unfolds. Decades of research in Computer-Supported Cooperative Work have characterized these requirements for human teams coordinating under constrained communication, yet existing MAS evaluations focus mainly on task outcomes or single-agent proficiency in reasoning, planning, and tool use. To enable a systematic analysis of agents' collaborative competence in MAS, we introduce CollabSim, a configurable simulation framework that combines a theory-grounded definition of collaborative capabilities, controlled manipulation of interaction conditions, and action-level probing of agents' internal states. Experiments across four LLMs show that CollabSim can capture condition effects, separate model performance patterns, and reveal task-dependent effects of agent design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的问题是：当前基于大语言模型的多智能体系统（MAS）在协作任务中频繁失败，但其根本原因并非单个智能体的任务解决能力不足，而是缺乏协作能力——即建立共同基础、维护共享任务理解、平衡个体与集体激励以及在交互过程中修复认知偏差的能力。尽管计算机支持的协同工作（CSCW）领域数十年的研究已揭示了人类团队在有限通信条件下所需的核心协作能力，但现有的MAS评估方法主要关注任务结果或单一智能体的推理、规划与工具使用能力，无法诊断交互过程中产生的协作失败。因此，本文的核心目标是引入一种基于CSCW理论的可配置模拟框架CollabSim，通过控制交互条件、结合基于理论定义的协作能力评估与智能体内部状态的动作级探测，实现对LLM智能体协作能力的系统性分析。

### Q2: 有哪些相关研究？

在相关研究中，本文主要关注LLM多智能体系统的协作能力评估，现有工作可分为三类：

1. **任务导向的评测基准**：如MultiAgentBench等框架通过设置协作任务评估团队级任务完成效果。本文指出这些方法过度聚焦于任务结果而非协作过程本身，难以揭示智能体在建立共同理解、修复沟通失误等协作核心环节的缺陷。

2. **角色扮演式社会模拟**：SOTOPIA等框架通过预设社交情境考察智能体的社交智能。本文认为这类工作虽能产生丰富的交互轨迹，但将协作条件固化为静态设计选择，缺乏对通信约束、激励机制等可控变量的实验性操控。

3. **动态多智能体架构**：现有系统如软件工程、科学推理等领域的应用，将协作视为提升任务效率的手段而非研究对象。本文区别于这些工作，首次从CSCW理论出发，系统定义"协作能力"的可操作维度（如共同基础建立、个体-集体利益平衡等），并通过配置化实验框架CollabSim实现对协作条件（如通信带宽、任务相互依赖性）的受控操作与智能体内部状态的细粒度探测。

### Q3: 论文如何解决这个问题？

CollabSim通过结合CSCW理论基础、受控交互条件操作和动作级内部状态探测，系统性地分析LLM多智能体系统的协作能力。其核心方法包含三个关键设计：首先，基于CSCW理论定义五类协作能力维度（建立共同基础、维护共享任务理解、平衡个体与集体激励、修复交互失调、协调受限通信），形成可量化的评估框架；其次，设计受控实验范式，允许研究人员操纵交互条件变量（如通信带宽、任务复杂度、信息不对称程度），通过条件对比揭示协作绩效的影响因素；最后，实现动作级内部状态探测机制，实时记录每个智能体的决策路径、信念更新和通信行为，支持细粒度分析。

架构上，CollabSim包含三个主要模块：环境配置模块负责定义任务场景（如协作规划、资源共享）和交互约束条件；智能体编排模块支持自定义LLM实例的初始知识库、角色分工和策略配置；分析管线模块则通过日志捕获智能体的每步动作，结合CSCW理论标签体系进行自动编码。关键技术包括：引入共享心智模型量化指标，通过对比不同LLM基础模型（如GPT-4、Claude）在协作任务中的表现差异，分离出模型自身推理能力与协作机制的影响；设计任务依赖性检测方法，揭示协作策略有效性随任务类型（如时空协调vs信息整合）的动态变化。实验证明该方法能有效捕获条件效应、分离模型性能模式，并发现智能体设计（如提示工程策略）在不同任务中的差异化影响。

### Q4: 论文做了哪些实验？

论文在四个协作任务上进行了大规模实验。实验设置包括：1）四种大语言模型，涵盖开源（Qwen3.6-35B, Llama-4）和商业模型（GPT-5.5, Claude 4.6 Sonnet）；2）两种智能体设计：基于人设的基线智能体和基于协作理论指导的智能体；3）对三个交互变量进行系统控制：通信带宽、团队规模和信息可见性。

四个任务数据集/基准测试为：Shape Factory（平均财富，成交率，订单完成率，消息-交易比）、DayTrader（平均财富，合作率，共享池规模，消息数）、Hidden Profile（投票准确率，投票变化率，关键候选人提及率，平均消息长度）和Map Task（路线绘制准确率，通信效率，绘制修订率，消息数）。每个任务还包含探测维度，智能体每轮报告对共享任务理解的自我报告置信度。

主要结果显示：CollabSim能捕捉条件效应、分离模型性能模式、并揭示智能体设计的任务依赖效应。例如，在Shape Factory中，信息可见性条件下，人设/理论指导的GPT-5.5智能体平均财富达到331/335（最优），而理论指导的Claude 4.6成交率最高达64.7%。在DayTrader中，理论指导的Claude 4.6在9人团队中财富达15005且合作率64.3%，显著优于人设基线。通信带宽限制普遍降低合作率，而理论指导设计在多任务中带来性能提升。

### Q5: 有什么可以进一步探索的点？

这篇论文的局限性与未来研究方向主要体现在几个方面。首先，实验场景的覆盖面有限，仅选取了四个代表性社会科学实验，未来可引入更多经典协作任务（如沙漠生存任务、密码游戏）以增强结论的普适性。其次，模型与Agent设计的多样性不足，仅测试了四种LLM和两种基础架构，后续应纳入推理增强型模型（如o1）、小型开源模型以及配备记忆或规划模块的Agent，以探究不同能力层级与架构设计在协作条件中的交互效应。此外，当前实验成本较高，可探索更高效的采样或压缩对话轨迹的方法。在方法论层面，CollabSim对协作能力的测量主要依赖预定义的行为标签，未来可引入开放性行为编码或自适应条件调控机制，以捕捉更复杂的协作动态。最后，建议将人类协作基准纳入对比，使Agent的协作缺陷评估更具生态效度。

### Q6: 总结一下论文的主要内容

CollabSim是一个基于CSCW理论的多智能体协作能力评估框架，旨在系统分析LLM代理在文本交互中的协作能力。现有研究指出，多智能体系统的失败往往源于缺乏协作能力（如建立共识、维护共享任务理解、平衡个人与集体激励）而非个体任务解决能力。该框架通过可控实验设计，操纵沟通带宽、信息可见性和团队规模等交互条件，并在动作层级探测代理的内部状态（包括任务状态认知、伙伴意图理解及自身推理逻辑）。在四个LLM上的实验表明，CollabSim能够捕捉条件效应、区分模型性能模式，并揭示代理设计对任务依赖性的影响。核心贡献在于将协作能力从任务结果中解耦，提供过程级评估手段，为诊断LLM代理在受限通信条件下的有效协作提供了系统方法。结论强调协作能力无法简化为更强的任务解决能力，需通过连接任务结果、交互痕迹与内部状态进行综合评估。
