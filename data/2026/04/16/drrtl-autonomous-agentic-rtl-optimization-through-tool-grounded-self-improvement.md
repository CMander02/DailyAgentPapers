---
title: "Dr.~RTL: Autonomous Agentic RTL Optimization through Tool-Grounded Self-Improvement"
authors:
  - "Wenji Fang"
  - "Yao Lu"
  - "Shang Liu"
  - "Jing Wang"
  - "Ziyan Guo"
  - "Junxian He"
  - "Fengbin Tu"
  - "Zhiyao Xie"
date: "2026-04-16"
arxiv_id: "2604.14989"
arxiv_url: "https://arxiv.org/abs/2604.14989"
pdf_url: "https://arxiv.org/pdf/2604.14989v1"
categories:
  - "cs.AI"
  - "cs.AR"
tags:
  - "Agentic Framework"
  - "Tool Use"
  - "Self-Improvement"
  - "Multi-Agent"
  - "RTL Optimization"
  - "Closed-Loop Optimization"
  - "Skill Learning"
relevance_score: 8.0
---

# Dr.~RTL: Autonomous Agentic RTL Optimization through Tool-Grounded Self-Improvement

## 原始摘要

Recent advances in large language models (LLMs) have sparked growing interest in automatic RTL optimization for better performance, power, and area (PPA). However, existing methods are still far from realistic RTL optimization. Their evaluation settings are often unrealistic: they are tested on manually degraded, small-scale RTL designs and rely on weak open-source tools. Their optimization methods are also limited, relying on coarse design-level feedback and simple pre-defined rewriting rules. To address these limitations, we present Dr. RTL, an agentic framework for RTL timing optimization in a realistic evaluation environment, with continual self-improvement through reusable optimization skills. We establish a realistic evaluation setting with more challenging RTL designs and an industrial EDA workflow. Within this setting, Dr. RTL performs closed-loop optimization through a multi-agent framework for critical-path analysis, parallel RTL rewriting, and tool-based evaluation. We further introduce group-relative skill learning, which compares parallel RTL rewrites and distills the optimization experience into an interpretable skill library. Currently, this library contains 47 pattern--strategy entries for cross-design reuse to improve PPA and accelerate convergence, and it can continue evolving over time. Evaluated on 20 real-world RTL designs, Dr. RTL achieves average WNS/TNS improvements of 21\%/17\% with a 6\% area reduction over the industry-leading commercial synthesis tool.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决数字集成电路设计领域中，寄存器传输级（RTL）自动优化面临的现实性不足和效率瓶颈问题。研究背景是，RTL设计质量直接决定了后续逻辑综合和物理设计的优化空间，但现代RTL设计因包含深流水线、宽数据路径等复杂结构，使得时序收敛极具挑战。传统上，工程师依赖综合工具反馈进行手动RTL重写，但该过程劳动密集、耗时且严重依赖隐性经验，难以系统自动化。

现有基于大语言模型（LLM）的RTL优化方法存在显著不足。在评估层面：它们通常在人为降级的小规模RTL设计上测试，起点不真实；依赖弱于工业标准的开源工具链，评估结果失真；且设计规模过小，无法反映实际工业设计的复杂性。在方法层面：现有方法主要依赖LLM代码检查，缺乏基于精细时序路径的EDA反馈指导；且局限于预定义的教科书式重写规则，这些规则在现代综合工具下往往无效，限制了非平凡优化策略的发现。

因此，本文要解决的核心问题是：如何在真实的工业评估环境中，实现有效且能持续自我改进的自主代理式RTL时序优化。具体而言，论文试图通过建立包含大规模人类编写RTL和工业EDA流程的评估环境，并设计一个基于工具、具备闭环优化和多智能体协作能力的框架（Dr. RTL），来克服现有方法的局限性。该框架不仅能通过关键路径分析和并行重写进行优化探索，还能通过“组相对技能学习”机制，从优化轨迹中提炼可重用、可解释的优化技能库，实现跨设计的知识复用与持续自我提升，最终在真实RTL设计上实现超越领先商业综合工具的PPA（性能、功耗、面积）优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。

在方法类研究中，RTLRewriter、SymRTLo、RTL-OPT、POET 和 CODMAS 等现有 LLM 驱动的 RTL 优化方法，通常依赖于单一的 LLM 进行规划，并采用预定义的、教科书式的重写规则。它们主要利用粗略的设计级 PPA 反馈（如整体时序和面积）来指导优化。本文提出的 Dr. RTL 与这些方法的核心区别在于：它采用了一个多智能体框架（包含协调器和子智能体）进行闭环优化，并引入了基于工具评估的细粒度关键路径分析来精准指导重写。更重要的是，本文提出了“群体相对技能学习”机制，能够从并行重写轨迹中自主提炼可重用、可解释的优化技能库，实现了持续的自我改进，而非依赖静态规则。

在应用与评测类研究中，现有工作大多在非现实的评测环境下进行，存在三大局限：使用人为降级的小规模 RTL 作为起点、依赖功能较弱的开源 EDA 工具链、以及测试设计规模极小。相比之下，本文建立了一个更贴近工业现实的评测环境：使用未经人为降级的、人类编写的原始 RTL 作为优化起点；采用工业级商业综合工具和时序等价性检查进行高保真评估；测试的设计规模（代码行数和模块数）比现有基准大一个数量级，更能反映真实设计的复杂性和关键路径行为。因此，本文旨在解决“真正的优化”问题，而非简单的“缺陷修复”。

### Q3: 论文如何解决这个问题？

论文通过一个名为Dr. RTL的自主智能体框架来解决现实RTL时序优化问题，其核心方法结合了闭环优化与基于群体相对性的技能学习机制。

整体框架采用多智能体架构，由编排器协调三个专门化智能体协同工作：时序分析智能体负责从综合后时序报告中识别关键路径瓶颈并进行根源分析；RTL优化智能体基于分析结果和累积的技能库，并行生成多个候选设计版本；评估智能体则执行商业综合流程和等价性检查，提供PPA和正确性反馈。这种分解实现了任务专精化、并行探索和模块化学习。

关键技术体现在两个方面。首先是闭环优化流程：系统从初始设计开始，在每个迭代中基于EDA工具反馈并行生成和评估N个候选设计，通过综合评分函数选择最佳且功能正确的设计进入下一轮，形成工具引导的搜索过程。其次是创新的群体相对技能学习机制：该方法通过比较同一优化上下文中并行生成的候选设计，计算相对优势信号来评估策略效果，而非依赖绝对PPA值。系统将优化轨迹组织为三层层次结构，从中提取可重用的模式-策略对作为优化技能存入知识库。模式捕捉关键路径上的结构瓶颈，策略描述相应的转换原则，并通过置信度机制持续更新。

主要创新点包括：建立了与现实工业EDA流程对接的评估环境；通过多智能体分解实现了与工具边界对齐的可靠优化；提出群体相对比较方法将噪声反馈转化为可靠学习信号；构建了可解释、可进化的技能库，目前包含47个模式-策略条目，支持跨设计重用以加速收敛。整个系统通过工具接地的自我改进，在优化质量和效率上实现持续提升。

### Q4: 论文做了哪些实验？

论文在真实的RTL时序优化场景下进行了全面的实验评估。实验设置方面，Dr. RTL采用一个多智能体框架进行闭环优化，包括关键路径分析、并行RTL重写和基于工具的评估。评估流程统一使用Synopsys Design Compiler和Nangate 45nm工艺库，在0.1ns的严格时钟周期约束下进行综合，并使用Cadence Jasper SEC进行功能等价性验证。每个设计运行10次迭代，每次迭代生成5个并行候选，总计50次优化尝试。

数据集为20个真实世界的人工编写Verilog设计，涵盖从缓冲区、处理器、信号处理模块到密码学设计和SoC的多种IP与系统，代码规模从128行到4615行不等，平均812行，具有复杂的功能和结构。

对比方法包括单次推理的大语言模型（Claude Opus和GPT 5.3）以及最先进的迭代式LLM优化基线方法（RTLRewriter和SymRTLo）。为确保公平，所有基线方法均使用与Dr. RTL相同的骨干模型（Claude Opus）和相同的迭代预算。

主要结果显示，Dr. RTL在20个设计上均实现了时序改进，平均WNS（最差负时序裕量）和TNS（总负时序裕量）分别改善了21.3%和16.9%，同时面积平均减少了5.8%。SEC（时序等价性检查）通过率平均达到86%。与基线相比，Dr. RTL显著优于单次LLM方法（如Claude Opus仅提升WNS 2.4%）和现有迭代方法（如RTLRewriter提升WNS 4.9%），证明了其框架的有效性。此外，通过四折交叉验证验证了其技能库（包含47个模式-策略条目）在未见设计上的泛化能力。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来可探索的方向包括：首先，当前方法主要聚焦于时序优化（WNS/TNS）和面积，对功耗的优化考虑相对简单（仅通过面积间接影响），未来可更深入地集成多目标权衡，甚至引入动态功耗分析。其次，技能库的构建依赖于组内相对比较，虽提升了可靠性，但可能受限于并行候选方案的数量和质量；可探索结合强化学习或贝叶斯优化，更主动地引导搜索方向，减少无效探索。此外，框架高度依赖工业EDA工具链进行验证，这虽保证了实用性，但也限制了其在不完全支持该流程的开源环境中的泛化能力；未来可研究如何适配开源工具（如Yosys），并验证其跨平台有效性。最后，当前技能模式偏重于RTL结构变换，未来可扩展至架构级优化（如流水线重组、存储器接口优化），并与高层次综合（HLS）结合，形成更完整的设计空间探索体系。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为Dr. RTL的自主智能体框架，旨在解决现有基于大语言模型（LLM）的RTL（寄存器传输级）自动优化方法在评估环境不现实、优化方法有限等方面的不足。其核心贡献在于建立了一个更贴近工业实际、更具挑战性的评估环境，并设计了一个具备持续自我改进能力的多智能体优化框架。

论文首先定义了现实RTL时序优化的问题，指出现有方法依赖人为降级的简单设计、弱开源工具以及粗粒度反馈和预定义重写规则的局限性。为解决此问题，Dr. RTL方法概述如下：1）构建一个包含工业EDA（电子设计自动化）流程的现实评估环境；2）采用多智能体框架进行闭环优化，包括关键路径分析、并行RTL重写和基于工具的评估；3）创新性地引入“组间相对技能学习”机制，通过比较并行重写结果，将优化经验提炼成可解释、可复用的技能库（包含47个模式-策略条目），该库支持跨设计重用并能持续进化。

主要结论是，在20个真实RTL设计上的评估表明，Dr. RTL相比业界领先的商业综合工具，平均实现了21%的WNS（最差负时序裕量）和17%的TNS（总负时序裕量）改善，同时面积减少了6%。这证明了该框架在现实场景下进行自主、持续RTL优化的有效性和潜力。
