---
title: "Self-Evolving Deep Research via Joint Generation and Evaluation"
authors:
  - "Han Zhu"
  - "Chengkun Cai"
  - "Yuanfeng Song"
  - "Xing Chen"
  - "Sirui Han"
  - "Yike Guo"
date: "2026-06-03"
arxiv_id: "2606.04507"
arxiv_url: "https://arxiv.org/abs/2606.04507"
pdf_url: "https://arxiv.org/pdf/2606.04507v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "训练框架"
  - "Agent评估"
  - "开放式Agent"
  - "自进化"
  - "报告生成"
relevance_score: 8.5
---

# Self-Evolving Deep Research via Joint Generation and Evaluation

## 原始摘要

Large Language Models (LLMs) have become increasingly adopted in daily applications, with deep research standing out as a particularly important capability. Unlike traditional question-answering (QA) tasks, deep research report generation lacks definitive ground-truth, making reward design inherently unverifiable and limiting effective reinforcement learning. Existing approaches mitigate this challenge with LLM-as-a-judge and query-dependent evaluation rubrics, but they still rely on static evaluators that cannot adapt their standards as the solver improves, leading to insufficient and eventually saturated optimization pressure. We address this limitation with a \textbf{s}elf-evolving \textbf{co}-evolutionary training framework for deep \textbf{re}search evaluation and generation (SCORE), which tightly couples an evaluator and a solver in a shared-parameter learning process. Rather than treating generation and evaluation as isolated modules, we leverage their intrinsic connection to enable joint improvement within a single shared-parameter model. To restrict this process, we introduce a meta-harness, which dynamically controls the evaluation environment based on solver performance, encouraging valid evaluation dimensions and sufficiently deep evaluator search. Extensive experiments on deep research benchmarks demonstrate consistent improvement in report generation quality, showing that co-evolving evaluation and generation is a promising direction for training open-ended research agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型在深度研究报告生成这一开放任务中面临的核心挑战。研究背景是，虽然LLM在复杂问答任务上通过强化学习取得了显著进展，但深度报告生成与传统QA不同，它缺乏明确的真实答案（ground-truth），导致奖励信号难以客观定义。现有方法的不足主要体现在两方面：一是使用“LLM作为评判者”和查询相关的评估标准，但这些评估器是静态的，无法随着生成模型（solver）的能力提升而调整其评估标准，导致优化压力不足甚至饱和；二是报告质量评估涉及多个维度且与查询相关，单一的固定指标会忽略关键维度，无法提供细粒度的训练信号。本文要解决的核心问题是：如何设计一个可动态演进的评估-生成机制，使评估器能够与生成器协同进化，从而在缺乏可验证奖励的开放场景下持续提供有效的优化压力。为此，论文提出了SCORE框架，通过共享参数的协进化训练，让评估器和生成器在相互约束中共同提升。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1. **方法类（搜索与推理优化）**：Search-o1、Search-R1、R1-Searcher 等早期框架将显式推理引入搜索流程，提升多跳问答能力。本文基于此进一步解决开放域报告生成的评估难题。WebThinker 和 DeepResearcher 分别采用迭代 DPO 和 GRPO 等强化学习方法优化智能体，但依赖静态评估器。本文提出的 SCORE 框架通过共进化机制实现评估器与生成器的动态联合优化，突破静态评估的限制。

2. **训练策略类（自我进化与自博弈）**：AbsoluteZero、R-Zero、Search Self-play 等利用自我博弈或自我进化解决数据稀缺下的复杂推理。WebThinker、EvolveSearch 基于自生成轨迹训练求解器。本文与此类工作类似，但创新性地将评估器与生成器绑定在同一共享参数模型中，并通过元控制动态调整评估标准，区别于传统分离式训练。

3. **评估与奖励设计类**：INTUITOR、JEPO 利用模型内部信号作为奖励。STORM、Co-STORM 采用多智能体框架或人工交互生成报告。本文指出深度研究缺乏真实标注，现有方法依赖静态评估器导致饱和问题，因此提出共进化训练框架，使评估标准随求解器能力提升自适应演化。

综上，本文的核心区别在于将生成与评估视为耦合的共进化过程，通过参数共享与元控制机制，在开放域报告生成中实现了更有效的自我优化，解决了传统强化学习在缺乏可靠奖励信号时的信用分配瓶颈。

### Q3: 论文如何解决这个问题？

SCORE提出了一个自进化的协同训练框架，将评估器和求解器耦合在共享参数模型中。核心方法包含四个组件：外部证据环境、固定元控制框架、评估器和求解器。其中求解器和评估器共享同一个底层actor网络，通过功能角色分离实现联合优化。

元控制框架作为不可训练的外部控制器，根据查询和训练统计动态塑造评估空间，指定候选评估维度、结构约束和过程要求。评估器从共享actor中采样查询相关的评估维度及其权重，构建结构化评估标准。求解器基于这些标准与外部证据环境交互，收集证据并生成多个候选报告。

关键技术包括双通道奖励设计：求解器端奖励由评估器生成，包含报告有效性分数和维度加权评分的组合；评估器端奖励基于报告间一致性计算，鼓励选择能产生稳定可重复行为的评估标准。训练采用交替更新策略，两个角色共享参数，通过KL散度正则化限制策略漂移。求解器使用GRPO进行优化，评估器采用REINFORCE风格更新。

创新点在于打破了传统生成与评估分离的范式，通过共享参数使评估标准能随求解器能力提升而自适应演化。元控制框架动态调节评估环境，确保评估维度有效且搜索充分，解决了静态评估器优化压力不足的问题。

### Q4: 论文做了哪些实验？

论文在DeepResearchBench和DeepResearchEval两个基准测试上进行了实验。实验设置使用VeRL框架，采用共享参数模型，求解器每步用GRPO更新，评估器每步用REINFORCE更新，Meta-Harness（GPT-5.2）每5步调整环境。训练集来自Reddit用户查询，评估时使用网络搜索。对比方法包括标准GRPO和DPO，基础模型为Qwen2.5-7B-Instruct和Llama-3.1-8B-Instruct，并集成到open-deep-research（ReAct范式）和gpt-researcher（Plan-and-Execute范式）两个代理系统中。主要结果：在DeepResearchBench上，SCORE方法在所有维度上取得一致提升，例如在Qwen2.5+open-deep-research设置下总体得分34.43（+2.51），综合度34.86（+5.93），洞察力31.38（+3.57），引用有效性19.35（+7.59）。GRPO和DPO在某些维度出现灾难性下降，甚至降为零（如Llama-3.1+gpt-researcher的引用有效性）。消融实验表明移除任何模块都会严重降低综合度，冻结求解器导致引用有效性大幅下降。滚动数实验显示K=3时奖励改进不足，K=10时导致模型崩溃。案例分析显示自适应评估框架能针对不同查询动态引入专门评估维度。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：自进化框架中评估器和求解器共享参数可能引入耦合偏差，导致两者在错误方向上相互强化；元约束机制对探索维度的控制仍较为粗糙，难以平衡评估的充分性与稳定性；实验仅在单一模型架构上验证，跨模型泛化能力未得到充分检验。未来可从三方面深入探索：(1)设计解耦机制，在共享参数基础上引入差异化正则化项，防止协同退化；(2)开发自适应元约束策略，通过贝叶斯优化或强化学习动态调整评估维度的重要性权重；(3)引入多任务学习范式，将生成质量的客观指标（如事实一致性、引用准确性）作为辅助奖励信号与主观评价融合。此外，可探索将检索增强生成（RAG）能力纳入自进化框架，使求解器在生成过程中主动利用外部知识库进行自我纠偏，从而提升长文本报告的深度与可靠性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为SCORE的自进化协同训练框架，用于解决深度研究报告生成中的评估难题。问题在于，深度研究报告缺乏真实答案，传统的基于奖励的强化学习难以实施，而静态评估器在求解器性能提升后无法适应标准，导致优化压力不足或最终饱和。为此，论文将评估器和求解器整合进一个共享参数的模型中，通过联合生成与评估实现自我进化。同时引入元控制器机制，根据求解器表现动态调整评估环境，鼓励评估维度充分探索。实验表明，该方法能持续提升报告生成质量，在深度研究基准测试上取得显著改进，且仅需极少量训练数据。核心贡献在于揭示了评估与生成能力的正相关性，并开辟了一个有前景的自进化训练范式，推动了开放研究智能体的发展。
