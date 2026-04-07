---
title: "Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints"
authors:
  - "Kefan Li"
  - "Yuan Yuan"
  - "Mengfei Wang"
  - "Shihao Zheng"
  - "Wei Wang"
  - "Ping Yang"
  - "Mu Li"
  - "Weifeng Lv"
date: "2026-04-06"
arxiv_id: "2604.04580"
arxiv_url: "https://arxiv.org/abs/2604.04580"
pdf_url: "https://arxiv.org/pdf/2604.04580v1"
categories:
  - "cs.SE"
tags:
  - "代码智能体"
  - "多智能体协作"
  - "软件工程智能体"
  - "工具使用"
  - "规划与推理"
  - "测试与验证"
  - "SWE-bench"
  - "代码修复"
relevance_score: 9.0
---

# Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints

## 原始摘要

Software engineers resolving repository-level issues do not treat existing tests as immutable correctness oracles. Instead, they iteratively refine both code and the tests used to characterize intended behavior, as new modifications expose missing assumptions or misinterpreted failure conditions. In contrast, most existing large language model (LLM)-based repair systems adopt a linear pipeline in which tests or other validation signals act mostly as post-hoc filters, treating behavioral constraints as fixed during repair. This formulation reduces repair to optimizing code under static and potentially misaligned constraints, leading to under-constrained search and brittle or overfitted fixes. We argue that repository-level issue resolution is fundamentally not optimization under fixed tests, but search over evolving behavioral constraints. To operationalize this view, we propose Agent-CoEvo, a coevolutionary multi-agent framework in which candidate code patches and test patches are jointly explored and iteratively refined. Rather than treating tests as immutable oracles, our framework models them as dynamic constraints that both guide and are revised by the repair process. Through mutual evaluation and semantic recombination, code and test candidates progressively narrow the space of behavior consistent with the issue description. Evaluated on SWE-bench Lite and SWT-bench Lite, Agent-CoEvo consistently outperforms state-of-the-art agent-based and agentless baselines in both repair success and test reproduction quality. Our findings suggest that enabling repair agents to revise behavioral constraints during search is critical for reliable issue resolution, pointing toward a shift from code-only optimization to coevolution of implementation and specification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在自动化仓库级（repository-level）软件问题修复时存在的一个根本性局限：现有方法通常将测试用例视为固定不变的正确性“神谕”（oracle），而现实中的软件工程师在解决问题时，会迭代地同时修改代码和测试用例。研究背景是，尽管LLM在代码生成、程序修复等任务上表现出色，但仓库级问题修复需要处理多文件依赖、项目特定约束和动态执行行为，远比函数级任务复杂。现有主流方法（如Agentless、SpecRover等）采用线性流水线，即先生成候选代码补丁，再用静态的测试集进行过滤。这种“固定测试”的假设存在严重不足：首先，自动化流程中可用的测试往往基于对问题的部分理解生成，本身可能包含错误或遗漏，将其作为固定约束会导致搜索空间要么约束不足（产生满足不完整测试集但实际错误的补丁），要么约束错误（正确的修复因测试本身有缺陷而被拒绝），最终导致系统产生脆弱或过拟合的修复方案。因此，本文要解决的核心问题是：如何将仓库级问题修复重新定义为在**演化中的行为约束**下进行搜索的过程，而非在固定测试下的代码优化。为此，论文提出了Agent-CoEvo框架，通过一个协同进化的多智能体系统，让代码补丁和测试补丁被联合探索与迭代精化，使行为约束（测试）在修复过程中也能被动态修订，从而更可靠地解决实际问题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**基于LLM的代码修复方法**和**基于代理的软件工程系统**。

在**代码修复方法**方面，现有工作如Agentless、SpecRover、Moatless Tools、KGCompass和DARS等，大多采用线性流水线范式：先生成候选代码补丁，再利用测试等验证信号进行事后过滤。这些方法将行为约束（如测试）视为修复过程中固定不变的正确性预言，本质上是在静态且可能未对齐的约束下进行代码优化。本文指出，这种“固定测试”的假设与真实世界中工程师协同演化代码和测试的实践存在根本性错配，容易导致搜索空间约束不足或产生脆弱的过拟合修复。

在**基于代理的系统**方面，现有研究致力于构建能够执行复杂软件工程任务的自主代理。然而，这些系统通常也将测试生成和代码修复视为分离的、顺序性的子任务。本文提出的Agent-CoEvo框架与这些工作的核心区别在于，它将代码补丁和测试补丁的探索与迭代精化建模为一个**协同演化**的搜索过程。测试不再是不可变的预言，而是能在修复过程中被修订的动态约束。通过多代理的相互评估与语义重组，框架能同时搜索与问题描述一致的行为空间，实现了实现与规约的共进化，从而超越了传统仅优化代码或顺序处理任务的范式。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Agent-CoEvo的协同进化多智能体框架来解决传统LLM修复系统将测试视为固定约束所导致的搜索空间受限和修复方案脆弱的问题。其核心思想是将仓库级问题解决重新定义为在**演化行为约束下的搜索**，而非在固定测试下的优化。

**整体框架**分为两个主要阶段。第一阶段是**问题定位**：由LocationAgent分析自然语言问题描述，生成一个复现脚本，通过动态执行跟踪精确定位到导致错误的文件和代码行，为后续修复提供上下文。第二阶段是**协同进化过程**，这是框架的核心搜索循环。

**核心方法与架构设计**围绕一个双种群进化算法展开，包含两个主要智能体：
1.  **CodeAgent**：负责维护和演化候选代码补丁种群。
2.  **TestAgent**：负责维护和演化候选测试补丁种群。

这两个种群通过一个迭代的**协同进化循环**进行联合优化，主要包含以下关键步骤：
*   **初始化与过滤**：两个智能体利用LLM独立生成初始种群。对于测试补丁，系统会过滤掉那些在原始错误仓库上能通过的测试，确保初始测试与报告的问题行为相关。
*   **交叉评估与适应度计算**：这是框架的创新核心。系统构建一个**执行矩阵**，记录每个代码补丁与每个测试补丁组合的执行结果（通过/失败）。基于此矩阵，采用一种**共识驱动的适应度函数**：
    *   **代码适应度**：结合了“通过测试的数量”和“行为一致的代码补丁数量”。这奖励那些既能通过大量测试，又与种群中其他高质量补丁行为一致的代码。
    *   **测试适应度**：基于其通过的代码补丁的适应度之和来计算。这鼓励演化出能更好区分优劣修复方案的、信息量更大的测试约束。
*   **选择与语义交叉**：采用锦标赛选择法挑选父代。关键的创新在于**语义交叉算子**：它并非简单的语法拼接，而是由LLM分析两个父代补丁的逻辑，综合其优势生成一个语义上融合的新补丁，从而聚合不同搜索轨迹中发现的部分行为修正。
*   **精英保留**：每代中最优的个体被直接保留到下一代，确保种群最优适应度不会下降。

**关键技术**包括：1）用于精确问题定位的动态脚本生成与执行跟踪；2）将代码与测试的交互建模为演化约束图的交叉评估机制；3）促进语义融合而非语法重组的LLM驱动交叉算子；4）确保每次评估隔离、可复现的Docker化工具集（如Bash工具、文件操作工具）。

**创新点**在于根本性地转变了问题范式——将测试从静态的、事后的正确性预言，转变为与代码修复**共同演化的动态行为约束**。通过代码假设与约束假设之间的相互评估和迭代精化，系统能够逐步收敛到与问题描述一致的行为空间，从而产生更健壮、更少过拟合的修复方案。

### Q4: 论文做了哪些实验？

论文在SWE-bench Lite和SWT-bench Lite两个数据集上进行了实验评估。实验设置方面，作者提出的Agent-CoEvo框架采用多智能体协同进化机制，种群大小设为10，最大进化迭代次数为5，其中定位智能体使用低温设置（0.2）以稳定定位，代码和测试智能体使用温度0.5以保持生成多样性，所有实验均通过OpenRouter API使用DeepSeek-V3-0324模型完成。

对比方法涵盖了三大类：1) 以代码为中心的修复智能体（如Agentless、SpecRover、Moatless Tools、SWE-Search、KGCompass、DARS），它们在固定测试验证下优化代码补丁；2) 测试生成智能体（如SWE-Agent+、AssertFlip），专注于构建捕获失败行为的测试，但不联合优化代码修改；3) 通用软件智能体（如AutoCodeRover、SWE-Agent、OpenHands），能生成代码和测试，但未将修复明确建模为对演化行为约束的耦合搜索。

主要结果如下：在SWE-bench Lite（300个问题）上，Agent-CoEvo取得了41.33%的解决率，优于最强的代码中心基线DARS（37.00%）和KGCompass（36.67%）。在SWT-bench Lite（276个实例）上，其解决率达到46.4%，显著超过之前的测试生成系统如AssertFlip（38.0%）；同时，其ΔC指标（反映测试对修改区域的覆盖改进）达到56.0%，也为最高。重叠分析显示，Agent-CoEvo解决了124个问题，其中13个是独有解决的，其联合召回率（UR）为71.68%，表明其能覆盖多数现有范式可解的问题并减少因约束不匹配导致的假阴性。消融实验进一步证实，移除测试智能体、进化机制或精英保留均会导致性能下降，凸显了协同进化各组件的重要性。

### Q5: 有什么可以进一步探索的点？

该论文提出的协同进化框架虽然有效，但仍存在一些局限性和值得深入探索的方向。首先，其计算成本相对较高，主要源于多智能体交互和迭代进化过程。未来研究可探索更高效的进化策略，例如引入启发式规则或元学习来指导搜索方向，减少不必要的迭代轮次，从而在保持性能的同时降低开销。

其次，当前框架主要依赖LLM进行语义交叉和评估，这可能受限于模型本身的推理能力和对复杂代码语义的理解。一个潜在的改进方向是结合形式化方法或符号执行，为行为约束的演化和验证提供更精确的数学基础，从而增强修复的可靠性和泛化能力。

此外，论文中的协同进化目前集中于代码和测试的共变，但实际软件修复往往涉及更广泛的上下文，如文档更新、API变更或依赖调整。未来工作可以将修复范围扩展到这些维度，实现更全面的仓库级问题解决。最后，如何将此类系统更好地集成到开发工作流中，提供可解释的进化路径和决策依据，也是推动其实际应用的关键。

### Q6: 总结一下论文的主要内容

该论文针对传统LLM代码修复系统将测试用例视为固定不变的正确性标准所导致的局限性，提出了一种新的视角和方法。核心问题在于，现实中的软件工程师在解决仓库级问题时，会同时迭代修改代码和测试用例，而现有方法将行为约束固定化，容易产生搜索空间不足、修复方案脆弱或过拟合的问题。

为此，作者提出了Agent-CoEvo框架，其核心贡献是将仓库级问题解决重新定义为代码与行为约束的共同进化过程。该方法采用多智能体协同进化框架，让代码补丁和测试补丁的候选方案被联合探索与迭代精炼。通过相互评估和语义重组，代码和测试候选方案逐步收敛到与问题描述一致的行为空间。

实验表明，在SWE-bench Lite和SWT-bench Lite基准测试上，Agent-CoEvo在修复成功率和测试重现质量上均持续优于最先进的基于智能体及非智能体的基线方法。主要结论是，允许修复智能体在搜索过程中修订行为约束，对于可靠的问题解决至关重要，这标志着从单纯的代码优化向实现与规约共同进化的范式转变。
