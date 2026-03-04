---
title: "PRISM: Pushing the Frontier of Deep Think via Process Reward Model-Guided Inference"
authors:
  - "Rituraj Sharma"
  - "Weiyuan Chen"
  - "Noah Provenzano"
  - "Tu Vu"
date: "2026-03-03"
arxiv_id: "2603.02479"
arxiv_url: "https://arxiv.org/abs/2603.02479"
pdf_url: "https://arxiv.org/pdf/2603.02479v1"
categories:
  - "cs.AI"
tags:
  - "推理增强"
  - "过程奖励模型"
  - "种群优化"
  - "数学推理"
  - "科学推理"
  - "推理算法"
relevance_score: 7.5
---

# PRISM: Pushing the Frontier of Deep Think via Process Reward Model-Guided Inference

## 原始摘要

DEEPTHINK methods improve reasoning by generating, refining, and aggregating populations of candidate solutions, which enables strong performance on complex mathematical and scientific tasks. However, existing frameworks often lack reliable correctness signals during inference, which creates a population-enhancement bottleneck where deeper deliberation amplifies errors, suppresses correct minority solutions, and yields weak returns to additional compute. In this paper, we introduce a functional decomposition of DEEPTHINK systems and propose PRISM, a Process Reward Model (PRM)-guided inference algorithm that uses step-level verification to guide both population refinement and solution aggregation. During refinement, PRISM treats candidate solutions as particles in a PRM-defined energy landscape and reshapes the population through score-guided resampling and stochastic refinement, which concentrates probability mass on higher-quality reasoning while preserving diversity. Across mathematics and science benchmarks, PRISM is competitive with or outperforms existing DEEPTHINK methods, reaching 90.0%, 75.4%, and 71.4% with gpt-oss-20b on AIME25, HMMT25, and GPQA Diamond, respectively, while matching or exceeding gpt-oss-120b. Additionally, our analysis shows that PRISM produces consistent net-directional correction during refinement, remains reliable when the initial population contains few correct candidates, and often lies on the compute-accuracy Pareto frontier.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度思考（DeepThink）推理范式中，由于缺乏可靠的正确性信号而导致的“群体增强瓶颈”问题。研究背景是，以大型语言模型为基础的深度思考方法通过生成、精炼和聚合多个候选解决方案，在复杂数学和科学任务上表现出色，已成为数学奥林匹克等竞赛中的先进工具。然而，现有方法在推理过程中往往依赖整体答案的评估或多数投票，缺乏对推理步骤级别的验证，这导致现有框架存在明显不足：在迭代精炼种群时，错误可能被放大，而逻辑正确但出现频率低的少数解决方案则容易被抑制，使得增加计算资源（如更深度的精炼）无法可靠提升性能，计算效率低下。

本文的核心问题是：如何通过引入细粒度的正确性指导，来突破群体精炼的瓶颈，实现更高效、可靠的推理过程。为此，论文提出了PRISM方法，利用过程奖励模型（PRM）在推理步骤级别提供验证信号，从而引导种群精炼（通过类似马尔可夫链蒙特卡洛的采样与突变来集中概率质量于高质量推理路径）和最终解决方案的聚合。这旨在将随机重写转变为方向性的错误纠正，确保计算资源能有效转化为准确性的提升。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕深度思考（DeepThink）方法及其改进，可分为方法类、应用类和评测类。

在方法类研究中，相关工作主要包括：1）**人口创建方法**，如通过随机解码（如温度采样或核采样）独立生成多个候选解（Sample-N），或单次生成多个解并附带置信度信号（如语言化采样）。这些方法旨在提供多样性，但缺乏对正确解的聚焦。2）**人口增强方法**，包括批评引导的细化（使用批评器独立验证和修订候选解）、多智能体交互（智能体相互挑战和更新推理）、共识驱动更新（引导候选解朝向多数意见）以及基于聚合的细化（递归重组候选解）。这些方法试图提升人口质量，但常因缺乏可靠正确性信号而导致错误传播或正确少数解被抑制，形成“人口增强瓶颈”。3）**解决方案聚合方法**，如多数投票（Majority Vote）或基于LLM的聚合（LLM Aggregate），这些方法依赖人口增强阶段的质量，若候选集质量低，聚合可能放大噪声。

本文提出的PRISM方法与上述工作的关系和区别在于：它通过引入过程奖励模型（PRM）提供步骤级验证信号，直接针对人口增强瓶颈进行改进。PRISM在细化阶段将候选解视为PRM定义的能量场中的粒子，通过分数引导的重采样和随机细化来集中概率质量于高质量推理，同时保持多样性；在聚合阶段探索PRM引导的正确性感知聚合（PRM-score Vote）。相比现有方法，PRISM在数学和科学基准测试中表现更优，能实现一致的正向修正，并在初始人口中正确候选较少时仍保持可靠，从而更有效地利用计算资源提升准确性。

### Q3: 论文如何解决这个问题？

论文通过提出PRISM算法来解决DEEPTHINK方法在推理过程中缺乏可靠正确性信号的问题，其核心是利用过程奖励模型（PRM）提供的步骤级验证来指导候选解的种群精炼和最终聚合。整体框架将推理过程视为在PRM定义的能量景观中演化的粒子群优化问题，其中高质量推理对应低能量区域。

主要模块包括：1）**评分模块**：首先将候选推理轨迹规范化为明确的步骤表示，然后使用PRM生成步骤级反馈，并将其映射为一致性分数，再通过温度参数控制转换为重要性权重，从而定义能量景观。2）**种群管理模块**：通过计算有效样本大小（ESS）监控种群多样性，当多样性低于阈值时进行系统重采样，复制高权重候选解并淘汰低权重解，以重新分配计算资源并保持稳定性。3）**随机精炼模块**：采用类似Metropolis-Hastings的更新机制，使用迭代模型基于PRM反馈提出精炼后的轨迹，并以概率方式接受新轨迹，该概率由新旧轨迹的权重比决定，从而在倾向于提高分数的同时允许偶尔接受分数下降的移动，避免陷入局部最优。4）**聚合模块**：精炼后，通过PRM分数加权投票进行答案聚合，即对每个唯一答案汇总其支持轨迹的PRM分数，选择总分最高的答案，确保最终预测基于推理质量而非仅出现频率。

创新点在于：首先，将PRM的步骤级验证信号深度整合到精炼和聚合的全过程，突破了传统方法仅依赖最终答案正确性的瓶颈；其次，通过能量景观建模和随机精炼机制，实现了方向性错误校正与多样性探索的平衡，有效防止了正确少数解被抑制；最后，引入冲突仲裁和克隆限制等稳定机制，确保了种群动态的鲁棒性。这些设计使得PRISM能在初始种群中正确候选较少时仍保持可靠，并在计算精度帕累托前沿上取得优势。

### Q4: 论文做了哪些实验？

论文在三个数学和科学推理基准（AIME25、HMMT25和GPQA Diamond）上进行了实验，以评估PRISM方法的有效性。实验设置严格控制，所有方法共享相同的基础模型（主要使用gpt-oss-20b，并对比gpt-oss-120b及Qwen系列模型）、初始候选解数量（N=10）和迭代深度（T=5）。对比方法包括无精炼的简单投票、SciMaster、Agentic Debate、MAD Conformist、MAD Follower和Recursive Self-Aggregation等代表性深度思考方法。评估指标包括最终准确率、计算量（总token消耗）以及人口准确率、NetFlip（净方向性修正）等动态指标。

主要结果显示，PRISM在多数基准上达到或超越了现有最佳方法。具体数据指标如下：在AIME25上，PRISM结合PRM分数投票达到90.0%的准确率，优于Recursive Self-Aggregation的87.8%；在HMMT25上达到75.4%；在GPQA Diamond上达到71.4%。同时，PRISM使gpt-oss-20b的性能匹配甚至超过了gpt-oss-120b的零样本基线（例如在GPQA上超越69.7%）。分析表明，PRISM在精炼过程中能产生稳定的正向净修正（NetFlip为正值），在初始人口中正确解稀少时仍保持较高鲁棒性，并且在计算-准确率帕累托边界上常处于最优位置，实现了更高效的计算资源利用。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从以下几个方面深入探索。首先，PRISM依赖过程奖励模型（PRM）提供步骤级验证信号，但PRM本身的准确性和泛化能力存在上限，尤其在复杂、开放领域任务中可能无法可靠评估推理质量。未来可研究如何构建更鲁棒、可解释的PRM，或探索多模态、多角度验证机制以减少对单一评分器的依赖。

其次，方法在计算效率与性能提升间取得了较好平衡，但动态重采样和随机细化机制仍可能引入额外开销。未来可优化算法收敛速度，例如通过自适应调整迭代深度或引入轻量级候选解筛选策略，以在资源受限场景下保持高效性。

此外，PRISM在初始种群质量较低时表现出较强鲁棒性，但其“引导推理”机制在处理高度不确定或对抗性输入时的稳定性尚未充分验证。可探索如何集成不确定性量化技术，使系统能识别并处理置信度低的推理步骤，从而进一步提升容错能力。

最后，当前研究集中于数学和科学基准测试，未来可将框架扩展至更广泛的推理任务（如代码生成、复杂规划），并研究跨领域迁移能力。同时，探索PRM与其他深度思维方法（如辩论、自洽性检查）的协同效应，可能催生更强大的复合型推理系统。

### Q6: 总结一下论文的主要内容

该论文针对现有DEEPTHINK推理方法在推断过程中缺乏可靠正确性信号的问题，提出了PRISM框架。其核心贡献是引入过程奖励模型（PRM）来指导推理，通过步骤级验证来优化候选解的生成、精炼和聚合过程。具体方法上，PRISM将候选解视为PRM定义的能量场中的粒子，利用分数引导的重采样和随机精炼来重塑解群，从而在保持多样性的同时将概率质量集中在更高质量的推理路径上。实验表明，PRISM在数学和科学基准测试（如AIME25、HMMT25和GPQA Diamond）上达到或超越了现有DEEPTHINK方法的性能，甚至能以较小模型匹配更大模型的性能。主要结论是PRISM能实现持续的正向修正，在初始解群中正确候选较少时仍保持可靠，并且通常在计算-准确率帕累托前沿上表现优异，有效突破了深度思考推理中的群体增强瓶颈。
