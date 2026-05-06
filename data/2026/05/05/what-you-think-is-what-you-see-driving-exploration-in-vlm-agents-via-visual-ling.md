---
title: "What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity"
authors:
  - "Haoxi Li"
  - "Qinglin Hou"
  - "Jianfei Ma"
  - "Jinxiang Lai"
  - "Tao Han"
  - "Sikai Bai"
  - "Jingcai Guo"
  - "Jie Zhang"
  - "Song Guo"
date: "2026-05-05"
arxiv_id: "2605.03782"
arxiv_url: "https://arxiv.org/abs/2605.03782"
pdf_url: "https://arxiv.org/pdf/2605.03782v1"
categories:
  - "cs.AI"
tags:
  - "VLM Agent"
  - "Curiosity-driven Exploration"
  - "世界模型"
  - "稀疏奖励"
  - "内在探索信号"
  - "视觉-语言对齐"
relevance_score: 8.5
---

# What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity

## 原始摘要

To navigate partially observable visual environments, recent VLM agents increasingly internalize world modeling capabilities into their policies via explicit CoT reasoning, enabling them to mentally simulate futures before acting. However, relying solely on passive reasoning over visited states is insufficient for sparse-reward tasks, as it lacks the epistemic drive to actively uncover the ``known unknown'' required for robust generalization. We ask: Can VLM agents actively find signals that challenge and refine their internal world model through curiosity-driven exploration? In this work, we propose GLANCE, a unified framework that bridges reasoning and exploration by grounding the agent's linguistic world model into the stable visual representations of an evolving target network. Crucially, GLANCE leverages the discrepancy between linguistic prediction and visual reality as an intrinsic curiosity signal within reinforcement learning, steering the agent to actively explore areas where its internal model is uncertain. Extensive experiments across a series of agentic tasks show the effectiveness of GLANCE, and demonstrate that aligning ``what the agent thinks'' with ``what the agent sees'' is key to solving complex or sparse agentic tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决VLM（视觉语言模型）智能体在部分可观察的视觉环境中，面对稀疏奖励任务时缺乏主动探索能力的问题。研究背景是，现有VLM智能体通过强化学习和链式思维推理将世界模型内化到策略中，使其能在行动前进行心理模拟。然而，现有方法存在明显不足：它们主要依赖对已访问状态的被动利用，试图在当前数据分布上优化推理准确性，而非驱动主动探索。这导致智能体在稀疏奖励环境中容易陷入虚假成功——例如，智能体可能完美描述了谜题中的“死胡同”，却未曾意识到应该探索另一条路径。其核心缺陷在于，这种被动解释缺乏认知驱动力，无法主动发现“已知的未知”，从而限制了智能体的鲁棒泛化能力。因此，本文要解决的核心问题是：如何让VLM智能体通过好奇心驱动的探索，主动挖掘那些能够挑战并完善其内部世界模型的信号。为此，论文提出了GLANCE框架，通过将智能体的语言世界模型与不断更新的目标网络的稳定视觉表征对齐，利用语言预测与视觉现实之间的不一致性作为内在好奇心信号，引导智能体主动探索其内部模型不确定的区域，从而突破被动推理的局限。

### Q2: 有哪些相关研究？

相关研究可分为方法类和应用类。在好奇驱动探索领域，传统工作如Prediction Error方法、Competence Maps等通过预测误差作为新奇度指标，在深度强化学习中结合神经网络模块解决稀疏奖励问题，但局限于像素或本体感受域，无法适应VLM代理的语言-视觉语义推理空间。本文GLANCE将好奇机制引入VLM，利用语言预测与视觉现实的不一致作为内在奖励信号。在世界模型方面，传统方法如Dreamer、MuZero在潜在空间学习转移模型进行规划，而LLM时代的方法如RAP、WebDreamer利用大语言模型预测动作结果，但将世界模型视为外部模块或依赖冻结知识。近期的VAGEN通过显式思维链推理将世界模型内化到VLM策略中，但依赖被动监督（如LLM评判器）在已访问状态上优化模型。与上述工作不同，GLANCE将世界建模与好奇驱动探索整合，将推理从被动推断转化为主动探索过程，主动寻求挑战和优化代理的内部信念状态，填补了VLM代理中语义推理与视觉感知对齐的空白。

### Q3: 论文如何解决这个问题？

GLANCE框架通过设计“视觉-语言好奇心”驱动机制，将VLM智能体的语言世界模型转化为探索信号。核心架构包含两条并行流：在线VLM智能体与动量目标网络。在线智能体由视觉编码器和LLM骨干组成，在每轮交互中生成语言假设状态（即Transformer最后一层对应预测token的隐向量），并通过轻量投影器将其映射到视觉空间。动量目标网络则是视觉编码器的指数移动平均版本，对下一观测编码生成稳定的视觉现实表征。关键技术是跨模态预测损失：计算语言假设投影与视觉现实之间的均方误差，作为自监督对齐目标。通过选择性梯度路由，仅更新投影器和在线视觉编码器，冻结LLM参数，既防止语言漂移又让视觉编码器“学习看到智能体所思考的内容”。该预测误差直接作为内在好奇心奖励，与外在奖励结合构成总奖励信号，驱动基于强化学习的策略优化。创新点包括：1）提出“观念即所见”原则，将语言推理的不确定性转化为结构化探索信号；2）设计自适应课程探索机制，通过监测损失变化率，在损失收敛时随机重初始化投影器，迫使智能体重新审视熟悉状态以维持探索动力。

### Q4: 论文做了哪些实验？

论文在5个多样化任务上评估了GLANCE框架，涵盖2D网格谜题(Sokoban、FrozenLake)、3D具身导航(Navigation、PrimitiveSkill)和开发生成推理(SVG重建)。使用Qwen2.5-VL-3B作为统一VLM骨干，对比了VAGEN、VAGEN-Base、Turn-level PPO、GRPO和Vanilla PPO等基线，以及7个现有大视觉语言模型的零样本性能。主要指标为平均成功率(SR，仅目标完成时给予非零奖励)和SVG任务的DreamSim与DINO复合相似度。实验结果表明：GLANCE在所有任务上一致优于仅依赖外部奖励的基线，在稀疏奖励RL设置下整体分数达0.86，显著超过VAGEN-Full；在最具挑战的Sokoban任务中成功率从0.79提升至0.85；PrimitiveSkill中表现突出，验证了好奇心驱动对复杂长程控制的关键作用。消融实验证实：自适应课程重置机制能有效防止内在奖励过早衰减；使用动量目标编码器显著优于直接复制在线网络；本文的自监督内在奖励可作为推理监督的替代信号；探索权重β在[0.1, 0.3]区间达到最佳平衡；计算开销仅增加约10%的边际成本。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面。首先，冻结LLM骨干网络虽避免了语言漂移，但限制了推理逻辑的适应性，未来可探索LoRA等参数高效微调方法，在保持语义稳定性的同时提升世界模型的动态校准能力。其次，轻量MLP投影层形成了信息瓶颈，难以捕捉细粒度的语义-视觉对齐，可尝试Transformer投影器或交叉注意力机制来增强对复杂时空关联的建模。此外，当前奖励完全依赖视觉-语言差异，可能忽视某些无显著视觉落差的认知不确定性，建议引入基于模型置信度的贝叶斯不确定性估计或对抗性样本生成作为辅助信号。更激进的方向是让智能体不仅观察差异，还能主动构建反事实视觉场景来验证假设，形成真正的元认知驱动循环。这类混合内在动机机制可能对稀疏奖励的长期推理任务更具鲁棒性。

### Q6: 总结一下论文的主要内容

论文提出GLANCE框架，解决VLM代理在部分可观测、稀疏奖励环境中的主动探索问题。核心创新在于将代理的语言世界模型与视觉观测间的差异，转化为强化学习中的内在好奇心奖励信号，驱动代理主动探索其内部模型不确定的区域。具体方法通过自监督对齐目标同时优化视觉编码器、提供细粒度内在奖励，并引入自适应课程重置维持长期探索动力。实验表明，GLANCE在多项具身任务中取得显著效果，证明“所想即所见”的对齐策略是解决复杂稀疏奖励任务的关键。该工作将VLM代理从被动推理者转变为主动假检验者，为自主具身发现提供了可扩展的基础路径。
