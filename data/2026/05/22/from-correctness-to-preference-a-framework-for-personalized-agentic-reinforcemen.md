---
title: "From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning"
authors:
  - "Ranxu zhang"
  - "zeyang li"
  - "Jiacheng Huang"
  - "Rui Zhang"
  - "Xiaozhou Xu"
  - "sun zhe"
  - "Yanyong Zhang"
  - "Chao Wang"
date: "2026-05-22"
arxiv_id: "2605.23382"
arxiv_url: "https://arxiv.org/abs/2605.23382"
pdf_url: "https://arxiv.org/pdf/2605.23382v1"
categories:
  - "cs.CL"
tags:
  - "Personalized Agent"
  - "Agentic Reinforcement Learning"
  - "Preference Optimization"
  - "Policy Optimization"
  - "Skill Memory"
  - "Multi-Agent"
relevance_score: 9.0
---

# From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning

## 原始摘要

Agentic reinforcement learning (Agentic RL) has achieved strong progress in tasks with clear success signals. However, many real-world agent applications require user-conditioned behavior: the same query may call for different planning strategies and tool-use decisions across users. This setting raises key challenges: generic rewards cannot capture heterogeneous user preferences, observed behaviors are entangled with conformity effects, and flat memories cannot support personalized skill retrieval. To this end, we propose a unified personalized Agentic RL framework that embeds personalization into training-time optimization. At its core is \emph{Personalized Anchor Reward-Decoupled Policy Optimization} (\textbf{PARPO}), which decouples generic task-quality rewards from personalized preference rewards and uses user-specific anchors to stabilize learning under heterogeneous reward scales. We further introduce a two-stage preference-disentangled reward model and \emph{Preference-Aligned Skill Evolution Graph Memory} (\textbf{PSGM}) for personalized supervision and preference-aligned skill retrieval. Together, they form a closed loop of preference identification, policy optimization, and structured skill accumulation. Experiments on ETAPP, ETAPP-Hard, and SJAgent show that our framework consistently outperforms strong memory and RL baselines. Code and data are included in the supplementary materials.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有智能体强化学习（Agentic RL）在真实世界用户条件化任务中缺乏个性化训练优化框架的问题。研究背景是当前基于大语言模型的Agentic RL在代码生成、网页导航等可验证任务中取得了显著进展，这些任务依赖明确的成功信号（如唯一正确答案）。然而，在电子商务助手、旅行规划等许多实际应用中，最优行为是用户依赖的：相同查询可能对应多个合理轨迹，用户偏好、习惯和约束决定了哪个结果更受欢迎。现有方法的不足主要体现在三个方面：第一，通用奖励只能捕获任务完成质量，无法表达特定用户对同一轨迹的差异化评价，也无法处理不同用户间奖励尺度的异质性；第二，观察到的用户行为常常受到内在兴趣和外部从众效应的纠缠影响，导致个性化偏好信号难以准确识别；第三，现有智能体记忆通常是扁平的、以查询为中心的，无法显式建模用户、意图、技能、工具和轨迹之间的结构化关系，从而无法支持个性化的技能检索。因此，本文的核心问题是构建一个统一的个性化Agentic RL框架，将个性化嵌入到训练时优化中，以同时解决奖励模糊性、偏好解耦和记忆组织这三大挑战。

### Q2: 有哪些相关研究？

相关研究主要分为三类：方法类包括Agentic RL在可验证任务中的进展，如Retool、ToolRL、AutoWebGLM、Search-R1及GRPO系列方法（GRPO、DAPO、GSPO、GiGPO、GDPO），这些方法依赖明确的任务成功信号，而本文则关注用户特定偏好而非通用正确性；在非可验证和开放式优化方面，OpenRubrics和Rubrics as Rewards使用LLM评估和规则监督，但仍优化通用目标而非个性化行为；应用类涉及个性化、偏好和记忆研究，如PersonaAgent、O-Mem、Preference-Aware Memory Update及Learning Personalized Agents from Human Feedback，CoPD研究用户行为中真实兴趣与从众效应的纠缠，而记忆和技能型智能体（如skill-based agents）仅关注推理时个性化。本文的区别在于：首次统一训练时的用户条件策略优化、真实偏好奖励建模和个性化技能检索，形成闭环框架，而非现有工作仅侧重单一环节。评测类方面，本文在ETAPP、ETAPP-Hard和SJAgent基准上验证，而先前研究缺乏此类综合用户条件环境评测。

### Q3: 论文如何解决这个问题？

该论文提出了一个名为PARPO的统一个性化智能体强化学习框架。核心方法是将个性化嵌入训练过程，通过解耦通用任务质量奖励和个性化偏好奖励，并使用用户特定锚点来稳定异构奖励尺度下的学习。

整体架构是一个闭环系统，包括个性化检索、生成、评估和优化。主要模块包括：1) **PARPO策略优化**：采用双轨GRPO风格优势估计器。基础优势用于通用任务质量，遵循标准组内归一化；个性化优势使用用户特定锚点校准，通过指数移动平均维护用户的历史个性化奖励均值和方差，形成稳定的基线。最终优势是两者的加权和，用于PPO风格的裁剪策略目标。2) **两阶段偏好解耦奖励模型**：第一阶段通过多视角注意力机制学习用户画像表示，缓解冷启动问题；第二阶段使用LightGCN从用户-项目交互图中提取协作表示，并分解为兴趣和从众两个分支，通过分支特定目标（如对低流行/高流行项加权）和正交正则化实现偏好解耦。3) **偏好对齐技能演化图记忆**：构建异构知识图谱，将用户、技能、工具等作为节点，通过边编码所有权、兼容性等关系。检索时先进行语义候选搜索，再通过2跳图遍历扩展，最后使用图感知评分函数排序，将偏好相关的技能插入到决策前的上下文中。

创新点在于将奖励解耦、用户锚点基线校准、偏好解耦奖励模型和结构化图记忆有机整合，形成了一个偏好识别、策略优化和技能积累的闭环，有效解决了通用奖励无法捕捉用户异质性偏好、行为受从众效应影响以及扁平记忆无法支持个性化技能检索等关键问题。

### Q4: 论文做了哪些实验？

论文在三个基准上评估了所提框架：ETAPP、其困难版本ETAPP-Hard（覆盖日常生活场景）和SJAgent（基于中国电商平台数据构建的商家决策环境）。实验设置包括与多种基线方法的对比：提示驱动方法（ReAct）、记忆方法（Mem0）、强化学习方法（GRPO、DAPO、GSPO、GiGPO）以及记忆与强化学习结合的方法（MemRL、SkillRL），并报告了GPT-4o和Claude Sonnet 4作为闭源参考。所有开源方法在相同模型规模（Qwen3-4B和Qwen3-8B）、任务设置和工具接口下评估。主要结果以表格形式呈现，显示所提方法在绝大多数指标上超越所有基线，尤其在Judge得分上表现突出（例如在Qwen3-8B的ETAPP上，Judge得分0.8333，而最强基线SkillRL为0.7792）；且通过配对t检验，性能提升在p<0.005水平上显著。消融实验在ETAPP上展开，分三组：A组验证PSGM记忆模块的贡献（去除记忆后Judge得分从0.7708降至0.7006）；B组验证PSGM内部组件（如社区结构、动态图更新等）；C组验证PARPO奖励设计（包括替换为GRPO、移除奖励分支、移除用户锚点等变体），结果表明所有变体均导致性能下降，其中移除兴趣偏好分支和移除顺从性矫正分支分别使Judge得分降至0.7188和0.7214，证实了各组件的必要性。此外还进行了盲审人类评估：在20个个性化ETAPP任务上，15位人类专家和4个LLM裁判从问题相关性、用户相关性和可读性三个维度评分，所提方法在所有维度上获得最高平均分，在用户相关性上领先优势最大。最后，为单独评估RL优化效果（排除记忆和奖励模型影响），对比了GRPO、GSPO、GiGPO和PARPO的训练动态，PARPO在奖励值、训练/验证成功率、工具调用成功率等方面均表现最优，且其在个人化、主动性、过程性和Judge四个奖励维度上的EMA得分均最高，对个人化维度的提升尤为明显。

### Q5: 有什么可以进一步探索的点？

首先，当前人类评估规模过小（仅15名专家、20个样本），未来需扩展到更大规模、更多样化的评估者以验证框架的鲁棒性和泛化性。其次，个性化偏好解耦依赖离线标注，未考虑偏好动态漂移——用户偏好可能随时间或任务难度变化，未来可设计在线偏好学习机制，使奖励模型自适应更新。此外，PSGM的记忆结构目前仅支持技能检索，缺乏对反事实经验的推理（如用户明确不喜欢的工具使用模式），可引入因果推断来区分“用户回避的路径”与“单纯错误的路径”。在算法层面，PARPO使用用户锚点稳定训练，但锚点选取可能引入偏差（如冷启动用户无历史数据），可尝试贝叶斯个性化锚点推断。最后，当前仅在三个基准测试，需探索跨领域（如医疗咨询、金融理财）的迁移能力，并研究多轮交互中用户偏好的隐式反馈建模（如犹豫时间、修改次数）。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个面向个性化智能体强化学习（Agentic RL）的统一框架，解决了传统方法无法处理用户偏好异质性的问题。核心贡献在于将个性化嵌入训练时优化，并提出三个关键组件：**PARPO**（个性化锚点奖励解耦策略优化）将通用任务质量奖励与个性化偏好奖励解耦，并利用用户特定锚点稳定学习；一个两阶段偏好解耦奖励模型用于从行为中分离内在兴趣与外部影响；以及**PSGM**（偏好对齐技能演化图记忆）实现偏好对齐的结构化技能检索。实验在ETAPP、ETAPP-Hard和实际电商平台SJAgent上验证，该方法在保持事实与逻辑质量的同时，显著提升了个性化和过程质量。该工作首次为依赖用户偏好的非确定性任务提供了系统性的训练时优化方案，对开发真正用户中心的智能体具有重要意义。
