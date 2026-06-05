---
title: "When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents"
authors:
  - "Dongsheng Zhu"
  - "Xuchen Ma"
  - "Yucheng Shen"
  - "Xiang Li"
  - "Yukun Zhao"
  - "Shuaiqiang Wang"
  - "Lingyong Yan"
  - "Dawei Yin"
date: "2026-06-04"
arxiv_id: "2606.05806"
arxiv_url: "https://arxiv.org/abs/2606.05806"
pdf_url: "https://arxiv.org/pdf/2606.05806v1"
github_url: "https://github.com/Zhudongsheng75/ToolMaze"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "工具使用"
  - "鲁棒性"
  - "评测基准"
  - "动态重规划"
  - "错误恢复"
relevance_score: 8.5
---

# When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents

## 原始摘要

Existing benchmarks evaluate Tool-Integrated Reasoning (TIR) in LLMs on idealized ''happy paths'', largely overlooking real-world tool failures. We introduce ToolMaze, a benchmark for dynamic path discovery and error recovery in TIR agents. To separate systematic replanning from blind trial-and-error, ToolMaze adopts a two-dimensional design: DAG-based topological complexity and a $2 \times 2$ taxonomy of tool perturbations (explicit/implicit, transient/permanent). Evaluations show that perturbations degrade performance across nearly all models, with the sharpest drops under implicit semantic failures. Driven by systemic over-trust in corrupted outputs, Perturbation Recovery Rate (PRR) plummets by around 37\% in these scenarios, while complex topologies trap agents in futile trial-and-error loops. Crucially, agentic fault-tolerance improves with model scale $3.66\times$ slower than basic task execution, highlighting dynamic replanning as a distinct bottleneck unaddressed by model scaling or prompting. Data and code are available at https://github.com/Zhudongsheng75/ToolMaze.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

现有工具集成推理基准测试大多在理想化“快乐路径”下评估LLM智能体，严重忽略了真实世界中工具执行的故障频发特性。实际环境中的工具调用并非线性流程，而是复杂、易失效的依赖图，智能体既可能遭遇网络错误等显式故障，更会面对结构正确但语义被破坏的隐式故障（如库存负值），这些故障若不被自主检测，将引发级联逻辑错误。当前研究通过故障注入等方式尝试评估智能体鲁棒性，但存在两大不足：一是未充分刻画解空间，难以区分系统重规划与盲目工具替换；二是扰动随机注入导致无法公平衡量搜索效率。

为此，本文提出ToolMaze基准，核心创新在于将鲁棒性评估形式化为两维网格——拓扑复杂度（基于DAG的四种递增层级）与扰动模式（显式/隐式×瞬时/永久构成的2×2分类），并在预定义工具节点注入扰动以支持受控评估。通过枚举所有有效恢复路径提供完整真值集，并引入扰动恢复率（PRR）与恢复成本（RC）等新指标，精准测量智能体真实重规划能力。最终要解决的核心问题是：当遭遇不同类型的工具执行故障时，LLM智能体如何实现动态路径发现与系统重规划？其故障耐受能力与模型规模扩展、基础任务执行之间存在怎样的差距？

### Q2: 有哪些相关研究？

在相关研究方面，本文工作可归为以下几类：

**方法类**：早期研究建立了LLM的基础工具使用能力，近期范式则聚焦于有状态、开放式的环境。规划中心型智能体构建全局DAG来处理多工具依赖关系。其他方法通过架构性安全措施或面向恢复的训练来提升韧性。

**鲁棒性/恢复评测类**：这是本文最直接的相关工作。现有基准如τ-bench引入pass^k区分稳定成功与偶然成功；AgentNoiseBench注入用户噪声和工具噪声；ReliabilityBench采用混沌工程风格的故障注入；AgentProp-Bench测量由参数级注入引起的传播级联；ToolGym研究中间故障的恢复，展示早期错误如何在下游工具交互中级联。此外，Multi-Mission Tool Bench研究相关动态任务，STT-Arena评估时空干扰下的重规划。

**与本文的区别**：现有工作集中于浅层链条、狭窄攻击面或非结构化故障，缺乏对隐式语义故障和DAG结构化恢复的深入探讨。本文提出了二维设计（DAG拓扑复杂度×2×2扰动分类学），系统隔离了盲目试错与系统性重规划，并发现智能体容错能力随模型规模增长的速度比基本任务执行慢3.66倍，突出动态重规划是模型扩展或提示工程尚未解决的独特瓶颈。

### Q3: 论文如何解决这个问题？

该论文通过构建一个名为ToolMaze的双维度评测框架，系统性地评估LLM智能体在面对工具故障时的动态重规划和异常恢复能力。核心方法围绕任务拓扑复杂度（C轴）和工具扰动模式（P轴）的交乘矩阵展开。在架构设计上，框架包含三个主要模块：任务构建模块采用工具优先范式，通过DAG架构师基于270个真实世界工具（分为源、处理器、动作三类）和六领域标记（金融、旅行等）组装有向无环图，并枚举所有有效路径作为完整解空间；扰动引擎模块动态注入确定性故障，支持2x2分类（显式/隐式、瞬时/永久）的四种扰动模式，并通过故障激活规则确保多路径任务中扰动发生且不重复；评估模块则从整体任务成功率、扰动恢复率、恢复代价三个互补维度量化性能。关键技术包括基于LLM的图验证与语义连贯性检查、解空间枚举以确立最短恢复路径作为基准、以及反向量化验证确保任务自然语言化后语义不失真。主要创新在于分离系统性重规划与盲目试错，揭示模型对隐式语义故障的过度信任导致恢复率下降37%，且复杂拓扑易使智能体陷入无效试错循环，同时发现智能体容错能力随模型规模提升速度比基本任务执行慢3.66倍，证明动态重规划是独立于规模与提示工程的关键瓶颈。

### Q4: 论文做了哪些实验？

论文构建了ToolMaze基准，包含270个工具和400个基础任务（按复杂度C1-C4各100个），通过四种扰动模式（明确/隐式、瞬时/永久）扩展为2000个实例。实验评估了GLM-5.1、Deepseek-V4-Pro、MiniMax-M2.7、Qwen3.5系列、GPT-5.5、Gemini-3.1-Pro-Preview、Claude-Sonnet-4-6等模型，在沙盒环境中最多执行25步，温度设为1。主要结果包括：从无扰动（NP）到扰动模式（P1-P4），所有模型性能显著下降，如Claude-Sonnet-4-6的TSR从77.00%大幅降低；隐式语义失败下扰动恢复率（PRR）平均下降37.15%；Gemini-3.1-Pro-Preview综合表现最佳。任务复杂度方面，C2时恢复力最强（TSR和PRR最高，RC最低），C3-C4复杂度增加导致性能恶化。值得注意的是，模型规模每增加一个数量级，基础任务完成率（TSR）提升17.85个百分点，而故障容错（PRR）仅提升4.88个百分点，差距约3.66倍，表明动态重新规划是模型缩放无法解决的核心瓶颈。

### Q5: 有什么可以进一步探索的点？

论文在DAG拓扑上建立基准，虽然便于精确度量恢复路径，但牺牲了真实环境的开放性和模糊性。未来可以将任务生成范式扩展到非结构化领域，例如Web导航或多轮对话，其中成功标准不再是明确路径，需设计更柔性的评估指标。当前故障分类（显式/隐式、短暂/永久）是基础框架，但现实系统面临级联故障和对抗注入等复杂场景，可构建多跳故障图并引入“扰动传播链”概念，比如研究一个API的隐性浮点错误如何引发下游数据库写入失败。此外，论文发现模型规模对容错的增益明显弱于对基本任务的提升，这提示轻量级错误检测模块或自适应重规划策略可能比单纯扩大模型更有效。未来可探索稀疏路由或元学习机制，让代理在发现工具输出可疑时主动查询日志或回溯决策路径，而避免陷入试错循环。结合在线强化学习，让代理从历史扰动中积累重规划经验，或能突破当前瓶颈。

### Q6: 总结一下论文的主要内容

论文提出了ToolMaze基准，旨在系统性评估大语言模型代理在工具使用中的动态重规划和异常恢复能力，填补了现有基准仅关注理想“快乐路径”的空白。该基准基于有向无环图设计拓扑复杂度，并引入2×2工具扰动分类（显式/隐式、暂时/永久）。实验发现，扰动会显著降低几乎所有模型的性能，尤其在隐式语义故障下，恢复率因模型对错误输出的过度信任而下降约37%，复杂拓扑则导致代理陷入无效试错循环。关键结论是，代理的容错性随模型规模提升的速度比基本任务执行慢3.66倍，表明动态重规划是模型扩展或提示策略无法解决的独立瓶颈。这项工作挑战了当前评估范式，强调了向自主异常检测和系统二式重规划转变的必要性，对构建真正鲁棒的智能代理有重要意义。
