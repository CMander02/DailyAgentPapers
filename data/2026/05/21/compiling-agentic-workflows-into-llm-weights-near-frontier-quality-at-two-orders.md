---
title: "Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost"
authors:
  - "Simon Dennis"
  - "Rivaan Patil"
  - "Kevin Shabahang"
  - "Hao Guo"
date: "2026-05-21"
arxiv_id: "2605.22502"
arxiv_url: "https://arxiv.org/abs/2605.22502"
pdf_url: "https://arxiv.org/pdf/2605.22502v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agentic Workflow Compilation"
  - "Subterranean Agent"
  - "Fine-tuning for Agent Tasks"
  - "Procedural Task Execution"
  - "Model Distillation for Agents"
  - "Cost-Efficient Agent Orchestration"
relevance_score: 9.5
---

# Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost

## 原始摘要

Agent orchestration frameworks have proliferated, collectively exceeding 290,000 GitHub stars across LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, Semantic Kernel, Strands, and LlamaIndex. All follow the same pattern: an external orchestrator above the LLM, injecting instructions and routing decisions every turn. Recent work has shown this architecture is dominated for procedural tasks by simply providing the procedure in a frontier model's system prompt [Dennis et al., 2026a], at the cost of consuming the context window, requiring a frontier model for every conversation, and exposing proprietary procedures to third-party providers. Compiling the procedure into the weights of a small fine-tuned model -- creating a subterranean agent -- should resolve all of these concerns, and prior work (SimpleTOD, FireAct, SynTOD, WorkflowLLM, Agent Lumos) has shown the technique works. Yet developer adoption has overwhelmingly favored orchestration. We identify three perceived barriers and address each empirically across travel booking (14 nodes), Zoom support (14 nodes, product-specific knowledge), and insurance claims (55 nodes, 6 decision hubs).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有agent编排框架的三大核心问题，以推动从外部编排向模型权重内编译（subterranean agent）的范式转变。研究背景是：当前主流编排框架（如LangGraph、CrewAI等）均依赖LLM之上的外部编排器，每轮交互都需注入指令并做路由决策，导致三方面不足：1）需持续使用顶尖模型（frontier model），成本高昂且占用上下文窗口；2）专有流程暴露给第三方提供商；3）社区虽有SimpleTOD、FireAct等编译方法研究，但开发者仍普遍采用外部编排。论文识别出开发者采纳编译的三大感知障碍：质量（微调小模型能否匹敌顶尖模型？）、成本（自托管后推理成本是否真正降低？）、灵活性（流程变更时编译模型能否快速适应？）。通过在旅行预订（14节点）、Zoom支持（14节点）、保险理赔（55节点，6个决策枢纽）三个实际领域，以n=200场景/条件/领域的实验，证明8B编译模型在质量上达到顶尖模型in-context方法的87-98%，与使用70倍大模型的LangGraph编排器质量相当；每个会话成本降低128-462倍；重编译周期仅需30-50分钟（类似CI/CD流水线）。核心问题是：如何实证消除开发者对将流程编译入模型权重的质量、成本与灵活性顾虑，从而替代外部编排范式。

### Q2: 有哪些相关研究？

与本文相关的研究可分为三类：

**方法类研究**：SimpleTOD、AutoTOD 将任务导向对话的子任务（理解、决策、生成）统一为序列预测，避免模块化系统的错误累积和泛化差问题。FireAct、AgentTuning、Agent Lumos 通过微调小模型（如 Llama2-7B）从 GPT-4 行为中蒸馏推理能力，在 HotpotQA 等任务上提升达 77%，甚至超过 GPT 智能体。WorkflowLLM、SynTOD 将 API 编排知识或流程状态图编译进 8B 级模型权重，其中 SynTOD 的流程图驱动合成数据生成与本文最接近。

**评测与应用缺位**：本文指出先前工作虽证明编译方法有效，但存在三个显著空白：未量化相比编排或上下文方法的推理成本优势、未测量重新编译周期、未同时与同模型编排基线和前沿模型基线对比以隔离编译效果。本文通过跨旅游预订（14 节点）、Zoom 支持（14 节点+专业知识）、保险索赔（55 节点+6 决策枢纽）三个场景的实证研究填补了这些空白，首次系统性展示编译方法能以两个数量级更低的成本接近前沿模型质量。

### Q3: 论文如何解决这个问题？

论文提出了一种将智能体工作流直接编译进大语言模型权重中的方法，称为"地下智能体"（Subterranean Agent）。核心思想是将原本由外部编排器动态注入指令和路由决策的过程，转化为模型自身的隐式行为，从而在推理时完全消除对编排器的依赖。

整体框架分为三个主要阶段：首先将工作流定义为有向图，包含节点（对话轮次）、边（条件转移）、起始节点和终止节点；然后通过遍历图中所有有效路径生成合成对话数据，每个对话都沿路径逐轮生成，且模型在推理时仅看到自然对话，不包含任何过程注释；最后使用全参数微调将过程内化到模型权重中，实验表明低秩适配（LoRA）方法在过程性任务上无法达到全参数微调的效果。

关键技术包括：在生成阶段使用Claude Sonnet 4.5按图遍历生成训练数据，每个节点获取模板和完整对话历史；在微调阶段进行全参数更新以修改模型的隐式状态追踪行为；推理时仅使用极简系统提示（如"你是一个有帮助的旅行预订助手"），无需任何过程指令、流程图状态或路由逻辑。

创新点在于将编排器从运行时组件转变为训练时数据生成工具，使小规模微调模型能够以两个数量级更低的成本达到接近前沿模型的质量，同时解决了过程暴露、上下文窗口消耗和对第三方提供商的依赖问题。在旅行预订、Zoom支持和保险理赔三个领域的实验验证了该方法在不同复杂度工作流上的有效性，节点数从14到55不等，路径数从60到2381条。

### Q4: 论文做了哪些实验？

论文在三个领域进行了实验：旅行预订（14个节点）、Zoom技术支持（14个节点，含产品特定知识）和保险理赔处理（55个节点，6个决策枢纽）。实验设置包括：对比方法包括3B和8B的“地下代理”（编译模型）、同基座模型的表面编排器、LangGraph编排器以及包含完整程序指令的上下文基线。数据集通过合成生成，旅行预订2,125条对话、Zoom 6,264条对话、保险理赔3,000条对话。模型采用Qwen 2.5 3B或Qwen3-8B进行全参数微调。主要结果：在旅行预订中，3B编译模型在任务成功（4.11 vs 3.93）、一致性（4.34 vs 4.12）等指标上优于同模型编排器；与LangGraph编排器相比，在信息准确性上领先（4.75 vs 4.21），但在自然性上落后（4.12 vs 4.84）。在Zoom上，8B编译模型在自然性上超过LangGraph编排器（4.87 vs 4.64），优雅处理差距缩小到92%。在保险理赔中，8B编译模型在优雅处理（4.81 vs 4.38）和自然性（4.92 vs 4.58）上显著领先LangGraph编排器。效率方面，编译模型在保险领域最快（43.2秒 vs 120.8秒）。失败率上，编译模型在旅行（5.5% vs 24.0%）和保险（9.0% vs 17.0%）中显著低于LangGraph编排器。

### Q5: 有什么可以进一步探索的点？

论文指出编译代理工作流到模型权重的三大障碍已被实证解决，但仍存在进一步探索空间。首先，当前实验仅聚焦于有限领域（旅游、保险等），未来需验证该方法在更复杂、多模态任务（如代码生成、医疗诊断）中的泛化能力。其次，编译模型依赖固定流程，对于动态决策（如需要实时上下文交互的开放域问题）可能僵化——可探索“权重-提示混合架构”，将核心逻辑固化于权重，而将临时状态或灵活分支保留在提示中。此外，编译流程的自动化程度有限：当前30-50分钟的重编译周期仍难满足高频迭代需求，可尝试引入强化学习或在线学习机制，允许模型在部署后通过用户反馈微调权重。最后，论文未对比多种编译策略（如参数高效微调 vs 全量微调）对长期任务稳定性的影响，这值得系统研究。总体而言，该方法在固定流程场景极具优势，但向动态、多步推理的扩展将是关键突破点。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献在于提出并验证了“地下智能体”（subterranean agent）的概念，即将程序性工作流编译到小型微调模型的权重中，替代传统的外部编排框架。该工作解决的问题是：当前主流的智能体编排框架（如LangGraph）虽然流行，但存在依赖前沿模型、消耗长上下文窗口、泄露专有流程等缺陷。论文方法上，作者将完整的节点程序（如预订行程、保险理赔）直接微调进一个8B参数的小模型权重中，创建自编排的智能体。在对14-55个节点的三个复杂领域（旅行预订、Zoom支持、保险理赔）进行的大规模实验（n=200/条件/领域）后，主要结论有三：一是编译后的小模型质量可达前沿模型（如GPT-4）在相同系统提示下的87-98%；二是每次对话的成本降低128-462倍，因为模型提示词大小恒定；三是重新编译适应新流程仅需30-50分钟的生产时间。这项研究证明了将工作流“固化”进模型权重是一种成本极低、质量接近前沿、且适合CI/CD部署的高效范式，打破了开发者对传统编排框架的依赖。
