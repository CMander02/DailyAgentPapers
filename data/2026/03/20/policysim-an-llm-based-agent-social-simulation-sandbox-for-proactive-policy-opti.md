---
title: "PolicySim: An LLM-Based Agent Social Simulation Sandbox for Proactive Policy Optimization"
authors:
  - "Renhong Huang"
  - "Ning Tang"
  - "Jiarong Xu"
  - "Yuxuan Cao"
  - "Qingqian Tu"
  - "Sheng Guo"
  - "Bo Zheng"
  - "Huiyuan Liu"
  - "Yang Yang"
date: "2026-03-20"
arxiv_id: "2603.19649"
arxiv_url: "https://arxiv.org/abs/2603.19649"
pdf_url: "https://arxiv.org/pdf/2603.19649v1"
categories:
  - "cs.SI"
  - "cs.AI"
tags:
  - "LLM-based Agent"
  - "Social Simulation"
  - "Multi-Agent System"
  - "Policy Optimization"
  - "User Modeling"
  - "Agent Evaluation"
  - "Supervised Fine-Tuning"
  - "Direct Preference Optimization"
relevance_score: 8.0
---

# PolicySim: An LLM-Based Agent Social Simulation Sandbox for Proactive Policy Optimization

## 原始摘要

Social platforms serve as central hubs for information exchange, where user behaviors and platform interventions jointly shape opinions. However, intervention policies like recommendation and content filtering, can unintentionally amplify echo chambers and polarization, posing significant societal risks. Proactively evaluating the impact of such policies is therefore crucial. Existing approaches primarily rely on reactive online A/B testing, where risks are identified only after deployment, making risk identification delayed and costly. LLM-based social simulations offer a promising pre-deployment alternative, but current methods fall short in realistically modeling platform interventions and incorporating feedback from the platform. Bridging these gaps is essential for building actionable frameworks to assess and optimize platform policies. To this end, we propose PolicySim, an LLM-based social simulation sandbox for the proactive assessment and optimization of intervention policies. PolicySim models the bidirectional dynamics between user behavior and platform interventions through two key components: (1) a user agent module refined via supervised fine-tuning (SFT) and direct preference optimization (DPO) to achieve platform-specific behavioral realism; and (2) an adaptive intervention module that employs a contextual bandit with message passing to capture dynamic network structures. Experiments show that PolicySim can accurately simulate platform ecosystems at both micro and macro levels and support effective intervention policy.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决社交平台干预政策（如推荐、内容过滤）在部署前难以评估其潜在社会风险的问题。当前，平台主要依赖部署后的A/B测试来评估政策效果，这种方法具有反应性、延迟性，且可能带来不可控的社会危害（如加剧回声室效应和极化）。近年来，基于大语言模型（LLM）的社会模拟为事前评估提供了新思路，但现有模拟方法存在明显不足：它们通常未明确建模平台干预机制，智能体行为设计依赖提示工程而缺乏真实平台行为数据支撑，且缺乏利用模拟反馈来优化现实政策的机制。

因此，本文的核心问题是：如何构建一个高保真、可操作的LLM多智能体社会模拟沙盒，以主动、安全地评估和优化平台干预政策，从而在部署前系统性地预测并缓解其可能引发的负面社会影响。为此，论文提出了PolicySim框架，它通过整合经监督微调（SFT）和直接偏好优化（DPO）训练的用户智能体模块来提升行为真实性，并引入基于上下文赌博机与消息传递的自适应干预模块，以捕获动态网络并优化政策，最终实现政策的事前评估与迭代优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：传统社会模拟方法、基于LLM的智能体模拟框架，以及面向平台干预策略优化的研究。

**1. 传统社会模拟与基于LLM的模拟方法**：传统方法如基于智能体的模型（Agent-Based Models）已被广泛用于研究意见动态、经济系统等复杂社会现象。近年来，随着大语言模型的发展，出现了如Oasis、HiSim等LLM驱动的多智能体社会模拟框架。这些工作为模拟社会互动提供了基础。然而，如论文所述，现有模拟大多**未明确建模平台干预策略**（如推荐、内容过滤），且智能体行为设计严重依赖提示工程，缺乏对真实社交媒体行为的忠实模拟，限制了结果的可信度。PolicySim通过引入专门的干预策略模块和基于SFT与DPO训练的用户智能体，旨在弥补这些不足。

**2. 平台干预策略的评估与优化方法**：当前主流方法是**在线A/B测试**，它需要在真实环境中部署策略并收集反馈，属于被动、事后评估，存在风险识别延迟、成本高且可能造成不可逆危害的问题。PolicySim的核心贡献在于提出了一种**主动的、部署前的评估与优化沙箱**，通过模拟中的反馈循环来优化策略，这与被动式的A/B测试形成鲜明对比。

**3. 特定领域的模拟与推荐系统研究**：部分工作如Agent4rec专注于电影推荐等特定领域的模拟，但通常规模有限或未考虑动态社交网络与自适应干预。论文中的对比表格（对比Oasis、Agent4rec、HiSim、Stopia等）清晰展示了PolicySim的差异：它同时具备大规模智能体（1000）、动态关系演化、明确的干预策略建模、自适应优化能力，并基于真实平台（X和微博）环境，从而构建了一个更全面、可操作的评估框架。

总之，PolicySim在继承LLM社会模拟方向的同时，关键创新在于**系统性地整合了高保真用户行为建模与自适应平台干预策略的闭环优化**，填补了现有工作在平台干预建模、行为真实性和利用模拟反馈进行策略优化方面的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为PolicySim的、基于大语言模型（LLM）的社交模拟沙盒，来主动评估和优化平台干预政策。其核心方法是模拟用户行为与平台干预之间的双向动态，从而在部署前预测政策影响，避免传统A/B测试的滞后与高风险。

整体框架由两大核心模块构成：用户代理模块和干预政策模块。用户代理模块负责生成逼真的用户行为。它包含用户画像、记忆、用户关系和行为模型等组件。为了提升真实性，论文创新性地采用了两阶段训练策略：首先通过监督微调（SFT）利用平台真实数据（事件、用户、行为）对LLM进行初始化；随后使用直接偏好优化（DPO）进一步对齐代理行为与真实社交行为偏好，确保风格和行为的一致性。此外，代理在每轮模拟中可执行多种行为（如发帖、转发、关注），并拥有结合短期与长期记忆的机制，通过语义相关性和时间衰减进行信息检索，从而模拟动态、有依赖性的用户决策。

干预政策模块则实例化了典型的平台机制，如推荐系统和曝光控制。其关键创新在于采用了**自适应干预策略**，将政策优化形式化为一个强化学习问题，并具体通过**上下文多臂老虎机**框架实现。该模块定义了依赖于政策类型的动作空间（如用户-帖子对或用户-概率对），并为每个“臂”（即候选动作）设计了融合用户画像、近期记忆并通过图上的消息传播聚合了社交网络影响的上下文嵌入。奖励函数则根据干预目标（如促进跨观点互动或抑制虚假信息）动态计算，量化政策效果。

最终，优化过程通过一个神经网络来利用已知知识预测奖励，同时用另一个网络估计探索的潜在收益，通过综合两者得分来平衡利用与探索，从而在模拟环境中自适应地迭代优化干预政策。整个沙盒通过目标奖励评估组件闭环运行，实现了对平台生态系统微观与宏观层面的准确模拟，并为政策优化提供了可操作的反馈。

### Q4: 论文做了哪些实验？

论文的实验分为两个主要阶段：一是评估社会模拟的真实性，二是评估自适应干预策略的有效性。

**实验设置与数据集**：实验使用了真实社交媒体数据集，主要包括TwiBot-20（包含229K用户、33.5M推文和456K关注链接）和微博数据集（附录中详述）。用户代理基于Qwen2.5-3B-Instruct模型，通过LoRA（秩为64）进行监督微调（SFT）和直接偏好优化（DPO），学习率为1e-6，批量大小为256。实验在12块NVIDIA A100 GPU上进行。

**对比方法**：在模拟真实性评估中，对比了多个开源LLM骨干模型（如GLM4-light、Llama-3-8B-Instruct、Qwen2.5系列）以及PolicySim的消融变体（如无用户画像生成的Ours-φ、仅SFT的Ours-SFT、仅DPO的Ours-DPO）。在干预策略评估中，对比了ε-greedy和UCB上下文赌博机基线方法。

**主要结果与关键指标**：
1.  **微观层面模拟真实性**：PolicySim在多项指标上表现最佳。内容质量方面，BERTScore F1达到58.05，BertSim达到88.06。行为对齐准确率为65.56%，较随机和骨干基线提升8.26%。自我一致性准确率为56.00%。社交能力方面，参与度（Engagement）得分为3.20（1-4分制），鲁棒性（Robustness）得分为2.73。实验表明，用户画像模块对塑造个性化行为至关重要，且SFT是DPO获得最优性能的必要基础。
2.  **宏观层面意见动态**：模拟通过按时间顺序注入触发新闻事件（如反堕胎立法相关新闻），成功复现了公众立场的演变轨迹，并观察到立场标准差随时间增加，表明出现了极化效应。当应用干预策略（如推荐系统）时，极化现象加剧。
3.  **自适应干预策略效果**：在多个优化目标下评估策略。例如，在目标1（减少毒性、增加跨群体互动等）下，PolicySim将毒性分数降至0.0386（最佳），并将跨群体互动提升至0.56。在目标2（减少错误信息传播）下，将错误信息比率降至24%，优于ε-greedy（26%）和UCB（30%）基线。

### Q5: 有什么可以进一步探索的点？

本文提出的PolicySim框架在利用大语言模型进行政策模拟方面迈出了重要一步，但其仍有若干局限性和值得探索的方向。首先，模拟的真实性高度依赖于基础LLM的能力和训练数据的质量，可能存在分布外泛化不足的问题，未来可探索结合更复杂的多模态数据或引入世界模型来增强对复杂社会动态的捕捉。其次，当前模块（如上下文赌博机）可能过于简化平台复杂的实时决策逻辑，未来可集成更强大的强化学习或基于扩散模型的决策器来优化长期策略。此外，研究主要关注已知的“回音室”等风险，对于政策可能引发的未知、涌现性社会效应（如突发性舆论转向）模拟能力有限，需开发更开放的风险探测机制。最后，将模拟结果安全、可信地转化为实际平台的操作指南仍是一个挑战，需要建立与真实A/B测试平台更紧密的闭环验证系统，并深入研究模拟环境与真实世界之间的因果迁移规律。

### Q6: 总结一下论文的主要内容

本文提出PolicySim，一个基于大语言模型（LLM）的智能体社会模拟沙箱，旨在对社交平台的干预政策（如推荐、内容过滤）进行主动评估与优化。核心问题是现有方法主要依赖部署后的在线A/B测试，风险识别滞后且成本高，而现有的LLM模拟方法又难以真实建模平台干预及平台反馈的动态双向影响。

为此，PolicySim通过两个关键组件建模用户行为与平台干预间的双向动态：其一，用户智能体模块，结合监督微调（SFT）和直接偏好优化（DPO）进行精调，以实现针对特定平台的行为真实性；其二，自适应干预模块，采用结合消息传递的上下文赌博机方法，以捕捉动态网络结构并模拟平台决策。

实验表明，PolicySim能在微观（个体行为）和宏观（生态系统）层面准确模拟平台生态，并支持对干预策略的有效测试与优化。其核心贡献在于构建了一个可操作的、部署前的评估框架，为主动识别和缓解政策可能引发的回声室、极化等社会风险提供了新途径。
