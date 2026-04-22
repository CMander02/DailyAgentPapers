---
title: "Refute-or-Promote: An Adversarial Stage-Gated Multi-Agent Review Methodology for High-Precision LLM-Assisted Defect Discovery"
authors:
  - "Abhinav Agarwal"
date: "2026-04-21"
arxiv_id: "2604.19049"
arxiv_url: "https://arxiv.org/abs/2604.19049"
pdf_url: "https://arxiv.org/pdf/2604.19049v1"
github_url: "https://github.com/abhinavagarwal07/refute-or-promote"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.SE"
tags:
  - "Multi-Agent"
  - "Tool Use"
  - "Agent Reliability"
  - "Adversarial Testing"
  - "Software Engineering Agent"
  - "Agent Evaluation"
  - "Agent Architecture"
relevance_score: 7.5
---

# Refute-or-Promote: An Adversarial Stage-Gated Multi-Agent Review Methodology for High-Precision LLM-Assisted Defect Discovery

## 原始摘要

LLM-assisted defect discovery has a precision crisis: plausible-but-wrong reports overwhelm maintainers and degrade credibility for real findings. We present Refute-or-Promote, an inference-time reliability pattern combining Stratified Context Hunting (SCH) for candidate generation, adversarial kill mandates, context asymmetry, and a Cross-Model Critic (CMC). Adversarial agents attempt to disprove candidates at each promotion gate; cold-start reviewers are intended to reduce anchoring cascades; cross-family review can catch correlated blind spots that same-family review misses. Over a 31-day campaign across 7 targets (security libraries, the ISO C++ standard, major compilers), the pipeline killed roughly 79% of 171 candidates before advancing to disclosure (retrospective aggregate); on a consolidated-protocol subset (lcms2, wolfSSL; n=30), the prospective kill rate was 83%. Outcomes: 4 CVEs (3 public, 1 embargoed); LWG 4549 accepted to the C++ working paper; 5 merged C++ editorial PRs; 3 compiler conformance bugs; 8 merged security-related fixes without CVE; an RFC 9000 errata filed under committee review; and 1+ FIPS 140-3 normative compliance issues under coordinated disclosure -- all evaluated by external acceptance, not benchmarks. The most instructive failure: ten dedicated reviewers unanimously endorsed a non-existent Bleichenbacher padding oracle in OpenSSL's CMS module; it was killed only by a single empirical test, motivating the mandatory empirical gate. No vulnerability was discovered autonomously; the contribution is external structure that filters LLM agents' persistent false positives. As a preliminary transfer test beyond defect discovery, a simplified cross-family critique variant also solved five previously unsolved SymPy instances on SWE-bench Verified and one SWE-rebench hard task.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）辅助缺陷发现中存在的“精度危机”问题。研究背景是，尽管LLM能够识别真实软件漏洞，但其在实际部署中会产生大量似是而非的错误报告，导致过高的误报率。这种问题已对开源维护者造成了严重困扰，例如curl的漏洞赏金计划因AI生成提交的确认率低于5%而永久关闭，HackerOne也因AI提交量过大而暂停了互联网漏洞赏金计划。现有基于LLM的方法主要优化了生成内容的“合理性”而非“正确性”，缺乏有效的机制来过滤这些持续产生的误报，从而淹没了真正的发现，损害了可信度。

本文的核心问题是：如何设计一种方法论，能够系统性地、高效地过滤掉LLM代理产生的顽固性误报，从而将缺陷发现的输出精度提升到可实际部署和披露的水平。为此，论文提出了“Refute-or-Promote”方法，这是一种推理阶段的可靠性模式。它通过结合分层上下文狩猎（SCH）进行候选生成，并引入对抗性淘汰指令、上下文不对称性、跨模型批评者（CMC）以及强制性的实证验证门控等多智能体对抗审查机制。该方法旨在针对合作式辩论可能无法捕获的各类误报，其最终目标不是实现自主漏洞发现，而是提供一个外部的、结构化的过滤框架，以显著提升LLM辅助缺陷发现流程的精确度，使其产出的结果足够可靠，能够被维护者接受并促成实际的修复、CVE分配或标准修订。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. LLM辅助漏洞发现**：如Big Sleep、DeepMind的CodeMender、RepoAudit等单智能体系统，以及Heelan、AISLE等工作。这些研究证明了LLM发现缺陷的潜力，但普遍面临高误报率问题。本文的Refute-or-Promote方法则通过引入对抗性审查和多阶段门控机制，专门针对误报过滤进行设计，旨在实现满足实际披露要求的高精度验证。

**2. 多智能体辩论与集成**：包括Reflexion、Self-Refine等基于自批判的迭代优化框架，以及Irving等人提出的用于AI对齐的辩论方法。本文方法与这些工作的主要区别在于：审查者被赋予明确的“否决”使命（kill mandate），而非改进或评估使命；采用跨模型族（cross-family）审查以避免共享偏见；并强调上下文隔离。Song的研究为本文的阶段门控设计提供了直接支持。

**3. 专门的对抗性漏洞发现系统**：例如AEGIS和VulTrial，它们采用辩证或模拟法庭角色扮演的结构，旨在达成共识或判决。本文则强调硬性对抗性否决使命、跨模型异质性，并在真实世界场景中通过外部机构接受（如CVE、合并的PR）进行评估，而非依赖基准测试。

**4. 其他多智能体漏洞检测系统**：如IRIS、MAVUL、VulAgent等。这些系统通常将提议者输出视为需要验证或改进的主张，而非首要进行证伪，且未使用跨模型族审查员。

**5. 同时期的对抗性与多智能体工作**：包括Jain等人提出的少数否决协议、InfCode的对称补丁/测试双智能体循环、SWE-Debate的收敛性辩论、Argus的合作式集成等。本文通过对比指出，Refute-or-Promote独特地结合了分层上下文搜索的候选生成、硬对抗性否决使命、跨模型批判、冷启动上下文不对称性以及强制性实证验证门控，并以真实世界缺陷发现成果作为评估依据。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为“反驳或提升”的四阶段对抗性协议来解决LLM辅助缺陷发现中精度不足的问题。该协议的核心思想是在推理时引入多阶段的对抗性审查，通过层层筛选来过滤掉大量似是而非的错误报告，只保留高可信度的发现。

整体框架包含七个主要阶段：准备阶段、候选生成阶段以及四个对抗性审查阶段（A到D）。在准备阶段，系统会检出目标代码的稳定发布分支，并行运行研究代理以收集历史CVE和代码热点分析，为后续步骤提供先验知识。候选生成阶段采用分层上下文狩猎策略，并行派遣多个猎手，从不同来源、子系统和迭代波次中生成候选缺陷，并要求每个猎手进行自我批判，说明候选可能不可利用的原因。

四个对抗性审查阶段是方法的核心。阶段A和B采用并行的创造性与对抗性双轨设计。在阶段A，一个创造性代理尝试论证缺陷的可利用性，而两个对抗性代理则仅基于候选声明（不接触创造性代理的推理）尝试进行代码层面的反驳，以避免锚定效应。候选只有在其对抗性代理无法提出有根据的反驳且创造性代理能提出合理的利用论证时才能通过。阶段B进一步升级，使用两个创造性代理（一个深度合成，一个冷启动）和三个对抗性代理（包括一个来自更高级模型），通过上下文不对称性（例如，有的对抗代理仅获知声明，有的获知完整合成信息）来增强审查的独立性。冷启动代理的独立判断被认为比知情代理间的共识具有更高价值信号。

阶段C是经验验证与影响校准门控。任何候选在缺乏经验证伪或确认的情况下都不能进入披露阶段。系统会尝试在本地或通过云虚拟机执行概念验证。此外，对抗性代理还会对候选缺陷的严重性评分进行系统性下调校准，纠正过高的声称。

阶段D引入了跨模型批评机制。来自不同模型家族的一个或多个代理，基于最小化上下文对候选进行独立批判。这旨在捕捉同家族模型审查可能因相关训练数据错误而共同遗漏的盲点。如果跨模型批评仅反驳了部分子主张，候选会返回早期阶段进行细化而非直接被丢弃。

该方法的创新点包括：1) 将分层上下文狩猎与多阶段对抗性门控相结合的系统性架构；2) 在对抗性审查中刻意设计上下文不对称性和冷启动审查，以减少锚定级联和虚假共识；3) 强制性的经验验证门控，确保理论发现具有实证基础；4) 引入跨模型批评作为最后防线，以发现相关盲点。整个流程由编排代理按协议执行，人类仅在最终披露前进行审查和干预，从而在自动化框架内实现了高精度的缺陷筛选。

### Q4: 论文做了哪些实验？

论文的实验设置是一个为期31天的多目标评估活动，覆盖了7个目标：安全库（如libfuse、wolfSSL、lcms2、OpenSSL）、ISO C++标准以及主要编译器（GCC、MSVC）。实验采用提出的“Refute-or-Promote”流水线，该流水线结合了分层上下文狩猎（SCH）生成候选缺陷、对抗性淘汰指令、上下文不对称和跨模型批评器（CMC）。实验涉及多个对抗性智能体在多个“晋升门”阶段试图反驳候选缺陷，并使用冷启动评审员以减少锚定效应，同时采用跨模型族评审来捕捉相同模型族可能遗漏的相关盲点。

使用的数据集/基准测试并非传统静态数据集，而是针对上述真实世界软件项目和标准文档的代码库与规范文本。此外，论文还进行了一个初步的迁移测试，使用简化的跨族批评变体在SWE-bench Verified基准上解决了五个先前未解决的SymPy实例和一个SWE-rebench困难任务。

对比方法方面，实验主要将提出的对抗性多智能体评审方法与基线LLM辅助缺陷发现（通常产生大量假阳性）进行对比。关键数据指标包括：在总计约171个初始安全漏斗候选缺陷中，约79%（约135个）在披露前被对抗性评审淘汰；在一个采用统一协议的前瞻性子集（lcms2和wolfSSL，n=30）中，淘汰率为83%（25/30）。最终产出成果包括：4个CVE（3个公开，1个禁运）、1个被C++工作文件接受的LWG缺陷（LWG 4549）、5个合并的C++编辑PR、3个编译器一致性错误、8个合并的非CVE安全相关修复、1个提交委员会评审的RFC 9000勘误，以及1个以上处于协调披露中的FIPS 140-3合规性问题。实验中的一个关键失败案例是，十个专用评审员一致认可了OpenSSL CMS模块中一个不存在的Bleichenbacher填充预言机，最终仅通过一次实证测试被淘汰，这促使方法中加入了强制性的实证验证门。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度展开。首先，方法在泛化性上存在局限：实验主要集中于C/C++代码库，在其他语言或领域的有效性未经验证；且协议在活动中持续演化，早期成功受目标选择、人工调整等混杂因素影响，缺乏严格的消融研究来分离各机制（如对抗性审查、上下文不对称）的独立贡献。其次，架构上存在假阴性风险：流程是单向的，侧重于通过“否决指令”过滤误报，但可能错误扼杀真实缺陷，仅依赖人工干预进行挽救，未来可探索引入具有“确认指令”的隔离复活代理来自动化纠正。此外，虽然初步尝试表明方法可迁移至代码修复任务（如解决SWE-bench中未破解的实例），但在跨领域（如从C++到安全审计）的负迁移现象仍需系统研究。

可能的改进思路包括：1）设计双向验证管道，整合自动化的复活机制以减少假阴性；2）开展大规模消融实验，量化各组件对精度和召回率的独立影响；3）将方法扩展至更广泛的软件工程任务（如自动化代码审查、形式化验证辅助），并探索在异构代理（如不同模型家族、专业领域代理）间建立更动态的对抗协作框架，以进一步降低共享训练数据先验带来的系统性偏差。

### Q6: 总结一下论文的主要内容

这篇论文针对LLM辅助缺陷发现中存在的“精度危机”——即大量看似合理但错误的报告淹没维护者、损害真实发现可信度的问题，提出了一种名为“Refute-or-Promote”的对抗性、分阶段、多智能体审查方法。其核心贡献是设计了一套推理时可靠性模式，通过架构性创新来过滤LLM智能体持续产生的误报。

该方法结合了多个关键机制：首先，使用分层上下文狩猎（SCH）生成候选缺陷；然后，在多个“晋升关卡”中引入对抗性智能体，其唯一任务是尝试反驳候选缺陷；同时采用上下文不对称和冷启动审查员设计，以减少锚定效应；还引入了跨模型批评家（CMC）进行跨家族审查，以捕捉同家族审查可能遗漏的相关盲点；最后，强制性的实证验证作为最终关卡。

在为期31天、涵盖7个目标（安全库、ISO C++标准、主要编译器）的活动中，该流程在进入披露阶段前淘汰了约79%的候选缺陷。实际产出包括4个CVE、被C++工作组采纳的提案、多个合并的修复等，所有成果均经外部实际接受评估。一个关键结论是：AI智能体间的共识不等于正确性（例如，80多个智能体曾一致认可一个不存在的漏洞）。论文指出，该方法通过对抗性任务分配、跨模型批评和强制实证验证这三种机制，分别针对推理偏差、锚定效应和相关训练误差等不同的失败类别，其组合构成了一种可推广到其他可独立验证真值的LLM输出领域的可靠性模式。
