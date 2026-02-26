---
title: "Structurally Aligned Subtask-Level Memory for Software Engineering Agents"
authors:
  - "Kangning Shen"
  - "Jingyuan Zhang"
  - "Chenxi Sun"
  - "Wencong Zeng"
  - "Yang Yue"
date: "2026-02-25"
arxiv_id: "2602.21611"
arxiv_url: "https://arxiv.org/abs/2602.21611"
pdf_url: "https://arxiv.org/pdf/2602.21611v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "记忆"
  - "软件工程智能体"
  - "长程推理"
  - "任务分解"
  - "检索增强"
relevance_score: 9.0
---

# Structurally Aligned Subtask-Level Memory for Software Engineering Agents

## 原始摘要

Large Language Models (LLMs) have demonstrated significant potential as autonomous software engineering (SWE) agents. Recent work has further explored augmenting these agents with memory mechanisms to support long-horizon reasoning. However, these approaches typically operate at a coarse instance granularity, treating the entire problem-solving episode as the atomic unit of storage and retrieval. We empirically demonstrate that instance-level memory suffers from a fundamental granularity mismatch, resulting in misguided retrieval when tasks with similar surface descriptions require distinct reasoning logic at specific stages. To address this, we propose Structurally Aligned Subtask-Level Memory, a method that aligns memory storage, retrieval, and updating with the agent's functional decomposition. Extensive experiments on SWE-bench Verified demonstrate that our method consistently outperforms both vanilla agents and strong instance-level memory baselines across diverse backbones, improving mean Pass@1 over the vanilla agent by +4.7 pp on average (e.g., +6.8 pp on Gemini 2.5 Pro). Performance gains grow with more interaction steps, showing that leveraging past experience benefits long-horizon reasoning in complex software engineering tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为自主软件工程（SWE）智能体时，在利用记忆机制进行长程推理时所面临的核心问题：现有基于实例级（instance-level）的记忆方法存在粒度不匹配的缺陷，导致经验检索不精确，从而影响复杂任务解决的效率与效果。

研究背景是，LLM在软件工程任务（如修复代码库问题）中展现出巨大潜力，这类任务通常需要多轮交互并遵循结构化的子任务工作流（如分析问题、定位错误、编辑代码等）。为了支持长程推理，近期研究开始为智能体引入记忆机制，使其能够学习和重用过往经验。然而，现有方法大多采用粗粒度的实例级记忆，即将整个问题解决过程（一个“事件”）作为存储和检索的基本单元。这种方法严重依赖全局任务相似性（例如基于整体问题描述的相似度）来检索历史经验。

现有方法的不足在于，这种粗粒度的设计与软件工程任务固有的组合性本质不匹配，导致了“粒度不匹配”问题。具体表现为两种失败模式：1）当两个任务表面描述相似但实际在特定解决阶段需要完全不同的推理逻辑时（例如“修复登录按钮”和“修复登录超时”），基于全局相似性的检索会引入误导性的无关经验；2）当两个任务全局上不相似，但在某个具体子任务（如“更新前端事件监听器”）上共享可复用技能时，实例级记忆又会因全局相似度低而无法检索到这些有价值的局部经验。

因此，本文要解决的核心问题是：如何使智能体的记忆机制与其推理过程的功能分解结构对齐，从而实现更精准、更有效的经验复用。为此，论文提出了“结构对齐的子任务级记忆”方法，将记忆的存储、检索和更新操作与智能体分解出的离散子任务（如分析、编辑等）粒度对齐，通过细粒度的、基于子任务类别和意图的检索策略，来克服实例级记忆的局限性，最终提升智能体在复杂软件工程长程任务中的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：软件工程领域的LLM智能体和智能体的记忆机制。

在**软件工程LLM智能体**方面，相关研究致力于提升大模型解决实际编程问题的能力。例如，SWE-bench基准测试系统评估了模型解决真实GitHub问题的能力，揭示了与工程实践的差距。为应对挑战，SWE-agent等工作设计了智能体-计算机接口，而其他研究则探索了分层规划、交互式平台、静态工作流或基于搜索的管道等方法。尽管取得进展，现有智能体在处理长程推理和跨文件依赖时，仍面临长上下文利用不均和短期记忆瓶颈的问题。

在**智能体记忆机制**方面，相关研究旨在通过结构化组件捕获过往交互中的有效策略。在软件工程场景中，一类工作将先前的智能体轨迹提炼为可重用的经验或“课程”；另一类则从项目制品（如提交历史）构建与仓库锚定的持久记忆，以辅助代码定位和长程调试。此外，还有研究关注记忆治理与可扩展性。然而，这些方法大多在**实例/片段**或**仓库/全局**的粗粒度上运作，主要依赖全局相似性进行检索，可能导致跨阶段噪声或遗漏可重用的阶段特定技能。

**本文与这些工作的关系和区别在于**：本文同样关注增强软件工程智能体的记忆能力，但明确指出并致力于解决现有**实例级记忆**存在的**粒度不匹配**根本问题。为此，本文提出了**结构对齐的子任务级记忆**，其核心区别在于：（1）将记忆单元从整个问题解决片段转移到**细粒度的子任务经验**；（2）通过从已完成的子任务中抽象出可操作的经验来**在线更新记忆**，从而直接将记忆的存储、检索和更新与智能体的功能分解结构对齐，以支持更精准的长程推理。

### Q3: 论文如何解决这个问题？

论文通过提出一种结构对齐的子任务级记忆方法来解决实例级记忆在软件工程任务中存在的粒度不匹配问题。该方法的核心思想是将记忆的存储、检索和更新与智能体的功能分解对齐，即以分解后的子任务单元而非整个任务轨迹作为记忆操作的基本单位。

整体框架是一个记忆增强的智能体工作流，其核心模块包括子任务定义、记忆状态、检索函数和更新函数。首先，智能体将解决软件工程任务的过程分解为一系列功能对齐的子任务。每个子任务被形式化为一个三元组 φ^(k) = (z^(k), d^(k), π^(k))，其中 z^(k) 代表功能类别（如分析、复现、编辑、验证），d^(k) 是结构化的描述（包含目标和关键词），π^(k) 是对应的执行轨迹段。这种结构化描述将局部推理需求与全局任务描述解耦。

记忆机制的具体实现包含三个关键技术环节：
1.  **记忆检索**：采用分层策略。在启动每个子任务时，首先进行基于类别的过滤，仅检索与当前子任务类别 z^(k) 匹配的记忆条目，这确保了结构对齐并缩小了搜索空间。随后在过滤后的候选集中，通过计算当前子任务描述 d^(k) 与存储的描述 m.d 之间的语义相似度（使用固定的嵌入模型）来选取最相关的记忆条目 m*。检索到的经验内容 m*.e 被注入到子任务的初始上下文中，为智能体提供相关知识。
2.  **记忆更新**：在每个子任务完成后执行结构化的更新。首先，通过一个基于LLM的经验提取器 E 对子任务轨迹 π^(k) 进行提炼，评估其正确性，并过滤掉仓库特定的噪声，提取出可转移的经验 e^(k)（包括成功模式或失败规避策略）。然后，将子任务意图 (z^(k), d^(k)) 与提取的经验 e^(k) 组合成新的记忆条目 m_new，并将其添加到记忆状态 S_sub 中。
3.  **自主子任务分割**：通过一种面向转换的分割策略，将过渡逻辑集成到系统提示中，使智能体能够在完成一个推理阶段（子任务k）后，自主预测下一个功能类别 z^(k+1) 并合成相应的描述 d^(k+1)。这种方法将分割直接编织到智能体的标准推理流中，引入了最小的架构开销。

该方法的创新点在于首次将记忆机制与智能体的推理过程在功能粒度上对齐，通过结构化的子任务定义和分层检索策略，有效解决了因任务表面描述相似但阶段推理逻辑不同而导致的误导性检索问题，从而显著提升了智能体在复杂软件工程任务中长期推理的性能。

### Q4: 论文做了哪些实验？

论文在SWE-bench Verified基准上进行了广泛的实验，这是一个包含500个真实GitHub问题的严格基准。实验采用Pass@1作为核心指标，衡量智能体单次尝试生成正确补丁的百分比。所有方法均在Mini SWE Agent框架上实现，使用贪婪解码（温度=0）以最小化随机性，并确保非内存配置（如执行环境、步骤限制）完全一致。

实验对比了三种方法：1）无记忆的Vanilla Agent；2）基于全局语义相似性存储和检索实例级推理摘要的Instance-level Memory基线（复现ReasoningBank）；3）论文提出的Structurally Aligned Subtask-Level Memory方法。为了验证鲁棒性，实验在四个骨干LLM上进行评估：Gemini 2.5 Flash、Gemini 2.5 Pro、Claude 3.7 Sonnet和Claude 4.0 Sonnet。所有实验遵循测试时流式协议，内存初始为空并在线累积经验。为减轻顺序影响，使用不同随机种子对500个实例的执行序列进行三次独立打乱运行，报告平均Pass@1（均值±标准差）以及Best@3（三次中的最佳运行）作为上限。

主要结果显示，提出的方法在所有骨干模型上均一致优于Vanilla Agent和Instance-level Memory基线。平均Pass@1提升+4.7个百分点（pp），具体提升幅度因模型而异，例如在Gemini 2.5 Pro上提升+6.8 pp，在Gemini 2.5 Flash上提升+5.6 pp，在Claude 4.0 Sonnet上提升+2.3 pp。关键发现包括：1）Instance-level Memory在Claude模型上表现不稳定（如Claude 3.7 Sonnet性能从52.2%降至51.1%，且方差高达±2.27），而提出的方法有效稳定了方差（如将Claude 3.7 Sonnet的σ从2.27降至1.33）；2）性能增益随交互步骤增加而增长，表明该方法能有效支持长视野推理；3）消融实验证实了结构化分解、类别隔离和抽象提取操作的必要性，其中仅使用结构化提示仅带来+1.0%的微小提升，而完整方法带来+3.9%的显著提升；4）按任务复杂度分析显示，该方法在困难任务（>28步）上带来+8.7%的显著提升（从35.5%至44.2%），而在简单任务上提升有限（+1.8%），表明其能有效为复杂推理提供计算捷径。

### Q5: 有什么可以进一步探索的点？

本文提出的子任务级记忆方法虽有效，但仍有局限。首先，其依赖于预设的功能分解结构，这可能限制了在更开放或动态任务中的泛化能力。未来可探索自适应或学习型的任务分解机制，使记忆结构能随任务演进动态调整。其次，实验集中于软件工程领域，其有效性在其他需长程推理的领域（如科学发现或复杂规划）尚待验证。此外，记忆的检索与更新效率在极长序列中可能成为瓶颈，需研究更高效的索引或压缩技术。结合见解，可考虑引入元学习，使智能体不仅能记忆具体经验，还能学习何时及如何复用策略，从而提升跨任务迁移能力。同时，探索多模态记忆（如结合代码、自然语言与执行轨迹）可能进一步丰富经验表示，增强复杂场景下的推理鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型作为自主软件工程代理时，现有记忆机制在粒度上不匹配的问题展开研究。当前方法通常将整个问题解决过程作为存储和检索的原子单元，但作者通过实证发现，这种实例级记忆在面对表面描述相似但具体阶段推理逻辑不同的任务时，会导致误导性检索。

为解决这一问题，论文提出了“结构对齐的子任务级记忆”方法。其核心贡献在于将记忆的存储、检索和更新过程与智能体的功能分解对齐，即根据任务的结构化子步骤来组织记忆，而非整个任务实例。这种方法确保了在复杂软件工程任务的长程推理中，智能体能够更精准地利用过往经验。

在SWE-bench Verified基准上的大量实验表明，该方法在不同模型骨干上均稳定优于原始智能体和强实例级记忆基线，平均将平均Pass@1提升了4.7个百分点（例如在Gemini 2.5 Pro上提升6.8个百分点）。主要结论是，随着交互步骤增加，性能增益更为显著，这验证了所提方法能有效利用历史经验，从而提升复杂软件工程任务中长程推理的能力。
