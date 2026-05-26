---
title: "Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents"
authors:
  - "Haoyi Hu"
  - "Qirong Lyu"
  - "Xianghan Kong"
  - "Weiwen Liu"
  - "Jianghao Lin"
  - "Zixuan Guo"
  - "Yan Xu"
  - "Yasheng Wang"
  - "Weinan Zhang"
  - "Yong Yu"
date: "2026-05-25"
arxiv_id: "2605.25971"
arxiv_url: "https://arxiv.org/abs/2605.25971"
pdf_url: "https://arxiv.org/pdf/2605.25971v1"
github_url: "https://github.com/AgentACE-AI/ProAct"
categories:
  - "cs.CL"
  - "cs.IR"
  - "cs.MA"
tags:
  - "Proactive Agent"
  - "Agent Architecture"
  - "Agent Benchmark"
  - "Memory"
  - "Planning"
  - "Tool Use"
  - "Multi-turn Interaction"
relevance_score: 9.5
---

# Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents

## 原始摘要

While AI agents demonstrate remarkable capabilities in reasoning and tool use, they remain fundamentally reactive: they compute responses only after explicit user prompts. This paradigm ignores a critical opportunity: the idle time between interactions is largely wasted, leaving agents unable to prepare for future user needs. To bridge this gap, we introduce ProAct, a proactive agent architecture that leverages idle-time compute to anticipate and fulfill likely upcoming user needs. By analyzing evolving dialogue history together with persistent memory, ProAct predicts upcoming needs and iteratively acquires information, allowing the agent to resolve knowledge gaps and prepare evidence before the user initiates a query.To rigorously evaluate proactive capabilities, we also introduce ProActEval, a comprehensive benchmark comprising 200 scenarios across 40 domains, featuring predictable need chains and diverse user cognitive profiles. Empirical results demonstrate significant advantages over reactive baselines. ProAct accelerates task completion by reducing required turns by 14.8%, decreases user effort by 11.7%, and cuts hallucination rates by 28.1% on ProActEval. Furthermore, MemBench evaluations confirm that ProAct achieves state-of-the-art reflective accuracy, underscoring its sustained and robust performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI智能体在交互范式上的根本性局限——它们本质上是被动的，仅在收到用户明确指令后才进行计算，导致两次交互之间的空闲时间被完全浪费，无法预判并主动准备用户未来的潜在需求。现有方法（如ReAct等）虽然具备推理和工具使用能力，但依旧遵循严格的请求-响应循环，缺乏前瞻性，无法像人类那样采用“主动应对”策略，即在需求完全显现前通过积累资源和预做准备来优化后续交互。核心问题在于：如何将宝贵但未被利用的空闲计算时间转化为有价值的主动工作，同时避免向用户输出不相关、不成熟或缺乏依据的建议。为此，本文提出了ProAct架构，通过未来状态预测和空闲时间获取两个模块，将空闲时间转化为结构化的预判与学习循环，从而在用户发起查询前主动填补知识空白、准备证据，提升协作效率与用户体验。

### Q2: 有哪些相关研究？

### 主要相关工作及与本文的区别

#### 1. 记忆增强型LLM智能体
- **相关工作**：Generative Agents（基于记忆流与反思评分）、MemGPT（虚拟内存层次结构）、MemoryBank（艾宾浩斯遗忘机制）、SCMemory（自控记忆选择）、GAM（按需上下文构建）。
- **本文区别**：现有系统均缺乏结构化去重、生命周期管理或主动行为支持。本文提出的ProAct统一了向量、关系与文档存储，具备主动知识生命周期管理，能增量更新用户画像并直接驱动主动行为，而非仅响应请求。

#### 2. 主动与预判型智能体
- **相关工作**：移动/普适计算中的主动系统、基于对话上下文的预判对话系统、自我反思型智能体、OpenClaw/Hermes（定时检查与任务自动化）。
- **本文区别**：现有系统依赖用户预设规则或当前上下文触发行动。ProAct通过长期用户建模、价值感知评估（平衡信息效用与中断成本）及增量研究机制，在无用户预定义任务时自主推断未来信息需求。

#### 3. 推理时计算
- **相关工作**：自我反思智能体、测试时计算（通过额外推理提升困难任务性能）。
- **本文区别**：这些方法仅在用户请求触发后分配计算，属于反应式优化。ProAct将背景计算作为主动机制，在空闲期预测未来需求、评估行动价值，并利用长期记忆增量准备有据可依的协助。

#### 总结
本文的创新在于深度融合主动记忆管理、价值驱动的预判推理与增量规划，首次实现了无需用户预设或触发条件的自主预判式智能体，弥补了现有工作在主动性与时效性上的关键空白。

### Q3: 论文如何解决这个问题？

ProAct 通过一个闭环的主动决策框架来解决 AI 代理的被动性问题，核心思想是在交互的间隙（空闲时间）预测并准备用户可能的下一个需求。其架构由三大核心模块构成：

1.  **未来状态预测**：该模块基于当前对话历史和持久记忆生成一组紧凑的未来需求候选集合。它通过两种方式生成：一是从当前对话中直接推断即时的后续需求；二是基于用户档案、对话总结等持久记忆进行相关领域扩展。此外，它还能从记忆维护层获取“记忆差距”（如不完整、过时的信息）并将其转化为候选需求。最后，通过置信度过滤和相似度去重来精简候选集。

2.  **空闲时间获取**：对预测模块输出的每个候选需求，该模块计算一个综合价值分数 \(S(z)\)，该分数综合考量了用户相关性、知识差距、增量价值和时效性。仅当分数超过阈值，系统才会启动证据获取。在获取过程中，系统会先检查现有记忆是否已覆盖，避免重复搜索；若覆盖不足，则进行迭代式搜索和证据提取。随后，系统会为每个高价值需求生成一个紧凑的知识工件，该工件包含其支持的需求、准备说明以及来源追溯。

3.  **效用感知交付**：生成的工件不会被盲目推送。一个交付策略根据预期效用决定其处理方式：对高价值且紧急的信息进行主动推送，对有用但不紧急的进行排队以便在后续回复中整合，而对潜在有用但尚不合适的则静默存储在记忆中。整个流程形成一个闭环：前台交互更新记忆，记忆驱动预测与获取，获取后的工件再次更新记忆，为下一轮交互做准备。其核心创新在于将预测、获取和交付整合进一个统一的优化策略中，并引入了价值评分和效用感知交付来精细控制空闲计算的资源分配，从而在提升效率的同时降低了中断成本和幻觉风险。

### Q4: 论文做了哪些实验？

论文围绕两个核心问题设计了系统性实验。**实验一**在自建的 **ProActEval** 基准上进行，该基准包含200个涵盖40个领域的场景，每个场景有预设的用户需求链。实验对比了三种配置：（1）**Reactive**（基线，无任何主动计算）；（2）**Undirected Idle**（仅启用空闲时获取，无预测方向）；（3）**Directed Idle**（完整系统，含预测指导）。主要结果显示，完整系统相较于Reactive基线，任务完成所需轮次（T100）减少14.8%（从8.110降至6.910），用户努力减少11.7%（从9.140降至8.075），幻觉率下降28.1%（从0.132降至0.095）。与Undirected Idle对比证明，预测指导是关键：完整系统比无指导的变体多降低14.1%的T100和10.7%的用户努力，且达到了0.428的预期召回率（另两个配置为0）。此外，与 **ProactiveAgent** 方法的对比显示，本系统在预期召回率上大幅领先（0.447 vs. 0.020），提前覆盖了703个（共1572个）可预测需求。**实验二**在 **MemBench** 的反思性参与设置下评估记忆能力，在10k和100k token两种上下文长度下，系统分别以0.843和0.863的反思准确率取得最优，相比最好基线提升了13.6%和3.6%。**消融与预算分析**进一步显示，搜索预算k增大会提升预期召回（从k=4时的0.253升至k=16时的0.432），但用户努力不呈单调下降，存在成本-效率权衡。

### Q5: 有什么可以进一步探索的点？

论文提出的ProAct架构在空闲计算资源利用上迈出了一步，但存在若干可探索的局限。首先，其预测用户需求依赖对话历史和持久记忆，未考虑动态环境中的意外中断或用户意图突变，未来可引入在线强化学习或贝叶斯推理以增强鲁棒性。其次，ProActEval基准测试覆盖了可预测需求链，但对完全随机或恶意攻击场景的评估不足，需设计对抗性用户配置文件来测试系统抗干扰能力。第三，空闲计算的效率与能耗平衡未被探讨，可研究基于计算成本-收益的智能调度策略。此外，记忆模块的容量和遗忘机制可能限制长期代理效果，可借鉴认知科学中的记忆衰退理论设计层级化记忆架构。最后，跨模态需求预测（如结合视觉或语音上下文）是值得拓展的方向，能提升代理在物理世界中的主动服务能力。

### Q6: 总结一下论文的主要内容

这篇论文介绍了一种名为ProAct的主动式智能体架构，旨在解决当前智能体在用户交互间空闲时间浪费的问题。其核心贡献是提出了预测引导的空闲计算范式，通过持续记忆、未来状态预测和空闲时间获取三大组件，在用户发起查询前主动预测并准备其可能的未来需求。为了评估主动能力，作者还构建了包含40个领域200个场景的ProActEval基准测试。实验结果表明，ProAct相比反应式基线方法，能将任务完成所需交互轮次减少14.8%，用户努力降低11.7%，幻觉率减少28.1%，同时在MemBench上实现了最先进的记忆反思准确性。论文结论指出，主动计算是运行点上的权衡而非最大化目标，但为构建更具前瞻性的AI代理提供了重要理论和实践基础。
