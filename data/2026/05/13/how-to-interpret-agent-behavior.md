---
title: "How to Interpret Agent Behavior"
authors:
  - "Jie Gao"
  - "Kaiser Sun"
  - "Jen-tse Huang"
  - "Katherine Van Koevering"
  - "Sijie Ji"
  - "Heyuan Huang"
  - "Weiyan Shi"
  - "Zhuoran Lu"
  - "Ziang Xiao"
  - "Daniel Khashabi"
  - "Mark Dredze"
date: "2026-05-13"
arxiv_id: "2605.13625"
arxiv_url: "https://arxiv.org/abs/2605.13625"
pdf_url: "https://arxiv.org/pdf/2605.13625v1"
categories:
  - "cs.AI"
tags:
  - "Agent行为分析"
  - "Agent可解释性"
  - "行为分类学"
  - "运行时追踪"
  - "Agent调试与监控"
relevance_score: 8.5
---

# How to Interpret Agent Behavior

## 原始摘要

Autonomous agents such as Claude Code and Codex now operate for hours or even days. Understanding their runtime behavior has become critical for downstream tasks such as diagnosing inefficiencies, fixing bugs, and ensuring better oversight. A primary way to gain this understanding is analyzing the reasoning trajectories and execution traces these agents generate. Yet such data remains in unstructured natural-language form, making it difficult for humans to interpret at scale. We introduce ACT*ONOMY (a combination of Action and Taxonomy), a taxonomy for describing and analyzing agent behavior at runtime. ACT*ONOMY has two components: (1) the taxonomy itself, developed through Grounded Theory and structured as a three-level hierarchy of 10 actions, 46 subactions, and 120 leaf categories; and (2) an open repository that hosts the living taxonomy, provides an automated analysis pipeline that applies it to agent trajectories analysis, and defines an extension protocol for customization and growth. Our experiments show that ACTONOMY can compare behavioral profiles across agents and characterize a single agent's behavior across diverse trajectories, surfacing patterns indicative of failure modes. By providing a shared vocabulary, ACT*ONOMY helps researchers, agent designers, and end users interpret agent behavior more consistently, enabling better oversight and control.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决解释和理解自主智能体运行时行为的难题。研究背景是，随着Claude Code、Codex等自主智能体能够长时间（数小时甚至数天）自主运行并执行复杂任务，理解其行为对于诊断效率低下、修复错误以及实现有效监督变得至关重要。当前的主要分析手段是检查智能体生成的推理轨迹和执行轨迹，这些数据能够揭示智能体的规划、推理和工具使用过程。然而，现有方法存在显著不足：一方面，传统的定量指标（如任务成功率）只能判断智能体是否成功，却无法解释其成功或失败的原因；另一方面，新兴的定性分析虽然通过人工阅读轨迹来理解行为，但面临两大挑战：轨迹是以非结构化的、自由形式的自然语言文本呈现，难以规模化地被人理解；同时，研究社区尚未就描述智能体行为达成一个共享的概念与词汇体系，导致研究发现难以交流和积累。因此，本文提出ACT*ONOMY，一个用于描述和分析智能体运行时行为的层次化分类体系，旨在提供一个共享的词汇表，使研究者、设计者和终端用户能够更一致地解释智能体行为，识别故障模式，并最终实现更好的监督与控制。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**代理轨迹分析**，现有工作如AgentBench、AgentBoard和SWE-bench主要依赖定量结果指标（如任务成功率），但无法解释代理行为的“如何”与“为何”。Cemri等人的工作仅分类了多代理失败模式，Kapoor等人编目了可靠性差距，而少数针对特定代理（如SWE-agent）的手动分析术语不通用。本文提出的ACT*ONOMY填补了这一空白，提供一个跨系统通用的描述性分类体系，并通过自动化流程将非结构化的代理轨迹转化为可读的行为画像。

第二类是**动作空间与认知架构框架**，如CoALA将语言代理组织为外部动作和内部动作，Newell的认知统一理论提供了认知的操作标准，WorldAPIs从wikiHow教程归纳原始API。这些工作提供了理论视角，但缺乏用于运行时轨迹分析的共享描述词汇。ACT*ONOMY基于认知架构理论并融合AI研究者的行为描述，构建了10个动作、46个子动作的层次化分类。

第三类是**基于LLM的定性编码**，传统定性方法（如扎根理论）可将非结构化数据转化为结构化词汇，且近期研究表明LLM可扩展此流程。本文结合了两者：通过人工定性编码从代理论文归纳分类，同时提供LLM作为定性编码器的自动化管道（AutoTraceQDA），实现大规模行为分析。

### Q3: 论文如何解决这个问题？

ACT*ONOMY通过构建分层的动作分类体系和自动化分析管线来解决智能体行为解释问题。核心是建立了一个三级分类体系：10个顶级动作、46个子动作和120个叶子类别，涵盖推理、执行、规划、评估、检索等核心行为维度。该分类体系采用扎根理论开发，并作为开放仓库持续演进。

关键技术是AutoTraceQDA自动化分析管线，包含五个步骤：1)预处理阶段将任意框架（如SWE-agent、AG2）的轨迹解析为"观察-思考-动作"三元组序列；2)行为指标提取阶段识别思考和动作中的行为相关片段；3)基于LLM的代码本分配阶段为每个片段标注三级类别标签，当无合适标签时主动提议扩展代码本；4)聚合汇总阶段计算统计数据、分割会话并生成自然语言摘要；5)最终生成可交互的行为画像。该管线通过迭代优化达到与人工编码高度一致（Cohen's κ>0.81）。

创新点在于：1)提供了标准化的行为描述词汇，使跨智能体比较和单一智能体行为特征分析成为可能；2)自动分析能发现人工分析遗漏的行为模式，如SWE-agent中非执行类动作的分布；3)叶子级别分析可揭示深层失败模式，如"未经验证就提交"的典型错误流程，为智能体调试和监控提供细粒度洞察。

### Q4: 论文做了哪些实验？

论文主要进行了两项实验。首先，为验证ACT*ONOMY的自动分析能力，实验选取了AG2、HyperAgent和SWE-Agent三种不同领域的智能体，从其公开轨迹中收集了300条轨迹，使用自动分析管线AUTOTRACEQDA为每个智能体生成了100个动作序列表征。实验对比了各智能体的行为分布及对平均行为的偏差（使用卡方检验的z分数）。结果显示，三者均以Reasoning和Executing行为为主，但AG2在Evaluating、Grounding和Deciding上显著高于平均，HyperAgent在Reflecting上显著高于平均，SWE-Agent在Executing上远高于平均，与各自任务特性一致。其次，为测试对单个智能体行为的分析能力，实验选取了SWE-agent在SWE-bench上的两条轨迹：成功修复的问题psf/requests-2317（10轮，33个标签）和失败的问题django/django-14411（16轮，53个标签）。通过逐轮动作分解和叶级标签分析，发现失败轨迹过度偏向Reasoning（22/53 vs Executing的14/53），且叶级分析揭示了一个“未验证就提交”的失败模式，该模式在原始人类分析中被忽略。整个分析管线在保留集上达到了人类编码者间高度一致性（Cohen's κ > 0.81）。

### Q5: 有什么可以进一步探索的点？

未来的探索可以从几个方向展开。首先，论文提出的行为分类法目前是独立于模型内部机制的分析工具，一个自然且重要的延伸是将其与机械可解释性结合——例如，通过探针或稀疏自编码器定位“反思”或“规划”等行为对应的神经表征，从而搭建外在行为与内在状态之间的桥梁。其次，现有验证聚焦于少数场景，未来需要在更多样化的智能体（如具身机器人、多智能体协作系统）中评估分类法的通用性和覆盖率。此外，可推动其向监控应用发展：利用行为画像进行回归测试、检测生产环境中的行为漂移，或对长时运行智能体进行实时干预。最后，分类法本身需要社区驱动的动态演进，例如通过协议支持用户自定义子类，以适应新涌现的行为模式，同时维持核心层级的一致性。

### Q6: 总结一下论文的主要内容

本文提出ACT*ONOMY，一个用于解释智能体运行时行为的系统化分类体系。针对自主智能体（如Claude Code、Codex）运行数小时甚至数天的场景，当前对其行为模式的理解因数据非结构化而难以规模化分析。核心贡献包括：（1）基于35篇论文（2024-2026）的行为描述和认知架构理论，通过扎根理论构建三级分类体系（10个动作、46个子动作、120个叶节点）；（2）开源仓库提供自动化分析管线（AutoTraceQDA）和扩展协议，支持对轨迹的引用式标注和社区定制。实验表明该分类法能跨智能体比较行为特征，并揭示单一智能体在多样轨迹中的故障模式。意义在于通过共享词汇表，使研究人员、设计者和用户更一致地解释智能体行为，从而改善监督和控制。
