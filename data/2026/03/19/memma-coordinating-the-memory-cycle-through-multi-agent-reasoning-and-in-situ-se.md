---
title: "MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution"
authors:
  - "Minhua Lin"
  - "Zhiwei Zhang"
  - "Hanqing Lu"
  - "Hui Liu"
  - "Xianfeng Tang"
  - "Qi He"
  - "Xiang Zhang"
  - "Suhang Wang"
date: "2026-03-19"
arxiv_id: "2603.18718"
arxiv_url: "https://arxiv.org/abs/2603.18718"
pdf_url: "https://arxiv.org/pdf/2603.18718v1"
github_url: "https://github.com/ventr1c/memma"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "记忆增强"
  - "多智能体协作"
  - "自我进化"
  - "规划与推理"
  - "工具使用"
  - "基准评测"
relevance_score: 9.0
---

# MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution

## 原始摘要

Memory-augmented LLM agents maintain external memory banks to support long-horizon interaction, yet most existing systems treat construction, retrieval, and utilization as isolated subroutines. This creates two coupled challenges: strategic blindness on the forward path of the memory cycle, where construction and retrieval are driven by local heuristics rather than explicit strategic reasoning, and sparse, delayed supervision on the backward path, where downstream failures rarely translate into direct repairs of the memory bank. To address these challenges, we propose MemMA, a plug-and-play multi-agent framework that coordinates the memory cycle along both the forward and backward paths. On the forward path, a Meta-Thinker produces structured guidance that steers a Memory Manager during construction and directs a Query Reasoner during iterative retrieval. On the backward path, MemMA introduces in-situ self-evolving memory construction, which synthesizes probe QA pairs, verifies the current memory, and converts failures into repair actions before the memory is finalized. Extensive experiments on LoCoMo show that MemMA consistently outperforms existing baselines across multiple LLM backbones and improves three different storage backends in a plug-and-play manner. Our code is publicly available at https://github.com/ventr1c/memma.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决增强记忆的大语言模型（LLM）智能体在长期交互任务中面临的核心挑战：现有系统通常将记忆周期的构建、检索和利用视为孤立的子程序，导致整体效能受限。

研究背景是，随着LLM从单次对话系统演变为需要执行持续数天或数周复杂工作流的持久性智能体系统，可控的长期记忆成为关键需求。智能体需要主动管理外部记忆库，以维持长期一致性。然而，现有方法大多将记忆操作视为孤立、被动的模块，忽略了记忆周期各阶段（构建、检索、利用）之间的内在耦合与依赖关系。这导致了两个相互关联的不足：首先，在记忆周期的前向路径上存在“战略盲目性”，即记忆的构建和检索由局部启发式规则驱动，缺乏明确的战略推理来协调这些行动，具体表现为短视的构建（不加分辨地积累或覆盖信息，留下冗余和冲突）和无目标的检索（进行浅层或重复搜索，无法有效缩小信息差距）。其次，在记忆周期的后向路径上存在“稀疏且延迟的监督”，即下游任务（如问答）的失败结果很少能直接转化为对记忆库本身的修复信号，使得错误（如遗漏、未解决的矛盾）在记忆库中持续存在并影响后续更新。

因此，本文要解决的核心问题是：如何设计一个框架，以协调的方式优化整个记忆周期，同时解决前向路径的战略盲目性和后向路径的反馈稀疏延迟问题。具体而言，论文提出了MemMA框架，通过多智能体协同推理，在前向路径上引入元思考者进行战略规划以指导记忆构建和迭代检索，在后向路径上引入原位自演化记忆构建机制，将下游失败即时转化为对当前记忆状态的修复行动，从而实现记忆周期的闭环优化。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕记忆增强型大语言模型（LLM）智能体展开，可分为以下几类：

**1. 记忆架构与组织方法**：这类研究致力于设计外部记忆库的存储结构（如向量数据库、图结构）或优化记忆的组织与整合策略（例如通过总结或聚类），以提升存储效率和信息密度。它们主要聚焦于记忆管线的单一阶段。

**2. 记忆检索方法**：这类工作专注于改进检索机制，例如设计更优的查询嵌入或重排序算法，以提高从记忆库中召回相关信息的准确性和效率。其优化目标同样相对独立。

**本文提出的MemMA框架与上述工作的核心区别在于其系统性的协调与闭环演化思想。** 现有方法大多将记忆的构建、检索和利用视为孤立的子程序进行优化。而MemMA则通过一个多智能体框架，在**前向路径**上，使用元思考者进行显式的战略推理，来协同指导记忆构建与迭代检索，解决了“战略盲区”问题；在**后向路径**上，创新性地引入了**原位自演化**机制，能够将下游利用失败直接转化为对记忆库的修复信号，实现了从稀疏、延迟监督到即时、直接反馈的转变。因此，MemMA的核心贡献在于以“即插即用”的方式，对整个记忆周期进行了端到端的协调与动态优化，而非孤立地改进某个环节。

### Q3: 论文如何解决这个问题？

论文通过提出MemMA框架来解决记忆循环中的战略盲目性和稀疏延迟监督问题。其核心方法采用多智能体架构，将战略推理与底层执行分离，并引入原位自演化机制提供密集反馈。

整体框架采用规划者-工作者架构，包含四个主要模块：元思考者（Meta-Thinker）负责高层战略推理，在记忆构建阶段分析新对话块与现有记忆的关系，生成关于保留、整合或解决冲突的元指导；在检索阶段评估证据充分性并诊断缺失信息。记忆管理器（Memory Manager）根据元指导执行原子化记忆编辑操作（如添加、更新、删除），实现后端无关的记忆存储。查询推理器（Query Reasoner）实施主动检索策略，通过“精炼-探测”循环迭代优化查询，每次迭代针对元思考者诊断的信息缺口进行定向检索。答案生成器（Answer Agent）基于最终证据集生成回答。

关键技术包含两大创新点：在正向路径上，通过元思考者的结构化指导协调记忆构建与检索，解决战略盲目性问题。元思考者提供聚焦点指导记忆构建避免盲目积累，并在检索中通过“可回答/不可回答”判断及缺失诊断引导正交证据获取。在反向路径上，设计原位自演化记忆构建机制：每个会话后自动合成探测问答对，立即验证临时记忆状态；通过反思模块将失败案例转化为修复建议；最后进行语义整合处理冗余与冲突，再将修复内容写回记忆库。这种设计将稀疏延迟的下游反馈转化为密集局部监督，在记忆固化前完成修复。

该框架以即插即用方式协调记忆循环的全过程，实现了构建、检索与利用的紧密耦合，显著提升了长程交互中记忆系统的效能。

### Q4: 论文做了哪些实验？

论文在LoCoMo基准测试上进行了全面的实验评估。实验设置方面，使用GPT-4o-mini和Claude-Haiku-4.5作为Memory Manager、Meta-Thinker和Query Reasoner的骨干模型，并固定GPT-4o-mini作为答案生成和评估的法官模型。关键参数包括检索条目预算top-30，迭代优化预算H=3，以及每个会话生成J=5个探测QA对用于自我演化。

数据集为LoCoMo，这是一个用于长程对话记忆的基准，实验聚焦于其推理密集的QA任务设置。对比方法包括两种被动基线（Full Text和Naive RAG）和四种主动记忆系统（LangMem、Mem0、A-Mem和LightMem）。

主要结果如下：
1.  **整体性能**：在两种骨干模型下，MemMA（以LightMem为存储后端，记为MemMA_LM）均取得了最佳整体性能。使用GPT-4o-mini时，其F1、B1和ACC分别达到49.40、38.28和81.58%，相比最强的基线LightMem分别提升了+4.82、+1.62和+5.92个百分点。
2.  **类别分析**：MemMA_LM在Multi-Hop和Single-Hop类别上提升显著。使用GPT-4o-mini时，Multi-Hop的ACC从65.62%提升至78.12%，Single-Hop的ACC从78.57%提升至82.86%。
3.  **后端灵活性**：MemMA被实例化在三种不同的存储后端（Single-Agent、A-Mem、LightMem）上，均能带来一致提升。例如，在GPT-4o-mini下，MemMA将Single-Agent后端的ACC从52.60%大幅提升至84.87%，将A-Mem从52.63%提升至78.29%，将LightMem从75.66%提升至81.58%。
4.  **消融研究**：关键组件的贡献得到验证。移除迭代检索（MemMA/R）导致性能下降最大（ACC从84.87%降至70.39%），表明其是前向路径最关键的部分。移除自我演化（MemMA/E）导致ACC从84.87%降至73.68%，表明其对修复构造遗漏至关重要。移除构造指导（MemMA/C）也带来性能下降，表明元思考者的战略指导能减少上游噪声。
5.  **参数分析**：检索预算k存在最优值，对于高质量后端（如LightMem），k=30-40时ACC最佳（81.58%），过大（k=50）会引入噪声。对于弱后端，ACC随k增大持续提升。优化预算H=2时通常达到最佳性能，表明诊断引导的检索能快速收敛，过多迭代可能导致检索漂移。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在评估场景和假设条件上。当前工作主要基于对话中心的长程记忆基准测试LoCoMo，虽然涵盖了多种推理类型，但并未覆盖所有需要持久记忆的场景，例如持续学习、跨模态交互或完全开放域的任务。此外，其反向路径的自我演化机制依赖于两个关键假设：交互流可以清晰划分为会话，以及合成的探测问答对能提供有效的局部监督。这在结构化的对话环境中是合理的，但在会话边界模糊（如流式交互）或交互目标极其开放、难以预先定义探测问题的场景中，该机制的适用性可能受限。

基于此，未来研究可以从以下几个方向深入：一是拓展评估范围，将MemMA框架应用于更广泛、更复杂的任务环境中，如具身智能、长期个性化服务或科学探索任务，以检验其泛化能力。二是改进反向路径的适应性，研究如何在非结构化、连续不断的交互流中动态划分“会话”或生成有效的自我监督信号，例如利用在线学习或强化学习技术，使记忆的演化更能适应实时反馈。三是探索记忆与其他认知模块（如规划、反思）的更深度协同，当前框架主要协调记忆周期的内部环节，未来可研究如何将记忆管理整合进更宏观的Agent决策循环中，实现真正意义上的认知闭环。

### Q6: 总结一下论文的主要内容

论文提出MemMA框架，旨在解决现有记忆增强LLM智能体在长程交互中面临的两个核心挑战：前向路径上的策略盲区（记忆构建与检索依赖局部启发式而非显式策略推理）和后向路径上的监督稀疏性（下游失败难以直接修复记忆库）。其核心贡献在于通过多智能体协同与原地自演化机制，统一协调记忆循环的前后向路径。

方法上，前向路径引入元思考者进行结构化策略规划，指导记忆管理器构建记忆并引导查询推理器迭代检索；后向路径创新性地提出原地自演化记忆构建，通过生成探测性问答对验证记忆内容，并在记忆固化前将失败案例转化为修复动作，实现即时优化。

实验表明，MemMA在LoCoMo基准上显著超越现有基线，兼容多种LLM骨干模型，并能以即插即用方式提升三类存储后端性能。该工作为记忆增强智能体提供了系统化的协同与自我优化机制，推动了长程交互中记忆管理的策略化与自适应能力发展。
