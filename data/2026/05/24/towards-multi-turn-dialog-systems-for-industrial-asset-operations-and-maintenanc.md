---
title: "Towards Multi-Turn Dialog Systems for Industrial Asset Operations and Maintenance"
authors:
  - "Chengrui Li"
  - "Rujing Li"
  - "Yitong Bai"
  - "Rui Li"
date: "2026-05-24"
arxiv_id: "2605.24953"
arxiv_url: "https://arxiv.org/abs/2605.24953"
pdf_url: "https://arxiv.org/pdf/2605.24953v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Tool Use"
  - "Industrial Agent"
  - "Multi-Turn Dialog"
  - "System Profiling"
relevance_score: 8.0
---

# Towards Multi-Turn Dialog Systems for Industrial Asset Operations and Maintenance

## 原始摘要

Industrial asset operations and maintenance question answering is inherently multi-turn, iterative, and highly dependent on external tool invocation. However, the conventional plan-execute single-agent architecture exhibits clear limitations in maintaining cross-turn context, and reusing intermediate results. In this paper, we present a multi-turn dialog system designed for industrial scenarios based on a supervisor-specialist multi-agent architecture. To alleviate tool invocation bottlenecks, the system incorporates structured artifact reuse, dynamic replanning, and parallel tool execution. Evaluation results show that our system achieves better response quality compared with the baseline, with planning effectiveness increasing by 54.5% and task completion improving by 37.8%. System profiling further shows that cross-turn artifact reuse effectively reduces redundant tool invocation, decreasing the tool-time share from 47.3% to 26.3% and making turns 2-5 approximately 4.2x faster than the first turn.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决工业资产运营与维护（O&M）场景中多轮对话系统的关键挑战。研究背景是，在工业4.0驱动下，工业O&M任务需要整合多种数据源（如数据库、设备知识、操作上下文等）进行推理，且用户提问通常是迭代式的，需要系统具备多轮对话能力。现有方法存在明显不足：传统的单智能体“规划-执行”架构是为单次任务设计的，缺乏跨轮次记忆和中间结果复用机制。具体而言，该基线系统有三个主要局限：一是在需要协调时序数据、工单、警报等多步骤诊断任务时，规划能力不足；二是可靠性差，容易因工具参数幻觉或执行失败而无法恢复；三是中间结果无法有效复用，导致在多轮对话中重复调用工具，造成高延迟和高成本。因此，本文的核心问题是：开发一个稳健、高效、可靠的多轮对话系统，以提升工业O&M的诊断质量并减少不必要的工具调用。系统采用“监督者-专家”多智能体架构，通过引入结构化工件复用、动态重规划和并行工具执行等优化技术，来克服工具调用瓶颈，实现跨轮次上下文保持与结果复用。

### Q2: 有哪些相关研究？

根据提供的论文内容，相关研究可分为以下几类：

**方法类**：ReAct范式（交推理与行动）和ReActXen将其应用于工业SCADA/IoT数据访问，提出IoTBench；AssetOpsBench提供工业资产运维基准，强调持久记忆的重要性。这些工作为工具调用和感知控制奠定基础，但未解决工具调用密集场景的延迟问题。本文在此基础上，通过结构化工件复用和并行执行改进了效率。

**记忆与检索类**：检索增强生成（RAG）结合参数化先验与非参数化外部记忆；MemGPT在跨记忆层协调虚拟上下文以支持长交互；Reflexion通过情景记忆缓冲记录反馈辅助决策。这些工作侧重记忆管理，但未针对工业工具调用主导的延迟优化，本文则专门设计了工件复用机制以减少冗余工具调用。

**多智能体架构类**：通用LLM多智能体框架探索多种协调模式；企业级工作研究了监督-专家层级，由监督者规划、委派和聚合专家输出。本文借鉴此层级结构，将其应用于端到端工业运维场景，并通过动态重规划和并行执行克服单智能体架构的上下文保持和中间结果复用局限。

**评测类**：IoTBench和AssetOpsBench分别提供工业传感器查询和资产运维基准，本文仅在系统层面评测规划有效性和任务完成度，未提出新基准。

### Q3: 论文如何解决这个问题？

该论文提出的多轮对话系统基于监督者-专家（Supervisor-Specialist）多智能体架构，专门针对工业资产运维场景中多轮迭代、强工具依赖的特点进行设计。整体框架分为三层：用户交互层负责接收问题、维护对话状态及可复用工件；智能体编排层包含一个监督智能体和多个专家智能体；工具与数据资源层通过MCP服务器接入IoT传感器检索、时序预测、异常检测等外部能力。核心方法上，系统通过三个关键技术突破基线架构的瓶颈：一是跨轮工件复用，专家智能体每次执行后生成结构化工件（包含资产标识、时间范围、工具调用、中间结果等），监督智能体在新轮次中优先检查已有工件，仅补充缺失信息，避免重复调用；二是动态规划与专家路由，监督智能体在每轮和每个专家结果返回后重新评估工作流，根据当前用户意图、已有工件和缺失证据动态分配任务，替代基线的线性计划执行；三是并行工具执行，当专家需要多个独立数据源时，可并发执行MCP调用并整合为单一工件。通过这些技术，系统实现了规划有效性提升54.5%、任务完成率提升37.8%，并将工具时间占比从47.3%降至26.3%，后续轮次执行速度比首轮快约4.2倍。

### Q4: 论文做了哪些实验？

论文在工业资产运维场景下，将所提出的监督-专家（supervisor-specialist）多智能体架构与传统的计划-执行（plan-execute）单智能体基线进行了对比实验。实验设置评估了16个多轮对话，涵盖全流程、系统配置、维护规划、操作监控等多个任务类别。主要对比方法包括计划-执行基线、顺序的监督-专家架构以及并行的监督-专家变体。实验采用主客观指标，包括规划有效性、工具使用质量、任务完成度、工具名称有效性、Schema符合性、执行成功率和恢复成功率。关键结果显示，监督-专家架构在所有指标上均优于基线：规划有效性提升54.5%（从0.538到0.831），任务完成度提升37.8%（从0.617到0.850），工具名称有效性和Schema符合性接近完美（1.000和0.997）。系统性能分析表明，跨轮工件复用减少了冗余工具调用，将工具时间占比从基线的47.3%降至约26.3%，并使第2-5轮的平均响应速度比第一轮快约4.2倍。虽然监督-专家架构的令牌消耗更高（3.32M vs 2.55M），但其总墙钟时间更短（65.2分钟 vs 83.9分钟），体现了更高的执行效率。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三方面：1）评估基于16个基准对话和有限的冷机资产，样本量小且场景单一，未能覆盖真实工业运维中的多样化故障模式、设备类型和用户行为；2）依赖预先定义的MCP工具接口和清洗后的数据，与实际生产环境中数据噪声大、工具接口不规范的情况存在差距；3）并行工具执行虽然降低了工具调用延迟，却增加了提示词大小和token消耗，将瓶颈转移到LLM生成延迟，导致并行架构未能稳定优于标准架构。

未来研究可从系统效率和评估覆盖两个方向深入。在系统层面，应将并行化从低层工具调用提升至专家级别并行执行，并结合证据摘要、剪枝和选择性工件检索来缓解提示词膨胀。在评估层面，需构建更大规模、更真实的工业数据集，引入更长对话轮次，并设计专用记忆指标如工件复用率、记忆召回准确率、冗余工具调用减少率和跨轮一致性等。这些改进将帮助验证系统能否从受控基准泛化到实际工业运维工作流。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种用于工业资产运维的多轮对话系统。当前工业场景中的问答具有多轮、迭代和高度依赖外部工具调用的特点，而传统的单智能体规划-执行架构在跨轮上下文保持和中间结果复用上存在明显局限。为此，论文设计了一种基于监督者-专家多智能体架构的系统。该方法通过将诊断工作流分解为多个专家智能体，并将其输出存储为可复用的工件，从而支持记忆感知的重新规划和更可靠的工具调用。此外，系统还集成了结构化工件复用、动态重规划和并行工具执行以缓解工具调用瓶颈。实验结果表明，与基线相比，该系统的规划有效性提升了54.5%，任务完成度提升了37.8%。进一步的分析显示，跨轮工件复用有效减少了冗余工具调用，将工具时间占比从47.3%降至26.3%，并使后续轮次（第2-5轮）的响应速度比首轮快约4.2倍。该工作证明了多智能体分解和结构化工件复用在构建面向工业运维的、以工具为中心的对话系统中的有效性。
