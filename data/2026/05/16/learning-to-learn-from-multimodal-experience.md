---
title: "Learning to Learn from Multimodal Experience"
authors:
  - "Xingyu Sui"
  - "Weixiang Zhao"
  - "Yongxin Tang"
  - "Yanyan Zhao"
  - "Yang Wu"
  - "Dandan Tu"
  - "Bing Qin"
date: "2026-05-16"
arxiv_id: "2605.16857"
arxiv_url: "https://arxiv.org/abs/2605.16857"
pdf_url: "https://arxiv.org/pdf/2605.16857v1"
categories:
  - "cs.AI"
tags:
  - "经验驱动学习"
  - "自适应记忆"
  - "多模态智能体"
  - "Agent记忆机制"
  - "交互学习"
relevance_score: 8.5
---

# Learning to Learn from Multimodal Experience

## 原始摘要

Experience-driven learning has emerged as a promising paradigm for enabling agents to improve from interaction trajectories by accumulating and reusing past experience. However, existing approaches are predominantly developed in textual settings and rely on manually designed memory schemas, limiting their applicability to multimodal environments. In real-world scenarios, experience is inherently multimodal, involving heterogeneous signals across perception, reasoning, and action, which makes effective memory design significantly more challenging. In particular, the optimal way to structure and utilize multimodal experience is highly task-dependent and evolves over time, rendering fixed memory designs insufficient. In this work, we propose a new paradigm, learning to learn from multimodal experience, which shifts memory design from a predefined component to an adaptive and learnable process. Our framework enables agents to dynamically construct, organize, and utilize memory based on task requirements and interaction history, effectively learning how to structure experience for improved performance. Experiments demonstrate that adaptive memory design substantially enhances agent performance and generalization across multimodal tasks, highlighting the critical role of learning memory mechanisms in experience-driven learning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多模态环境下经验驱动学习中记忆设计的核心问题。研究背景是，基于经验的学习已成为智能体通过交互轨迹积累和复用经验的重要范式，但现有方法主要局限于文本环境，依赖人工设计的固定记忆模式，难以适应多模态场景。在多模态环境中，经验本身是感知、推理、动作等多模态信号的异构混合，其最优的记忆结构高度依赖任务并随时间动态演化，而传统固定记忆设计要么丢弃关键信息（如细粒度视觉线索），要么引入过多噪声，导致学习效率低下和泛化能力不足。本文提出的核心问题是：如何让智能体不再依赖固定的、由人预设的记忆模式，而是能够自适应地学习如何构建、组织和利用多模态经验。为此，论文提出“从多模态经验中学习如何学习”的新范式，将记忆设计从静态工程决策转变为动态可学习的过程，使智能体能够根据任务需求和交互历史动态优化记忆策略，从而提升性能与泛化能力。

### Q2: 有哪些相关研究？

相关研究可分为两类。第一类是**带记忆的经验学习**，现有方法主要在文本环境中使用预定义记忆模式（如insights、skills、workflows）提取经验。部分工作将记忆扩展到多模态，例如通过视觉信息增强经验提取或使用图结构记忆建模跨模态依赖。但它们仍依赖固定记忆格式，无法适应任务需求变化，本文通过可学习的记忆动态构建机制突破了这一限制。

第二类是**自动记忆设计**，现有工作分为两类：一是在受限设计空间中优化预定义记忆组件组合，二是在开放设计空间中将记忆定义为可执行程序进行优化。然而这些方法局限于纯文本环境，难以泛化到多模态场景。虽然一项并发研究将自动记忆设计扩展到多模态，但主要针对问答任务。本文则提出搜索可执行记忆程序，使记忆机制能根据任务和交互历史自适应调整，从而在多模态任务中实现更好的泛化性。

### Q3: 论文如何解决这个问题？

论文提出了一种名为\methodname的自适应记忆机制框架，旨在解决多模态经验驱动学习中固定记忆设计的局限性。核心思路是将记忆设计从预定义组件转变为可学习、自适应的过程，通过程序搜索自动发现最优的记忆结构。

整体框架包含四个主要阶段：统一接口定义、协议化评估、反射引导变异和树搜索分配。首先，通过定义统一的memo-program接口，将记忆机制封装为包含`update`和`retrieve`两个操作的可执行Python程序，保持外部交互标准化的同时内部机制完全开放。然后，采用更新-检索协议评估每个候选程序：先在更新轨迹集上调用update构建内存状态，再在保留测试任务上调用retrieve获取记忆载荷，由固定执行代理完成任务并计算平均奖励作为验证分数。接着，基于执行证据（包括检索内容、轨迹与分数）进行诊断，识别记忆缺失、冗余或误导向等问题，并由代码生成模型变异父程序产生子代。最后，采用树搜索策略平衡探索与利用，通过UCB分数选择重评估现有程序或生成新程序，并加入最小宽度约束避免路径坍缩。

关键技术包括：统一的多模态记忆接口和episode recorder表示；基于下游奖励的客观评价协议；利用大语言模型进行诊断和代码变异；以及结合局部改进潜力和置信度上界的树搜索优化。该框架的创新点在于将记忆的存储、索引、检索和格式化等能力完全交由程序表示，并通过自动搜索实现端到端的自适应优化。

### Q4: 论文做了哪些实验？

论文在四个多模态基准上评估了方法：GUI/Web导航任务（WebVoyager、Mind2Web）和视觉推理任务（AgentVista、MMSearch-Plus）。采用Qwen3-VL-32B、GPT-5.4-nano及Qwen3.5-Plus作为执行代理骨干，元代理为GPT-5，LLM评判器为GPT-5.4-mini。对比了三类基线：文本基线（Trajectory Retrieval、ReasoningBank、G-Memory）、多模态基线（XSkill、M²）和自动设计基线（ALMA）。所有方法在基准训练集上独立搜索记忆，并在未见测试集上离线评估，报告三次运行的平均分，使用成功率（GUI导航）和评判器准确率（视觉推理）作为指标。结果表明，所提方法在两种执行模型上均优于所有基线。在Qwen3-VL-32B上，方法在WebVoyager（51.84，+15.52）、Mind2Web（45.25，+22.94）、AgentVista（14.36，+3.50）、MMSearch-Plus（11.46，+5.69）上均取得最佳。平均GUI提升19.23分，平均VR提升4.60分。在GPT-5.4-nano上，方法在各基准上分别提升4.41、6.02、2.58、2.51分，平均GUI和VR分别提升5.21、2.55分。跨基准迁移实验显示，搜索到的记忆机制具有良好的可迁移性，但最优性能通常出现在搜索与评估基准一致时。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在以下几个方面：首先，当前方法依赖于预定义的搜索空间和操作原语，这限制了记忆结构的表达能力，未来可探索更灵活的神经符号系统或可微分记忆模块以实现端到端的记忆演化。其次，实验主要聚焦于GUI导航和视觉推理任务，在更复杂的具身交互环境（如机器人操作）和语言粒度的多模态场景中，记忆的时空对齐与长程依赖性建模仍是挑战。改进方向包括引入层次化记忆压缩机制以降低存储开销，以及利用元强化学习框架让记忆更新策略联合优化。此外，当前树搜索的预算控制机制较为粗糙，可设计基于不确定性估计的动态预算分配策略，从而在探索效率与记忆质量之间取得更好平衡。最后，将跨任务迁移的记忆结构进行预训练，并研究记忆组件的可解释性，也是值得探索的方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种从多模态经验中学习的新范式，核心贡献在于将记忆设计从固定的预定义组件转变为可自适应学习的过程。现有方法主要依赖人工设计的固定记忆模式，难以适应任务和环境的动态变化，且多局限于文本场景。作者提出的框架将每个记忆机制表示为可执行的“备忘录程序”，通过迭代评估、反思、变异和预算感知的树搜索，自动探索有效的存储、组织和检索策略。实验表明，该方法在GUI/Web导航和多模态视觉推理任务上显著优于无记忆代理、人工设计记忆基线及纯文本方法。主要结论是，有效的多模态代理学习不仅依赖于更好的基础模型或更大的经验缓冲区，更需要自适应地决定如何结构化和利用经验，这为提升代理的泛化能力和效率提供了新的优化方向。
