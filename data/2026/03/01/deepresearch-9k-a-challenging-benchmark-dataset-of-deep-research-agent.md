---
title: "DeepResearch-9K: A Challenging Benchmark Dataset of Deep-Research Agent"
authors:
  - "Tongzhou Wu"
  - "Yuhao Wang"
  - "Xinyu Ma"
  - "Xiuqiang He"
  - "Shuaiqiang Wang"
date: "2026-03-01"
arxiv_id: "2603.01152"
arxiv_url: "https://arxiv.org/abs/2603.01152"
pdf_url: "https://arxiv.org/pdf/2603.01152v1"
github_url: "https://github.com/Applied-Machine-Learning-Lab/DeepResearch-R1"
categories:
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Reasoning & Planning"
relevance_score: 9.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "Tongyi-DeepResearch-30B-A3B, Qwen2.5-3B, Llama3.2-3B"
  key_technique: "DeepResearch-R1 (multi-turn web interaction framework with RL training)"
  primary_benchmark: "DeepResearch-9K"
---

# DeepResearch-9K: A Challenging Benchmark Dataset of Deep-Research Agent

## 原始摘要

Deep-research agents are capable of executing multi-step web exploration, targeted retrieval, and sophisticated question answering. Despite their powerful capabilities, deep-research agents face two critical bottlenecks: (1) the lack of large-scale, challenging datasets with real-world difficulty, and (2) the absence of accessible, open-source frameworks for data synthesis and agent training. To bridge these gaps, we first construct DeepResearch-9K, a large-scale challenging dataset specifically designed for deep-research scenarios built from open-source multi-hop question-answering (QA) datasets via a low-cost autonomous pipeline. Notably, it consists of (1) 9000 questions spanning three difficulty levels from L1 to L3 (2) high-quality search trajectories with reasoning chains from Tongyi-DeepResearch-30B-A3B, a state-of-the-art deep-research agent, and (3) verifiable answers. Furthermore, we develop an open-source training framework DeepResearch-R1 that supports (1) multi-turn web interactions, (2) different reinforcement learning (RL) approaches, and (3) different reward models such as rule-based outcome reward and LLM-as-judge feedback. Finally, empirical results demonstrate that agents trained on DeepResearch-9K under our DeepResearch-R1 achieve state-of-the-art results on challenging deep-research benchmarks. We release the DeepResearch-9K dataset on https://huggingface.co/datasets/artillerywu/DeepResearch-9K and the code of DeepResearch-R1 on https://github.com/Applied-Machine-Learning-Lab/DeepResearch-R1.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究智能体（deep-research agent）领域面临的两个关键瓶颈问题。研究背景是，随着大语言模型（LLMs）在推理能力和上下文窗口上的显著进步，智能体研究正转向更自主的系统，能够执行多步骤网络探索、针对性检索和复杂问答等深度研究工作。然而，该领域的发展受到严重制约。

现有方法的不足主要体现在数据和框架两方面。首先，缺乏大规模、高难度、贴近真实世界复杂性的基准数据集。早期的开源基准（如NQ、HotpotQA）主要评估信息整合能力，未能充分体现深度研究所需的自主性。较新的基准（如GAIA、BrowseComp）虽然提升了难度，但仍缺乏能迫使模型处理多步骤复杂研究轨迹的环境。具体而言，现有数据集存在三大局限：1）推理链不足，通常只需少量搜索，无法反映真实研究中冗长的逻辑链；2）搜索工具调用频率与难度脱节，现有多跳问答数据集未能系统地将难度与所需的工具调用次数关联；3）环境静态且受限，依赖封闭的静态语料库，无法模拟开放网络动态、不可预测的特性，限制了智能体的自主探索、战略规划和迭代验证能力。

因此，本文要解决的核心问题是：通过构建一个具有不同难度级别的大规模挑战性基准数据集（DeepResearch-9K），并配套一个开源的训练框架（DeepResearch-R1），来系统性地评估和提升智能体在开放式深度研究场景中的能力。具体而言，数据集旨在弥补“高质量、大规模挑战数据”的空白，而开源框架则旨在解决“易获取的数据合成与智能体训练工具”的缺失，从而共同推动深度研究智能体的发展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为评测基准和训练框架两大类。

在**评测基准**方面，相关工作旨在评估智能体在复杂、开放环境中的研究能力。GAIA 通过所需推理步骤和工具调用数量来区分任务，模拟现实世界的问答。GPQA 和 Humanity's Last Exam 专注于专家级、领域特定的难题，推动智能体进行深度研究。BrowseComp 则要求智能体通过主动浏览和跨网站比较信息来回答问题，测试其在时间限制下的比较研究能力。与这些工作相比，本文提出的 DeepResearch-9K 不仅是一个评测基准，更关键的是它旨在填补**训练资源**的空白。现有基准主要用于评估，而本文的数据集专门为训练智能体而构建，提供了大规模、高质量的多步交互轨迹。

在**训练框架**方面，DR-Arena 和 DeepResearch Bench 等框架为评估自主研究智能体提供了标准化环境。DeepWideSearch 评估长视野、探索性网络搜索中的战略规划。ToolBench 和 Search-R1 等工作展示了工具使用轨迹或“思维-行动”轨迹在训练中的价值。本文的 DeepResearch-R1 框架与这些工作有联系，但其核心区别在于，它明确设计为一个可复用的开源管道，专注于**自动化生成具有挑战性的训练数据**，并支持多轮网络交互、多种强化学习方法及奖励模型，从而直接应对当前缺乏用于合成训练数据和迭代改进智能体的可访问框架这一更广泛的缺失。

### Q3: 论文如何解决这个问题？

论文通过构建一个大规模、高难度的数据集DeepResearch-9K，并配套开发一个开源训练框架DeepResearch-R1，系统性地解决了深度研究智能体面临的数据集和训练框架两大瓶颈。

**核心方法与架构设计**：
1.  **数据集构建（DeepResearch-9K）**：采用分层构造策略，核心是一个**多级难度扩展方法**。该方法从三个开源多跳问答数据集（2WikiMultihopQA、HotpotQA、MuSiQue）中采样，提取种子实体，并围绕其构建难度递增的推理链。
    *   **整体框架**：构建流程分为四个阶段：种子实体识别与提取、渐进式推理链构建、渐进式实体混淆、基于规则的质量保证。
    *   **主要模块/组件**：
        *   **难度分级（L1-L3）**：这是核心创新。L1（直接属性映射）进行实体替换，要求1-2次搜索；L2（多跳关系桥接）构建A→B→C链，移除专有名词等，增加搜索次数；L3（深度研究）构建5-6步的“接力链”，强制要求每个跳转都需要新的独立搜索查询，且单个知识源不能包含连续两个以上实体，最终问题被编码成密集的叙事段落，使用高级混淆（无专有名词、精确日期、地点，代之以功能角色、历史时期等描述），目标是最少需要15次独立搜索。
        *   **渐进式实体混淆策略**：与难度级别对应，从L1的简单同义词替换，到L2/L3的严格禁止使用明确标识符，迫使智能体进行语义推理和跨源验证。
        *   **DeepResearch-Hard子集**：额外构建一个仅包含教师模型（Tongyi-DeepResearch-30B-A3B）也无法正确回答的实例的子集，用于严格评估智能体的极限。
    *   **创新点**：提出了系统性的、可量化的难度扩展维度（搜索工具调用频率、逻辑链难度、同义替换、实体混淆程度），特别是L3级别的设计模拟了真实研究中需要长程战略规划和分步推理的场景。

2.  **训练框架（DeepResearch-R1）**：为了利用上述数据集训练智能体，论文开发了开源的DeepResearch-R1框架。
    *   **整体框架**：一个支持深度研究智能体训练的统一平台。
    *   **主要模块/组件**：
        *   **多轮网络交互支持**：模拟智能体在实际研究中的浏览、搜索、信息提取等步骤。
        *   **多种强化学习（RL）方法支持**：提供了灵活性，允许研究者尝试不同的RL算法来优化智能体策略。
        *   **多样化奖励模型**：支持基于规则的结果奖励和“LLM-as-judge”（大语言模型作为评判员）的反馈，用于指导智能体的学习过程。
    *   **创新点**：提供了一个集成的、开源的解决方案，将具有挑战性的数据集与一个支持现代训练技术（特别是多种RL方法和奖励机制）的灵活框架结合起来，降低了深度研究智能体开发的门槛。

综上，论文的解决方案是“数据”与“工具”并重：通过精心设计的自动化管道合成高质量、分难度的基准数据集，同时提供一个功能全面的开源训练框架，共同推动深度研究智能体在复杂、真实场景下的能力发展。

### Q4: 论文做了哪些实验？

论文的实验主要包括两部分：在DeepResearch-9K数据集和BrowseComp-Plus基准上的能力评估，以及对不同训练范式的分析。

**实验设置与数据集**：研究构建了DeepResearch-9K数据集，包含从HotpotQA、2WikiMultihopQA和MuSiQue中采样的9000个问题，分为L1到L3三个难度等级。使用Tongyi-DeepResearch-30B-A3B作为教师模型生成搜索轨迹和答案，并通过DeepSeek-V3评估，得到5026个正确样本和3974个错误样本（DeepResearch-Hard）。训练集由全部正确轨迹和随机选取的2200个错误样本组成（共7226个实例），测试集为剩余的1774个样本。外部评估使用BrowseComp-Plus基准（包含830个复杂任务）。

**对比方法与训练范式**：训练基于DeepResearch-R1框架，采用两阶段强化学习（RL）范式。1）Zero-RL：直接在基础语言模型上使用完整训练集进行RL，以引导基础推理和工具使用能力。2）SFT+RL：先在正确轨迹子集上进行监督微调（SFT）学习教师模型的模式，再进行完整训练集的RL训练。两种范式均结合了GRPO和PPO算法，奖励信号由DeepSeek-V3提供。实验在Qwen-2.5-3B和Llama-3.2-3B两个基础模型架构上实施。

**主要结果与关键指标**：评估指标为搜索次数和准确率。教师模型Tongyi-DeepResearch-30B-A3B在DeepResearch-9K上的准确率：L1为72.47%，L2为71.33%，L3为23.73%，总体55.84%。在BrowseComp-Plus上的准确率为24.94%，与L3难度相当，验证了数据集的挑战性。不同训练策略的结果显示：Qwen-2.5-3B模型严重依赖SFT预训练，Zero-RL准确率约12%，SFT+RL提升至20%以上；Llama-3.2-3B模型使用PPO（Zero-RL）取得了最高测试准确率22.50%，超过了DeepSeek V3基线（20.18%）。所有模型性能在20%左右徘徊，凸显了数据集的难度。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从数据集、框架和评估三方面探讨。首先，DeepResearch-9K虽具挑战性，但其数据源主要基于现有多跳QA数据集，可能未充分覆盖真实世界中更开放、动态的研究场景（如跨领域知识整合或实时信息验证）。未来可探索更具多样性和复杂性的数据合成方法，例如引入多模态信息或模拟更长的决策链。其次，DeepResearch-R1框架虽支持多种RL方法，但对不同奖励模型（如规则奖励与LLM评判）的融合与优化仍可深入，未来可研究自适应奖励机制或引入人类反馈进行微调。此外，当前评估主要对比特定模型，未来需在更广泛的基准和实际应用场景中测试泛化能力。结合个人见解，可能的改进包括：设计更具解释性的轨迹评估指标，以分析agent决策过程中的关键错误；探索课程学习策略，让agent从易到难逐步掌握深度研究技能；以及开发能处理模糊或冲突信息的机制，以提升在不确定环境下的鲁棒性。

### Q6: 总结一下论文的主要内容

本文针对深度研究智能体面临的两大瓶颈——缺乏大规模、高难度的真实世界数据集，以及缺少开源的数据合成与训练框架——提出了系统性的解决方案。核心贡献是构建了DeepResearch-9K数据集，它包含9000个从开源多跳问答数据集通过低成本自动化流程构建的问题，覆盖三个难度等级，并提供了由先进智能体生成的高质量搜索轨迹、推理链和可验证答案。同时，论文开发了开源训练框架DeepResearch-R1，支持多轮网页交互、多种强化学习方法及不同奖励模型。实验表明，利用该数据集和框架训练的智能体在多个深度研究基准测试中取得了最先进的性能。这项工作为深度研究智能体的评估与训练提供了重要的数据和工具基础，推动了该领域的发展。
