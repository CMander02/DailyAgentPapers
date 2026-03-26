---
title: "The Specification Gap: Coordination Failure Under Partial Knowledge in Code Agents"
authors:
  - "Camilo Chacón Sartori"
date: "2026-03-25"
arxiv_id: "2603.24284"
arxiv_url: "https://arxiv.org/abs/2603.24284"
pdf_url: "https://arxiv.org/pdf/2603.24284v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.MA"
tags:
  - "Multi-Agent Collaboration"
  - "Code Agent"
  - "Specification"
  - "Coordination Failure"
  - "Evaluation"
  - "LLM-based Agent"
relevance_score: 7.5
---

# The Specification Gap: Coordination Failure Under Partial Knowledge in Code Agents

## 原始摘要

When multiple LLM-based code agents independently implement parts of the same class, they must agree on shared internal representations, even when the specification leaves those choices implicit. We study this coordination problem across 51 class-generation tasks, progressively stripping specification detail from full docstrings (L0) to bare signatures (L3), and introducing opposing structural biases (lists vs. dictionaries) to stress-test integration. Three findings emerge. First, a persistent specification gap: two-agent integration accuracy drops from 58% to 25% as detail is removed, while a single-agent baseline degrades more gracefully (89% to 56%), leaving a 25--39 pp coordination gap that is consistent across two Claude models (Sonnet, Haiku) and three independent runs. Second, an AST-based conflict detector achieves 97% precision at the weakest specification level without additional LLM calls, yet a factorial recovery experiment shows that restoring the full specification alone recovers the single-agent ceiling (89%), while providing conflict reports adds no measurable benefit. Third, decomposing the gap into coordination cost (+16 pp) and information asymmetry (+11 pp) suggests that the two effects are independent and approximately additive. The gap is not merely a consequence of hidden information, but reflects the difficulty of producing compatible code without shared decisions. These results support a specification-first view of multi-agent code generation: richer specifications are both the primary coordination mechanism and the sufficient recovery instrument.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究多智能体代码生成中的协调失败问题，尤其关注在部分知识条件下，多个基于大语言模型的代码智能体在协作实现同一类时，因缺乏明确的共享决策而导致的集成兼容性下降。研究背景是，当前大语言模型在单智能体代码生成任务中表现优异，但扩展到多智能体协作时，若将类的实现分解给不同智能体独立完成，它们必须就类的内部共享状态（如构造函数中初始化的数据结构）达成一致，而规格说明往往对此未作明确定义，从而引发协调问题。

现有方法的不足在于，尽管传统软件工程通过精确的模块接口规格来解决协调问题，但对于代码智能体而言，“足够精确”的标准尚不明确。现有研究多集中于提升单智能体性能或简单的任务分解，缺乏对多智能体在规格说明不完整时协调失败的系统性分析，尤其忽略了因结构偏见（如一个智能体偏好列表、另一个偏好字典）导致的集成不兼容错误。

本文要解决的核心问题是：当多个代码智能体基于不完整的规格说明独立实现同一类的不同方法时，如何量化协调失败的程度，并探究其根本原因。论文通过设计控制实验，逐步剥离规格说明细节（从完整文档字符串到仅有方法签名），并引入对立的结构偏见来压力测试集成，从而实证研究规格说明完整性对多智能体集成成功率的影响，揭示协调成本与信息不对称的独立作用，并评估冲突检测与规格恢复等干预措施的有效性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多智能体代码生成系统、软件工程规范理论，以及代码生成评估与静态分析。

在多智能体代码生成系统方面，MetaGPT、ChatDev和CodeAgent等研究探索了通过角色分配、聊天交互或工具集成来实现协作。近期工作进一步引入了自适应规划、模拟调试和基于Git的协作。这些系统展示了多智能体协作的潜力，但并未深入探究**规范完整性如何具体影响协调**。本文通过控制实验，将规范完整性作为单一变量进行操纵，从而**补充和深化**了这类研究，旨在隔离并量化“规范缺口”对协调的影响。

在软件工程规范理论方面，Parnas关于模块化分解需要精确接口的论述，以及Meyer的“契约式设计”原则，都强调了规范作为独立开发模块间的协调契约。康威定律则指出系统结构反映组织沟通结构。本文将这些经典理论**应用于多智能体LLM系统**，实证检验了规范质量是否以及如何预测独立智能体产出兼容代码的程度。

在评估与静态分析方面，HumanEval和MBPP评估单函数生成，ClassEval则扩展至具有方法间依赖的类级生成，为研究多智能体协调提供了基础。本文的基准测试AmbigClass正是基于ClassEval构建。同时，传统软件工程中类型冲突检测、合并冲突检测等静态分析技术被**适配应用于LLM生成的代码**，本文使用基于AST的分析来检测智能体输出间的类型不匹配和状态访问冲突，为协调失败提供了高效的检测工具。

### Q3: 论文如何解决这个问题？

论文通过一个精心设计的实验来探究和解决多智能体代码生成中的协调失败问题，其核心方法是控制变量以量化“规范缺口”并测试恢复策略。

**整体框架与实验设计**：研究构建了一个名为AmbigClass的基准，包含51个任务（源自ClassEval）和四个逐步简化的规范级别（L0到L3）。实验设置了两种主要条件：1) **单智能体基线**：一个无偏见的智能体接收完整的类骨架（包括 `__init__` 方法），作为性能上限。2) **拆分智能体条件**：两个带有对立结构偏好的智能体（一个偏好列表，一个偏好字典）分别接收隐藏了 `__init__` 方法的类骨架，并独立实现互不相交的方法子集，然后对它们的输出进行简单的文本合并。通过比较这两种条件在不同规范级别下的集成成功率，可以分离出由规范不完整导致的协调失败。

**主要模块与关键技术**：
1.  **规范级别控制**：这是核心变量。L0包含完整的文档字符串、示例和数据结构引用；L3仅保留方法签名。关键过渡在L1和L2之间，L1及之前级别明确提及数据结构（如“列表”），而L2/L3使用抽象语言，迫使智能体进行推断。
2.  **对立偏见引入**：为两个拆分智能体植入对立的结构偏好（列表 vs. 字典），这作为一个受控代理，模拟了开发者在没有明确共享决策时可能出现的隐性设计分歧，从而放大并可靠地引发协调冲突。
3.  **AST冲突检测器**：这是一个独立的分析模块，用于在集成前分析两个智能体输出的抽象语法树（AST），检测类型、状态和协议冲突，以提供协调失败的客观信号。
4.  **因子恢复实验**：为了测试恢复策略，研究在L3（最弱规范）下进行了一个2x2因子实验。变量是合并智能体接收的信息：**规范级别**（L3 vs. L0）和**冲突报告**（有 vs. 无）。这产生了四种合并条件（如“仅规范”、“解析”等），用以评估不同信息对恢复的贡献。

**创新点**：
- **量化“规范缺口”**：研究不仅展示了多智能体集成成功率随规范简化而急剧下降（从58%到25%），并与单智能体更平缓的下降（89%到56%）对比，从而精确定义了高达25-39个百分点的“协调缺口”。
- **分解失败原因**：通过实验设计，将协调失败分解为**协调成本**（+16个百分点，源于独立决策的困难）和**信息不对称**（+11个百分点，源于规范隐藏的信息）两个近似独立的可加效应。
- **确立规范的充分性**：恢复实验的关键发现是，仅向合并智能体**提供完整规范（L0）** 就足以将性能恢复到单智能体上限（89%），而**额外提供冲突报告并未带来可测量的收益**。这强有力地支持了“规范优先”的观点：更丰富的规范本身既是主要的协调机制，也是从协调失败中恢复的充分工具。AST检测器虽能高精度（97%）识别冲突，但无法替代完整规范在协调中的根本作用。

### Q4: 论文做了哪些实验？

论文实验围绕四个研究问题展开。实验设置方面，研究者构建了51个类生成任务，并设计了四种逐步简化的规范级别：L0（完整文档字符串，包含数据结构和用法示例）、L1（移除示例）、L2（移除数据结构引用）、L3（仅方法签名）。同时，通过引入对立的结构性偏见（如列表 vs. 字典）来测试集成鲁棒性。主要对比了两种代理条件：单代理（Single，生成完整类）和拆分代理（Split，两个代理独立实现类的不同部分后再集成）。

数据集/基准测试基于这51个任务，通过单元测试通过率（Test Pass Rate）和AST检测到的冲突数量（Conflicts）来评估性能。关键数据指标包括：在L0级别，单代理测试通过率为88.6%，拆分代理为58.2%，存在30.4个百分点的差距（Gap）；到L3级别，单代理降至55.8%，拆分代理降至24.6%，差距为31.3个百分点。AST冲突检测器在L3级别的精确度达到96.7%。恢复实验采用2x2因子设计，发现仅提供完整规范（Spec-Only）可使合并代理的通过率达到88.9%，与单代理天花板（88.3%）相当，而提供冲突报告在弱规范下无改善，在完整规范下甚至有轻微负面影响（-6.6个百分点）。结果表明，规范完整性是成功的关键，且多代理协调存在固有成本。

### Q5: 有什么可以进一步探索的点？

该论文揭示了在多智能体代码生成中，由于规范不完整导致的协调失败问题，但仍存在多个可深入探索的方向。首先，研究局限于类生成任务，未来可扩展至更复杂的系统架构或微服务协调场景，考察动态交互下的协调机制。其次，实验仅使用Claude模型，需验证不同模型家族（如GPT、Gemini）或开源模型是否表现出类似模式，以及模型规模对协调能力的影响。第三，当前冲突检测基于AST，但未探索语义层面的不一致性（如算法逻辑冲突），可结合形式化方法或轻量级定理证明提升检测深度。此外，论文发现冲突报告未能提升恢复效果，这可能源于报告形式或智能体利用能力的限制，未来可设计结构化协调协议（如共识算法或共享记忆），让智能体主动协商而非被动接收信息。最后，可探索“增量规范”范式，即智能体在生成过程中逐步提炼并共享隐式决策，从而缩小规范缺口。

### Q6: 总结一下论文的主要内容

这篇论文研究了基于LLM的代码智能体在多智能体协作生成代码时面临的“规范缺口”问题。当多个智能体在没有明确共享决策的情况下，独立实现同一类的不同部分时，它们必须在内部表示（如数据结构）上达成一致，即使规范中对此是隐含的。作者通过51个类生成任务进行实验，逐步减少规范细节（从完整文档L0到仅有签名的L3），并引入对立的结构偏好（列表vs字典）来测试集成。

核心贡献与发现有三点：
1.  **揭示了显著的协调失败**：随着规范细节减少，双智能体集成准确率从58%骤降至25%，而单智能体基线下降更平缓（89%到56%），两者间存在25-39个百分点的稳定“协调缺口”，这在不同模型和多次运行中均一致存在。
2.  **评估了冲突检测与恢复方法**：基于AST的冲突检测器在最低规范级别下能达到97%的精确度且无需额外LLM调用。然而，恢复实验表明，仅恢复完整规范就足以使性能达到单智能体上限（89%），而提供冲突报告并无额外收益。
3.  **量化并分解了缺口成因**：将协调缺口分解为协调成本（+16个百分点）和信息不对称（+11个百分点），表明这两种效应是独立且近似可加的。问题根源不仅是信息隐藏，更在于缺乏共享决策时生成兼容代码的固有难度。

论文意义在于强调了“规范优先”的多智能体代码生成观：更丰富的规范既是主要的协调机制，也是充分的恢复工具，为解决多智能体协作中的协调失败提供了关键见解。
