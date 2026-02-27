---
title: "MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios"
authors:
  - "Zhiheng Song"
  - "Jingshuai Zhang"
  - "Chuan Qin"
  - "Chao Wang"
  - "Chao Chen"
  - "Longfei Xu"
  - "Kaikui Liu"
  - "Xiangxiang Chu"
  - "Hengshu Zhu"
date: "2026-02-26"
arxiv_id: "2602.22638"
arxiv_url: "https://arxiv.org/abs/2602.22638"
pdf_url: "https://arxiv.org/pdf/2602.22638v1"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Route Planning"
  - "Tool Use"
  - "Evaluation Protocol"
  - "Real-World Scenarios"
relevance_score: 8.0
---

# MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios

## 原始摘要

Route-planning agents powered by large language models (LLMs) have emerged as a promising paradigm for supporting everyday human mobility through natural language interaction and tool-mediated decision making. However, systematic evaluation in real-world mobility settings is hindered by diverse routing demands, non-deterministic mapping services, and limited reproducibility. In this study, we introduce MobilityBench, a scalable benchmark for evaluating LLM-based route-planning agents in real-world mobility scenarios. MobilityBench is constructed from large-scale, anonymized real user queries collected from Amap and covers a broad spectrum of route-planning intents across multiple cities worldwide. To enable reproducible, end-to-end evaluation, we design a deterministic API-replay sandbox that eliminates environmental variance from live services. We further propose a multi-dimensional evaluation protocol centered on outcome validity, complemented by assessments of instruction understanding, planning, tool use, and efficiency. Using MobilityBench, we evaluate multiple LLM-based route-planning agents across diverse real-world mobility scenarios and provide an in-depth analysis of their behaviors and performance. Our findings reveal that current models perform competently on Basic information retrieval and Route Planning tasks, yet struggle considerably with Preference-Constrained Route Planning, underscoring significant room for improvement in personalized mobility applications. We publicly release the benchmark data, evaluation toolkit, and documentation at https://github.com/AMAP-ML/MobilityBench .

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的路线规划智能体在现实世界移动场景中缺乏系统性、可复现且全面评估基准的问题。研究背景是，随着LLM与工具调用能力的结合，能够通过自然语言交互和API调用来支持日常人类移动的路线规划智能体已成为一个新兴且有前景的范式。然而，现有评估方法存在显著不足：一方面，近期的相关基准（如TravelBench和TravelPlanner）主要关注高层行程生成和抽象约束推理，未能充分捕捉日常移动中路线规划的复杂性，后者需要对大规模地图环境和动态变化条件进行细粒度推理；另一方面，在真实移动场景中进行系统评估面临根本性挑战，包括难以覆盖不同难度和约束组合的多样化场景、实时地图API因交通动态等因素导致的非确定性和不可复现性、缺乏超越主观评判的全面客观评估标准，以及缺少可扩展且可复现的评估工具包。

因此，本文要解决的核心问题是：如何构建一个能够反映现实世界移动需求多样性、消除外部服务非确定性干扰、并提供多维度可靠评估的标准化基准，以系统衡量LLM路线规划智能体的真实能力。具体而言，论文提出了MobilityBench这一基准，它基于真实用户查询构建，并设计了确定性的API回放沙箱以确保评估的可复现性，同时制定了以结果有效性为核心、辅以指令理解、规划、工具使用和效率评估的多维度评估协议。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统路径规划算法、基于LLM的路径规划与代理研究，以及面向代理的评测基准。

在**传统路径规划方法**方面，早期研究基于图论，聚焦于距离、时间等物理成本的最优化，代表性算法如Dijkstra和A*。随着需求多样化，研究转向偏好感知的路径规划，例如将推荐模型（如INTSR）与路径搜索结合。然而，这些方法依赖结构化特征或预定义的偏好空间，难以处理自然语言表达的模糊、长尾需求。

在**基于LLM的路径规划与代理**方面，研究利用LLM理解复杂语义指令的能力。但LLM单独用于空间推理和约束优化并不可靠，因此出现了混合框架，将LLM与传统规划器结合，用于高层决策引导或意图约束提取。此外，工具增强的语言代理（如STAgent）通过调用地图API等外部工具进行结构化决策，成为现实移动场景中的新兴范式。现有旅行规划代理（如TravelPlanner）主要关注高层行程生成和抽象约束推理，未能紧密整合语义理解与真实路网的低层路径优化。

在**评测基准**方面，通用代理评测工作（如ToolBench、τ-bench）关注指令遵循和工具交互能力。在特定领域，尤其是城市计算和旅行规划领域，出现了如TravelPlanner（关注多日行程构建）和TravelBench（关注多轮对话偏好推理）等基准。然而，这些基准主要评估高层行程生成，未能系统评估代理在细粒度、移动场景特定约束（如偏好约束路径规划、有序途经点、交通方式依赖等）下的路径规划能力。

本文提出的MobilityBench与上述工作的区别在于：它专门针对**现实世界移动场景下的细粒度路径规划任务**构建评测基准，其数据源于真实用户查询，覆盖广泛意图，并通过确定性的API重放沙盒实现可复现的端到端评估，填补了现有研究在系统评估个性化、约束性路径规划能力方面的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为MobilityBench的、可扩展的基准测试来解决现实世界移动场景中基于大语言模型（LLM）的路径规划智能体的系统性评估难题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块：**
MobilityBench的架构围绕“情节”构建，每个情节是一个四元组 `e = (x, z, S, y)`，分别代表：匿名自然语言用户查询`x`、上下文信息`z`、可重放的确定性API响应快照`S`，以及用于自动化评估的结构化真实标注`y`。这确保了评估的自包含性和可复现性。

1.  **基准数据构建模块**：从高德地图收集的大规模匿名真实用户语音查询（转录为文本）出发，经过多阶段过滤和整理流程，确保查询在“无需澄清”的假设下是自包含且可解的。利用Qwen-4B模型进行意图分类，并通过开放式标注协议和专家裁决，最终形成了一个涵盖4大类、11种具体场景的任务分类体系，包括基础信息检索、路径依赖信息检索、基础路径规划和偏好约束路径规划。

2.  **结构化真实标注生成模块**：为每个情节构建可自动化评估的参考标准`y`。其核心是定义并执行一个“标准工具程序”，该程序由领域专家制定的标准操作流程驱动，明确了解决查询所需的最少工具调用序列。程序包含三个核心步骤：查询槽位提取与归一化、文本位置解析为结构化地理实体/坐标、调用下游工具（如路径规划、实时交通）并验证约束可行性。最终将完整的执行轨迹和关键中间产物整合为真实标注。

3.  **确定性重放沙箱模块**：为了解决实时地图服务带来的非确定性和不可复现性问题，论文设计了一个API重放沙箱。在评估时，智能体的所有工具调用都被路由至此沙箱，而非实时API。沙箱根据规范化参数（如坐标、时间）从预录制的缓存中返回在构建真实标注时捕获的响应。对于缓存未命中情况，采用模糊匹配或空间最近邻匹配等回退策略。所有调用都经过严格的模式验证，确保了评估环境的一致性和公平性。

4.  **多维评估协议模块**：为了超越粗糙的端到端成功率，论文提出了一个细粒度的多维评估协议，将智能体行为分解为四个核心能力进行评估：
    *   **指令理解**：通过意图检测和信息提取两个指标，评估智能体理解用户意图和提取约束的能力。
    *   **规划**：通过任务分解等指标，评估智能体将高层目标分解为连贯原子动作序列的能力。
    *   **工具使用**：评估智能体正确、合规调用工具的能力。
    *   **决策制定**：以结果有效性为核心，评估智能体最终提供的答案或路径的准确性。

**创新点：**
*   **真实性与可扩展性**：基于大规模真实用户查询构建，覆盖全球广泛地理区域和多样化的移动意图，确保了基准的现实意义和广度。
*   **可复现的评估环境**：创新的确定性重放沙箱设计，彻底消除了实时服务波动对评估的影响，为公平、可重复的智能体比较奠定了基础。
*   **结构化与可解释的真实标注**：不仅提供最终答案，还定义了解决每个问题所需的最小工具交互序列和中间证据，为自动化评估和深度诊断分析提供了稳定、可解释的参考。
*   **细粒度的诊断性评估**：提出的多维评估协议能够深入剖析智能体在推理链各环节（理解、规划、工具使用、决策）的表现，精准定位性能瓶颈，超越了黑盒式的端到端评估。

### Q4: 论文做了哪些实验？

论文实验围绕MobilityBench基准展开，旨在评估基于大语言模型的路径规划智能体在真实世界移动场景下的性能。

**实验设置与数据集**：实验使用了从高德地图收集的大规模匿名真实用户查询构建的MobilityBench基准数据集，包含10万个场景片段。为确保统计显著性和计算效率，研究采用分层随机抽样，最终得到一个包含7,098个片段的评估集，覆盖全球多个城市和多样化的路径规划意图。评估在一个确定性的API重放沙盒中进行，以消除实时服务带来的环境差异，确保可复现的端到端评估。

**对比方法与评估协议**：研究评估了多种具有代表性的开源和闭源大语言模型作为智能体骨干，包括Qwen系列、DeepSeek系列、OpenAI GPT系列、Anthropic Claude系列和Google Gemini系列。基于这些骨干模型，构建了两种主流的智能体框架进行对比：ReAct（反应式）和Plan-and-Execute（规划与执行）。评估采用了一个多维度的评估协议，核心是结果有效性（Outcome Validity），并辅以对指令理解、规划、工具使用和效率的评估。

**主要结果与关键指标**：实验结果显示，在Plan-and-Execute框架下，Claude-Opus-4.5表现最佳，其交付率（Delivery Rate）达到83.53%，最终通过率（Final Pass Rate）为65.77%。总体而言，当前模型在基础信息检索和路径规划任务上表现良好，但在偏好约束的路径规划任务上存在显著困难。关键性能指标包括指令理解（如意图检测ID、信息提取IE）、规划（如任务分解精度DEC-P和召回率DEC-R）、工具使用（如工具选择精度TS-P和召回率TS-R、模式合规性SC）、决策制定（交付率DR、最终通过率FPR）以及效率（输入令牌IT、输出令牌OT）。例如，在ReAct框架下，最佳模型的交付率为85.95%，最终通过率为69.09%。这些发现揭示了现有模型在个性化移动应用方面仍有巨大改进空间。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估场景虽基于真实用户查询，但通过确定性API回放沙箱模拟，可能无法完全捕捉实时地图服务（如交通流量、临时封路）的动态性和不确定性，这限制了在完全开放环境下的泛化能力验证。未来研究可探索在动态环境中测试智能体，引入实时数据流以评估其应对突发变化的能力。此外，当前评估侧重于个性化偏好约束下的路径规划，但未深入涉及多模态交互（如结合视觉或语音输入）或长期学习（如从用户反馈中持续优化）。改进思路可包括：开发自适应工具调用机制，使智能体能动态选择API以平衡效率与准确性；结合强化学习让智能体在模拟环境中通过试错学习复杂约束下的决策；以及扩展基准以涵盖跨城市、多目标路径规划等更复杂场景，推动智能体向实用化个人移动助手演进。

### Q6: 总结一下论文的主要内容

该论文提出了MobilityBench，一个用于评估基于大语言模型（LLM）的路线规划智能体在真实世界移动场景中性能的基准测试。其核心问题是现有评估方法因真实场景中用户需求多样、地图服务非确定性以及可复现性差而受到阻碍。

论文的主要贡献是构建了一个可扩展的基准。方法上，它基于从Amap收集的大规模匿名真实用户查询构建数据集，覆盖全球多城市的广泛路线规划意图。为确保可复现的端到端评估，论文设计了一个确定性的API回放沙箱，消除了实时服务带来的环境差异。此外，论文提出了一个以结果有效性为核心、辅以指令理解、规划、工具使用和效率评估的多维评估协议。

主要结论是，通过对多个LLM智能体的评估发现，当前模型在基本信息检索和路线规划任务上表现尚可，但在偏好约束路线规划方面存在显著困难，这表明在个性化移动应用方面仍有巨大改进空间。该基准的发布旨在推动该领域更系统、可复现的研究。
