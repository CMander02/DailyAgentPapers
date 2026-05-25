---
title: "How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning"
authors:
  - "Zeyu He"
  - "Hannah Kim"
  - "Dan Zhang"
  - "Estevam Hruschka"
date: "2026-05-21"
arxiv_id: "2605.23023"
arxiv_url: "https://arxiv.org/abs/2605.23023"
pdf_url: "https://arxiv.org/pdf/2605.23023v1"
github_url: "https://github.com/megagonlabs/ambipom"
categories:
  - "cs.MA"
  - "cs.HC"
tags:
  - "多智能体系统"
  - "人机协作规划"
  - "用户交互"
  - "过程级监督"
  - "人机协作"
relevance_score: 8.0
---

# How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning

## 原始摘要

In orchestrated multi-agent systems, humans often struggle to manage plans due to their complexity and limited transparency. Existing approaches rely on outcome-level supervision, where users verify only final outputs without visibility into intermediate reasoning. We formalize a design space for human-LLM co-planning interactions along three axes: mode (semantic vs. structural), scope (global vs. targeted), and level (low vs. high-level edits). We realize it in AMBIPOM, a prototype supporting process-level supervision through both semantic and structural interactions. Through a user study, we characterize how users navigate this space, revealing hybrid workflows and effort-control-risk trade-offs; through a controlled benchmark, we analyze how LLMs revise plans under varying scope and revision strategies. Our findings yield design insights for more transparent, controllable, and effective human-AI co-planning. We release code and data at https://github.com/megagonlabs/ambipom.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在编排式多智能体系统（MAS）中，人类难以有效管理复杂、不透明的规划过程的问题。现有方法大多依赖结果级监督，即用户只能验证最终输出，无法洞察中间推理和协调过程，导致诊断失败和进行针对性修正的能力受限，尤其是在复杂多智能体计划中。为解决这一核心问题，论文提出并形式化了一种人类与LLM（大型语言模型）协作规划的设计空间，从三个轴维度建模交互：**模式**（语义反馈 vs. 结构直接操作）、**范围**（全局影响 vs. 基于选定子图的靶向修改）和**层级**（低层原子编辑 vs. 高层组合操作如合并/拆分）。论文通过原型系统AMBIPOM实例化该设计空间，旨在通过过程级监督（而非结果级监督）提升计划的可视性、可控性和可修正性，并研究用户在该空间中的行为模式以及LLM在不同协作策略下的修订能力，最终实现更透明、可控且高效的人机协作规划。

### Q2: 有哪些相关研究？

相关工作可分为三大类。一是**方法类**，如COCOA、Magnetic-UI、AGDebugger等框架，允许用户通过直接操作线性计划（增删改步骤）或拦截编辑agent间消息来实现协作。本文与它们的核心区别在于，这些工作仅支持单一维度的交互（如仅修改步骤内容），而本文系统化定义了模式（语义/结构）、范围（全局/局部）和层级（高/低层次编辑）三轴设计空间，并实现了AMBIPOM原型以覆盖多种交互类型。二是**应用类**，如GitHub Copilot、Gemini Deep Research等主流AI助手采用聊天式规划，用户只能作为被动顾问通过高层提示修改计划。本文指出这种模式缺乏透明度和细粒度控制，转而强调在复杂多agent系统中引入过程级监督。三是**评测类**，最接近的前作AIPOM虽结合了聊天与图形编辑器，但仅沿模式轴实现过程监督。本文首次通过用户研究和受控基准实验，系统比较了不同交互维度下的工作流特征和修订策略，揭示了混合工作流与收益-控制-风险权衡。

### Q3: 论文如何解决这个问题？

该论文通过提出一个名为AMBIPOM的原型系统来解决人类在多智能体系统中管理复杂计划时的困难。核心方法围绕人机协作规划展开，设计了一个三维交互空间：模式（语义vs.结构）、范围（全局vs.局部）和层级（低级vs.高级编辑）。

整体框架包含一个基于LLM的规划器和四个专门的执行智能体（代码、数学、搜索、常识）。系统采用双面板界面：聊天面板支持语义交互（自然语言反馈），计划面板支持结构交互（可视化DAG编辑）。关键技术包括四种交互类型：全局重规划（用户对整个计划提供文本反馈，LLM重新生成）、局部重规划（用户选择子图并提供文本反馈，仅重新生成该子图）、低级直接操作（用户手动增删节点/边、修改任务描述等确定性操作）、高级直接操作（合并/分割节点，可手动或由LLM辅助自动执行）。

创新点在于：1）形式化了人机协规划的设计空间，明确了模式、范围和层级三个关键维度；2）实现了过程级监督，用户不仅可以查看最终输出，还能观察和修改中间推理步骤；3）支持混合工作流，用户可在语义和结构交互间灵活切换；4）自动合并/分割功能降低了用户操作负担，同时保持计划的结构有效性。系统通过共享计划状态确保语义和结构交互的实时一致性。

### Q4: 论文做了哪些实验？

论文进行了两类实验。第一项是用户研究：招募13名参与者，在AMBIPOM原型系统与仅支持基本交互的基线系统间进行对比，采用被试内设计。任务基于四类结构模式（逐步数学推理、多跳计算、列表检索与聚合、Top-K检索与聚合）的8个问题，要求参与者修改初始计划并得出正确答案。主要发现：使用高级交互（如DM_high^+）并未比基本交互产生更高计划质量，但DM_high^+降低了认知负荷，TF减少了对话轮次；用户倾向于混合使用交互类型，并受到努力-控制-风险的权衡驱动。

第二项是受控基准实验：构建了包含200个黄金计划和1150个破坏后计划的基准，通过7种操作类型（如添加节点、合并等）评估四种反馈条件（GF、TF、TF+P、GF-to-DM）的规划修订效果。主要结果：全局反馈（GF）在所有条件下均成功（成功率1.0），而TF、TF+P成功率分别为0.976和0.986；GF-to-DM成功率最低（0.788）。在计划质量上，GF在各项指标（如GED、语义相似度、稳定性）上通常优于TF。此外，在逐步数学推理子集上，GF的最终答案执行准确率达0.920，高于GF-to-DM（0.823）。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来研究方向主要体现在以下几个方面：首先，当前研究主要聚焦于静态计划修订，未充分探索动态环境中计划需要实时迭代更新的场景，未来可引入在线学习机制使系统能根据环境反馈自适应调整协作策略。其次，用户研究中受试者均具备一定技术背景，对于非专业用户的认知负荷和交互效率尚未评估，可设计任务感知的自适应交互模式，降低规划透明度的认知成本。在技术层面，AMBIPOM对结构性编辑的支持限于简单拓扑修改，建议引入基于图神经网络的计划状态嵌入方法，实现更复杂的上下文感知编辑。此外，当前未量化不同scope和mode组合对任务完成质量的非线性影响，可构建多目标优化框架平衡人类控制偏好与LLM生成效率。最后，需要探索多轮次协商中的信任演化机制，通过交互式反事实解释增强人类对LLM修订逻辑的理解。

### Q6: 总结一下论文的主要内容

本文提出了一种名为AMBIPOM的原型系统，旨在解决多智能体系统中人类难以管理复杂计划且缺乏透明性的问题。现有方法主要依赖结果级监督，用户只能验证最终输出，无法了解中间推理过程。论文首先形式化了人机协同规划的设计空间，包含三个维度：模式（语义反馈 vs. 结构编辑）、范围（全局 vs. 局部）和层级（低级 vs. 高级编辑）。AMBIPOM通过有向无环图明确表示多智能体计划，支持流程级监督。通过用户研究，论文揭示了用户如何结合不同交互类型形成混合工作流，并展示了努力-控制-风险的权衡；通过受控基准实验，分析了LLM在不同范围和修订策略下的计划修改能力。主要结论是：透明的流程级监督能显著提升人机协同规划的可控性和有效性，为设计更透明、可控的人机协同系统提供了重要洞见。
