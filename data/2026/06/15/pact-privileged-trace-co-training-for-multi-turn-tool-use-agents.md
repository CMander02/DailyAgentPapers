---
title: "PACT: Privileged Trace Co-Training for Multi-Turn Tool-Use Agents"
authors:
  - "Zhenbang Du"
  - "Jun Luo"
  - "Zhiwei Zheng"
  - "Xiangchi Yuan"
  - "Kejing Xia"
  - "Dachuan Shi"
  - "Qirui Jin"
  - "Qijia He"
  - "Shaofeng Zou"
  - "Yingbin Liang"
  - "Wenke Lee"
date: "2026-06-15"
arxiv_id: "2606.16215"
arxiv_url: "https://arxiv.org/abs/2606.16215"
pdf_url: "https://arxiv.org/pdf/2606.16215v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Multi-turn Tool-use Agent"
  - "Privileged Trace Co-Training"
  - "RL for Agent"
  - "Supervised Fine-tuning"
  - "Agent Optimization"
relevance_score: 9.0
---

# PACT: Privileged Trace Co-Training for Multi-Turn Tool-Use Agents

## 原始摘要

Multi-turn tool-use agents must reason, call tools, and adapt to observations across several interaction turns. Post-training such agents is challenging, as reinforcement learning often suffers from sparse rewards and weak credit assignment despite matching the prompt-only inference setting, while supervised fine-tuning on expert traces provides dense process supervision but can over-constrain the model to fixed trajectories. To tackle this, we propose PACT, a Privileged trAce Co-Training framework for multi-turn tool-use agents. The key idea is to use expert traces only as training-time optimization signals rather than rollout-time hints. PACT keeps rollout generation prompt-only, then uses expert traces to guide optimization through two complementary signals: a trace-conditioned RL surrogate that evaluates prompt-only rollouts under expert-trace context, and a component-aware SFT loss that supervises reasoning prefixes and tool-calls with annealed strength. To reduce over-reliance on the training-only trace context, PACT further introduces a prompt-only anchoring. We also provide a latent-trace view that connects the two trace-based objectives and explains how expert traces can guide optimization without being used during rollout generation. Experiments on FTRL, BFCL, and ToolHop show that PACT consistently improves over strong SFT- and RL-based baselines, highlighting the value of privileged trace co-training for multi-turn tool-use learning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多轮工具使用智能体后训练中的核心矛盾。现有方法面临两难：强化学习虽然在推理时不依赖专家轨迹，但多轮场景下的奖励稀疏且信用分配困难，难以学到有效策略；而基于专家轨迹的监督微调虽然能提供密集的过程监督，却会过度约束模型，使其只能模仿固定轨迹，限制了探索能力。尽管已有结合两者的尝试，但要么通过提示方式在生成时引入专家轨迹，改变了推理条件，与纯提示推理冲突；要么主要针对单轮思考链，无法处理含工具调用和观察反馈的复杂多轮交互结构。因此，本文要解决的核心问题是：如何在不改变纯提示式推理行为的前提下，利用专家轨迹有效指导多轮工具使用智能体的强化学习优化，从而同时获得强化学习的探索灵活性和监督微调的过程引导信号，提升最终任务表现。

### Q2: 有哪些相关研究？

在工具使用智能体领域，相关工作分为两类：一类是基于提示和指令微调的方法（如ReAct、Toolformer、ToolLLM），通过将推理与外部动作交错来训练模型；另一类是基于强化学习（RL）的方法（如Agent Lightning、ToolRL、MatchTIR），通过交互环境设计奖励和信用分配。PACT与这些方法的关键区别在于不修改奖励函数或环境，而是研究如何将专家轨迹作为训练时的特权上下文来使用，同时在 rollout 生成阶段保持纯提示模式。

在SFT与RL结合方面，相关工作包括UFT（利用部分解决方案提示桥接模仿和探索）、BRIDGE（双层优化使SFT与RL协作）、MIFO（缓解SFT和RL之间的遗忘）以及CHORD（通过全局系数平衡离策略专家数据与在策略RL）。PACT针对多轮工具使用场景的丰富结构（包括推理、结构化工具调用和环境观测），在这些工作基础上创新性地提出：保持rollout生成纯提示模式，但将专家轨迹作为优化时的特权上下文，用于RL似然评估和对模型可控的轨迹组件进行过程监督。这种方法与现有方法的主要区别在于分离了生成和优化阶段，避免了专家轨迹对模型输出的过约束。

### Q3: 论文如何解决这个问题？

PACT通过一种新颖的特权轨迹共训练框架解决多轮工具使用智能体的后训练问题。核心思想是将专家轨迹仅作为训练时的优化信号，而非推理时的提示。方法首先在纯提示条件下采样多条完整轨迹，保持与推理时一致的分布，避免专家轨迹的干扰。然后利用专家轨迹作为特权上下文，提供两种互补的优化信号：一是轨迹条件化的RL替代目标，将专家轨迹作为上下文计算策略比率，同时保留纯提示轨迹的回报和优势值，从而在不改变轨迹分布的情况下提供过程引导；二是组件感知的SFT损失，仅监督模型可控的部分（推理前缀和工具调用），对推理前缀采用语义片段级别的退火策略，从完整推理逐步缩减到空，对工具调用采用退火缩放，从强模仿逐渐过渡到自由探索。为减少对特权上下文的过度依赖，PACT引入纯提示锚定机制，对部分提示随机使用标准纯提示RL损失进行优化。整体架构包括一个策略网络，通过采样生成纯提示轨迹，并使用专家轨迹计算两种损失，最终结合权重进行参数更新。创新点在于将专家轨迹作为特权信息用于优化而非生成，通过双重目标提供密集过程监督，并通过锚定机制维持纯提示条件下的泛化能力。

### Q4: 论文做了哪些实验？

论文在FTRL、BFCL和ToolHop三个基准上进行了实验，使用Qwen3-1.7B和Qwen3-4B模型。训练数据来自FTRL（约2200样本），batch size为256，最大交互轮次10。对比方法包括SFT、GRPO、FTRL、ToolRL、CHORD、MatchTIR以及SFT→MatchTIR。主要指标：FTRL报告Solve-R/Solve-P/Solve-F1，BFCL报告Multi-Turn/Search/Memory/Avg，ToolHop报告Answer Correctness (AC)。结果显示：在1.7B模型上，PACT平均分达24.90，超过最强基线MatchTIR（21.70），在FTRL上Solve-R从24.12提升至28.33，BFCL四项均最优，ToolHop AC从32.26提升至34.47。在4B模型上，PACT平均分达36.90，超过最强基线（33.07），FTRL Solve-R从37.17提升至42.41，BFCl所有指标最优，ToolHop AC从47.54提升至49.55。消融实验表明：trace-conditioned RL（Solve-R 36.10）优于prompt-only RL（35.31），结合component-aware SFT达最优（40.45/32.94/33.21）；去除工具响应导致F1从33.21降至25.94，表明观测信息关键；推理引导采用分段退火（Seg A）、工具调用采用尺度退火（Scale A）效果最佳；prompt-only锚定概率q=0.2~0.5时泛化性能最好。

### Q5: 有什么可以进一步探索的点？

根据论文内容及我的分析，主要有以下几个值得深入探索的方向：

1.  **降低对专家轨迹的依赖**：论文明确提到构建高质量专家轨迹仍需要离线数据准备步骤，这是一个实际障碍。未来可以探索如何利用弱监督、自我生成或从失败轨迹中学习的方式，减少对人工标注专家数据的依赖，或实现自动化轨迹分割与质量评估。
2.  **优化自适应调度策略**：当前方法对推理前缀退火、工具调用损失缩放和纯提示锚定使用了简单的线性或固定调度。未来可以研究基于训练动态（如梯度变化、模型置信度）的自适应调度机制，这有望显著提升训练效率和最终性能。
3.  **扩展模型规模与任务多样性**：由于计算限制，实验仅覆盖了部分模型尺寸和基准。未来的关键方向是将PACT扩展到更大规模的模型（如70B+）以及更多样化、更复杂的工具使用环境（如涉及多步骤网络浏览或代码执行的场景），以全面检验方法的泛化能力和鲁棒性。

### Q6: 总结一下论文的主要内容

多轮工具使用智能体需在多次交互中推理、调用工具并适应观察，其训练面临挑战：强化学习存在稀疏奖励和信用分配问题，而监督微调则可能过度约束模型。为此，本文提出PACT（特权轨迹协同训练）框架，核心贡献在于将专家轨迹仅用作训练时的优化信号，而非生成时的提示。方法上，PACT保持生成仅基于提示，通过两种互补目标利用专家轨迹：一是轨迹条件强化学习代理，在专家轨迹上下文中评估提示生成的轨迹；二是成分感知监督微调损失，以退火强度监督推理前缀和工具调用。为减少对训练时轨迹上下文的过度依赖，引入提示唯一锚定。潜在轨迹视角解释了这两个基于轨迹目标的互补性。实验结果表明，PACT在FTRL、BFCL和ToolHop基准上持续优于强基线的监督微调和强化学习方法，证明了在生成中不使用专家轨迹的情况下，将其用于优化能有效提升多轮工具使用学习性能。
