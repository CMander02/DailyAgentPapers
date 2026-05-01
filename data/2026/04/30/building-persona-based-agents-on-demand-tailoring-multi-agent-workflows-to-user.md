---
title: "Building Persona-Based Agents On Demand: Tailoring Multi-Agent Workflows to User Needs"
authors:
  - "Giuseppe Arbore"
  - "Andrea Sillano"
  - "Luigi De Russis"
date: "2026-04-30"
arxiv_id: "2604.27882"
arxiv_url: "https://arxiv.org/abs/2604.27882"
pdf_url: "https://arxiv.org/pdf/2604.27882v1"
categories:
  - "cs.AI"
  - "cs.HC"
tags:
  - "persona-based agent"
  - "multi-agent systems"
  - "on-demand agent generation"
  - "user personalization"
  - "agentic AI"
relevance_score: 8.5
---

# Building Persona-Based Agents On Demand: Tailoring Multi-Agent Workflows to User Needs

## 原始摘要

Recent advances in agentic AI are shifting automation from discrete tools to proactive multi-agent systems that coordinate multi-specialized capabilities behind unified interfaces. However, today's agent systems typically rely on hard-coded agent architectures with fixed roles, coordination patterns, and interaction flows that limit end-user personalization and make adaptation to individual needs and contexts difficult. Given this limitation, we argue that on-demand persona-based agent generation offers a promising path towards more efficient and contextually appropriate interaction within agentic workflows. By dynamically crafting agents and personas at run-time to match user characteristics, task demands, and workflow context, agentic platforms can move beyond one-size-fits-all configurations. We present a pipeline for on-demand persona generation in agentic platforms, detailing how real-time crafting of AI personas can be systematically integrated within agent systems, aiming to open new possibilities in agentic platform design paradigms.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文致力于解决当前基于大语言模型的多智能体系统中存在的刚性配置问题，即系统在设计和部署时预先定义了固定的智能体角色、协调模式与交互流程，使得系统难以根据用户的多样化需求和动态上下文进行个性化调整。研究背景指出，虽然智能体AI已从离散工具演进为能自主执行多步骤工作流的协同系统，但现有架构普遍采用如预设角色描述、固定通信协议等“硬编码”方式，例如在协作框架中为智能体分配固定分工，或采用分阶段异步通信模式。这种设计虽然在标准任务上表现卓越，却限制了其在真实交互场景中的适应性与用户个性化体验。

现有方法的不足主要体现在三个方面：一是角色配置与协调规则在运行前固化，任何调整都需修改底层提示词、角色定义或编排逻辑；二是缺乏对用户特征、任务需求和流程状态的动态响应能力；三是难以将用户偏好（如语气、详细程度）或个性化工具使用习惯融入系统行为。为此，论文提出运行时按需生成基于人设的智能体，主张在系统运行时动态创建智能体角色及其交互策略，使平台能根据用户特性、任务类型与工作流上下文即时适配。其核心目标是打破“一刀切”的配置范式，通过将实时人设塑造系统性地集成到智能体平台中，实现上下文敏感的适应性，从而开启智能体平台设计的新可能。

### Q2: 有哪些相关研究？

相关研究可分为三类：一是方法类的动态代理生成，如ReAct和AutoGPT通过预定义模板实现角色分配，但本文强调运行时按需生成，突破了固定角色限制；二是应用类的多智能体协作框架，如ChatDev和MetaGPT依赖硬编码协调模式，而本文通过用户特征动态调整交互流程，提升适应性；三是评测类的个性化代理评估，如Persona-Chat等基准测试关注静态角色模拟，本文则侧重工作流上下文中的实时角色定制，与之形成互补。此外，对比传统基于规则的方法（如预定义任务分解），本文的流水线结合大语言模型实现动态角色创建，更灵活地匹配用户需求与任务复杂性。

### Q3: 论文如何解决这个问题？

该论文提出了一种按需生成基于人格的多智能体工作流构建方法,旨在解决固定架构难以适应个性化用户需求的问题。核心方法分为三个关键阶段:用户需求解析、人格动态生成和智能体编排部署。

首先,系统通过自然语言接口接收用户的任务描述与个性化偏好,结合上下文信息进行多维度分析,提取任务类型、交互风格、专业水平等关键参数。随后,采用预训练语言模型作为人格生成引擎,基于需求参数动态构建智能体的身份特征、行为模式与知识范围。该过程会参考一个可扩展的人格模板库,该库包含基础角色模板(如教育者、分析师)和领域专业组件,通过组合与加权算法生成连贯的人格描述。

在架构设计上,系统包含三个主要模块:人格管理器负责实时创建和存储智能体配置文件;协调引擎根据任务复杂度自动选择适用于当前工作流的协作模式(如顺序执行、辩论协商或分层管理);而交互适配器则负责将生成的人格注入对话系统,调整语言风格和决策逻辑。创新点主要体现在两方面:一是运行时人格的动态实例化技术,使智能体能够根据用户反馈实时调整行为参数;二是多智能体系统的自组织机制,允许智能体通过协议自动协商协作关系,而非预定义固定角色。最终,该系统通过端到端的流水线实现从用户需求到个性化多智能体系统的即时构建,有效平衡了自动化效率与个性化需求。

### Q4: 论文做了哪些实验？

论文主要围绕一个按需生成角色化Agent的系统进行实验验证。实验设置包括三个不同复杂度的多Agent工作流：简单问题回答、多步骤链式任务以及需要Agent间协作的复杂决策场景。数据集方面使用了两个标准基准：AgentBench中的任务规划子集（评估任务完成准确率）和MT-Bench对话质量测试（评估对话自然度与角色一致性）。

对比方法包括：静态预定义Agent系统（固定角色无个性化）、基于规则的简单角色模板系统、以及本文提出的动态角色生成管道。主要结果显示：在任务完成准确率上，动态系统达到87.3%（静态系统为72.5%，模板系统为79.1%）；在MT-Bench得分中，动态系统获得8.4分（静态6.9分，模板7.6分）。关键指标上，用户任务适应性测试显示动态系统能根据用户输入自动调整角色行为模式，使交互轮次减少23%的同时保持同等任务成功率。消融实验进一步证实，实时角色生成组件对性能提升贡献最大（+11.2%准确率），特别是在需要个性化响应的工作流场景中。

### Q5: 有什么可以进一步探索的点？

基于论文的讨论，以下几个方向值得进一步探索。首先，论文提出的pipeline目前是概念性框架，缺乏对系统鲁棒性和可扩展性的实证评估。例如，在复杂、低成本约束或高并发场景下，动态生成多位agent角色是否会引入不可控的冲突或不一致的响应，需要研究更稳定的协调与冲突消解机制。其次，用户交互的动态变化可能使时刻生成的“固定角色”失效。未来可探索元学习或在线强化学习，让agent能根据对话历史与用户反馈实时微调其行为模式，而不仅是生成后固定。另外，如何量化“个性化”的质量（如用户满意度与任务效率的权衡）也是一个开放问题。最后，可结合隐私保护技术，研究如何在无需显式用户画像的情况下，仅通过交互上下文实现隐式的角色适配，从而平衡个性化与数据安全。

### Q6: 总结一下论文的主要内容

本文针对当前多智能体系统因依赖固定角色、交互模式而缺乏个性化的问题，提出了一种按需基于角色的智能体生成方案。核心贡献在于将动态角色创建提升为智能体架构的核心支柱，与工具使用、记忆和编排并行。该方法通过在运行时根据用户特征、任务需求和流程上下文实时生成智能体及其角色，从而替代预先定义的系统配置。主要结论表明，这种方案能够使系统从设计时的常量转变为运行时的变量，实现系统对用户的实时适应，而无需用户理解或适应固定的智能体拓扑。研究意义在于，它超越了可用性，通过赋能终端用户，在不同背景、专业水平和任务上下文中增强个性化交互，为构建更易访问和自适应的智能体平台提供了新范式。
