---
title: "CARD: Towards Conditional Design of Multi-agent Topological Structures"
authors:
  - "Tongtong Wu"
  - "Yanming Li"
  - "Ziye Tang"
  - "Chen Jiang"
  - "Linhao Luo"
date: "2026-03-01"
arxiv_id: "2603.01089"
arxiv_url: "https://arxiv.org/abs/2603.01089"
pdf_url: "https://arxiv.org/pdf/2603.01089v1"
github_url: "https://github.com/Warma10032/CARD"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "Multi-Agent Systems"
  - "Learning & Optimization"
relevance_score: 8.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "CARD (Conditional Agentic Graph Designer), AMACP protocol, conditional variational graph encoder"
  primary_benchmark: "HumanEval, MATH, MMLU"
---

# CARD: Towards Conditional Design of Multi-agent Topological Structures

## 原始摘要

Large language model (LLM)-based multi-agent systems have shown strong capabilities in tasks such as code generation and collaborative reasoning. However, the effectiveness and robustness of these systems critically depend on their communication topology, which is often fixed or statically learned, ignoring real-world dynamics such as model upgrades, API (or tool) changes, or knowledge source variability. To address this limitation, we propose CARD (Conditional Agentic Graph Designer), a conditional graph-generation framework that instantiates AMACP, a protocol for adaptive multi-agent communication. CARD explicitly incorporates dynamic environmental signals into graph construction, enabling topology adaptation at both training and runtime. Through a conditional variational graph encoder and environment-aware optimization, CARD produces communication structures that are both effective and resilient to shifts in model capability or resource availability. Empirical results on HumanEval, MATH, and MMLU demonstrate that CARD consistently outperforms static and prompt-based baselines, achieving higher accuracy and robustness across diverse conditions. The source code is available at: https://github.com/Warma10032/CARD.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的多智能体系统中，通信拓扑结构静态僵化、无法适应动态环境变化的核心问题。

研究背景是，LLM驱动的多智能体系统在代码生成、协作推理等复杂任务上展现出强大能力，但其性能高度依赖于智能体间的通信拓扑结构。现有方法主要分为两类：一是依赖人工设计的固定流水线或序列，虽在稳定场景下有效但缺乏灵活性；二是通过“文本梯度”反向传播或可微分模块自动学习拓扑，但这些方法通常假设环境是静态的。现有方法的不足在于，它们忽略了现实世界中模型升级、API（或工具）变更、知识源波动等动态因素。当这些条件变化时，静态或简单学习得到的拓扑结构会变得脆弱，导致冗余交互或信息流中断，损害系统的有效性和鲁棒性。

因此，本文要解决的核心问题是：如何为多智能体系统设计一种能够**动态适应**不断变化的外部环境（如模型能力、资源可用性）的通信拓扑结构。为此，论文首先形式化了自适应多智能体通信协议（AMACP），该协议要求拓扑结构同时满足任务有效性、资源成本效率和环境适应性。然后，论文提出了CARD（条件智能体图设计器）这一条件图生成框架来实例化该协议。CARD通过显式地将动态环境信号编码到图构建过程中，在训练和运行时都能实现拓扑结构的自适应调整，从而生成既高效又能抵御环境变化的通信结构。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：协同LLM智能体与基于图的多智能体系统。

在协同LLM智能体方面，早期研究依赖于手动设计的协调流程，例如链式思考提示、辩论框架或固定的树状/图状结构。为了减少人工设计的负担，后续工作提出了自动化的拓扑学习方法，如GPT-Swarm、G-Designer和Aflow，它们通过可微分模块或启发式搜索来优化智能体连接，在静态环境中表现出色。然而，这些方法均假设环境是静止的，缺乏应对模型能力、工具访问或数据质量变化的机制。本文提出的CARD框架则通过将动态环境信号显式地融入图生成过程，实现了在训练和运行时都能自适应调整拓扑结构，从而弥补了这一缺陷。

在多智能体图表示方面，尽管分布式系统文献中提出过一些动态通信协议，但大多数学习到的拓扑在模型升级、外部工具可靠性波动或数据源质量变化等动态条件下仍然是静态且脆弱的。预先定义或简单优化的图结构可能导致冗余交互或信息流中断。本文的CARD框架通过条件变分图编码器和环境感知优化，将外部信号（如模型版本、工具性能、数据源保真度）作为图生成的条件，从而能够生成适应性强、鲁棒的多智能体拓扑结构，与现有静态或仅基于提示的方法形成鲜明对比。

### Q3: 论文如何解决这个问题？

论文通过提出CARD框架来解决多智能体系统通信拓扑结构固定、无法适应动态环境变化的问题。其核心方法是一个条件化的图生成框架，能够根据环境信号动态构建和调整智能体间的通信结构。

整体框架包含四个关键阶段：智能体表示、条件图生成、环境感知训练和运行时适应。在智能体表示阶段，每个智能体被表示为两个向量：描述静态属性的配置文件向量（包括基础模型、角色和工具）和描述运行时环境状态的动态条件向量（如模型可用性、令牌成本等）。这些文本描述通过模板函数生成并编码为节点特征。

条件图生成阶段采用编码器-解码器架构。两个可学习的图编码器分别处理配置文件特征和条件特征，生成潜在表示。解码器则基于这些潜在表示和查询嵌入，预测智能体间的边概率，并通过阈值处理生成最终的通信拓扑图。该模块的创新点在于显式地将动态环境条件作为图生成的输入，使拓扑结构能够随环境变化而调整。

环境感知训练阶段通过一个复合损失函数优化模型参数。该损失函数包含任务效用项和条件感知成本项。任务效用衡量系统输出的准确性，而条件感知成本则正则化通信图，鼓励在保持性能的同时提高通信效率。具体地，成本正则化器根据边概率和预期令牌成本计算加权通信成本，实现效用与成本的平衡。

运行时适应是CARD的关键创新点。当部署环境发生变化时，框架无需重新训练，只需将更新的条件信号输入编码器-解码器模块，即可重新解码生成新的通信拓扑。这种单次重计算机制使系统能够实时适应模型能力、工具可靠性或成本等外部条件的变化，确保协作的鲁棒性和成本效率。

### Q4: 论文做了哪些实验？

论文在三个标准基准测试上进行了实验：代码生成（HumanEval）、数学推理（MATH）和通用语言理解（MMLU）。实验设置方面，评估了来自不同供应商的多种语言模型（如gpt4o-mini、deepseek-v3、llama3-70B、gpt4o、qwen-72B），以代表不同的技术范式。

对比方法分为三类：1) 单智能体方法（Vanilla LLM、CoT）；2) 固定拓扑的多智能体方法（Random-graph、LLM-Debate）；3) 自动优化拓扑的方法（GPT-swarm、Aflow、G-designer）。CARD与这些基线在支持多智能体协作、自动拓扑设计和条件配置方面进行了对比。

主要结果显示，CARD在整体性能上持续领先。关键数据指标如下：在HumanEval上平均准确率达到90.50%，在MATH上为74.50%，在MMLU上为86.67%。具体来看，在15个模型-基准组合中，CARD在13个中取得最高或并列最高分。例如，在HumanEval上，CARD在gpt4o-mini上达到93.33%，优于最佳基线Aflow的90.83%；在MATH上，CARD在qwen-72B上达到82.50%，而G-designer为79.16%。消融实验进一步表明，CARD的条件适应机制在所有基准测试中都带来了稳健的非负增益（如MATH上提升+0.83%至+3.34%），且在外域设置下性能下降更小，凸显了其适应能力。

### Q5: 有什么可以进一步探索的点？

该论文在动态环境下的多智能体通信拓扑设计方面取得了进展，但仍存在一些局限性和值得深入探索的方向。首先，CARD框架主要依赖预定义的动态信号（如模型版本、API状态），未来可探索更复杂、隐式的环境信号自动感知与提取机制，例如通过元学习或在线学习来实时推断系统状态变化。其次，实验集中于代码生成和数学推理等封闭任务，未来需在开放域、长期协作任务中验证其泛化能力，尤其是面对突发干扰或部分智能体失效时的鲁棒性。此外，当前拓扑生成基于条件变分图编码器，可结合图神经网络与强化学习，使智能体能够根据任务进度自主协商并优化连接结构，实现更细粒度的自适应。最后，论文未充分考虑通信开销与效率的权衡，未来可引入多目标优化，在保证性能的同时最小化通信延迟与资源消耗。

### Q6: 总结一下论文的主要内容

本文提出了一种名为CARD的条件性多智能体通信拓扑设计框架，旨在解决现有基于大语言模型的多智能体系统中通信结构固定或静态学习、难以适应现实动态变化的问题。其核心贡献是引入了AMACP协议，通过条件图生成技术，将环境动态信号（如模型升级、API变更）显式地融入图结构的构建中，从而在训练和运行时实现拓扑的自适应调整。方法上，CARD采用条件变分图编码器和环境感知优化，生成既高效又对能力或资源变化具有鲁棒性的通信结构。实验在HumanEval、MATH和MMLU基准上验证了其有效性，结果表明CARD在多种条件下均能稳定超越静态及基于提示的基线方法，显著提升了任务准确性与系统鲁棒性。这项工作为构建动态可适应的多智能体系统提供了重要的方法论支持。
