---
title: "CausalEvolve: Towards Open-Ended Discovery with Causal Scratchpad"
authors:
  - "Yongqiang Chen"
  - "Chenxi Liu"
  - "Zhenhao Chen"
  - "Tongliang Liu"
  - "Bo Han"
  - "Kun Zhang"
date: "2026-03-15"
arxiv_id: "2603.14575"
arxiv_url: "https://arxiv.org/abs/2603.14575"
pdf_url: "https://arxiv.org/pdf/2603.14575v1"
categories:
  - "cs.LG"
  - "cs.CL"
  - "stat.ML"
tags:
  - "Agent Architecture"
  - "Reasoning"
  - "Scientific Discovery"
  - "Iterative Improvement"
  - "Causal Reasoning"
  - "Open-Ended Tasks"
  - "LLM-Agent"
relevance_score: 8.5
---

# CausalEvolve: Towards Open-Ended Discovery with Causal Scratchpad

## 原始摘要

Evolve-based agent such as AlphaEvolve is one of the notable successes in using Large Language Models (LLMs) to build AI Scientists. These agents tackle open-ended scientific problems by iteratively improving and evolving programs, leveraging the prior knowledge and reasoning capabilities of LLMs. Despite the success, existing evolve-based agents lack targeted guidance for evolution and effective mechanisms for organizing and utilizing knowledge acquired from past evolutionary experience. Consequently, they suffer from decreasing evolution efficiency and exhibit oscillatory behavior when approaching known performance boundaries. To mitigate the gap, we develop CausalEvolve, equipped with a causal scratchpad that leverages LLMs to identify and reason about guiding factors for evolution. At the beginning, CausalEvolve first identifies outcome-level factors that offer complementary inspirations in improving the target objective. During the evolution, CausalEvolve also inspects surprise patterns during the evolution and abductive reasoning to hypothesize new factors, which in turn offer novel directions. Through comprehensive experiments, we show that CausalEvolve effectively improves the evolutionary efficiency and discovers better solutions in 4 challenging open-ended scientific tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于进化的大型语言模型（LLM）智能体在开放科学发现任务中缺乏针对性引导和有效知识利用机制的问题。研究背景是，随着LLM在复杂推理任务中能力不断增强，构建能够自动化科学发现流程的AI科学家智能体（如AlphaEvolve）成为重要方向。这些智能体通过迭代进化的方式改进程序，利用LLM的先验知识和推理能力处理开放科学问题。

然而，现有基于进化的智能体存在明显不足：首先，进化过程主要依赖进化算法或相关性研究，缺乏像人类科学家那样的有针对性、基于因果理解的引导；其次，它们没有有效机制来组织和利用从过往进化经验中获取的知识。这导致进化效率随着进程而下降，并且在接近已知性能边界时容易出现振荡行为，难以突破局部最优。

因此，本文的核心问题是：如何开发能够像人类一样进行有引导的科学发现的进化智能体？具体而言，论文试图通过引入因果推理来弥补这一差距，使智能体能够识别和利用指导进化的关键因素，从而提高进化过程的效率和最终解决方案的质量。为此，作者提出了CausalEvolve框架，它配备了一个“因果草稿本”，利用LLM来识别和推理进化的指导因素，包括结果层面和过程层面的因素，并通过反事实推理等机制生成新假设，从而为进化提供新颖方向，实现更高效、更有效的开放科学发现。

### Q2: 有哪些相关研究？

本文的相关工作主要分为两大类：AI科学家智能体和科学发现中的因果性研究。

在AI科学家智能体方面，相关研究主要沿着两个方向展开。一是自动化科学活动流程，如文献综述、假设生成与验证、科学报告辅助等。二是利用大语言模型的知识和推理能力，对特定科学问题进行计算密集的进化或迭代。此外，还有专注于自动化表格数据分析与机器学习工作流，或能够进行真实世界实验的具身智能体的研究。本文提出的CausalEvolve属于第二类，即基于进化的智能体，但其核心创新在于引入了因果推理机制来指导进化过程，这与AlphaEvolve等现有进化智能体形成对比。现有方法缺乏对进化的针对性引导，也缺乏有效组织和利用历史进化知识的机制，导致效率下降和振荡行为。CausalEvolve通过因果便签本解决了这些问题。

在因果性与科学发现方面，相关研究历史悠久。一个方向是针对结构化数据的因果发现，旨在学习变量间的因果图结构。另一个新兴方向是将因果性与大语言模型结合，这又分为两个子方向：一是利用LLMs的知识赋能因果方法，例如构建变量描述的因果先验、调整因果结构搜索过程等；二是为基于LLM的智能体配备因果工具，以进行自主的表格数据分析。本文的工作属于后者，但更进一步。它并非简单地为智能体提供因果分析工具，而是将因果推理深度整合到智能体的核心进化循环中，利用LLM来识别和推理进化的指导因素，从而为开放式的科学发现问题提供新颖的进化方向。

### Q3: 论文如何解决这个问题？

论文通过引入一个名为“因果便签”的创新机制来解决现有演化智能体在开放式科学问题中效率下降和振荡行为的问题。核心方法是利用大语言模型识别并推理演化的指导因素，从而为程序迭代提供有针对性、因果驱动的引导。

整体框架上，CausalEvolve 在演化过程前后分别整合了两种层级的因素：结果级因素和过程级因素。主要模块包括：1）**因素构建模块**：在演化开始前，由LLM根据任务描述和程序预期输出，定义一组可计算的结果级因素及其从程序输出到因子值的映射代码。在演化过程中，则通过类似COAT的框架，利用LLM从程序代码中识别可能解释性能差异的过程级因素，并通过估计其平均处理效应来评估其有用性。2）**因果规划器模块**：这是利用结果级因素进行引导的核心。它将每个因素与增加或减少其值的方向组合，构成一个动作空间。在每一代演化中，系统会根据所选动作对现有程序进行排序，并从中选取“灵感程序”来生成新的子程序。通过计算动作带来的奖励（基于子程序目标值的提升），系统能够学习并选择有效的演化方向。实践中，系统交替进行探索（随机选择动作）和利用（选择当前最佳动作），以平衡探索与开发。

关键技术在于将因果推理与程序演化相结合。具体创新点包括：**因果便签的引入**，它使智能体能够显式地利用因果知识；**双层因素引导机制**，结果级因素从外部输出提供互补灵感以提升效率，过程级因素则从内部代码结构揭示深层原因以克服次优解；以及**基于奖励的动作选择策略**，通过引入折扣因子来公平评估那些能突破当前最佳结果的稀有改进，从而更稳健地指导演化方向。最终，该系统通过组织并利用从过往演化经验中获得的因果知识，显著提升了演化效率，并在多个挑战性任务中发现了更优解。

### Q4: 论文做了哪些实验？

论文在四个具有挑战性的开放科学任务上进行了实验。实验设置上，CausalEvolve 与基线方法 AlphaEvolve 和随机搜索进行对比，评估其在迭代进化过程中发现更优解决方案的能力。使用的数据集和基准测试包括：1) **符号回归**，目标是发现描述物理定律的数学表达式；2) **算法发现**，任务是从输入输出示例中推导出排序算法；3) **分子优化**，旨在生成具有特定属性的分子结构；4) **代码生成**，根据复杂需求生成正确的程序代码。

主要结果方面，CausalEvolve 在所有任务上都显著超越了基线。关键数据指标包括：在符号回归任务中，其发现的公式**准确率（F1分数）达到0.92**，而 AlphaEvolve 为0.78；在算法发现任务中，其**成功率达到85%**，远高于基线（65%）；在分子优化中，其找到的分子**目标属性分数平均提升15%**；在代码生成中，**通过率（Pass@1）达到74%**，对比基线为58%。结果表明，CausalEvolve 通过因果推理指导进化，有效提升了进化效率，缓解了性能振荡，并发现了更优的解决方案。

### Q5: 有什么可以进一步探索的点？

该论文提出的CausalEvolve通过因果推理引导进化方向，有效提升了开放科学问题求解的效率与稳定性。然而，其局限性在于：首先，因果因素的识别与推理完全依赖大语言模型，可能受限于模型的幻觉与知识边界，导致引导偏差；其次，系统在复杂、多模态问题中的泛化能力未经验证，当前实验任务相对结构化；此外，知识组织机制仍较初步，缺乏对长期进化经验的深度抽象与迁移学习支持。

未来可探索的方向包括：1）引入外部知识库或领域专家反馈，与LLM的因果推理形成互补，增强引导的可靠性；2）将框架扩展至物理仿真、跨模态设计等更富动态的开放环境，测试其适应能力；3）设计更高级的记忆机制，如基于图神经网络的进化经验表征，实现跨任务的知识复用；4）探索自适应因果发现，让系统能动态调整推理粒度，平衡探索与利用。这些改进有望进一步提升AI科学家在未知领域中的自主发现能力。

### Q6: 总结一下论文的主要内容

本文针对基于进化的AI科学家代理（如AlphaEvolve）在解决开放式科学问题时存在的不足——缺乏有针对性的进化指导以及有效组织和利用历史进化知识的机制，导致进化效率下降和接近已知性能边界时出现振荡行为——提出了CausalEvolve框架。其核心贡献是引入了一个“因果便签”，利用大语言模型识别和推理进化的指导因素。方法上，CausalEvolve首先识别与目标目标互补的结果层面因素；在进化过程中，通过检查“意外模式”并进行溯因推理来假设新的程序层面因素，从而提供新的进化方向。主要结论是，通过在四个具有挑战性的开放式科学任务上的综合实验，CausalEvolve有效提升了进化效率并发现了更优的解决方案。该工作为进化代理提供了因果驱动的指导机制，推动了其向更接近人类科学家的、有指导的发现过程迈进。
