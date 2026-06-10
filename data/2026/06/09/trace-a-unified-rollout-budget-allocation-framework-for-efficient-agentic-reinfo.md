---
title: "TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning"
authors:
  - "Heming Zou"
  - "Qi Wang"
  - "Yun Qu"
  - "Yuhang Jiang"
  - "Lizhou Cai"
  - "Yixiu Mao"
  - "Ru Peng"
  - "Xin Xu"
  - "Weijie Liu"
  - "Kai Yang"
  - "Saiyong Yang"
  - "Xiangyang Ji"
date: "2026-06-09"
arxiv_id: "2606.11119"
arxiv_url: "https://arxiv.org/abs/2606.11119"
pdf_url: "https://arxiv.org/pdf/2606.11119v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "RLVR"
  - "rollout budget allocation"
  - "multi-turn agent"
  - "tree-structured rollout"
  - "reward contrast"
  - "policy optimization"
  - "ReAct"
relevance_score: 9.5
---

# TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning

## 原始摘要

Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models. However, rollout-intensive policy optimization is often limited by insufficient reward contrast, arising when overly simple or complex prompts generate low-variance feedback and when outcome-only rewards assign the same terminal assessment to every decision in a multi-turn rollout. Past efforts have focused on allocating available rollout resources to promising prompts, yet they only leverage sample informativeness at the prompt level and neglect variation in prefix-level informativeness across turns within the same rollout. This work targets multi-turn agentic RL by modeling each ReAct-style thought-action-observation turn as a semantically distinct node, allowing budget allocation to extend from prompt roots to turn-level prefixes with further continuations, which naturally forms tree-structured rollouts. We introduce Tree Rollout Allocation for Contrastive Exploration (TRACE), a unified rollout allocation framework that enhances reward contrast within a fixed sampling budget. Technically, TRACE allocates rollout budget to both prompt roots and intermediate prefixes that are most likely to yield mixed terminal rewards. A shared generalizable predictor estimates conditional success probability at these anchors from prefix histories to guide this allocation. The resulting adaptive tree structure enriches outcome-only feedback and amplifies the policy-update signal. Empirically, TRACE achieves competitive performance and efficiency gains on typical agentic benchmarks, e.g., improving Qwen3-14B Multi-Hop QA average accuracy by 2.8 points over competitive baselines at equal sampling cost.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在基于可验证奖励的强化学习（RLVR）中，由于采样预算有限，生成的轨迹（rollout）奖励对比度不足的问题。研究背景是，虽然RLVR能有效提升大语言模型的推理和智能体能力，但其计算成本极高，因为需要生成长链推理和与环境交互的轨迹。现有方法存在两个层面的不足：首先，在提示（prompt）层面，过简单或过困难的样本会产生低方差的奖励反馈，导致学习信号稀疏；其次，在轨迹层面，现有的策略仅对完整提示进行预算分配（例如决定每个提示生成多少条完整轨迹），忽视了多轮交互中前缀（prefix）级别的信息量差异，导致一条完整轨迹内的所有决策都只能共享同一个末端奖励，缺乏局部对比信号，使得信用分配困难。本文的核心问题是，如何在固定采样预算下，通过统一优化预算分配来最大化奖励对比度。具体而言，本文提出将预算不仅分配给提示根节点（root-level），还分配给轨迹中可能产生混合终端奖励（即有成功也有失败结果）的中间前缀节点（prefix-level），从而将扁平的轨迹集合转换为树状结构，以在相同预算下获得更丰富的对比性奖励信号，提升策略更新的效率。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕三个方向：**方法类**、**应用类**和**评测类**。

**方法类**方面，最直接的相关工作是**预算分配**（Budget Allocation）策略，如PPO-Active、ActiveRL等，它们关注如何在强化学习中将有限的采样预算分配给更有价值的prompt，以提升奖励信号的对比度。TRACE与这些工作的核心区别在于，前者仅在**prompt根节点**层面分配预算，而TRACE将分配粒度细化到**中间turn前缀**层面，利用ReAct模式中的turn级语义差异构建树状结构。

另一类方法是**对比探索**（Contrastive Exploration），如基于不确定性或训练动态的采样方法，旨在提高奖励方差。TRACE不仅关注prompt间差异，更深入捕获同一rollout内不同前缀的回报分化，从而在固定预算下更有效地生成对比性轨迹。

**应用类**方面，相关研究包括**工具使用**（Tool Use）和**多轮交互**（Multi-turn Interaction）中的在线RL训练，如FireAct、WebGPT等，这些方法在agentic任务中使用RL优化策略，但通常以完整轨迹为单位统一授予奖励。TRACE的贡献在于将末端奖励反向归因到每个中间决策节点，使信号更精细。

**评测类**方面，现有工作多集中在**多跳问答**（Multi-Hop QA）和**数字推理**（如HotpotQA、GSM8K）上，TRACE沿用这些基准，并对比了统一预算下的效率和效果差异。总体而言，TRACE在预算分配范式和奖励信号密度上均实现了关键突破。

### Q3: 论文如何解决这个问题？

TRACE通过统一分配卷展预算来增强奖励对比，核心是构建树状结构。整体框架分为两阶段：全局根分配和局部前缀扩展。

**核心方法**：TRACE将每个ReAct式思考-行动-观察回合视为语义不同的节点，将预算分配从提示根扩展到回合级前缀。通过一个共享的通用预测器 $\tilde V_\psi$，它根据前缀历史估计条件成功概率 $V_t^\pi$，指导预算分配。

**架构设计**：
- **全局根分配**：对候选提示池，基于预测的根成功概率 $v_i$，求解预算约束优化问题，分配根卷展数量 $m_i$。目标是最大化根卷展产生混合奖励（同时有成功和失败）的概率，公式为 $V_{\text{root}}(x_i,m) = 1 - v_i^m - (1-v_i)^m$。
- **局部前缀扩展**：对活跃提示 $x_i$ 的每个非叶子前缀节点 $(j,t)$，分配 $K_{i,j,t}$ 个续写。目标是最大化至少有一个续写翻转当前终端奖励的概率，公式为 $V_{\text{pref}}(i,j,t,k) = 1 - [r_{i,j}\tilde V_\psi(\mathcal{H}_{i,j,t}) + (1-r_{i,j})(1-\tilde V_\psi(\mathcal{H}_{i,j,t}))]^k$。总续写预算为 $m_iN$。
- **预测器训练**：通过自底向上的递归树目标 $\widehat V(y)$（经验成功率）对 $\tilde V_\psi$ 进行均方误差回归训练。

**关键技术**：
- **混合奖励对比构建**：将分配目标定为诱导根和前缀节点下产生混合终端奖励，从而为树感知优化器提供隐式成对偏好对比，增强策略更新信号。
- **两阶段解耦**：根分配和前缀扩展分步进行，且扩展在提示级别本地完成，避免了跨提示等待，提高了并行效率与系统扩展性。

**创新点**：将卷展预算分配从提示根扩展到前缀级别，通过预测条件成功概率的伯努利方差 $\mathbb{E}[[Z]_{t:T} \mid \mathcal{F}_t] = V_t^\pi(1-V_t^\pi)$ 衡量对比潜力，实现对比增强的分配。

### Q4: 论文做了哪些实验？

论文在三个多轮交互场景上评估了TRACE框架，使用Qwen3-8B和Qwen3-14B作为策略主干。实验设置包括：数学推理（训练于DeepScaler语料库，评测AIME24、AMC23等6个基准）、多跳QA（训练于HotpotQA，评测其验证集以及2WikiMultiHopQA等4个基准）、以及函数调用（训练于BFCL v4多轮分割80%，评测剩余20%包含Base、Long-context等4个子集）。对比方法包括ReAct（基础模型评测）、GRPO（随机提示采样）、PCL（基于难度的提示筛选）和TreePO（树形展开但随机选择节点）。主要采用准确率（数学推理）、F1≥0.3的精确匹配和Token级F1（多跳QA）以及BFCL成功率（函数调用）作为指标。结果显示，在相同采样预算下，TRACE在三个场景中均取得更优性能：例如在数学推理中，TRACE将Qwen3-8B的GRPO平均准确率从70.0提升至71.1，Qwen3-14B从73.5提升至74.9；在多跳QA中，Qwen3-14B平均准确率提升2.8个百分点。此外，TRACE的有效对比率（训练批次中包含成功/失败终端的提示比例）显著提高，数学推理场景中Qwen3-8B从26.8%升至60.6%，Qwen3-14B从34.7%升至59.7%。消融实验验证了根预算分配和前缀预算分配两个阶段均有效且可叠加，不同预算规模（如512根+2延续 vs 1024根+2延续）下TRACE均优于TreePO，且根覆盖更广时效果更佳。

### Q5: 有什么可以进一步探索的点？

TRACE主要针对结果奖励的RLVR，其局限性在于无法有效处理缺乏明确终端验证的任务，例如开放域对话或长期规划，这些任务的奖励信号可能稀疏或延迟。未来可探索结合过程奖励或内在动机来扩展奖赏结构。在预算分配上，TRACE依赖预测器估计条件成功概率，但当前采用的简单实例化可能在高维或动态环境中不够鲁棒。改进方向包括利用贝叶斯优化或元学习来自适应调整预测模型，或引入不确定性量化以平衡探索与利用。实验仅覆盖数学推理、多跳QA和函数调用等基准，未涉及更复杂、非平稳的智能体场景（如多智能体博弈或实时策略）。进一步工作应评估TRACE在分布式、动态交互环境下的扩展性，例如集成分层RL或场景采样策略。此外，前缀级分配可能忽略动作间的长程依赖，利用图神经网络建模决策轨迹的拓扑结构或能提升对比多样性，从而优化策略梯度信号。

### Q6: 总结一下论文的主要内容

该论文针对强化学习与可验证奖励（RLVR）在多轮智能体任务中面临的奖励对比不足问题，提出一种统一的预算分配框架TRACE。问题定义在于：现有方法仅基于提示级别分配采样预算，忽略了同一轨迹内不同轮次（前缀）的信息量差异，导致低方差奖励信号难以有效驱动策略更新。方法核心是构建树状展开结构，将每个ReAct式思维-动作-观察轮次作为语义节点，通过共享可泛化的条件成功概率预测器，将采样的预算动态分配给提示根节点及中间前缀节点中更可能产生混合奖励（部分成功与部分失败）的锚点。由此，自适应树状结构强化了基于结果的奖励对比，提升了策略更新信号。主要结论表明，在数学推理、多跳问答和函数调用等基准上，TRACE在等采样成本下性能显著提升，例如在Qwen3-14B多跳问答平均准确率上比强基线高2.8个百分点。其意义在于将智能体RLVR采样重新定义为“在展开树的何处分支”，而非仅考虑独立展开的数量。
