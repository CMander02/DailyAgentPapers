---
title: "COEVO: Co-Evolutionary Framework for Joint Functional Correctness and PPA Optimization in LLM-Based RTL Generation"
authors:
  - "Heng Ping"
  - "Peiyu Zhang"
  - "Shixuan Li"
  - "Wei Yang"
  - "Anzhe Cheng"
  - "Shukai Duan"
  - "Xiaole Zhang"
  - "Paul Bogdan"
date: "2026-04-16"
arxiv_id: "2604.15001"
arxiv_url: "https://arxiv.org/abs/2604.15001"
pdf_url: "https://arxiv.org/pdf/2604.15001v1"
categories:
  - "cs.AI"
tags:
  - "Code Agent"
  - "Multi-Agent System"
  - "Evolutionary Algorithm"
  - "Multi-Objective Optimization"
  - "Hardware Design"
  - "RTL Generation"
  - "LLM-based Code Generation"
  - "Functional Correctness"
  - "PPA Optimization"
relevance_score: 7.5
---

# COEVO: Co-Evolutionary Framework for Joint Functional Correctness and PPA Optimization in LLM-Based RTL Generation

## 原始摘要

LLM-based RTL code generation methods increasingly target both functional correctness and PPA quality, yet existing approaches universally decouple the two objectives, optimizing PPA only after correctness is fully achieved. Whether through sequential multi-agent pipelines, evolutionary search with binary correctness gates, or hierarchical reward dependencies, partially correct but architecturally promising candidates are systematically discarded. Moreover, existing methods reduce the multi-objective PPA space to a single scalar fitness, obscuring the trade-offs among area, delay, and power. To address these limitations, we propose COEVO, a co-evolutionary framework that unifies correctness and PPA optimization within a single evolutionary loop. COEVO formulates correctness as a continuous co-optimization dimension alongside area, delay, and power, enabled by an enhanced testbench that provides fine-grained scoring and detailed diagnostic feedback. An adaptive correctness gate with annealing allows PPA-promising but partially correct candidates to guide the search toward jointly optimal solutions. To preserve the full PPA trade-off structure, COEVO employs four-dimensional Pareto-based non-dominated sorting with configurable intra-level sorting, replacing scalar fitness without manual weight tuning. Evaluated on VerilogEval 2.0 and RTLLM 2.0, COEVO achieves 97.5\% and 94.5\% Pass@1 with GPT-5.4-mini, surpassing all agentic baselines across four LLM backbones, while attaining the best PPA on 43 out of 49 synthesizable RTLLM designs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的寄存器传输级（RTL）代码生成中，如何**联合优化功能正确性与功耗、性能、面积（PPA）质量**的核心问题。

**研究背景**：随着芯片设计复杂度提升，自动化RTL生成成为关键。LLM在此领域展现出潜力，现有研究主要通过领域微调、强化学习或多智能体框架来提升生成代码的功能正确性。然而，仅功能正确不足以满足实际部署需求，LLM生成的RTL在PPA指标上往往逊于工程师手写设计。因此，在从自然语言规约生成RTL的过程中，同时优化功能正确性和PPA质量成为一个重要研究方向。

**现有方法的不足**：当前方法普遍存在两个根本性局限。首先，它们将正确性与PPA优化**解耦**处理。无论是多智能体流水线、带有二元正确性门控的进化搜索，还是分层奖励依赖的方法，都只在完全确保功能正确后才开始优化PPA。这导致所有部分正确但可能在架构上极具潜力的候选设计被系统性地丢弃，失去了它们作为通往最终优质解决方案的“垫脚石”作用。其次，现有方法通常将多目标的PPA空间（面积、延迟、功耗）**简化为一个单一的标量适应度值**（例如通过加权求和），这掩盖了PPA指标之间的权衡关系，并且需要手动调整权重，无法保证帕累托最优性。

**本文要解决的核心问题**：针对上述不足，论文提出了COEVO框架，其核心目标是**在一个统一的进化循环中，协同优化功能正确性与PPA**。具体而言，它需要解决：1）如何将功能正确性从二元前提条件转变为可与PPA指标**连续协同优化的维度**，从而允许部分正确的、PPA表现优异的候选设计引导搜索过程；2）如何在不进行手动权重调整的情况下，**完整保留并优化PPA多目标之间的权衡结构**，避免将其压缩为单一标量。通过引入增强的测试平台、自适应正确性门控以及基于四维帕累托的非支配排序机制，COEVO旨在同时追求功能正确性的最大化与PPA指标的最小化，实现真正意义上的联合优化。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三大类：方法类、应用类和评测类，它们共同构成了LLM-based RTL生成的研究背景。

在**方法类**工作中，主要分为三类。第一类是**领域微调与强化学习**方法，如RTLCoder、BetterV等通过微调提升功能正确性，VeriRL、VeriReason等则融入编译器反馈进行强化学习。第二类是**智能体框架**，如MAGE、VeriMoA等通过角色分解或多智能体协作生成正确代码，但均未系统优化PPA（性能、功耗、面积）。第三类是**进化计算方法**，如FunSearch、EoH等将LLM与进化算法结合进行代码优化；在RTL领域，REvolution、EvolVE等进化方法虽引入种群迭代，但仍将正确性与PPA解耦优化。

在**应用类**工作中，聚焦于**PPA优化**。部分研究（如RTLRewriter、POET）在已有正确RTL基础上进行PPA重写或进化，不涉及从规范生成RTL。而在**spec-to-RTL生成**中，Prompt for Power等方法通过上下文学习注入PPA知识；VeriOpt、VeriAgent等多智能体框架将正确性与PPA任务分配给独立智能体；ChipSeek-R1则将分层PPA奖励融入强化学习。这些方法普遍将多目标PPA简化为单一标量适应度（如加权和、面积延时积），且严格区分正确性与PPA优化阶段，常丢弃部分正确但有架构潜力的候选设计。

本文提出的COEVO框架与上述工作密切相关但存在关键区别。它属于进化计算方法范畴，但**统一了正确性与PPA的协同进化**，将正确性作为连续的第四维度与PPA共同纳入帕累托优化，避免了现有方法（包括进化类方法如REvolution）的解耦局限。同时，它采用**四维非支配排序**替代手动加权标量适应度，完整保留了PPA权衡结构。相较于仅优化PPA的应用类工作（如POET），COEVO直接面向spec-to-RTL生成，实现了正确性与PPA的联合搜索。

### Q3: 论文如何解决这个问题？

COEVO通过一个协同进化框架，将功能正确性和PPA（面积、延迟、功耗）优化统一在单一的进化循环中，解决了现有方法将两者解耦、过早丢弃部分正确但有架构潜力的候选方案，以及将多目标PPA空间简化为单一标量适应度的问题。

其核心架构是一个多代进化过程，每代包含三个主要阶段：1）**子代生成**：基于当前种群，通过LLM驱动的进化算子产生新候选设计；2）**设计评估**：通过仿真评估功能正确性，通过逻辑综合评估PPA指标；3）**生存者选择**：结合父代和子代，通过基于帕累托的选择机制筛选出下一代种群。

关键技术包括：
1.  **连续化正确性度量与增强测试平台**：将功能正确性从二元判断转化为连续分数（通过测试用例比例计算），并利用LLM生成包含边界条件和典型操作的增强测试平台，提供细粒度评分和详细的诊断反馈（如失败用例的预期与实际信号值），为进化提供指导。
2.  **七类LLM驱动的进化算子**：这些算子嵌入领域知识，分为三类：面向正确性的算子（如修复错误、简化设计）、面向PPA的算子（如优化、重构、探索新架构）以及联合正确性-PPA的算子（如PPA感知的错误修复、架构融合）。算子通过基于上置信界（UCB）的自适应机制进行选择，以平衡探索与利用。
3.  **自适应正确性门控与退火机制**：设置一个随时间逐渐提高的正确性阈值。早期允许部分正确但有PPA潜力的候选生存，以保留其有益的架构特征；后期则逐步提高阈值，引导种群趋向完全正确。这避免了硬性二元门控导致的信息丢失。
4.  **四维帕累托非支配排序与可配置层内排序**：在生存者选择中，将每个候选视为在四个维度（正确性、面积、延迟、功耗）上的解，进行非支配排序，得到帕累托前沿及后续层级。这保留了多目标间的权衡关系，无需手动设置权重将其压缩为标量。层内可根据优化偏好（如优先正确性或特定PPA指标）进行次级排序，实现可配置的优化导向。

整体上，COEVO的创新在于将正确性与PPA作为协同进化的连续维度，通过自适应门控和帕累托排序在统一框架内处理多目标优化，使得部分正确的有潜力设计能持续贡献于搜索过程，从而联合逼近功能正确且PPA更优的最终设计。

### Q4: 论文做了哪些实验？

论文在VerilogEval 2.0（156个任务）和RTLLM 2.0（50个任务）两个标准基准上进行了全面实验，旨在回答四个研究问题。实验使用了包括GPT-4o-mini、GPT-4.1-mini、GPT-5-mini、GPT-5.4-mini以及Qwen2.5-Coder-7B在内的多个LLM骨干模型。

在功能正确性（RQ1）方面，COEVO与两类基线方法进行了对比：智能体方法（如I/O prompting、VeriOpt、VeriAgent、VerilogCoder、VeriMoA、REvolution、EvolVE）和基于训练的方法。主要结果显示，COEVO在功能正确性上显著超越了所有基线。关键指标Pass@1在VerilogEval 2.0上达到97.5%，在RTLLM 2.0上达到94.5%（使用GPT-5.4-mini），在所有测试的LLM骨干模型上都优于现有智能体方法。

在PPA优化（RQ2）方面，论文在RTLLM 2.0中可综合的设计上进行了评估。COEVO在49个可综合设计中的43个上取得了最佳的PPA（面积、功耗、延迟）结果，证明了其在多目标优化上的有效性。

此外，论文通过消融实验（RQ3）分析了核心组件（如连续正确性优化、自适应门控、四维帕累托排序）的贡献，并通过可视化多代进化过程（RQ4）展示了COEVO如何协同优化正确性与PPA。

### Q5: 有什么可以进一步探索的点？

本文提出的COEVO框架在联合优化功能正确性与PPA方面取得了显著进展，但其仍存在一些局限性和值得深入探索的方向。首先，框架依赖于LLM生成初始RTL代码的质量，若初始种群多样性不足或质量较差，可能影响进化搜索的效率与最终结果。其次，虽然采用了四维帕累托排序，但在高维目标空间中，非支配解的数量可能爆炸式增长，如何有效维护与选择种群仍需更高效的机制。此外，当前方法主要针对中小规模设计，对于超大规模或高度复杂的电路，进化搜索的计算开销与可扩展性面临挑战。

未来研究可从以下几方面展开：一是探索更智能的初始种群生成策略，例如结合强化学习预训练LLM，使其能产生更具PPA潜力的代码变体。二是研究动态目标空间降维技术，在保持权衡信息的同时降低算法复杂度。三是将框架扩展至系统级设计，考虑跨模块优化与接口约束。最后，可探索异构进化策略，针对不同电路特性自适应调整搜索参数，进一步提升优化效率与泛化能力。

### Q6: 总结一下论文的主要内容

本文提出COEVO框架，旨在解决基于LLM的RTL生成中功能正确性与PPA（面积、延迟、功耗）质量联合优化的难题。现有方法普遍将二者解耦，仅在确保功能正确后才优化PPA，导致部分正确但架构优良的设计被丢弃，且将多目标PPA优化简化为单一标量，掩盖了权衡关系。COEVO的核心贡献在于将正确性作为与面积、延迟、功耗并列的连续优化维度，通过增强的测试平台提供细粒度评分和诊断反馈，并采用自适应正确性门控和退火机制，允许部分正确的候选设计引导搜索。同时，框架引入基于四维帕累托的非支配排序与可配置的层内排序方法，替代需手动调权的标量适应度，从而保留完整的PPA权衡结构。实验表明，COEVO在VerilogEval 2.0和RTLLM 2.0基准上取得了当前最优的功能正确率（如GPT-5.4-mini达到97.5%和94.5% Pass@1），并在多数可综合设计中实现了最佳PPA，验证了其统一协同进化方法的有效性。
