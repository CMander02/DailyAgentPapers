---
title: "APPO: Agentic Procedural Policy Optimization"
authors:
  - "Xucong Wang"
  - "Ziyu Ma"
  - "Yong Wang"
  - "Yuxiang Ji"
  - "Shidong Yang"
  - "Guanhua Chen"
  - "Pengkun Wang"
  - "Xiangxiang Chu"
date: "2026-06-10"
arxiv_id: "2606.12384"
arxiv_url: "https://arxiv.org/abs/2606.12384"
pdf_url: "https://arxiv.org/pdf/2606.12384v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agentic RL"
  - "Credit Assignment"
  - "Multi-turn Tool Use"
  - "LLM Agent Training"
  - "Branching Policy Optimization"
  - "Fine-grained Decision Points"
relevance_score: 9.5
---

# APPO: Agentic Procedural Policy Optimization

## 原始摘要

Recent advances in agentic Reinforcement Learning (RL) have substantially improved the multi-turn tool-use capabilities of large language model agents. However, most existing methods assign credit over coarse heuristic units, such as tool-call boundaries or fixed workflows, making it difficult to identify which intermediate decisions influence downstream outcomes. In this work, we study agentic RL from two perspectives: \textit{where to branch and how to assign credit after branching}. Our pilot analysis shows that influential decision points are broadly distributed throughout the generated sequence rather than concentrated at tool calls, while token entropy alone does not reliably reflect their impact on final outcomes. Motivated by these observations, we propose \textbf{Agentic Procedural Policy Optimization (APPO)}, which shifts branching and credit assignment from coarse interaction units to fine-grained decision points in the sequence. APPO selects branching locations using a Branching Score that combines token uncertainty with policy-induced likelihood gains of subsequent continuations, enabling more targeted exploration while filtering out spurious high-entropy positions. It further introduces procedure-level advantage scaling to better distribute credit across branched rollouts. Experiments on 13 benchmarks show that APPO consistently improves strong agentic RL baselines by nearly 4 points, while keeping efficient tool-calls and maintaining behavior interpretability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI Agent在多轮工具使用中的强化学习过程中，信用分配（credit assignment）粒度太粗的问题。现有方法大多基于工具调用边界或固定工作流等粗略的启发式单元进行信用分配，这导致难以识别哪些中间决策真正影响了最终结果。虽然有些工作通过从中途分支（branching）探索来提高采样效率，但它们的分支单位仍然是粗粒度的，忽略了思考过程中程序性知识的重要性。

论文的初步分析发现，具有影响力的决策点广泛分布在生成的整个序列中，而非集中在工具调用处，而且仅凭令牌熵（token entropy）无法可靠地反映这些决策点对最终结果的影响。因此，本文的核心问题是：如何设计一种更细粒度的信用分配机制，能够有效识别并利用思考过程中的程序性决策点，从而实现更高效、更精准的策略优化。为此，论文提出了APPO，将分支和信用分配从粗粒度的交互单元转移到序列中的细粒度决策点。

### Q2: 有哪些相关研究？

本文的相关研究可分为以下几类：

1. **方法类（Agentic RL基础方法）**：如PPO、GRPO、DAPO、GSPO等，这些工作改进了策略梯度、优势函数或正则化项。本文APPO在此基础上关注更细粒度的信用分配，而非粗粒度的工具调用边界。

2. **树状RL方法**：又分为三子类——  
   - **离线训练**：如MCTS-DPO、SPORT，利用分支节点构建偏好数据。  
   - **在线训练**：如Tree-GRPO随机选择分支节点，ARPO识别工具调用后的高熵token进行重采样。  
   - **测试时扩展**：通过多分支提升推理性能。  
   与这些工作不同，APPO提出基于“过程（procedure）”的细粒度分支，即用自定义分支分数（Branching Score）综合token不确定性和策略似然增益来选择分支位置，而非仅依赖高熵或工具调用。

3. **应用类**：聚焦智能体技能内化与自我进化。APPO通过过程级优势缩放（Procedure-level Advantage Scaling）在分支轨迹中更精确地分配信用，提升了工具使用效率与行为可解释性。

核心区别：现有方法多在粗粒度单元（如工具调用步）处分支和分配信用，而APPO在序列中的细粒度决策点进行操作，并通过分支分数与过程级优势实现更精准的探索与信用分配。

### Q3: 论文如何解决这个问题？

APPO的核心方法是将强化学习中的分支与信用分配从粗粒度的工具调用边界转移到细粒度的序列决策点。整体框架包括三个主要阶段：初始化、采样分支和终止。

首先，在初始化阶段，模型为每个任务生成N个完整轨迹作为树的根节点。然后在采样阶段，APPO引入创新的分支评分（Branching Score, BS）来识别关键决策点。BS结合两个因素：一是token熵，衡量局部不确定性；二是未来价值（future value），通过累积衰减的重要性采样比率（Ω）计算，反映当前token对未来结果的影响程度。BS通过标准化后相乘得到，选取每条轨迹中评分最高的B个token作为分支点。在这些点上重新采样后续内容，生成新的分支轨迹，形成树状结构。终止条件为预算耗尽或不进行新分支。

该方法的创新点包括：1) 用分支评分替代纯熵值选择分支点，过滤掉不相关的词法不确定性；2) 采用双组优势估计（初始轨迹和分支轨迹分别计算），避免策略混合带来的偏差；3) 引入未来感知优势项（future-aware advantage），通过Ω值对下游影响更大的决策赋予更高信用，组合成最终优势值。APPO还从理论上证明了该方法能降低梯度方差并提供策略改进保证。

### Q4: 论文做了哪些实验？

论文在13个基准上进行了全面实验，涵盖三大类任务：（1）数学推理（GSM8K、MATH、AIME24/25、MATH500）；（2）知识密集型推理（HotpotQA、2WikiMultihopQA、Musique、Bamboogle、WebWalker）；（3）深度搜索（GAIA、Humanity's Last Exam、Xbench）。对比方法包括四种：Vanilla RL（GRPO、Reinforce++等）、Agentic RL（GIGPO、ARPO）、LLM基座（Llama3.1-8B、Qwen2.5、GPT-4o等）以及搜索智能体（Search-o1、WebThinker）。主要结果：APPO在数学推理上平均超越最佳Agentic RL基线2.45个百分点；在GAIA上Qwen3-8B/14B分别达到42.7和46.6；在五个问答数据集上平均达58.1（Llama3.1-8B）和58.1（Qwen2.5-7B）。消融实验表明，用熵替换分支分数（BS）导致平均下降0.9-1.7分，去除未来优势估计（Âᶠᵘᵗ）下降更显著（Qwen2.5下降3.4分）。Pass@K分析显示APPO在Pass@5上的优势进一步扩大（如GAIA从46.1到64.0）。训练动态表明APPO达到更高终奖励且训练更稳定。

### Q5: 有什么可以进一步探索的点？

APPO的核心局限在于分支评分函数仍依赖策略诱导的似然增益，这本质上是一种启发式度量，可能无法捕捉到那些通过策略平滑变化但实际影响下游的决策点。未来可探索基于因果效应或反事实推理的细粒度分支定位，例如通过局部干预实验明确哪些token的扰动会显著改变终端奖励。另一个方向是跨序列的信用分配：当前方法仅在单次分支的rollout内缩放优势，忽略了不同轨迹间共享决策路径的补偿机制，可引入全局价值函数蒸馏或层级化元学习器来动态调整分支时机。此外，APPO在涉及长期依赖的真实工具调用场景（如代码执行链）中，其分支粒度可能导致策略方差爆炸，因此需研究基于图神经网络的分层信用模型，将过程奖励与终端奖励解耦。最后，结合在线蒸馏的自适应分支阈值（根据任务复杂度自动调节灵敏度）也是提升泛化性的关键。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为APPO（Agentic Procedural Policy Optimization）的新方法，旨在改进大型语言模型智能体的多轮工具使用能力。现有智能体强化学习方法通常基于粗粒度的交互单元，如工具调用边界或固定工作流，进行信用分配，导致难以识别影响下游结果的关键中间决策。APPO从“在哪里分支”和“分支后如何分配信用”两个角度重新审视智能体强化学习，将分支和信用分配从粗粒度交互单元转移到序列中的细粒度决策点。具体而言，APPO使用结合令牌不确定性与后续延续的策略诱导似然增益的分支分数来选择分支位置，从而实现更有针对性的探索；并引入过程级优势缩放来更好地在分支轨迹间分配信用。在13个基准测试上的实验表明，APPO在保持工具调用效率和可解释性的同时，将强智能体强化学习基准的性能平均提升了近4个百分点。
