---
title: "CollabBench: Benchmarking and Unleashing Collaborative Ability of LLMs with Diverse Players via Proactive Engagement"
authors:
  - "Hong Qian"
  - "Yuanhao Liu"
  - "Zihan Zhou"
  - "Zongbao Zhang"
  - "Hanjie Ge"
  - "Haotian Shi"
  - "Liang Dou"
  - "Xiangfeng Wang"
  - "Jingwen Yang"
  - "Aimin Zhou"
date: "2026-06-04"
arxiv_id: "2606.05793"
arxiv_url: "https://arxiv.org/abs/2606.05793"
pdf_url: "https://arxiv.org/pdf/2606.05793v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.CY"
  - "cs.LG"
tags:
  - "LLM Agent 协作"
  - "多智能体系统"
  - "基准评测"
  - "协作行为建模"
  - "主动交互"
  - "游戏环境"
relevance_score: 8.5
---

# CollabBench: Benchmarking and Unleashing Collaborative Ability of LLMs with Diverse Players via Proactive Engagement

## 原始摘要

While LLM-based agents excel at individual tasks, effective collaboration with realistic human partners remains challenging. Most of the existing conversation-level collaborative studies lack grounded interaction and behavioral execution, motivating the need for cooperative game environments that enable contextualized and immersive collaboration. To this end, this paper proposes CollabBench, a benchmark for evaluating and training collaborative agents in cooperative games. CollabBench features a Diverse Player Profile Simulation pipeline to model varied players behaviors, and a Collaborative Agentic Training paradigm that unifies reasoning, communication, and action via agentic rollouts, optimized with a hybrid reward balancing task efficiency and affective adaptation. We further extend classic environments to CWAH-MultiPlayer and Cook-MultiPlayer for systematic evaluation under diverse personalities. Experiments with efficiency and affective metrics show that our trained models outperform base models, achieving 19.5% higher efficiency and 24.4% improved affective performance. Further analysis reveals key collaborative limitations of existing models and offers insights for future collaborative training.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有基于大语言模型（LLM）的智能体在与多样化人类伙伴进行有效协作时面临的三大核心挑战。研究背景是，尽管LLM智能体在深度研究、数学推理等独立任务上表现出色，但在需要实时行动和情境感知的协作场景中表现不佳。现有方法的不足主要体现在三个方面：第一，大多数关于人机协作的研究停留在对话层面（如文档编辑、数学问题求解），缺乏基于共享环境的接地交互和行为执行，导致协作脱离即时情境；第二，现有方法难以在游戏等强上下文环境中模拟具有不同个性和行为风格的人类伙伴，已有的角色扮演和用户建模方法依赖静态数据，无法捕捉行动层面的动态行为；第三，评估指标过于单一，仅关注任务效率（如游戏得分），忽视了帮助性、信任感和共情等社交情感维度，而这些对高质量人机协作至关重要。为此，本文提出了CollabBench基准，其核心目标是：通过构建基于大五人格理论的多样化玩家模拟管道，提出融合推理、沟通和行动的协作智能体训练范式，并引入兼顾效率与情感的混合奖励机制，最终系统性地评估和提升LLM智能体在合作游戏中与不同伙伴主动协作的能力。

### Q2: 有哪些相关研究？

相关研究主要分为三类：

1. **个性感知人类模拟**：传统方法依赖行为数据学习模拟器，近期工作利用LLM基于预定义描述生成多样化角色。但本文指出，现有工作缺乏面向合作游戏场景的多样化、具身化行为数据，且对话级模拟器个性多样性有限，难以直接迁移到合作游戏任务。CollabBench通过引入多样化的玩家画像模拟管线（Diverse Player Profile Simulation Pipeline），弥补了这一空白。

2. **基于代理训练的LLM游戏方法**：现有研究（如VOYAGER、RAGEN、AgentGym-RL）主要关注通过架构设计或强化学习增强单代理能力，而协作代理研究（如ProAgent、CoELA）多为架构中心化、缺乏明确的协作意识训练机制。本文提出统一的推理-通信-行动代理展开范式（Collaborative Agentic Training），并引入混合奖励平衡任务效率与情感适应，直接针对协作意识优化。

3. **LLM代理与人类协作评估**：近期工作开始使用多维评估（如LLM-as-a-judge评估交互性与共情），但基于游戏的评估仍偏重效率指标（游戏得分、成功率）。CollabBench扩展了CWAH-MultiPlayer和Cook-MultiPlayer环境，同时采用效率与情感指标进行系统化评估，克服了现有评估协议缺乏规模化和可扩展性的局限。

### Q3: 论文如何解决这个问题？

该论文通过构建一套完整的训练与评估框架来解决LLM协作能力不足的问题。整体框架包括三个核心部分。首先，为了解决真实人类交互数据稀缺的问题，提出了多样玩家画像模拟流水线。该流水线基于大五人格理论创建人格驱动玩家画像，并利用多个LLM通过ReAct机制生成多样化行为轨迹，再通过聚类、LLM总结和交互过滤建立高保真人格-行为映射，最终得到能忠实模拟不同个性玩家的P_sim集合。其次，设计了协作智能体训练范式。其核心创新是将推理、通信与行动在单个rollout中统一输出为<think>、<message>、<action>结构，这降低了延迟并促进了对通信与行动的联合推理。同时，该范式引入了混合奖励机制，包含一个稀疏的轨迹级效率奖励和一个稠密的步级情感奖励。步级情感奖励由格式、通信和交互性三个子奖励构成，其中交互性奖励采用LLM评估器基于伙伴画像来判断协作质量。为了联合优化这两种奖励，论文采用了GIGPO算法，该GRPO变体通过构建层级优势估计，将全局任务效率优势与局部情感交互优势相结合，以指导策略更新。最后，将经典环境扩展到CWAH-MultiPlayer和Cook-MultiPlayer，并设计了CB-Efficiency和CB-Affective两维评估指标。实验证明，训练后的模型较基础模型在效率（19.5%）和情感表现（24.4%）上均有显著提升。

### Q4: 论文做了哪些实验？

论文在CollabBench上进行了多项实验。实验设置方面，基于CWAH-MultiPlayer和Cook-MultiPlayer两个合作游戏环境，使用DeepSeek-V3.1作为队友模拟器，以CoELA和ProAgent为智能体框架。基准模型包括GPT-5.2、DeepSeek-V3.1和Qwen2.5-72B-Instruct。主要实验结果：1) 训练后的Qwen2.5-7B-Instruct在效率和情感指标上分别提升19.5%和24.4%；2) 当前主流模型在平衡效率与情感协作方面存在局限，情感表现较弱；3) 在CWAH-MultiPlayer中，不同LLM间的游戏得分Pearson相关系数达0.821，表明基准具有鲁棒性；4) t-SNE可视化显示CollabBench覆盖更多交互模式，体现高多样性。消融实验表明，移除情感奖励或角色设定会导致情感表现大幅下降。用户研究（15名参与者）显示，完全训练模型在帮助性、可信度和共情维度上均显著优于基线模型，而移除情感奖励的模型被描述为“高效但冷漠”。

### Q5: 有什么可以进一步探索的点？

CollabBench在沉浸式玩家模拟和情感化协作训练方面仍有显著探索空间。当前利用LLM生成多样玩家行为虽具可扩展性，但“具身化”行为与自我认知、人格的一致性尚浅。未来可引入强化学习或MBTI等成熟人格框架，使模拟角色的游戏内行动与语言交流更协调统一，从而更逼近真实人类协作的复杂性。此外，现有LLM在任务效率与玩家体验间存在持续的能力缺口，模型常出现模式化、低信息密度的沟通，且难以平衡情感优化中的奖励黑客问题。改进方向包括：设计更精细的、能奖励真正信息增益而非单纯高频接触的通信-动作联合奖励函数；或借鉴多智能体协同中的通信协议学习，让模型在交互中动态习得何时、如何与不同人格类型的队友进行高效且富有同理心的沟通。探索将元学习或在线适应机制融入训练，使协作智能体能在与未见过的玩家配置协作时，快速调整其策略与沟通风格，将有效提升其泛化鲁棒性。

### Q6: 总结一下论文的主要内容

CollabBench提出了一个评估和训练大语言模型协作能力的基准，聚焦于解决现有研究缺乏沉浸式、有行为执行的协作环境问题。该工作首先通过多样化玩家画像模拟管道，基于大五人格理论生成具有不同行为模式的虚拟玩家，并将经典环境扩展为CWAH-MultiPlayer和Cook-MultiPlayer，以支持多玩家协作评估。为训练协作智能体，论文提出协作智能体训练范式，通过智能体回滚统一推理、沟通和行动，并采用混合奖励机制同时优化任务效率和情感适应。实验表明，该训练使模型在效率指标上提升19.5%，在帮助性、信任度和共情等情感指标上提升24.4%。该工作揭示了现有模型在协作中的局限性，并为未来人机协作训练提供了方向。
