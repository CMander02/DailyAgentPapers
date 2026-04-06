---
title: "Beyond Resolution Rates: Behavioral Drivers of Coding Agent Success and Failure"
authors:
  - "Tural Mehtiyev"
  - "Wesley Assunção"
date: "2026-04-02"
arxiv_id: "2604.02547"
arxiv_url: "https://arxiv.org/abs/2604.02547"
pdf_url: "https://arxiv.org/pdf/2604.02547v1"
categories:
  - "cs.SE"
tags:
  - "Coding Agent"
  - "Empirical Study"
  - "Failure Analysis"
  - "Behavioral Analysis"
  - "Tool-Augmented Interaction"
  - "LLM Capability"
  - "Agent Framework"
  - "Benchmarking"
relevance_score: 8.5
---

# Beyond Resolution Rates: Behavioral Drivers of Coding Agent Success and Failure

## 原始摘要

Coding agents represent a new paradigm in automated software engineering, combining the reasoning capabilities of Large Language Models (LLMs) with tool-augmented interaction loops. However, coding agents still have severe limitations. Top-ranked LLM-based coding agents still fail on over 20% of benchmarked problems. Yet, we lack a systematic understanding of why (i.e., the causes) agents fail, and how failure unfolds behaviorally. We present a large-scale empirical study analyzing 9,374 trajectories from 19 agents (8 coding agent frameworks, 14 LLMs) on 500 tasks. We organize our analysis around three research questions. First, we investigate why agents fail on specific tasks and find that patch complexity alone does not explain difficulty: 12 never-solved tasks require only simple patches and were considered easy by human annotators, yet all agents fail due to gaps in architectural reasoning and domain knowledge. Second, we examine how behavioral patterns differentiate success from failure. The widely reported correlation between trajectory length and failure reverses direction once task difficulty is controlled, revealing it as a confound. Instead, trajectory structure discriminates consistently: agents that gather context before editing and invest in validation succeed more often, and these strategies are agent-determined rather than task-adaptive. Third, we disentangle LLM capability from framework design and find that the LLM is the primary driver of both outcome and behavior: agents sharing the same LLM agree on far more tasks than agents sharing the same framework, and the framework performance gap shrinks with each generation of LLM improvement. Framework prompts do influence agent tactics, but this influence diminishes with stronger LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在超越传统的成功率指标，深入探究编码智能体（Coding Agents）成功与失败背后的行为驱动因素。研究背景是，基于大语言模型（LLM）和工具增强交互循环的编码智能体已成为自动化软件工程的新范式，它们能像自主开发者一样操作代码库。然而，现有最先进的智能体在基准测试中仍有超过20%的失败率，这构成了一个严峻的现实问题。

现有研究的不足在于，它们通常只关注结果层面的指标（如解决率），或在小样本中分析失败原因和行为模式，但很少在控制任务难度的大规模数据集上，系统性地将失败的“原因”（why）与“过程”（how）两个维度联系起来。这导致我们缺乏对“特定行为如何导致特定失败原因”以及“应优先改进智能体设计的哪个方面”的系统性理解，从而限制了科学洞察和实际进展。

因此，本文要解决的核心问题是：**系统性地理解编码智能体为何失败以及失败行为如何展开**。具体通过三个研究问题展开：1) 探究智能体在某些任务上失败的根本原因，特别是那些看似简单却无人能解的任务；2) 分析成功与失败轨迹在行为模式上的差异，并检验被广泛报告的轨迹长度与失败的相关性是否可靠；3) 厘清智能体成功的主要驱动力是LLM的能力还是框架设计，以指导未来的改进方向。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕编码智能体的评估、行为分析和架构设计展开，可分为以下几类：

**1. 评估与基准测试类**：现有研究如SWE-bench等基准测试主要关注智能体的“解决率”，通过任务完成情况衡量性能。本文指出这类工作忽略了失败原因和行为模式的深入分析，仅以结果为导向。本文则转向行为轨迹分析，探究失败背后的认知与策略缺陷。

**2. 智能体框架与方法类**：相关研究包括SWE-agent、OpenHands等框架，它们通过设计工具使用循环、上下文管理来提升智能体性能。本文与这些工作的关系在于使用了多种框架进行实验，但区别在于：本文发现框架设计对行为策略的影响有限，而大语言模型（LLM）能力才是主导因素；随着LLM迭代，框架间的性能差距逐渐缩小。

**3. 行为与轨迹分析类**：部分研究关注智能体轨迹长度与失败的关系，认为较长轨迹常伴随失败。本文通过控制任务难度发现这一相关性是混淆因素，并进一步揭示轨迹结构（如先收集上下文再编辑、注重验证）才是成功的关键区分点。本文首次系统性地将行为模式与任务难度解耦，强调策略的智能体内生性而非任务适应性。

**4. LLM能力分析类**：已有工作多单独评估LLM的代码生成能力。本文创新性地将LLM与框架分离比较，发现相同LLM的智能体在任务结果和行为上高度一致，而相同框架的智能体差异显著，从而论证LLM是性能和行为的主要驱动者。

### Q3: 论文如何解决这个问题？

论文通过一个大规模实证研究来解决对编码智能体失败原因和行为模式缺乏系统性理解的问题。其核心方法是设计一个包含三个研究问题的分析框架，并利用从19个智能体（涵盖8个框架和14个LLM）在500个任务上收集的9,374条轨迹数据进行定量与定性相结合的分析。

整体框架和研究设计围绕三个核心研究问题展开。首先，为了探究智能体在特定任务上失败的根本原因（RQ1），研究不仅提取了包括补丁复杂度、测试需求、问题描述质量和元数据在内的四大类任务特征进行定量分析，更对12个所有智能体均未解决的“简单”任务进行了深入的定性轨迹分析。研究发现，补丁复杂度本身并不能解释失败；深层原因在于智能体存在**架构推理鸿沟**：它们能正确定位错误文件并生成看似合理的补丁，但倾向于在错误的架构层级进行干预（例如修补症状而非根本原因），或存在领域知识缺口。

其次，为了辨别成功与失败的行为模式差异（RQ2），研究创新性地采用了**双重分析方法**以控制混杂变量。**方法A**固定智能体，比较其在不同任务上的成功与失败轨迹，但受任务难度干扰。**方法B**固定任务，比较不同智能体在该任务上的成功与失败轨迹，从而控制了任务难度。通过这种方法，论文揭示了被广泛报告的“失败轨迹更长”现象实际上与任务难度混杂；一旦控制难度，趋势发生逆转。真正能区分成功的行为特征是**轨迹结构**：成功的智能体倾向于在编辑前进行更多的**上下文收集（探索）**，并在整个过程中投入更多的**验证努力**。这些策略模式主要由智能体自身决定，而非针对任务自适应调整。

最后，为了厘清LLM能力与框架设计各自的影响（RQ3），研究利用其完整的“智能体×任务”矩阵设计了一个“自然实验”：通过保持框架不变、更换LLM来隔离LLM效应；通过保持LLM不变、更换框架来隔离框架效应。分析发现，**LLM是结果和行为的主要驱动因素**：共享相同LLM的智能体在任务结果上的一致性远高于共享相同框架的智能体，并且随着LLM代际提升，不同框架之间的性能差距在缩小。框架提示确实会影响智能体的战术，但这种影响随着LLM能力的增强而减弱。

关键技术包括：1）**丰富的轨迹编码方案**，将智能体动作与环境反馈结合，定义了13种符号（如Lb浏览、P修补、Vp验证通过等），以捕捉执行质量和错误类型；2）**系统的特征提取管道**，从任务描述和补丁中自动计算多维特征；3）**统计与可视化分析**，结合非参数检验（Mann-Whitney U, Cliff‘s δ）和详细的案例研究。该研究的创新点在于首次大规模地控制了任务难度和智能体身份这两个关键混杂因素，从而揭示了之前被掩盖的行为真相，并明确指出编码智能体当前的能力上限在于架构推理，而非简单的补丁生成。

### Q4: 论文做了哪些实验？

本研究基于SWE-bench Verified基准，对19个智能体（涵盖8个框架和14个LLM）在500个真实世界bug修复任务上的9,374条执行轨迹进行了大规模实证分析。实验设置包括从公共排行榜收集完整的“智能体×任务”矩阵数据，并对轨迹进行细粒度编码（13种动作/响应符号），同时提取了任务级别的四大类特征（补丁复杂度、测试需求、问题描述质量和元数据）。主要实验围绕三个研究问题展开：

首先，针对失败原因（RQ1），实验识别出12个所有智能体均未解决的“简单”任务（单文件、≤10行修改），并与25个具有类似补丁复杂度但总能解决的任务进行对比。定量分析显示，两组任务在补丁复杂度上无显著差异（如平均修改行数：4.75 vs. 3.76，p=0.24），但测试需求特征（如Fail-to-pass计数：2.42 vs. 1.24，p<0.001）和问题描述特征（如包含复现代码的比例：0.67 vs. 0.24，p=0.014）存在显著区别。定性轨迹分析进一步揭示，失败主要源于**架构推理鸿沟**：智能体能正确定位文件（12/12）并编辑（10/12），但倾向于在错误层级（如修补症状而非根因）进行干预。

其次，针对行为模式（RQ2），实验通过两种方法控制混淆变量。方法A（固定智能体，跨任务比较）复现了先前结论：失败轨迹显著更长（长度增加14.0%至111.9%，所有p<0.001）。但方法B（固定任务，跨智能体比较）发现，在控制任务难度后，**成功轨迹反而更长**（成功平均44.0步 vs. 失败39.6步，长10.0%），且在63%的任务上成功轨迹更长（p=1.9×10⁻⁹），表明轨迹长度与任务难度强相关，而非策略质量。进一步分析行为结构发现，成功智能体更倾向于**先收集上下文再编辑**（首次编辑步数与解决率正相关，ρ=+0.68，p<0.001），并在轨迹中投入更多**验证步骤**（验证步骤比例与解决率正相关，ρ=+0.50，p<0.05）。

最后，针对LLM与框架影响（RQ3），实验通过“自然实验”设计分离两者效应。结果表明，**LLM是结果和行为的主要驱动因素**：使用相同LLM的智能体在任务结果上的一致性远高于使用相同框架的智能体。随着LLM代际提升，框架间的性能差距缩小。框架提示虽能影响战术，但其影响力随LLM能力增强而减弱。

### Q5: 有什么可以进一步探索的点？

该论文揭示了当前代码智能体的核心局限在于**架构推理能力不足**，而非简单的补丁复杂度或轨迹长度问题。基于此，未来研究可从以下几个方向深入探索：

1.  **增强架构感知与因果推理**：研究发现，智能体常能定位正确文件，却因在错误的架构层次（如修补症状而非根因）而失败。未来可探索为智能体注入显式的软件架构知识，例如通过图神经网络建模代码库的组件边界、依赖方向和因果链，或设计专门的“架构反思”步骤，引导其分析问题应归属的抽象层次（如显示层 vs. 序列化层）。

2.  **开发更精细的评估基准与诊断工具**：当前基准（如SWE-bench）的测试需求指标虽能部分区分难度，但未能充分捕捉架构复杂性。未来可构建包含“架构陷阱”任务的诊断性基准，并开发相应的轨迹分析工具，以自动识别智能体在“调用者-被调用者”、“生产者-消费者”等关系判断上的错误模式，从而提供更精准的能力评估。

3.  **设计自适应与策略性的智能体框架**：论文指出成功智能体的行为模式（如先收集上下文再编辑、投入验证）是智能体自身决定的，而非针对任务自适应。未来框架设计可超越静态提示，引入元认知或强化学习机制，使智能体能根据任务早期反馈（如编辑后测试频繁失败）动态调整策略，例如在陷入“修补-验证”死循环时主动切换为深度代码探索。

4.  **深入理解LLM能力与框架作用的演进关系**：研究证实LLM是结果和行为的主要驱动因素，框架的影响随LLM代际提升而减弱。未来需持续追踪：随着LLM代码能力提升，框架的设计空间将如何演变？是否会出现“框架收敛”，即仅需极简设计便能充分发挥最强LLM的架构推理潜力？这要求对LLM的内部推理机制与外部工具使用的交互进行更细粒度研究。

### Q6: 总结一下论文的主要内容

该论文对代码生成智能体的失败原因与行为模式进行了大规模实证研究。研究基于9,374条执行轨迹，涉及19个智能体（8个框架、14个大语言模型）在500项任务上的表现。

核心问题是探究智能体为何失败以及失败如何通过行为模式体现。研究发现：首先，失败不能简单归因于补丁复杂度，有12项从未解决的任务仅需简单修改，但所有智能体均因架构推理和领域知识缺陷而失败。其次，在控制任务难度后，轨迹长度与失败的相关性发生逆转，表明其是混淆变量；真正区分成败的是轨迹结构：先收集上下文再编辑、并投入资源进行验证的智能体成功率更高，且这些策略由智能体自身决定，而非任务自适应。最后，研究分离了大语言模型能力与框架设计的影响，发现大语言模型是结果和行为的主要驱动因素：使用相同大语言模型的智能体在任务上的一致性远高于使用相同框架的智能体，且框架间的性能差距随大语言模型代际提升而缩小。框架提示虽能影响策略，但其影响力随大语言模型变强而减弱。

论文的意义在于超越了仅关注解决率的评估，通过行为分析揭示了智能体失败的根本原因和成功的关键策略，为未来改进代码智能体的设计和评估提供了实证基础。
