---
title: "InfEngine: A Self-Verifying and Self-Optimizing Intelligent Engine for Infrared Radiation Computing"
authors:
  - "Kun Ding"
  - "Jian Xu"
  - "Ying Wang"
  - "Peipei Yang"
  - "Shiming Xiang"
date: "2026-02-22"
arxiv_id: "2602.18985"
arxiv_url: "https://arxiv.org/abs/2602.18985"
pdf_url: "https://arxiv.org/pdf/2602.18985v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "工具使用"
  - "自优化"
  - "科学计算"
relevance_score: 9.0
---

# InfEngine: A Self-Verifying and Self-Optimizing Intelligent Engine for Infrared Radiation Computing

## 原始摘要

Infrared radiation computing underpins advances in climate science, remote sensing and spectroscopy but remains constrained by manual workflows. We introduce InfEngine, an autonomous intelligent computational engine designed to drive a paradigm shift from human-led orchestration to collaborative automation. It integrates four specialized agents through two core innovations: self-verification, enabled by joint solver-evaluator debugging, improves functional correctness and scientific plausibility; self-optimization, realized via evolutionary algorithms with self-discovered fitness functions, facilitates autonomous performance optimization. Evaluated on InfBench with 200 infrared-specific tasks and powered by InfTools with 270 curated tools, InfEngine achieves a 92.7% pass rate and delivers workflows 21x faster than manual expert effort. More fundamentally, it illustrates how researchers can transition from manual coding to collaborating with self-verifying, self-optimizing computational partners. By generating reusable, verified and optimized code, InfEngine transforms computational workflows into persistent scientific assets, accelerating the cycle of scientific discovery. Code: https://github.com/kding1225/infengine

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决红外辐射计算领域因高度依赖人工操作而导致的效率低下和可扩展性受限的核心问题。当前，构建完整的红外辐射计算工作流（包括源建模、光谱分析、辐射传输模拟等）需要研究人员作为“指挥者和验证者”，手动集成各种软件包、求解器和物理模型。这个过程不仅劳动密集、需要深厚的领域专业知识，还成为快速迭代和规模化应用的瓶颈。

论文提出的InfEngine是一个自主智能计算引擎，其目标是推动从“人工主导编排”到“人机协作自动化”的范式转变。它通过集成四个专门智能体的多智能体架构，并引入两大核心创新来解决上述问题：1）**自我验证**：通过联合求解器-评估器调试机制，确保生成的代码不仅语法正确，更具备功能正确性和科学合理性，避免产生物理上不可信结果的“静默失败”。2）**自我优化**：利用进化算法，并将验证后的评估器自动转化为适应度函数，实现对解决方案性能的自主、迭代优化，而无需人工指定优化目标。

因此，论文的根本目标是利用具备自我验证与自我优化能力的智能体系统，将研究人员从繁琐的手工编码和集成工作中解放出来，将其转变为可重用、已验证、已优化的持久性科学资产，从而加速科学发现周期。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕两大范式展开：**工具调用**和**代码生成**。

在**工具调用**方面，相关工作包括：SciAgent、AWL等用于科学推理；ChemCrow、ChatMOF等用于化学领域；GeneGPT用于基因组学；PDE-Agent用于求解微分方程。这些研究展示了LLM通过调用预定义工具库来解决特定领域问题的能力。

在**代码生成**方面，相关工作包括：CodeCoT等方法提升通用编程的代码生成质量；FunSearch、EoH、EvoVLMA、Evo-MCTS等工作探索了自动化算法发现与优化。

本文提出的InfEngine与这些工作的关系在于：它同时借鉴并超越了这两种范式。一方面，它像工具调用研究一样，构建了领域专用的工具库（InfTools）；另一方面，它又像代码生成研究一样，能生成可执行的复杂代码。其核心创新在于解决了现有研究的局限性：针对工具调用范式灵活性不足、难以生成可复用软件制品的问题，InfEngine通过代码生成来克服；针对代码生成范式可能产生科学上无效结果、缺乏自我优化机制的问题，InfEngine引入了**自我验证**（通过联合调试确保功能正确性与科学合理性）和**自我优化**（通过进化算法自主优化性能）两大核心机制。特别是其自我优化能力，不同于FunSearch等需要人工指定优化目标，能够从问题描述中自主合成优化目标，实现了更高程度的自动化。

### Q3: 论文如何解决这个问题？

InfEngine通过一个多智能体架构，结合自验证和自优化两大核心创新，将用户自然语言问题转化为可验证、可优化且可部署的代码解决方案，从而解决红外辐射计算领域手动工作流程的瓶颈问题。

其核心架构包含四个专门化的智能体，通过协作流程实现自动化。首先，**问题分析智能体**对用户查询进行分类，并检索InfTools工具库中的相关工具。根据任务类型（辅助型或优化型），系统进入不同的处理分支。

对于辅助型任务，系统启用**自验证**机制。**问题求解智能体**生成初始解决方案代码，同时**评估器生成智能体**根据问题上下文自动生成一个评估脚本。两者协同工作，进行联合调试：求解器生成的代码会由评估器进行功能正确性和科学合理性的检查，任何失败都会触发迭代修正，直到代码通过验证。这种“求解器-评估器”联合调试是实现可靠代码生成的关键。

对于优化型任务，在获得已验证的基础解决方案后，**代码进化智能体**启动**自优化**流程。它采用进化算法，对代码进行迭代变异和交叉。其独特之处在于，适应度函数并非预先设定，而是由系统根据问题描述和生成的评估器**自行发现和构建**，从而实现对性能目标的自主优化。这一过程不断产生新的代码变体，并利用评估器进行评分筛选，最终得到性能最优的解决方案。

整个系统的运行建立在两大基础之上：一是包含270个标准化封装领域工具（InfTools）的知识库，为代码生成提供可组合的原子操作；二是包含200个任务的专用基准测试集（InfBench），其双任务分类（辅助vs优化）为评估自验证和自优化能力提供了严谨的框架。最终，InfEngine的输出不是一次性的答案，而是经过验证和优化、包含所有依赖的、可重用的求解器代码包，从而将计算工作流程转化为持久化的科学资产。

### Q4: 论文做了哪些实验？

论文在InfBench基准上进行了四类核心实验。**实验设置**：使用包含200个红外特定任务的InfBench和270个专用工具集InfTools。InfEngine采用多智能体交互生成代码，设置进化迭代次数N=10，种群大小m=5。基线方法（Direct、FewShot、CodeCoT、SelfDebug、Reflexion、MapCoder）通过检索增强生成（RAG）获得相关工具描述以进行公平对比。主要实验在Qwen3-8B模型上进行。

**基准测试与主要结果**：
1.  **与不同方法对比**：InfEngine在InfBench上达到92.7%的通过率（Overall Pass@1=0.949）和0.733的综合得分，全面超越所有基线。尤其在优化型任务中表现近乎完美（Pass@1=0.991），且在训练和测试集上均取得最佳排名分数（Train Rank=0.749, Test Rank=0.710），显示出优异的泛化能力（训练与测试分数强相关R²=0.699）。
2.  **不同LLM骨干测试**：在七种不同规模的LLM上测试，结果显示性能随模型能力提升而增强。即使使用较小的Qwen3-4B模型，其通过率（0.840）也可与基线方法在更大模型上的结果竞争。
3.  **与人类专家对比**：在效率上，InfEngine生成工作流的速度比人工专家快21倍（辅助型任务加速8.6-22.7倍，优化型任务加速1.2-4.4倍）。在质量上，InfEngine在优化型任务上产生的解决方案，其综合胜率/平率在测试集上超过50%，匹配或超越了人工编写代码的水平。
4.  **组件消融研究**：通过对比完整系统、仅保留自验证的变体（InfEngine-evo）和进一步移除评估器生成的变体（InfEngine-eval-evo），验证了自验证和自优化组件的有效性。自验证确保了代码正确性，自优化则在优化型任务中驱动了显著的性能提升（完整系统在测试分数上对仅验证变体的胜率达54.3%）。

### Q5: 有什么可以进一步探索的点？

基于论文讨论部分，InfEngine的局限性及未来可探索方向包括：**工具生态扩展**，当前InfTools虽涵盖270个工具，但相比真实科研中庞大且常为专有的工具链仍有限，未来需让领域专家能基于接口标准封装自有工具，整合孤立能力。**领域泛化验证**，目前验证集中于红外辐射计算，需将基准扩展至计算化学、材料信息学等邻近领域，以证明架构的通用性。**优化效率提升**，进化算法计算开销较大，需研究更高效的搜索策略以降低优化成本。

更长远的方向是**向智能计算平台演进**，构建一个联邦式、工具无关的平台，能聚合和编排来自公共库及机构私有库的领域专用工具，通过统一接口为研究者生成针对其特定计算环境与资源定制的、经过验证和优化的求解器代码，实现平台智能与私有数据及硬件的无缝衔接。这一转变有望将科学工作流转化为可持久共享的资产，重塑科研循环，使研究者能更专注于高层问题提出与决策，加速跨学科发现。

### Q6: 总结一下论文的主要内容

这篇论文提出了InfEngine，一个面向红外辐射计算的自验证与自优化智能引擎，旨在将传统依赖人工编排的工作流转变为协同自动化的新范式。其核心贡献在于构建了一个由四个专业智能体组成的自主计算系统，并通过两大创新机制实现突破：一是**自验证机制**，通过求解器与评估器的联合调试，确保计算结果的函数正确性与科学合理性；二是**自优化机制**，利用进化算法并结合自主发现的适应度函数，实现工作流程的自动化性能优化。在包含200个红外特定任务的InfBench基准测试中，InfEngine借助270个精选工具（InfTools），达到了92.7%的任务通过率，并将工作流生成速度提升至专家手动操作的21倍。该研究的根本意义在于展示了一种科研范式的转变——研究者可以从手动编码转向与具备自我验证与优化能力的计算伙伴协同工作，其产出的可复用、已验证和优化的代码能将计算工作流转化为持久的科学资产，从而显著加速科学发现周期。
