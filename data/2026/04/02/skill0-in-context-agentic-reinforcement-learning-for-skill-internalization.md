---
title: "SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization"
authors:
  - "Zhengxi Lu"
  - "Zhiyuan Yao"
  - "Jinyang Wu"
  - "Chengcheng Han"
  - "Qi Gu"
  - "Xunliang Cai"
  - "Weiming Lu"
  - "Jun Xiao"
  - "Yueting Zhuang"
  - "Yongliang Shen"
date: "2026-04-02"
arxiv_id: "2604.02268"
arxiv_url: "https://arxiv.org/abs/2604.02268"
pdf_url: "https://arxiv.org/pdf/2604.02268v1"
github_url: "https://github.com/ZJU-REAL/SkillZero"
categories:
  - "cs.LG"
tags:
  - "Agent Training"
  - "Skill Internalization"
  - "In-Context Reinforcement Learning"
  - "Tool Use"
  - "Multi-Turn Planning"
  - "Curriculum Learning"
  - "Parameter-Efficient Adaptation"
  - "Agent Benchmarking"
relevance_score: 9.0
---

# SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization

## 原始摘要

Agent skills, structured packages of procedural knowledge and executable resources that agents dynamically load at inference time, have become a reliable mechanism for augmenting LLM agents. Yet inference-time skill augmentation is fundamentally limited: retrieval noise introduces irrelevant guidance, injected skill content imposes substantial token overhead, and the model never truly acquires the knowledge it merely follows. We ask whether skills can instead be internalized into model parameters, enabling zero-shot autonomous behavior without any runtime skill retrieval. We introduce SKILL0, an in-context reinforcement learning framework designed for skill internalization. SKILL0 introduces a training-time curriculum that begins with full skill context and progressively withdraws it. Skills are grouped offline by category and rendered with interaction history into a compact visual context, teaching he model tool invocation and multi-turn task completion. A Dynamic Curriculum then evaluates each skill file's on-policy helpfulness, retaining only those from which the current policy still benefits within a linearly decaying budget, until the agent operates in a fully zero-shot setting. Extensive agentic experiments demonstrate that SKILL0 achieves substantial improvements over the standard RL baseline (+9.7\% for ALFWorld and +6.6\% for Search-QA), while maintaining a highly efficient context of fewer than 0.5k tokens per step. Our code is available at https://github.com/ZJU-REAL/SkillZero.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型的智能体在技能运用上的根本性局限。研究背景是，随着Claude Code、OpenClaw等智能体框架的出现，结构化的“智能体技能”（即打包好的程序性知识和可执行资源）已成为在推理时扩展智能体专业能力的标准机制。现有主流方法是“推理时技能增强”，即在每一步都从技能库中检索相关技能，并将其作为自然语言指导注入模型的上下文。然而，这种方法存在三个主要不足：首先，检索噪声会引入不相关或误导性的指导，污染智能体的上下文；其次，注入的技能内容会带来显著的令牌开销，在多轮交互中会限制可扩展性；第三，也是最关键的一点，模型仅仅是遵循提示中的技能描述来执行，而非真正学习技能，其能力依赖于外部上下文，并未内化为模型自身的知识。

因此，本文要解决的核心问题是：能否将技能内化到模型参数中，从而在推理时实现无需任何运行时技能检索的零样本自主行为？为此，论文提出了SKILL0框架，这是一个为技能内化而设计的上下文内强化学习框架。它通过一种动态课程学习机制，在训练初期提供完整的技能上下文，然后逐步撤出，最终使智能体在完全零样本（即无技能上下文）的设置下运行，从而将能力从外部上下文系统地转移到模型内部参数中。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于技能的LLM智能体增强方法，可归类如下：

**技能提取与检索方法**：早期基于记忆的方法直接将原始轨迹存入外部数据库供经验回放参考，但存在冗长、冗余和噪声问题。后续研究转向**技能**——一种从历史轨迹中提炼的可重用、抽象化、结构化的行为基元。这些工作聚焦于技能的提取、组织与检索，将技能作为推理时可咨询的情景记忆，并在强化学习框架中提供高效指导。本文与这类工作的关系在于同样利用技能增强智能体，但核心区别在于**目标不同**：现有方法主要依赖运行时检索技能，而本文旨在探索技能能否**内化到模型参数中**，实现零样本自主行为，从而避免检索噪声、令牌开销和知识未真正掌握等问题。

**智能体强化学习（Agentic RL）**：随着LLM强化学习的发展，智能体强化学习已成为赋予LLM智能体强大决策能力的关键后训练方法。本文提出的SKILL0框架属于此类，但引入了**动态课程学习**的创新机制：通过逐步撤除技能上下文，并基于策略帮助性评估筛选技能，最终使智能体在完全零样本环境中运行。

**应用领域**：相关研究涉及代码生成、GUI自动化、游戏玩法和具身控制等开放世界环境。本文的实验在ALFWorld和Search-QA等典型智能体任务上进行验证，证明了方法在提升性能的同时保持高效上下文使用的优势。

### Q3: 论文如何解决这个问题？

论文通过提出SKILL0框架来解决技能内部化问题，其核心方法是一种结合了上下文学习与强化学习的“上下文内强化学习”范式。整体框架旨在通过训练阶段的动态课程学习，逐步将外部技能知识内化到模型参数中，最终实现无需运行时技能检索的零样本自主行为。

架构设计包含几个关键模块：首先是技能管理模块，将技能库组织为层次化结构，包含通用技能和任务特定技能，并以Markdown文件形式存储。其次是上下文渲染机制，为了解决技能和交互历史带来的令牌开销，该机制将文本交互上下文压缩成紧凑的RGB图像，再通过视觉编码器转换为视觉表示作为策略网络的输入。一个创新点是允许策略网络在每一步同时生成任务动作和压缩比率，以实现自适应的上下文压缩。

核心创新点在于其动态课程学习策略，该策略分为两个阶段：离线的相关性驱动技能分组和在线的重要性驱动动态课程。在离线阶段，根据技能类别将验证任务分组，为每个技能文件建立专属的评估子任务。在在线训练阶段，课程被划分为多个渐进阶段，并设定线性衰减的技能预算。在每个阶段，定期评估每个技能文件对当前策略的“帮助性”，即提供技能与不提供技能时在对应验证子任务上的性能差异。只有那些对当前策略仍有正面帮助的技能才会被保留在活动技能子集中，随着技能预算的线性减少，活动技能集逐渐缩小，直至为空，使智能体完全依赖内部化知识。

此外，训练目标采用了复合奖励函数，同时优化任务成功率和上下文压缩效率，并通过近端策略优化等强化学习算法进行策略更新。这种方法确保了策略在技能上下文逐渐撤出的过程中平稳过渡，避免了分布突变，最终实现了技能知识从外部依赖到参数内部化的高效、稳定迁移。

### Q4: 论文做了哪些实验？

论文在ALFWorld和Search-QA两个基准上进行了广泛的智能体实验。实验设置方面，使用Qwen2.5-VL系列模型（3B和7B参数），在4块H800 GPU上进行最多180步的训练。对于ALFWorld，采用GiGPO的数据划分，每批次采样16个任务，每个提示进行8次rollout，最大提示长度为3072个token。对于Search-QA，遵循Search-R1的实验设置，使用E5作为检索器，训练数据来自NQ和HotpotQA，其余数据集用于域外评估，每批次采样128个任务，最大提示长度为4096个token。课程学习设置中，验证子集大小为1000，课程阶段数Ns=3，SkillBank从SkillRL初始化。

对比方法包括：上下文技能提示方法（Zero-Shot, Few-Shot）、基于强化学习的方法（GRPO, AgentOCR, EvolveR, SkillRL），以及在ALFWorld上额外比较的基于提示或记忆的方法（如ReAct, Reflexion, Mem0等），和在Search-QA上比较的搜索增强方法（如Search-R1, ZeroSearch等）。

主要结果与关键指标如下：在ALFWorld上，SKILL0（3B模型）平均成功率达到87.9%，比AgentOCR（78.2%）高出9.7个百分点，同时每步平均上下文token成本仅为0.38k。在Search-QA上，SKILL0（3B模型）平均成功率达到40.8%，比AgentOCR（34.2%）高出6.6个百分点，每步token成本为0.18k。使用7B模型时，SKILL0在ALFWorld和Search-QA上分别达到89.8%和44.4%的成功率，显著优于其他RL基线。此外，SKILL0在无需推理时技能检索的情况下，取得了与甚至优于技能增强方法（如SkillRL）的性能，同时token效率极高（相比SkillRL的2.21k/0.87k token，降低了5倍以上），验证了其成功将技能内化到模型参数中。消融实验进一步证明了动态课程学习与技能预算策略的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于其初始技能库的质量依赖性和离线分组的领域适应性。未来研究可进一步探索以下几个方向：首先，如何实现技能库的动态更新与增量学习，使模型能持续吸收新技能而无需完全重新训练。其次，当前技能分组基于离线相关性，可研究在线自适应分组机制，使技能组织能随任务环境变化而动态调整。此外，论文主要关注工具调用类技能，未来可扩展至更复杂的推理或规划技能的内部化。另一个重要方向是研究多模态技能的内部化，如图像理解或物理交互技能。最后，可探索技能内部化与模型安全性、可控性的平衡，防止内部化技能被误用或产生不可预测的行为。这些方向将推动智能体从工具增强向真正自主的智能系统演进。

### Q6: 总结一下论文的主要内容

这篇论文提出了SKILL0框架，旨在解决当前LLM智能体在推理时动态加载技能（Skill）所面临的三大问题：检索噪声引入无关指导、技能内容注入带来大量token开销，以及模型仅能被动遵循而未能真正内化知识。其核心贡献是设计了一种上下文强化学习（In-Context RL）方法，将技能知识内部化到模型参数中，最终实现无需运行时技能检索的零样本自主行为。

方法上，SKILL0首先将技能按类别离线分组，并将其与交互历史一起渲染成紧凑的视觉上下文，以教导模型工具调用和多轮任务完成。关键创新在于其训练课程（Dynamic Curriculum）：它从提供完整的技能上下文开始，然后根据在线策略评估每个技能文件的有用性，在一个线性衰减的预算内仅保留当前策略仍能受益的技能，逐步撤出技能上下文，直至智能体在完全零样本的环境中运行。

主要结论是，SKILL0在ALFWorld和Search-QA等智能体任务上的实验表明，其性能显著优于标准RL基线（分别提升9.7%和6.6%），同时保持了极高的上下文效率（每步少于0.5k个token）。这证明了通过结构化的课程学习实现技能内部化的可行性，为构建更高效、自主的LLM智能体提供了新路径。
