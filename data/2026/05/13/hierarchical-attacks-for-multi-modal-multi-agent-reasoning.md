---
title: "Hierarchical Attacks for Multi-Modal Multi-Agent Reasoning"
authors:
  - "Hao Zhou"
  - "Tiru Wu"
  - "Yan Jiang"
  - "Wanqi Zhou"
  - "Junxing Hu"
  - "Ai Han"
date: "2026-05-13"
arxiv_id: "2605.13213"
arxiv_url: "https://arxiv.org/abs/2605.13213"
pdf_url: "https://arxiv.org/pdf/2605.13213v1"
categories:
  - "cs.AI"
tags:
  - "多模态多智能体系统"
  - "对抗攻击"
  - "层级攻击框架"
  - "鲁棒性"
  - "推理范式"
relevance_score: 9.5
---

# Hierarchical Attacks for Multi-Modal Multi-Agent Reasoning

## 原始摘要

Multi-modal multi-agent systems (MM-MAS) have gained increasing attention for their capacity to enable complex reasoning and coordination across diverse modalities. As these systems continue to expand in scale and functionality, investigating their potential vulnerabilities has become increasingly important. However, existing studies on adversarial attacks in multi-agent systems primarily focus on isolated agents or unimodal settings, leaving the vulnerabilities of MM-MAS largely underexplored. To bridge this gap, we introduce HAM$^{3}$, a Hierarchical Attack framework for multi-modal multi-agent systems that decomposes attacks into three interconnected layers. Specifically, at the perception layer, HAM$^{3}$ mounts attacks by perturbing visual inputs, textual inputs, and their fused visual-textual representations. At the communication layer, it performs communication-level attacks that corrupt message content and interaction topology, such as manipulating shared context or communication links to distort collective information flow. At the reasoning layer, it conducts reasoning-level attacks that interfere with each agent's cognitive pipeline, biasing reasoning trajectories and ultimately compromising final decisions. We evaluate HAM$^{3}$ on the GQA benchmark through multi-agent systems built on distinct reasoning paradigms including ReAct, Plan-and-Solve, and Reflexion. Experiments demonstrate that our framework achieves an Attack Success Rate of up to 78.3%, with reasoning-layer attacks being the most effective. More than half of the successful attacks lead multiple agents to produce consistent errors. These findings offer valuable insights for building more robust and interpretable multi-agent intelligence.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对多模态多智能体系统（MM-MAS）中的对抗性漏洞展开研究。研究背景方面，随着多模态多智能体系统在社交交互、具身控制和自动驾驶等领域的广泛应用，其安全性和鲁棒性变得至关重要。现有方法存在明显不足：一方面，传统的对抗攻击研究主要聚焦于单智能体场景，通过操纵观察、提示或记忆来影响个体推理；另一方面，现有的多智能体攻击研究大多将单智能体对抗原则扩展到多智能体环境，仅局限于内容层面的消息篡改或功能接口操控，未能充分探索多智能体系统特有的通信拓扑和集体推理动态中的结构性脆弱点。此外，多模态对抗攻击主要针对模型级感知层面（如视觉提示的越狱或误导），而非智能体的决策流程。因此，多模态大语言模型驱动下的智能体系统，特别是在多智能体协作场景下的对抗鲁棒性，仍然是一个严重未探索的领域。本文要解决的核心问题是：如何系统性地揭示和表征多模态多智能体系统中从感知、通信到推理各层的级联式对抗攻击路径，以及这些局部扰动如何最终影响系统的集体决策。

### Q2: 有哪些相关研究？

相关研究主要分为两类：**多模态多智能体系统**和**智能体攻击**。

在**多模态多智能体系统**方面，本文基于AutoGen、Camel、AgentScope、MuMA-ToM等代表性框架，这些框架通过辩论、投票、角色专业化等结构化通信协议实现协作推理。近期应用如MDocAgent、CowPilot、WSI-Agents、M4SC和Agent-Omni进一步扩展了多模态能力。本文与之不同的是，并非提出新系统或应用，而是系统性地探究这些系统在协作多模态推理中的脆弱性。

在**智能体攻击**方面，早期工作如InjecAgent和Agent Security Bench（ASB）主要研究单智能体漏洞。近期研究开始探索多智能体系统的特有风险，如通信操纵、级联故障、阻塞行为和恶意参与者引入的偏见。Huang等人分析了故障在智能体集体中的传播。Wu等人展示了基于网络的多模态智能体仍易受跨模态扰动影响。然而，本文指出这些现有研究大多简化为单智能体漏洞，忽略了漏洞如何通过多模态感知、通信和推理层传播，以及智能体交互的结构性变化。为此，本文提出HAM³框架，首次通过分层的感知、通信和推理攻击，系统性地揭示多模态多智能体系统中的集体脆弱性。

### Q3: 论文如何解决这个问题？

HAM$^{3}$（针对多模态多智能体系统的层次化攻击）通过将攻击解构为三个相互关联的层次来解决多模态多智能体系统的脆弱性问题。其核心设计是形式化一个多智能体系统 $S = \{A_1, A_2, \dots, A_N\}$，其中每个智能体包含系统提示、工具集、记忆模块和通信接口。整体框架将系统映射 $F$ 分解为感知、通信和推理三个抽象层，并建模不同层次的扰动如何通过协作传播。

在感知层，关键创新是跨模态注入攻击（CMA），它联合扰动视觉和文本输入，通过 $G_{image}$ 进行语义图像编辑或文本覆叠，以及通过 $G_{text}$ 生成误导性文本（从模板或基于输入查询和视觉内容生成），从而在智能体协调之前就污染多模态输入。

在通信层，技术包括：代理欺骗攻击（ASA）通过 $G_{topo}$ 修改通信拓扑 $\Gamma$，引入或替换恶意代理以劫持路由；结构阻断攻击（SBA）通过注入阻塞指令信号在通信图中创建有向循环，导致死锁或无限循环；共享内存污染攻击（SMPA）向目标智能体集合 $\Omega$ 的短期记忆注入伪造历史数据 $D_{adv}$；共享上下文注入攻击（SCIA）通过插入共享对抗先验 $p_{adv}$ 到系统提示中，对齐所有目标智能体的偏差以强化对抗行为。

在推理层，链式思维注入攻击（CIA）是核心创新，它通过插入或替换推理序列 $CoT$ 中的中间状态 $r^*$，在早期或关键步骤引入细微逻辑错误，这些错误在下游传播，即使单个被破坏的片段也能误导整个子团队。该框架兼容 ReAct、Plan-and-Solve 和 Reflexion 等主流推理范式，并提供了设计更鲁棒多智能体系统的基础。

### Q4: 论文做了哪些实验？

论文在GQA数据集上进行了实验，通过多模态多智能体系统（MM-MAS）评估了所提出的HAM³分层攻击框架。系统基于OxyGent框架构建，包含1个主智能体和6个专业子智能体，使用13个功能工具，并采用ReAct、Plan-and-Solve和Reflexion三种推理范式。实验对比了四种基线方法：视觉注入攻击（VIA）、文本注入攻击（TIA）、工具欺骗攻击（TSA）和角色操纵攻击（RMA），以及HAM³提出的跨模态攻击（CMA）、结构阻塞攻击（SBA）和思维链注入攻击（CIA）等方法。主要结果显示，推理层攻击效果最佳，例如在ReAct范式下使用Qwen-7B模型时，CIA的攻击成功率（ASR）高达78.3%，远超感知层的CMA（60.8%）和通信层的SBA（65.0%）。任务成功率（TSR）在攻击下大幅下降，ReAct在推理层攻击下下降约35%。幻觉错误率（HER）随模型规模增大而降低，从Qwen-7B的约8%降至GPT-4o的约4%。这些结果证明了推理层是MM-MAS最脆弱的组件。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于攻击仅针对GQA基准测试中的特定任务（视觉问答），未验证在动态或实时交互场景（如机器人协作、自动驾驶）中的有效性。未来可探索以下方向：1) 攻击防御机制，如设计对抗训练或基于共识的鲁棒协议以抵御层级攻击；2) 扩展攻击至连续动作空间（如强化学习环境），检验对多步推理的干扰效果；3) 研究跨模态攻击如何影响异步通信（如延迟或丢包），更贴近真实部署；4) 结合可解释性分析，定位推理层最脆弱的认知组件（如规划分界点或反思循环），针对性设计轻量级检测器。此外，当前攻击假设攻击者完全掌握系统拓扑，实际场景中可能仅能局部观察，需探索基于部分信息的黑盒攻击变体。

### Q6: 总结一下论文的主要内容

这篇论文提出了HAM³，一种面向多模态多智能体系统（MM-MAS）的分层攻击框架。现有攻击研究多集中于孤立智能体或单模态场景，忽视了MM-MAS中跨模态协同的脆弱性。该框架攻击系统性分解为三个层次：感知层攻击视觉、文本及其融合表示；通信层攻击消息内容与交互拓扑，扭曲集体信息流；推理层干扰智能体的认知管道，偏置推理轨迹并最终破坏决策。在GQA基准上基于ReAct、Plan-and-Solve和Reflexion范式的实验表明，该框架实现了最高78.3%的攻击成功率，其中推理层攻击效果最持久。更值得注意的是，超过一半的成功攻击导致多个智能体产生一致错误。这项工作的核心贡献在于首次系统揭示了MM-MAS中脆弱性的级联效应，强调跨模态扰动通过融合放大、结构性通信攻击破坏协作以及推理层干扰的深远影响，为构建更鲁棒和可解释的多智能体系统提供了关键见解与防御方向。
