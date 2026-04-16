---
title: "MUSE: Multi-Domain Chinese User Simulation via Self-Evolving Profiles and Rubric-Guided Alignment"
authors:
  - "Zihao Liu"
  - "Hantao Zhou"
  - "Jiguo Li"
  - "Jun Xu"
  - "Jiuchong Gao"
  - "Jinghua Hao"
  - "Renqing He"
  - "Peng Wang"
date: "2026-04-15"
arxiv_id: "2604.13828"
arxiv_url: "https://arxiv.org/abs/2604.13828"
pdf_url: "https://arxiv.org/pdf/2604.13828v1"
categories:
  - "cs.CL"
tags:
  - "用户模拟"
  - "强化学习"
  - "多轮对话"
  - "对齐"
  - "中文"
  - "多领域"
  - "评估"
  - "训练数据"
relevance_score: 7.5
---

# MUSE: Multi-Domain Chinese User Simulation via Self-Evolving Profiles and Rubric-Guided Alignment

## 原始摘要

User simulators are essential for the scalable training and evaluation of interactive AI systems. However, existing approaches often rely on shallow user profiling, struggle to maintain persona consistency over long interactions, and are largely limited to English or single-domain settings. We present MUSE, a multi-domain Chinese user simulation framework designed to generate human-like, controllable, and behaviorally consistent responses. First, we propose Iterative Profile Self-Evolution (IPSE), which gradually optimizes user profiles by comparing and reasoning discrepancies between simulated trajectories and real dialogue behaviors. We then apply Role-Reversal Supervised Fine-Tuning to improve local response realism and human-like expression. To enable fine-grained behavioral alignment, we further train a specialized rubric-based reward model and incorporate it into rubric-guided multi-turn reinforcement learning, which optimizes the simulator at the dialogue level and enhances long-horizon behavioral consistency. Experiments show that MUSE consistently outperforms strong baselines in both utterance-level and session-level evaluations, generating responses that are more realistic, coherent, and persona-consistent over extended interactions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决交互式AI系统开发中，用户模拟（User Simulation）所面临的三个核心挑战。研究背景在于，随着大语言模型（LLM）推动对话AI发展，构建和评估交互系统需要可扩展、低成本的方法，用户模拟因此成为关键。然而，现有方法存在明显不足：首先，用户画像构建多依赖人工规则或简单的单次LLM提取，前者费时费力、难以扩展，后者则生成扁平化、缺乏细微行为特征的画像。其次，现有模拟器难以在长程多轮对话中保持角色一致性和上下文连贯性，容易随着交互进行而偏离设定身份。最后，现有研究主要集中在英语场景，对中文等多语言、多领域场景的探索有限。

针对这些不足，本文提出了MUSE框架，其核心目标是构建一个能够生成高度拟人化、可控且行为一致的多领域中文用户模拟器。具体而言，论文要解决的核心问题是如何从真实对话数据中自动提炼出细腻、动态的用户画像，并确保模拟器在局部响应和长程对话两个层面上都能与目标行为对齐，从而在中文等多领域场景下实现高质量、可扩展的用户模拟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。在方法类中，传统用户模拟器分为基于规则（如议程基用户模拟器ABUS）和数据驱动（使用监督或强化学习）两类，前者可控但构建费力，后者依赖固定对话流程，泛化能力和自然性有限。随着大语言模型（LLM）兴起，当前方法主要分为基于提示的方法（直接提示现成LLM扮演用户）和基于微调的方法（采用SFT或RL进行优化）。本文提出的MUSE框架属于基于微调的范畴，但与现有工作（如使用多轮RL惩罚人设漂移、训练“用户LM”减少助手偏见、或采用条件SFT和循环一致RL的USP）相比，其创新在于：1）引入了迭代式档案自我进化（IPSE）机制来优化用户档案，增强长程一致性；2）结合了基于量规的奖励模型和量规引导的多轮强化学习，实现了细粒度的行为对齐，并扩展到了多领域中文场景。在应用类中，用户模拟器主要用于生成合成数据、提供交互式RL环境以及评估智能体性能，本文的研究支撑了这些应用目标，并通过多领域设计提升了适用性。

### Q3: 论文如何解决这个问题？

论文通过一个四阶段的系统性框架来解决多领域中文用户模拟中存在的用户画像浅层、长对话一致性差以及领域受限等问题。

**核心方法与架构设计：**
整体框架包含四个关键阶段，层层递进。首先，提出**迭代式画像自我进化（IPSE）** 框架，用于从真实对话中合成高质量、跨领域且保持人物一致性的用户画像。该模块通过“非对称交互”生成模拟对话，再使用推理模型分析模拟对话与真实对话的行为差异，通过链式思维（Chain-of-Thought）进行迭代优化，最终得到最优用户画像。这解决了单次提取画像不完整或过于泛化的问题。

其次，采用**角色反转监督微调（Role-Reversal SFT）**。与传统方法训练模型预测助手回复不同，此阶段使用IPSE优化后的画像和完整对话上下文作为输入，训练模型预测用户的下一轮话语。这使模拟器在局部层面学习了真实的人类行为模式和表达方式。

**关键技术及创新点：**
1.  **基于量规的奖励模型训练**：为了提供细粒度的行为对齐信号，论文创新性地训练了一个专用的奖励模型。该模型依据一个明确的三维度量规（人类相似度、人物一致性、上下文连贯性）对每个模拟的用户话语进行评分。训练采用两阶段策略：先通过监督学习进行预热，再使用**基于可验证奖励的强化学习（RLVR）** 进行校准，其中采用了“距离感知结果奖励”函数，对接近正确的预测给予部分奖励，实现了比二元监督更精细的优化。

2.  **量规引导的多轮强化学习**：最后阶段将训练好的奖励模型整合进多轮强化学习框架。模拟器在特定用户画像下与助手模型进行多轮交互，生成完整对话轨迹。奖励模型为每一轮用户话语提供即时奖励，这些轮次奖励被平均聚合为会话级奖励。通过**分组相对策略优化（GRPO）** 最大化该会话级奖励，从而在对话层面优化模拟器策略，确保其在长程互动中始终保持符合量规标准的一致性行为。

综上，MUSE的创新点在于将**迭代式画像优化**、**角色反转学习**与**基于细粒度量规的会话级强化学习**有机结合，形成了一个从画像构建、局部行为模仿到全局一致性优化的完整技术链条，最终生成了更真实、连贯且人物一致的多领域中文用户模拟响应。

### Q4: 论文做了哪些实验？

论文的实验设置基于一个自建的大规模中文多领域对话数据集，覆盖通用聊天、客服、医疗、法律、体育娱乐、科技教育六个领域，共计9,776个对话会话。实验以Qwen3-8B为骨干模型，训练过程包括：首先基于对话难度（根据约束密度、信息保留和意图波动性评分）划分数据，前90%用于角色反转监督微调（SFT），后10%用于强化学习（RL）；随后训练一个基于量规的奖励模型（含监督预热和RLVR两阶段）；最后进行多轮RL优化（使用GRPO方法）。

对比方法包括UserLM、USP、Qwen3-8B和GPT-4o。评估分为语句级和会话级两个层面。语句级评估包含客观指标（AI生成概率AI Prob越低越好、风格相似度Style Sim越高越好、作者验证准确率AVA越高越好）和LLM评判指标（上下文相关性、响应忠实度、目标贡献度、语言自然性，均为0-1分值）。会话级评估则涵盖人物一致性、目标导向有效性、对话连贯性和约束遵守度四个维度。

主要结果显示：在语句级评估中，MUSE在几乎所有指标上均优于基线，例如AI Prob降至31.18（最佳），风格相似度达0.7534，LLM评判指标如响应忠实度达0.9776。在会话级评估中，MUSE表现更为突出，其人物一致性达0.8378，目标导向有效性达0.7967，对话连贯性达0.8685，约束遵守度达0.8739，平均得分0.8442，全面超越GPT-4o等基线。消融实验表明，移除RL的MUSE（w/o RL）在会话级指标上增益有限，凸显了多轮RL对长期行为一致性的关键作用。此外，论文还通过困惑度测试验证了所提IPSE框架在用户画像提取上的优越性（困惑度73.12，优于单次提取方法）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在语言、领域和交互长度上。首先，MUSE 的训练数据仅涵盖六个中文领域，其提取的用户画像和行为准则可能带有语言和领域特定的先验知识，因此在跨语言、跨文化或更专业、未见领域的泛化能力尚不明确。其次，当前的强化学习框架受限于预定义的轮次和上下文长度，在更长或更开放对话中的行为一致性仍有待探索。

未来研究方向可以从以下几个方面展开：一是探索跨语言和跨文化的迁移学习，通过多语言预训练或适配器技术，将框架扩展至其他语言和文化背景。二是研究更高效的长程交互模拟，例如引入分层强化学习或记忆增强机制，以处理更复杂的多轮对话。三是结合动态画像更新，使系统能在对话中实时调整用户画像，进一步提升一致性和适应性。此外，可以探索在更广泛或小众领域的应用，验证其泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出了MUSE框架，旨在解决多领域中文用户模拟中存在的用户画像浅层、长对话中角色一致性难以维持以及现有方法多局限于英语或单一领域的问题。其核心贡献在于通过三个关键方法实现了高保真且行为一致的用户模拟：首先，提出迭代式画像自进化（IPSE）机制，通过比较模拟轨迹与真实对话行为的差异来逐步优化用户画像，确保角色一致性基础；其次，采用角色反转监督微调提升单轮回复的真实性与人性化表达；最后，训练基于量规的奖励模型，并结合量规引导的多轮强化学习，在对话层面进行细粒度行为对齐，增强长程交互中的行为一致性。实验表明，MUSE在语句级和会话级评估中均优于基线模型，能生成更真实、连贯且角色一致的响应，为智能体训练、合成数据生成和多轮评估提供了可扩展且可控的解决方案。
