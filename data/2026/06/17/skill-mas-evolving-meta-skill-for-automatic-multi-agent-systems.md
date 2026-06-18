---
title: "Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems"
authors:
  - "Hehai Lin"
  - "Qi Yang"
  - "Chengwei Qin"
date: "2026-06-17"
arxiv_id: "2606.18837"
arxiv_url: "https://arxiv.org/abs/2606.18837"
pdf_url: "https://arxiv.org/pdf/2606.18837v1"
categories:
  - "cs.MA"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Multi-Agent Systems"
  - "Meta-Skill Learning"
  - "Experience Optimization"
  - "LLM-based Agents"
  - "Automatic Agent Generation"
relevance_score: 9.5
---

# Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems

## 原始摘要

Large Language Model (LLM)-based automatic Multi-Agent Systems (MAS) generation has become a crucial frontier for tackling complex tasks. However, existing methods face a dilemma between model capability and experience retention. Inference-time MAS leverages frozen frontier LLMs but repeats identical searches without learning from past experience. Conversely, Training-time MAS internalizes experience via gradient updates but is constrained by the low capability ceiling of smaller models, and is hard to scale to large frontier LLMs. To bridge this gap, we propose Skill-MAS, a novel third path that decouples experience retention from parametric updates by conceptualizing the high-level orchestration capability as an evolvable Meta-Skill. Skill-MAS refines this architectural knowledge through a closed optimization loop: (1) Multi-Trajectory Rollout samples a behavioral distribution for each task under the current Meta-Skill; and (2) Selective Reflection adaptively selects priority tasks and applies hierarchical contrastive analysis to distill systemic experience into generalizable, strategy-level principles. Extensive experiments across four complex benchmarks and four distinct LLMs demonstrate that Skill-MAS not only achieves remarkable performance gains but also maintains a favorable cost-performance trade-off. Further analysis reveals that the evolved Meta-Skills are highly robust and exhibit strong transferability across unseen tasks and different LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有基于大语言模型的自动多智能体系统（MAS）生成方法在模型能力与经验保留之间的两难困境。当前方法主要分为两类：一是推理时MAS，它利用冻结的前沿大模型进行搜索，虽具备强大推理能力，但缺乏记忆机制，无法从过往经验中学习，导致重复执行相同搜索。二是训练时MAS，通过微调小型模型（如7B参数）来内化经验，但受限于小型模型的能力上限，难以扩展到具备最强推理能力的大型前沿模型（>100B），且需要大量高质量训练数据。为弥补这一鸿沟，本文提出Skill-MAS，开创性地将高层编排能力概念化为一种可进化的“元技能”（Meta-Skill），从而将经验保留与参数更新解耦。其核心思想是：不更新模型参数，而是通过一个闭环优化过程（包括多轨迹展开和选择性反思）不断提炼和进化元技能，使冻结的前沿大模型能够渐进式地学习并改进其编排专长。最终，该方法旨在实现高性能模型与经验可累积性的有效结合，并取得更优的成本-性能平衡。

### Q2: 有哪些相关研究？

相关研究可分为三类：**推理时方法**、**训练时方法**和**技能演化方法**。  
推理时方法（如AFlow、EvoAgent、AOrchestra、MAS-Zero）利用冻结的前沿大模型作为元智能体，通过搜索算法（如蒙特卡洛树搜索）或进化原则生成多智能体系统，但每次迭代重复相同搜索，缺乏对历史经验的学习。  
训练时方法（如ScoreFlow、MAS$^2$、MAS-Orchestra）通过梯度更新（如直接偏好优化、GRPO）让小模型内化经验，但受限于小模型能力上限，且难以扩展至百亿参数级前沿模型。  
技能演化方法（如MemSkill、Trace2Skill、Skill0、D2Skill、SKILLRL）专注于从单智能体场景中提取可复用的执行级技能（如记忆管理、多跳推理），并在多智能体系统中（如CoEvoSkills、EvoSkill）演化子智能体角色。  
本文与上述工作的本质区别在于：**Skill-MAS首次提出元技能（Meta-Skill）概念**，将元智能体的高级编排能力解耦为可演化的结构化知识，而非参数更新或固定搜索。它通过多轨迹采样和选择性反射的闭环优化，从历史编排经验中蒸馏出策略级原则，实现了跨任务和跨模型的可迁移性，填补了推理时与训练时方法之间的空白。

### Q3: 论文如何解决这个问题？

Skill-MAS通过引入元技能（Meta-Skill）的概念，将多智能体系统（MAS）生成中的经验保留与参数更新解耦，形成了一种不依赖梯度更新的进化优化路径。核心方法是一个闭环进化框架，包含三个主要模块：

1. **多轨迹展开（Multi-Trajectory Rollout）**：在每轮进化中，基于当前元技能，为每个验证任务采样K条完整轨迹。每条轨迹记录了MAS的生成过程、架构和最终得分，从而形成行为分布。由此计算每个任务的不确定性（得分标准差）和难度（负平均分），将单次结果转化为分布特征，为后续诊断提供依据。

2. **选择性反思（Selective Reflection）**：首先通过融合不确定性和难度计算优先级，并利用二阶差分法（类似肘部法则）自动选择信息量最大的任务子集，避免分析噪音。在选中的任务上执行双层反思：层内对比分析将轨迹分为高分和低分两组，通过LLM对比识别分歧点、成功因素和失败模式，生成每任务的补丁建议；层间综合则跨任务提取系统级共性的弱点和优点，形成结构化证据包，包含优先修复列表。

3. **技能优化（Skill Optimization）**：优化器根据证据包审查当前元技能，移除或重写无效规则，并严格在任务分解、智能体工程和工作流编排三个模块内进行局部修改。修改必须基于证据抽象成可泛化的策略原则而非任务特定补丁，通过结构有效性检查后作为下一轮的新元技能。

整个框架迭代R轮，选择验证性能最优的元技能用于测试集评估。创新点在于：将高层编排能力作为可进化的元技能，从行为分布中提取系统级经验，实现跨任务、跨模型的强迁移性，同时保持较小的参数开销。

### Q4: 论文做了哪些实验？

论文在四个复杂基准测试（DeepResearchBench、HLE-Math、BrowseComp-Plus、VITA）和四种LLM（Gemini-3.1-Flash、GPT-5.4-Nano、Qwen3.5-Plus、DeepSeek-V4-Flash）上评估了Skill-MAS。对比方法包括推理时MAS（EvoAgent、AOrchestra、AFlow）和训练时MAS（MAS²、MAS-Orchestra）。主要实验设置：采用初始元技能（Skill-MAS-init）和优化后元技能（Skill-MAS-optimized）进行评估，性能指标归一化到0-100%，成本以美元计。主要结果如下：

1. **总体性能**：Skill-MAS-optimized在所有LLM和基准上平均性能最高（如Gemini-3.1-Flash上29.49%，DeepSeek-V4-Flash上41.05%），显著优于最佳基线（如AFlow在Gemini上21.29%）。唯一例外是GPT-5.4-Nano的DeepResearchBench上EvoAgent略高（52.91% vs 48.90%）。

2. **消融实验**：增加多轨迹回滚数量（K=3,5,7）时性能持续提升，验证了元技能优化的有效性。

3. **迁移实验**：元技能跨LLM和跨任务迁移均显示正向增益（Δ>0）。无迁移场景增益最大（如GPT 5.4-Nano在BCP上Δ+7.74），跨LLM同任务迁移（如GPT→DeepSeek在BCP上Δ+2.97）和同LLM跨任务迁移（如GPT在BCP→VITA上Δ+7.15）表现良好，最难的是跨LLM且跨任务迁移（Δ最低为+1.19）。

4. **成本-性能权衡**：推理时MAS成本高（如EvoAgent在Gemini上单样本$8.20），训练时MAS性能差但成本低（如MAS²在GPT上$1.27）。Skill-MAS以中等成本取得了最佳性能（如Qwen3.5上$2.43，性能38.41%）。

### Q5: 有什么可以进一步探索的点？

Skill-MAS 在解耦经验保留与参数更新方面迈出了重要一步，但仍有几个值得进一步探索的方向。首先，其“选择性反思”机制依赖于“优先级任务”的选取标准，当前方法可能不够鲁棒或高效，未来可探索基于强化学习或主动学习的自适应优先级策略。其次，Meta-Skill的表示形式目前较为隐含（通过提示实现），若能将高层编排能力显式建模为可组合、可模块化的结构（如子技能图），可能提升其可解释性和泛化能力。再者，论文主要评估了跨LLM和跨任务的迁移，但对于任务复杂度剧变或出现全新交互模式时的零样本适应能力尚未充分分析。此外，当前仅在少数基准上测试，未来可在更动态、开放式的多智能体协作场景（如实时决策、对话生成）中验证其鲁棒性。最后，可以探索将Skill-MAS与轻量级参数微调结合，形成“经验-参数”混合进化框架，以兼顾小样本适应性与大规模泛化能力。

### Q6: 总结一下论文的主要内容

Skill-MAS提出了一种无需梯度更新即可增强多智能体系统能力的新方法。当前基于LLM的自动MAS存在两难：推理时方法使用冻结的前沿模型但无法积累经验，训练时方法通过梯度更新内化经验却受限于小模型能力。Skill-MAS通过将高级编排能力概念化为可进化的元技能，将经验保留与参数更新解耦。方法包含两个核心步骤：多轨迹展开，在当前元技能下采样行为分布；选择性反思，自适应筛选优先任务并应用层次对比分析，将系统经验提炼为可泛化的策略级原则。在四个复杂基准和四种不同LLM上的实验表明，Skill-MAS不仅实现了显著性能提升，还保持了良好的成本-性能平衡。进一步分析显示，进化后的元技能具有高度鲁棒性和强迁移性，能有效适用于未见过的任务和不同的LLM。这为解决LLM多智能体系统的经验积累与模型能力矛盾提供了新思路，无需更新模型参数即可实现系统级学习。
