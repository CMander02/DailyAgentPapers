---
title: "Think, But Don't Overthink: Reproducing Recursive Language Models"
authors:
  - "Daren Wang"
date: "2026-03-03"
arxiv_id: "2603.02615"
arxiv_url: "https://arxiv.org/abs/2603.02615"
pdf_url: "https://arxiv.org/pdf/2603.02615v1"
github_url: "https://github.com/drbillwang/rlm-reproduction"
categories:
  - "cs.CL"
tags:
  - "Agent架构"
  - "工具使用"
  - "推理"
  - "记忆"
  - "基准评测"
relevance_score: 9.0
---

# Think, But Don't Overthink: Reproducing Recursive Language Models

## 原始摘要

This project reproduces and extends the recently proposed ``Recursive Language Models'' (RLMs) framework by Zhang et al. (2026). This framework enables Large Language Models (LLMs) to process near-infinite contexts by offloading the prompt into an external REPL environment. While the original paper relies on a default recursion depth of 1 and suggests deeper recursion as a future direction, this study specifically investigates the impact of scaling the recursion depth. Using state-of-the-art open-source agentic models (DeepSeek v3.2 and Kimi K2), I evaluated pure LLM, RLM (depth=1), and RLM (depth=2) on the S-NIAH and OOLONG benchmarks. The findings reveal a compelling phenomenon: Deeper recursion causes models to ``overthink''. While depth-1 RLMs effectively boost accuracy on complex reasoning tasks, applying deeper recursion (depth=2) or using RLMs on simple retrieval tasks paradoxically degrades performance and exponentially inflates execution time (e.g., from 3.6s to 344.5s) and token costs. Code and data are available at: https://github.com/drbillwang/rlm-reproduction

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在复现并拓展近期提出的“递归语言模型”（RLM）框架，以探究递归深度对模型性能的影响。研究背景在于，传统大语言模型（LLM）受限于上下文长度，难以处理超长输入，而RLM通过将提示词卸载到外部REPL环境中，允许模型以编程方式分解输入并递归调用自身，理论上能处理近乎无限的上下文。现有方法（即原始RLM论文）默认采用递归深度为1，虽在复杂任务上表现出色，但尚未系统探索更深递归的效果，也未在简单任务上充分验证其必要性。

现有方法的不足在于：原始工作仅验证了深度为1的RLM在复杂推理任务上的优势，但未深入分析递归深度扩展带来的潜在问题，也未在简单检索任务上评估其效率。本文要解决的核心问题是：当增加递归深度（如深度2）时，RLM在简单和复杂任务上的性能如何变化？是否存在“过度思考”风险？通过使用先进开源模型（DeepSeek v3.2和Kimi K2）在S-NIAH（简单检索）和OOLONG（复杂推理）基准上的实验，论文发现深度1的RLM能有效提升复杂任务准确率，但在简单任务上反而劣于纯LLM；更深递归（深度2）会导致性能下降、执行时间和令牌成本指数级增长，揭示出模型“过度思考”的负面效应，从而明确了递归深度需根据任务复杂度权衡的结论。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕**递归语言模型（RLMs）的扩展与评估**展开，可分为方法类、应用类与评测类。

在**方法类**方面，核心相关工作是Zhang等人（2026）提出的原始RLMs框架，它通过将提示卸载到外部REPL环境来处理超长上下文。本文直接复现并扩展了这一框架，其核心区别在于**系统性地研究了递归深度（depth）的缩放影响**，而原论文仅使用了默认深度1并将更深递归列为未来方向。

在**应用与评测类**方面，相关研究包括用于评估长上下文与推理能力的基准。本文选用了**S-NIAH（检索任务）和OOLONG（复杂推理任务）** 这两个基准进行实证评估。与一般性的基准评测工作不同，本文的侧重点在于**分析RLMs在不同任务类型和递归深度下的性能与成本变化**，特别是发现了“过度思考”现象。

此外，本文还涉及**智能体模型**的相关研究，因为它使用了当前先进的开源智能体模型（如DeepSeek v3.2和Kimi K2）作为基础LLM来驱动RLMs。这区别于原论文可能使用的模型，旨在检验RLMs框架在不同强大模型上的泛化性。

总之，本文与相关工作的关系是**继承、深化和实证检验**。它在原始RLMs方法的基础上，通过控制递归深度这一关键变量，在标准基准上揭示了性能与效率的权衡规律，从而对RLMs的实际应用边界提供了新的重要见解。

### Q3: 论文如何解决这个问题？

论文通过构建并扩展“递归语言模型”（RLM）框架来解决大语言模型处理超长上下文时面临的计算负担和性能瓶颈问题。其核心方法是设计一个外部REPL（读取-求值-打印循环）环境，将长提示词（prompt）卸载至此环境中执行，使LLM能够以递归方式交互式地处理近乎无限的上下文内容，而无需一次性将全部信息加载至模型内部。

整体框架包含三个主要模块：主控LLM、外部REPL环境以及递归调度器。主控LLM负责接收用户查询，并根据当前递归深度决定是否将计算任务（如信息检索、推理步骤）委托给REPL环境执行；REPL环境则模拟一个可编程的交互式会话，能够存储上下文、执行代码或检索操作，并将结果返回给主控模型；递归调度器管理递归深度，控制任务分解与结果整合的层次。关键技术在于通过递归调用机制，将复杂任务分解为多个子步骤，在REPL中逐步执行，从而避免模型因一次性处理过长输入而产生的注意力稀释或记忆溢出问题。

本研究的创新点在于对原始RLM框架（默认递归深度为1）进行了深度扩展实验，首次系统评估了递归深度缩放的影响。研究发现，递归深度为1时，RLM能有效提升复杂推理任务（如OOLONG长上下文QA）的准确性；但当深度增加至2时，模型会出现“过度思考”（overthink）现象，即在简单检索任务（如S-NIAH）上性能反而下降，且执行时间和令牌消耗呈指数级增长（例如从3.6秒激增至344.5秒）。这一发现揭示了递归深度与任务复杂度之间的平衡关系：适度的递归有助于分解难题，但过深的递归会导致冗余计算和效率骤减，从而为RLM的实际应用提供了重要的参数优化依据。

### Q4: 论文做了哪些实验？

本研究主要进行了两项核心实验，以评估递归语言模型（RLM）在不同递归深度下的性能与效率。

**实验设置与数据集**：实验使用了两种先进的开源智能体模型：DeepSeek v3.2 和 Kimi K2。评估了三种配置：纯基础大语言模型（Base LLM）、RLM（递归深度=1）和 RLM（递归深度=2）。测试在两个基准上进行：S-NIAH（用于评估恒定复杂度O(1)的检索任务）和 OOLONG（用于评估需要线性O(N)扩展和语义聚合的复杂推理任务）。

**主要结果与关键指标**：
1.  **准确率**：在简单的S-NIAH任务上，引入RLM反而损害了性能。例如，DeepSeek v3.2的准确率从基础模型的100%降至深度1的85%，深度2的70%。在复杂的OOLONG任务上，RLM（深度1）对基础能力弱的模型有显著提升（如DeepSeek v3.2从0%提升至42.1%），但深度2的递归均导致性能下降（DeepSeek v3.2降至33.7%）。对于本身长上下文能力强的Kimi K2，RLM则导致其性能从86.6%崩溃至60%（深度1）和55%（深度2）。
2.  **效率与成本**：递归深度导致执行时间和令牌消耗呈指数级增长。以DeepSeek v3.2在S-NIAH任务为例，执行时间从基础模型的3.6秒激增至深度1的89.3秒和深度2的344.5秒。Kimi K2在深度2时单次查询时间峰值达545.5秒。令牌使用量和相应的API成本在启用RLM架构后也急剧增加。
3.  **定性分析**：研究通过分析原始响应日志，揭示了RLM特有的三种失败模式：深度递归导致的“参数化幻觉”（模型脱离上下文依赖预训练知识）、REPL环境中的“格式化崩溃”（模型混淆代码环境与最终输出格式）以及“表演性推理与无尽验证”（模型陷入过度的、循环的自我验证，极大延长执行时间）。这些发现直接印证了“思考，但不要过度思考”的核心假设。

### Q5: 有什么可以进一步探索的点？

基于论文内容，该研究揭示了递归语言模型（RLM）在深度增加时出现的“过度思考”问题，这为未来研究指明了几个关键方向。首先，论文明确指出当前RLM缺乏有效的停止机制，导致深度递归时产生冗余循环和格式崩溃，因此设计更智能的递归终止条件是迫切的改进点。例如，可以引入动态深度评估或置信度阈值，让模型自行判断何时停止递归调用。

其次，论文提到深度递归会引发参数化幻觉和性能劣化，这表明现有LLM与程序化环境的对齐不足。未来可以探索专门针对递归推理进行预训练或微调的“原生RLM”，使其内在适应外部REPL环境，从而减少幻觉并保持格式约束。

此外，研究发现RLM对简单任务或本身具备强大上下文能力的模型（如Kimi K2）反而有害，这提示需要更精细的任务适应性机制。未来工作可以研究如何根据任务复杂度动态调整递归策略，避免不必要的递归开销。

最后，深度递归导致的执行时间和令牌成本指数级增长是实际应用的瓶颈。除了算法优化，未来可以结合系统级改进，如缓存中间结果或并行化子调用，以提升效率。总之，这些方向共同指向了使RLM更高效、鲁棒且实用的目标。

### Q6: 总结一下论文的主要内容

这篇论文对Zhang等人（2026）提出的“递归语言模型”（RLM）框架进行了复现和扩展研究。RLM通过将长提示词卸载到外部REPL环境中处理，使大语言模型能够处理近乎无限的上下文。原论文默认递归深度为1，本研究则重点探究了增加递归深度的影响。

论文的核心贡献在于揭示了RLM应用中“思考，但勿过度思考”的权衡现象。作者使用DeepSeek v3.2和Kimi K2等先进开源模型，在S-NIAH（简单检索）和OOLONG（复杂推理）基准上评估了纯LLM、RLM（深度=1）和RLM（深度=2）的性能。研究发现：深度为1的RLM能有效提升复杂推理任务的准确率（如将DeepSeek v3.2在OOLONG上的准确率从0%提升至42.1%），但将其用于简单检索任务或使用深度为2的递归时，性能反而会下降。更深度的递归会导致模型“过度思考”，产生冗余子调用，引发格式崩溃、参数幻觉和性能回退，同时造成执行时间（例如从3.6秒激增至344.5秒）和令牌成本的指数级增长。

主要结论是，虽然RLM在理论上能扩展模型上下文窗口，但其巨大的延迟开销、爆炸的API成本以及递归退化风险，使得其大规模工业部署目前仍面临挑战，尤其当现代前沿模型已具备原生长上下文处理能力时。未来工作需要设计更好的REPL停止机制，并训练能本征适应程序化环境而不产生幻觉或格式错误的原生RLM。
