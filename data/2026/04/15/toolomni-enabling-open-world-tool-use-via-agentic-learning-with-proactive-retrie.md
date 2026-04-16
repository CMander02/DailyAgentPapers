---
title: "ToolOmni: Enabling Open-World Tool Use via Agentic learning with Proactive Retrieval and Grounded Execution"
authors:
  - "Shouzheng Huang"
  - "Meishan Zhang"
  - "Baotian Hu"
  - "Min Zhang"
date: "2026-04-15"
arxiv_id: "2604.13787"
arxiv_url: "https://arxiv.org/abs/2604.13787"
pdf_url: "https://arxiv.org/pdf/2604.13787v1"
categories:
  - "cs.CL"
tags:
  - "Tool Use"
  - "Agent Framework"
  - "Open-World"
  - "Reinforcement Learning"
  - "Retrieval-Augmented"
  - "Generalization"
  - "SFT"
  - "GRPO"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# ToolOmni: Enabling Open-World Tool Use via Agentic learning with Proactive Retrieval and Grounded Execution

## 原始摘要

Large Language Models (LLMs) enhance their problem-solving capability by utilizing external tools. However, in open-world scenarios with massive and evolving tool repositories, existing methods relying on static embedding retrieval or parameter memorization of tools struggle to align user intent with tool semantics or generalize to unseen tools, respectively, leading to suboptimal accuracy of open-world tool retrieval and execution. To address these, we present ToolOmni, a unified agentic framework that enables LLMs for open-world tool use by proactive retrieval and grounded execution within a reasoning loop. First, we construct a cold-start multi-turn interaction dataset to instill foundational agentic capabilities via Supervised Fine-Tuning (SFT). Then, we introduce open-world tool learning based on a Decoupled Multi-Objective GRPO algorithm, which simultaneously optimizes LLMs for both tool retrieval accuracy and execution efficacy in online environments. Extensive experiments demonstrate that ToolOmni achieves state-of-the-art performance both in retrieval and execution, surpassing strong baselines by a significant margin of +10.8% in end-to-end execution success rate, while exhibiting exceptional robustness and generalization capabilities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在开放世界场景中有效使用外部工具的核心挑战。研究背景是，虽然LLM通过调用工具（如计算器、API）能极大增强问题解决能力，但现实中的工具库往往规模庞大且持续动态更新（即“开放世界”）。现有主流方法存在明显不足：一类是基于静态嵌入向量的检索方法，它被动地将用户查询与工具描述进行相似度匹配，但由于检索过程与智能体的任务推理脱节，难以在复杂意图下精准匹配到功能核心工具，导致检索准确率低；另一类是将工具文档知识参数化记忆到模型中的方法，虽然对已知工具有效，但一旦工具库更新就需要昂贵的重新训练，无法泛化到未见过的工具，适应性差。

因此，本文要解决的核心问题是：如何让LLM在工具库海量且动态演化的开放世界环境中，既能主动、精准地检索到所需工具，又能基于检索结果进行有效的推理和执行，从而实现端到端的高成功率工具使用。为此，论文提出了ToolOmni框架，其核心创新在于将**主动检索**与**基于推理的落地执行**耦合在一个统一的智能体循环中，并通过一个两阶段训练策略（监督微调冷启动+基于改进的GRPO算法的强化学习）来同步优化检索准确率和执行效能，以提升模型在开放世界中的整体工具使用能力、鲁棒性和泛化性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为工具检索、工具增强与执行、以及智能体训练框架三大类。

在**工具检索**方面，相关工作主要采用基于嵌入模型的语义相似度检索（如检索Top-k相关工具），或通过LLM改写查询、扩展工具文档来提升检索性能。另一类方法则训练LLM将工具信息编码为参数知识，使其能直接生成工具标识符。本文同样利用基于嵌入的检索，但创新性地改变了交互范式：让智能体主动构建查询，并将嵌入模型本身作为一个可执行工具来调用。

在**工具增强与执行**方面，ReAct 提出了“思考-行动-观察”的循环框架，让模型生成显式推理轨迹来交织规划与执行。ToolLLM 采用了基于深度优先搜索的树状框架（DFSDT），允许模型探索多条执行路径并根据工具反馈进行回溯。Meta-Tool 引入了即插即用的检索模块，但将检索和执行视为分离的流水线阶段。本文受这些研究启发，但将主动工具发现与执行统一为一个端到端的过程，以应对开放世界场景。

在**智能体训练框架**方面，近期研究利用强化学习与验证反馈（RLVR）等代理训练框架来提升LLM使用外部工具的能力。这些工作将外部搜索和代码执行视为可执行工具，促进了端到端的推理范式。本文在此基础上，提出了解耦多目标GRPO算法，在在线环境中联合优化工具检索准确性和执行效能，从而实现了对开放世界工具使用的统一智能体框架。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ToolOmni的统一智能体框架来解决开放世界工具使用中的检索与执行难题。其核心方法是将整个过程建模为一个由策略模型驱动的级联检索-执行框架，并采用两阶段训练策略来优化模型能力。

整体框架分为两个解耦的阶段：主动检索和基于上下文的执行。在主动检索阶段，智能体不是被动接受单次检索结果，而是主动分析用户意图，迭代生成搜索查询，与检索服务器交互以逐步筛选和累积候选工具集，直至形成一个任务完备的工具子集。在执行阶段，智能体基于检索到的工具文档，在推理循环中交替进行推理和工具调用，最终生成答案。

关键技术包括：1）数据构建与监督微调：首先精心构建了一个包含检索与执行轨迹的高质量多轮交互数据集，通过监督微调为模型注入基础的智能体能力。2）解耦的多目标在线强化学习：这是核心创新点。论文提出了基于GRPO的解耦多目标优化算法，同时优化工具检索准确性和执行有效性。该算法设计了独立的检索奖励和执行奖励函数，并采用组相对优势估计，将两个子任务的优势信号在组内分别归一化，避免了稀疏的执行奖励干扰检索学习过程。在策略梯度更新时，采用顺序更新而非直接求和，防止梯度冲突，并通过选择性展开机制确保执行策略仅在高质量检索结果上训练，从而稳定了优化过程。3）主动检索与上下文执行机制：智能体自主决定检索时机和查询内容，并通过特殊标签结构化其推理、行动和结果，实现了可解释且可控的交互流程。

创新点主要体现在：将开放世界工具使用形式化为一个由统一策略驱动的、迭代的主动检索与上下文执行循环；提出了一种解耦的多目标在线强化学习方法，能同时且稳定地优化检索与执行性能；通过精心设计的奖励函数、组相对优势估计和训练稳定性优化，有效解决了开放场景下工具海量、动态变化所带来的对齐与泛化挑战。

### Q4: 论文做了哪些实验？

论文在ToolBench基准上进行了广泛的实验，以评估ToolOmni在开放世界工具使用中的性能。实验设置方面，模型基于Qwen3-4B-Instruct初始化，并使用提出的解耦多目标GRPO算法（G=5， T=1.0）在8张NVIDIA H100 GPU上进行训练。

实验主要包含四个部分：
1.  **工具检索性能评估**：在In-Domain（特定工具子集）和Multi-Domain（超过16，000个API的完整仓库）两种设置下，与稀疏检索（BM25）、稠密检索（ToolRetriever， EmbSim）、迭代反馈方法（IterFeedback， Re-Invoke）以及生成式方法（ToolGen）进行对比。关键指标为NDCG@k（k ∈ {1， 3， 5}）。结果显示，在最具挑战性的Multi-Domain设置中，ToolOmni取得了最高的平均NDCG（78.29%），在top-1和top-3精度上显著优于基线。
2.  **端到端任务执行性能评估**：在给定真实工具（With Golden Truth）和结合检索器（With Retriever， 即端到端）两种场景下，与流水线智能体（GPT-3.5， ToolLLaMA）和统一生成模型（ToolGen）进行对比。关键指标为可解通过率（SoPR）和可解胜率（SoWR）。在端到端设置中，ToolOmni取得了54.13%的平均SoPR和50.16%的平均SoWR，分别比最强的GPT-3.5流水线基线高出+11.78%和+10.39%，证明了其整体优势。
3.  **鲁棒性与泛化能力分析**：
    *   **泛化性能**：在工具泛化（Tool Gen.）和类别泛化（Category Gen.）测试中，ToolOmni分别取得了52.20%和55.95%的SoPR，显著优于基线，尤其在全新领域（Category Gen.）表现突出。
    *   **抗检索噪声能力**：在检索上下文中注入不同数量（N ∈ {0， 5， 10， 15}）的对抗性工具后，ToolOmni表现出适应性恢复能力，在N=15时准确率反弹至58.2%，而ToolLlama-v2则单调下降至20.5%。
4.  **消融研究与敏感性分析**：
    *   **核心组件贡献**：移除了迭代检索、监督微调（SFT）或强化学习（RL）的变体性能均显著下降。例如，移除RL导致检索NDCG下降28.99%，移除SFT导致执行SoPR下降9.1%。
    *   **RL组件设计**：验证了解耦多目标GRPO算法的有效性。移除轨迹过滤机制导致SoPR大幅降至38.5%；使用联合更新（Combined Update）或原始GRPO（Vanilla GRPO）也会导致性能下降。
    *   **超参数敏感性**：检索工具数量k在5时达到最佳平衡（平均NDCG 78.29%），过多或过少都会降低性能。格式奖励权重在0.4时取得最佳执行效果（SoPR 44.3%），权重过高会损害推理能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的ToolOmni框架在开放世界工具使用上取得了显著进展，但仍存在值得深入探索的局限性。首先，其采用的级联范式（先检索后执行）虽然稳定，但在处理需要动态调整工具链的复杂任务时缺乏灵活性。未来可探索更紧密耦合的“检索-执行-规划”一体化架构，使智能体能根据中间结果实时调整策略，例如引入基于执行反馈的在线重规划机制。

其次，当前工作仅在4B参数的模型上进行验证，未能探索更大规模基础模型带来的性能上限和涌现能力。后续研究可在70B甚至更大模型上验证框架的可扩展性，并研究模型规模与工具学习效率之间的关系。此外，论文未涉及多模态工具的场景，未来可扩展至支持图像、音频等多模态工具的检索与执行。

从方法学角度看，Decoupled Multi-Objective GRPO算法虽优化了检索与执行目标，但未考虑工具之间的依赖关系与组合逻辑。可引入图神经网络对工具库进行结构化建模，提升复杂工作流的构建能力。最后，真实开放世界的工具库具有高度动态性，当前静态评估未能充分体现持续学习需求，需设计增量学习机制以支持工具库的实时更新。

### Q6: 总结一下论文的主要内容

本文针对开放世界场景下海量且动态演化的工具库，提出ToolOmni框架，旨在解决现有方法因静态检索或参数记忆导致的工具检索与执行准确率不足的问题。其核心贡献在于通过主动检索与基于推理循环的落地执行，构建一个统一的智能体框架，使大语言模型能够有效利用未知工具。方法上，首先通过监督微调构建多轮交互数据集以奠定智能体基础能力；进而提出解耦多目标GRPO算法，在在线环境中同步优化工具检索准确率与执行效能。实验表明，ToolOmni在检索和执行任务上均达到最先进性能，端到端执行成功率显著超越基线10.8%，并展现出优异的鲁棒性和对未见工具及领域的泛化能力。这验证了通过迭代推理进行工具选择与执行是实现可扩展、鲁棒工具学习的关键。
