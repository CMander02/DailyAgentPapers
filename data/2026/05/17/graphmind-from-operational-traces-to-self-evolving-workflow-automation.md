---
title: "GraphMind: From Operational Traces to Self-Evolving Workflow Automation"
authors:
  - "Yiwen Zhu"
  - "Joyce Cahoon"
  - "Anna Pavlenko"
  - "Qiushi Bai"
  - "Nima Shahbazi"
  - "Divya Vermareddy"
  - "Meina Wang"
  - "Mathieu Demarne"
  - "Swati Bararia"
  - "Wenjing Wang"
  - "Hemkesh Vijaya Kumar"
  - "Hannah Lerner"
  - "Katherine Lin"
  - "Steve Toscano"
  - "Miso Cilimdzic"
  - "Subru Krishnan"
date: "2026-05-17"
arxiv_id: "2605.17617"
arxiv_url: "https://arxiv.org/abs/2605.17617"
pdf_url: "https://arxiv.org/pdf/2605.17617v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "工作流自动化"
  - "LLM推理"
  - "自适应学习"
  - "企业运营"
  - "图构建与执行"
  - "强化学习"
  - "端到端系统"
relevance_score: 8.5
---

# GraphMind: From Operational Traces to Self-Evolving Workflow Automation

## 原始摘要

Complex operational workflows coordinating personnel, tools, and information are central to enterprise operations, yet end-to-end automation remains challenging due to extensive requirements for human inputs and the inability to adapt over time. We present GraphMind, an end-to-end system that constructs, executes, and evolves action-centric workflow graphs without human effort. The system operates in three phases. First, a scalable offline pipeline extracts structured workflow graphs from large volumes of human resolution traces, capturing problems, actions, and their causal relationships. Second, an online multi-agent traversal engine navigates the graph to dynamically construct and execute workflows, combining graph-guided retrieval with LLM-driven reasoning at each step. Third, Adaptive Traversal Reinforcement (ATR) reinforces successful traversal paths and decays stale elements. This closed-loop mechanism enables the graph to self-optimize and adapt to shifting operational conditions. GraphMind has been deployed across four production cloud database services for incident investigation. Evaluated on production data, the system substantially outperforms a Trace-RAG baseline in mitigation reach, groundedness, and diagnostic throughput, scoring 4.95/5 in blind expert review. The ATR layer provides further gains across all metrics, demonstrating that workflow graphs can learn and improve from execution-derived feedback.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决企业运营中复杂工作流的端到端自动化难题。现有方法如基于LLM的代理和手动编写的知识文档（如操作手册）存在显著不足：手动编写成本高、需深度领域知识，且难以维护；随着系统演化，文档容易过时；检索时消耗大量上下文标记，效率低下；同时难以覆盖专家通过即兴处理但未记录的长尾边缘情况。虽然操作痕迹记录了专家处理复杂工作流的实际过程，但作为结构化的可重用知识仍未被充分利用。

本文提出的GraphMind系统，核心目标是利用操作痕迹自动构建、执行并自我演化以行动为中心的工作流图。该系统通过三个关键阶段实现：离线阶段从大量人工解决痕迹中提取结构化工作流图；在线阶段通过多智能体遍历引擎结合图引导检索与LLM推理动态构建并执行工作流；自适应遍历强化阶段则通过类似蚁群优化的机制，沿着成功路径沉积“信息素”并衰减陈旧元素，形成闭环反馈。这解决了现有知识格式在存储效率、智能体友好性、人力成本、覆盖范围及自我演化能力上的综合不足，使工作流图能从自身执行经验中持续学习与优化。

### Q2: 有哪些相关研究？

**相关研究工作可分为以下几类：**

**1. 过程挖掘与工作流自动化类**  
经典的过程挖掘从事件日志中恢复工作流，但其依赖结构化日志。GraphMind 针对更嘈杂的自然语言操作轨迹，利用 LLM 提取可执行的工作流图，拓展了该类方法的应用范围。  

**2. 知识图谱与图增强检索类**  
相关工作将 LLM 与知识图谱结合（如 GraphRAG），通过微调或检索增强推理。GraphMind 与之区别在于：将图谱保持为外部存储，通过迭代路径检索执行，且允许执行结果（成功/失败）重塑图谱结构，引入强化权重（ATR）实现自动演化。  

**3. AIOps 与事件管理类**  
D-Bot、Panda、RCACopilot 等利用 LLM 进行故障排查，神经符号方法使用结构图约束 LLM 输出。GraphMind 在此基础上进一步实现了动作中心知识库的自动构建和持续改进，填补了“从执行反馈中自优化”的空白。  

**4. 群体智能与蚁群优化类**  
蚁群优化（ACO）通过信息素积累和衰减指导搜索。GraphMind 借鉴其“强化-衰减”直觉，但将其应用于 LLM 引导的工作流自动化的图演化中，而非传统组合优化。  

**5. LLM 代理与智能体 RAG 类**  
工具增强的代理和智能体 RAG 支持迭代推理。GraphMind 将该循环锚定在学习到的、带有强化加权先验的工作流图上，增强了 LLM 推理的指导性和鲁棒性。

### Q3: 论文如何解决这个问题？

GraphMind通过三阶段闭环系统解决工作流自动化的挑战。首先是离线图构建阶段（热启动），利用可扩展的流水线从大规模人工处置记录中提取结构化工作流图。该流程包括：（1）基于LLM的提取器从每条记录中抽取子图，捕获问题、动作及因果关系；（2）去聚类与合并，将现有图节点还原为原始提取并与新提取合并；（3）语义聚类，通过嵌入向量进行凝聚聚类，对语义相似的节点去重（使用正则化掩码、预训练嵌入模型和余弦距离阈值）；（4）图与索引更新，同步到向量索引以支持高效检索。图采用类型化模式，包括域、问题、动作三种节点和CAUSES、RESOLVES、LEADS_TO、BELONGS_TO四种边，支持从根因到解决策略的结构化遍历。

在线阶段采用多智能体图遍历引擎，通过嵌套控制流动态执行工作流。外层循环维护全局上下文（长期记忆），内层循环迭代探索图结构。关键模块包括：Graph Loader，利用LLM推理生成查询文本和目标节点类型，通过向量检索获取top-k根节点，并沿强化权重分布的边进行m跳概率扩展（使用对数压缩的权重分布）；Action Planner，基于上下文、扩展子图（以Mermaid图呈现并标注节点权重）和系统指令选择候选动作，当无动作时生成转向信号驱动下一次迭代；Execution Agents，执行选定动作（如诊断查询或修复步骤）并将观察结果整合进上下文，最终LLM综合生成诊断报告。

创新点在于Adaptive Traversal Reinforcement（ATR）闭环机制。每次在线遍历生成轨迹后，系统基于有用性、基础性和用户评分计算质量分数，仅对高质量轨迹（阈值4/5）沿路径的边和节点沉积强化，短成功路径获得更强强化以偏向高效序列。同时定期以衰减率ρ降低所有权重，防止早期模式永久主导并适应基础设施演化。ATR还支持边合成：当成功遍历访问未连接节点时，自动创建新边（初始权重低于均值），需后续遍历确认。该机制使工作流图能从执行反馈中自我优化，适应不断变化的运营条件。

### Q4: 论文做了哪些实验？

论文进行了三组实验。**实验设置**：(1) 离线提取质量评估，手动标注30张工单作为ground truth（71个问题节点、191个动作节点、262条边）；(2) 基于一年约1300个生产事件构建的工作流图进行在线可控评估（93个保留事件）；(3) 自适应遍历强化（ATR）对图演化和遍历的影响。**对比方法**：Trace-RAG基线（类似RCACopilot，检索LLM压缩的事件摘要）。**主要结果**：离线提取达到节点F1=0.89（93%精确率，85%召回率），边F1=0.92（91%精确率，92%召回率），其中CAUSES关系F1最高（0.98），RESOLVES最困难（0.86）。在线评估中，GraphMind在缓解达成率（98.5% vs 90.9%）、基础事实性（96.2% vs 77.3%）和有用性（3.49 vs 3.32）上均显著优于Trace-RAG，KQL吞吐量高4倍（10.0 vs 2.5）。盲审评分4.95/5（Trace-RAG为3.68/5）。ATR层在所有指标上带来进一步提升，验证了工作流图可从执行反馈中自我优化。

### Q5: 有什么可以进一步探索的点？

首先，ATR目前仅对高质量轨迹(Q≥δq)进行正强化，完全丢弃了低质量轨迹的反馈信号。未来可引入负强化机制，对失败路径的边缘和节点施加惩罚，加速收敛至有效诊断路径，但需设计衰减函数以避免因暂时性失败永久剔除有价值的路径，如采用带遗忘因子的弹性惩罚。其次，概率边缘选择偏向利用历史最优路径，随着图规模增大，需发展更智能的动态剪枝策略。可结合图神经网络学习节点表征，基于实时上下文预测边缘有效性，而非仅依赖历史权重。最后，借鉴蚂蚁种群的分工机制，可引入领域差异化强化：为容量故障、认证失败等不同问题类型维护独立的权重通道w_d(e)。这样能减少跨领域噪声干扰，使系统更快收敛到领域特定的高效诊断策略。此外，边合成机制可扩展为自适应拓扑重构，允许在重复失败路径中动态插入新节点或合并冗余分支，进一步提升自演化能力。

### Q6: 总结一下论文的主要内容

GraphMind提出了一种从操作轨迹中自动构建、执行和演化工作流图的端到端系统。核心挑战在于企业级复杂工作流（如数据库故障诊断）的端到端自动化因依赖人工知识且无法适应变化而难以实现。该系统包含三个核心模块：首先，离线流水线从海量人工解决记录中提取结构化工作流图，以动作为中心捕获问题与操作的因果关联；其次，在线多智能体遍历引擎结合图引导检索与LLM推理，动态构建并执行工作流；最后，自适应遍历强化（ATR）机制受蚁群算法启发，通过奖励成功路径、衰减过时节点实现闭环自优化。在四大云数据库服务的事故诊断生产中，GraphMind在缓解覆盖、可归因性及专家评分（4.95/5）上显著超越Trace-RAG基线，且ATR进一步提升所有指标。工作流图能通过自主执行持续学习，无需人工维护，为首个实现从轨迹自动演化工作流的系统。
