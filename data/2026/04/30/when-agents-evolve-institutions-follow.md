---
title: "When Agents Evolve, Institutions Follow"
authors:
  - "Chao Fei"
  - "Hongcheng Guo"
  - "Yanghua Xiao"
date: "2026-04-30"
arxiv_id: "2604.27691"
arxiv_url: "https://arxiv.org/abs/2604.27691"
pdf_url: "https://arxiv.org/pdf/2604.27691v1"
github_url: "https://github.com/cf3i/SocialSystemArena"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "治理结构"
  - "集体智能"
  - "LLM智能体架构"
  - "机构设计"
  - "实验评估"
relevance_score: 9.5
---

# When Agents Evolve, Institutions Follow

## 原始摘要

Across millennia, complex societies have faced the same coordination problem of how to organize collective action among cognitively bounded and informationally incomplete individuals. Different civilizations developed different political institutions to answer the same basic questions of who proposes, who reviews, who executes, and how errors are corrected. We argue that multi-agent systems built on large language models face the same challenge. Their central problem is not only individual intelligence, but collective organization. Historical institutions therefore provide a structured design space for multi-agent architectures, making key trade-offs between efficiency and error correction, centralization and distribution, and specialization and redundancy empirically testable. We translate seven historical political institutions, spanning four canonical governance patterns, into executable multi-agent architectures and evaluate them under identical conditions across three large language models and two benchmarks. We find that governance topology strongly shapes collective performance. Within a single model, the gap between the best and worst institution exceeds 57 percentage points, while the optimal architecture shifts systematically with model capability and task characteristics. These results suggest that collective intelligence will not advance through a single optimal organizational form, but through governance mechanisms that can be reselected and reconfigured as tasks and capabilities evolve. More broadly, this points to a transition from \textbf{self-evolving agents} to the \textbf{self-evolving multi-agent system}. The code is available on \href{https://github.com/cf3i/SocialSystemArena}{GitHub}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体系统在组织集体行动时面临的协调问题。研究背景是，历史上的复杂社会长期面临在认知有限和信息不完整的个体间组织集体行动的挑战，不同文明发展出了不同的政治制度来分别解决谁提议、谁审查、谁执行以及如何纠错等基本问题。现有方法（如角色提示、辩论、规划、工具使用）虽然推动了多智能体系统的发展，但主要关注个体智能的增强，而忽视了治理拓扑（即集体组织形式）这一核心设计变量。本文的核心问题是：多智能体系统的性能不仅取决于单个智能体的能力，更取决于它们如何组织起来进行集体行动。因此，论文将七种历史政治制度（涵盖四种经典治理模式）转化为可执行的多智能体架构，在统一条件下评估其性能，试图证明治理拓扑是影响系统性能的关键因素，并且最优架构会随模型能力和任务特征而系统性地变化，从而推动研究从“自我进化的智能体”转向“自我进化的多智能体系统”。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及四类工作。第一类是**方法类**，即现有的LLM多智能体框架（如多轮对话、序列化流水线、角色扮演、动态团队招募、对抗式辩论等），每种框架都采用了不同的通信模式。本文与它们的核心区别在于，这些工作通常固定在一种拓扑结构上，未在受控条件下比较不同治理模式的差异，而本文系统性地设计了七种历史政治制度对应的架构。

第二类是**方法类**中的自动拓扑搜索研究（如GPTSwarm、G-Designer、MacNet、EvoMAC、EvoAgent），它们通过优化边连接或进化算法自适应生成拓扑。本文与它们的不同在于，这些方法通常在单一模型后端上验证，且未考察发现的结构是否能跨不同LLM和任务分布泛化，而本文在三种大模型和两个基准上进行了跨模型对比。

第三类是**应用类**的人工社会模拟研究（如基于LLM的自主规划与协作、GovSim中的制度机制必要性分析）。本文与它们的区别是，它们观察给定群体中涌现的行为，但未系统改变制度结构来分离其对任务结果的因果效应，而本文明确地将治理拓扑作为自变量进行控制实验。

第四类是**评测类**的系统评估基准（如AgentBench、AgentBoard、ReAct、Toolformer等）。这些基准普遍固定治理结构而只变化底层模型，将治理拓扑作为一个未控制的变量，而本文则明确指出治理拓扑是影响性能的关键且被忽视的变量，填补了这一空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为SocialSystemArena的统一框架，将七种历史政治制度（如秦汉郡县制、唐三省六部制、美国联邦制、雅典民主等）转化为可执行的多智能体治理架构，并系统评估不同治理拓扑对LLM多智能体系统集体性能的影响。核心方法包含三个层面：首先，形式化定义治理规范G = (P, A, S, T, F)，其中P为四种规范消息流模式（流水线、门控流水线、自治集群、共识），A为分配角色与人格提示的智能体集合，S为有序阶段序列，T为基于智能体路由决策的状态转移函数，F为可插拔行为修饰器集合（如监控、循环守卫、共享状态传播）。其次，设计统一的GovernanceRuntime执行引擎，通过阶段调度、并行投票/集群执行、特征插件集成等机制，确保治理规范G是唯一控制变量。最后，通过三个LLM后端和两个基准任务进行对照实验，发现治理拓扑显著影响集体表现，最佳与最差制度间性能差距超过57个百分点，且最优架构随模型能力和任务特性系统性地变化。创新点在于将历史政治制度的机构设计（如门控流水线的错误修正循环）转化为可测试的MAS架构变量，揭示了集体智能提升不仅依赖智能体自身进化，更需通过可重选与可重构的治理机制实现系统的自进化。

### Q4: 论文做了哪些实验？

论文在 PinchBench（23 个单轮工具使用任务）和 ClaweBench（104 个多步现实世界任务，涵盖 24 个类别、6 个难度级别）两个基准上进行了评估，使用了三个 LLM 后端（MiniMax M2.5、Kimi K2.5、Gemini 2.5 Flash）和八个治理结构（七个历史制度加上单智能体 SAS 基线）。主要指标为任务成功率（Task Success Rate）。主要结果：在 PinchBench 上，治理拓扑显著影响性能，同一模型内最优与最差制度间差距超过 57 个百分比点；不存在普遍最优的制度，最优架构随模型能力和任务特征而系统性地变化（例如，MiniMax 上 Tang 最优达 88.2%，Kimi 上 Mongol 最优为 67.3%，Gemini 上 Edo 最优为 87.7%）。在更复杂的 ClaweBench 上，性能范围被压缩（差距缩小到约 8-12 个百分点），模型排名发生逆转（Kimi 从 PinchBench 最弱变为最强），且复杂拓扑（如 Edo、Tang）的优势减弱。效率分析显示，门控拓扑（如 Tang）存在门循环故障模式，当 LLM 无法满足门标准时，会大幅增加步骤和 token 消耗（如 Kimi 上的 Tang 平均每任务 26.7 步，89K tokens），但性能反而下降。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于将历史制度建模为静态规范，忽略了真实制度随压力动态演化的特性。未来可探索**元治理层**，根据任务复杂度、门控通过率等实时信号动态重配置治理拓扑，实现从“自演化智能体”到“自演化多智能体系统”的跃迁。当前仅评估了三个商业LLM，需扩展至开源模型以验证泛化性。此外，门密度（ρ）虽能预测开销，但最优ρ与模型能力、任务复杂度的定量关系尚未建模——可尝试引入自适应门控机制，在高复杂度任务中自动降低门密度以避免审查环路崩溃。另一个关键方向是扩充制度设计空间：除历史政治体制外，可吸取现代组织架构（如矩阵管理、Holacracy）或生物群体决策模型（如蜂群共识），构建更丰富的治理基元库。最终目标应是发展一套原则性方法，使系统能根据任务特征与模型缺陷，自动匹配合适的治理结构，从而超越人工试错式的架构搜索。

### Q6: 总结一下论文的主要内容

这篇论文将历史上的七种政治制度（如中央集权、分层审查、自治联邦、共识民主等）转化为可执行的多智能体架构，通过统一实验平台（SocialSystemArena）在三类大语言模型和两个基准任务上评估其性能。核心贡献在于将治理拓扑作为多智能体系统的一阶设计变量，揭示了其表现差异巨大（同一模型上最优与最差制度差距超57个百分点），且最优架构随模型能力和任务特征动态变化，不存在普适的最优形式。研究结论表明，集体智能的进步不应仅依赖单体智能体的自我进化，而需要转向能够根据任务和能力变化重新选择与配置治理机制的自演化多智能体系统，为多智能体协作设计提供了结构化的历史制度设计空间和可实证的分析框架。
