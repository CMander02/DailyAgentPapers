---
title: "Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps"
authors:
  - "Alankrit Chona"
  - "Igor Kozlov"
  - "Ambuj Kumar"
date: "2026-04-21"
arxiv_id: "2604.19533"
arxiv_url: "https://arxiv.org/abs/2604.19533"
pdf_url: "https://arxiv.org/pdf/2604.19533v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent评测基准"
  - "网络安全"
  - "威胁狩猎"
  - "工具使用"
  - "SQL查询"
  - "多阶段任务"
relevance_score: 8.5
---

# Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps

## 原始摘要

We introduce the Cyber Defense Benchmark, a benchmark for measuring how well large language model (LLM) agents perform the core SOC analyst task of threat hunting: given a database of raw Windows event logs with no guided questions or hints, identify the exact timestamps of malicious events.
  The benchmark wraps 106 real attack procedures from the OTRF Security-Datasets corpus - spanning 86 MITRE ATT&CK sub-techniques across 12 tactics - into a Gymnasium reinforcement-learning environment. Each episode presents the agent with an in-memory SQLite database of 75,000-135,000 log records produced by a deterministic campaign simulator that time-shifts and entity-obfuscates the raw recordings.
  The agent must iteratively submit SQL queries to discover malicious event timestamps and explicitly flag them, scored CTF-style against Sigma-rule-derived ground truth.
  Evaluating five frontier models - Claude Opus 4.6, GPT-5, Gemini 3.1 Pro, Kimi K2.5, and Gemini 3 Flash - on 26 campaigns covering 105 of 106 procedures, we find that all models fail dramatically: the best model (Claude Opus 4.6) submits correct flags for only 3.8% of malicious events on average, and no run across any model ever finds all flags.
  We define a passing score as >= 50% recall on every ATT&CK tactic - the minimum bar for unsupervised SOC deployment. No model passes: the leader clears this bar on 5 of 13 tactics and the remaining four on zero.
  These results suggest that current LLMs are poorly suited for open-ended, evidence-driven threat hunting despite strong performance on curated Q&A security benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个关键问题：如何准确评估大型语言模型（LLM）作为智能体（Agent）在真实网络安全运营（SecOps）场景中的核心能力——威胁狩猎。当前，虽然LLM在基于问答的安全知识测试上表现良好，但其在开放式、证据驱动的威胁狩猎任务中的能力尚未得到严格评估。现有的安全基准测试要么是知识性的（测试事实回忆），要么是引导式的（提供预定义的问题），都无法模拟真实威胁狩猎中分析师需要自主生成假设、迭代查询海量原始日志数据并最终精确定位恶意活动的核心挑战。因此，本文提出了“网络防御基准测试”，旨在填补这一空白，为衡量LLM智能体在防御性、主动性网络威胁调查中的实际表现提供一个严格、可复现的评估框架。

### Q2: 有哪些相关研究？

相关研究主要分为四类。第一类是LLM安全知识基准，如SecBench、CyberMetric和CTI-Bench，它们评估LLM对网络安全事实和程序性知识的掌握，但未测试其在操作环境中的证据收集技能。第二类是日志分析与威胁检测研究，例如微软安全副驾驶评估，它使用合成日志和预定义的攻击场景进行结构化问答，移除了关键的假设形成步骤。第三类是攻击性智能体评估，如InterCode-CTF、NYU CTF Bench和PentestBench，它们评估LLM在渗透测试和夺旗挑战中的进攻能力。第四类是数据集，本文基于OTRF Security-Datasets（Mordor）这一包含真实攻击过程记录的Windows事件日志公共语料库。本文的工作与前三类都不同：它专注于防御性威胁狩猎，要求智能体在无引导、无攻击场景提示的情况下，主动从海量原始日志中发现证据，这是首个针对此任务的基准测试。

### Q3: 论文如何解决这个问题？

论文通过设计并实现一个名为“网络防御基准测试”的综合性评估环境来解决该问题。核心方法包括：1. **任务定义**：将威胁狩猎建模为一个部分可观察的序列决策问题。智能体被赋予一个包含7.5万至13.5万条原始Windows事件日志的内存SQLite数据库和一个简短的威胁情报简报，必须通过迭代提交SQL查询来探索数据，并最终提交其认为是恶意的精确时间戳。每个回合最多返回10行查询结果，总查询预算为50次。2. **环境构建**：基于Gymnasium强化学习库构建了`HolodeckHuntEnv`环境。行动空间是自由格式的SQL字符串，观察空间包含简报、最近查询及其结果。环境设计极简，仅提供SQL作为信息获取机制，模拟真实SIEM查询编写。3. **数据集与活动模拟**：基于OTRF Security-Datasets的106个真实攻击过程记录，涵盖86个MITRE ATT&CK子技术和12种战术。通过一个确定性活动模拟器，将多个过程组合成多阶段杀伤链（短、中、长模板），并进行时间偏移、实体混淆（替换IP、主机名等）和GUID重新匿名化，以防止模型通过记忆特定字符串来作弊。4. **真值标注**：使用Sigma规则检测和LLM因果关系增强的组合管道来生成恶意事件时间戳的真值标签。5. **智能体接口**：定义了一个结构化的`HunterAction`，要求智能体输出推理过程、选择工具（运行SQL、提交标志、放弃），并通过JSON模式约束解码来强制执行。

### Q4: 论文做了哪些实验？

论文对五个前沿LLM模型进行了大规模评估：Claude Opus 4.6、GPT-5、Gemini 3.1 Pro、Kimi K2.5和Gemini 3 Flash。实验设置如下：使用26个活动种子（覆盖了106个过程中的105个），每个模型在每个活动上运行一次推演（共98次运行）。每个智能体使用相同的系统提示，包含任务说明、505列的完整数据库模式和操作指南，不提供任何攻击提示。主要评估指标包括：正确提交的恶意事件时间戳数量（`n_flags_in_submitted`，主要指标）、出现在任何查询结果中的真值标志数量（`n_flags_in_query`，观察上限）、召回率、API成本和消耗的令牌数。实验结果表明所有模型都表现惨淡：最佳模型Claude Opus 4.6平均仅提交了3.8%的恶意事件标志，且没有任何一次运行能找到所有标志。所有运行都以“放弃”或“查询预算耗尽”告终，从未触发“成功完成”结局。论文定义了一个及格线：在每个涉及的MITRE ATT&CK战术上达到≥50%的召回率（这是无监督SOC部署的最低门槛）。没有模型通过：领先模型在13个战术中的5个上达标，其余四个模型在0个战术上达标。模型在“初始访问”、“凭据访问”等战术上表现尤其差。成本效益分析显示，Claude Opus 4.6性能最好但成本最高（平均每次运行17.89美元），而Gemini 3 Flash以极低成本（0.10美元）达到了与GPT-5相近的性能。

### Q5: 有什么可以进一步探索的点？

论文指出了几个重要的局限性和未来方向：1. **评估协议**：当前采用单次推演评估，结果方差较大（如Gemini 3.1 Pro标准差达28.4），未来需要至少3次以上的多次推演平均以提高统计可靠性。2. **数据范围**：基准测试目前仅包含Windows事件日志，未来需要纳入Linux auditd、AWS CloudTrail、网络流量数据等，以覆盖更真实的SOC工作负载。3. **任务变体**：可以设计“警报增强”设置，即先给智能体提供一个Sigma规则警报，再评估其从已知指标出发进行深度调查的能力，从而将“发现广度”与“调查深度”分开测试。4. **智能体训练**：当前评估的智能体均为零样本提示，未来可以探索使用强化学习在该基准的奖励函数上训练智能体，可能显著提高召回率。5. **细粒度评估**：当前的真值标志合并了所有子链的恶意事件，未来可以按杀伤链成员关系标记标志，从而支持按链和按阶段的召回率度量。这些方向将有助于更全面、更稳健地推进LLM智能体在网络防御领域的能力发展。

### Q6: 总结一下论文的主要内容

本文提出了首个专注于评估LLM智能体在开放式、证据驱动威胁狩猎任务中能力的基准测试——“网络防御基准测试”。该基准将106个真实攻击过程记录包装成一个Gymnasium强化学习环境，要求智能体在无引导的情况下，通过迭代查询海量SQLite日志数据库来精确定位恶意事件的时间戳。通过引入活动模拟器进行时间偏移和实体混淆，确保了评估的泛化性和防作弊性。对五个前沿模型的评估揭示了令人震惊的结果：即使最好的模型（Claude Opus 4.6）平均也只能发现不到4%的恶意事件，且所有模型都远未达到操作部署的最低门槛（每个战术召回率≥50%）。这表明，尽管LLM在 curated 的安全问答基准上表现良好，但它们目前严重缺乏在真实、开放式的网络防御调查中所必需的大规模证据收集、假设生成和精确归因能力。该基准为社区提供了一个严谨、可复现的工具，以衡量和推动LLM在网络安全领域智能体能力的进步。
