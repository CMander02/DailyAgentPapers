---
title: "ToolSpec: Accelerating Tool Calling via Schema-Aware and Retrieval-Augmented Speculative Decoding"
authors:
  - "Heming Xia"
  - "Yongqi Li"
  - "Cunxiao Du"
  - "Mingbo Song"
  - "Wenjie Li"
date: "2026-04-15"
arxiv_id: "2604.13519"
arxiv_url: "https://arxiv.org/abs/2604.13519"
pdf_url: "https://arxiv.org/pdf/2604.13519v1"
categories:
  - "cs.CL"
tags:
  - "Tool Calling"
  - "Speculative Decoding"
  - "System Optimization"
  - "Latency Reduction"
  - "Retrieval-Augmented Generation"
  - "Schema-Aware"
  - "Multi-Step Interaction"
relevance_score: 8.0
---

# ToolSpec: Accelerating Tool Calling via Schema-Aware and Retrieval-Augmented Speculative Decoding

## 原始摘要

Tool calling has greatly expanded the practical utility of large language models (LLMs) by enabling them to interact with external applications. As LLM capabilities advance, effective tool use increasingly involves multi-step, multi-turn interactions to solve complex tasks. However, the resulting growth in tool interactions incurs substantial latency, posing a key challenge for real-time LLM serving. Through empirical analysis, we find that tool-calling traces are highly structured, conform to constrained schemas, and often exhibit recurring invocation patterns. Motivated by this, we propose ToolSpec, a schema-aware, retrieval-augmented speculative decoding method for accelerating tool calling. ToolSpec exploits predefined tool schemas to generate accurate drafts, using a finite-state machine to alternate between deterministic schema token filling and speculative generation for variable fields. In addition, ToolSpec retrieves similar historical tool invocations and reuses them as drafts to further improve efficiency. ToolSpec presents a plug-and-play solution that can be seamlessly integrated into existing LLM workflows. Experiments across multiple benchmarks demonstrate that ToolSpec achieves up to a 4.2x speedup, substantially outperforming existing training-free speculative decoding methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）工具调用过程中生成延迟过高的问题，这是实时LLM服务面临的主要挑战。研究背景是，随着LLM能力的提升，工具调用日益复杂，涉及多步骤、多轮次的交互以完成复杂任务，这导致工具调用频率增加，进而产生了显著的延迟。现有方法主要通过将工具调用轨迹建模为有向无环图以实现并行执行，或重叠工具执行与文本生成来加速，但这些工作主要关注**加速工具执行本身**，而忽视了工具调用生成阶段可能成为瓶颈。

通过初步分析，作者发现生成延迟在端到端推理延迟中占比很高（例如在ToolBench基准上可达约80%），且随着模型规模和生成序列长度增加而增长，成为许多工具使用场景中的主要延迟来源。现有加速方法未能充分解决这一生成瓶颈。

因此，本文的核心问题是：**如何高效加速工具调用的生成过程**。论文观察到工具调用输出具有高度结构化（通常遵循严格的JSON模式）和重复出现调用模式的特点。基于此，本文提出了ToolSpec方法，一种模式感知和检索增强的推测解码方法，旨在利用预定义的工具模式来生成高质量草稿，并通过检索相似历史调用来复用，从而显著减少生成延迟，提升整体效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：**高效工具调用**和**推测解码**。

在**高效工具调用**方面，现有工作主要关注优化工具的执行过程。例如，一些研究利用有向无环图（DAG）对工具间的依赖关系进行建模，以实现独立API调用的并行执行，从而降低延迟。另一类工作则尝试在生成过程中主动执行工具调用，以减少系统空闲时间。与这些聚焦于**工具执行**优化的方法不同，本文的工作将注意力转向加速**工具调用的生成过程**，旨在从生成层面进一步提升推理效率。

在**推测解码**方面，该范式已被广泛用于加速LLM推理。典型方法如Eagle系列，通过引入轻量级草稿模型来生成候选令牌序列，然后由目标LLM并行验证，但这类方法通常需要额外的训练或参数量。另一类研究则关注免训练的推测解码方法，例如Token Recycling通过存储历史步骤的候选令牌构建邻接矩阵，并利用广度优先搜索构建草稿树；SAM-Decoding则利用后缀自动机从输入上下文或静态文本语料库中高效检索高质量草稿。本文提出的ToolSpec属于免训练的推测解码方法，但其核心创新在于**针对工具调用的结构化特性**，利用预定义的模式和检索历史调用来生成精确草稿，这与通用文本的推测解码方法有显著区别。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为ToolSpec的、即插即用的推测解码方法来解决工具调用延迟高的问题。该方法的核心思想是利用工具调用高度结构化、符合预定模式且历史调用存在重复模式的特点，来生成高质量的草稿，从而加速解码过程。

其整体框架遵循标准推测解码范式，但创新性地集成了两种互补的草稿生成策略：**模式感知草稿生成**和**检索增强推测**。主要组件包括一个从工具文档中解析出的结构化模式、一个基于该模式构建的有限状态机（FSM）以及一个存储历史成功工具调用的数据存储库。

**模式感知草稿生成**是核心创新之一。该方法首先从工具文档中提取规范，定义出模式令牌集合、可调用工具集及其参数字段。基于此模式构建一个FSM，将工具调用生成过程分解为几个结构状态：工具名状态（qt）、参数名状态（qp）、参数值状态（qv）和普通自然语言生成状态（qo）。解码时，FSM根据生成的特定令牌（如 `<tool_call>`）和分隔符（如 `,`、`}`）在这些状态间转换。对于结构性状态（如qt和qp），由于选择范围受模式严格约束（例如，工具名必须来自预定义集合），ToolSpec采用**确定性模式令牌填充**策略，通过约束解码并行生成所有候选草稿序列。对于开放性状态（如qv和qo），则切换到通用的推测生成算法来预测可变字段（如参数值）。这种在确定性填充和推测生成之间的无缝切换，极大地提高了结构性部分的草稿准确性和生成效率。

**检索增强推测**是另一项关键技术，用于在序列层面加速生成。它基于工具调用存在重复模式的观察，维护一个历史成功调用的数据存储库。对于当前查询，该方法检索出最相似的k个历史工具调用。然后，将当前已生成输出的后缀与检索到的历史调用进行匹配。一旦找到匹配的后缀，就直接提取历史调用中接下来的n个令牌作为后续生成的草稿候选。这种方法特别适用于加速那些具有重复结构的工具调用，例如在工具名和键值对对齐后，剩余的调用结构往往遵循固定模式。

最终，由这两种策略生成的草稿序列会被提交给目标大语言模型进行并行验证，接受其中最长的、符合模型概率分布的前缀。通过结合模式的结构性约束和历史模式的复用，ToolSpec能够以极低的开销生成高准确度的草稿，从而最大化每次推测的接受长度，实现了解码并行度的显著提升和端到端延迟的大幅降低。实验表明，该方法在多个基准测试上实现了最高4.2倍的加速，显著优于其他无需训练的推测解码方法。

### Q4: 论文做了哪些实验？

论文在多个模型和基准测试上进行了实验，以评估ToolSpec方法的加速效果。实验设置方面，主要使用了Qwen2.5-Instruct系列、ToolLLaMA系列、LLaMA-3.1-8B-Instruct和LLaMA-3.2-3B-Instruct等模型，并在四个广泛使用的工具调用基准测试上评估：API-Bank、ToolAlpaca、BFCLv2和ToolBench。检索参数k设为3，后缀匹配长度L∈{5,6,7}，延续提取长度n∈{32,16,8,8}，并采用Token Recycling作为基础推测策略。

对比方法包括三种即插即用方法：PLD、TR和SAM-Decoding，以及需要训练的先进方法Eagle-2和Eagle-3。评估指标包括平均接受令牌数（#MAT）、吞吐量（tokens/s）和相对于标准自回归解码的端到端加速比。

主要结果显示，ToolSpec在所有模型和任务上均优于现有方法，实现了3.5倍到4.2倍的加速比。相比之前最佳方法，其加速比相对提升了高达61%（从2.5倍提升至4.2倍）。关键数据指标方面，平均接受令牌数（#MAT）在不同设置下介于4.02到5.49之间，而推测开销仅约6%，使得高效率得以转化为端到端加速。在专门用于工具调用的ToolLLaMA模型上，ToolSpec在ToolBench基准上也实现了约3.7倍的加速。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其假设工具调用严格遵循预定义模式且存在重复模式，这在高度动态或非结构化的任务场景中可能不适用。未来研究可探索如何增强系统对模式外调用和罕见模式的适应性，例如引入自适应学习机制，动态更新检索库或调整推测策略。此外，可结合强化学习优化推测与验证的平衡，减少因草案错误导致的回滚开销。从工程角度看，将方法扩展到更大模型（如千亿参数）和多模态工具调用是重要方向，同时需评估在边缘设备上的部署可行性，以支持低延迟实时应用。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）工具调用过程中因多步、多轮交互导致延迟显著增加的问题，提出了一种名为ToolSpec的加速方法。其核心贡献在于设计了一种无需额外训练、即插即用的推测解码方案，通过利用工具调用的结构化特性来提升生成效率。

具体而言，该方法首先基于经验分析发现工具调用轨迹高度结构化、符合约束模式且常出现重复调用模式。为此，ToolSpec结合了模式感知和检索增强两种策略：一方面，它利用预定义的工具模式生成精确的草稿，采用有限状态机在确定性模式令牌填充和可变字段的推测生成之间交替；另一方面，它检索相似的历史工具调用并将其复用为草稿，以进一步提高效率。

实验结果表明，ToolSpec在多个基准测试中实现了最高4.2倍的加速，显著优于现有的无需训练的推测解码方法，同时保持了输出分布的一致性。这项工作为LLM的高效工具使用提供了实用的解决方案，并揭示了格式遵循对加速效果的重要影响。
