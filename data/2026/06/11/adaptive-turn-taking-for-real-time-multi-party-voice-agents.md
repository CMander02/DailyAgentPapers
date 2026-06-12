---
title: "Adaptive Turn-Taking for Real-time Multi-Party Voice Agents"
authors:
  - "Soumyajit Mitra"
  - "Prabhat Pandey"
  - "Abhinav Jain"
  - "Shanmukha Sahith"
  - "K V Vijay Girish"
date: "2026-06-11"
arxiv_id: "2606.13544"
arxiv_url: "https://arxiv.org/abs/2606.13544"
pdf_url: "https://arxiv.org/pdf/2606.13544v1"
categories:
  - "eess.AS"
  - "cs.AI"
  - "cs.CL"
tags:
  - "语音Agent"
  - "多智能体交互"
  - "对话管理"
  - "多轮对话"
  - "角色条件化"
  - "推理增强"
  - "合成数据集"
  - "实时对话系统"
relevance_score: 8.5
---

# Adaptive Turn-Taking for Real-time Multi-Party Voice Agents

## 原始摘要

Turn-taking in multi-party spoken conversations remains a fundamental challenge for voice-based agents, particularly under dynamic floor competition and varying user expectations. We propose ModeratorLM, a role-playing voice agent that conditions turn-taking behavior on an explicitly assigned role in multi-party settings. The system is built on a speech large language model operating in chunk-wise streaming manner. We further introduce a reasoning-augmented variant that incorporates chain-of-thought reasoning over conversational context and the assigned role. We construct RolePlayConv, a large-scale synthetic dataset of spoken multi-party conversations with diverse assistant roles. Experiments on real-world meeting data and RolePlayConv show improved turn-taking precision by over 40% and recall by more than 70%, while substantially reducing false-positive interruptions compared to non-role-conditioned baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多轮语音对话中智能体的动态轮流发言问题。研究背景是当前语音对话系统（如全双工智能体）在两人对话中能通过暂停时长、沉默检测等声学线索进行有效轮流发言，但这些方法在多轮对话场景下表现不佳。现有方法的不足在于：多轮对话存在重叠语音、动态争夺发言权、以及需要协商分配发言顺序等复杂交互，智能体不仅要决定何时发言，还要判断是否应该介入；同时，用户对智能体角色（如被动听众或主动协调者）的期望因场景而异，但现有角色扮演语言代理主要聚焦于文本对话中的语言风格、性格特征等，忽略了在语音交互中角色对实时轮流发言行为的影响。本文提出的核心问题是：如何让语音智能体根据明确分配的角色，在多轮多人对话中自适应地调整轮流发言行为（即何时及如何介入对话），从而减少虚假打断、提升角色一致的发言决策与响应生成。为此，本文设计了ModeratorLM系统，通过基于语音大模型的流式处理，结合角色条件化与推理增强机制，首次在语音领域实现角色感知的多轮对话轮流发言控制。

### Q2: 有哪些相关研究？

基于论文内容，相关研究可归纳为以下类别：

**1. 对话系统与全双工代理**：现有工作聚焦于低延迟流式语音处理（如streaming speech modules）和全双工交互（如backchannel、barge-in），但主要局限于双人对话（dyadic），依赖暂停时长、静音检测等声学线索。本文将其扩展至多人场景，提出了角色条件化的轮次控制。

**2. 角色扮演语言代理（RLPA）**：已有研究探索基于文本的多人对话角色扮演（如persona adoption、character traits），但忽略了角色对实时语音轮次行为的影响。本文首次将角色条件引入语音代理，并通过显式角色分配控制干预时机和内容。

**3. 评测与数据集**：现有基准主要针对双人对话轮次评估，而本文构建了大规模合成数据集RolePlayConv，覆盖多种辅助角色（如主持人、书记员），填补了多人角色化语音对话数据的空白。

**4. 推理增强方法**：本文的ModeratorLM-Think在语音大语言模型上引入了链式思考（chain-of-thought reasoning），在对话上下文和角色约束下生成推理轨迹，显著提升了角色对齐的轮次决策，区别于仅依赖端到端预测的基线。

### Q3: 论文如何解决这个问题？

论文通过提出ModeratorLM系统来解决多方语音对话中的轮次转换挑战。核心方法是一个基于语音大语言模型的流式架构，将轮次转换决策完全委托给模型本身，摒弃了传统的独立语音活动检测模块。系统由语音编码器和骨干大语言模型组成，语音编码器独立处理每个音频块并生成块级嵌入，通过可训练的线性投影层映射到大语言模型嵌入空间。多通道音频先下混为单通道信号，然后以流式方式将块级语音嵌入顺序附加到大语言模型上下文。训练时采用动态大小的音频块，每个块对应的文本转录（含说话人标注）与语音嵌入共同作为输入。大语言模型为每个音频块输出两种类型：轮次转换+响应（生成控制标记和助理文本回复）或不轮次（空序列）。关键技术包括：引入推理增强变体ModeratorLM-Think，在潜在轮次转换点执行思维链推理；构建大规模合成多方对话数据集RolePlayConv，包含125种详细助理角色及其属性，通过多阶段流水线生成覆盖3-6个说话人的对话，并利用Zonos-v0.1 TTS模型合成为语音。创新点在于明确将轮次转换行为条件化为显式分配的角色，并通过动态音频块训练和推理增强显著提升转接精度（超过40%）和召回率（超过70%），同时大幅降低误报中断。

### Q4: 论文做了哪些实验？

论文在真实会议数据集NOTSOFAR-1(NSF-1)和合成的多轮对话数据集RolePlayConv上评估了ModeratorLM及其推理增强变体ModeratorLM-Think。实验对比了两个非角色条件化的基线：Moshi（双人对话模型）和MP-Baseline（无角色条件下在RolePlayConv上微调）。主要结果包括：在NSF-1和RolePlayConv上，ModeratorLM相比基线将轮换精度提升超过40%，召回率提升超过70%，并显著降低了误报率。在RolePlayConv上，ModeratorLM的精确度为0.71、召回率0.57、宏平均准确度0.76；ModeratorLM-Think的精确度为0.79、召回率0.82、宏平均准确度0.91，表明链式推理有效改善了保守轮换问题。基于LLM裁判（Claude-Sonnet-3.5）的角色忠诚度评估中，ModerLM-Think的轮换得分0.72、响应得分7.4，高于ModeratorLM（0.68, 6.9）和MP-Baseline（0.58, 4.6）。消融实验显示，固定分块（2秒）提升了ModeratorLM的精度（0.88）和召回率（0.78），但现实应用中缺乏边界信息；ModeratorLM-Think对分块策略更鲁棒。无文本输入时性能严重下降（精确度0.39-0.42，召回率0.14-0.42），使用ASR假设时仅轻微退化（精确度0.75，召回率0.80），表明模型依赖文本信息但能容忍转录误差。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其依赖合成数据集进行训练，可能未完全覆盖真实多轮对话的复杂性和噪声干扰。此外，系统基于分块流式处理，可能在高频轮替场景中产生延迟或误判。未来可探索全双工多智能体架构，支持同时聆听与发言的实时交互；引入动态优先级机制，根据用户语气、语义紧迫性自适应调整抢占策略；或将强化学习与角色约束结合，通过奖励函数优化长尾场景下的轮替平衡。另外，当前CoT推理的显式计算可能增加延迟，可尝试轻量化隐式推理模块，或采用时序因果注意力来建模上下文与角色的联合影响。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种面向多人群聊场景的角色驱动语音智能体ModeratorLM，旨在解决基于语音的智能体在动态发言权竞争和用户期望差异下的自适应话权切换问题。系统基于分块流式处理的语音大语言模型，通过显式分配角色（如主持人、参与者）来调节话权切换行为。作者还引入了推理增强变体，利用链式思维对对话上下文和角色进行推理。为训练模型，他们构建了大规模合成多轮多人语音对话数据集RolePlayConv。在真实会议数据和合成数据集上的实验表明，相比无角色条件的基线模型，该方法在话权切换精确率上提升超过40%，召回率提升超过70%，同时显著减少了误中断。该工作的核心贡献在于将角色感知与推理能力融入语音对话系统，实现了更自然、更符合用户预期的多人实时话权管理。
