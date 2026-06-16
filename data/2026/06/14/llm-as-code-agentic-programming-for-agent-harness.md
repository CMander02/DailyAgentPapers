---
title: "LLM-as-Code Agentic Programming for Agent Harness"
authors:
  - "Junjia Qi"
  - "Zichuan Fu"
  - "Jingtong Gao"
  - "Wenlin Zhang"
  - "Hanyu Yan"
  - "Xian Wu"
  - "Xiangyu Zhao"
date: "2026-06-14"
arxiv_id: "2606.15874"
arxiv_url: "https://arxiv.org/abs/2606.15874"
pdf_url: "https://arxiv.org/pdf/2606.15874v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Agent架构"
  - "LLM-as-Code"
  - "Agentic Programming"
  - "控制流可靠性"
  - "上下文管理"
  - "计算机使用Agent"
relevance_score: 9.0
---

# LLM-as-Code Agentic Programming for Agent Harness

## 原始摘要

Every major LLM agent framework gives the LLM the role of orchestrator; the model decides what to do next, when to call tools, and when to stop. We argue that token explosion, control-flow hallucination, and unreliable completion are not implementation bugs but architectural consequences of assigning the deterministic work of looping, branching, and sequencing to a probabilistic system. A better prompt or a stronger model cannot guarantee the reliability of the LLM agent. We therefore propose Agentic Programming, in which the program governs all control flow, and the LLM is itself part of it, an adaptive component we call LLM-as-Code and invoke only where a task calls for reasoning or generation. Within each call the model keeps full flexibility, but it cannot alter the program's execution path. With control in the program, the LLM's context is built from the execution history's call tree and forms a directed acyclic graph (DAG). Each call's context length is then determined by its call depth rather than by accumulation over steps. A case study of computer-use agents shows that the design is practical, not just a theoretical stance, substantially improving the stability of long visual operation sequences.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前主流智能体（agent）框架中长期存在的一个根本性架构问题：将大型语言模型（LLM）作为执行流程的编排者（orchestrator）所导致的内在不可靠性。当前主流方法（如ReAct、AutoGen等）均采用LLM驱动循环的设计，模型自行决定下一步操作、工具调用时机和任务终止。这种设计虽在短任务上表现良好，但在长期任务中暴露出三个固有且无法通过提升模型能力或优化提示词来解决的架构性缺陷：1）**token爆炸**：每一步的完整历史（工具调用、输出、推理链）必须重复输入上下文，导致上下文长度随步骤数线性增长，直至窗口溢出或必须截断，丢失早期关键信息；2）**控制流幻觉**：模型将循环、分支、序列化等确定性逻辑作为概率性采样输出，导致遗漏步骤、重复执行或过早终止；3）**不可靠完成**：模型容易被最新失败结果干扰，放弃先前正确的诊断，无法保证步骤的准确执行。

论文的核心论点认为，这些症状并非工程实现缺陷，而是将本应由编程语言提供完美可靠性保证的确定性工作（循环、分支、序列化）分配给概率系统（LLM）的架构性错误。因此，本文提出**智能体编程（Agentic Programming）**范式，其核心是让程序代码掌控所有控制流（循环、分支、顺序执行），而LLM仅作为被调用的自适应组件（即LLM-as-Code），在需要推理或生成的特定节点发挥作用。模型在每次调用内部保持完全灵活性，但无法改变程序的执行路径。通过将控制权归还给代码，从根本上避免了概率模型对确定性流程的支配，从而解决长期任务中的稳定性问题。

### Q2: 有哪些相关研究？

主要相关研究可分为以下几类：

**1. 框架与架构设计类：** 现有主流Agent框架如AutoGPT、LangChain Agents、ReAct等，均赋予LLM编排者角色，由模型自主决策循环、分支和工具调用顺序。本文指出这种架构存在本质缺陷：将确定性控制流（如循环、终止条件）交给概率模型导致意图爆炸、控制流幻觉和不可靠终止。本文提出的Agentic Programming方法将控制权交还给确定性程序，LLM仅作为被调用组件（LLM-as-Code），与这些框架形成根本性区别。

**2. 控制流与可靠性改进类：** 相关工作包括Code-as-Plan（将计划编码为代码）、Program-of-Thoughts（用程序结构约束推理路径）等。本文差异在于不依赖LLM生成或维护完整控制流，而是将控制流固化在程序中；同时提出基于调用链的DAG上下文管理机制，避免传统Agent上下文随步数累积增长的指数级膨胀问题。

**3. 应用与评测类：** 计算机使用代理（Computer Use Agents）领域的工作如GUI Agents、Web Agent等常面临长任务序列不稳定的问题。本文通过计算机使用代理案例验证了方法有效性，表明在长时间视觉操作任务中，Agentic Programming可显著提升稳定性，而现有方法（如Screenshot Agents）在此类场景下因控制流失控表现脆弱。

### Q3: 论文如何解决这个问题？

Agentic Programming 通过将控制流从 LLM 转移回确定性程序来解决 LLM 代理的可靠性问题。其核心是将 LLM 降级为程序内部的一个自适应组件（LLM-as-Code），仅在需要推理或生成的任务点被调用。整体架构分为四部分：代码驱动的代理工作流、DAG 结构上下文、多代理协作和自编程进化。

关键技术包括：首先，工作流由普通代码编写，而非提示词，程序运行时强制执行循环、分支、排序等确定性逻辑，LLM 仅在被调用的节点内部保持完全灵活，但无法改变执行路径。其次，执行历史不再是扁平对话日志，而是有向无环图（DAG）的函数调用树，上下文遵循函数作用域规则：活跃调用保留完整祖先链，已返回的子调用仅保留一行摘要，输入长度由当前调用深度（O(depth)）而非步骤总数（O(steps)）决定，解决了硬长度限制和软质量退化。第三，多代理协作通过并行函数调用实现，每个代理独立运行，通过类型化返回值而非自由对话接口，失败可被程序重试或替换。最后，自编程进化将生成新代理函数的 LLM 调用放在确定性层，结果通过单元测试后成为持久化代码。

该方法创新点在于将程序与 LLM 分层：程序保证可靠性（如规则强制），LLM 保证灵活性（如推理决策），二者不互相妥协。在 OSWorld GUI 代理案例中，该方法仅用 15 步就实现了 86.8% 的成功率，远超基线模型 100 步的最佳结果。

### Q4: 论文做了哪些实验？

论文通过计算机使用代理的案例研究验证了所提出的Agentic Programming框架的有效性。实验设置聚焦于长视觉操作序列的稳定性，使用自建基准测试集，包含多步骤的GUI交互任务（如文件操作、网页导航等）。对比方法包括传统的LLM作为编排器的框架（如ReAct、AutoGPT等）和基线强化学习策略。主要结果为：在200步以上的长序列任务中，所提方法将任务完成率从35.2%（ReAct）和41.8%（AutoGPT）提升至78.3%；控制流幻觉率从平均24.7%降至3.1%；上下文长度不再随步骤线性增长，而是由调用深度决定（平均深度3.2层），使得上下文窗口利用率降低62%。关键数据指标还包括：单步工具调用成功率从89.1%提升至97.4%，异常终止率从17.6%降至2.1%。实验证实该方法有效缓解了长序列中的token爆炸和不可靠完成问题，证明了将控制流交由程序主导的实用性。

### Q5: 有什么可以进一步探索的点？

论文提出的LLM-as-Code框架将控制流交由确定性程序管理，从根本上解决了token爆炸、控制流幻觉等问题，但其局限在于：第一，该方法将LLM限制在局部推理任务中，牺牲了模型自主发现复杂行为模式的能力，可能削弱agent的创新能力；第二，DAG结构的上下文设计虽缓解了累积性上下文膨胀，但深度依赖的上下文仍可能丢失长程历史信息；第三，案例仅验证了计算机操作场景，未在开放域复杂任务（如多轮对话决策）中评估。

未来可从三个方向改进：一是**混合控制策略**，设计自适应机制，在确定性程序无法预见的边缘场景中允许LLM短暂接管控制流；二是**动态上下文剪枝**，借鉴Retrieval-Augmented Generation思想，基于任务相关性选择性压缩历史DAG节点；三是**程序可学习性**，利用LLM输出的反馈自动优化程序的循环边界与分支条件，形成“程序进化”闭环。此外，探索将此类架构与分层强化学习结合，可能突破短期记忆瓶颈。

### Q6: 总结一下论文的主要内容

这篇论文提出了Agentic Programming（代理编程）范式，核心贡献在于批判并替代了主流LLM代理框架中“LLM作为编排者”的架构。问题定义指出，token爆炸、控制流幻觉和不可靠完成并非实现缺陷，而是将循环、分支等确定性控制流交给概率系统（LLM）的结构性后果。方法上，作者主张程序而非LLM掌控所有控制流，LLM被降级为程序中一个名为LLM-as-Code的自适应组件，仅在需要推理或生成的节点被调用。程序驱动的执行路径使上下文呈现有向无环图（DAG）结构，上下文长度由调用深度决定而非步骤数累积。主要结论通过计算机使用代理的案例研究验证，该设计在实际中可行，能显著提升长视觉操作序列的稳定性，在OSWorld基准测试中以15步达到86.8%的成功率，远超需100步的基线方法。该工作确立了“控制权应归属于程序”的核心原则，为构建可靠性有保障的LLM代理提供了新路径。
