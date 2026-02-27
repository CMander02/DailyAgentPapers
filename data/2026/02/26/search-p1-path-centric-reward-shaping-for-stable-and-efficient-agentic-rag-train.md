---
title: "Search-P1: Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training"
authors:
  - "Tianle Xia"
  - "Ming Xu"
  - "Lingxiang Hu"
  - "Yiding Sun"
  - "Wenwei Li"
  - "Linfang Shang"
  - "Liqun Liu"
  - "Peng Shu"
  - "Huan Yu"
  - "Jie Jiang"
date: "2026-02-26"
arxiv_id: "2602.22576"
arxiv_url: "https://arxiv.org/abs/2602.22576"
pdf_url: "https://arxiv.org/pdf/2602.22576v1"
categories:
  - "cs.CL"
  - "cs.IR"
  - "cs.LG"
tags:
  - "Agentic RAG"
  - "Agent 训练"
  - "强化学习"
  - "奖励塑形"
  - "推理轨迹"
  - "多步推理"
  - "工具使用"
relevance_score: 9.0
---

# Search-P1: Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training

## 原始摘要

Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by incorporating external knowledge, yet traditional single-round retrieval struggles with complex multi-step reasoning. Agentic RAG addresses this by enabling LLMs to dynamically decide when and what to retrieve, but current RL-based training methods suffer from sparse outcome rewards that discard intermediate signals and low sample efficiency where failed samples contribute nothing. We propose Search-P1, a framework that introduces path-centric reward shaping for agentic RAG training, comprising two key components: (1) Path-Centric Reward, which evaluates the structural quality of reasoning trajectories through order-agnostic step coverage and soft scoring that extracts learning signals even from failed samples, and (2) Dual-Track Path Scoring with offline-generated reference planners that assesses paths from both self-consistency and reference-alignment perspectives. Experiments on multiple QA benchmarks demonstrate that Search-P1 achieves significant improvements over Search-R1 and other strong baselines, with an average accuracy gain of 7.7 points.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于强化学习（RL）训练智能体化检索增强生成（Agentic RAG）系统时存在的核心挑战。研究背景是，传统单轮检索的RAG难以处理需要多步推理的复杂问题，而新兴的智能体化RAG允许大语言模型动态决定检索时机与内容，从而支持迭代式信息获取与答案精炼。然而，当前基于RL的训练方法（如Search-R1）存在明显不足：首先，它们依赖稀疏的结果奖励，即仅根据最终答案的正确与否提供二元奖励，完全忽略了中间推理路径的结构质量；其次，样本效率低下，任何未能得出完全正确答案的轨迹（即使是部分正确）都会获得零奖励，导致这些样本对训练毫无贡献；最后，由于大多数样本获得的奖励信号相似且信息量弱，训练收敛缓慢。

针对上述问题，本文提出了名为Search-P1的框架，其核心是引入以路径为中心的奖励塑形。该方法要解决的核心问题是如何为智能体化RAG的训练提供更密集、更丰富的奖励信号，以克服奖励稀疏性、提升样本效率并加速收敛。具体而言，框架通过两个关键组件实现这一目标：一是设计路径中心奖励，它通过顺序无关的步骤覆盖度和软评分来评估推理轨迹的结构质量，从而能从失败的样本中也能提取学习信号；二是引入双轨迹路径评分，利用离线生成的参考规划器，从自我一致性和参考对齐两个视角综合评估路径。这样，训练过程不仅能利用最终结果，还能充分利用中间推理步骤的质量信息，将原本无效的样本转化为有效的训练数据，最终实现更稳定、更高效的智能体化RAG训练。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：基于提示的智能RAG和基于强化学习的智能RAG。

在**基于提示的智能RAG**方面，相关研究通过设计提示词来引导大语言模型进行多轮检索与推理的交替。这些方法依赖于基础模型遵循指令的能力，但缺乏对检索决策的专门优化训练。

在**基于强化学习的智能RAG**方面，近期研究应用强化学习来训练自适应的搜索智能体。一些后续工作引入了辅助信号以稳定训练或提升搜索效率。另有研究探索了为RAG设计过程奖励，但其核心仍主要依赖于二元的最终结果反馈。这些现有方法普遍面临奖励稀疏（丢弃中间信号）和样本效率低（失败样本无贡献）的问题。

本文提出的Search-P1框架与上述工作密切相关，但存在关键区别。它属于基于强化学习的训练方法范畴，其核心创新在于**路径中心化的奖励塑形**。与主要依赖最终结果奖励或简单过程奖励的现有RL方法不同，本文通过“路径中心化奖励”和“双轨路径评分”机制，系统性地评估推理轨迹的结构质量，并从一致性和参考对齐两个视角提供更密集的训练信号，从而有效利用了失败样本中的学习信号，解决了现有方法在稳定性和样本效率上的不足。

### Q3: 论文如何解决这个问题？

论文通过提出名为Search-P1的路径中心奖励塑形框架，来解决基于强化学习的智能体RAG训练中存在的奖励稀疏和样本效率低下的问题。其核心方法是设计一个综合的奖励函数，不仅评估最终答案的正确性，更着重评估推理轨迹的结构质量，从而从失败样本中也能提取有效的训练信号。

整体框架首先对智能体RAG的推理轨迹进行了结构化重构，将隐含的规划步骤显式化为一个明确的“规划器”（planner）。这使得后续可以对模型声明的规划与其执行的一致性进行评估。框架主要由两个关键技术组件构成：

1.  **双轨路径评分**：这是路径中心奖励的核心计算模块。它从两个互补的视角评估轨迹质量：
    *   **Track A（自洽性评估）**：评估模型是否有效执行了自己声明的计划。其评分结合了计划本身的质量评分、计划步骤的执行比例，以及有效执行步骤占所有行动步骤的比例。这鼓励模型制定合理计划并忠实执行。
    *   **Track B（参考对齐评估）**：评估轨迹对离线生成的“参考规划器”中关键步骤的覆盖程度。参考规划器通过对大语言模型生成的多个成功轨迹进行投票提炼而成，代表了高效解决问题的关键步骤集。评分采用与顺序无关的匹配方式，计算覆盖的关键步骤比例，同样引入了效率惩罚项以防止冗余步骤。
    最终的路径奖励取两个轨道得分的最大值，这一设计具有创新性：当参考规划欠佳或模型发现了更优策略时，自洽性评分可以主导奖励，反之亦然，从而兼顾了遵循标准路径与探索创新策略的灵活性。

2.  **软结果评分**：为了解决失败样本奖励为零的问题，该模块对最终答案错误的轨迹也分配奖励。奖励由两部分加权组成：一部分评估答案的部分正确性，另一部分独立评估推理过程的质量。这使得即使最终答案错误，但推理路径质量较高的样本也能贡献正向的学习信号，极大提高了样本效率。

整体奖励函数是路径奖励、软结果奖励以及一个鼓励格式规范的奖励的加权和。通过这种路径中心的奖励塑形，Search-P1将训练焦点从稀疏的结果奖励转移到密集的路径质量信号上，稳定了训练过程，并充分利用了所有样本，包括失败案例，从而实现了更高效和稳定的智能体RAG训练。

### Q4: 论文做了哪些实验？

实验在多个问答基准上进行，以评估Search-P1框架的有效性。实验设置方面，研究使用了Qwen2.5-7B-Instruct和Qwen2.5-3B-Instruct作为基础模型，并采用2018年维基百科转储作为知识源，E5作为检索器，每个搜索步骤返回前3个相关段落。评估指标为准确率（ACC），即检查模型生成的响应中是否包含真实答案。

使用的数据集分为两类：1）通用问答（NQ、TriviaQA、PopQA）；2）多跳问答（HotpotQA、2WikiMultiHopQA、Musique、Bamboogle）。此外，还使用了一个内部专有的广告问答数据集AD-QA（包含1000个多跳测试实例）来评估实际应用性。NQ和HotpotQA的训练集被合并用于统一训练，并在所有数据集上进行评估以检验域内（NQ、HotpotQA）和域外（其他数据集）的泛化能力。

对比方法包括：1）直接推理（Direct、CoT）；2）标准RAG；3）基于提示的智能体RAG（IRCoT、Search-o1）；4）基于强化学习的智能体RAG（Search-R1、HiPRAG）。所有基于强化学习的方法共享相同的训练和检索配置，仅奖励函数不同。

主要结果显示，Search-P1在两种模型规模下均取得了最高的平均准确率。具体而言，在7B模型上，Search-P1的平均准确率达到47.3%，显著优于最强的基线Search-R1（39.6%），平均提升了7.7个百分点。在内部AD-QA数据集上，Search-P1（86.2%）相比Search-R1（65.6%）提升了20.6个百分点，显示出其在复杂工业场景中的实用价值。3B模型也呈现一致趋势，Search-P1（41.5%）相比Search-R1（33.6%）提升了7.9个百分点。消融实验表明，移除参考对齐（Reference-Alignment）组件会导致准确率下降5.3%，移除自洽性（Self-Consistency）组件则下降3.1%，验证了双轨路径评分的必要性。此外，软格式奖励和软结果评分的设计也被证明能加速训练收敛并提升性能，尤其在多跳问答和AD-QA等复杂任务上收益更为明显。

### Q5: 有什么可以进一步探索的点？

该论文提出的路径中心奖励机制虽有效，但仍有进一步探索空间。其局限性在于：路径评估依赖离线生成的参考规划器，这限制了其在开放领域或动态知识库中的泛化能力；同时，软评分机制虽利用失败样本，但对路径中局部错误与全局逻辑断裂的区分仍较粗糙。

未来研究方向可包括：1）开发在线或自适应参考规划器，通过少量示例或元学习动态生成参考路径，减少对固定数据集的依赖；2）引入分层奖励机制，将路径结构质量分解为步骤相关性、信息增益、逻辑连贯性等多维度细粒度评分，以更精准地引导训练；3）探索多智能体协作的RAG训练，让多个检索智能体并行探索不同路径，通过竞争或投票机制优化整体决策多样性，可能进一步提升复杂推理的鲁棒性和效率。

### Q6: 总结一下论文的主要内容

该论文针对智能体化检索增强生成（Agentic RAG）训练中存在的奖励稀疏和样本效率低的问题，提出了Search-P1框架。其核心贡献是引入了以路径为中心的奖励塑形方法。该方法包含两个关键组件：一是路径中心奖励，它通过顺序无关的步骤覆盖度和软评分来评估推理轨迹的结构质量，即使从失败样本中也能提取学习信号；二是双轨路径评分，利用离线生成的参考规划器，从自洽性和参考对齐性两个角度评估路径。实验表明，Search-P1在多个问答基准测试上显著优于Search-R1等基线方法，平均准确率提升了7.7个百分点。该工作通过有效利用中间推理信号，提升了训练稳定性和样本效率，为复杂多步推理的Agentic RAG系统提供了更高效的训练范式。
