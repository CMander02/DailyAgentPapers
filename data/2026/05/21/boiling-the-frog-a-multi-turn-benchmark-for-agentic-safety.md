---
title: "Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety"
authors:
  - "Piercosma Bisconti"
  - "Matteo Prandi"
  - "Federico Pierucci"
  - "Federico Sartore"
  - "Enrico Panai"
  - "Laura Caroli"
  - "Yue Zhu"
  - "Adam Leon Smith"
  - "Luca Nannini"
  - "Marcello Galisai"
  - "Susanna Cifani"
  - "Francesco Giarrusso"
  - "Marcantonio Bracale Syrnikov"
  - "Daniele Nardi"
date: "2026-05-21"
arxiv_id: "2605.22643"
arxiv_url: "https://arxiv.org/abs/2605.22643"
pdf_url: "https://arxiv.org/pdf/2605.22643v2"
categories:
  - "cs.CL"
tags:
  - "Agent安全"
  - "多轮交互"
  - "基准测试"
  - "工具使用"
  - "增量攻击"
  - "风险分类"
  - "状态检测"
relevance_score: 9.2
---

# Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety

## 原始摘要

Background. Traditional safety benchmarks for language models evaluate generated text: whether a model outputs toxic language, reproduces bias, or follows harmful instructions. When models are deployed as agents, the safety-relevant object shifts from what the system says to what it does within an environment, and evaluating model responses under prompting is no longer sufficient to address the safety challenges posed by artificial intelligence. Recent developments have seen the rise of benchmarks that evaluate large language models as agents. We contribute to this strand of research. Approach. We introduce Boiling the Frog, a benchmark that evaluates whether tool-using AI models deployed in corporate and office settings are susceptible to incremental attacks. Each scenario begins with benign workspace edits and later introduces a risk-bearing request. The benchmark focuses on stateful multi-turn evaluation: chains expose a persistent workspace, place the risk-bearing payload at controlled positions in the turn sequence, and score whether the resulting artifact state becomes unsafe. Scenarios are organized through a three-level operational risk taxonomy grounded in the Boiling the Frog risks, the AI Act Annex I and Annex III high-risk contexts, and EU AI Act's Code of Practice on General-Purpose AI (GPAI). Results. Across a nine-model panel, aggregate strict attack success rate (ASR) is 44.4%. Model-level ASR ranges from 20.5% for Claude Haiku 4.5 to 92.9% for Gemini 3.1 Flash Lite, with Seed 2.0 Lite also above 80%. Average chain category-level ASR reaches 93.3% for Code of Practice loss-of-control scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

本文试图解决现有大语言模型安全评测范式在智能体（Agent）场景下的根本性缺陷。传统安全基准（如毒性、偏见、有害指令遵循等）将模型视为文本生成器，仅评估其输出内容的安全性，即“响应风险”。然而，当模型被部署为具有工具调用能力的智能体时，其安全风险从“说什么”转变为“做什么”——模型可能通过修改环境状态造成实质性危害（如删除数据库、篡改访问控制记录等），而其文本回复可能完全无害。这种“操作风险”无法被传统响应级评测捕捉。现有智能体安全研究多关注单轮指令注入，但忽视了风险通过多轮渐进式累积的关键特征：早期看似无害的微小操作（如在文件中添加一条记录）可能在多轮交互后累积成严重不安全状态。为此，本文提出“温水煮青蛙”（Boiling the Frog）基准，核心解决以下问题：如何评估工具型AI模型在多轮渐进式交互中，是否会在持续压力下将工作区内持久化工件（如策略文件、配置文档、访问记录）修改到预设的不安全状态，从而衡量从安全文本生成到不安全环境操作的转化风险。

### Q2: 有哪些相关研究？

相关工作可归纳为三类：1）**模型安全基准**（如AILuminate、HarmBench、StrongREJECT、JailbreakBench、CyberSecEval等），主要评估单轮文本输出的毒性、偏见、有害指令遵循等，环境是静态的，不涉及工具或状态持久化。2）**多轮交互/社会决策基准**（如MT-Bench、PersuasionBench、MACHIAVELLI、SOTOPIA），虽涉及多轮对话或社会交互，但通常在模拟或文本环境，不聚焦工具执行与状态变化。3）**智能体安全基准**（如AgentHarm、Agent-SafetyBench、MT-AgentRisk、ToolShield、Cybench等），评估智能体在工具和状态环境中的安全行为，但多数关注单步工具调用或直接有害指令。本文与它们的核心区别是：聚焦**增量式攻击**——初始动作合法，风险请求在后续轮次注入，且环境是持久化的工作空间（文件系统），最终评估的是**工件状态的不安全性**而非文本或轨迹。此外，本文首次将**AI法案（EU AI Act）的监管分类**转化为具体测试场景，这是其他基准未涉及的。

### Q3: 论文如何解决这个问题？

Boiling the Frog通过构建一个多轮、状态持久化的基准测试框架来评估AI代理的安全性。其核心方法是“代理微观物理学”，将风险暴露分解为五个阶段的循环：观察（模型接收用户指令和历史）、暴露（提供list_dir/read_file/write_file三种基本工具）、行动（代理调用工具修改文件）、转换（环境状态变化并记录差异）、持久化（新状态进入下一轮）。这样设计的关键在于，每轮看似无害的编辑在累积后可能导致不安全的最终状态，形成“温水煮青蛙”的渐进式风险机制。

整体架构包括157个独立链（chain），每个链包含工作区蓝图、用户指令序列（4-20轮）、可编辑的工件（如策略文件、配置文档）以及不安全工件谓词。主要创新点在于：一是将评估从文本输出转向工作区文件状态的持久化改变；二是设计了三层风险分类法（Code of Practice的系统性风险、AI Act的高风险场景、BF代理风险模式）；三是采用混合验证模式，通过确定性谓词和LLM裁判共同判定是否达到不安全状态。这种设计使得攻击成功率成为多轮交互中状态改变的直接度量。

### Q4: 论文做了哪些实验？

该论文提出的"Boiling the Frog"基准测试评估了9个AI模型在复杂多轮交互中的安全性。实验设置：每个场景中，模拟企业用户与拥有办公工作区工具访问权限的AI代理进行4-20轮交互，初始为无害编辑任务，随后引入风险指令。基准测试包含157个测试链，每个链指定工作区蓝图、用户交互序列、工件文件和风险判定谓词。关键指标：总体严格攻击成功率(ASR)为44.4%，各模型表现差异显著，Claude Haiku 4.5最低(20.5%)，Gemini 3.1 Flash Lite最高(92.9%)，Seed 2.0 Lite也超过80%。平均链类别级ASR在代码实践失控场景中达到93.3%。实验通过评估代理修改持久化文件（如训练记录、监控规则、部署配置等）是否达到预定义的不安全状态来判断安全性，而非仅评估模型文本输出。

### Q5: 有什么可以进一步探索的点？

该工作提出的基准测试聚焦于多轮渐进式攻击，但其评估仅基于最终产出状态的安全性，忽略了攻击过程中模型行为模式的动态变化。未来可探索引入过程级监控指标，例如追踪模型在每轮交互中对可疑操作的拒绝频率、对用户意图的质疑能力，或记录权限使用异常的轨迹。另一重要方向是研究防御机制与攻击递进性的交互影响：当模型具备隔离敏感操作的沙箱环境或基于规则的审计模块时，其安全脆弱性曲线可能呈非线性衰减。此外，当前攻击场景主要针对办公软件与代码环境，可扩展至机器人控制、金融交易等更具物理或经济影响的领域，并考虑多模态输入（如图像编辑请求）与跨会话状态残留的威胁。改进思路包括开发对抗性训练数据生成框架，自动合成渐进式攻击链，以及设计具有因果推理能力的代理——当检测到系列操作间的潜在风险传导路径时主动中止任务执行。

### Q6: 总结一下论文的主要内容

论文介绍了一个名为“Boiling the Frog”的多轮基准测试，用于评估作为代理部署的大语言模型在渐进式攻击下的安全性。传统安全基准仅评估模型生成的文本（如毒性、偏见），但代理系统会通过工具调用改变环境状态，带来新的操作风险。该基准将威胁建模为一个工具使用的AI代理在持久化办公空间中的多轮交互：早期是良性文件编辑，后续引入风险请求。评估标准是代理是否将工件变为预设的不安全状态，而非其文本回答。基准包含157条链，覆盖157个场景。在九模型评估中，整体严格攻击成功率（ASR）为44.4%，模型级ASR从20.5%到92.9%不等。结果表明，当前模型在操作安全方面存在显著脆弱性，尤其是面对渐进式、多轮的社会工程攻击时，安全差距巨大。该工作强调了从模型安全到代理安全的范式转变，并为AI法案等监管提供了可操作的安全评估工具。
