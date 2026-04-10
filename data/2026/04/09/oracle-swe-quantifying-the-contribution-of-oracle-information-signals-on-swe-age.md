---
title: "ORACLE-SWE: Quantifying the Contribution of Oracle Information Signals on SWE Agents"
authors:
  - "Kenan Li"
  - "Qirui Jin"
  - "Liao Zhu"
  - "Xiaosong Huang"
  - "Yijia Wu"
  - "Yikai Zhang"
  - "Xin Zhang"
  - "Zijian Jin"
  - "Yufan Huang"
  - "Elsie Nallipogu"
  - "Chaoyun Zhang"
  - "Yu Kang"
  - "Saravan Rajmohan"
  - "Qingwei Lin"
  - "Wenke Lee"
  - "Dongmei Zhang"
date: "2026-04-09"
arxiv_id: "2604.07789"
arxiv_url: "https://arxiv.org/abs/2604.07789"
pdf_url: "https://arxiv.org/pdf/2604.07789v1"
categories:
  - "cs.MA"
  - "cs.CL"
  - "cs.SE"
tags:
  - "软件工程智能体"
  - "信息信号分析"
  - "性能评估"
  - "基准测试"
  - "大语言模型"
relevance_score: 7.5
---

# ORACLE-SWE: Quantifying the Contribution of Oracle Information Signals on SWE Agents

## 原始摘要

Recent advances in language model (LM) agents have significantly improved automated software engineering (SWE). Prior work has proposed various agentic workflows and training strategies as well as analyzed failure modes of agentic systems on SWE tasks, focusing on several contextual information signals: Reproduction Test, Regression Test, Edit Location, Execution Context, and API Usage. However, the individual contribution of each signal to overall success remains underexplored, particularly their ideal contribution when intermediate information is perfectly obtained. To address this gap, we introduce Oracle-SWE, a unified method to isolate and extract oracle information signals from SWE benchmarks and quantify the impact of each signal on agent performance. To further validate the pattern, we evaluate the performance gain of signals extracted by strong LMs when provided to a base agent, approximating real-world task-resolution settings. These evaluations aim to guide research prioritization for autonomous coding systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个关于语言模型（LM）代理在自动化软件工程（SWE）任务中性能提升的关键问题：在解决SWE任务时，多种上下文信息信号（如复现测试、回归测试、编辑位置、执行上下文和API使用）被广泛使用，但每种信号对任务成功的具体贡献程度尚不明确，尤其是在理想情况下（即能完美获取这些信号的“先知”信息时）它们各自的潜在影响上限未被量化。

研究背景是，随着语言模型编程能力日益复杂，评估重点已从单代码生成转向仓库级问题解决（如SWE-bench及其衍生基准）。现有方法包括各种代理工作流程和训练策略，并分析了代理在SWE任务中的失败模式，普遍依赖上述五种信息信号。然而，现有研究的不足在于，它们大多隐含地使用这些信号，但缺乏对这些信号个体贡献的系统性隔离和量化分析，特别是未能回答“如果这些信号能完美提供，系统性能可能提升多少”这一关键问题，这阻碍了针对性地优化自主编码系统的研究方向。

因此，本文要解决的核心问题是：量化每种“先知”信息信号对SWE代理性能的独立贡献上限，以指导未来研究的优先级。为此，论文提出了ORACLE-SWE方法，通过从SWE基准中提取先知信号并进行受控消融实验，测量每种信号对代理成功率的影响。此外，论文还通过让强LM代理实际提取这些信号并评估其贡献，验证了先知分析结论在现实任务解决中的适用性，从而为自主编码系统的改进提供了实证依据。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕自动化软件工程（SWE）中基于语言模型的智能体展开，可分为方法类、训练类和评测分析类。

**方法类**：大量工作聚焦于设计智能体工作流，将仓库探索结构化为多阶段流程。例如，Agentless、SWE-agent和OpenHands采用“定位-编辑-测试验证”的经典范式，使用基础工具（如shell命令）与仓库交互。闭源系统如Claude Code引入更高级的工具（如规划工具）和子任务委托机制。另一类研究则采用**多智能体或专门组件**的显式分解，如TDFlow将工作流分配给不同专职智能体。此外，许多方法通过构建**代码图**（结合仓库结构、AST和调用关系）来增强上下文理解，如MarsCode、Lingma Agent和GraphLocator。

**训练类**：部分研究直接训练语言模型执行SWE流程中的关键子任务（如问题定位、补丁生成、复现测试生成），通常采用监督微调（SFT）和强化学习（RL），例如SoRFT、SWE-RL和SWE-Swiss。近期工作转向利用完整的智能体轨迹进行训练，通过拒绝采样SFT或基于最终成功/失败的RL进行优化，如SkyRL。

**评测分析类**：越来越多的研究分析智能体在SWE任务中的失败模式。例如，SWE-agent使用GPT-4o对失败运行进行分类，指出复现、定位和代码生成等方面的错误。其他工作通过分析异常轨迹或评估日志，总结了代码生成问题、上下文理解不足及API误用等常见错误类别。

**本文与这些工作的关系和区别**：现有研究多集中于设计工作流、训练模型或分析失败模式，并普遍识别出影响成功的关键信息因素（如代码搜索相关的编辑位置、执行上下文、API使用，以及测试验证相关的复现测试和回归测试）。然而，**这些因素各自对整体成功的具体贡献尚未被深入量化**。本文提出的ORACLE-SWE方法，旨在**隔离和提取这些“预言机”信息信号，并量化每个信号对智能体性能的独立影响**，从而填补了这一空白，为未来自主编码系统的研发重点提供指导。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ORACLE-SWE的统一方法来解决量化各信息信号对软件工程（SWE）智能体性能贡献的问题。该方法的核心在于从SWE基准测试中隔离和提取“预言机”（oracle）信息信号，并量化每个信号对智能体性能的个体影响。

**整体框架与主要模块**：该方法首先定义了五个关键信息信号的“预言机”版本：编辑位置（Edit Location）、执行上下文（Execution Context）、API使用（API Usage）、复现测试（Reproduction Test）和回归测试（Regression Test）。系统的主要模块是**信息提取管道**，针对每个信号设计了专门的提取方法，从基准数据集和对应的代码仓库中获取近乎完美的中间信息。

**关键技术细节与创新点**：
1.  **编辑位置提取**：直接从黄金补丁中提取发生修改的代码区域，包括源代码片段，并标注文件路径、函数名和行号前缀。
2.  **执行上下文提取**：核心创新在于处理无法正常获取堆栈跟踪的情况。对于Python项目，通过在预言机编辑位置插入**自定义堆栈跟踪收集器**，在执行复现测试时记录最深可达的调用栈。对于Go项目，由于构建阶段经常失败，也主要依赖此自定义收集器来获取上下文。正常情况则从错误堆栈跟踪中提取，并屏蔽来自测试函数的帧以防止信息泄露。
3.  **API使用提取**：记录补丁中修改或新增的所有函数调用，包括函数名、参数、使用区域及函数定义。创新点在于针对动态类型（Python）和静态类型（Go）语言采用不同的定义解析方法：Python通过**执行覆盖率分析**来链接调用点与实现；Go则利用**类型检查、导入分析和参数签名**进行静态解析。
4.  **测试信号提取**：
    *   **复现测试**：提取执行命令、必须通过的测试列表及其完整源代码。一个关键设计是**有意应用测试补丁**，使智能体能够直接执行这些测试并基于错误输出迭代改进。
    *   **回归测试**：提取执行命令以及修复后必须保持通过的测试列表。
    测试函数的位置通过其名称推断，并使用基于AST的解析提取函数体。同时提供仅运行相关测试的命令，不支持选择性执行的实例则被排除。

**方法创新性**：该工作的主要创新在于系统性地构建了一套提取“完美”中间信息的自动化流程，从而能够在受控环境下隔离并量化每个信息信号的理想贡献。这为评估智能体在真实任务解决场景中的性能提升提供了基准，并旨在指导自主编码系统研究的优先级排序。

### Q4: 论文做了哪些实验？

本论文的实验设计旨在量化五个关键信息信号（Reproduction Test, Regression Test, Edit Location, Execution Context, API Usage）对软件工程（SWE）智能体性能的贡献。实验设置分为两个主要部分：上限贡献消融研究和两阶段验证实验。

**实验设置与数据集**：
研究采用**SWE-agent**作为基础智能体，其工具接口仅限于bash命令和字符串替换编辑器，最大步数限制为120步，以避免复杂系统设计带来的混淆效应。实验在三个数据集上进行：**SWE-bench-Verified**（459个实例）、**SWE-bench-Live**的已验证Python子集（353个实例）以及**SWE-bench-Pro**的Python（220个实例）和Golang（211个实例）子集。为确保任务可行性，过滤了补丁失败或测试无法选择性执行的实例。

**对比方法与主要结果**：
1.  **上限贡献消融研究**：通过将真实（oracle）信号单独或组合注入初始用户提示，模拟理想信息获取场景，测量各信号对成功率的贡献。关键指标为**成功率**和相应的**LM API成本**。结果表明，不同信号对性能提升有显著差异，组合注入可逼近性能上限。
2.  **两阶段验证实验**：为评估信号在实际条件下的可获取性及贡献，设计了两个阶段。**Stage 1**使用强模型（如GPT-5或Claude-4.6-Sonnet）提取各信号；**Stage 2**使用弱模型（如GPT-4o或GPT-5）利用提取的信号解决问题。两阶段共享120步的总预算（分配50步用于提取，70步用于解决）。基线是单独使用强模型或弱模型的单智能体设置。理想情况下，两阶段流水线应优于弱模型，并接近强模型的性能。实验评估了不同模型组合在多个数据集上的表现，以验证发现的普适性。

**关键数据指标**：
- 数据集规模：Verified (459), Live (353), Pro/Python (220), Pro/Golang (211)。
- 步数分配：提取阶段50步，解决阶段70步（总计120步）。
- 模型对比：涉及GPT-5、GPT-4o、Claude-4.5-Sonnet、Claude-4.6-Sonnet等。
- 执行上下文获取：部分任务使用原生错误堆栈跟踪（Verified: 159, Live: 72, Pro/Python: 50），其余使用自定义堆栈跟踪收集器；Golang任务全部依赖自定义收集器。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性及摘要中对“理想贡献”的探讨，未来研究可从以下几个方向深入探索：

首先，**信息信号的扩展与精细化分解**。当前研究选取的五类信号（如回归测试、编辑位置等）是基于已有观察的主观归纳，并非穷尽。未来可系统性地挖掘更多潜在的关键信息信号（例如代码变更意图、依赖关系、用户历史行为），并建立更客观、可量化的分类体系，以更全面地揭示各类信息对智能体性能的真实贡献。

其次，**研究方法的深化与实际应用迁移**。论文通过“Oracle”方法在理想条件下量化信号贡献，但现实任务中信息往往不完美或存在噪声。未来工作可探索在非理想、渐进式信息获取场景下，如何动态评估信号的边际效益，并研究如何让基础智能体（而非仅依靠外部强模型）自主、高效地提取和利用这些关键信号，以提升其在真实软件开发环境中的实用性。

最后，**信号间的交互作用与协同机制**。当前研究侧重于隔离分析单个信号的贡献，但实际解决问题时，多种信号可能以非线性方式协同作用。未来可探究信号之间的互补、冗余甚至冲突关系，并据此设计更智能的信息融合与决策策略，从而优化智能体的整体工作流和架构设计。

### Q6: 总结一下论文的主要内容

该论文针对软件工程（SWE）智能体研究中未充分探索的问题，即五种常见上下文信息信号在理想化（完美获取）状态下对任务成功的个体贡献度，提出了ORACLE-SWE方法进行量化分析。核心贡献在于设计了一种统一框架，能从SWE基准测试中隔离并提取这些“预言机”（oracle）信息信号，从而精确评估每个信号的潜在影响力。方法概述是通过构建预言机信号来模拟完美信息条件，并进一步用强语言模型提取近似信号提供给基础智能体，以验证其在现实任务解决中的性能增益。主要结论有三点：一是高质量、能捕捉边界情况的复现测试是最具影响力的信号；二是执行上下文（如代码图）仅在错误堆栈跟踪可用时（仅占实例的四分之一）才显著有效；三是编辑位置和API使用信号在彼此配对或与复现测试结合时效果会显著提升。这项研究的意义在于为自主编码系统的研发优先级提供了数据驱动的指导。
