---
title: "GraphPO: Graph-based Policy Optimization for Reasoning Models"
authors:
  - "Yuliang Zhan"
  - "Xinyu Tang"
  - "Jian Li"
  - "Dandan Zheng"
  - "Weilong Chai"
  - "Jingdong Chen"
  - "Jun Zhou"
  - "Ge Wu"
  - "Wenyue Tang"
  - "Hao Sun"
date: "2026-06-17"
arxiv_id: "2606.18954"
arxiv_url: "https://arxiv.org/abs/2606.18954"
pdf_url: "https://arxiv.org/pdf/2606.18954v1"
categories:
  - "cs.CL"
tags:
  - "RLVR"
  - "多步推理"
  - "策略优化"
  - "图结构"
  - "探索效率"
  - "过程奖励"
  - "LLM推理"
  - "Agent推理"
relevance_score: 8.5
---

# GraphPO: Graph-based Policy Optimization for Reasoning Models

## 原始摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has become a standard paradigm for enhancing the capability of large reasoning models. RLVR typically samples responses independently and optimizes the policy using from final answers. This paradigm has two limitations. First, independently responses often contain similar intermediate reasoning steps, causing redundant exploration and wasted computation. Second, sparse final-answer rewards make it hard to identify useful steps. Tree-based methods partly address this problem by sharing prefixes and comparing branches from the same prefix to provide fine-grained signals. However, tree branches are still expanded independently. When different branches reach similar reasoning states, they cannot share information and repeat similar exploration. Moreover, tree-based methods ignore such dispersion and only perform local comparisons within separate branches, which can lead to higher variance in advantage estimation. To address this challenge, we propose GraphPO (Graph-based Policy Optimization), a novel RL framework that represents rollouts as a directed acyclic graph, with reasoning steps as edges and semantic states summarized from the reasoning paths as nodes. GraphPO merges semantically equivalent reasoning paths into equivalence classes, allowing them to share suffixes and reallocating budget away from redundant expansions to diverse exploration. Furthermore, we assign efficiency advantages to incoming edges and correctness advantages to outgoing edges, thereby improving inference efficiency while deriving process supervision from outcome. Theory shows that GraphPO reduces advantage-estimation variance and enhances reasoning efficiency. Experiments on three LLMs across reasoning and agentic search benchmarks show that GraphPO consistently outperforms chain- and tree-based baselines with the same token budgets or response budgets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前强化学习与可验证奖励（RLVR）范式下，大型推理模型在探索效率和奖励分配上的双重瓶颈。研究背景是，RLVR通常独立采样响应，仅基于最终答案的稀疏奖励进行策略优化。现有方法存在两个主要不足：一是独立采样导致中间推理步骤大量重复，造成计算资源的浪费和探索冗余；二是仅依赖最终答案的稀疏奖励难以识别并奖励对正确结果有贡献的中间步骤，限制了信用分配的有效性。尽管基于树的方法通过共享前缀和分支比较提供了更细粒度的信号，部分缓解了稀疏奖励问题，但树结构仍存在根本局限：不同分支一旦分开，即使达到相似的推理状态，也无法共享信息，导致重复探索；同时，方法仅在分支内部进行局部比较，忽略了跨分支的状态等价性，导致优势估计方差较高。为此，本文提出GraphPO（图策略优化），核心创新在于将推理轨迹建模为有向无环图，通过将语义等价的推理状态聚合成节点，合并冗余路径，从而重新分配计算预算以促进多样化探索。同时，GraphPO利用图结构推导过程监督信号，引入路径效率优势和分支正确性优势，以降低优势估计方差并提升推理效率，最终在相同计算预算下获得更优性能。

### Q2: 有哪些相关研究？

相关研究可从方法和应用两个类别归纳。方法类方面，本文主要与两类工作对比：一是基于稀疏奖励的强化学习（RLVR），这类方法使用二元结果奖励，但信号过于稀疏，难以有效分配信用到推理步骤；一些改进使用过程奖励模型（PRM）来稠密化监督，但需要昂贵标注且迁移性差。GraphPO通过合并语义等价状态实现后缀共享，在不依赖额外标注条件下提供更稠密的信用分配信号。二是基于树搜索的强化学习方法，如共享前缀的树结构回滚或动态分支扩展，它们通过前缀共享生成更多轨迹，但分支树拓扑结构中不同分支仍独立处理，即使后续达到语义等价状态也无法互相利用。GraphPO将这些分支合并为有向无环图（DAG），在等价类内实现信号共享和预算重分配。应用类方面，论文在不同规模的语言模型上进行了推理和智能体搜索基准测试，验证了方法有效性。与这些基础工作相比，GraphPO的创新在于：1）打破树结构的分支独立性，通过语义等价合并减少冗余探索；2）在DAG基础上设计效率优势和正确性优势的双重优势函数，从结果信号中派生过程监督；3）理论上证明了该方法能降低优势估计方差并提升推理效率。

### Q3: 论文如何解决这个问题？

GraphPO提出了一种基于图的强化学习框架，用于改进推理模型的策略优化。其核心方法是将传统的独立响应采样或树形展开转化为有向无环图（DAG）结构，其中节点代表从推理路径中总结出的语义状态，边代表具体的推理步骤。

整体框架包含四个主要模块：第一是**图构建**，通过逐步扩展节点和边，并使用策略模型本身对每个节点的语义状态进行嵌入，通过余弦相似度检测语义等价的状态，将相似的节点合并到同一个等价类中，从而让不同的推理路径共享后续的后缀，避免了冗余探索并可以重新分配采样预算。第二是**图奖励**，通过共享等价类内节点的下游奖励信号，将稀疏的最终答案奖励转化为稠密的步骤级奖励，具体做法是先为每个节点估计一个状态分数（基于可到达的终端状态及其验证奖励），然后计算步骤前后状态分数的差值作为步骤奖励，并用端点相似度进行折扣。第三是**双组图优势估计**，包含正确性组和效率组。正确性组比较离开同一语义状态的不同步骤，为其分配优势；效率组比较到达同一等价类的不同路径，通过路径长度差异分配优势，从而鼓励更短的、正确的推理路径。最后，**策略优化**采用类似PPO的目标函数，将正确性优势与效率优势相结合，进行梯度的稳定更新。其创新点在于通过语义等价合并实现推理路径的共享与预算重分配，并通过双组优势设计同时优化推理正确性与效率。

### Q4: 论文做了哪些实验？

实验在三个数学推理基准（AIME24、AIME25、MATH500）和两个额外推理基准（GPQA、LiveCodeBench）上进行，并扩展至四个深度搜索任务（General AI Assistant、WebWalker、BrowseComp、XBench）。使用Qwen2.5-7B-Instruct、Qwen2.5-7B-Math、Qwen3-8B-Base和Deepseek-R1-Distill-Qwen-7B四个LLM，对比方法包括链式RLVR（GRPO、DAPO）和树结构方法（TreeRL、SPO、TREE-GRPO、PROS、TreePO），GraphPO设置合并阈值κ=0.92、池化系数w=0.7。

主要结果：GraphPO在所有模型和基准上全面超越基线。例如在Qwen2.5-7B-Math上，GraphPO在AIME24达32.1%（TreeRL为26.1%，DAPO为25.7%），AIME25达24.5%，MATH500达91.6%，平均准确率40.9%领先第二名的PROS（37.7%）。在Deepseek-R1-Distill-Qwen-7B上，平均准确率64.0%远超PROS的60.8%。在搜索任务中，GraphPO整体得分11.8%，优于Tree-GRPO的10.3%。消融实验显示中等合并阈值性能最佳，过高（退化为树）或过低均导致性能下降。训练动态分析表明GraphPO熵衰减最慢（探索性最强）、生成长度最短（效率最高），且无需标注过程数据即可超越PRM方法。

### Q5: 有什么可以进一步探索的点？

以下是一些值得进一步探索的方向：

1. **动态图结构管理**：当前方法依赖预定义的语义等价阈值来合并节点，未来可以探索自适应的阈值调整策略，使图结构能随训练过程动态演化，避免过度合并或遗漏关键差异。

2. **长链推理中的图扩展成本**：随着推理步数增加，图节点和边可能呈指数级增长，需要研究高效的剪枝或近似算法（如重要性采样、拓扑压缩）来降低计算和存储开销。

3. **跨任务泛化性**：论文在数学推理和agent搜索任务上验证了效果，但尚未分析在代码生成、多步问答等异质任务上的表现，以及图结构是否可能引入任务特定的偏差。

4. **与过程奖励模型结合**：GraphPO从结果监督中推导过程信号，但若已有部分过程标注，如何融合外部过程奖励模型与图结构优势，可能进一步提升监督效率。

5. **图拓扑对策略梯度的理论分析**：可以更深入地刻画图合并策略对优势估计偏差和方差的影响边界，尤其是当语义等价判定存在噪声时，对学习稳定性的影响。

### Q6: 总结一下论文的主要内容

GraphPO（基于图的策略优化）是一种针对大型推理模型的新型强化学习框架。针对链式方法独立采样导致冗余探索和分支方法忽略语义状态分散的问题，GraphPO将轨迹建模为有向无环图，其中推理步骤作为边，语义状态作为节点。通过合并语义等价的推理路径并共享后缀，该框架将计算预算从冗余探索重新分配给多样化探索。同时，它引入双组图优势，利用正确性优势比较共享的出边，效率优势比较到达相同语义状态的不同入边，从而从结果奖励中导出过程监督。理论分析表明，该方法降低了优势估计方差并提升了推理效率。在多种大模型上的推理和智能体搜索实验显示，在相同预算下，GraphPO比链式和树式基线方法表现更优，显著提高了响应效率。
