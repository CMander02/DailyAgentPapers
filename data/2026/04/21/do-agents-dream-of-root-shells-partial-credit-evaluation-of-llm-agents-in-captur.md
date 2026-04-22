---
title: "Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Capture The Flag Challenges"
authors:
  - "Ali Al-Kaswan"
  - "Maksim Plotnikov"
  - "Maxim Hájek"
  - "Roland Vízner"
  - "Arie van Deursen"
  - "Maliheh Izadi"
date: "2026-04-21"
arxiv_id: "2604.19354"
arxiv_url: "https://arxiv.org/abs/2604.19354"
pdf_url: "https://arxiv.org/pdf/2604.19354v1"
categories:
  - "cs.AI"
  - "cs.CR"
  - "cs.SE"
tags:
  - "Agent Benchmark"
  - "Cybersecurity Agent"
  - "Tool-Augmented Agent"
  - "Evaluation Methodology"
  - "Autonomous Agent"
relevance_score: 8.0
---

# Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Capture The Flag Challenges

## 原始摘要

Large Language Model (LLM) agents are increasingly proposed for autonomous cybersecurity tasks, but their capabilities in realistic offensive settings remain poorly understood. We present DeepRed, an open-source benchmark for evaluating LLM-based agents on realistic Capture The Flag (CTF) challenges in isolated virtualized environments. DeepRed places an agent in a Kali attacker environment with terminal tools and optional web search, connected over a private network to a target challenge, and records full execution traces for analysis. To move beyond binary solved/unsolved outcomes, we introduce a partial-credit scoring method based on challenge-specific checkpoints derived from public writeups, together with an automated summarise-then-judge labelling pipeline for assigning checkpoint completion from logs. Using DeepRed, we benchmark ten commercially accessible LLMs on ten VM-based CTF challenges spanning different challenge categories. The results indicate that current agents remain limited: the best model achieves only 35% average checkpoint completion, performing strongest on common challenge types and weakest on tasks requiring non-standard discovery and longer-horizon adaptation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何准确评估大型语言模型（LLM）智能体在现实网络安全攻防任务中的自主能力这一核心问题。研究背景是，LLM及其驱动的智能体在代码生成、漏洞分析等网络安全领域展现出双重应用潜力，但对其在真实对抗环境下的实际能力缺乏深入理解。捕获旗帜（CTF）挑战作为网络安全实践的典型场景，要求智能体具备多步骤推理、工具调用、环境交互和长期规划等复杂能力，是评估此类智能体的理想测试平台。

现有方法的不足主要体现在两方面：首先，大多数评估缺乏真实、隔离的交互环境，无法反映智能体在完整攻击链中的表现；其次，评估指标往往过于粗糙，仅以最终是否成功获取标志（Flag）作为二元判断标准。这种“非成即败”的评估方式无法有效衡量智能体在复杂任务中取得的阶段性进展，而当前LLM智能体虽然难以独立完成整个挑战，却常常能实现有意义的局部突破，因此现有评估方法无法精细刻画其真实能力边界。

为此，本文提出了DeepRed评估框架，其核心要解决的就是在上述真实、隔离的CTF环境中，对LLM智能体进行细粒度、可复现的能力评估。具体而言，论文通过构建一个包含攻击者环境（Kali虚拟机）和目标挑战的虚拟化测试平台，并引入基于检查点的部分信用评分方法，将每个挑战分解为一系列从公开解题报告中提炼出的关键步骤（检查点），从而能够量化智能体在解决挑战过程中所达到的进度，而非仅仅关注最终结果。这为深入理解当前LLM智能体在自主网络安全任务中的优势、局限和失败模式提供了更科学的依据。

### Q2: 有哪些相关研究？

相关研究主要可分为两大类：评测基准和智能体架构。在评测基准方面，NYU CTF Bench 提供了一个涵盖多类别、多难度的大规模已验证CTF挑战基准，用于在受控环境中比较模型和智能体。PentestGPT 评估了LLM在基准目标和详细子任务上辅助渗透测试的能力，揭示了其在复杂工作流中的潜力与在困难目标上的局限。CVE-Bench 则将评估扩展到真实世界Web应用漏洞的利用，试图弥合CTF任务与真实攻击场景之间的差距。在智能体架构方面，EnIGMA 提出了一种专为网络安全工作流设计的LLM智能体，集成了调试器、服务器连接工具等交互式工具，其结果表明更强的工具集成能显著提升智能体在多个安全基准上的性能。

本文与这些工作的关系在于，同样关注LLM智能体在攻击性网络安全任务中的评估。区别主要体现在两点：首先，本文的DeepRed基准将智能体置于完全虚拟化的独立攻击者与目标机环境中进行评测，这比多数现有工作在受控设置下的评估更贴近真实的CTF交互场景。其次，本文引入了基于执行日志的、利用挑战特定检查点进行部分信用评分的自动化流程，提供了比二元成败结果更细粒度的分析能力，从而能更深入理解智能体的局限与进展。

### Q3: 论文如何解决这个问题？

论文通过设计并实现一个名为DeepRed的开源基准测试框架来解决对LLM智能体在真实网络安全攻防场景中能力评估不足的问题。其核心方法是构建一个隔离的虚拟化环境，模拟真实的CTF（Capture The Flag）攻击场景，并引入基于检查点的部分信用评分方法，以细粒度地评估智能体的进展，而非仅依赖二进制的成功/失败结果。

整体框架由三大部分构成：基准测试工具链、挑战数据集和模型集。工具链的设计围绕**真实性、隔离性和可扩展性**三大要求。它使用完整的虚拟机（VM）而非容器来部署挑战，提供了更强的隔离性，并兼容依赖底层系统行为的挑战。攻击者环境是一个Kali Linux VM，通过一个getty服务将终端会话暴露给主机，主机端则通过工具接口让智能体以编程方式发送命令和接收输出。智能体采用基于smolagents的**CodeAgent**架构，允许其编写简短的Python程序来协调命令执行、维护状态和实施多步逻辑，这相比标准的JSON工具调用循环减少了交互开销。此外，智能体还配备了经过过滤的DuckDuckGo网络搜索能力，以防止答案直接泄露。

**关键技术**与**创新点**主要体现在评估方法上。为了解决智能体端到端成功率低、二进制成功指标信号分辨率低的问题，DeepRed引入了**部分信用评分**和**自动化标注流水线**。具体而言：
1.  **基于检查点的评分**：每个CTF挑战都根据公开的解题报告分解为一系列可观察的、技术性的中间里程碑（检查点），例如识别服务、获取初始shell、权限提升等。评估时根据执行轨迹对每个检查点进行通过/失败判定，最终得分是完成检查点的总和。
2.  **自动化标注流水线**：该流水线分为“总结-判断”两步。首先，由于原始执行日志可能很长，使用一个**总结LLM**将交互轨迹浓缩为结构化的分步摘要。然后，将摘要和挑战特定的评分规则一起提交给一个**判断LLM**，由它根据结果（而非具体工具使用）来分配检查点标签。论文通过实验验证了该自动化流程与人类评分者之间具有较高的一致性（最佳组合的Cohen's kappa达到0.72），从而将每次评估从数小时人工工作减少到几分钟，实现了大规模、可重复的基准测试。

通过这一套从隔离执行环境到细粒度自动化评估的完整架构，DeepRed能够对LLM智能体在真实网络安全任务中的能力进行更深入、更有效的量化评估。

### Q4: 论文做了哪些实验？

论文在DeepRed基准测试框架下进行了实验，评估了LLM智能体在现实网络安全任务中的表现。实验设置上，研究者构建了十个基于虚拟机的CTF挑战环境，涵盖不同类别，将智能体置于Kali攻击环境中，提供终端工具和可选网络搜索功能，并通过私有网络连接到目标挑战。每个模型-挑战组合运行三次，使用模型提供商的默认参数配置。

数据集/基准测试为DeepRed，包含十个VM-based CTF挑战（如Whitedoor、Quick、Sysadmin等）。对比方法涉及十个商业可访问的LLM模型，包括GPT-5.1 Codex Max、MiniMax-M1、MiMo-V2 Flash、Devstral 2512、Palmyra X5、Gemini 2.0 Flash、Nova-2 Lite v1、Grok Code Fast 1、Qwen3-Next 80B和Nemotron-3 Nano。

主要结果采用部分信用评分法（基于挑战特定检查点）衡量。关键数据指标显示：最佳模型GPT-5.1 Codex Max的平均检查点完成率为35%（区间29%-44%），其余模型如MiniMax-M1为22%，Nemotron-3 Nano最低仅5%。挑战难度差异显著，Whitedoor完成率最高（24.6%），Fuzzz最低（10.1%）。令牌使用量从Grok Code Fast 1的880万到MiMo-V2 Flash的5810万不等，但更高消耗不保证更好结果；步骤数通常集中在40-60次行动之间，表明性能差异主要源于行动有效性而非交互量。

### Q5: 有什么可以进一步探索的点？

基于论文讨论，可进一步探索的点包括：在评估方法上，当前基于里程碑的评分依赖人工撰写的解题报告，存在路径单一、步骤省略等偏差，未来可研究如何自动提取多解路径的里程碑，或利用LLM辅助生成更全面的评估标准。在任务设计上，当前CTF挑战相对简单，未能涵盖真实攻防中的持久化、横向移动等复杂场景，需构建更贴近实际的基准环境。在智能体能力上，模型在长时规划、状态跟踪和非标准发现方面表现薄弱，可探索增强记忆机制、动态规划调整以及多智能体协作等架构改进。此外，实验规模有限，未来需扩大模型和挑战的多样性，并考虑不同提示策略和架构的影响，以更全面评估智能体的网络安全能力。

### Q6: 总结一下论文的主要内容

该论文提出了DeepRed，一个用于在真实网络安全环境中评估基于大语言模型的智能体能力的开源基准测试框架。其核心贡献在于解决了现有评估方法对自主网络安全任务（特别是攻击性场景）能力理解不足的问题。

论文定义的问题是评估LLM智能体在实战网络攻防（CTF）挑战中的表现。方法上，DeepRed将智能体置于隔离的虚拟化Kali攻击环境中，提供终端工具和可选网络搜索，并连接到目标挑战。为超越简单的“解决/未解决”二元结果，研究引入了基于挑战特定检查点的部分信用评分方法，这些检查点源自公开的解题报告，并配合一个自动化的“总结-判断”标注流程来从日志中分配检查点完成情况。

主要结论是，通过对十个商业可访问的LLM在十个涵盖不同类别的VM-based CTF挑战上进行基准测试，发现当前智能体的能力仍然有限：最佳模型仅实现了平均35%的检查点完成率，在常见挑战类型上表现最强，而在需要非标准发现和更长视野适应的任务上表现最弱。该工作的意义在于提供了一个更细致、更现实的评估平台，有助于推动更强大的自主网络安全智能体的开发。
