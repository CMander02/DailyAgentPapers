---
title: "SpecHop: Continuous Speculation for Accelerating Multi-Hop Retrieval Agents"
authors:
  - "Mehrdad Saberi"
  - "Keivan Rezaei"
  - "Soheil Feizi"
date: "2026-05-21"
arxiv_id: "2605.21965"
arxiv_url: "https://arxiv.org/abs/2605.21965"
pdf_url: "https://arxiv.org/pdf/2605.21965v1"
github_url: "https://github.com/mehrdadsaberi/spechop"
categories:
  - "cs.CL"
tags:
  - "LLM Agent加速"
  - "Multi-Hop检索"
  - "推测执行"
  - "延迟优化"
  - "工具使用"
relevance_score: 8.5
---

# SpecHop: Continuous Speculation for Accelerating Multi-Hop Retrieval Agents

## 原始摘要

Large language models increasingly use external tools such as web search and document retrieval to solve information-intensive tasks. However, multi-hop tool use in complex tasks introduces substantial latency, since the model must repeatedly wait for tool observations before continuing. We study how to accelerate such trajectories without changing the final trajectory the model would have taken without acceleration, assuming access to faster but less reliable speculator tools. We develop a theoretical framework for lossless speculation in multi-hop tool-use settings, characterizing the optimal achievable latency gain. We propose SpecHop, a continuous speculation framework that maintains multiple speculative threads, verifies predicted observations asynchronously as target tool outputs arrive, commits correct branches, and rolls back incorrect ones. This preserves accuracy while reducing wall-clock latency. We show that SpecHop can approach oracle latency gains with enough active threads. Empirically, on retrieval-augmented multi-hop tasks, SpecHop closely matches theoretical predictions and reduces latency by up to 40\% in some settings. Code: https://github.com/mehrdadsaberi/spechop

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对的是大型语言模型（LLM）在多跳工具使用场景中的延迟瓶颈问题。研究背景是，LLM 越来越多地依赖外部工具（如网页搜索、文档检索）来执行复杂的信息密集型任务，例如深度研究和智能体工作流。在这些多跳交互中，模型的轨迹是一个顺序的推理-工具调用-等待观察的循环过程。现有方法的不足在于，每次工具调用（如网页搜索）都会引入显著的等待延迟，而模型在等待期间只能空闲。实际评测显示，在 GPT-5 的深度研究智能体中，网页搜索平均占了端到端延迟的 73%，复杂情况下甚至高达 91%。这严重限制了整体效率。本文要解决的核心问题是：如何在保证最终输出轨迹完全不变（即“无损加速”）的前提下，通过利用更快但可靠性较低的推测器（speculator），来加速多跳工具使用轨迹的执行，从而大幅降低实际等待时间。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是**推测解码**领域，其核心是“草稿-验证”范式，用小模型快速生成候选token再由大模型验证，保证输出无损。本文借鉴了这一思想，但将推测对象从token扩展到工具观测结果，这是本质区别。

其次，**推测执行**原理源自计算机体系结构，通过分支预测和回滚机制避免流水线停顿。本文将其从指令级执行迁移到语言模型智能体的轨迹级工具调用，是一个跨领域的创新应用。

第三，**检索增强生成（RAG）与智能体工具使用**的加速研究。相关工作包括：在流水线初始阶段进行静态检索并并行使用多个推测模型；通过识别生成模式提前预测工具调用，从而提前启动工具；以及最接近本文的工作，即用更快的推测模型替代部分外部调用。与这些工作不同，本文提出了连续推测框架SpecHop，能维护多个推测线程，通过异步验证和回滚，在不改变最终轨迹的前提下实现损失加速，理论分析和实验均表明其能接近最优延迟增益。

### Q3: 论文如何解决这个问题？

SpecHop通过连续投机执行框架加速多跳检索代理，核心思路是利用更快的投机工具并行推测结果，同时异步验证以保证准确性。整体框架将轨迹分解为多个状态跳，每个跳包括生成中间段、调用工具获取观察。SpecHop维护多个并行投机线程：从当前状态开始，模型生成段和动作后，并行启动目标工具和投机工具，投机工具快速返回推测观察，模型立即基于该观察继续执行下一跳，从而创建新的投机线程。系统同时保持k个活跃线程，形成投机窗口。

主要模块包括：目标工具（准确但慢）、投机工具（快但近似）、验证器（比较两工具输出是否等价）。关键技术是异步验证与滚动恢复：当最早线程的目标工具结果返回时，验证器将其与对应的投机观察比较。若匹配，则提交该跳并向前移动窗口，立即从最后一个活跃线程继续投机；若不匹配，则丢弃所有下游投机线程，回滚到已验证的目标工具状态继续执行。这种方法避免了等待每个工具结果，只要投机成功就持续前推。

创新点在于连续投机机制：通过保持k个活跃线程持续推测，避免了固定窗口的停顿瓶颈，使系统能接近理论最优延迟增益（当k足够大时）。理论分析表明，相对延迟取决于投机成功率p、投机工具相对速度α和模型解码与工具延迟比β，实验在检索增强多跳任务上实现高达40%的延迟降低。

### Q4: 论文做了哪些实验？

论文在三个多跳问答数据集（2WikiMultihopQA、MuSiQue、DeepResearch-9K）上评估了SpecHop。实验设置如下：使用CoRAG-Llama3.1-8B-MultihopQA作为生成器模型，分别用E5检索（本地KILT/Wikipedia语料库）和Web搜索（DuckDuckGo）作为目标工具。对比方法包括标准顺序执行和仅使用推测器的完全推测执行。实验使用多种推测器模型，包括Llama 3.1 8B、Qwen 3 8B、GPT-4o mini和GPT-4o，并采用基于规则（精确匹配与Jaccard相似度）的验证器。

主要结果表明：SpecHop的延迟改善接近理论最优值。例如，在2WikiMultihopQA上以GPT-4o为推测器进行Web搜索时，相对延迟为0.60（理论最优0.50），实现了40%的延迟降低。重要的是，SpecHop完全保持了任务准确性——EM和F1分数与标准执行几乎一致（如Web搜索设置下2WikiMultihopQA的EM分别为68.7和69.3），而完全推测则导致严重退化（EM从68.7降至38.7）。此外，通过调整活跃线程数k，可以在延迟和计算成本之间进行权衡（如DeepResearch-9K上k=3时相对延迟0.75）。最后，使用基于缓存的推测器（5%-25%的索引）也获得了显著加速（Web搜索相对延迟降至0.64）。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其主要依赖的“speculator”模型假设了较快的响应但可靠性较低，实际应用中可能面临speculator性能波动或失效的风险，特别是当预测与真实结果偏差较大时，回滚机制会引入额外开销。此外，当前框架主要针对检索式多跳任务，未涉及更复杂的工具链（如代码执行、数据库查询）或动态决策场景，且理论分析假设了目标工具响应时间固定，现实中存在不可预测的延迟。

未来可从以下方向深入探索：一是研究自适应speculator切换策略，根据历史准确率动态调整推测线程数量或替换更快/更准的模型；二是扩展至异构工具场景，例如结合代码执行或结构化查询，并设计跨工具的并发推测与验证机制；三是优化回滚成本，通过部分回滚或缓存中间状态减少验证失败时的计算浪费。此外，探索将SpecHop与模型训练联合优化，让LLM本身学习更可靠的推测路径，或引入不确定性估计来动态决定何时开启推测执行。

### Q6: 总结一下论文的主要内容

这篇论文提出了 SpecHop，一种用于加速多跳检索代理的连续推测框架。核心问题是语言模型在多步工具调用中因等待工具返回结果而产生的高延迟。SpecHop 通过维护多个并行的推测线程，在目标工具执行的同时，利用更快的“推测器”预测后续观察结果并继续执行。这些推测结果会通过验证器与工具返回的真实结果进行异步对比，以提交正确分支并回滚错误分支，从而在不改变原模型轨迹的前提下，显著降低端到端壁钟延迟。实验结果表明，在多个检索增强的多跳问答数据集上，SpecHop 保持了任务准确率，并将延迟最高降低了 40%，理论分析与实验结果高度一致。该工作为加速复杂的工具型智能体流程提供了理论框架和实用方法。
