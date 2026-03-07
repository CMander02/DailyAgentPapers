---
title: "Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use"
authors:
  - "Aradhye Agarwal"
  - "Gurdit Siyan"
  - "Yash Pandya"
  - "Joykirat Singh"
  - "Akshay Nambi"
date: "2026-03-03"
arxiv_id: "2603.03205"
arxiv_url: "https://arxiv.org/abs/2603.03205"
pdf_url: "https://arxiv.org/pdf/2603.03205v1"
categories:
  - "cs.CL"
tags:
  - "Tool Use & API Interaction"
  - "Safety & Alignment"
relevance_score: 8.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Safety & Alignment"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "Qwen2.5-7B, Qwen3-4B-Thinking, Phi-4"
  key_technique: "MOSAIC (post-training framework with plan-check-act/refuse loop and preference-based RL)"
  primary_benchmark: "N/A"
---

# Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use

## 原始摘要

Agentic language models operate in a fundamentally different safety regime than chat models: they must plan, call tools, and execute long-horizon actions where a single misstep, such as accessing files or entering credentials, can cause irreversible harm. Existing alignment methods, largely optimized for static generation and task completion, break down in these settings due to sequential decision-making, adversarial tool feedback, and overconfident intermediate reasoning. We introduce MOSAIC, a post-training framework that aligns agents for safe multi-step tool use by making safety decisions explicit and learnable. MOSAIC structures inference as a plan, check, then act or refuse loop, with explicit safety reasoning and refusal as first-class actions. To train without trajectory-level labels, we use preference-based reinforcement learning with pairwise trajectory comparisons, which captures safety distinctions often missed by scalar rewards. We evaluate MOSAIC zero-shot across three model families, Qwen2.5-7B, Qwen3-4B-Thinking, and Phi-4, and across out-of-distribution benchmarks spanning harmful tasks, prompt injection, benign tool use, and cross-domain privacy leakage. MOSAIC reduces harmful behavior by up to 50%, increases harmful-task refusal by over 20% on injection attacks, cuts privacy leakage, and preserves or improves benign task performance, demonstrating robust generalization across models, domains, and agentic settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体语言模型在多步工具使用场景中的安全问题。随着语言模型越来越多地被部署为能够规划、调用工具并与外部系统多步交互的智能体，其失败后果已从文本生成错误升级为可能造成不可逆现实危害的行动。例如，一个拥有文件、部署或支付工具访问权限的智能体，可能通过一系列看似合理的步骤，将良性请求升级为危险操作。

现有方法存在明显不足。传统的对齐方法主要针对静态生成和任务完成进行优化，在智能体面临的序列决策、对抗性工具反馈和过度自信的中间推理等场景下会失效。当前在智能体推理和强化学习方面的进展，虽然提升了数学、编程等领域最终任务的准确性，但其优化目标仍侧重于任务完成度。在多步工具使用环境中，冗长的推理轨迹常常忽略对安全性、事实依据或操作不可逆性的显式检查，导致深思熟虑后仍执行不安全行动。此外，仅依赖最终结果的标量奖励会将多步安全决策压缩为单一的终端信号，无法捕捉轨迹层面的安全差异（例如，早期拒绝与执行不安全中间行动后的晚期中止有本质区别）。

因此，本文要解决的核心问题是：如何让智能体语言模型在复杂的多步工具使用过程中，学会在何时安全地执行行动、何时必须明确拒绝，从而实现可靠的安全控制。论文通过引入MOSAIC框架来应对这一挑战，该框架将推理重构为“规划、检查、然后执行或拒绝”的循环，并将安全推理和拒绝作为首要的、显式的决策动作，而非长篇幅推理的隐含副产品。同时，论文采用基于偏好的强化学习与轨迹对比较方法进行训练，以学习那些被标量奖励所忽略的、与安全时机相关的关键区别。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、评测类和应用类。

在**方法类**研究中，现有工作主要集中在对话模型的安全对齐（如输出过滤、单轮安全防护）和任务导向的强化学习（如优化数学、编码等最终任务准确性）。然而，这些方法在智能体场景中存在局限：它们通常针对静态生成或任务完成进行优化，难以处理序列决策、对抗性工具反馈以及过度自信的中间推理，导致无法有效应对多步工具使用中的安全风险。本文提出的MOSAIC框架通过引入显式的“计划-检查-执行/拒绝”循环和基于偏好的强化学习，与这些方法形成区别，专注于学习轨迹级别的安全决策。

在**评测类**研究中，相关基准包括AgentHarm（恶意与良性任务）、Agent Security Bench（提示注入和对抗性工具使用）、BFCL（良性任务）和PrivacyLens（隐私泄漏）。这些基准用于评估智能体在多步工具使用中的安全性和效用。本文的工作正是在这些跨领域、分布外的基准上进行评估，证明了其方法的泛化能力。

在**应用类**研究中，近期进展关注智能体推理和工具调用，但往往忽视对安全性、 grounding 或不可逆性的显式检查。本文通过将安全检查和拒绝作为一等公民的显式决策，直接解决了现有应用在长视野行动中安全机制隐含或缺失的问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MOSAIC的后训练框架来解决智能体在多步工具使用中的安全问题。其核心思路是将安全决策显式化、可学习化，并设计了一个结构化的推理循环来引导智能体在关键步骤进行安全检查，从而在必要时拒绝执行。

**整体框架与架构设计**：MOSAIC的核心是一个“规划/思考 → 检查 → 执行/拒绝”的推理循环。智能体在每个步骤首先通过一个“思考”模块生成计划，然后由一个可选的“安全检查”模块评估该计划的风险，最后再选择执行工具调用、直接回答或拒绝行动。这种设计将安全检查提升为一等公民，使其成为智能体决策流程中一个明确的、可训练的环节，而非隐含在一般推理中的副产品。

**主要模块与关键技术**：
1.  **模块化推理块**：系统包含两个核心模块：`\rthink{}`用于规划，`\rsafety{}`用于执行显式的安全检查。安全检查模块评估计划在有害意图、敏感数据处理、权限变更和不可逆影响等多个维度的风险。
2.  **学习型安全门控**：为了平衡安全与效率，MOSAIC引入了一个隐式的学习门控机制。在每个“思考”步骤后，智能体自主决定是否触发安全检查模块。这个决策是通过端到端强化学习从轨迹级反馈中学得的，使得智能体能在高风险步骤进行显式安全推理，而在常规步骤跳过，实现选择性计算。
3.  **显式拒绝作为一等行动**：`\refusal`被设计为一个明确的、带有理由说明的终端行动。这提供了一个可审计的机制来终止不安全的轨迹，防止不安全的中间工具调用产生连锁反应，并为校准的“放弃执行”提供了直接的学习信号。
4.  **基于偏好的强化学习**：针对智能体安全缺乏真实标签的挑战，论文采用基于成对轨迹比较的偏好强化学习（使用GRPO算法）进行端到端训练。具体而言，使用一个LLM作为评判员，对同一任务下的两条完整轨迹进行偏好判断，选择更安全、更合适的一条。这种成对比较能将早期拒绝与后期中止等关键安全差异编码为相对排序，提供了比标量奖励模型更清晰的监督信号。最终优化的复合奖励函数综合了基于偏好的对齐奖励、确保输出格式正确的格式奖励以及控制冗长度的长度惩罚。

**创新点**：
*   **结构化安全推理循环**：将安全检查作为智能体决策流程中一个结构化的、可选的阶段，使安全决策显式化。
*   **学习型选择性安全检查**：通过端到端学习动态决定何时进行显式安全推理，兼顾了安全性与计算效率。
*   **将拒绝优化为一等行动**：将拒绝整合到与工具调用相同的行动空间中并进行优化，而非作为后处理过滤器。
*   **偏好驱动的轨迹级对齐**：利用成对轨迹比较的偏好学习来捕捉标量奖励难以区分的时序性安全差异，提供了更精准的监督信号。

### Q4: 论文做了哪些实验？

论文在实验设置上，使用Agent-SafetyBench数据集进行训练，该数据集包含349个交互环境和约2000个任务实例，涵盖8个安全风险类别和10种常见智能体故障模式。训练采用基于偏好的强化学习，利用LLM作为评判员生成轨迹间的成对安全偏好作为训练信号。实验在配备4块NVIDIA A100 GPU的机器上进行，使用verl库作为强化学习框架，并进行了定制化扩展以支持智能体安全训练。

评估采用了多个分布外基准测试：Agent Security Bench (ASB) 评估对直接和间接提示注入的鲁棒性；AgentHarm (AH) 测量显性恶意行为与良性任务完成情况；BFCL v3 评估良性多轮工具调用的可靠性；PrivacyLens 测试跨域隐私泄漏。对比方法包括前沿闭源模型（GPT-4o, GPT-5）和对应的开源基础模型（Qwen2.5-7B-Instruct, Qwen3-4B-Thinking-2507, Phi-4）。

主要结果显示，MOSAIC框架显著提升了智能体的安全性。对于前沿模型，MOSAIC将有害任务拒绝率从0%提升至90%以上（例如GPT-4o），并将有害分数降低了超过75%（GPT-4o从0.31降至0.07），同时保持了高良性任务完成率（CR: GPT-4o 0.93, GPT-5 0.99）。对于开源模型，MOSAIC带来了模型自适应的增益：Qwen2.5-7B的有害任务分数从0.18降至0.09（降低50%），有害任务拒绝率从0.74提升至0.87；Qwen3-4B-Thinking的良性任务完成率几乎翻倍（ASB CR从0.44提升至0.85）；而过度保守的Phi-4则大幅减少了良性任务拒绝（从0.43降至0.19），并提升了完成率（从0.78至0.91）。在BFCLv3良性工具使用基准上，Qwen2.5的多轮工具调用准确率从21.0%提升至28.5%（+35%）。这些结果表明，MOSAIC能够有效缩小开源模型与未加安全防护的前沿模型之间的安全差距，并通过显式的安全推理和拒绝机制实现模型自适应的安全-效用权衡。

### Q5: 有什么可以进一步探索的点？

该论文提出的MOSAIC框架在提升智能体多步工具使用的安全性方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其训练依赖于人工标注的轨迹偏好对，这在大规模应用时可能面临成本高、一致性难以保证的挑战。未来可探索如何利用合成数据、自监督学习或更高效的弱监督信号来降低对人工标注的依赖。其次，当前方法主要关注“拒绝”这一安全动作，但在复杂场景中，安全策略可能包含更丰富的干预方式，如请求人工确认、切换到安全模式或进行风险缓解操作，未来可设计更细粒度的安全动作空间。此外，论文评估集中于已知的有害任务和注入攻击，对于更隐蔽的、由多步推理间接引发的“涌现性风险”或对抗性工具反馈的长期影响，其泛化能力仍需进一步验证。一个可能的改进方向是引入动态风险估计模块，使智能体不仅能判断当前步骤的安全性，还能预测未来动作序列的潜在风险，从而实现更前瞻性的防护。最后，将安全推理与任务规划更紧密地耦合，而非作为独立检查环节，可能有助于减少安全机制对任务效率的影响，实现安全性与效用的更高层次平衡。

### Q6: 总结一下论文的主要内容

该论文针对智能体语言模型在多步工具调用中的安全问题，提出了一种名为MOSAIC的后训练对齐框架。核心问题是现有对齐方法在序列决策、对抗性工具反馈和过度自信的中间推理场景下容易失效，可能导致不可逆的危害。MOSAIC通过将推理过程结构化为“规划-检查-执行或拒绝”的循环，将安全推理和拒绝作为显式且可学习的一类动作，使安全决策变得明确。方法上，它采用基于偏好的强化学习，利用轨迹对比较来捕捉标量奖励难以区分的细微安全差异，从而无需轨迹级标注即可训练。主要结论显示，MOSAIC在多种模型和分布外基准测试中显著提升了安全性：有害行为减少高达50%，对注入攻击的有害任务拒绝率提升超过20%，同时降低了隐私泄露风险，并保持或改善了良性任务性能。其意义在于为智能体模型的安全部署提供了可泛化、兼顾安全与效用的有效解决方案。
