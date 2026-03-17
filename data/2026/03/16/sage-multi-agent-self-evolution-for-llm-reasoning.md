---
title: "SAGE: Multi-Agent Self-Evolution for LLM Reasoning"
authors:
  - "Yulin Peng"
  - "Xinxin Zhu"
  - "Chenxing Wei"
  - "Nianbo Zeng"
  - "Leilei Wang"
  - "Ying Tiffany He"
  - "F. Richard Yu"
date: "2026-03-16"
arxiv_id: "2603.15255"
arxiv_url: "https://arxiv.org/abs/2603.15255"
pdf_url: "https://arxiv.org/pdf/2603.15255v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体协作"
  - "自我演化"
  - "推理"
  - "规划"
  - "强化学习"
  - "代码生成"
  - "数学推理"
  - "训练框架"
relevance_score: 9.0
---

# SAGE: Multi-Agent Self-Evolution for LLM Reasoning

## 原始摘要

Reinforcement learning with verifiable rewards improves reasoning in large language models (LLMs), but many methods still rely on large human-labeled datasets. While self-play reduces this dependency, it often lacks explicit planning and strong quality control, limiting stability in long-horizon multi-step reasoning. We present SAGE (Self-evolving Agents for Generalized reasoning Evolution), a closed-loop framework where four agents: Challenger, Planner, Solver, and Critic, co-evolve from a shared LLM backbone using only a small seed set. The Challenger continuously generates increasingly difficult tasks; the Planner converts each task into a structured multi-step plan; and the Solver follows the plan to produce an answer, whose correctness is determined by external verifiers. The Critic scores and filters both generated questions and plans to prevent curriculum drift and maintain training signal quality, enabling stable self-training. Across mathematics and code-generation benchmarks, SAGE delivers consistent gains across model scales, improving the Qwen-2.5-7B model by 8.9% on LiveCodeBench and 10.7% on OlympiadBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在复杂推理任务中依赖大规模人工标注数据进行强化学习训练的问题。当前，虽然基于可验证奖励的强化学习提升了模型的推理能力，但主流方法仍需大量人工标注数据集，这限制了模型的扩展性和自主适应能力，尤其是在模型能力接近或超越人类水平的领域。现有的一些自博弈和多智能体方法尝试减少对外部数据的依赖，例如通过自对弈或角色分工实现协作推理，但这些方法仍存在明显不足：它们通常在开放域任务中缺乏鲁棒的验证机制，难以有效整合规划能力来处理多步骤的复杂推理，且容易因任务难度失控或质量下降而导致训练不稳定。

针对这些挑战，本文提出了SAGE框架，其核心问题是设计一个能够实现稳定、自主进化的多智能体系统，仅需少量种子示例即可在数学和代码生成等可验证领域进行持续改进。SAGE通过四个专门化的智能体（挑战者、规划者、求解者和批评者）构成闭环，协同进化。挑战者负责生成日益困难的任务，规划者将其转化为结构化多步计划，求解者执行计划产生答案，并由外部验证器判断正确性。批评者则对生成的任务和计划进行评分过滤，防止课程漂移并维持训练信号质量，从而在减少人工数据依赖的同时，确保长期多步推理训练的稳定性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：强化学习用于LLM推理、多智能体LLM系统，以及自博弈与自进化智能体。

在**强化学习用于LLM推理**方面，相关工作如DeepSeek-R1和WebAgent-R1利用可验证奖励（RLVR）来提升数学推理或网页导航能力，而GRPO等无批评者方法则试图降低训练开销。这些方法通常依赖人工标注数据或具身环境。SAGE与它们的不同在于，它仅需少量种子数据，主要依赖自我生成且可验证的任务进行学习，减少了对外部数据的依赖。

在**多智能体LLM系统**方面，MetaGPT通过编码人类工作流程实现任务分解，CAMEL研究角色扮演智能体的协作行为，MARS和MARFT则利用多智能体自博弈或强化微调来提升性能。MALT等框架已将推理分解为生成、验证和精炼等步骤。SAGE沿袭了这一思路，但其创新在于在单一LLM主干上实例化了四个具有特定角色（挑战者、规划者、求解者、批评者）的智能体，并通过共享反馈对它们进行联合训练，实现了更紧密的协同进化。

在**自博弈与自进化智能体**方面，SPIRAL通过零和博弈的自博弈诱导推理策略，Absolute Zero和Agentic Self-Learning等框架通过自我生成任务并利用执行器验证来实现自主进化。AgentEvolver和Agent0也探索了好奇心驱动或工具集成的自进化循环。SAGE与这些工作的主要区别在于，它通过显式地集成**规划者**和**批评者**角色来分解推理过程，并对所有智能体进行联合训练，从而在数学和代码生成领域实现了更稳定、更深层次的多步推理进化。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SAGE的多智能体自进化框架来解决大语言模型在长视野、多步推理任务中缺乏显式规划和强质量控制的问题。其核心方法是构建一个由四个智能体组成的闭环系统，它们共享同一个LLM主干网络，并通过对抗性协同进化来自我提升。

整体框架是一个迭代的闭环流程，包含挑战、规划、求解和批评四个阶段。主要模块包括：1）**Challenger**：从少量种子问题出发，生成带有可验证器的新任务，其奖励由Critic的质量评分、基于Solver失败率的难度奖励以及格式奖励三部分复合而成，以此推动课程向更难但可解的方向演进。2）**Planner**：为给定问题生成结构化多步计划，其输出由Critic评估，只有达到阈值的高质量计划才会被传递给Solver，从而引入了显式规划。3）**Solver**：依据问题（和可能的计划）生成最终答案，其奖励综合了计划质量、外部验证器给出的正确性分数以及格式奖励。4）**Critic**：负责质量控制和格式审查，它对Challenger生成的问题和Planner生成的计划进行评分与过滤，防止课程漂移和数据质量退化；同时通过格式奖励确保输出结构的稳定性。

关键技术体现在多个方面。首先，**对抗性协同进化机制**：Challenger与Solver形成对抗，Solver因正确解答而受奖励，Challenger则因生成Solver无法通过验证的难题而受奖励，这驱动了任务难度的自适应提升。其次，**复合奖励设计**：每个智能体的奖励都融合了任务特定目标（如正确性、难度）和格式合规性，并通过归一化处理确保训练信号稳定。第三，**严格的质量过滤**：对生成的问题和计划设置了阈值（如α=0.7, β=0.3），并结合外部验证器（如代码测试、数学符号验证）进行双重把关，有效防止了数据退化。最后，**同步更新策略**：所有智能体在每次迭代后基于各自角色特定的奖励，通过改进的强化学习算法（Task-Relative REINFORCE++）对共享的LLM主干参数进行联合更新，实现了知识的有效共享与迁移。

创新点在于将多智能体分工协作、显式规划模块、基于验证器的客观奖励以及闭环课程进化有机结合，仅需少量种子数据即可实现稳定、高效的自我训练，显著提升了模型在数学和代码生成等复杂推理任务上的性能。

### Q4: 论文做了哪些实验？

实验基于VeRL框架实现，使用Qwen2.5-3B-Instruct、Qwen2.5-7B-Instruct和Qwen3-4B-Base模型作为骨干，所有智能体均从对应基础模型初始化，采用LoRA（秩128，学习率3e-6）进行训练。对比方法包括原始基础模型、使用相同种子集训练的Absolute-Zero-Reasoning（AZR）和Multi-Agent Evolve（MAE）基线。训练集包含从MATH、GSM8K、HumanEval和MBPP中采样的500个实例。评估涵盖数学推理（GSM8K、MATH作为分布内测试；AIME'24、AIME'25、OlympiadBench、AMC'23作为分布外测试）和代码生成（HumanEval+、MBPP+作为分布内测试；LiveCodeBench v1-v5作为分布外测试），均报告贪婪解码的准确率（pass@1）。

主要结果显示，SAGE在所有模型规模上均带来一致提升。在Qwen-2.5-3B-Instruct上，SAGE的总体平均准确率达42.0%，较基础模型提升1.6%，其中GSM8K从84.6%提升至85.5%，MATH从60.4%提升至66.2%。在Qwen-2.5-7B-Instruct上，总体平均准确率达50.1%，提升2.5%，并在LiveCodeBench上提升8.9%，在OlympiadBench上提升10.7%。分布外泛化能力突出：在Qwen-2.5-7B上，分布外平均准确率提升4.2%（从24.6%至28.8%），同时保持分布内性能；在LiveCodeBench上，SAGE在三个骨干模型上均取得最佳成绩（16.9%、26.4%、30.6%）。消融实验表明，移除任一智能体训练均会导致性能下降，例如移除挑战者训练使LiveCodeBench准确率从16.9%降至9.0%，移除求解器训练使总体平均准确率降至38.2%，验证了各组件互补作用。训练动态分析显示，验证准确率在约100-140步达到峰值（69.5%），随后因过度专业化而逐渐下降；有效问题池规模从初始1,136扩展至20,532，增长18倍。

### Q5: 有什么可以进一步探索的点？

本论文提出的SAGE框架在可验证领域表现出色，但其局限性和未来探索方向值得深入思考。首先，SAGE严重依赖可自动验证正确性的领域（如数学和代码），这限制了其在开放式、主观性任务（如创意写作、伦理推理）中的应用。未来可探索集成学习到的奖励模型或人类偏好模型，以扩展至更广泛的场景。其次，尽管种子集需求已大幅减少至500例，但在极端低资源环境中仍可能构成瓶颈。研究如何通过无监督或弱监督方法进一步降低初始化依赖，甚至实现“零种子”启动，将是一个重要方向。此外，当前框架专注于数学和代码生成，未来可测试其在逻辑推理、科学问题解决等结构化领域的泛化能力，以验证多智能体架构的普适性。从方法改进角度看，可考虑引入动态智能体角色调整机制，使智能体数量或职能能根据任务复杂度自适应演化，以提升效率。同时，当前训练仍可能受噪声累积或课程漂移影响，未来可探索更鲁棒的批判者过滤机制或集成不确定性估计来提升稳定性。最后，将SAGE与外部知识库或工具调用相结合，可能进一步增强其解决复杂现实问题的能力。

### Q6: 总结一下论文的主要内容

该论文提出了SAGE框架，旨在解决大语言模型在多步推理任务中依赖大量人工标注数据、缺乏显式规划与质量控制的问题。其核心贡献是设计了一个由挑战者、规划者、求解者和评判者四个智能体组成的闭环自进化系统，它们共享同一个LLM主干，仅需少量种子问题即可启动协同进化。

方法上，挑战者持续生成难度递增的新任务；规划者将任务转化为结构化的多步计划；求解者执行计划给出答案，其正确性由外部验证器判定；评判者则对生成的问题和计划进行评分筛选，以防止课程漂移并保障训练信号质量，从而实现稳定的自我训练。

主要结论表明，SAGE在数学和代码生成基准测试上均取得了稳定提升，且增益在不同模型规模上保持一致。例如，它将Qwen-2.5-7B模型在LiveCodeBench和OlympiadBench上的性能分别提升了8.9%和10.7%，验证了该框架在减少人工依赖的同时，有效增强了LLM的长期多步推理能力。
