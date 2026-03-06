---
title: "EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection"
authors:
  - "Shuo Yang"
  - "Soyeon Caren Han"
  - "Xueqi Ma"
  - "Yan Li"
  - "Mohammad Reza Ghasemi Madani"
  - "Eduard Hovy"
date: "2026-03-05"
arxiv_id: "2603.04900"
arxiv_url: "https://arxiv.org/abs/2603.04900"
pdf_url: "https://arxiv.org/pdf/2603.04900v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "工具使用"
  - "策略优化"
  - "自演化"
  - "模块化"
  - "进化算法"
  - "信用分配"
  - "长视野任务"
relevance_score: 9.5
---

# EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection

## 原始摘要

LLM-based agents depend on effective tool-use policies to solve complex tasks, yet optimizing these policies remains challenging due to delayed supervision and the difficulty of credit assignment in long-horizon trajectories. Existing optimization approaches tend to be either monolithic, which are prone to entangling behaviors, or single-aspect, which ignore cross-module error propagation. To address these limitations, we propose EvoTool, a self-evolving framework that optimizes a modular tool-use policy via a gradient-free evolutionary paradigm. EvoTool decomposes agent's tool-use policy into four modules, including Planner, Selector, Caller, and Synthesizer, and iteratively improves them in a self-improving loop through three novel mechanisms. Trajectory-Grounded Blame Attribution uses diagnostic traces to localize failures to a specific module. Feedback-Guided Targeted Mutation then edits only that module via natural-language critique. Diversity-Aware Population Selection preserves complementary candidates to ensure solution diversity. Across four benchmarks, EvoTool outperforms strong baselines by over 5 points on both GPT-4.1 and Qwen3-8B, while achieving superior efficiency and transferability. The code will be released once paper is accepted.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体在复杂任务中工具使用策略的优化难题。研究背景是，当前基于LLM的智能体依赖外部工具来完成复杂任务，其工具使用策略需要协调目标分解、工具选择、参数构建和结果综合等多个相互依赖的能力。然而，在实际应用中，由于任务往往是长视野、决策链紧密耦合的，且监督信号通常只在任务结束时才给出，这导致了一个严重的“信用分配”问题：难以追溯失败的具体根源，从而阻碍了策略的针对性改进。

现有方法存在明显不足。早期方法依赖人工设计的提示模式或固定启发式规则，不仅需要大量手动工作，而且在遇到未预见的错误时容易导致系统崩溃。近期的自动化优化方法则走向两个极端：一种是“整体式策略优化”，对整个智能体提示进行全局黑盒搜索，这容易导致不同模块的行为纠缠在一起，修复一个错误可能破坏其他能力；另一种是“单方面优化”，仅孤立地改进单个组件（如规划或工具调用），却忽略了长轨迹中跨模块的错误传播。这两种范式都无法同时实现精准的错误定位和多模块的协调优化。

因此，本文要解决的核心问题是：如何在大语言模型智能体的工具使用策略优化中，有效解决延迟监督下的信用分配难题，并实现跨多个相互依赖模块的、精准且协调的策略改进。为此，论文提出了EvoTool框架，通过一种无梯度的进化范式，将工具使用策略分解为规划器、选择器、调用器和综合器四个模块，并利用轨迹归因的责备分配、反馈引导的定向突变和多样性感知的种群选择三个新机制，在自进化循环中迭代优化这些模块，从而实现既精准定位错误又兼顾整体协调性的策略优化。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕智能体工具使用策略学习和自进化系统两个方向展开。

在**智能体工具使用策略学习**方面，相关工作可分为三类。早期方法依赖静态工程，如手工设计提示模式和固定控制启发式，其泛化能力差且人工成本高。随后出现了基于训练的方法，通过监督微调或强化学习内化工具使用，但模型权重固定且数据需求大，难以适应动态环境。近期研究转向免训练优化，通过在线交互反馈优化行为而无需更新权重，但面临全局编辑易导致行为纠缠、局部优化又忽略模块间错误传播的权衡。本文提出的EvoTool属于免训练优化范畴，其创新在于通过梯度自由搜索，结合归因与定向突变，实现了对故障模块的精准修复。

在**自进化智能体系统**方面，相关研究旨在使智能体通过行动、评估和更新策略的循环来持续提升能力。这包括将失败转化为自然语言反馈的自我反思与校正，以及积累技能或更新组件的持续改进循环。然而，现有框架多依赖贪婪选择，容易过早收敛于单一策略，丢弃了应对异构任务所需的多样化行为。为此，本文引入了多样性感知的种群选择机制，以维持异构候选策略池，避免早熟收敛。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为EvoTool的自进化框架来解决工具使用策略优化问题，其核心是采用一种免梯度的进化范式，对模块化的工具使用策略进行迭代优化。整体框架将智能体的工具使用策略分解为四个模块：规划器（Planner）、选择器（Selector）、调用器（Caller）和合成器（Synthesizer），并保持基础大语言模型的权重不变。框架维护一个候选模块规格的种群，通过一个自改进循环进行迭代优化。

该框架的核心方法依赖于三个新颖的机制。首先，**基于轨迹的归因机制** 负责定位故障模块。它从任务执行的轨迹中提取诊断事件，并利用一个“归因大模型”为每个模块输出归因分数，从而将失败或次优表现归咎于特定的责任模块。其次，**反馈引导的定向突变机制** 仅对归因出的目标模块进行更新。它利用一个“突变大模型”，根据完整的交互轨迹生成自然语言反馈，该反馈既解释错误模式，又提出针对该模块规格的具体、局部化的编辑建议，从而产生一个仅在目标模块上与父代不同的子代候选。最后，**多样性感知的种群选择机制** 确保解决方案的多样性。它在一个保留的评估集上，采用实例级胜者准则来筛选种群：一个候选策略只有在至少一个实例上取得最高分才会被保留。这保留了具有互补能力的候选者，防止种群收敛到单一模式。

EvoTool的创新点在于其模块化、定向化和多样化的协同设计。与整体优化方法容易导致行为纠缠，或单方面优化方法忽略跨模块错误传播不同，EvoTool通过精准的归因实现了细粒度的、可解释的模块级更新，有效缓解了长视野轨迹中信用分配和延迟监督的挑战。同时，其多样性选择策略避免了遗忘已掌握的行为，提升了策略的鲁棒性和泛化能力。实验表明，该方法在多个基准测试上显著优于现有基线，并展现出更高的效率和可迁移性。

### Q4: 论文做了哪些实验？

论文在四个基准测试上进行了实验评估。实验设置方面，使用了GPT-4.1和Qwen3-8B作为基础大语言模型，并在相同的工具集和评估预算下与基线方法进行公平比较。

使用的数据集/基准测试包括：1) ToolBench，用于测试在RapidAPI上的大规模API泛化能力，报告G1/G2/G3子集的通过率；2) RestBench，评估在真实REST API上的顺序工具使用，报告TMDB和Spotify子集的成功率；3) τ-Bench，评估零售和航空领域中具状态、长视野的智能体-用户交互，报告Pass@1以评估单次尝试成功率；4) BFCL，评估工具调用的函数调用能力，报告选定的单轮和多轮子集的准确率。

对比方法涵盖三类工具使用策略设计：1) 手工设计的策略，如ReAct、CoT和Plan-and-Solve；2) 整体式策略优化方法，如OPRO、PromptBreeder和EvoPrompt；3) 单方面（局部）策略优化方法，如AdaPlanner、DRAFT、EasyTool和AnyTool。

主要结果与关键数据指标如下：在GPT-4.1后端上，EvoTool取得了70.6的整体平均分，比最强的单方面基线DRAFT高出近6分，比最佳的整体式基线EvoPrompt高出约7分。在Qwen3-8B上，它比第二好的基线高出5.2分。在复杂的τ-Bench上，EvoTool达到了52.0分，显著高于DRAFT的38.8分和EasyTool的40.6分。在BFCL多轮任务上，EvoTool也以42.3分领先。此外，EvoTool在性能进展上表现出最一致的提升，并且在成本效益上，能以最少的token使用量实现优越的性能。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在计算效率和泛化场景两方面。首先，尽管通过归因和定向突变减少了计算开销，但进化过程仍需多次迭代推理，在严格实时场景下可能产生延迟。其次，当前评估局限于文本和API环境，未能验证框架在多模态工具或具身智能体中的适用性。

未来研究方向可从三个维度拓展：一是优化进化效率，例如引入轻量级价值网络预筛选突变方向，或设计分层进化策略减少迭代轮次；二是拓展应用边界，探索框架在视觉-语言工具链或机器人任务规划中的迁移能力，需研究跨模态错误的模块化归因方法；三是增强策略的泛化性，当前模块划分可能未覆盖复杂工具交互中的边缘情况，可结合课程学习逐步增加任务复杂度，或引入外部知识库辅助突变生成，使进化过程更稳定高效。

### Q6: 总结一下论文的主要内容

该论文提出了EvoTool框架，旨在解决基于大语言模型（LLM）的智能体在复杂任务中工具使用策略优化面临的挑战，如延迟监督和长轨迹中的信用分配困难。现有方法往往存在行为纠缠或忽略模块间错误传播的问题。

EvoTool的核心贡献在于采用一种无梯度的进化范式，对模块化的工具使用策略进行自我演化优化。它将策略分解为规划器、选择器、调用器和合成器四个模块，并通过三个新颖机制在自改进循环中迭代优化：基于轨迹的归因定位失败模块，反馈引导的定向突变通过自然语言批评仅编辑问题模块，以及多样性感知的种群选择保留互补候选方案以确保多样性。

实验表明，在四个基准测试上，EvoTool在GPT-4.1和Qwen3-8B上均显著优于基线模型超过5个百分点，同时展现出更高的效率和可迁移性。该工作为LLM智能体的策略优化提供了一种模块化、可解释且高效的进化新路径。
