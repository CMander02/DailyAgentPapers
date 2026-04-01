---
title: "An Empirical Study of Multi-Agent Collaboration for Automated Research"
authors:
  - "Yang Shen"
  - "Zhenyi Yi"
  - "Ziyi Zhao"
  - "Lijun Sun"
  - "Dongyang Li"
  - "Chin-Teng Lin"
  - "Yuhui Shi"
date: "2026-03-31"
arxiv_id: "2603.29632"
arxiv_url: "https://arxiv.org/abs/2603.29632"
pdf_url: "https://arxiv.org/pdf/2603.29632v1"
categories:
  - "cs.MA"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Automated Research"
  - "Empirical Study"
  - "Agent Collaboration"
  - "LLM-based Agents"
  - "Coordination Frameworks"
  - "Execution-based Evaluation"
relevance_score: 7.5
---

# An Empirical Study of Multi-Agent Collaboration for Automated Research

## 原始摘要

As AI agents evolve, the community is rapidly shifting from single Large Language Models (LLMs) to Multi-Agent Systems (MAS) to overcome cognitive bottlenecks in automated research. However, the optimal multi-agent coordination framework for these autonomous agents remains largely unexplored. In this paper, we present a systematic empirical study investigating the comparative efficacy of distinct multi-agent structures for automated machine learning optimization. Utilizing a rigorously controlled, execution-based testbed equipped with Git worktree isolation and explicit global memory, we benchmark a single-agent baseline against two multi-agent paradigms: a subagent architecture (parallel exploration with post-hoc consolidation) and an agent team architecture (experts with pre-execution handoffs). By evaluating these systems under strictly fixed computational time budgets, our findings reveal a fundamental trade-off between operational stability and theoretical deliberation. The subagent mode functions as a highly resilient, high-throughput search engine optimal for broad, shallow optimizations under strict time constraints. Conversely, the agent team topology exhibits higher operational fragility due to multi-author code generation but achieves the deep theoretical alignment necessary for complex architectural refactoring given extended compute budgets. These empirical insights provide actionable guidelines for designing future autoresearch systems, advocating for dynamically routed architectures that adapt their collaborative structures to real-time task complexity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在自动化研究（特别是机器学习优化）中，如何设计有效的多智能体协作框架以克服单智能体系统的认知瓶颈这一核心问题。研究背景是，随着AI智能体的发展，为实现自动化科学研究，社区正从单一大型语言模型转向多智能体系统。现有方法，如Karpathy的“autoresearch”项目所代表的单智能体架构，在应对复杂研究任务时暴露出明显不足：难以维持长程上下文、在深度代码重构中易产生幻觉、且搜索路径趋于确定，缺乏突破性。尽管已有一些扩展尝试（如引入并行搜索或持久记忆），但单智能体的根本瓶颈依然存在。

现有多智能体系统的研究虽多，但对于在高度动态、经验驱动的自动化机器学习研究场景中，何种多智能体协作拓扑结构能最大化研究效率，仍是一个未被充分探索的关键开放性问题。具体而言，现有方法缺乏对不同协作范式（如协调时机、角色分配）在严格计算时间约束下的系统性实证比较。

因此，本文要解决的核心问题是：在自动化机器学习优化任务中，如何通过实证研究，系统比较不同多智能体协作结构（如子智能体并行探索与事后整合、专家团队预执行交接等）的效能，揭示其内在权衡，并为设计高效、稳定的自动化研究系统提供可操作的指导原则。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：自动化研究系统、通用智能体框架与协作范式，以及本文工作的直接基础。

在**自动化研究系统**方面，代表性工作包括Sakana AI的AI Scientist和Analemma的FARS。AI Scientist展示了LLM驱动端到端科学发现（从想法生成到论文撰写与评审）的潜力，但其核心是线性的单智能体流程。FARS则是一个真正的多智能体研究系统，包含构思、规划、实验和写作四个专门化智能体，但其运行成本极高（如生成166篇论文花费18.6万美元）。这些系统虽展示了自动化研究的可能性，但要么缺乏多智能体间的深度协作，要么成本令人望而却步。

在**通用智能体框架与协作范式**方面，一系列工作以轻量级的单智能体系统Autoresearch为基础进行了扩展。例如，AutoResearch Claw引入了多批次并行评估；EvoScientist增加了持久经验记忆以实现跨轮次学习；ARIS引入了跨模型评审机制以缓解单模型评估盲点；ArgusBot通过规划、执行、评审等专门化角色分配来解决长程执行瓶颈；Bilevel Autoresearch则采用元优化方法，在运行时动态生成并注入新的搜索机制代码。这些工作主要关注算法生成、批处理或元优化，但大多仍围绕单智能体自动化或缺乏智能体间通信的角色化多智能体系统。

**本文工作**直接建立在Autoresearch（用于神经网络超参数搜索的单智能体循环）的基础之上。与上述所有工作不同，本文的核心贡献是**在严格固定计算预算下，对多智能体协作结构（子智能体架构与智能体团队架构）进行系统的实证比较与评估**，重点关注智能体间的交互与通信，揭示了操作稳定性与理论深度之间的权衡，并为此前未被充分探索的多智能体协调框架提供了实证依据。

### Q3: 论文如何解决这个问题？

论文通过构建一个严谨的实证研究测试平台，并对比两种主流的多智能体协作架构，来探究如何优化自动研究中的多智能体协调框架。其核心方法是将自动机器学习研究过程建模为一个受约束的搜索优化问题，目标是在固定的计算时间预算内，最小化目标代码库的验证损失。

整体框架包括一个严格控制变量的测试平台和两种被评估的多智能体架构。测试平台的关键设计旨在隔离协作拓扑的影响，并消除混杂变量。首先，它利用**Git工作树隔离**机制，为每个智能体或候选方案动态分配完全隔离的代码环境，确保并行探索不会相互污染。其次，为防止代码破坏，智能体与代码库的交互被限制在严格的**搜索/替换契约**内，智能体必须输出结构化的提案。第三，所有生成的补丁在消耗实际训练时间预算前，都需经过**轻量级预检编译检查**，以拦截语法错误。最后，为了克服长期任务中的灾难性遗忘，平台为所有架构统一配备了**显式全局记忆机制**（`program_exp.md`），用于记录历史经验（如成功的改进或导致崩溃的机制）。

论文系统比较了两种多智能体范式：
1.  **子智能体架构**：这是一种分层设计，包含一个中央协调器和多个并行工作的子智能体（工人）。在每一轮中，多个工人智能体在隔离的工作树中独立生成补丁提案并进行短时训练。如果同一轮中有多个候选补丁成功改进了基线指标，则会触发一个**协调器智能体**，尝试将这些高潜力的补丁合并为一个统一的脚本。合并后的方案只有在性能严格超过该轮最佳独立补丁时才会被接受，确保了合并不会导致性能回退。该架构的核心创新在于通过并行搜索分散认知负荷，并通过事后集中合并来整合成果，实现了高吞吐量的广泛搜索。

2.  **智能体团队架构**：这是一种更加协作和去中心化的范式，模拟了专家团队的合作。系统预定义了多个专家角色（如架构师、优化器、效率专家），他们在每一轮中**顺序地、迭代地**在同一个共享工作树上修改代码。每个专家接收当前代码状态以及前序专家传递的构思摘要和动机（称为“群聊”上下文），然后进行增量编辑。训练仅在所有专家完成“群聊”后进行。为了缓解多作者代码生成的脆弱性，该架构引入了一个关键的创新组件——**隔离的工程师智能体**作为回退机制。当生成的代码出现运行时崩溃时，工程师会进行保守的调试以恢复可执行性，同时严格保留专家们的意图。

论文的创新点在于通过上述严格受控的实验设置，首次实证揭示了多智能体协作中**操作稳定性与理论深度之间的权衡**。子智能体架构作为高吞吐量搜索引擎，在严格时间约束下对广泛、浅层的优化具有高韧性和效率；而智能体团队架构虽然因多作者代码生成而具有更高的操作脆弱性，但在给定充足计算预算时，能通过专家间的深度理论对齐，实现复杂的架构重构。这些发现为设计能够根据实时任务复杂度动态调整协作结构的未来自动研究系统提供了可操作的指导。

### Q4: 论文做了哪些实验？

该论文通过一个标准化的测试平台进行了三项实验，以比较不同多智能体协作结构的效能。实验设置方面，研究使用了GLM-4.7和GLM-4.6v作为智能体模型，并在NVIDIA RTX 3090 GPU上运行。实验对比了三种架构：一个单智能体基线、一个子智能体架构（并行探索与事后整合）和一个智能体团队架构（专家间执行前交接）。实验在严格固定的计算时间预算（T_max = 300秒和600秒）下进行。

数据集/基准测试基于一个自动化机器学习优化任务，具体是优化一个目标模型的性能。主要评估指标是验证集上每字节比特数（val_bpb）的绝对减少量（Δ val_bpb），该值越高表示优化越成功。此外，还通过成功率（提案失败、预检失败、训练崩溃、训练成功四个阶段的比例）来衡量系统的操作稳定性。

主要结果如下：在300秒的短时间预算下，子智能体模式表现出早期优势，实现了七次有效改进，而智能体团队仅三次。子智能体模式具有高吞吐量和稳定性（预检失败和崩溃率最低），但其改进缺乏多样性，容易陷入对单一超参数（如MLP扩展比率）的贪婪局部优化。相反，智能体团队模式虽然初始改进慢、生成的提案少且操作更脆弱（因多作者代码生成导致错误累积），但其改进具有更高的多样性和结构复杂性。例如，在300秒预算内，团队能提出同时调整窗口注意力模式、学习率预热计划和词嵌入大小的统一补丁。在600秒的更长预算下，智能体团队能实现更深度的架构重构，展示了其在复杂任务上的理论规划优势。关键数据指标包括：Δ val_bpb的提升值、不同模式下有效改进的次数（如300秒内子智能体7次 vs. 团队3次），以及各阶段的比例分布（反映了子智能体的高稳定性和团队的高脆弱性）。

### Q5: 有什么可以进一步探索的点？

本文揭示了子代理架构与团队架构在稳定性与理论深度间的权衡，但研究仍存在局限。实验集中于自动化机器学习优化，其结论在其他科研领域（如理论数学或实验科学）的普适性有待验证。此外，系统依赖固定的计算预算进行评估，未充分考虑动态资源分配或长期学习能力。

未来研究方向可包括：第一，设计动态路由架构，使系统能根据任务复杂度实时切换协作模式，例如引入元控制器进行决策。第二，探索更复杂的通信与协调机制，如引入辩论或投票机制以提升团队架构的稳定性。第三，将研究拓展至多模态任务或跨领域协作，检验架构在更广泛科学问题中的有效性。最后，可考虑引入人类反馈循环，形成混合智能系统，以结合人类直觉与AI的搜索能力。

### Q6: 总结一下论文的主要内容

该论文针对自动化研究中多智能体协作框架的优化问题进行了系统性实证研究。针对当前从单一大语言模型转向多智能体系统以克服认知瓶颈的趋势，作者指出最优的多智能体协调框架仍属未知。研究聚焦于自动化机器学习优化任务，通过构建一个严格控制的、基于执行的测试平台（包含Git工作树隔离和显式全局内存），比较了三种架构的性能：单智能体基线、子智能体架构（并行探索后整合）和智能体团队架构（专家间预执行交接）。在固定计算时间预算下，研究发现存在操作稳定性与理论深度之间的根本权衡。子智能体模式具有高韧性和高吞吐量，适合时间严格约束下的广泛、浅层优化；而智能体团队拓扑虽因多作者代码生成导致操作更脆弱，但在充足计算预算下能实现深度理论对齐，胜任复杂的架构重构。该研究为未来自动化研究系统的设计提供了实用指南，主张采用能根据实时任务复杂度动态调整协作结构的自适应路由架构。
