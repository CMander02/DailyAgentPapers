---
title: "ExComm: Exploration-Stage Communication for Error-Resilient Agentic Test-Time Scaling"
authors:
  - "Woomin Song"
  - "Beomjun Kim"
  - "Daewon Choi"
  - "Sai Muralidhar Jayanthi"
  - "Saket Dingliwal"
  - "Jinwoo Shin"
  - "Aram Galstyan"
date: "2026-05-21"
arxiv_id: "2605.22102"
arxiv_url: "https://arxiv.org/abs/2605.22102"
pdf_url: "https://arxiv.org/pdf/2605.22102v1"
categories:
  - "cs.AI"
tags:
  - "Agent通信"
  - "Agent推理"
  - "错误传播"
  - "多智能体协作"
  - "测试时扩展"
  - "信念管理"
relevance_score: 9.5
---

# ExComm: Exploration-Stage Communication for Error-Resilient Agentic Test-Time Scaling

## 原始摘要

A common failure mode in long-horizon agentic test-time scaling is error propagation, where factual errors or invalid deductions introduced at intermediate steps persist in the agent's belief state and contaminate later reasoning. Existing test-time scaling methods provide limited control over this process, as they often rely on agents to detect their own mistakes, select among flawed trajectories, or refine solutions only after errors have already shaped the reasoning path. We propose ExComm, a communication protocol for exploration-stage agentic test-time scaling. ExComm is motivated by the empirical observation that the majority of intermediate errors in parallel agentic reasoning produce detectable cross-agent factual conflicts. Leveraging the iterative structure of agentic workflows, ExComm periodically audits agent belief states to detect such conflicts, resolves them through a dedicated tool-based verification loop, and returns concise, targeted feedback to the involved agents. Corrections are incorporated through soft belief updates, which append verified feedback rather than overwriting existing beliefs. Furthermore, to prevent collapsing trajectory diversity due to communication, ExComm further introduces a trajectory diversification module that redirects redundant trajectories toward orthogonal strategies. Experiments on AIME 2024, AIME 2025, and GAIA with Gemini-2.5-Flash-Lite and Qwen3.5-4B show that ExComm consistently outperforms strong test-time scaling baselines, achieving average performance gains of 5.7% and 5.0% over the best-performing baselines, respectively. Further analyses demonstrate improved error recovery, favorable scaling behavior, stronger diversity than adapted communication baselines, and the best performance-cost trade-off among the evaluated methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长时间跨度智能体测试时扩展中的错误传播问题。在现有方法中，当智能体在中间步骤引入事实错误或无效推理时，这些错误会持续存在于智能体的信念状态中，污染后续推理。当前测试时扩展方法对此控制有限：并行采样依赖智能体自身检测错误，但自我修正不可靠；树搜索通过分支选择而非显式修正来缓解错误，未剪枝的错误会继续影响推理；后处理聚合或改进方法则在错误已塑造推理路径后才介入。然而，智能体工作流具有反复与工具交互并更新信念的迭代结构，为早期错误检测与修正提供了自然点。本文的核心创新是利用该结构，提出ExComm协议，在探索阶段通过检测并行智能体推理轨迹间的事实冲突（实证发现67-71%的中间错误会产生跨智能体事实冲突），利用工具验证循环解决冲突，并进行软信念更新（追加而非覆盖已验证反馈），同时引入轨迹多样化模块防止信息共享导致的轨迹坍缩，从而实现在错误传播前修正信念，提升最终答案质量。

### Q2: 有哪些相关研究？

相关工作主要分为三大类。第一类是**LLM Agent系统**，这类工作关注如何将大模型与工具（如搜索、计算器）结合，通过ReAct循环等框架执行复杂任务。本文与它们的核心区别在于，本文充分利用了Agent工作流中“探索阶段”的迭代结构，在推理过程中而非最终答案生成后进行干预，从而进行错误恢复。

第二类是**测试时扩展方法**，主要包含并行采样、顺序修正和搜索方法。虽然这些方法在静态文本推理中效果显著，但本文指出它们在长程Agent任务中无法有效阻止错误累积。与这些方法不同，ExComm不依赖Agent自我检错或在错误轨迹中选择，而是通过主动检测和修正跨Agent的事实冲突来实现错误控制。

第三类是**多Agent通信方法**，如多Agent辩论和混合Agent（Mixture-of-Agents）。这些方法通过交换、聚合或精炼中间输出来提升答案质量。本文与其核心区别在于目标不同：ExComm专注于探索阶段的错误控制，通过工具验证来检测并解决事实冲突，并提供针对性反馈，而非仅仅改进候选答案。此外，ExComm还引入了轨迹多样化模块，避免了通信可能带来的轨迹多样性坍缩问题。

### Q3: 论文如何解决这个问题？

ExComm通过一个协同通信协议来解决长程智能体推理中的错误传播问题。其核心架构包含两个主要模块：在线信念一致性模块和轨迹多样化模块，两者在探索阶段周期性地介入。

首先，**在线信念一致性模块**基于实证发现——并行智能体推理中67%~71.5%的错误会导致跨智能体的信念冲突。该模块在每个执行步骤后收集所有并行智能体的信念状态，提取相互排斥的事实声明作为冲突。然后，它启动一个独立于原始智能体的、基于工具（ReAct循环）的专用推理环路来裁决这些冲突，确定正确事实。裁决结果以**软更新**方式追加到相关智能体信念中，而非直接覆盖，这保留了智能体在裁决错误时自我修正的能力，并维持了轨迹多样性。

其次，**轨迹多样化模块**并行运作，统一分析所有智能体的执行计划，识别冗余或未探索的推理方向。它生成结构化的多样化指令，将过度相似或冗余的轨迹重定向到正交的策略上。该模块直接修改智能体的计划（非信念），从而在不破坏推理连贯性的前提下，显式增强探索空间的覆盖。

整体框架是一个**探索阶段通信协议**：并行智能体按基座循环执行（初始化→选择任务→执行→更新信念→重规划），每步之后，上述两模块介入，分别进行信念校对与计划多样化。其创新点在于：(1) 将错误纠正前置到探索阶段，而非事后验证；(2) 通过软更新实现了容错的信念修正；(3) 设计了全局协调的多样化机制防止轨迹坍塌，在提升准确率同时维持了良好的性能-成本平衡。

### Q4: 论文做了哪些实验？

论文在三个基准测试上进行了实验：AIME 2024、AIME 2025（数学推理）和GAIA（多层级智能体推理）。实验设置使用Gemini-2.5-Flash-Lite和Qwen3.5-4B两种模型，并行方法默认使用4个求解智能体，指标为多数投票准确率。对比基线包括：单智能体（Base Agent）、顺序修订、独立缩放、独立缩放+顺序修订、以及树搜索。主要实验结果显示，所提方法在所有基准上一致优于最强基线，平均性能提升分别为5.7%（Gemini）和5.0%（Qwen）。具体地，在Gemini上AIME 2024达到72.5%，AIME 2025为60.6%，GAIA L1/L2/L3分别为52.2%/30.8%/14.8%，平均46.2%；在Qwen上分别为87.8%/75.8%/69.5%/49.8%/28.7%，平均62.3%。错误恢复实验表明，该方法在错误恢复率上显著领先，Gemini上平均恢复率达38.7%，Qwen上为61.8%。缩放实验显示，扩展模型至Qwen3-235B或将智能体增至8个时，该方法仍保持最优性能。通信基线比较验证了其在准确性和轨迹多样性（以Self-BLEU衡量）上的优势，且具有最佳性能-成本权衡。

### Q5: 有什么可以进一步探索的点？

ExComm在错误检测和修复上依赖跨智能体的显式事实冲突，这隐含假设错误一定能通过对比暴露，但实际中可能所有智能体在相同采样下犯同类隐性错误，导致冲突不出现。未来可从两个方向改进：一是引入外部知识库或预训练模型进行独立验证，打破依赖内部冲突的局限；二是利用强化学习优化通信时机的选择，避免固定时间间隔审计带来的冗余或延迟，使资源分配更自适应。此外，当前软更新以防覆盖，但也可能积累冗余反馈干扰推理，需要设计更智能的遗忘机制或置信度过滤策略。最后，将ExComm扩展到多模态协作场景以处理更复杂的错误类型值得探索。

### Q6: 总结一下论文的主要内容

ExComm论文提出了一种用于智能体测试时扩展的探索阶段通信协议，旨在解决长期推理中错误传播的关键问题。该问题表现为智能体在中间步骤产生的错误会持续影响后续推理。方法核心包括两个模块：在线信念一致性模块通过检测并行推理轨迹间的跨智能体事实冲突（占错误的67-71%），利用工具验证循环解决冲突，并以软信念更新的方式将验证后的反馈附加到智能体信念中而非覆盖原有信念；轨迹多样化模块则监控策略冗余，引导智能体转向正交探索方向以避免多样性崩溃。在AIME 2024/2025和GAIA基准测试上，使用Gemini-2.5-Flash-Lite和Qwen3.5-4B模型时，ExComm相比最佳基线分别获得5.7%和5.0%的平均性能提升。实验表明该方法在错误恢复、扩展行为、多样性保持和性价比方面均优于现有方法，为智能体测试时扩展提供了有效的错误控制方案。
