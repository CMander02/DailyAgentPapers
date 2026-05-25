---
title: "Efficient Agentic Reasoning Through Self-Regulated Simulative Planning"
authors:
  - "Mingkai Deng"
  - "Jinyu Hou"
  - "Lara Sá Neves"
  - "Varad Pimpalkhute"
  - "Taylor W. Killian"
  - "Zhengzhong Liu"
  - "Eric P. Xing"
date: "2026-05-21"
arxiv_id: "2605.22138"
arxiv_url: "https://arxiv.org/abs/2605.22138"
pdf_url: "https://arxiv.org/pdf/2605.22138v1"
github_url: "https://github.com/sailing-lab/sr2am"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
  - "cs.RO"
tags:
  - "Agent架构"
  - "自我调节规划"
  - "模拟推理"
  - "LLM-as-Agent"
  - "高效推理"
  - "多系统决策"
  - "强化学习"
  - "规划频率控制"
relevance_score: 9.5
---

# Efficient Agentic Reasoning Through Self-Regulated Simulative Planning

## 原始摘要

How should an agent decide when and how to plan? A dominant approach builds agents as reactive policies with adaptive computation (e.g., chain-of-thought), trained end-to-end expecting planning to emerge implicitly. Without control over the presence, structure, or horizon of planning, these systems dramatically increase reasoning length, yielding inefficient token use without reliable accuracy gains. We argue efficient agentic reasoning benefits from decomposing decision-making into three systems: simulative reasoning (System II) grounding deliberation in future-state prediction via a world model; self-regulation (System III) deciding when and how deeply to plan via a learned configurator; and reactive execution (System I) handling fine-grained action. Simulative reasoning provides unified planning across diverse tasks without per-domain engineering, while self-regulation ensures the planner is invoked only when needed. To test this, we develop SR$^2$AM (Self-Regulated Simulative Reasoning Agentic LLM), realizing both as distinct stages within an LLM's chain-of-thought, with the LLM as world model. We explore two instantiations: recording decisions from a prompted multi-module system (v0.1) and reconstructing structured plans from traces of pretrained reasoning LLMs (v1.0), trained via supervised then reinforcement learning (RL). Across math, science, tabular analysis, and web information seeking, v0.1-8B and v1.0-30B achieve Pass@1 competitive with 120-355B and 685B-1T parameter systems respectively, while v1.0-30B uses 25.8-95.3% fewer reasoning tokens than comparable agentic LLMs. RL increases average planning horizon by 22.8% while planning frequency grows only 2.0%, showing it learns to plan further ahead rather than more often. More broadly, learned self-regulation instantiates a principle we expect to extend beyond planning to how agents govern their own learning and adaptation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前智能体推理中存在的规划效率与可控性不足的问题。研究背景是，当前主流方法（如使用大语言模型的链式思考）将智能体构建为具有自适应计算的反应式策略，通过端到端训练期望规划能力隐式涌现。然而，这种范式存在显著不足：由于缺乏对规划的触发、结构和深度的显式控制，系统会生成大量不必要的推理步骤，导致推理token消耗急剧增加，却无法保证可靠的准确率提升。更关键的是，这种无差别的链式思考无法将规划过程与自由推理、执行过程分离，使得规划行为既难以独立分析调节，也无法按需进行优化。针对这一问题，本文的核心目标是提出一种更高效的智能体推理架构，通过将决策过程分解为三个协同系统：模拟推理（System II，基于世界模型进行未来状态预测的规划）、自我调节（System III，通过学习的配置器决定何时以及多深入地规划）和反应执行（System I，处理细粒度动作），来实现对规划过程的精准调控。本文通过SR²AM系统具体实现了这一分解，旨在验证这种三系统分解相比无调节或部分调节的方案，能在交互式推理任务中取得更好的准确率与效率权衡。

### Q2: 有哪些相关研究？

作者将相关研究分为三类：1) **自适应推理控制方法**，如AdaCoT和Ton，这些工作尝试控制推理长度或选择执行模式，但仅在任务层面选择，缺乏细粒度的、动态的规划调节。本文提出的System III（自调节器）则能逐步骤决定是否规划以及规划的深度，更为精细。2) **基于世界模型的规划工作**，如Reasoning via Planning和SiRA，利用世界模型进行规划，但通常要求每步都进行模拟或使用外部规则，缺乏计算效率。本文的System II（模拟推理）将LLM本身作为世界模型，仅在System III触发时才进行模拟，实现了按需规划。3) **端到端隐式规划方法**，即当前主流的反应式策略（如CoT和VLAs），期望从数据中隐式涌现规划，但缺乏对推理结构、长度和存在性的控制，导致token效率低且准确性不可靠。本文明确将推理分解为三个系统，提供可独立分析和优化的规划结构，与这些无差别推理的方法形成对比。

### Q3: 论文如何解决这个问题？

论文通过提出**SR$^2$AM（自调节模拟推理智能体大模型）** 来解决智能体规划效率与准确性平衡的问题。核心方法是将决策过程分解为三个独立但协作的系统，并以大模型作为实现载体。

整体框架基于“三系统”架构：
1. **反应执行系统（系统I）**：处理细粒度的动作执行和即时响应，对应无需深度规划的日常操作。
2. **模拟推理系统（系统II）**：利用世界模型（此处为LLM本身）进行未来状态预测。它通过提出候选动作序列、用语言空间的世界模型模拟其后果（即“如果……那么……”的推理），并选择最大化长期目标进展的方案，生成结构化计划（包含当前信念、动作序列及预测的未来状态）。
3. **自调节系统（系统III）**：引入一个“配置器”模块，基于当前信念状态动态决策“何时”及“多深”地启用规划（即决定是创建新计划、延续旧计划还是跳过规划）。这避免了每步都进行昂贵的模拟推理，实现了计算资源的自适应分配。

关键技术包括两种实例化方法：
- **v0.1（多模块推理）**：通过提示工程将配置器、规划器、信念形成等模块作为可调用工具，记录其交互轨迹作为监督数据，证明了框架可行性。
- **v1.0（计划重构）**：从预训练推理大模型的链式思考痕迹中，用注解模型自动提取配置器决策和结构化计划内容，实现了更可扩展的数据生成，且能保留原始的自由形式推理。

训练策略分两步：先对基础LLM进行监督微调（编码模拟推理与自调节行为），再通过强化学习（基于GRPO算法）协调三系统，优化包含答案正确性、格式合规性等要素的奖励函数。实验表明，该方法在多项任务中能以极少的推理token（节省25.8%-95.3%）达到与超大参数模型相当的性能，且强化学习使模型更倾向于“规划得更远而非更频繁”。核心创新在于将规划行为从隐式涌现转变为显式、受控的模拟推理过程。

### Q4: 论文做了哪些实验？

论文在11个代表性基准上进行了评估，涵盖数学（AIME-24、AIME-25、MATH-500）、科学（GPQA-Diamond、SuperGPQA、HLE）、表格分析（FinQA、MultiHier）和网页信息检索（BrowseComp、GAIA-103、XBench-DeepSearch）。对比方法包括：参考系统（如GPT-5.4、DeepSeek-V3.2等预训练LLM，含/不含工具）、无调控推理系统（如Tongyi-DeepResearch、MiroThinker-v1.5-30B）和部分调控推理系统（如A²FM）。主要结果：SR²AM-v0.1-8B在Pass@1上达到57.0，与120-355B参数的系统竞争力相当；SR²AM-v1.0-30B达到71.3，与685B的DeepSeek-V3.2（73.2）和1T的Kimi-K2.5（70.9）竞争。在推理效率上，v1.0-30B相比可比代理LLM减少了25.8%-95.3%的推理token数（如对比MiroThinker-v1.5-30B，token数从11,295降至5,518）。消融实验表明，移除各系统（如自由推理System I、模拟规划System II、选择性规划System III）均导致性能下降或token增加。强化学习后，平均规划视界增加22.8%，但规划频率仅上升2.0%，表明RL优化了规划深度而非频率。

### Q5: 有什么可以进一步探索的点？

论文的局限在于未探讨自调节机制在更复杂多步任务中的泛化能力，如长程依赖或环境动态变化的场景，且当前系统将世界模型内置于LLM，可能限制模拟推理的准确性。未来可研究方向包括：1) 引入外部可训练的世界模型，通过对比学习或图神经网络预测状态转移，增强长期规划可靠性；2) 将自调节扩展至学习与适应过程，如控制何时触发在线微调或检索增强，形成元认知循环；3) 研究规划深度与推理成本的帕累托前沿，结合层次强化学习实现动态计算资源分配。此外，可尝试多智能体协同场景下自调节策略的分布式涌现，或利用提示工程压缩规划链式表示，减少token开销。最终目标是建立通用型自我调控框架，使AI能自主决策任务分解与计算投入的平衡。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个名为SR²AM的自调节模拟推理智能体框架，核心是将智能体决策分解为三个协同系统：反应执行（系统I）、基于世界模型的模拟规划（系统II）以及通过学习型配置器控制何时及多深进行规划的自我调节（系统III）。该方法旨在解决当前主流的端到端链式推理方法中规划结构不可控、推理效率低下的问题。论文通过两种实现路径（v0.1基于提示的多模块系统，v1.0从预训练推理模型轨迹中重构结构计划）验证了该架构。在数学、科学、表格分析和网络信息获取等任务上，8B参数的v0.1版本和30B参数的v1.0版本在Pass@1指标上分别能与120-355B和685B-1T参数的系统竞争；同时v1.0-30B节省了25.8%-95.3%的推理token。强化学习进一步使平均规划视野提升22.8%，而规划频率仅增加2.0%，表明模型学会了更前瞻而非更频繁地规划。这项研究为构建更高效、可控的智能体推理系统提供了新的设计原则。
