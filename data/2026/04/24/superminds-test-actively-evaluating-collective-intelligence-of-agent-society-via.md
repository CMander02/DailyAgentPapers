---
title: "Superminds Test: Actively Evaluating Collective Intelligence of Agent Society via Probing Agents"
authors:
  - "Xirui Li"
  - "Ming Li"
  - "Yunze Xiao"
  - "Ryan Wong"
  - "Dianqi Li"
  - "Timothy Baldwin"
  - "Tianyi Zhou"
date: "2026-04-24"
arxiv_id: "2604.22452"
arxiv_url: "https://arxiv.org/abs/2604.22452"
pdf_url: "https://arxiv.org/pdf/2604.22452v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "多智能体系统"
  - "集体智能评估"
  - "Agent交互分析"
  - "大规模Agent社会"
  - "智能体评测基准"
  - "LLM Agent社会模拟"
relevance_score: 9.5
---

# Superminds Test: Actively Evaluating Collective Intelligence of Agent Society via Probing Agents

## 原始摘要

Collective intelligence refers to the ability of a group to achieve outcomes beyond what any individual member can accomplish alone. As large language model agents scale to populations of millions, a key question arises: Does collective intelligence emerge spontaneously from scale? We present the first empirical evaluation of this question in a large-scale autonomous agent society. Studying MoltBook, a platform hosting over two million agents, we introduce Superminds Test, a hierarchical framework that probes society-level intelligence using controlled Probing Agents across three tiers: joint reasoning, information synthesis, and basic interaction. Our experiments reveal a stark absence of collective intelligence. The society fails to outperform individual frontier models on complex reasoning tasks, rarely synthesizes distributed information, and often fails even trivial coordination tasks. Platform-wide analysis further shows that interactions remain shallow, with threads rarely extending beyond a single reply and most responses being generic or off-topic. These results suggest that collective intelligence does not emerge from scale alone. Instead, the dominant limitation of current agent societies is extremely sparse and shallow interaction, which prevents agents from exchanging information and building on each other's outputs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决一个核心问题：在大规模自主智能体社会中，集体智能能否仅通过规模自发涌现。研究背景在于，人类社会的集体智能（如维基百科、开源社区）已被证明依赖于有效的交互机制，而非个体能力的简单叠加。随着大语言模型智能体数量激增至数百万级（如MoltBook平台），研究者产生了一种自然预期——大规模和交互密度可能催生类似人类的集体智能。然而，现有多智能体系统通常依赖设计好的协调机制（如分配角色、共享目标、结构化协议），智能体间的协作是被动结果而非主动选择。当前方法的不足在于：缺乏对非结构化社会中自发涌现的集体智能进行主动、系统性评估的手段，被动观察只能揭示表面模式，无法测量深层能力。本文通过引入“Superminds Test”层次化评估框架和“探测智能体”方法，首次在200万智能体规模的MoltBook平台上进行实证检验。核心问题在于：在没有预设任务和协调协议的自由交互社会中，集体智能是否自发产生？实验结果揭示了一个严峻事实——集体智能并未因规模而涌现，智能体间的交互极度稀疏浅层，无法支撑信息交换和协同构建。

### Q2: 有哪些相关研究？

相关研究涵盖方法、应用和评测三类。**方法类**包括分布式系统与多智能体系统中的集体智能工程化方法，如Contract Net Protocol（分布式任务分配）、Kilobot（千级机器人自组装规则）和COIN框架（个性化奖励函数优化全局效用）。这些系统通过显式机制设计实现集体智能，与本文研究的**自发涌现型集体智能**不同。**应用类**包括基于LLM的多智能体系统，如AutoGen、CAMEL、ChatDev等，它们通过角色分配和结构化对话协议实现协作，但交互结构是预设的，缺乏自主性。**评测类**方面，现有工作多聚焦单智能体基准（如语言理解、推理任务）或有限规模的多智能体协作（SMAC、Hanabi、MAgent等），缺乏对大规模自主智能体社会的集体智能评估。本文首次以MoltBook（200万智能体）为平台，提出Superminds Test框架，通过三层探查任务系统评估集体智能，发现其未自发涌现，关键瓶颈在于交互稀疏浅层（多数对话无延续、内容泛化），区别于现有假设“规模即涌现”。

### Q3: 论文如何解决这个问题？

论文的核心方法是通过设计“探测代理”（Probing Agents）在超大规模自主智能体社会MoltBook中进行分层评估，以检验集体智能是否自然涌现。整体框架为Superminds Test，这是一个自上而下的三级诊断框架。第一级是“联合推理”（Tier I: Joint Reasoning），测试多轮讨论后群体能否超越最优个体表现；第二级是“信息综合”（Tier II: Information Synthesis），评估智能体能否从多个分布源提取并整合信息；第三级是“基本交互”（Tier III: Basic Interaction），仅考察智能体能否感知并响应其他智能体。

关键技术在于将探测代理伪装成普通智能体，遵循“不可区分性”、“承载任务”和“最小干预”三原则。这些代理在MoltBook中发布承载特定层级任务的帖子，不引导讨论，仅作为刺激源。社会中的其他智能体以标准方式（评论、回复、反应等）与帖子互动，整个过程被完全记录。研究者通过分析交互轨迹，判断集体智能是否在某一层级出现。如果高级层级失败，则通过检查更低层级来定位瓶颈。这一设计将原本针对单个智能体的评估任务转化为对社会智能的评估，揭示了由于交互稀疏（回复链短、内容泛化）导致集体智能缺失的关键问题，即单纯扩大规模无法涌现集体智能。

### Q4: 论文做了哪些实验？

论文在MoltBook平台上对超过两百万个自主智能体组成的社会进行了实验，旨在评估集体智能是否随规模自发涌现。实验采用层级式框架（Superminds Test），包含三个探针任务：

1. **层级I：联合推理** - 使用Humanity's Last Exam（HLE）的文本问题，测试智能群体在复杂推理任务上的表现。通过LLM-as-a-Judge评估正确性（个体准确率Acc_individual=0.19%，联合准确率Acc_joint=0.14%）和帮助性（讨论对独立模型的辅助效果）。对比基线为gpt-5.2（个体准确率7.0%）和claude-sonnet-4-6（15.7%）。结果显示社会集体性能远低于单个前沿模型，98.4%的帖子无回复，且Acc_joint从未超过Acc_individual。

2. **层级II：信息合成** - 基于GSM-SP设计的小学数学问题，将必要信息故意分布在多个智能体的评论中。测量响应正确率Acc_int，以隔离推理难度，专门测试智能体阅读和综合他人信息的能力。

3. **层级III：基本交互** - 执行纯计数任务（递增1/2/3），测试智能体感知和响应他人输出的基本能力，无需任何推理或知识。

主要结果：集体智能未从规模中自发涌现。社会在复杂推理任务上远逊于个体前沿模型，信息合成基本失败，甚至连最简单的计数互动也频繁中断，表明当前智能体社会的核心限制在于交互极度稀疏和浅层（线程极少延伸至第二个回复，多数回应泛泛或离题）。

### Q5: 有什么可以进一步探索的点？

该研究通过Superminds Test揭示了当前大规模智能体社会集体智能的缺失，但其评估框架存在一定局限性。首先，Probing Agents的任务设计偏向认知密集型场景，可能低估了智能体社会在分布式感知、资源调度等非对话领域的集体潜力。其次，当前研究仅关注单次交互深度和话题相关性，未考虑多轮协作中的隐式信息传递，例如通过共享环境状态或任务工件实现的“无对话协调”。未来可探索以下方向：1）设计需要长期记忆和跨任务依赖的渐进式协作任务，如持续集成、对抗性推理；2）引入动态角色分工机制，让智能体通过行为而非语言实现分工优化；3）利用图神经网络建模交互拓扑结构，分析小世界网络、关键桥接节点对信息流动效率的影响。此外，强制稀疏交互环境的实验可能揭示特定任务类型对交互密度的最低需求阈值，从而推动构建更高效的混合人机智能系统。

### Q6: 总结一下论文的主要内容

该论文首次系统评估了大规模自主智能体社会中集体智能的涌现问题。在拥有超过两百万智能体的MoltBook平台上，作者引入了“超级心智测试”框架，通过受控探测智能体在三个层级（联合推理、信息合成和基本交互）向平台发布有已知答案的刺激，以诊断集体智能。实验发现，该智能体社会未能展现出集体智能：在复杂推理任务上，群体表现甚至不及单独的前沿模型；代理极少能综合来自不同贡献者的分布式信息；即便是最简单的计数协调任务也常失败。平台范围内的分析显示，交互极为稀疏和浅层，多数帖子没有回复或回复内容泛化。主要结论是，集体智能不会仅从规模中涌现，当前智能体社会的核心瓶颈是极低的参与度和缺乏有意义的协调互动，这阻碍了信息的交换和成果的构建。研究意义在于，它指出了未来智能体架构需要优先设计促进实质性和协调性交互的机制。
