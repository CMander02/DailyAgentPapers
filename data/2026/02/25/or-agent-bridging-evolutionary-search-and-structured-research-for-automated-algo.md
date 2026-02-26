---
title: "OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery"
authors:
  - "Qi Liu"
  - "Ruochen Hao"
  - "Can Li"
  - "Wanjing Ma"
date: "2026-02-14"
arxiv_id: "2602.13769"
arxiv_url: "https://arxiv.org/abs/2602.13769"
pdf_url: "https://arxiv.org/pdf/2602.13769v2"
categories:
  - "cs.AI"
  - "cs.CE"
  - "cs.NE"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "Agent 自演化"
  - "自动化科学发现"
  - "结构化规划"
  - "进化搜索"
  - "反思机制"
  - "研究框架"
  - "算法发现"
relevance_score: 9.0
---

# OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery

## 原始摘要

Automating scientific discovery in complex, experiment-driven domains requires more than iterative mutation of programs; it demands structured hypothesis management, environment interaction, and principled reflection. We present OR-Agent, a configurable multi-agent research framework designed for automated exploration in rich experimental environments. OR-Agent organizes research as a structured tree-based workflow that explicitly models branching hypothesis generation and systematic backtracking, enabling controlled management of research trajectories beyond simple mutation-crossover loops. At its core, we introduce an evolutionary-systematic ideation mechanism that unifies evolutionary selection of research starting points, comprehensive research plan generation, and coordinated exploration within a research tree. We introduce a hierarchical optimization-inspired reflection system in which short-term reflections act as verbal gradients, long-term reflections as verbal momentum, and memory compression as semantic weight decay, collectively forming a principled mechanism for governing research dynamics. We conduct extensive experiments across classical combinatorial optimization benchmarks as well as simulation-based cooperative driving scenarios. Results demonstrate that OR-Agent outperforms strong evolutionary baselines while providing a general, extensible, and inspectable framework for AI-assisted scientific discovery. All code and experimental data are publicly available at https://github.com/qiliuchn/OR-Agent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动化科学发现过程中缺乏结构化、可管理的研究流程的问题。研究背景是，尽管大语言模型和自主智能体在代码生成、假设提出等方面展现出潜力，但现有方法多局限于单次程序生成或简单的进化式搜索，缺乏对复杂、实验驱动的科学探索过程的系统性模拟。传统科学研究涉及假设生成、实验设计、结果分析和回溯调整等非线性、分支化的迭代流程，而现有AI方法往往无法有效管理这些动态的研究轨迹，难以在有限计算资源下平衡探索与利用。

现有方法的不足主要体现在：它们通常依赖简单的突变-交叉循环，缺乏对研究分支的显式管理，无法系统地进行回溯或深度局部探索，且记忆和反思机制较为薄弱。这导致研究过程缺乏结构性，难以在复杂问题空间中高效导航。

本文要解决的核心问题是：如何构建一个能模拟人类研究流程、支持结构化假设管理和系统性探索的自动化研究框架。为此，论文提出了OR-Agent，一个可配置的多智能体框架，它将研究组织为树形工作流，显式建模分支假设生成和系统回溯，从而超越简单的进化循环。其核心创新在于统一了进化选择与系统化构思机制，并引入受优化启发的分层反思系统，以指导研究动态。该框架旨在为算法发现等科学探索任务提供一个通用、可扩展且可检查的自动化研究基础设施。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：自动化算法发现与进化计算、基于大语言模型的科学发现系统，以及面向运筹学（Operations Research, OR）的AI方法。

在**自动化算法发现与进化计算**方面，传统遗传编程（genetic programming）是基础。近期研究开始利用大语言模型（LLM）作为灵活的进化算子，例如FunSearch利用LLM引导变异进行科学发现，LMX实现了语义上有意义的交叉操作。后续系统如EoH、ReEvo和AlphaEvolve进一步探索了反思机制和代码级进化。然而，这些方法通常依赖简单的适应度反馈，缺乏系统性精炼。本文提出的OR-Agent通过将进化算子嵌入到一个支持深度迭代精炼、显式环境探索和反思机制的树搜索工作流中，对此进行了扩展。

在**基于LLM的科学发现系统**领域，近期系统致力于自动化整个科学研究生命周期。本文工作与此目标一致，但特别强调在需要迭代实验的复杂实验驱动环境中进行结构化探索。OR-Agent通过树形工作流管理分支假设生成和系统性回溯，超越了简单的变异-交叉循环。

在**面向运筹学的AI方法**方面，相关技术已从强化学习和神经组合优化发展到基于LLM的方法，后者用于生成解决方案、通过迭代提示提高质量或构建优化问题。超启发式方法则提供了在启发式空间上进行搜索的统一视角。但现有系统大多局限于简单评估设置，缺乏深度、环境驱动的探索机制。OR-Agent通过明确针对需要迭代实验的复杂环境，并引入分层优化启发的反思系统（如将短期反思视为“语言梯度”，长期反思视为“语言动量”），直接解决了这一局限性。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为OR-Agent的可配置多智能体研究框架来解决自动化算法发现中的结构化探索问题。其核心方法是将研究过程组织成一个基于树形结构的工作流，统一了进化搜索的起点选择与系统性的深度研究。

整体框架是一个职责明确的多智能体系统：OR Agent作为入口点管理全局配置并协调多个Lead Agent；Solution Database作为持久化存储库，保存所有生成的解决方案及相关元数据，充当共享的进化记忆；每个Lead Agent作为一轮研究的“首席研究员”，负责选择父解决方案、管理工作流并决定扩展、回溯或终止探索。此外，Idea Agent基于先验实验和反思生成高层解决方案思路；Code Agent将思路转化为可执行代码并进行调试优化；Experiment Agent执行实验、探索复杂环境并总结发现。多个Lead Agent可并发运行，实现不同研究方向的并行探索。

架构设计的创新点主要体现在三个方面。首先，它提出了“进化-系统性构思机制”，将进化算法中对研究起点的选择与全面的研究计划生成、在研究树内的协调探索相结合。研究始于从结构化解决方案数据库中采样父解决方案（类似进化算法的种群初始化），但不同于传统方法依赖频繁的变异和交叉操作，OR-Agent强调在选定有希望的起点后进行深入、系统的局部探索，这更贴近人类科研实践中对方向的迭代精炼和针对性实验。

其次，框架采用了树形结构研究工作流与精炼循环范式。每个Lead Agent将其研究过程组织为一个动态演进的树（通过FlowGraph实现），节点对应包含思路、实现和实验证据的中间研究状态，子节点代表精炼后的变体。研究过程嵌入在迭代的精炼循环中：思路精炼循环持续调整假设，代码精炼循环解决实现错误和性能瓶颈，实验精炼循环反复探测环境以获取反馈。这种显式结构化管理使得研究过程超越了简单的线性或单次探索。

关键技术包括协调式思路生成和研究树遍历策略。为克服独立生成思路导致的冗余问题，Idea Agent在扩展节点时会联合生成一组代表不同方向的子思路，将其视为一个连贯的研究计划，从而显著提高假设空间的覆盖度。在遍历时，Lead Agent采用简单的贪心策略选择未完成的最佳叶节点进行扩展，并允许新方向在初期出现性能退化，仅当持续无改进时才标记节点为终止，这平衡了探索与利用。

此外，框架引入了层次化的、受优化启发的反思系统，其中短期反思充当“语言梯度”，长期反思充当“语言动量”，记忆压缩则类似语义权重衰减，共同构成一个管理研究动态的原则性机制。通过开放研究画布进行人机协作的问题规范，以及支持不同上下文范围（如仅父节点、完整祖先路径或整个研究树）的“树感知”上下文工程，进一步确保了研究的可控性和可解释性。

### Q4: 论文做了哪些实验？

实验设置方面，论文在两类环境中评估OR-Agent：12个经典组合优化问题和1个基于仿真的协同驾驶任务。实验采用两种计算预算进行评估：大语言模型调用次数和函数评估次数，以应对不同场景下的瓶颈。使用的模型为Qwen3（用于经典问题）和DeepSeek V3.2（用于驾驶问题）。

数据集与基准测试包括从ReEvo基准套件扩展而来的12个经典运筹学问题，涵盖旅行商问题（TSP）、车辆路径问题（CVRP）、装箱问题（BPP）等多个范式，以及一个在SUMO中实现的协同驾驶场景。性能评估采用归一化分数，计算公式为（算法得分-最佳得分）/（最佳得分-最差得分），以公平比较异构问题。

对比方法包括多个基于大语言模型的算法发现框架：FunSearch、AEL、EoH和ReEvo。在协同驾驶问题上，还额外与SUMO默认驾驶模型进行了比较。

主要结果如下：在12个经典问题上，OR-Agent的平均归一化分数达到0.924，显著优于所有基线方法（FunSearch: 0.323, AEL: 0.477, EoH: 0.582, ReEvo: 0.492）。在多个具体问题上（如TSP-ACO、TSP-LEHD、BPP-Offline-ACO等），OR-Agent均取得了1.000的最高分。在协同驾驶任务中，在受限运行时间下，OR-Agent得分为48.00，远超最佳基线得分16.10；经过长时间运行后，其最佳解决方案平均得分达到90.24，超过了SUMO默认模型的85.25，且在零碰撞的前提下提升了效率和平滑度。

此外，论文还进行了消融实验，探究了思维深度和记忆压缩的影响。结果表明，标准配置（平衡的树深度）在全局覆盖和局部优化间取得了最佳平衡；而在记忆压缩方面，无显式压缩（约4000词）取得了最佳整体性能。

### Q5: 有什么可以进一步探索的点？

该论文提出的OR-Agent框架在自动化算法发现领域做出了有益尝试，但其局限性和未来探索空间仍较为明显。首先，其核心实验验证集中于组合优化和特定模拟场景，在更开放、定义模糊的真实科学问题（如生物化学实验设计）中的泛化能力有待检验。其次，框架虽引入“言语梯度”等隐喻机制来管理反思，但这些组件的实际效能与更严谨的数学化或理论化解释之间仍存在隔阂，其长期反思的“动量”效应缺乏可量化的评估标准。

未来研究方向可从以下几方面深入：一是**领域扩展与评估体系构建**，需将框架应用于更广泛的科学发现任务，并建立超越性能指标的评估标准，如假设新颖性、研究路径效率等。二是**机制深化与理论夯实**，可尝试将“言语”组件转化为更形式化的元学习或贝叶斯优化过程，使反思机制具有可证明的收敛性质。三是**人机协作模式的探索**，当前框架为全自动，未来可设计混合主动学习循环，允许人类专家介入关键分支决策，形成双向引导。此外，研究树的“记忆压缩”机制可借鉴神经网络剪枝思想，实现更动态的语义知识蒸馏，以应对长期探索中的认知负载问题。

### Q6: 总结一下论文的主要内容

该论文提出了OR-Agent，一个用于自动化算法发现的多智能体研究框架。核心问题是传统进化搜索方法在复杂实验驱动领域中缺乏结构化的假设管理与系统性探索能力。为此，OR-Agent设计了一种树形结构研究工作流，将研究过程组织为可分支、可回溯的探索轨迹，超越了简单的变异-交叉循环。方法上，它结合了进化选择与系统化构思机制：首先进化选择研究起点，然后生成全面研究计划并进行结构化探索；同时引入分层优化启发的反思系统，其中短期反思充当语言梯度，长期反思作为语言动量，记忆压缩则类比语义权重衰减，共同调控研究动态。实验表明，在组合优化基准和协同驾驶模拟场景中，OR-Agent优于强进化基线。其主要贡献在于提供了一个可配置、可扩展、可检查的通用框架，为AI辅助科学发现提供了结构化探索与反思的新范式。
