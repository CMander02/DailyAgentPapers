---
title: "Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis"
authors:
  - "Zhiyuan Zhai"
  - "Wenjing Yan"
  - "Xiaodan Shao"
  - "Xin Wang"
date: "2026-04-16"
arxiv_id: "2604.14877"
arxiv_url: "https://arxiv.org/abs/2604.14877"
pdf_url: "https://arxiv.org/pdf/2604.14877v1"
categories:
  - "cs.LG"
tags:
  - "强化学习"
  - "工具使用"
  - "能力边界分析"
  - "评估指标"
  - "交互深度"
  - "信息整合"
  - "实验验证"
  - "对比分析"
relevance_score: 8.5
---

# Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis

## 原始摘要

Does reinforcement learning genuinely expand what LLM agents can do, or merely make them more reliable? For static reasoning, recent work answers the second: base and RL pass@k curves converge at large k. We ask whether this holds for agentic tool use, where T rounds of interaction enable compositional strategies that re-sampling cannot recover. We introduce PASS@(k,T), a two-dimensional metric that jointly varies sampling budget k and interaction depth T, separating capability expansion from efficiency improvement. Our main finding is that, contrary to the static-reasoning result, tool-use RL genuinely enlarges the capability boundary: the RL agent's pass-curve pulls above the base model's and the gap widens at large k rather than converging. The expansion is specific to compositional, sequential information gathering; on simpler tasks RL behaves as prior work predicts. Under matched training data, supervised fine-tuning regresses the boundary on the same compositional tasks, isolating self-directed exploration as the causal factor. Mechanism analysis shows RL reweights the base strategy distribution toward the subset whose downstream reasoning more often yields a correct answer, with the improvement concentrated on how the agent integrates retrieved information. These results reconcile optimistic and pessimistic readings of RL for LLMs: both are correct, on different task types.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究强化学习（RL）对大型语言模型（LLM）智能体能力影响的本质问题：RL究竟是真正扩展了智能体能够完成的任务范围（能力边界），还是仅仅提高了其在已有能力范围内的执行效率和可靠性？这一问题的厘清对于AI研究方向的资源分配至关重要——若RL主要扩展能力，则应重点投入RL算法与探索机制；若仅提升效率，则更应关注基础模型的预训练与数据质量。

研究背景在于，基于LLM的、能通过工具与环境交互的智能体是当前AI发展的前沿，而RL已成为训练此类智能体的主流方法，并在多项基准测试中取得了显著成效。然而，现有评估方法（如单一的准确率或pass@1指标）存在根本性不足：它们将能力扩展与效率提升混为一谈，无法区分性能提升是源于智能体学会了解决全新问题，还是仅仅更可靠地解决了其原本就能偶然解决的问题。现有智能体基准测试仅报告聚合准确率，缺乏对这种差异的分解能力。

因此，本文要解决的核心问题是：如何设计一个评估框架，以严格区分并量化RL带来的“能力边界扩展”与“效率改进”，并借此实证检验在需要组合式、多步信息收集的工具使用任务中，RL是否真正扩展了LLM智能体的能力边界。为此，论文引入了创新的二维评估指标PASS@(k, T)，它同时考虑独立尝试次数(k)和交互深度(T)，从而能够分离采样效率与交互能力。通过应用该框架，论文旨在验证一个关键假设：与静态推理任务中RL仅提升效率的结论不同，在工具使用场景下，RL可能通过促进自我探索和发现新的组合策略，真正地扩展了智能体的能力上限。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、评测类和理论分析类。在方法类方面，已有工作如Agent-R1、ReTool和Agent-Q等，将强化学习（RL）端到端地应用于LLM智能体训练，以提升其在网页导航、代码生成和工具增强推理等任务上的表现。这些研究通常关注整体性能提升，但未深入区分RL带来的究竟是能力边界扩展还是效率改善。在评测类方面，现有智能体基准测试主要报告聚合准确率（如pass@1），无法分解能力与效率的贡献；而针对静态推理任务的研究（如RLVR）发现，基础模型与RL模型的pass@k曲线在较大k值下会收敛，暗示RL可能仅提升可靠性而非扩展能力。本文提出的PASS@(k,T)指标则突破了这一局限，首次通过联合变化采样预算k和交互深度T来二维评估智能体能力，从而能够清晰区分上述两种效应。在理论分析类方面，先前研究对RL在LLM中作用的解读存在分歧（乐观与悲观观点并存），本文通过机制分析（如困惑度分解、策略交换检验）揭示了RL在组合性工具使用任务中如何重新加权策略分布，从而扩展能力边界，这与静态推理任务的结论形成鲜明对比，并调和了不同领域的发现。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为PASS@(k, T)的二维评估框架来解决如何区分强化学习（RL）对LLM智能体是“能力扩展”还是“效率提升”的问题。该框架的核心创新在于同时考虑了两个关键资源维度：采样预算k（独立运行次数）和交互深度T（与环境进行工具调用的轮次）。这解决了传统静态评估（如pass@k）在智能体场景中的不足，因为智能体可以通过多轮交互组合策略解决单轮交互无法解决的问题。

整体框架将智能体与环境的交互形式化为一个序列决策过程。策略π在最多T轮内与环境交互，每轮观察状态s_t（包含任务、历史动作和观测），选择动作a_t（工具调用或最终答案），并接收观测o_t。一个轨迹τ记录了完整的交互序列，其成功与否取决于最终答案是否正确。PASS@(k, T)定义为：在给定问题q上，独立运行策略π共k次，每次最多进行T轮交互，至少有一次运行产生正确答案的概率。该指标通过无偏超几何估计器计算。

主要模块与关键技术包括：1）**能力边界**的正式定义：即策略π在深度T下，即使k→∞也能解决的问题集合。2）**能力扩展**与**效率提升**的严格区分：能力扩展指RL智能体能解决基座模型无法解决的问题（集合差非空）；效率提升指两者都能解决，但RL模型更可靠（pass@1更高）。3）**诊断工具**：利用PASS@(k, T)的二维结构进行深入分析，例如计算边际价值Δ_k和Δ_T来判断增加采样还是加深交互更有效，以及定义交互饱和深度T*来评估模型从深层交互链中提取价值的能力。

该方法的创新点在于首次在工具使用场景中，通过联合变化k和T，清晰分离了能力扩展（对应T轴，解锁组合策略）与效率提升（对应k轴，提高采样可靠性）。实验发现，在需要组合式信息收集的任务上，RL确实扩大了能力边界（RL的pass曲线在k很大时仍高于基座模型且差距扩大），而在简单任务上则仅表现为效率提升，这调和了以往对RL效果乐观与悲观的观点。

### Q4: 论文做了哪些实验？

论文在三个任务类别上进行了实验：A类（纯数学推理，无工具使用）、B类（独立检索的HotPotQA比较问题）和C类（顺序依赖检索的HotPotQA桥接问题）。实验设置基于Qwen2.5-7B-Instruct基础模型，对比了基础模型（$\pi_{base}$）、监督微调模型（$\pi_{SFT}$）和强化学习模型（$\pi_{RL}$），其中SFT和RL使用完全相同的200个训练问题（来自B类和C类），以确保公平比较。SFT使用专家轨迹进行LoRA微调，而RL使用GRPO算法和二元精确匹配奖励进行训练。评估采用新提出的PASS@(k,T)指标，其中采样预算k取值1至64，交互深度T取值0至5，每个条件生成64条轨迹。

主要结果如下：在A类任务上，RL未带来能力边界扩展，$\mathcal{B}_{RL}$与$\mathcal{B}_{base}$均为84个可解问题。在B类任务上，RL小幅扩展能力边界，$\mathcal{B}_{RL}$为86，比基础模型多解决5个问题（$\mathcal{B}_{RL} \setminus \mathcal{B}_{base}=5$），仅丢失1个（$\mathcal{B}_{base} \setminus \mathcal{B}_{RL}=1$），净增4个；SFT表现类似。在C类任务上，RL显著扩展能力边界：$\mathcal{B}_{RL}$达到81，比基础模型（77）多解决5个问题，仅丢失1个，净增4个；而SFT反而收缩了边界，$\mathcal{B}_{SFT}$降至73，净损失4个。关键数据指标显示，在C类任务上，RL相比SFT的能力集合不对称性为9:1（$\mathcal{B}_{RL} \setminus \mathcal{B}_{SFT}=9$，$\mathcal{B}_{SFT} \setminus \mathcal{B}_{RL}=1$），凸显了自探索学习信号的作用。PASS@(k,T)曲线分析表明，在C类任务上，RL在k较小时略低于基础模型，但随着k增大（约k>4），RL曲线反超且差距扩大，在k=64时达到0.81（基础模型0.77，SFT 0.73），证明了RL是能力扩展而非效率提升。交互饱和分析显示，在C类任务上，基础模型和RL均在T=2时达到饱和，但RL的饱和性能更高。边际价值分析指出，在C类任务中，当T达到2后，增加采样预算k是提升性能的主要方式。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在实验设置上：仅使用了7B规模的单一基础模型、基于BM25的10段落检索而非网络级检索、单一检索工具以及200个问题的有限训练预算。这些限制可能影响结论的泛化能力。

未来研究可以从以下几个方向深入：首先，进行规模扩展实验，验证结论在14B或更大模型、更复杂检索工具（如网络搜索）以及更大规模训练数据下的稳健性。其次，探索更长的交互深度（T > T_train），研究智能体在超出训练时长的序列中如何维持或扩展能力边界。再者，论文发现强化学习通过重加权基础策略分布来提升能力，未来可深入分析这种重加权的具体机制，例如研究智能体如何更有效地整合检索到的信息，并尝试设计更高效的训练信号来促进这一过程。此外，可以探索将PASS@(k,T)分析框架应用于更广泛的智能体任务类型（如代码生成、具身推理），以全面评估强化学习在不同复杂度任务中的作用边界。最后，结合论文关于监督微调在组合任务上导致能力边界倒退的发现，未来可以研究如何融合不同学习信号（如RL与SFT），以在提升效率的同时避免能力退化。

### Q6: 总结一下论文的主要内容

这篇论文探讨强化学习（RL）是否能真正扩展大语言模型（LLM）智能体的能力边界，还是仅仅提高其可靠性。为此，作者提出了一个新的评估指标 PASS@(k,T)，该指标同时考虑采样预算 k 和交互深度 T，以区分能力扩展与效率提升。研究发现，与静态推理任务中 RL 仅提升可靠性的结论不同，在需要组合式、顺序信息检索的工具使用任务中，RL 能真正扩展能力边界：RL 智能体的性能曲线显著高于基础模型，且随着 k 增大差距扩大而非收敛。这种扩展归因于 RL 通过自我探索，对基础策略分布进行了重新加权，使其更倾向于那些能通过下游推理得出正确答案的策略子集。相比之下，在相同数据下，监督微调（SFT）反而会削弱模型在此类复杂任务上的能力边界。论文结论表明，RL 对 LLM 的价值取决于任务类型：对于简单任务，RL 和 SFT 效果相当；对于复杂的组合任务，RL 是实现能力扩展的关键。
