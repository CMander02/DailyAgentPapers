---
title: "Benchmarking Autonomous Agents against Temporal, Spatial, and Semantic Evasions"
authors:
  - "Jianan Ma"
  - "Xiaohu Du"
  - "Ruixiao Lin"
  - "Yaoxiang Bian"
  - "Jialuo Chen"
  - "Jingyi Wang"
  - "Xiaofang Yang"
  - "Shiwen Cui"
  - "Changhua Meng"
  - "Xinhao Deng"
  - "Zhen Wang"
date: "2026-05-21"
arxiv_id: "2605.22321"
arxiv_url: "https://arxiv.org/abs/2605.22321"
pdf_url: "https://arxiv.org/pdf/2605.22321v1"
github_url: "https://github.com/antgroup/Agent3Sigma-Stage"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.SE"
tags:
  - "多轮攻击"
  - "安全评估基准"
  - "LLM智能体安全"
  - "规避攻击"
  - "智能体漏洞分析"
relevance_score: 9.0
---

# Benchmarking Autonomous Agents against Temporal, Spatial, and Semantic Evasions

## 原始摘要

As autonomous agents (e.g., OpenClaw) increasingly operate with deep system-level privileges to execute complex tasks, they introduce severe, unmitigated security risks. Current vulnerability analyses overwhelmingly focus on single-turn, stateless behaviors, overlooking the expanded attack surface inherent in stateful, multi-turn interactions and dynamic tool invocations. In this paper, we propose a novel, multi-dimensional evasion framework targeting LLM-based agent systems. We introduce three stealthy attack vectors: (1) Temporal evasion, which fragments malicious payloads across sequential interaction turns; (2) Spatial evasion, which conceals payloads within complex external artifacts that evade standard LLM parsing mechanisms; and (3) Semantic evasion, which obscures malicious intents beneath benign contextual noise. To systematically quantify these threats, we construct A3S-Bench, a comprehensive benchmark comprising 2,254 real-world agent execution trajectories. Evaluating a standard agent framework separately integrated with 10 mainstream LLM backbones against 20 practical threat scenarios, we demonstrate that our evasion framework elevates the average risk trigger rate from a 28.3\% baseline to 52.6\%. These findings reveal systemic, architecture-level vulnerabilities in current autonomous agent systems that existing defenses fail to address, highlighting an urgent need for defense mechanisms tailored to the unique threats.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有自主智能体系统（如OpenClaw）中未被充分认识的安全漏洞问题。研究背景是，随着这些智能体获得深度系统级权限来执行复杂任务，它们引入了严重且未缓解的安全风险。当前漏洞分析主要集中于单轮、无状态行为，忽略了有状态、多轮交互和动态工具调用所固有的更广泛攻击面。

现有方法的不足体现在：它们无法有效检测针对LLM智能体的多维度、隐蔽性逃避攻击，尤其是涉及跨轮次、跨外部工件以及利用上下文噪声的复杂攻击模式。

本文要解决的核心问题是：如何系统性地建模并量化针对LLM智能体的时间（跨交互轮次分段恶意负载）、空间（将负载藏于复杂外部工件）、语义（用上下文噪声掩盖恶意意图）这三种新型攻击向量带来的威胁。为此，论文提出了一个多维逃避框架，并构建了A3S-Bench基准（含2254条真实执行轨迹），以评估主流LLM后端在面对20种威胁场景时的脆弱性。实验表明，该逃避框架能将平均风险触发率从28.3%提升至52.6%，揭示了现有防御无法解决的系统性架构级漏洞。

### Q2: 有哪些相关研究？

相关研究可分为测评基准、攻击方法和安全分析三类。在测评基准方面，InjecAgent和AgentDojo评估间接提示注入，AgentHarm测试有害多步任务，ToolEmu、ASB和R-Judge考虑了多轮交互或多攻击向量，但均针对固定工具集、无状态会话和模拟环境。本文的A3S-Bench涵盖真实执行轨迹、多轮攻击和联合安全-效用评估，弥补了这些基准在数据集规模和攻击向量多样性上的不足。在攻击方法方面，PASB形式化了内存投毒和工具返回欺骗，BadAgent展示了后门注入，但本文首次系统提出时间（跨轮次碎片化）、空间（嵌入复杂工件逃避解析）和语义（通过上下文噪声隐藏意图）三个维度的逃逸框架，实现了更高的风险触发率（从28.3%提升至52.6%）。在安全分析方面，ClawSafety发现模型级安全不迁移到智能体级，Wang等人指出风险由骨干模型和智能体脚手架共同决定，Claw-Eval广泛评估了OpenClaw可信度但未涉及对抗注入。本文通过2，254条真实轨迹和10个主流LLM的评测，揭示了现有防御无法解决的架构级漏洞，特别是针对持续状态和系统级权限的新型威胁。

### Q3: 论文如何解决这个问题？

该论文通过构建一个多维度的对抗性评估框架A3S-Bench来系统性地量化自主智能体的安全风险。核心方法包括三个部分：首先，提出一个风险分类体系，将安全问题分为边界突破、状态破坏和有害操作三大类，细分为10个风险类别。其次，设计了三类高级规避攻击策略：时间维度上的跨轮次碎片化，将恶意载荷分散在多个交互轮次中，使得单轮检查无法检测；空间维度上的检测范围规避，将载荷隐藏在外部工作区文件内，绕过基于对话的监控；语义维度上的良性上下文隐藏，将恶意意图嵌入合法操作流程中。最后，开发了自动化数据合成管道，通过种子生成、种子筛选和载荷注入三个阶段，生成了包含2,254条真实执行轨迹的基准测试集。该框架的创新点在于：首次系统性地利用自主智能体的多轮交互、工具调用和持久化状态等特性来构建攻击向量，揭示了从28.3%基线到52.6%的风险触发率提升，证明了现有防御机制在架构层面存在系统性漏洞。

### Q4: 论文做了哪些实验？

论文构建了A3S-Bench基准测试，包含2,254条多轮对话轨迹（742条良性种子和1,512条对抗样本），覆盖6种使用场景、10类风险类别和两种难度级别（基础22种技术、高级12种技术）。实验采用三种注入模式：单轮直接（48.5%）、单轮间接（30.7%）和多轮（20.8%）。评估了10个主流通用大语言模型作为OpenClaw后端，包括2个专有模型（Claude Sonnet 4.5、GPT-5.2）和8个开放权重模型（Kimi-K2.5、MiniMax-M2.5、GLM-5、DeepSeek-V3.2、DeepSeek-V4-Flash、Qwen3.5系列的397B/122B/35B）。采用LLM-as-judge方法（Claude Opus 4.5，温度0），沿三个维度评估：任务完成率（TCR，效用分数≥4的比例）、风险触发率（RTR@1/2/3，N=3次独立运行中至少k次触发）、以及通用安全评分（GSS，1-5分）。主要结果显示，所提出的多维度规避框架（时间、空间、语义规避）将平均风险触发率从基线28.3%提升至52.6%，揭示了当前自主智能体系统中系统级架构漏洞，现有防御措施无法应对。

### Q5: 有什么可以进一步探索的点？

该论文揭示了自主智能体在时序、空间和语义维度上的新型规避攻击，但仍存在若干可深入探索的方向。首先，论文仅考虑了单次会话内的多轮攻击，未来可研究跨会话持久性攻击——攻击者通过污染长期记忆或配置文件，在用户重启智能体后仍能触发恶意行为。其次，当前防御实验仅测试了现有关闸模型和系统更新，可设计更高效的动态防御机制，如基于注意力机制的跨轮次意图连贯性检测、对外部工件进行结构化解析的沙箱、以及上下文漂移监测。再者，论文主要针对OpenClaw框架，不同智能体架构（如基于计划-执行循环、反思型推理）的防御鲁棒性差异值得对比。此外，可探索对抗训练方法，在合成数据中注入多轮规避样本以增强模型对其的识别能力。最后，实际部署场景中用户行为存在噪音，研究如何在确保安全的同时降低误报率也是重要方向。

### Q6: 总结一下论文的主要内容

该论文研究了自主Agent系统在时间、空间和语义三个维度上的安全漏洞。作者定义了问题：现有安全分析主要针对单轮、无状态行为，忽视了多轮交互和动态工具调用带来的攻击面。方法上，提出了多维逃逸攻击框架，包括时间逃逸（跨轮分片恶意负载）、空间逃逸（将负载隐藏于复杂外部工件）和语义逃逸（用良性上下文噪声掩盖恶意意图）。构建了A3S-Bench基准，包含2254条真实执行轨迹，评估了10种主流LLM骨干网络。主要结论：该逃逸框架将平均风险触发率从28.3%基线提升至52.6%，揭示了现有自主Agent系统存在系统性架构级漏洞，且现有防御措施难以应对，突显了针对这些特殊威胁设计防御机制的迫切需求。
