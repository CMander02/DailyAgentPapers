---
title: "Hierarchical Reinforcement Learning with Augmented Step-Level Transitions for LLM Agents"
authors:
  - "Shuai Zhen"
  - "Yanhua Yu"
  - "Ruopei Guo"
  - "Nan Cheng"
  - "Yang Deng"
date: "2026-04-07"
arxiv_id: "2604.05808"
arxiv_url: "https://arxiv.org/abs/2604.05808"
pdf_url: "https://arxiv.org/pdf/2604.05808v1"
github_url: "https://github.com/TonyStark042/STEP-HRL"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "强化学习"
  - "分层强化学习"
  - "LLM Agent"
  - "决策制定"
  - "任务分解"
  - "记忆管理"
  - "计算效率"
  - "基准测试"
relevance_score: 8.5
---

# Hierarchical Reinforcement Learning with Augmented Step-Level Transitions for LLM Agents

## 原始摘要

Large language model (LLM) agents have demonstrated strong capabilities in complex interactive decision-making tasks. However, existing LLM agents typically rely on increasingly long interaction histories, resulting in high computational cost and limited scalability. In this paper, we propose STEP-HRL, a hierarchical reinforcement learning (HRL) framework that enables step-level learning by conditioning only on single-step transitions rather than full interaction histories. STEP-HRL structures tasks hierarchically, using completed subtasks to represent global progress of overall task. By introducing a local progress module, it also iteratively and selectively summarizes interaction history within each subtask to produce a compact summary of local progress. Together, these components yield augmented step-level transitions for both high-level and low-level policies. Experimental results on ScienceWorld and ALFWorld benchmarks consistently demonstrate that STEP-HRL substantially outperforms baselines in terms of performance and generalization while reducing token usage. Our code is available at https://github.com/TonyStark042/STEP-HRL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在复杂顺序决策任务中，因依赖不断增长的完整交互历史而导致的效率低下和可扩展性受限问题。研究背景是，LLM作为自主智能体在交互环境中展现出强大的推理与规划能力，强化学习（RL）被引入以通过环境交互和奖励反馈来优化策略。然而，现有大多数基于RL的LLM智能体采用“历史条件化”的范式，即策略的输入是过去所有观察和动作构成的冗长序列。这种设计源于将决策视为序列预测的建模视角，虽有助于部分可观测环境中的状态推断，但存在根本性不足：注意力机制的计算成本随上下文长度呈二次方增长；未经筛选的历史会积累冗余或无关信息，可能掩盖关键决策信号并降低推理质量；这本质上是一种建模选择而非强化学习的必然要求。

现有方法主要通过压缩交互历史或改进长期信用分配来缓解症状，但并未挑战“策略必须条件化于完整历史”这一核心假设。分层强化学习（HRL）虽引入了时间抽象，有望分解长程任务，但现有HRL方法中高层和底层策略仍依赖于累积的交互历史，未能从根本上摆脱长上下文的依赖。

因此，本文的核心问题是：如何重新设计LLM智能体的强化学习框架，使其摆脱对冗长交互历史的依赖，实现更高效、可扩展的步级（step-level）决策。为此，论文提出了STEP-HRL框架，其核心思想是从“进度”视角重构长程决策：利用已完成的高层子任务表示全局进度，并引入一个本地进度模块，在子任务内部迭代地选择性总结交互历史，形成简洁的本地进度表示。这使得底层策略仅需基于当前子任务、观察和提炼后的本地进度做决策，实现恒定大小的输入；高层策略也基于增强的步级转移进行学习。该方法旨在显著降低计算开销（token使用量），同时提升任务性能和泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两类：LLM智能体与强化学习在LLM智能体中的应用。

在**LLM智能体**方面，早期研究主要采用基于提示的方法，如Chain-of-Thought、ReAct和Reflexion，通过生成推理轨迹来支持多步决策。后续工作则通过引入工具使用、记忆机制和多智能体协调等系统组件来增强智能体。另一类工作侧重于通过行为克隆等微调方法从专家示范中学习，但其严重依赖高质量专家数据，且在长视野任务中因探索有限和分布偏移而性能下降。本文提出的STEP-HRL框架属于架构增强范畴，但通过分层结构和局部进展总结，旨在克服长历史依赖问题。

在**强化学习在LLM智能体中的应用**方面，先前工作主要采用基于交互的流程，使用PPO等算法进行微调，或通过偏好优化（如DPO）进行更新。为了获得更细粒度的学习信号，有研究将RL目标分解以提供动作级反馈，或分层估计步级优势。然而，这些方法大多依赖完整的交互历史进行决策，导致信用分配困难和计算成本高。尽管已有工作探索了分层强化学习（HRL）框架（如EPO和GLIDER）来分解复杂任务，但它们仍依赖于历史条件策略。本文的STEP-HRL与这些HRL方法相关，但关键区别在于它通过引入局部进展模块，仅基于单步转移（而非完整历史）进行步级学习，从而实现了更高效的信用分配和显著降低的计算开销。

### Q3: 论文如何解决这个问题？

论文通过提出STEP-HRL这一分层强化学习框架来解决LLM智能体因依赖完整交互历史而导致的效率低下和可扩展性受限问题。其核心方法是构建一个层次化任务结构，并引入“局部进展”模块来压缩历史信息，从而在策略决策时仅依赖于单步转移而非冗长历史。

整体框架包含三个主要策略模块：高层策略、低层策略和局部进展策略，它们共享参数但配备独立的评论家网络进行离线训练。高层策略负责根据任务指令、已完成子任务序列、上一个子任务的最终局部进展以及下一个子任务的初始观察，来生成下一个子任务。低层策略则负责在给定当前子任务、当前观察和由局部进展策略生成的紧凑局部进展摘要的条件下，生成具体的原子动作。局部进展策略是该方法的关键创新点，它迭代地、选择性地总结每个子任务内的交互历史。具体而言，在子任务执行过程中，该策略基于上一个局部进展状态、当前子任务描述、上一步执行的动作及其产生的观察，生成更新后的局部进展状态。这个进展状态动态地编码了与子任务相关的局部历史信息。

通过这种设计，低层策略的决策可以基于增强的单步转移（包含观察、局部进展、动作、内在奖励、下一观察和下一进展），而无需依赖完整的子任务内历史。同时，当子任务完成时，其最终的局部进展状态会被传递给高层策略，作为子任务执行细节的摘要，从而也实现了高层决策的单步化。这种机制将原本需要长序列历史作为条件的决策问题，转化为基于紧凑状态表示的单步决策问题。

在训练方面，方法首先利用专家演示数据通过行为克隆对三个策略进行初始化。随后，结合收集的离线数据，采用基于隐式价值学习的演员-评论家框架进行优化。评论家网络在话语级别（基于最后一个令牌的隐藏状态）估计状态价值和动作价值函数，并利用期望回归和优势加权回归目标来隐式地提升策略，避免了在动作空间上的显式最大化，从而实现了稳定高效的离线强化学习。这种参数高效的设计促进了不同决策层级间的知识迁移，并显著降低了计算开销。

### Q4: 论文做了哪些实验？

论文在ScienceWorld和ALFWorld两个基准上进行了实验评估。实验设置方面，使用Mistral-7B、Gemma-7B和Llama3-8B作为骨干模型，并采用LoRA进行微调。训练分为行为克隆（5轮，学习率1e-4）和离线强化学习（3轮，actor学习率1e-5，critic学习率1e-4）两个阶段，使用AdamW优化器，在8张A100 GPU上运行。

对比方法包括：基于提示的ReAct、Reflexion、SwiftSage，以及基于微调的ETO、WKM和GLIDER。主要结果如下：在ScienceWorld上，STEP-HRL在Mistral-7B上对已见和未见任务的成功率分别达到80.28%和75.21%，相比最佳基线GLIDER（67.31%和65.14%）绝对提升约13-19个百分点，相对提升15.46%-19.27%。在ALFWorld上，STEP-HRL在Mistral-7B上取得96.43%（已见）和97.01%（未见）的成功率，相比最佳基线WKM（73.57%和76.87%）绝对提升超过20个百分点，相对提升26.20%-31.07%。其他骨干模型上也观察到类似优势。

此外，消融实验表明，移除局部进度模块（w/o LP）、分层结构（w/o Hier）或离线RL阶段（w/o RL）均会导致性能显著下降。效率分析显示，STEP-HRL实现了近似恒定的每步token使用量，显著低于标准RL和HRL方法，降低了计算成本。敏感性分析则验证了离线RL中超参数（如优势温度β=0.95）和数据混合策略（专家与BC轨迹1:2混合）的有效性。

### Q5: 有什么可以进一步探索的点？

STEP-HRL的局限性主要在于对高质量专家演示的依赖，以及子任务终止预测的潜在不准确性。这为未来研究提供了几个清晰的探索方向。

首先，可以探索如何减少对专家数据的依赖。一个方向是结合自监督或弱监督学习，例如利用环境的内在奖励或任务完成度的稀疏信号来自动推断子任务结构和进度。另一个方向是开发更鲁棒的子任务边界发现算法，或许可以结合LLM自身的世界知识进行零样本或少样本的划分。

其次，子任务终止机制有明确的改进空间。可以将终止预测与原始动作解耦，设计一个独立的、基于更丰富上下文（如当前状态与子任务目标的匹配度）的终止判断模块。这有助于减少错误终止，提升高层与底层策略的对齐。

此外，论文展示了在结构化环境中的有效性，但其在开放域、动态变化环境中的泛化能力仍是未知数。未来可以探索将STEP-HRL与更强大的世界模型或在线学习机制结合，使智能体能在与环境的持续交互中动态调整其层次结构和进度评估，从而迈向更自主、更通用的层次强化学习。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型（LLM）智能体在复杂交互决策任务中依赖冗长交互历史、导致计算成本高和可扩展性受限的问题，提出了STEP-HRL框架。其核心贡献是引入一种分层强化学习（HRL）方法，通过增强的步级转移实现高效学习，避免使用完整历史记录。方法上，STEP-HRL将任务层次化分解，利用完成的子任务表示全局进度，并创新性地设计了局部进度模块，迭代总结每个子任务内的交互历史，生成紧凑的局部进度摘要。这使得高层和低层策略都能基于增强的步级状态表示进行决策。实验在ScienceWorld和ALFWorld基准测试中表明，STEP-HRL在性能和泛化能力上显著优于基线方法，同时大幅降低了令牌使用量。该研究为LLM智能体提供了一种实用且可扩展的训练途径，通过结构化的进度摘要实现步级抽象，有望提升未来LLM智能体的效率与鲁棒性。
