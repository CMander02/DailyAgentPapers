---
title: "How Does Reasoning Flow? Tracing Attention-Induced Information Flow for Targeted RL in LLMs"
authors:
  - "Zhichen Dong"
  - "Yang Li"
  - "Yuhan Sun"
  - "Weixun Wang"
  - "Yijia Luo"
  - "Zinian Peng"
  - "Taiheng Ye"
  - "Chao Yang"
  - "Wenbo Su"
  - "Yu Cheng"
  - "Bo Zheng"
  - "Junchi Yan"
date: "2026-06-09"
arxiv_id: "2606.10646"
arxiv_url: "https://arxiv.org/abs/2606.10646"
pdf_url: "https://arxiv.org/pdf/2606.10646v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "强化学习"
  - "Token级信用分配"
  - "推理流追踪"
  - "注意力机制"
  - "图模型"
  - "奖励塑造"
relevance_score: 8.5
---

# How Does Reasoning Flow? Tracing Attention-Induced Information Flow for Targeted RL in LLMs

## 原始摘要

Token-level credit assignment remains a key obstacle for reinforcement learning (RL) in large language models (LLMs), where RL recipes typically treat all tokens equally, failing to distinguish decisive reasoning steps from routine formatting or fluent filler. Recent attempts leverage model-internal signals to assign finer-grained credit, but these are often point-wise heuristics that ignore the global structure of information propagation. We propose FlowTracer, an RL framework that traces answer-targeted reasoning flow on an attention-induced directed acyclic graph in which nodes correspond to tokens and edge capacities come from aggregated attention weights and derives token credit from this global structure. The edge capacities are reweighted to retain only the influence that can reach the answer region, while enforcing local flow conservation so intermediate tokens neither lose nor gain effective mass due to path length or irrelevant branches. On this graph, FlowTracer extracts an information-flow backbone connecting the question to the answer and scores tokens by flow throughput, revealing high-impact hubs and aggregation checkpoints that mediate long-range dependencies. These derived importances are used to shape token-level rewards, enabling learning signals to focus precisely on the tokens that route information toward (or away from) correct answers and delivering consistent performance gains across a range of reasoning tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型强化学习中细粒度信度分配（token-level credit assignment）的核心难题。研究背景是：强化学习（特别是RLVR）虽在数学推理等任务中取得成功，但自回归生成的长轨迹中只有稀疏的最终正确性监督，而现有方法通常对所有token一视同仁，无法区分关键的推理步骤与格式填充或流畅性词汇。现有方法的不足体现在两个层面：一是传统的泛化优势估计（GAE）依赖准确的状态值估计，而在复杂语言上下文中token级状态值难以从外部准确估算，导致信号噪声大且不稳定；二是最近利用模型内部信号（如注意力统计、熵）的启发式方法，仅使用逐点局部线索，忽视了信息在全序列中如何传播和转换的全局结构。因此，本文的核心问题是：推理信息如何在LLM内部从提示流向最终答案？为了回答该问题，论文提出FlowTracer框架，通过将token序列建模为注意力诱导的有向无环图，利用全局图结构提取从问题到答案的信息流骨干，并基于流吞吐量确定token重要性，从而实现对关键推理token的精准奖励塑形，解决细粒度信度分配难题。

### Q2: 有哪些相关研究？

在本文相关研究中，主要分为两类：基于LLM内部动态的优化信号提取和RL在LLM中的信用分配。

在LLM内部动态研究方面，已有工作利用注意力机制、特定功能层、表示空间中的方向等内部成分提取细粒度信号，通过表示编辑、侧路分类器和组件级训练增强模型。动态方法则通过注意力追踪信息传播，揭示事实关联、多路径计算和关键推理步骤。但原始注意力嘈杂且局限于单步点状影响。本文对此提出类似Doob-h变换的方法，提取与答案相关的多跳推理骨干，提供稳健优化信号，这与近期标签重新利用的思路相关，将标签视为指导预测的参考而非单纯损失目标。

在LLM的RL信用分配方面，标准RL（如GRPO）使用稀疏结果奖励或均匀分配信用，无法区分关键推理步骤与格式填充。近期改进利用熵、置信度、梯度等点状信号，但忽略了令牌间关系。本文则通过建模推理流中的多跳影响，识别令牌的真实贡献，实现更精确的信用分配，区分于现有方法。

### Q3: 论文如何解决这个问题？

FlowTracer通过构建注意力诱导的有向无环图 (DAG) 来追踪答案定向的推理流，并据此进行细粒度信用分配，以解决强化学习 (RL) 中所有token被等同对待的问题。其核心方法包含三个关键阶段：

1.  **构建原始影响图**：基于LLM生成的token序列，构建一个时间有序的DAG，其中节点对应每个token，边的权重由聚合后的注意力分数（如跨层和头部的均值）定义。该权重代表从源token到目标token的局部影响耦合强度。

2.  **Doob-h型重加权以实现有效影响**：为解决原始图不满足流量守恒和包含大量与答案无关子结构的问题，引入一个虚拟汇节点（连接所有答案token），并定义一个势函数h(i)，表示从节点i成功到达答案的总影响。通过重加权公式 W'_ik = (W_ik * h(k)) / h(i)，实现了两个关键目标：一是保证局部流量守恒，即每个中间节点的出度之和为1，消除了拓扑结构带来的偏差；二是自动抑制流向死胡同分支（h(k)约为0）的流量，使其重新分配至最终能到达答案的路径上，形成保守的、答案定向的流场。

3.  **前向传播计算token级吞吐量**：从问题token注入单位影响，在重加权后的图上进行前向传播，计算每个节点k的流值 f(k)。该值代表源自问题并最终流向答案的有效影响中经过该token的份额。由此得到token的总吞吐量，高吞吐量的token被识别为在高影响信息枢纽和聚合检查点，它们在推理过程中扮演关键角色。这些token的重要性得分被用于塑造token级别的奖励信号，在RL（如GRPO）中引入非均匀缩放因子，对高流量token赋予更大的更新权重（如γ_flow=1.5），从而实现对决定性推理步骤的精准强化。

### Q4: 论文做了哪些实验？

论文在Qwen3-4B、Qwen3-8B以及Llama-3.1-8B、Llama-3.2-3B等基础模型上进行了实验。对比方法包括标准GRPO和五种替代信用分配策略：Random（随机）、Entropy（高熵）、Gradient（梯度幅度）、Correlation（互依赖）和Attention（最大注意力分数）。评估使用三类别基准：数学推理（AIME24、AIME25、AMC23、MATH500、OlympiadBench）、多领域问答（CrossThinkQA）和领域特定谜题（Countdown）。训练设置全局batch size为512，微batch为32，梯度累积16步，学习率1e-6，无KL散度和熵正则化，温度T=0.99，3B/4B模型在8 GPU上训练500步，8B模型在16 GPU上训练600步。主要结果：在数学推理中，FlowTracer在Qwen3-4B上平均得分1K长度下39.4（较GRPO +2.2）、8K下48.6（+3.8）；Qwen3-8B上1K平均42.3（+2.9）、8K平均51.6（+1.3），在多项基准上取得最优，如AIME25 8K达21.9（+5.8）。在多领域QA和Countdown任务中，FlowTracer也一致优于所有基线方法。

### Q5: 有什么可以进一步探索的点？

论文的核心创新在于将注意力权重构建为有向图并利用流守恒原理进行信用分配，但存在几个值得深化的方向。首先，当前方法假设注意力权重能完全反映信息流动，但注意力机制可能捕捉到虚假的统计关联而非因果逻辑，未来可结合因果干预或反事实推理来区分相关性与因果性。其次，图构建依赖硬阈值裁剪弱连接，这可能丢弃远距离但关键的跳跃连接，可引入动态阈值或多尺度图融合策略。此外，该方法仅关注从问题到答案的正向流，未建模错误答案的反向传播路径，未来可扩展对称分析以识别误导性token的模式。在应用层面，对长链推理任务中注意力矩阵的稀疏性可能导致流图碎片化，可尝试将语义单元（如短语、逻辑步骤）作为节点而非单个token来增强鲁棒性。最后，与过程监督（process supervision）或渐进式推理验证方法的结合，可能进一步提升复杂数学题中的信用分配准确性。

### Q6: 总结一下论文的主要内容

FlowTracer提出了一种基于注意力诱导有向无环图的强化学习框架，用于解决大语言模型中token级信用分配难题。传统强化学习方法对所有token一视同仁，无法区分关键推理步骤与格式填充。FlowTracer通过构建以token为节点、聚合注意力权重为边容量的图结构，重新加权边容量以保留能到达答案区域的信息流，并强制执行局部流量守恒。在此基础上提取从问题到答案的信息流主干，通过流吞吐量评分识别高影响力中枢和聚合检查点。这些重要性分数用于塑造token级奖励，使学习信号精确聚焦于引导信息流向正确或错误答案的token，在多个推理任务上取得一致性能提升。该工作的核心贡献在于将信息传播的全局结构纳入信用分配，克服了点式启发式方法的局限性。
