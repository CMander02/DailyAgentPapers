---
title: "InfoPO: Information-Driven Policy Optimization for User-Centric Agents"
authors:
  - "Fanqi Kong"
  - "Jiayi Zhang"
  - "Mingyi Deng"
  - "Chenglin Wu"
  - "Yuyu Luo"
date: "2026-02-28"
arxiv_id: "2603.00656"
arxiv_url: "https://arxiv.org/abs/2603.00656"
pdf_url: "https://arxiv.org/pdf/2603.00656v1"
github_url: "https://github.com/kfq20/InfoPO"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Human-Agent Interaction"
relevance_score: 8.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Human-Agent Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "InfoPO (Information-Driven Policy Optimization)"
  primary_benchmark: "N/A"
---

# InfoPO: Information-Driven Policy Optimization for User-Centric Agents

## 原始摘要

Real-world user requests to LLM agents are often underspecified. Agents must interact to acquire missing information and make correct downstream decisions. However, current multi-turn GRPO-based methods often rely on trajectory-level reward computation, which leads to credit assignment problems and insufficient advantage signals within rollout groups. A feasible approach is to identify valuable interaction turns at a fine granularity to drive more targeted learning. To address this, we introduce InfoPO (Information-Driven Policy Optimization), which frames multi-turn interaction as a process of active uncertainty reduction and computes an information-gain reward that credits turns whose feedback measurably changes the agent's subsequent action distribution compared to a masked-feedback counterfactual. It then combines this signal with task outcomes via an adaptive variance-gated fusion to identify information importance while maintaining task-oriented goal direction. Across diverse tasks, including intent clarification, collaborative coding, and tool-augmented decision making, InfoPO consistently outperforms prompting and multi-turn RL baselines. It also demonstrates robustness under user simulator shifts and generalizes effectively to environment-interactive tasks. Overall, InfoPO provides a principled and scalable mechanism for optimizing complex agent-user collaboration. Code is available at https://github.com/kfq20/InfoPO.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在与用户进行多轮交互时，因用户请求信息不完整（underspecified）而面临的策略优化难题。研究背景是，现实世界中用户向AI智能体提出的请求常常模糊不清，智能体必须通过主动交互来获取缺失信息，才能做出正确的后续决策。当前主流方法多基于分组相对策略优化（GRPO），并依赖轨迹级别的奖励计算，这导致了两个核心不足：一是长期信用分配问题，稀疏且延迟的最终任务奖励难以准确评估中间交互回合的贡献；二是在一个 rollout 组内，优势信号区分度不足，无法为关键的信息澄清回合提供精细化的学习信号。

因此，本文要解决的核心问题是：如何为多轮交互策略提供更精细、更有效的学习信号，以优化智能体在信息不完整场景下的主动信息获取（意图澄清）与任务执行之间的协同。为此，论文提出了信息驱动的策略优化方法 InfoPO，其核心思想是将多轮交互建模为一个主动减少不确定性的过程。它通过计算一个细粒度的、基于信息增益的回合级奖励来解决上述问题。该方法利用反事实掩码技术，比较反馈信息实际存在与被掩码时智能体后续行动分布的变化，从而将奖励直接归因于那些能显著改变后续决策的关键交互回合。同时，通过一种自适应的方差门控融合机制，将信息增益奖励与任务结果奖励动态结合，确保学习过程既关注信息获取的重要性，又不偏离最终的任务目标导向。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为用户中心智能体、智能体强化学习和强化学习奖励塑形三类。

在用户中心智能体方面，相关研究致力于超越单纯任务完成，转向推断用户潜在意图和偏好，涉及意图澄清策略、个性化基准（如LaMP）以及结合反馈与外部工具的工作流测试平台。本文的InfoPO聚焦于此类多轮交互中的信用分配问题，与现有工作共享问题背景，但核心区别在于提出了细粒度的信息增益奖励来优化学习过程。

在智能体强化学习方面，强化学习已被广泛用于提升LLM智能体的决策能力，特别是针对多轮信用分配的研究，出现了分层训练、协作训练以及针对长轨迹不稳定性进行优化的方法（如RLVR风格设计、组相对方法）。本文的InfoPO属于此类方法，其创新点在于引入了基于反事实推理的轮次级信息优势信号，以解决现有方法中轨迹级奖励导致的信用分配模糊和优势信号不足的问题。

在奖励塑形方面，经典方法通过添加内在奖励（如基于好奇心的奖励）来促进探索或加速稀疏奖励下的学习；在LLM训练中，则体现为偏好监督或过程奖励模型。InfoPO的工作与此类研究精神一致，旨在提供更密集的学习信号。其关键区别在于，InfoPO的轮次级信息增益奖励源自通用的不确定性减少原理，无需依赖任务特定的启发式规则或预先训练好的过程奖励模型，从而更具原则性和可扩展性。

### Q3: 论文如何解决这个问题？

论文通过提出InfoPO（信息驱动的策略优化）这一多轮强化学习算法来解决用户请求不明确时智能体交互中的信用分配问题。其核心方法是将多轮交互建模为主动不确定性降低过程，并设计了一种细粒度的、基于信息增益的奖励机制，以精准评估每轮交互对后续决策的贡献。

整体框架基于分组相对策略优化（GRPO），但进行了关键创新。主要模块包括：1）**反事实信息增益奖励计算器**：在每个交互轮次t，智能体执行动作a_t并获得反馈o_t。为量化该反馈的信息价值，算法构建一个反事实场景，即假设未收到该反馈（用占位符∅表示），并计算在真实反馈和反事实条件下，智能体生成下一动作a_{t+1}的对数概率差异的平均值，作为该轮的信息增益奖励r_t^{info}。这种方法实现了因果隔离（确保奖励变化仅源于反馈）和计算高效性（通过并行前向传播避免多次自回归展开）。2）**优势估计与自适应融合模块**：算法为每个提示采样一组轨迹，并分别计算基于任务结果的标准化优势A^{ext}和基于信息增益的标准化优势A^{info}。关键创新在于**方差门控自适应融合策略**：通过一个门控函数g(σ_g^{ext})，根据组内外部奖励的方差σ_g^{ext}动态调整信息增益优势的权重。当外部奖励难以区分（方差小）时，增大信息增益的权重以驱动学习；当外部奖励区分度大时，则侧重于任务结果。最终统一优势为两者加权和。3）**策略优化目标**：使用包含裁剪机制的PPO风格目标函数，结合统一优势信号和相对于参考策略的KL散度惩罚，以稳定训练并控制分布偏移。

创新点在于：第一，提出了一个与任务无关的、细粒度的信息进度度量标准，其数学期望等价于反馈与后续动作之间的条件互信息，从信息论角度提供了理论依据。第二，设计了方差门控融合机制，使智能体能自适应地在探索信息（当任务反馈模糊时）和利用任务奖励（当反馈明确时）之间取得平衡。第三，理论证明了高任务成功率需要累积足够的信息增益，为该方法必要性提供了支撑。

### Q4: 论文做了哪些实验？

本论文在三个多轮、以用户为中心的基准测试上进行了实验，以评估所提出的InfoPO方法。

**实验设置与数据集**：实验使用了三个基准测试：(1) **UserGym**：包含八个统一环境，涵盖旅行规划、偏好说服、目标推断等多种交互范式，评估成功率或累计奖励。(2) **ColBench**：一个协作编程基准，智能体通过迭代讨论细化技术需求并生成Python代码，评估指标为通过隐藏单元测试的比例（Pass）和任务完成率（Succ.）。(3) **τ²-Bench**：一个涉及航空、零售和电信领域的复杂双重控制任务，需要高级协调，报告4次独立运行的平均成功率（Avg@4）。所有实验均基于Qwen2.5-7B-Instruct和Qwen3-4B模型，直接进行强化学习训练，无监督微调冷启动。使用GPT-4o-mini作为默认用户模拟器。

**对比方法**：对比的基线方法包括：(i) **UserRL**：一个代表性的以用户为中心的多轮训练框架。(ii) **RAGEN**：通过基于方差的轨迹过滤和解耦裁剪来关注训练稳定性。(iii) **Search-R1**：通过检索令牌掩码优化基于搜索的推理。(iv) **ReAct**和**Reflexion**：作为非训练的提示基线，用于量化策略优化的必要性。此外，还评估了闭源模型（如Gemini-3-Flash、GPT-4.1）的提示性能，并设置了InfoPO的多个消融版本（如去除外部奖励、去除门控机制、去除标准化）。

**主要结果与关键指标**：在Qwen2.5-7B-Instruct模型上，InfoPO在开源RL基线中取得了最强的整体结果。在UserGym的8个子环境中，InfoPO在7个上优于最强基线，关键指标如Search（0.480 vs. 0.446）、Intention（1.892 vs. 1.826）、Telepathy（0.488 vs. 0.424）均有显著提升。在ColBench上，InfoPO在技术指标上明显改进（Pass: 0.534 vs. 0.457; Success: 0.426 vs. 0.352），略超GPT-4.1（0.529/0.403）。在τ²-Bench上，InfoPO在所有任务家族中匹配或改进了最佳开源基线（Telecom: 0.181; Retail: 0.188; Air: 0.150）。训练动态显示，InfoPO能更早启动优化，达到更高奖励水平且振荡减少。消融实验表明，去除外部监督会导致性能大幅下降；禁用动态门控会损害训练稳定性；去除标准化则会降低性能并增加交互长度敏感性。交互动态分析显示，InfoPO呈现出“探索-巩固”模式，能策略性地利用交互获取关键信息，而不会陷入冗长重复。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其信息增益奖励的计算依赖于反事实推理，即假设未收到用户反馈时的动作分布，这在复杂或高维状态空间中可能难以准确估计。未来研究可探索更高效的不确定性量化方法，例如集成学习或贝叶斯神经网络，以提升奖励信号的鲁棒性。此外，当前方法主要针对离散对话交互，可扩展至连续动作空间（如机器人控制）或多模态交互场景。另一个方向是自适应融合机制，目前方差门控融合可能对超参数敏感，可引入元学习动态调整融合权重。最后，可考虑将信息驱动优化与符号推理结合，使智能体不仅能减少不确定性，还能主动规划信息获取策略，实现更高效的人机协作。

### Q6: 总结一下论文的主要内容

论文针对LLM代理在现实应用中常面临用户请求信息不足的问题，提出了一种信息驱动的策略优化方法InfoPO。核心贡献在于将多轮交互建模为主动减少不确定性的过程，并设计了基于信息增益的奖励机制，以细粒度地评估每次交互的价值。该方法通过对比实际反馈与掩码反馈的反事实情景，计算反馈对代理后续行动分布的影响，从而更精确地分配奖励，解决了传统基于轨迹奖励方法中的信用分配问题。此外，InfoPO采用自适应方差门控融合，将信息增益奖励与任务结果奖励结合，确保学习过程既关注信息获取又保持任务导向。实验表明，在意图澄清、协作编程和工具增强决策等任务中，InfoPO均优于提示学习和多轮强化学习基线，并在用户模拟器变化和环境交互任务中表现出良好的鲁棒性和泛化能力。该方法为优化复杂人机协作提供了原则性且可扩展的机制。
