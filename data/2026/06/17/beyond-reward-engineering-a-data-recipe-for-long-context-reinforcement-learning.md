---
title: "Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning"
authors:
  - "Xiaoyue Xu"
  - "Sikui Zhang"
  - "Xiaorong Wang"
  - "Xu Han"
  - "Chaojun Xiao"
date: "2026-06-17"
arxiv_id: "2606.18831"
arxiv_url: "https://arxiv.org/abs/2606.18831"
pdf_url: "https://arxiv.org/pdf/2606.18831v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Long-Context RL"
  - "Data-Centric RL"
  - "Outcome-Based GRPO"
  - "Agentic Task Transfer"
relevance_score: 9.5
---

# Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning

## 原始摘要

Long-context reasoning is an essential capability for large language models, particularly when they are deployed as autonomous agents that must reason over lengthy trajectories. Reinforcement learning (RL) has recently emerged as a dominant paradigm for improving this ability, yet existing work largely focuses on reward engineering while diverse training data remains scarce. We revisit this problem from a data-centric perspective and show that a simple yet effective data recipe alone, paired with a minimal outcome-based GRPO setup, suffices to substantially improve long-context reasoning. Our recipe targets three complementary task families -- retrieval, multi-evidence synthesis, and reasoning -- for which we construct and curate eight datasets totaling ~14K examples. Experiments on three models (Qwen3-4B/8B/30B-A3B) yield average gains of +7.2/+3.2/+6.4 points across seven long-context benchmarks, surpassing prior RL training sets. We further demonstrate that these gains transfer to agentic tasks, where continuing RL training on an agent-tuned model with our data recipe improves GAIA by +4.8 and BrowseComp by +7.0 points. We will release our datasets to facilitate future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在长上下文推理任务中性能不足的问题，尤其是在模型作为自主智能体需要处理长轨迹时。当前研究背景是，强化学习已被证明能有效提升模型的推理能力，但多数工作聚焦于短上下文任务。现有方法的不足在于：一方面，仅使用结果奖励信号对于长上下文任务过于稀疏，难以引导模型在长输入中定位关键证据，导致上下文召回率停滞且出现捷径推理；另一方面，现有研究多集中于奖赏工程，即设计辅助信号来显式评估证据定位或中间推理，而高质量训练数据却十分稀缺——现有合成数据要么任务覆盖狭窄，要么未开源。本文从数据中心的视角出发，假设长上下文推理可分解为若干互补的核心能力，并基于此构建了覆盖检索、多证据综合和推理三类任务的简单数据方案，配合基础的结果型GRPO设置，无需任何特殊奖赏工程，即可显著提升模型的长上下文推理能力。核心问题是：通过精心构建多样化训练数据，而非复杂的奖赏设计，能否有效增强大语言模型的长上下文推理性能以及向智能体任务的迁移能力。

### Q2: 有哪些相关研究？

相关研究主要集中在长上下文推理的后训练方法上，可按方法论和应用场景分为以下几类：

1. **方法类（算法中心）**：这类工作改进RL训练流程，如补充中间步骤质量的辅助奖励信号（超越仅用结果奖励的RLVR），以及优化策略更新或选择性权重更新。本文与它们不同的是，不依赖复杂奖励工程，而是聚焦数据本身，用简单的基于结果的GRPO设置即可有效。

2. **数据类（数据中心）**：现有工作如DocQA-RL（约1.6K文档QA）、LoongRL（通过KeyChain UUID管道合成）、以及基于原子技能分解构建数据集。然而这些数据集规模有限、多样性不足或仅覆盖单一合成任务格式。本文贡献了一个更统一的数据配方，覆盖检索、多证据合成和推理三种互补核心能力，包含8个数据集约1.4万样本，显著超越先前RL训练集。

3. **应用与评测类**：在SFT方面，LongAlign构建长指令遵循数据集，ACC编译长智能体轨迹；而本文进一步证明其数据配方能迁移至智能体任务（如GAIA和BrowseComp），并通过继续RL训练带来显著提升。本文的主要区别在于数据来源多样（非单一合成）、任务类型互补，且跨多个长上下文基准和智能体场景验证了泛化性。

### Q3: 论文如何解决这个问题？

该论文采用数据驱动的策略，核心方法是设计一套聚焦三种互补能力的数据配方，并结合极简的结果导向强化学习（GRPO）设置，而非依赖复杂的奖励工程设计。

整体框架包含两个核心部分：一个精心构建的长上下文训练数据混合集，以及一个简化的RL训练流程。数据配方针对检索、多证据合成和推理三种能力，构造并整理了8个数据集，共约1.4万样本。

关键技术包括：
1. **检索任务**：设计了FuzzyNeedle（通过同义改写消除词汇匹配捷径）和MultiNeedle（从多个相似“针”中按顺序检索目标）两个数据集，克服模型依赖关键词匹配和面对大量分散信息时性能下降的问题。
2. **多证据合成任务**：设计了CrossEntity（要求跨实体聚合衍生属性）、WebSearch（通过桥接关系链进行多跳搜索并排除干扰项）、MultiQuery（要求不遗漏任何证据点）、KeyChain（通过UUID链追踪问题）以及从HotpotQA等改编的长文档QA，共同解决表面形式捷径、覆盖不全和干扰混淆三大缺陷。
3. **推理任务**：构造了LongMath数据集，将困难数学问题的变量和条件分布到长故事片段中，并散布于无关长文档，以在长上下文中保留深度推理能力。

在训练流程上，论文采用GRPO，并使用任务平衡采样和任务级优势归一化来稳定多数据集训练。奖励设计则简单有效，大部分使用词级别的召回率奖励，对CrossEntity和LongMath则使用LLM作为裁判进行评估。这一方法在三个模型上平均提升了+7.2/+3.2/+6.4个点，并有效迁移到智能体任务。

### Q4: 论文做了哪些实验？

论文在三个基座模型（Qwen3-4B/8B/30B-A3B）上进行了强化学习实验，训练采用GRPO方法，使用Miles框架，每个prompt采样8个rollout，输入长度上限64K token，生成长度16K token，学习率1e-6。评估使用了七个长上下文基准测试，分为三组：多跳QA（LongBench v1 QA五个子集和FRAMES）、整体长上下文推理（LongBench v2、AA-LCR、DocFinQA）和合成长上下文推理（LongReason、GraphWalks）。对比方法包括DocQA-RL-1.6K和KeyChain-15K两个现有的RL训练数据集。主要结果表明：在Qwen3-4B/8B/30B-A3B上分别获得平均+7.2/+3.2/+6.4分的提升，显著优于基线。具体地，在挑战性基准上表现突出，如Qwen3-4B在LongBench v2、AA-LCR和DocFinQA上分别提升+7.0、+10.5和+8.6分。消融实验验证了所有三类数据（检索、多证据合成、推理）都贡献了提升，全部使用达到最佳平均分57.58。此外，在64K训练上限下，模型能泛化到更长上下文（512K+仍有+2.1增益），并在代理任务GAIA和BrowseComp上分别提升+4.8和+7.0分。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要包括：实验仅限Qwen3系列模型（最大30B-A3B），未在更大模型或其他架构上验证；RL训练限制在64K token输入，未探索更长序列场景；大部分数据集为合成数据，可能与真实长上下文分布存在偏差；智能体迁移研究仅基于一个模型和两个基准，结论不够广泛。未来可探索的方向包括：将数据配方扩展到更大规模模型（如>100B参数）以及DeepSeek、Llama等其他系列；突破64K token限制，验证超长上下文（如128K+）下的效果；引入真实世界的长上下文数据（如法律文档、科研论文）提升泛化性；设计更智能的合成数据生成策略，结合难例挖掘和课程学习；深入研究长上下文推理与智能体任务之间的具体关联机制，例如分析推理链长度、检索精度与智能体成功率的关系；探索多任务联合训练或自适应数据混合策略，以进一步提升效率。

### Q6: 总结一下论文的主要内容

这篇论文针对大语言模型在长上下文推理中过度依赖奖励工程设计的问题，提出了一种以数据为中心的简单但有效的解决方案。其核心贡献在于，通过精心设计包含检索、多证据合成和推理三个互补任务家族的数据配方（共约1.4万样本），配合最简化的基于结果的GRPO训练设置，即可显著提升模型的长上下文推理能力。在Qwen3-4B/8B/30B-A3B三个模型上的实验显示，该方法在七个长上下文基准测试中平均提升了+7.2、+3.2和+6.4个点，超越了以往的RL训练集。主要结论是，这种提升能够有效迁移到智能体任务中，在GAIA和BrowseComp上分别获得了+4.8和+7.0的提升，表明强化核心长上下文能力是增强模型智能体能力的有力途径。这项工作为未来长上下文RL研究提供了一个关键且可复现的数据基准，推动了该领域的实用化发展。
