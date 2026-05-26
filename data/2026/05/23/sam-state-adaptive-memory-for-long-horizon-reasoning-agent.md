---
title: "SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent"
authors:
  - "Yuyang Hu"
  - "Hongjin Qian"
  - "Shuting Wang"
  - "Jiongnan Liu"
  - "Ziliang Zhao"
  - "Jiejun Tan"
  - "Zheng Liu"
  - "Zhicheng Dou"
date: "2026-05-23"
arxiv_id: "2605.24468"
arxiv_url: "https://arxiv.org/abs/2605.24468"
pdf_url: "https://arxiv.org/pdf/2605.24468v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Long-Horizon Reasoning"
  - "State-Adaptive Memory"
  - "Retrieval-Augmented Agent"
  - "Reinforcement Learning for Agent"
  - "Tool-Use Agent"
  - "Web Agent"
  - "Multi-Turn Agent"
relevance_score: 9.5
---

# SAM: State-Adaptive Memory for Long-Horizon Reasoning Agent

## 原始摘要

Long-horizon agentic reasoning requires large language models to act over long interaction histories containing thoughts, tool calls, observations, and partial conclusions. The challenge is not merely that these histories grow long, but that information needed for the current decision may be scattered across distant steps and only become relevant later. Existing approaches address this difficulty by truncating the interaction history, compressing it into shorter surrogates, or retrieving selected parts of it for reuse, but they do not explicitly model how access to past interaction should adapt to the agent's evolving state. We instead cast long-horizon reasoning as a problem of state-adaptive memory. To this end, we propose State-Adaptive Memory~(SAM), a standalone framework that consolidates ongoing interaction into compact memory cues while preserving raw trajectory pages for intent-driven recall. These cues are not treated as replacements for history; rather, they serve as lightweight handles that allow the agent to reconstruct temporally distant information according to its current needs, without retraining the underlying backbone. We further optimize the memory module through expert-guided supervision and reinforcement learning, aligning it with trajectory-level utility. Across BrowseComp, BrowseComp-ZH, WideSearch, and HLE, SAM consistently outperforms strong baselines over diverse agent backbones. Our results suggest that explicit memory modeling provides a simple and effective foundation for long-horizon agentic reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长时程推理智能体（Long-Horizon Agent）在复杂的多步交互任务中，如何有效管理和利用日益增长的历史信息这一核心问题。

**研究背景**：大语言模型（LLMs）被用作智能体执行长时程推理任务时，需要不断与外部环境交互，生成思考、工具调用、观察和部分结论。随着交互历史急剧增长，传统单步生成模式失效，智能体必须从混乱、漫长的历史中恢复有用信息。

**现有方法的不足**：当前主流策略如截断历史、压缩成摘要或检索部分内容，都假设所需信息位于近期或能被充分压缩。然而，长时程轨迹中，关键信息可能分散在远距离步骤，其重要性随任务进展才逐步显现。现有方法未能显式建模智能体“当前状态”如何驱动对“过去信息”的访问需求，导致历史像被动的负担，而非可导航的记忆空间。

**核心问题**：论文提出“状态自适应记忆”（State-Adaptive Memory）概念，核心问题是：如何设计一个独立于智能体主干网络的记忆模型，使智能体能够根据其当前决策意图，从保留的原始轨迹页面中主动重构和恢复时空上遥远的信息，从而实现需求驱动的历史访问，而非基于局部或近期信息的被动压缩与依赖。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是行动空间方法：允许智能体在推理过程中调用上下文编辑操作，将上下文维护转化为策略的习得技能。第二类是损失性替代方法：通过提示或训练的折叠算子、推理时剪枝、RL训练的紧凑内部状态或每轮工作空间重建，用摘要替代历史记录。第三类是历史检索方法：保持历史不压缩，通过密集记忆、静态意图索引或学习的潜在压缩进行检索。与这些不同，SAM将长程推理视为状态自适应记忆问题：它作为一个独立模块，将交互过程整合为紧凑的记忆线索，同时保留原始轨迹页面，使这些线索成为意图驱动检索的轻量级句柄，并通过专家引导监督和轨迹级效用对齐的强化学习进行优化。SAM的核心区别在于：不将记忆线索视为历史替代品，而是允许智能体根据当前状态重建远距离信息，无需重新训练基础模型即可跨多种骨干网络应用。

### Q3: 论文如何解决这个问题？

论文提出了一种名为SAM（State-Adaptive Memory，状态自适应记忆）的独立框架来解决长程推理中的状态变化历史访问问题。核心思想是将交互历史组织成记忆空间，而非作为线性前缀向前携带。整体框架由三个主要组件构成：**页面化情节整合**、**智能体引导的线索选择**和**意图驱动的情节召回**。

首先，**页面化情节整合**将轨迹按token预算划分为连续的页面，保留推理、动作和反馈的局部时序连贯性。对于每个页面，记忆模型生成一个紧凑的**记忆线索**，捕获页面中建立的结论、排除项、未解决问题及未来可能相关的信息。原始页面被移除出活跃上下文，存储到外部页面存储库中，而线索保留在记忆库中。线索并非替代页面，而是作为轻量级句柄，允许后续对原始页面进行访问。

其次，**智能体引导的线索选择**允许推理智能体在需要额外过去信息时，基于当前意图从记忆库中选择候选线索子集。该选择过程不由固定检索分数决定，而是利用线索提供的粗略但持久的过去交互地图，使智能体依据当前状态判断哪些早期页面值得重新访问。

最后，**意图驱动的情节召回**在选定线索后，对应的原始页面被取出，记忆模型根据当前召回意图从中提取最相关的信息，重构出聚焦于当前决策的支持上下文。这区别于简单回放历史或使用摘要替代历史，因为召回内容是基于当前意图从原始页面重建的。

在技术优化上，论文采用**专家引导的监督微调**和**OAT-GRPO**强化学习两步训练策略。监督微调使用前沿大模型生成的专家轨迹作为目标。OAT-GRPO创新性地引入**树结构奖励**，在每次记忆操作处分支成多个样本，实现局部信用分配；并引入**预言机锚定的可恢复性奖励**，通过委员会模型定义目标空间来稠化稀疏的任务成功信号。核心创新在于将长程推理重新定义为一个状态自适应记忆问题，分离了记忆访问与推理策略内部机制，使记忆成为可独立优化的外部能力。

### Q4: 论文做了哪些实验？

论文在四个长程智能体基准测试上评估了提出的SAM方法。实验设置包括：(1) 训练数据由OpenSeeker（11.7K QA对）和OpenResearcher构建，经过过滤去除短轨迹和答案不一致的样本。(2) 评估基准为BrowseComp（长程网页浏览）、BrowseComp-ZH（跨语言多跳搜索）、WideSearch（大搜索空间探索）和HLE（知识密集型科学推理），其中BrowseComp和HLE各采样200题，其余使用完整测试集。(3) 对比方法涵盖三类：基础模型（OpenAI-o3、GPT-5.4等）、开源智能体系统（WebThinker、WebSailor等）和上下文管理基线（无上下文管理、丢弃工具、最近k步、滚动摘要），均与SAM共享相同的智能体主干（GLM-4.7和Qwen3.5-35B-A3B）和推理协议（128K上下文窗口，64K触发管理，avg@3）。主要结果显示：在GLM-4.7主干上，SAM在四个基准上的得分分别为56.5、64.2、38.2和69.2，平均57.0，显著优于最佳启发式基线（summary的54.6）和无管理基线（49.4）；在Qwen3.5上，SAM平均48.8同样领先所有对比方法。SAM在内存需求最大的BrowseComp和BrowseComp-ZH上优势最明显，且同一Qwen3.5-9B记忆模块在不同主干和基准上均表现最佳。

### Q5: 有什么可以进一步探索的点？

**论文局限性与未来方向**

当前SAM虽在长程推理中表现优异，但存在几点可探索的方向：1）**记忆与推理的解耦代价**：当前设计依赖独立的记忆模块（9B-27B参数），虽支持冻结主模型，但额外引入的参数量与推理成本（每轮需检索+交叉注意力）在资源受限场景下仍显冗余，未来可研究记忆模块的轻量化（如蒸馏至1B级）或通过稀疏注意力直接融入主模型。2）**召回机制的粒度限制**：论文指出页面大小在128K时性能下降，说明密集页面稀释了意图信号。可探索自适应分页策略（如依据事件语义密度动态切割），或允许跨页的语义链接（如构建记忆图谱）。3）**多模态与结构化记忆**：当前仅处理文本轨迹，但Agent在实际中常涉及图像、表格等结构化信息。未来可扩展记忆编码器以融合多模态特征，并设计跨模态的检索对齐。4）**训练范式的泛化性**：SFT+GRPO的两阶段训练在GLM-4.7上有效，但在其他架构（如Mamba、RWKV）中是否同样成立？可进一步研究记忆模块与不同主模型架构的协同优化。5）**在线适应与遗忘机制**：当前记忆是累积式增长，但长时间对话中旧记忆可能干扰新决策。引入遗忘曲线或重要性衰减函数（类似人类记忆的“艾宾浩斯遗忘”），可能提升长程鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文提出了状态自适应记忆（SAM）框架，用于解决长程智能体推理中的信息分散问题。核心问题在于，随着交互历史变长，当前决策所需的信息往往散布在遥远的步骤中，现有方法通过截断、压缩或检索历史，但未能根据智能体状态动态调整信息访问。SAM将长程推理视为状态自适应记忆问题，通过将持续交互整合为紧凑记忆线索，并保留原始轨迹页面用于意图驱动的回溯，使智能体能按需重建遥远信息，且无需重新训练基础模型。该方法还通过专家引导监督和强化学习优化记忆模块。在BrowseComp、WideSearch和HLE等基准测试中，SAM在多种智能体骨干网络上持续优于强基线。研究结论表明，显式记忆建模为长程智能体推理提供了简单而有效的通用基础。
