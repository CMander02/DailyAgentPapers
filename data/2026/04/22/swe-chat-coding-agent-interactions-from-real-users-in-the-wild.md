---
title: "SWE-chat: Coding Agent Interactions From Real Users in the Wild"
authors:
  - "Joachim Baumann"
  - "Vishakh Padmakumar"
  - "Xiang Li"
  - "John Yang"
  - "Diyi Yang"
  - "Sanmi Koyejo"
date: "2026-04-22"
arxiv_id: "2604.20779"
arxiv_url: "https://arxiv.org/abs/2604.20779"
pdf_url: "https://arxiv.org/pdf/2604.20779v1"
categories:
  - "cs.AI"
  - "cs.CY"
  - "cs.SE"
tags:
  - "Coding Agent"
  - "Dataset"
  - "Human-Agent Interaction"
  - "Empirical Study"
  - "Real-World Evaluation"
  - "Failure Analysis"
  - "Tool Usage"
relevance_score: 8.0
---

# SWE-chat: Coding Agent Interactions From Real Users in the Wild

## 原始摘要

AI coding agents are being adopted at scale, yet we lack empirical evidence on how people actually use them and how much of their output is useful in practice. We present SWE-chat, the first large-scale dataset of real coding agent sessions collected from open-source developers in the wild. The dataset currently contains 6,000 sessions, comprising more than 63,000 user prompts and 355,000 agent tool calls. SWE-chat is a living dataset; our collection pipeline automatically and continually discovers and processes sessions from public repositories. Leveraging SWE-chat, we provide an initial empirical characterization of real-world coding agent usage and failure modes. We find that coding patterns are bimodal: in 41% of sessions, agents author virtually all committed code ("vibe coding"), while in 23%, humans write all code themselves. Despite rapidly improving capabilities, coding agents remain inefficient in natural settings. Just 44% of all agent-produced code survives into user commits, and agent-written code introduces more security vulnerabilities than code authored by humans. Furthermore, users push back against agent outputs -- through corrections, failure reports, and interruptions -- in 44% of all turns. By capturing complete interaction traces with human vs. agent code authorship attribution, SWE-chat provides an empirical foundation for moving beyond curated benchmarks towards an evidence-based understanding of how AI agents perform in real developer workflows.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI编程代理（AI coding agents）大规模应用背景下，缺乏对其真实使用情况和实际效用进行实证研究的问题。研究背景是，尽管AI编程代理（如增强了大语言模型并具备自主编码环境交互能力的工具）已被广泛采用，甚至能完成部分耗时的人类编程任务，但现有研究多局限于人工构建的、解决方案明确的基准测试（如GitHub问题集），这些测试忽略了真实开发中人与代理的协作工作流和交互维度。现有方法的不足在于，没有公开的大规模数据集能完整记录开发者如何在实际场景中提示、引导、覆盖以及最终采纳或丢弃代理生成的代码，导致我们无法确知代理输出的代码有多少被实际使用、其失败模式如何以及用户如何应对。

因此，本文的核心问题是：通过构建并利用首个大规模真实世界编程代理会话数据集SWE-chat，从实证角度刻画用户与编程代理的真实交互模式（RQ1）以及代理的失败模式和用户应对方式（RQ2），从而超越传统基准测试，为理解AI代理在真实开发工作流中的表现提供证据基础，并推动开发更有用的代理。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：数据集构建、编码代理评估以及实际使用模式分析。

在**数据集构建**方面，现有研究多基于模拟任务或实验室环境收集交互数据（如HumanEval、SWE-bench），而SWE-chat首次大规模采集了开源开发者真实环境中的完整会话，提供了带有代码归属标注的完整交互轨迹，弥补了真实场景数据缺失的空白。

在**编码代理评估**方面，传统工作侧重于静态基准测试（如代码生成正确率），而本文利用真实数据分析了代理在实际工作流中的效率（仅44%代理生成代码被提交）与安全性（引入更多漏洞），将评估重点从性能转向实用性和可靠性。

在**实际使用模式**方面，先前研究多关注用户接受度或个案分析，本文通过大规模实证揭示了双峰使用模式（“氛围编码”与完全人工编写），并量化了用户对代理输出的高频率修正与中断（44%的轮次），深化了对人机协作动态的理解。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为SWE-chat的大规模真实世界数据集来解决缺乏关于人们如何实际使用AI编程助手以及其输出在实践中多大程度有用的实证证据这一问题。其核心方法并非提出一个新的算法或模型，而是建立一个数据收集、处理和标注的完整管道，以支持对真实人机协作编程的实证研究。

整体框架是一个持续运行的自动化数据收集与分析系统。主要模块包括：1）**数据收集管道**：通过集成Entire.io的CLI工具，从已选择加入的公开GitHub仓库中自动捕获编程助手会话记录。这些记录包含用户提示、助手响应、工具调用（文件编辑、shell命令、代码搜索等）和令牌使用情况，并关联到具有代码行级作者归属的提交。2）**数据集构建与扩展**：将原始日志处理成结构化的会话数据，形成一个“活”的数据集，能够自动持续地发现和处理新会话。当前数据集包含约6000个会话、超过63000个用户提示和355000次助手工具调用。3）**数据丰富化与标注**：为了深入理解复杂的人机行为，研究团队为数据集添加了多层次的注释。这包括在**会话级别**评估整体成功率、识别用户行为模式（如专家挑剔者、模糊需求者、改变主意者）；在**用户提示级别**标注意图（如创建新代码、重构、调试）和用户对助手输出的“推回”类型（如纠正、拒绝、失败报告）。这些标注主要利用经过验证的LLM作为评判员来实现可扩展性。4）**度量与分析框架**：定义了一套量化指标来评估助手效率与代码质量，例如计算助手产生的代码最终进入用户提交的比例（代码存活率）、分析助手自我重写带来的开销（编码效率），以及评估每提交一行代码所需的令牌、成本、时间和用户努力。此外，通过静态分析工具（如Semgrep）对比提交前后的代码快照，以衡量不同编码模式引入安全漏洞的比率。

创新点在于：首先，这是首个从开源开发者真实工作环境中收集的大规模编程助手交互数据集，突破了以往依赖人工基准测试的局限。其次，其设计是一个持续生长的“活”数据集，能动态反映技术使用趋势。第三，通过结合详细的交互日志、代码作者归属和多维度人工标注，为分析真实人机协作的成功与失败模式提供了前所未有的细粒度实证基础。最后，所定义的度量体系（如代码存活率、安全漏洞引入率）为客观评估编程助手在实践中的效用和效率提供了新的方法论。

### Q4: 论文做了哪些实验？

该研究基于SWE-chat数据集进行了实证分析，主要包含两类实验。

**实验设置与数据集**：研究使用自行构建的SWE-chat数据集，该数据集持续从公开代码仓库自动收集真实的编程智能体交互会话。当前版本包含6,000个会话、63,000条用户提示和355,000次智能体工具调用。研究通过代码作者归属（人类 vs. 智能体）对交互进行标注，并定义了三种编码模式：纯人类编码（22.7%会话）、协作编码（36.5%会话）和氛围编码（40.8%会话，即智能体撰写99%以上代码）。

**对比方法与主要结果**：
1.  **交互模式分析**：用户请求多样，最常见的是理解现有代码（19.0%）和创建新代码（13.4%）。智能体单轮调用工具多，三分之一为bash命令。用户行为角色可分为“专家挑剔者”、“模糊需求者”和“目标变更者”，大多数用户属于专家挑剔者。
2.  **效率与代码留存**：仅44.3%的智能体生成代码最终被用户提交。氛围编码模式下留存率较高（59.0%），但代价是每100行提交代码的中位令牌消耗达204K（约为协作模式的3倍），中位成本为$0.13/100行，耗时也更长（中位12.6分钟/100行）。
3.  **安全漏洞**：氛围编码提交引入安全漏洞的比率高达每千行0.76个，分别是纯人类编码（0.08）的9倍和协作编码（0.14）的5倍。同时其修复漏洞的比率也更高（0.52/千行）。
4.  **用户监督**：用户频繁干预智能体：44%的轮次中用户会通过纠正、报告失败或中断进行反馈；39%的轮次后用户会进行“软性推回”纠正。智能体主动要求澄清的比例很低（1.1%-2.6%）。

**关键指标**：代码留存率44.3%；氛围编码代码留存率59.0%；氛围编码漏洞引入率0.76/千行；用户推回比例44%轮次；氛围编码令牌消耗204K/100行。

### Q5: 有什么可以进一步探索的点？

基于论文讨论部分，未来研究可进一步探索以下几个方向。首先，在提升人机协作效率方面，当前智能体自主性增强但主动寻求澄清的频率极低（仅1.4%），导致用户需频繁干预（44%的轮次）。未来可研究如何设计更自适应的人机交互机制，例如通过分析数据集中的“纠正-响应”循环，开发能主动识别不确定性并适时寻求用户指导的智能体，从而减少人工监督负担。其次，在代码安全性与可靠性方面，智能体生成的代码引入安全漏洞的概率是纯人工代码的9倍，且智能体极少主动报告不确定性。未来需探索在真实工作流中有效的安全干预措施（如针对性微调或系统提示强化），并利用该数据集构建自然测试环境进行评估。再者，在评估方法创新上，现有基准测试多关注单次代码生成，而真实场景中智能体主要用于理解现有代码并进行多轮迭代交互。未来可基于该数据集构建更贴近实际工作流的评估基准，例如评估智能体在给定真实对话上下文后提出合理后续行动的能力。此外，该数据集为训练用户模拟器提供了丰富素材，可支持离线评估范式的开发，降低实验成本并扩大研究范围。最后，作为持续更新的动态数据集，它支持纵向分析，有助于追踪智能体使用模式的演变，为技术优化提供实时依据。

### Q6: 总结一下论文的主要内容

该论文的核心贡献是构建了首个大规模真实世界AI编程代理交互数据集SWE-chat，并基于此对实际使用模式与失败情况进行了实证分析。针对当前缺乏真实交互数据的问题，该数据集从开源开发者中自动收集了6000个会话、6.3万条用户提示和35.5万次工具调用，并持续更新。方法上，论文通过追踪完整交互轨迹和代码作者归属（人工vs代理），量化分析了使用行为与输出效率。主要结论显示：用户使用模式呈现双峰分布，41%的会话中代理编写几乎所有代码（氛围编程），但代理产出代码仅44%被最终提交，且效率较低，氛围编程每行提交代码消耗的token和成本是协作编程的3倍。此外，代理编写代码引入的安全漏洞是人工代码的9倍，用户在44%的交互轮次中会对代理输出进行纠正或中断。这些发现揭示了当前编程代理在真实场景中的局限性，为超越传统基准测试、构建更实用的AI代理提供了实证基础。
