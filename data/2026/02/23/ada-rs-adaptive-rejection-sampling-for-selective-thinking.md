---
title: "Ada-RS: Adaptive Rejection Sampling for Selective Thinking"
authors:
  - "Yirou Ge"
  - "Yixi Li"
  - "Alec Chiu"
  - "Shivani Shekhar"
  - "Zijie Pan"
  - "Avinash Thangali"
  - "Yun-Shiuan Chuang"
  - "Chaitanya Kulkarni"
  - "Uma Kona"
  - "Linsey Pang"
  - "Prakhar Mehrotra"
date: "2026-02-23"
arxiv_id: "2602.19519"
arxiv_url: "https://arxiv.org/abs/2602.19519"
pdf_url: "https://arxiv.org/pdf/2602.19519v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 推理"
  - "Agent 效率优化"
  - "选择性思考"
  - "工具使用"
  - "拒绝采样"
  - "偏好学习"
  - "策略优化"
relevance_score: 7.5
---

# Ada-RS: Adaptive Rejection Sampling for Selective Thinking

## 原始摘要

Large language models (LLMs) are increasingly being deployed in cost and latency-sensitive settings. While chain-of-thought improves reasoning, it can waste tokens on simple requests. We study selective thinking for tool-using LLMs and introduce Adaptive Rejection Sampling (Ada-RS), an algorithm-agnostic sample filtering framework for learning selective and efficient reasoning. For each given context, Ada-RS scores multiple sampled completions with an adaptive length-penalized reward then applies stochastic rejection sampling to retain only high-reward candidates (or preference pairs) for downstream optimization. We demonstrate how Ada-RS plugs into both preference pair (e.g. DPO) or grouped policy optimization strategies (e.g. DAPO). Using Qwen3-8B with LoRA on a synthetic tool call-oriented e-commerce benchmark, Ada-RS improves the accuracy-efficiency frontier over standard algorithms by reducing average output tokens by up to 80% and reducing thinking rate by up to 95% while maintaining or improving tool call accuracy. These results highlight that training-signal selection is a powerful lever for efficient reasoning in latency-sensitive deployments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在成本和延迟敏感的实际部署场景中，因过度或不必要的推理（如链式思维，CoT）而导致的效率低下问题。具体而言，当LLM作为工具调用智能体（例如在客服助手或电商导购中）处理用户请求时，许多简单查询（如寒暄、快速澄清）并不需要复杂的逐步推理，生成冗长的“思考”痕迹会浪费大量计算令牌，增加推理成本和响应延迟，损害用户体验。

因此，论文的核心问题是：如何让LLM学会**选择性思考**——即智能地决定何时需要进行深入推理，何时可以直接跳过推理、简洁回应或调用工具。这并非单纯提升推理能力，而是优化推理资源的分配，在保证处理复杂任务质量的同时，最大限度地减少简单任务上的开销。

论文指出，现有选择性思考方法多依赖于调整决策边界或设计专门的训练目标。本文则从一个互补的角度切入，聚焦于**训练样本的筛选**。为此，作者提出了自适应拒绝采样框架（Ada-RS），其核心思想是在模型训练阶段，对多个采样生成的回复进行评分（结合质量与长度惩罚），并通过随机拒绝采样，仅保留那些对学习“高效且选择性思考”最有信息量的高质量候选样本（或偏好对），用于下游的优化算法（如DPO、分组策略优化）。该方法旨在从训练信号构建的源头入手，鼓励模型生成既准确又简洁的回应，从而在延迟敏感的实际系统中实现更优的准确率-效率权衡。

### Q2: 有哪些相关研究？

相关工作主要围绕如何实现高效推理，特别是选择性思考（Selective Thinking）。现有研究可分为两类：

1.  **显式控制推理**：通过在推理时使用特殊提示指令、格式约束或难度感知提示来直接控制模型是否进行思考。例如，Ma等人（2025）和AutoThink等工作通过提示层面进行控制。这类方法部署简单，但依赖外部提示，模型未内化“何时需要思考”的决策，且性能对提示措辞敏感，泛化性可能受限。

2.  **通过训练实现选择性思考**：旨在通过修改奖励函数或训练目标，让模型学习在任务成功与推理成本间进行权衡。例如，Yang等人（2025）和Lou等人（2025）通过奖励设计，Zhang等人（2025）和Xiang等人（2026）通过目标函数调整来实现。相比提示方法，这类方法能让模型更好地内化决策，但需要精细调整惩罚强度或多阶段训练，以避免模型陷入“总是思考”或“从不思考”的退化解。

本文提出的Ada-RS与上述研究目标一致，但侧重点不同。先前工作侧重于**奖励设计或替代训练目标**，而本文聚焦于**训练信号的构建与选择**。Ada-RS通过自适应拒绝采样，在训练中随机保留具有高自适应长度惩罚奖励的样本（或偏好对），旨在减少冗长轨迹对训练的影响，同时保留对困难输入的显式推理能力。因此，本文可视为对现有训练方法的一种补充和优化，通过改进训练数据的筛选机制来更高效地学习选择性思考。

### Q3: 论文如何解决这个问题？

论文通过提出自适应拒绝采样（Ada-RS）框架来解决工具调用型大语言模型在选择性思维（selective thinking）中效率与准确性的权衡问题。其核心方法是设计一个轻量级的样本筛选机制，可灵活嵌入离策略（如DPO）和同策略（如DAPO）优化流程中，从模型生成的多个候选推理轨迹中，自适应地筛选出高质量、高效率的样本用于下游训练。

架构设计上，Ada-RS包含两个关键技术组件。首先是**自适应长度惩罚（ALP）**，它定义了一个复合奖励函数 \( r(y_i, x) = \mathbbm{1}(y_i, x) - \alpha \cdot s_K(x) \cdot |t_i| \)。该奖励不仅评估任务完成正确性（\(\mathbbm{1}(y_i, x)\)），还引入了一个与推理长度（\(|t_i|\)）成比例的惩罚项。关键创新在于惩罚系数 \( s_K(x) \) 是当前策略下该提示的在线解决率估计。这意味着对于模型已能轻松解决（高解决率）的简单问题，系统会施加更强的长度惩罚，从而抑制不必要的冗长推理；而对于困难问题（低解决率），则减轻惩罚，允许更长的思考过程。这种动态调整实现了“该想时才想”的自适应效率控制。

其次是**基于奖励的随机拒绝采样**，它利用上述奖励对候选样本进行筛选，以构建更优质的训练信号。框架支持两种模式：1) **成对拒绝采样**，用于偏好学习（如DPO）。它计算候选对之间的奖励差值 \(\Delta_{ij}\)，并以概率 \( p_{ij} = \exp((\Delta_{ij} - \Delta_{\text{max}})/\beta_{\mathrm{rs}}) \) 接受该对，将其转化为优胜（\(y^w\)）和劣汰（\(y^l\)）样本对。2) **分组拒绝采样**，用于分组策略优化（如DAPO）。它基于每个候选的标准化奖励（\( (r_i-\mu)/\sigma \)），以概率 \( p_i = \min(\exp((r_i-\mu)/\sigma / \beta_{\mathrm{rs}}), 1) \) 独立决定是否保留该样本。通过温度参数 \(\beta_{\mathrm{rs}}\) 控制筛选的严格度，从而在集中训练于高奖励样本和保持多样性之间取得平衡。

最终，论文展示了如何将Ada-RS具体实例化为**Ada-RS-DPO**和**Ada-RS-DAPO**两种算法。前者通过成对采样构建高质量偏好对来优化DPO目标，并辅以负对数似然损失来稳定训练；后者则将分组采样嵌入DAPO的同策略更新中，在计算损失前过滤候选，使梯度更新集中于既正确又高效的推理轨迹上。这种算法无关的筛选框架，通过优化训练信号的选择，显著提升了模型在延迟敏感场景下的推理效率边界。

### Q4: 论文做了哪些实验？

实验基于Qwen3-8B模型，使用LoRA适配器进行训练。评估在一个合成的多轮次、多步骤电子商务数据集上进行，该数据集模拟了用户画像和任务，包含约8000多个对话和15000次工具调用。基准测试包括无微调基线（始终思考/从不思考）、监督微调（SFT）、DPO和DAPO，并与Ada-RS的消融实验对比。核心评估指标为思考率（模型产生推理痕迹的实例百分比）、输出令牌长度（平均生成令牌数）和工具调用准确率。

主要结果显示，SFT能实现最高准确率（约89%），但思考率高且输出冗长。标准DPO未能改变模型“始终思考”的默认行为。而Ada-RS框架（包括自适应长度惩罚奖励和随机拒绝采样）显著改善了准确率-效率前沿：Ada-RS-DPO在保持与SFT相近的准确率（约89%）的同时，将平均输出令牌减少了约80%（从约450个降至约88个），并将思考率大幅降低至约6%。Ada-RS-DAPO进一步将思考率降至更低水平（约5%）。消融实验表明，拒绝采样与负对数似然稳定项的结合对于诱导选择性思考至关重要，缺少稳定项会导致学习不稳定和准确率下降。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在实验范围较窄和评估指标不够全面。未来可进一步探索以下方向：首先，将Ada-RS框架扩展到更多领域（如医疗、金融）和更大规模的模型上，验证其通用性和可扩展性；其次，开发更全面的评估体系，不仅关注单步工具调用的准确性，还需引入多轮对话下的端到端任务完成率、用户满意度等面向实际应用的指标；此外，可以研究如何将Ada-RS与其他高效推理技术（如思维蒸馏、早期退出机制）结合，以进一步优化延迟与性能的权衡；最后，探索在更复杂的交互环境（如动态工具集、开放域任务）中自适应拒绝采样的鲁棒性，推动其在真实场景中的部署。

### Q6: 总结一下论文的主要内容

这篇论文针对成本与延迟敏感场景下大语言模型（LLM）的推理效率问题，提出了**自适应拒绝采样（Ada-RS）**框架。其核心贡献在于，通过一种与具体优化算法无关的样本过滤机制，引导模型学会“选择性思考”——即仅在复杂任务上进行显式推理（如思维链），而对简单请求则直接输出答案，从而避免不必要的令牌消耗。

Ada-RS 的工作原理是：对于给定上下文，模型生成多个候选完成序列，并使用一个结合了效果与长度惩罚的自适应奖励函数进行评分；随后通过随机拒绝采样，仅保留高奖励的候选样本（或偏好对）用于下游的模型优化（如 DPO 或 DAPO）。实验表明，在工具调用任务上，Ada-RS 能显著提升模型的效率-精度边界，在保持甚至提升工具调用准确率的同时，将平均输出令牌数减少高达 80%，并将“思考”频率降低高达 95%。

这项工作的意义在于，它揭示了**训练信号的选择与过滤**本身是优化模型推理效率的一个关键杠杆，为实现严格产品约束下高效、精准的推理模型部署提供了新思路。
