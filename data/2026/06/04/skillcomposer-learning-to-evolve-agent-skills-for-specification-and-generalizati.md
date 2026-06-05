---
title: "SkillComposer: Learning to Evolve Agent Skills for Specification and Generalization"
authors:
  - "Qi Zhang"
  - "Zhaopeng Feng"
  - "Xiaonan Shi"
  - "Xiaomeng Hu"
  - "Chu Liu"
  - "Pengjun Xie"
  - "Xiaobin Wang"
  - "Jieping Ye"
  - "Bryan Hooi"
  - "Haobo Wang"
  - "Junbo Zhao"
date: "2026-06-04"
arxiv_id: "2606.06079"
arxiv_url: "https://arxiv.org/abs/2606.06079"
pdf_url: "https://arxiv.org/pdf/2606.06079v1"
categories:
  - "cs.CL"
tags:
  - "Agent技能进化"
  - "技能规范与泛化"
  - "技能组合与自适应推理"
  - "推理性技能构建"
  - "LLM Agent技能库"
relevance_score: 9.5
---

# SkillComposer: Learning to Evolve Agent Skills for Specification and Generalization

## 原始摘要

Agent skills, which consist of reusable strategies that guide agent reasoning and action, have shown strong potential for improving model capability at inference time. However, current skill construction methods treat the problem as one-shot extraction, overlooking a fundamental tension: a skill tailored to the specific task fails to transfer, while the abstracted skill often provides insufficient guidance. We attribute this fragility to the absence of explicit mechanisms for skill specification and generalization. To address this gap, we introduce SkillComposer, a framework that decomposes skill construction into three learnable operations: create, improve, and merge. Trained via systematic rejection sampling recipe, SkillComposer enables language models to self-evolve skills at inference time and supports three deployment modes: offline for building generalized libraries, online for task-specific refinement, and hybrid for combining both. Comprehensive experiments on $τ^2$-Bench, LiveCodeBench v6, and AppWorld show that SkillComposer consistently outperforms baselines. Our SkillComposer-4B improves a 27B executor by up to +4.5 on agent tasks and +3.4 on code tasks, while generalizing across domains and task types unseen during training. Analysis reveals that merge and improve address orthogonal quality dimensions and that skill composition is a transferable meta-ability, providing a practical recipe for skill-augmented inference.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前基于智能体技能（agent skills）的推理增强方法中存在的核心矛盾：技能构建被当作一次性提取任务，缺乏对技能特化（specification）与泛化（generalization）的显式机制。现有方法主要依赖高质量人工编写或从成功轨迹中提取程序化知识，但前者成本高昂且难以扩展，后者则导致模型自主生成的技能质量有限，甚至产生负面效果。具体而言，一个为特定任务定制的技能往往无法迁移至其他场景，而过度抽象的技能又因缺乏具体指导而效果不佳。这种脆弱性根源于技能构建过程中缺少两项关键能力：既能通过抽象将相似任务经验整合为可迁移的策略（泛化），又能根据具体任务模式调整技能细节（特化）。为此，论文提出SkillComposer框架，将技能构建分解为三个可学习的操作：创建（从轨迹中提取程序化知识）、改进（针对新执行经验细化技能）和合并（融合语义相近的技能以增强泛化性）。通过拒绝抽样训练机制，这些操作使语言模型能在推理时自主进化技能，并支持离线构建通用库、在线实时特化、以及混合部署三种模式，最终在多种基准测试中显著提升模型性能并展现跨领域泛化能力。

### Q2: 有哪些相关研究？

在相关研究方面，本文首先回顾了**Agent技能与技能库**领域的工作。例如，**SkillX**通过提取轨迹构建分层技能并利用执行反馈精炼，**SkillRL**通过强化学习让技能库与智能体策略共同进化，还有工作将文本技能升级为可执行程序函数。这些研究主要将技能视为外部产物，依赖人工编写、成功轨迹或外部优化，而**SkillComposer**将技能构建视为模型自身的可学习能力。

其次，在**技能进化与质量控制**方面，**EvoSkill**通过迭代失败分析发现并编辑技能，**CoEvoSkills**结合技能生成器与代理验证器构建多文件技能包，**SkillClaw**通过跨用户交互轨迹集体精炼共享技能库。同时，基准研究揭示了技能益处的脆弱性：精心策划的技能可显著提升智能体，但自生技能可能无增益，且在现实检索与适配条件下性能下降。不同于这些工作的静态或外部优化思路，**SkillComposer**将技能构建分解为三个可训练操作（创建、改进、合并），并通过基于增量通过率的拒绝采样监督进行学习，使技能进化成为语言模型的内在能力，分别驱动技能的特化与泛化，并支持离线、在线和混合三种部署模式。

### Q3: 论文如何解决这个问题？

SkillComposer通过将技能构建分解为可学习的三个核心操作来解决技能特异性和泛化性之间的张力:Create(创建)、Merge(合并)和Improve(改进)。整体框架包含技能库构建和推理时演化两个阶段。在技能库构建阶段,Create操作从原始轨迹中提取可复用技能;Merge操作通过多视角相似度计算(对名称、描述和主体三部分计算相似度并取均值)识别语义相似的技能对,合并为更通用的单一技能,防止技能库无限制膨胀。Improve操作则基于执行经验对已有技能进行迭代精炼,以捕捉新发现的模式。关键技术在于采用拒绝采样训练策略,以增量通过率(Delta Pass Rate)作为统一质量信号——只有当候选技能在评估任务上提升执行器的pass@1超过阈值时才被保留为训练样本。其中,Improve同时考虑同任务和跨任务评估以兼顾规格化和泛化能力。方法支持三种部署模式:离线模式预构建通用技能库并在推理时检索和自选择;在线模式对每个新任务逐次创建并迭代改进;混合模式结合两者优势,从离线库出发进行在线演化。实验表明,SkillComposer-4B能提升27B执行器在Agent任务上最多4.5个点、代码任务上3.4个点,且Merge和Improve覆盖了正交的质量维度,技能组合能力是可迁移的元技能。

### Q4: 论文做了哪些实验？

论文在三个基准测试上进行了评估。实验设置：使用7,000条SFT数据微调Qwen3.5-4B作为SkillComposer，用vllm运行技能执行器和SkillComposer，技能执行器分别为Qwen3.5-4B和Qwen3.5-27B。数据集/基准测试包括：(1) τ²-Bench（多轮智能体基准，含Retail、Airline、Telecom三个域，仅Retail用于训练）；(2) LiveCodeBench v6（无污染代码生成基准，分Easy、Medium、Hard）；(3) AppWorld（交互式智能体基准，用于跨任务泛化测试）。对比方法为No Skill（原始LLM）和MemP（从有效轨迹提取程序记忆）。主要结果：在4B执行器上，SkillComposer在混合模式下τ²-Bench总分最高（85.7，比No Skill高+6.2），在线模式下LiveCodeBench总分最高（59.1，比No Skill高+2.5）。在27B执行器上，SkillComposer-4B在线模式在τ²-Bench达88.0（+4.5），LiveCodeBench达83.1（+3.4）。跨域泛化方面，Airline域（训练中未见）最高提升+13.7（4B混合模式达82.5），Telecom域最高+4.4（27B在线模式98.8）。

### Q5: 有什么可以进一步探索的点？

未来可探索的方向包括：首先，当前拒绝采样流程计算开销大，可探索更高效的训练数据收集方法，例如利用模型自身生成反馈或引入强化学习来简化采样过程。其次，实验仅局限在Qwen3.5系列，未来应在更多架构和规模（如Llama、GPT系列）上验证SkillComposer的泛化能力。在操作层面，离线场景下Skill Improve反而降低迁移性，表明需进一步优化specification与generalization的平衡，例如设计动态切换机制，让模型根据任务特性自动选择提升或合并操作。此外，当前技能库的构建主要依赖手工回合数，可探索自适应终止条件，当技能不再显著改善性能时停止迭代。最后，技能组成的跨任务迁移已得到初步验证，但跨领域（如从代码到多步推理）的泛化机制仍待深入，可引入元学习框架来加速新领域的技能演化过程。

### Q6: 总结一下论文的主要内容

这篇论文提出了SkillComposer，一个将智能体技能构建分解为“创建”、“改进”和“合并”三种可学习操作的框架。当前方法面临技能要么过于具体导致无法泛化，要么过于抽象导致指导不足的根本矛盾，缺乏对技能特化与泛化的明确机制。SkillComposer通过delta通过率引导的拒绝采样来训练这些操作，使语言模型能在推理时自我演化技能，并支持三种部署模式：离线构建通用技能库、在线进行任务特定细化以及混合模式。在τ²-Bench、LiveCodeBench v6和AppWorld上的综合实验表明，SkillComposer一致优于基线方法，例如4B模型可提升27B执行器在智能体任务上最高4.5分。分析揭示，“合并”驱动泛化而“改进”驱动特化，技能组合是一种可迁移的元能力，为技能增强推理提供了实用方案。
