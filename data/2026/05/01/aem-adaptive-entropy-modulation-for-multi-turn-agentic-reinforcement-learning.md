---
title: "AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning"
authors:
  - "Haotian Zhao"
  - "Yuxin Zhang"
  - "Songlin Zhou"
  - "Stephen S. -T. Yau"
  - "Wenyu Zhang"
  - "Lun Tian"
  - "Tianshu Zhu"
  - "Yifeng Huang"
  - "Yucheng Zeng"
  - "Jingnan Gu"
  - "Daxiang Dong"
  - "Jianmin Wu"
date: "2026-05-01"
arxiv_id: "2605.00425"
arxiv_url: "https://arxiv.org/abs/2605.00425"
pdf_url: "https://arxiv.org/pdf/2605.00425v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "多轮训练"
  - "强化学习"
  - "信用分配"
  - "熵调制"
  - "SWE-bench"
relevance_score: 8.5
---

# AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning

## 原始摘要

Reinforcement learning (RL) has significantly advanced the ability of large language model (LLM) agents to interact with environments and solve multi-turn tasks. Yet effective training remains challenging, as sparse, outcome-only rewards make it difficult to assign credit to individual steps in an agent's action trajectory. A common remedy is to introduce dense intermediate supervision, such as process reward models or auxiliary self-supervised signals, but this increases supervision and tuning complexity and often generalizes poorly across tasks and domains. This paper presents AEM, a supervision-free credit assignment method that adaptively modulates entropy dynamics during RL training to achieve a more effective exploration-exploitation trade-off. Theoretically, we elevate entropy analysis from the token level to the response level to reduce token sampling variance and show that entropy drift under natural gradients is intrinsically governed by the product of the advantage and the relative response surprisal. Specifically, we derive a practical proxy to reshape training dynamics, enabling a natural transition from exploration to exploitation. Extensive experiments across various benchmarks and models ranging from 1.5B to 32B parameters demonstrate the effectiveness of AEM, including a notable 1.4 percent gain when integrated into a state-of-the-art baseline on the highly challenging SWE-bench-Verified benchmark.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多轮交互式智能体（agentic RL）中大语言模型（LLM）强化学习训练中的信用分配（credit assignment）问题。研究背景是，LLM正被部署为与环境进行多轮交互的智能体，然而现有的强化学习方法（如GRPO）面临挑战：任务奖励极度稀疏，仅在最终结果给予反馈，无法有效区分探索性步骤、决定性步骤和冗余步骤对最终结果的贡献。现有的解决方法存在诸多不足：过程奖励模型需要额外训练且泛化性差；自监督方法如GI-GPO、IGPO等容易受到上下文不一致、分组偏差和结构性假设的限制；而Tree-GRPO等树结构优化方法在多轮场景下计算开销过高。因此，本文核心要解决的是：如何在不依赖额外监督、繁重计算或严苛结构性假设的前提下，实现高效、细粒度的信度分配。作者提出AEM（自适应熵调节）方法，从理论上将熵分析从token级别提升至response级别，并推导出熵动态受优势函数与相对惊奇度的乘积控制，从而利用正负样本的动态平衡来自适应调节策略熵，在训练中实现从探索到开发的自然过渡。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类。第一类是**从LLM到智能体强化学习**的工作，如ReAct和Toolformer，它们将LLM从被动生成器转变为能与环境交互的决策者，并采用RLOO、GRPO等基于群体的方法进行训练。本文指出，这些方法从单轮扩展到多轮智能体场景时，会加剧稀疏奖励问题，缺乏对中间步骤的指导，导致梯度方差大和信用分配模糊。第二类是**智能体RL中的信用分配方法**，现有方法分为依赖外部信号（如价值函数或步骤级监督）和从轨迹中内部推导信用两类。前者增加了额外的建模和扩展成本，后者虽改进了粒度但在多轮设置中计算开销大。本文强调这些方法都忽略了策略自身的熵，而熵作为模型在每个决策中的不确定性，是一种天然的信用调制信号。第三类是**熵感知的策略优化**，如熵正则化或熵引导的优势缩放，它们将熵用于鼓励探索或稳定训练。但与这些仅使用词元级熵或主要稳定训练的方法不同，本文提出了响应级熵作为内在信号，自适应地调节每个响应的优势，从而在多轮智能体RL中实现可扩展的信用分配和探索-利用的平衡，且无需额外的监督。

### Q3: 论文如何解决这个问题？

AEM通过自适应熵调制实现免监督的信用分配，其核心方法是将响应级相对意外度转化为调节系数$\alpha$，重塑探索-利用动态。整体架构不改变底层RL优化器，仅作为即插即用模块在优势估计器之后应用。

**核心机制**：理论分析证明，在Fisher-Rao度量下，全局熵漂移由采样响应的优势$A(a,s)$和相对意外度$S(a|s)-\mathcal{H}_{\text{resp}}(s)$共同决定。AEM利用每个响应的平均token熵$\bar{\mathcal{H}}$作为相对意外度的代理，采用逐token可分解的Doob分解形式降低采样方差。

**关键技术**：对每个rollout内的所有响应组成群组$\mathcal{G}$，对$\bar{\mathcal{H}}$进行min-max归一化得到$\tilde{\mathcal{H}}$，通过指数变换生成自校准调制系数$\alpha=\exp(-\lambda\tilde{\mathcal{H}})/\text{avg}(\exp(-\lambda\tilde{\mathcal{H}}))$。该系数满足：当$\alpha>1$（低意外响应）时对优势加权，$\alpha<1$（高意外响应）时对优势降权。

**探索-利用动态**：训练早期负优势响应（探索阶段）占主导，高意外响应被降权（$\alpha<1$）从而减弱熵减压力，低意外响应被加权（$\alpha>1$）从而放大熵增压力，整体促进探索；训练后期正优势响应（利用阶段）占主导，高意外响应通过降权减弱熵增压力，低意外响应通过加权放大熵减压力，整体促进收敛。这种单调递减映射通过求解一个带熵正则的最小化问题达到最优权衡。

### Q4: 论文做了哪些实验？

AEM在三个多轮LLM智能体基准上进行了评估：ALFWorld（文本具身推理）、WebShop（网页购物）和SWE-bench-Verified（现实软件工程）。实验使用1.5B和7B参数的Qwen2.5-Instruct模型，并对比了ReAct、PPO、GRPO、GSPO、DAPO等基线方法，以及DeepSWE框架（用于32B参数模型）。所有方法均采用基于规则的奖励（成功奖励10分，失败0分，无效动作-0.1；SWE任务为二元奖励）。关键结果如下：在ALFWorld上，AEM将GRPO的总体成功率从68.0%提升至76.8%（1.5B模型），并将DAPO从88.5%提升至94.5%；在WebShop上，AEM将GRPO的得分从83.6提升至86.4，并将DAPO从86.5提升至88.0。在更具挑战性的SWE-bench-Verified上，AEM将DeepSWE基线的成功率从42.3%提升至43.7%（提升1.4%）。分析实验验证了AEM通过奖励和响应熵的联合调节，实现了从探索到利用的自然过渡，且仅增加轻量级计算开销。

### Q5: 有什么可以进一步探索的点？

论文提出AEM通过响应级熵调制实现免监督的信用分配，但其局限在于假设熵动态与优势函数乘积关系可直接作为训练代理，未考虑复杂环境中奖励稀疏性与动作空间异质性带来的分布偏移。未来可探索以下方向：1）将响应级熵调制与过程级信用信号结合，例如用AEM动态调节过程奖励权重，缓解纯监督方法的泛化问题；2）引入元学习框架，让模型自适应学习熵调制系数而非固定公式，提升不同任务域的鲁棒性；3）探索多智能体场景下集体熵动态的协同调控策略，例如通过智能体间相对熵差异驱动协作探索。此外，当前方法对长程依赖任务（如复杂数学推理）的改进空间值得关注，可尝试将AEM与层次化强化学习结合，在子目标层实现更细粒度的探索-利用平衡。

### Q6: 总结一下论文的主要内容

强化学习（RL）在训练大语言模型（LLM）智能体完成多轮任务时，面临稀疏奖励难以对中间步骤进行信用分配的挑战。现有方法如过程奖励模型或自监督信号虽能提供密集监督，但增加了调优复杂度且泛化性差。本文提出AEM，一种无监督信用分配方法，通过自适应调节熵动态来优化探索-利用权衡。理论上，将熵分析从token级提升到响应级，以降低采样方差，并证明自然梯度下的熵漂移由优势与相对响应惊异度的乘积决定。据此推导出实用代理来重塑训练动态，实现从探索到利用的自然过渡。在ALFWorld、WebShop及SWE-bench-Verified等基准测试中，采用1.5B至32B参数的模型进行实验，AEM显著提升了基线方法，最高增益达8.8%，在SWE-bench-Verified上更是为最先进基线带来了1.4%的增益，证明了其作为多轮LLM智能体优化的有效归纳偏置。
