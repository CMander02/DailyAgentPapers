---
title: "SCI-PRM: A Tool Aware Process Reward Model for Scientific Reasoning Verification"
authors:
  - "Xiangyu Zhao"
  - "Hengyuan Zhao"
  - "Yiheng Wang"
  - "Wanghan Xu"
  - "Yuhao Zhou"
  - "Qinglong Cao"
  - "Zhiwang Zhou"
  - "Lei Bai"
  - "Wenlong Zhang"
  - "Xiao-Ming Wu"
date: "2026-06-03"
arxiv_id: "2606.04579"
arxiv_url: "https://arxiv.org/abs/2606.04579"
pdf_url: "https://arxiv.org/pdf/2606.04579v1"
categories:
  - "cs.AI"
tags:
  - "Process Reward Model"
  - "Scientific Reasoning"
  - "Tool Use"
  - "Training Data"
  - "Test-Time Scaling"
  - "Reinforcement Learning"
relevance_score: 8.5
---

# SCI-PRM: A Tool Aware Process Reward Model for Scientific Reasoning Verification

## 原始摘要

While Process Reward Models (PRMs) have achieved remarkable success in mathematical reasoning, their application in complex scientific domains-such as biology, chemistry, and physics remains largely unexplored. Scientific problems demand not only logical rigor but also factual consistency and the precise usage of domain-specific tools, areas where current models often suffer from hallucinations and lack of verification. In this paper, we first construct SCIPRM70K, a large-scale dataset featuring Chain-of-Tool trajectories that explicitly interleave reasoning with the execution of scientific tools. Building upon this, we train an efficient reward model called Sci-PRM to provide fine-grained supervision on tool selection, execution accuracy, and result interpretation at each step in one inference. Experiments demonstrate that Sci-PRM significantly enhances foundation models in two key aspects: (1) it enables effective test-time scaling via Best-of-N selection; and (2) when integrated into Reinforcement Learning, it serves as a dense reward signal that mitigates the critical issue of advantage disappearance, allowing the model to break through existing performance ceilings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在科学推理（如生物、化学、物理等）中面临的领域特定幻觉和缺乏验证的问题。现有方法存在两个主要不足：第一，尽管过程奖励模型（PRM）在数学推理上取得显著成功，但直接应用于科学领域时表现不佳。科学推理不仅要求逻辑严谨，更强调事实一致性和领域工具（如分子数据库、代码执行、文献检索等）的精确使用，而通用LLM评估器（如GPT-5-Mini）在评估涉及工具调用的科学推理步骤时，准确率显著下降，无法区分工具选择、调用和结果解读等细粒度错误。第二，现有的面向工具的奖励模型研究主要聚焦通用领域，无法处理科学问题中工具选择的专业性（如匹配特定子问题）、调用的精确性（单位、格式、参数）以及结果解读的约束性。此外，直接调用科学API的时耗过长（每次1-5分钟），不适用于测试时扩展或强化学习中的快速奖励信号。因此，本文的核心目标是构建一个专门的、具有工具感知能力的科学推理过程奖励模型Sci-PRM。该模型通过解析推理轨迹中显式交织的思维链与工具调用链，对每一步的工具选择、调用准确性和结果利用进行细粒度监督，以在测试时通过Best-of-N选择有效扩展，并在强化学习训练中提供密集奖励信号，从而突破现有性能天花板并减少科学推理中的幻觉。

### Q2: 有哪些相关研究？

相关研究可分为四类：

1. **奖励模型方法**：主流工作包括Outcome-Supervised Reward Models (ORMs) 和 Process-Supervised Reward Models (PRMs)。PRMs在数学和代码生成等领域效果显著，但现有研究主要集中在通用推理域，缺乏对生物、化学等需要领域知识验证的科学领域的探索。本文专门面向科学推理，弥补了这一空白。

2. **工具增强型评估**：Math-Shepherd等工作采用"工具辅助裁判"策略，但依赖通用工具（计算器、搜索引擎）和提示工程，缺乏对科学专用工具（如RDKit、Biopython）验证能力的训练。本文则显式训练奖励模型内部化工具验证能力。

3. **工具增强推理**：通过集成外部工具增强LLM能力，但现有方法在科学领域存在两大局限：一是缺乏对工具选择、执行精度和结果解读的细粒度监督；二是"执行反馈循环"范式在调用专业工具时计算开销巨大。本文通过离线训练Sci-PRM作为高质量代理，避免了实时调用工具的瓶颈。

4. **强化学习优化**：近期工作探索将推理与工具执行交错训练（如GSM8K上的PPO/GRPO），但实时执行科学工具成本过高。本文提出的Sci-PRM可提供密集奖励信号，有效缓解优势消失问题，突破性能天花板。

### Q3: 论文如何解决这个问题？

这篇论文提出了一种工具感知的过程奖励模型（SCI-PRM），用于解决科学推理中工具使用的验证难题。整体框架包含三个核心阶段：

首先，构建了**SCIPRM70K数据集**，通过“生成-执行-判断”范式创建工具增强的推理轨迹。具体来说，系统在LLM生成过程中暂停以执行真实工具调用（如搜索引擎或Python代码沙箱），并获取实际观测结果，确保后续推理基于真实执行反馈而非幻觉。

关键技术之一是**两阶段自动标注**：第一阶段通过执行验证（如代码运行状态、搜索返回结果）过滤技术不可行的步骤；第二阶段采用**蒙特卡洛树搜索（MCTS）一致性检验**，从每个步骤进行K次独立展开，只有当某步骤持续导向正确答案且满足置信度阈值时才标记为正样本，从而兼顾工具选择恰当性、参数准确性和结果解释的正确性。

模型架构基于Qwen3-VL-8B主干，采用**两阶段课程训练**：先通过SFT注入结构化推理和步骤级标注能力，再使用动态优势策略优化（DAPO）强化验证一致性。在推理时，SCI-PRM对每个步骤输出0-1的质量分数，并通过带长度惩罚的累积评分选择最佳轨迹（Best-of-N），同时可作为稠密奖励信号用于强化学习训练工具使用智能体。

创新点包括：首次构建大规模工具增强的科学推理过程数据集、提出结合执行验证与MCTS逻辑验证的步骤级标注方法、以及将过程奖励模型同时应用于测试时扩展和强化学习场景，有效解决了传统奖励模型在科学推理中的幻觉和优势消失问题。

### Q4: 论文做了哪些实验？

论文构建了SCIPRM70K数据集（含约8.5k条SFT轨迹和27.3K步RL轨迹），并划分1.5k条作为SCIPRM-Bench基准。实验在四个科学基准上进行：BioProBench（生物实验流程）、ChemBench（化学反应与性质计算）、Mol-Instructions（蛋白质结构分析）和MSEarth（地球科学推理）。对比方法包括：1) 作为奖励模型时，与随机基线、闭源模型（Doubao-Seed-1.6、GLM-4.6V、Gemini-3-Flash、GPT-5-Mini）及开源模型（Qwen3-VL-8B/32B、LLaMA-3.2-11B-V）比较；2) 下游推理中对比Majority Voting、ORM-Guided Best-of-N和SCI-PRM Best-of-N。

主要结果：在SCIPRM-Bench上，SCI-PRM的总体F1达0.7691，超过GPT-5-Mini（0.7592）和Qwen3-VL-32B（0.7539）。工具调用F1为0.5619，优于所有基线（随机0.3523、GPT-5-Mini 0.5338、Gemini-3-Flash 0.5587）。工具差距（No-Tool F1 - Tool F1）为0.2714，显著低于GLM-4.6V（0.3851）和Qwen3-VL-32B（0.3900），表明SCI-PRM在工具使用场景下退化最小。在搜索信息验证中，SCI-PRM的准确率、精度等指标均表现领先，有效缓解了科学推理中的幻觉问题。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：SCIPRM70K数据集覆盖的科学领域和工具类型相对有限，可能无法泛化到更广泛的科学推理场景；当前PRM仅基于步骤级工具使用进行评分，未考虑步骤间的长期因果依赖和工具调用的链式传播错误；奖励信号主要来自工具执行正确性，对科学事实的深层逻辑一致性缺乏直接验证。

未来可探索的方向包括：（1）构建包含更多交叉学科（如药物设计、材料科学）和异构工具（实验模拟器、知识图谱）的数据集；（2）设计动态奖励机制，对工具调用序列中的错误传播进行回溯建模；（3）引入科学知识库作为外部验证器，将逻辑一致性和事实正确性共同作为奖励函数组成部分；（4）探索多模态PRM，处理包含图表、分子结构等非文本信息的科学推理；（5）研究如何将Sci-PRM产生的密集奖励与稀疏的人类反馈信号进行高效融合，解决长链条推理中的信用分配问题。

### Q6: 总结一下论文的主要内容

本论文提出了SCIPRM70K数据集和工具感知过程奖励模型SCI-PRM，用于解决科学推理验证中存在的幻觉和工具使用规范性不足问题。科学推理（生物、化学、物理等）不仅需要逻辑严密性，还需要事实一致性和领域特定工具的精确使用，而现有过程奖励模型大多局限于数学推理，缺乏对工具调用过程的细粒度监督。SCI-PRM通过链式工具轨迹显式地将推理与科学工具执行交错，并在每个推理步骤对工具选择、执行准确性和结果解释提供细粒度奖励信号。实验表明，SCI-PRM在测试时通过Best-of-N选择能有效扩展推理能力，在强化学习中作为密集奖励信号可缓解优势消失问题，帮助模型突破性能上限，显著提高了科学推理的准确性和事实一致性。该工作首次将过程奖励模型系统性地应用于科学领域，为工具增强的科学LLM验证提供了有效方案。
