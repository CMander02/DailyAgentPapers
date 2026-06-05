---
title: "Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows"
authors:
  - "Yuhang Fu"
  - "Ruishan Fang"
  - "Jiaqi Shao"
  - "Huiyu Zheng"
  - "Zhengtao Zhu"
  - "Bing Luo"
  - "Tao Lin"
date: "2026-06-04"
arxiv_id: "2606.05670"
arxiv_url: "https://arxiv.org/abs/2606.05670"
pdf_url: "https://arxiv.org/pdf/2606.05670v1"
github_url: "https://github.com/LINs-lab/MASArena"
categories:
  - "cs.AI"
tags:
  - "LLM Agent Workflows"
  - "Multi-Agent Systems"
  - "Evaluation Framework"
  - "Benchmarking"
  - "Controlled Experiments"
relevance_score: 9.0
---

# Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows

## 原始摘要

Does adding more agents help an LLM workflow once compared systems share the same benchmark loader, tool access, answer contract, usage accounting, and trajectory logging? We introduce BenchAgent, an evaluation framework that places single-agent, fixed multi-agent (MAS), and evolving MAS workflows under one normalized execution and logging protocol. BenchAgent evaluates these substrate-internal workflows across ten reasoning, coding, and tool-use benchmarks with GPT-4.1, and separately reports a Protocol-Aligned External (PAE) GAIA study of a runtime-generated workflow. Under SI conditions, at most one of six tested MAS exceeds the matched single-agent anchor on benchmark-balanced average accuracy: EvoAgent lies within the Wilson one-run guidance, while the remaining five trail by 2.56-11.29 points and occupy more expensive accuracy-cost trade-offs. On the PAE GAIA snapshot, a Claude-Code-style runtime workflow reaches 66.72% overall and 69.23% on Level 3, more than 20 points above the strongest non-Claude baseline, Jarvis, a fixed MAS.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大语言模型（LLM）代理工作流评估中的一个核心问题：在严格规范实验条件的前提下，增加代理数量（即采用多代理系统MAS）是否真能提升任务性能。研究背景是，LLM代理研究已从单代理的“思考-行动”循环扩展到固定多代理系统、动态/演化多代理系统乃至运行时生成的工作流。现有评估方法的不足在于，不同范式的工作流对比时，输入数据、工具接口、答案格式、使用量统计和轨迹记录常不一致，导致性能差异可能源于协议优势（例如多代理系统天然多出的额外轮次）而非真正的协调增益。本文通过引入BenchAgent评估框架，将单代理、固定MAS和演化MAS置于统一的执行和日志协议下，在推理、编码和工具使用等十个基准上使用GPT-4.1进行对比。核心问题是：在消除外围差异后，仅仅改变工作流组织结构本身，是否能带来可靠且显著的边际性能提升。实验结果表明，在受控的子内部（SI）条件下，六种测试的MAS中最多只有一个（EvoAgent）微弱超过匹配的单代理基线，其余五个落后2.56-11.29分，且成本更高。因此，本文试图通过标准化评估协议，严谨地验证“更多代理是否真的有助于LLM工作流”这一根本问题。

### Q2: 有哪些相关研究？

在相关工作中，本文首先将单智能体基线视为匹配的工作流锚点，提及ReAct、Toolformer、WebGPT、SWE-agent和HuggingGPT/JARVIS等系统，指出单一控制器即可构成竞争性工作流，这与近期研究发现强单智能体基线可匹配或超越同质化多智能体系统（MAS）的结论一致。在方法类工作中，多智能体系统包括CAMEL和MetaGPT定义的角色与通信协议、AutoGen的可对话智能体框架、辩论式系统以及Li等人的采样-投票方法；动态与演化系统包括AgentVerse、EvoAgent、ADAS、AFlow、Magentic-One、MaAS和MASPO，它们在设计空间内搜索或变异工作流结构。本文与这些工作的核心区别在于：现有比较很少在统一的日志和计费协议下同时运行单智能体、固定MAS、演化MAS和运行时工作流。在评测类工作中，AgentBench、GAIA、AgentBoard、WebArena、SWE-bench、ToolBench和Silo-Bench扩展了交互式、工具使用和软件开发等场景的评估；Harbor最接近本工作，但BenchAgent聚焦于对齐执行接口、工具表面、使用计费和轨迹，而非引入新数据集或基准拆分。工程类系统如LangGraph、CrewAI和Claude Code等虽推动工作流设计的执行，但本文将其作为工程描述而非实证证据引用，并通过GAIA实验询问其准确率-成本轮廓是否与BenchAgent系统不同。

### Q3: 论文如何解决这个问题？

论文通过提出**BenchAgent**评估框架来解决“增加更多智能体是否有助于LLM工作流”的问题，核心方法是**受控且协议对齐的比较**。框架设计了统一的执行与日志协议，标准化了六个接口：基准加载、输入/输出格式、运行时控制、工具访问、用量记录和评估器调用。这使得不同工作流（单智能体、固定MAS、进化MAS）可在相同控制基板上比较，通过**工作流提升度**（workflow lift）衡量替换为MAS后准确率和成本的变化。

架构上，BenchAgent将系统视为工作流组织，定义主动智能体集、通信拓扑和工具范围随时间变化的类别：单智能体（固定单一控制器）、固定MAS（预定义角色如求解器-批评者-聚合器）、进化MAS（运行时动态选择拓扑）、运行时生成工作流（完全动态调整）。关键创新点包括：**协议对齐**确保所有对比系统共用基准加载器、工具接口、答案契约和轨迹日志；**威尔逊单次运行指导**（Wilson guidance）用于解释单次运行差距，避免将小于置信区间半宽（约17-18点）的差异视为稳定排序证据。

实验结果显示，在受控条件下，仅六分之一MAS（EvoAgent）勉强等同于单智能体基线，其余落后2.56-11.29点且成本更高；而协议对齐的外部比较中，Claude-Code式运行时工作流在GAIA上达66.72%，超过最强非Claude基线20点以上，表明**额外智能体通常无效，但运行时动态生成可能提升性能**。

### Q4: 论文做了哪些实验？

论文进行了两组受控实验。第一组为基底内部（SI）对比，在MATH、AIME、GSM8K、DROP、BBH、MMLU-Pro、HumanEval、MBPP、HotpotQA和IFEval这10个基准上，将单智能体锚点（BenchAgent Core）与五个固定MAS（Jarvis、LLM-Debate、AutoGen、CAMEL、ChatEval）和一个演化MAS（EvoAgent）进行比较，使用GPT-4.1模型，所有系统共享相同的加载器、工具集（推理基准仅Python解释器，HotpotQA用完整工具集）、评估器和日志协议。结果显示，仅EvoAgent的平均准确率（75.56%）略高于单智能体（74.12%），但增益（+1.44点）小于Wilson单次运行置信区间；其余5个MAS落后2.56-11.29点，且占用更昂贵的精度-成本权衡。第二组为PAE对齐的外部实验，在GAIA验证集（L1：53题，L2：86题，L3：26题）上评估了一个Claude-Code风格的运行时生成工作流（CC-workflow）。CC-workflow达到66.72%的整体准确率，L3为69.23%，领先最强非Claude基线Jarvis（46.66%）超过20点，且使用的令牌数和时间更少。研究表明，在受控条件下，多数MAS并未带来稳定的正向工作流提升，其效果取决于任务与协议的匹配，而非简单的智能体数量。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其控制变量实验主要基于GPT-4.1，未探索不同基座模型（如Claude、开源模型）对多智能体效益的影响。未来可研究方向包括：1）在PAE GAIA中分析Claude-Code运行时工作流的高性能来源，是否源于代码生成能力还是动态解构机制；2）设计自适应智能体数量调整机制，使系统能在简单任务中自动缩减规模以节约成本；3）探索多智能体在需要多模态融合或长期依赖推理任务中的表现，当前基准偏重单轮推理；4）改进EvoAgent等架构的通信协议，避免信息冗余或角色冲突造成的性能倒挂。结合见解，可引入基于任务复杂度的动态开销预算分配，在保持性能同时优化成本效率。

### Q6: 总结一下论文的主要内容

本文提出了BenchAgent，一个标准化的工作流评估框架，旨在解决多智能体系统评估中因协议差异导致比较不公平的问题。该框架统一了基准加载、工具访问、答案契约、使用计量和轨迹日志记录，使单智能体、固定多智能体系统和动态多智能体系统可在相同条件下比较。使用GPT-4.1作为后端，在10个推理、编码和工具使用基准上评估发现：在受控条件下，6个测试的多智能体系统中最多只有一个超过匹配的单智能体基线（EvoAgent仅高出1.44分），其余5个落后2.56-11.29分，且在准确率-成本权衡中表现更差。在跨协议GAIA对比中，Claude-Code风格的工作流达到66.72%的整体准确率，比最强非Claude基线Jarvis高出20个百分点以上。核心贡献在于揭示了仅仅增加智能体数量或显式协调机制并不必然带来性能提升，反而可能导致更高成本，强调了规范化评估协议的重要性。
