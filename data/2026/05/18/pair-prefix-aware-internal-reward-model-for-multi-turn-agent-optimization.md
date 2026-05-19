---
title: "PAIR: Prefix-Aware Internal Reward Model for Multi-Turn Agent Optimization"
authors:
  - "Wonjoong Kim"
  - "Yeonjun In"
  - "Sangwu Park"
  - "Dongha Lee"
  - "Chanyoung Park"
date: "2026-05-18"
arxiv_id: "2605.17877"
arxiv_url: "https://arxiv.org/abs/2605.17877"
pdf_url: "https://arxiv.org/pdf/2605.17877v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "多轮交互优化"
  - "奖励模型"
  - "GRPO"
  - "隐状态探测"
  - "信用分配"
  - "内部奖励信号"
relevance_score: 8.5
---

# PAIR: Prefix-Aware Internal Reward Model for Multi-Turn Agent Optimization

## 原始摘要

A significant hurdle for current LLMs is the execution of complex, multi-stage tasks. Group Relative Policy Optimization (GRPO) has been emerging as a leading choice, but its reliance on sparse outcome rewards severely limits credit assignment across intermediate steps. Existing remedies such as running full rollouts to assign step-level advantages, calling external LLM judges at each step, or computing intrinsic rewards that require ground-truth answers at every evaluation introduce significant costs or practical constraints. We hypothesize that internal correctness probing over LLM hidden states can be repurposed as a step-level reward signal, potentially addressing all of these limitations at once. However, existing probing research assumes clean inputs, and we first show that this assumption breaks down in multi-step settings: hidden-state probes degrade severely under prefix contamination tracking coherence with the (possibly corrupted) prefix rather than grounded correctness, while attention-based features remain robust to contamination but underperform on clean prefixes. Building on this complementary relationship, we propose the Prefix-Aware Internal Reward (PAIR), a two-stage model with a frozen hidden-state probe estimating belief-consistency and a lightweight attention-based head correcting it toward grounded correctness. Experimental results show that PAIR achieves the highest AUROC on contaminated trajectories while operating at negligible inference cost, enabling dense step-level reward signals for GRPO training without external model calls, ground-truth dependencies, or full-trajectory rollouts.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决在复杂多步骤智能体任务中，使用GRPO进行强化学习训练时面临的稀疏奖励和信用分配难题。研究背景是，当前LLM在执行多步推理或工具调用等任务时，GRPO因其高效性被广泛采用，但其依赖的最终结果奖励（稀疏奖励）无法有效区分中间步骤的贡献，导致训练收敛慢、样本效率低。现有改进方法各有缺陷：运行完整轨迹再反向传播奖励会浪费大量计算资源；每步调用外部LLM作为裁判成本高且延迟大；利用模型自身log-probability作为奖励则需要在线访问真实答案，不实用；外部奖励模型（如PRM）需要额外训练和维护。论文提出的核心问题是：能否仅利用LLM自身的内部状态（隐藏状态和注意力模式），在不依赖全轨迹回滚、外部模型调用或真实答案的前提下，为每一步提供密集的奖励信号？作者发现，在多步设置下，直接应用现有内部探针会遭遇“前缀污染”问题：模型在推理中产生的错误前缀会污染后续步骤的隐藏状态，使探针失效。因此，论文旨在设计一种鲁棒的方法，利用内部表示来提供可靠的、密集的逐步奖励，以优化多步智能体的GRPO训练。

### Q2: 有哪些相关研究？

相关研究可以分为以下几类：

1. **方法类**：本文基于Group Relative Policy Optimization (GRPO)，解决了其在多轮智能体环境中稀疏结果奖励导致的信用分配问题。与现有方法如Process Reward Models (PRMs)相比，PRMs为中间推理步骤提供监督，但在智能体环境中步骤正确性依赖上下文且不易验证，而本文从LLM内部表示直接推导步骤级奖励，无需外部模型调用或真实答案依赖。Tree-based Rewards (如AT²PO、Tree-GRPO)通过树搜索和兄弟轨迹比较获得步骤级优势，但计算成本高，本文则避免了全轨迹展开。

2. **评测类**：LLM-as-a-Judge方法（如MT-PPO）使用外部LLM评估每轮质量，但带来API成本和推理延迟，本文通过内部奖励模型消除了这些开销。Intrinsic and External Rewards (如AgentPRM、SWEET-RL)依赖外部奖励模型，而IGPO、TIPS利用真实答案的对数概率作为奖励，但对真实轨迹有依赖，本文则实现了运行时无真实答案依赖。

3. **内部探测类**：现有工作如CoE、注意头熵和Lookback分析证明内部表示可预测模型正确性，但仅在清洁前缀和单轮设置下验证。本文发现了多轮场景下前缀污染导致内部探测失效的关键问题，并提出PAIR模型，结合对污染鲁棒但清洁前缀表现不佳的注意力特征与相反特点的隐藏状态探测，实现自适应组合，提供可靠的步骤级奖励信号。

### Q3: 论文如何解决这个问题？

PAIR（Prefix-Aware Internal Reward Model）通过一个两阶段架构解决多轮智能体优化中奖励信号稀疏和信用分配问题。核心思想是解耦“信念一致性”（与历史前缀的连贯性）和“基础正确性”（实际任务进展），利用隐藏状态探针对清洁前缀效果好但受污染后崩溃、注意力特征对污染鲁棒但清洁时较弱这一互补关系。

整体框架包含两个主要模块：第一阶段是信念一致性估计器，使用冻结的线性逻辑回归探针从最后一层隐藏状态中提取特征，输出分数s_bc，该探针仅在清洁数据上训练，擅长评估与历史连贯的正确步骤。第二阶段是注意力校正头，使用另一个逻辑回归模型，输入注意力特征（包含每个注意力头的峰值、标准差、前缀及本步注意力比率）与第一阶段分数s_bc的拼接，输出最终正确性分数s_final。该校正头在清洁和受污染轨迹的混合数据上训练，学习保留清洁前缀下的s_bc，同时利用注意力特征对受污染前缀下分离的情况进行修正。

关键技术在于两阶段设计的结构：第一阶段保持隐藏状态探针在清洁轨迹上的优势，第二阶段利用注意力特征的污染鲁棒性纠正偏差，避免简单特征拼接导致信号抵消。整个系统无需外部模型调用或真实标签，在推理时仅需一次前向传播，成本极低，可为GRPO提供密集的步骤级奖励信号。

### Q4: 论文做了哪些实验？

论文在GTA（229个样本，2-8轮多步工具组合）和ToolBench（1000个样本，最少3轮，涵盖16000+API）两个多步智能体基准上进行了实验。使用Qwen2.5-7B-Instruct作为策略模型，PAIR从同一模型提取内部表示。对比方法包括五类：仅结果奖励（标准GRPO）、外部奖励（LLM Judge用GPT-4o-mini每步打分）、基于树的（AT²PO和Tree-GRPO）、内部探针（Last-Token、Mean-Pooled、Multi-Layer等隐藏状态探针及Attention、Hidden+Attn等注意力探针，以及Lookback Ratio等无监督方法）和内在奖励（IGPO和TIPS）。主要结果以成功率衡量，PAIR在两个数据集上均取得最佳：GTA上0.2489±0.042，ToolBench上0.4498±0.025；第二好的LLM-as-a-judge分别为0.2387和0.4203。消融实验显示，PAIR在受污染轨迹上的AUROC最高；动量奖励相比直接使用探针分数在GTA和ToolBench上分别提升约8%（0.230→0.2489，0.415→0.4498）。PAIR是唯一无需外部模型调用、完整轨迹回滚或真实答案即可获得密集步级奖励的方法。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于PAIR假设prefix污染主要源于历史错误，未考虑更复杂的场景如外部扰动或对抗性注入。未来可探索方向包括：1) 将PAIR扩展为动态自适应机制，根据任务阶段自动调整hidden-state probe与attention-based head的权重，而非固定两阶段模型；2) 引入因果干预框架，学习去偏的隐状态表示，使其在多种污染模式下保持稳健；3) 探索将PAIR与mamba类状态空间模型结合，利用其线性复杂度的长程依赖建模能力，缓解多轮对话中前缀信息的遗忘问题；4) 设计多智能体协作训练范式，将PAIR作为内部奖励模型与外部验证器协同优化，提升复杂任务下的credit assignment精度。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为PAIR（前缀感知内部奖励模型）的方法，用于解决多轮智能体优化中GRPO算法的稀疏奖励问题。在复杂多步推理任务中，GRPO仅依赖最终结果奖励，导致中间步骤的信用分配困难。作者发现，现有补救方法（如全轨迹展开、外部LLM评判或依赖真实答案）各有局限。论文的核心洞察是，LLM的隐藏状态在干净前缀下能有效编码正确性，但在前缀受到早期错误污染时会严重退化，转而追踪与前缀的信念一致性；而注意力特征对污染更鲁棒，但干净情况下表现不足。基于这种互补性，PAIR采用两阶段架构：先用冻结的隐藏状态探针估计信念一致性分数，再通过轻量级注意力校正头将其向真实正确性修正。实验表明，PAIR在污染轨迹上实现了最高AUROC，且推理成本极低，能为GRPO提供稠密步级奖励信号，无需外部模型调用、真实答案依赖或全轨迹展开，在GTA和ToolBench基准上均取得了最优性能。
