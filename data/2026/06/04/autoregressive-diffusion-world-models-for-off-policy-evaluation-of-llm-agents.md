---
title: "Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents"
authors:
  - "Kaixuan Liu"
  - "Guojun Xiong"
  - "Weinan Zhang"
  - "Shengpu Tang"
date: "2026-06-04"
arxiv_id: "2606.05558"
arxiv_url: "https://arxiv.org/abs/2606.05558"
pdf_url: "https://arxiv.org/pdf/2606.05558v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent评估"
  - "离线策略评估"
  - "扩散世界模型"
  - "多轮交互"
  - "策略条件生成"
relevance_score: 8.5
---

# Autoregressive Diffusion World Models for Off-Policy Evaluation of LLM Agents

## 原始摘要

Evaluating large language model (LLM) agents in multi-turn interactive environments is expensive and risky, as it requires online environment interaction. We propose ADWM (Autoregressive Diffusion World Model), an evaluation framework that estimates the performance of a new LLM agent policy purely from pre-collected trajectories. The core idea is to learn a latent diffusion world model that simulates how the environment responds to the evaluation policy, without ever executing it in the real environment. Existing diffusion-based OPE methods guide full trajectories in a single pass by jointly diffusing states and actions, an assumption that breaks down for LLM agents whose actions are discrete text that must be sampled from the policy after observing the environment. Unlike autoregressive world models that suffer from compounding errors, ADWM models each transition as an independent denoising process, enabling reliable step-by-step rollouts where the world model and agent alternate in causal order. Crucially, the LLM agent under evaluation directly guides the diffusion generation at each step via a policy-conditioned score function, ensuring that simulated trajectories accurately reflect its decision-making patterns. Empirically, ADWM achieves accurate value estimates and evaluation reliability across diverse multi-turn agent tasks, demonstrating its promise as a practical framework for offline LLM agent evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体在多轮交互式环境中进行离线策略评估（OPE）时面临的挑战。研究背景是LLM智能体被广泛应用于网站导航、代码执行等高风险任务，部署前评估其性能至关重要。然而，传统的在线评估需要在真实环境中执行智能体，成本高昂且可能产生不可逆的副作用。现有方法存在不足：重要性采样方法在长序列任务中权重呈指数级增长，导致估计器失效；基于值函数的方法在评估策略与行为策略差异大时存在偏差；双重稳健方法虽部分缓解问题，但无法解决高维文本空间中的长期分布偏移。模型基方法的自回归世界模型在逐token生成观察时，误差会累积和恶化。

本文提出ADWM框架，核心问题是实现无需在线环境交互的LLM智能体性能评估。ADWM通过将世界模型实例化为扩散过程，将策略引导的轨迹分布分解为单步条件概率的乘积，利用策略条件得分函数指导每一步的去噪生成，使模拟轨迹准确反映评估策略的决策模式。这避免了误差跨步累积，同时解决了训练策略与评估策略之间的分布偏移问题，从而在纯离线数据下可靠估计新策略的价值。

### Q2: 有哪些相关研究？

基于提供的论文信息，本文在相关研究中主要涉及两类工作：

1. **基于模型的离策略评估方法**：这类方法从离线数据中学习环境转移模型，并通过模拟评估策略的轨迹来估计其价值。传统方法的根本困难在于误差累积：小的建模误差随时间步长被放大，导致长程模拟偏离真实环境动态。现有工作通过悲观值惩罚或保守策略优化来缓解此问题，但都设计用于低维连续控制，无法处理自由形式的文本观测。此外，这些方法无法将模拟轨迹有条件地生成于评估策略，而是反映行为分布。ADWM通过将每个状态转移建模为独立的去噪过程来打破误差累积链，并利用引导评分函数确保每一步的生成都依赖于评估策略。

2. **基于扩散模型的世界建模**：扩散模型已被用于环境模拟，通过独立去噪每个转移步来缓解自回归世界模型的累积误差。然而，现有全序列扩散方法将状态和动作联合扩散，这要求动作是实值向量且由扩散过程本身生成，因此无法支持逐步交互——这对LLM智能体失效，因为其动作是离散文本，必须在观测环境后从策略中采样。ADWM推导出精确的因子化评分函数，使得评估策略能够自回归地引导每一步去噪过程，而无需将动作作为扩散过程的一部分。

### Q3: 论文如何解决这个问题？

ADWM（自回归扩散世界模型）通过将策略引导的轨迹分布分解为单步条件概率，解决LLM智能体离线评估中的因果依赖问题。其核心设计包括三个关键技术：

1. **结构化潜空间**：观察文本通过端到端训练的编码器E映射为潜状态z_t，投影器G_ψ将其转换为软令牌ñ_t供策略π_e读取。InfoNCE对比损失确保潜表示与策略嵌入空间对齐，辅助逆动力学损失和模仿学习损失增强动作感知能力。

2. **三因子引导扩散**：基于定理证明，单步条件概率分解为三项乘积并转换为加性分数：
   - **先验分数**：无条件扩散模型p_θ提供环境动力学先验
   - **动作后验分数**：通过无分类器引导（CFG）从动作条件与无条件输出差异中恢复
   - **延续分数**：通过展开未来轨迹计算π_e对数似然的梯度，反映长程策略兼容性
   这三项在逆扩散过程中动态融合，其中CFG尺度控制动作一致性强度，延续系数η_k随去噪进程退火增强。

3. **自回归执行框架**：世界模型与π_e交替操作——模型先生成ñ_t，π_e据此采样a_t，再驱动下一步扩散生成。每个时间步独立执行K步去噪，避免传统自回归模型的误差累积。蒙特卡洛价值估计通过奖励头r_ρ预测即时奖励，终止头d_ρ决定episode结束，完全无需真实环境交互。

### Q4: 论文做了哪些实验？

论文围绕ADWM框架在离策略评估（OPE）中的有效性进行了系统实验。实验设置上，基于四个LLM智能体基准测试：HotpotQA（密集逐步奖励F1）、ScienceWorld（部分奖励）、WebShop（连续部分奖励）和ALFWorld（稀疏二值成功）。每个基准中，行为策略π_b用于收集世界模型训练数据，评估策略π_e为待评新策略（如DPO/PRM、ETO、LEAP迭代版等），两者严格不同。为度量性能，对每个评估策略构造ε-贪婪变体（ε=0,0.25,0.5,0.75,1.0），生成不同质量等级策略，并计算Spearman等级相关系数ρ对比ADWM预测的累计奖励Ĵ与真实环境曲线。

对比方法包括直接法（DM）、重要性采样（IS）、加权IS（WIS）、拟合Q评估（FQE）和双鲁棒估计（DR）。主要结果中，ADWM在所有6个（π_b,π_e）配置上均获得正ρ（均值+0.82，最小值+0.67），而所有经典基线至少在三组配置上失败：IS和DR因重要性权重爆炸崩溃（ρ低至-0.90），WIS退化为单权重轨迹（ρ=0），FQE仅在ALFWorld-iter1上表现良好（ρ=+0.82）但均值仅+0.10。消融实验表明，ADWM的三个核心组件（局部CFG、延续引导、ψ适配器）在不同奖励结构下互补：局部CFG对稀疏奖励最关键（移除后WebShop的ρ从+0.90降至+0.10），延续引导主导目标导向轨迹，ψ适配器在语言丰富环境（HotpotQA）至关重要。

### Q5: 有什么可以进一步探索的点？

**局限性与未来方向：**

1. **扩散效率与实时性瓶颈**：ADWM每一步需完整执行扩散去噪过程，多轮交互下计算开销显著高于单步自回归模型。未来可探索蒸馏或一致性模型加速采样，例如将扩散过程压缩为单步预测。

2. **长程依赖与状态漂移**：虽然独立去噪缓解了误差累积，但长序列中历史轨迹的语义信息可能逐渐衰减。可引入记忆增强模块（如Transformer-XL风格的长程注意力）或层级扩散结构（粗粒度规划+细粒度修正）。

3. **离散文本的扩散适用性**：文本动作的离散性导致扩散噪声需在连续空间与离散语义间转换，可能导致生成质量波动。建议研究指数族扩散或离散空间直接扩散机制，避免连续-离散映射损失。

4. **策略分布偏移鲁棒性**：当评估策略与行为策略差异极大时，指导信号可能误导高概率区域外的探索。可利用对抗性奖励塑形或集成多样性采样的策略条件分布校正。

5. **多模态环境泛化**：当前聚焦文本动作，但真实环境常包含视觉/结构化状态。可扩展为多模态扩散世界模型，统一编码不同模态的低维潜表示。

### Q6: 总结一下论文的主要内容

ADWM提出了一种离线评估多轮交互LLM代理策略价值的新框架。核心问题是：在无法直接与环境交互的情况下，如何仅基于预采集的轨迹数据可靠评估新策略。现有方法面临分布偏移、指数级重要性权重失效或误差累积等难题。ADWM创新性地将每个环境转移建模为独立的去噪扩散过程，而非像传统自回归模型那样逐token生成观测，从而避免了跨步骤的误差累积。关键理论贡献在于证明了策略引导的轨迹分布可以精确分解为一系列自回归单步条件分布的乘积，每个条件分布包含先验、动作后验和策略延续因子。该分解被映射为受策略引导的扩散过程：通过将评估策略的对数似然梯度注入每一步去噪中，使得模拟生成的轨迹能准确反映该策略的决策模式，无需重新训练世界模型。实验表明，ADWM在多种多轮代理任务中均能准确估计值函数并正确排序策略，其鲁棒性源自三种引导组件的协同作用。该工作为LLM代理的安全、低成本离线评估提供了实用框架。
