---
title: "EffiSkill: Agent Skill Based Automated Code Efficiency Optimization"
authors:
  - "Zimu Wang"
  - "Yuling Shi"
  - "Mengfan Li"
  - "Zijun Liu"
  - "Jie M. Zhang"
  - "Chengcheng Wan"
  - "Xiaodong Gu"
date: "2026-03-29"
arxiv_id: "2603.27850"
arxiv_url: "https://arxiv.org/abs/2603.27850"
pdf_url: "https://arxiv.org/pdf/2603.27850v1"
categories:
  - "cs.SE"
  - "cs.CL"
tags:
  - "Code Agent"
  - "Agent Skill"
  - "Knowledge Distillation"
  - "Tool Use"
  - "Execution-Free Optimization"
  - "Agent Planning"
  - "Software Engineering"
relevance_score: 8.0
---

# EffiSkill: Agent Skill Based Automated Code Efficiency Optimization

## 原始摘要

Code efficiency is a fundamental aspect of software quality, yet how to harness large language models (LLMs) to optimize programs remains challenging. Prior approaches have sought for one-shot rewriting, retrieved exemplars, or prompt-based search, but they do not explicitly distill reusable optimization knowledge, which limits generalization beyond individual instances.
  In this paper, we present EffiSkill, a framework for code-efficiency optimization that builds a portable optimization toolbox for LLM-based agents. The key idea is to model recurring slow-to-fast transformations as reusable agent skills that capture both concrete transformation mechanisms and higher-level optimization strategies. EffiSkill adopts a two-stage design: Stage I mines Operator and Meta Skills from large-scale slow/fast program pairs to build a skill library; Stage II applies this library to unseen programs through execution-free diagnosis, skill retrieval, plan composition, and candidate generation, without runtime feedback.
  Results on EffiBench-X show that EffiSkill achieves higher optimization success rates, improving over the strongest baseline by 3.69 to 12.52 percentage points across model and language settings. These findings suggest that mechanism-level skill reuse provides a useful foundation for execution-free code optimization, and that the resulting skill library can serve as a reusable resource for broader agent workflows.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用大语言模型（LLM）进行代码效率优化时，现有方法难以提炼和复用可重用优化知识的问题。研究背景是代码效率作为软件质量的基本要素至关重要，而传统的基于人工规则的优化方法覆盖范围有限且需要大量专家投入。近期，基于LLM的数据驱动方法（如提示、检索增强或基于搜索的优化）展现出潜力，但它们存在核心不足：这些方法主要在单个实例层面操作，无论是“一次性重写”还是依赖检索示例的搜索方法，都未能将反复出现的优化模式显式地提炼为可迁移、可重用的知识。这导致优化知识被束缚于具体实例，限制了其泛化到新程序的能力，并且难以处理需要多步结构化推理的复杂优化。

因此，本文要解决的核心问题是：如何超越对单个优化实例的处理，构建一个可移植、可重用的优化知识库，以系统化地提升LLM代理在代码效率优化任务中的泛化能力和效果。为此，论文提出了EffiSkill框架，其核心思想是将反复出现的“慢到快”代码转换建模为可重用的“代理技能”，这些技能既包含具体的转换机制，也包含更高层的优化策略。该框架采用两阶段设计：第一阶段从大规模的慢/快程序对中挖掘“操作技能”和“元技能”以构建技能库；第二阶段将该技能库应用于未见程序，通过免执行的诊断、技能检索、计划组合和候选生成来完成优化，无需运行时反馈。最终目标不仅是提升优化成功率，更是创建一个可作为即插即用工具箱的结构化技能库，为更广泛的智能体工作流提供可复用的优化资源。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。

在方法类方面，相关工作主要围绕利用大语言模型（LLM）进行代码优化。先前的方法包括：1）**一次性重写**，即直接提示LLM生成优化版本；2）**基于检索的范例**，通过检索相似的低效代码及其优化版本来指导生成；3）**基于提示的搜索**，通过迭代提示或搜索来探索优化空间。然而，这些方法侧重于处理单个实例，未能显式地提炼出可复用的优化知识，从而限制了其泛化能力。EffiSkill与这些工作的核心区别在于，它明确地将反复出现的“慢到快”转换模式建模为**可复用的智能体技能**，构建了一个可移植的优化工具箱。这超越了基于实例或提示的方法，实现了机制层面的知识抽象和复用。

在应用类方面，相关工作涉及**基于智能体的代码生成与优化框架**。近期研究将技能概念化为封装任务指令、工具使用模式和辅助资源的模块化单元，以提升LLM系统的模块化和组合性。例如，工具增强的语言模型学习调用外部函数，智能体框架交织推理与行动以构建多步解决方案。EffiSkill与这些工作的关系在于，它借鉴了智能体技能和模块化设计的理念，但将其专门化到代码效率优化领域。其独特之处在于将技能进一步区分为**操作技能**（编码具体的转换机制）和**元技能**（编码高层控制逻辑，如诊断、检索和组合），从而形成了一个结构化的、可执行的技能库，支持无需执行反馈的优化流程。这为更广泛的智能体工作流提供了可复用的资源基础。

### Q3: 论文如何解决这个问题？

EffiSkill 通过构建一个可移植的优化工具箱来解决代码效率优化问题，其核心是将反复出现的慢到快转换模式建模为可复用的智能体技能。该方法采用两阶段设计，将优化知识的学习与应用解耦。

**整体框架与主要模块：**
框架分为技能挖掘（Stage I）和技能引导优化（Stage II）两个阶段。Stage I 从大量慢/快程序对中离线挖掘并构建一个技能库，该库包含两种互补的技能：**操作技能** 和 **元技能**。操作技能编码了具体的转换机制（如算法替换、状态压缩、常数因子优化）及其适用条件和预期效果；元技能则作为过程控制器，指导在优化过程中如何选择、组合和执行操作技能。Stage II 将技能库应用于新程序，其流程包括：1) **诊断**：分析问题陈述和基线解决方案，生成结构化摘要以识别瓶颈和优化范围；2) **技能检索**：基于诊断结果，检索多组（例如3组）可能的操作技能集合，代表不同的优化路径；3) **计划组合**：对于每个检索到的技能包，元技能将其组合成2到3个具体的优化计划，每个计划都明确了转换策略、预期效率提升和风险；4) **候选生成**：根据组合出的计划，生成优化后的代码候选，同时保持原始程序接口和预期行为。

**关键技术：**
在技能挖掘阶段，关键技术包括：1) **跟踪提取**：使用大语言模型从慢/快程序对中生成结构化的优化跟踪，包含问题摘要、慢速审计、快速审计和差异总结；2) **签名抽象**：将每个跟踪抽象为紧凑的签名，总结转换机制的类型、复杂度变化、触发条件等；3) **混合聚类与技能提炼**：在结合了TF-IDF（词频-逆文档频率）特征和句子嵌入的混合语义空间中对签名进行聚类，自动估计聚类数量，并将每个聚类提炼为一个操作技能；4) **技能库构建**：对高度相似的操作技能进行合并，并基于操作技能库归纳出元技能。

**创新点：**
主要创新在于：1) **显式提炼可复用的优化知识**：不同于以往的一次性重写或基于提示的搜索，EffiSkill 从大量实例中蒸馏出机制层面的、可迁移的优化技能，提升了泛化能力。2) **执行无关的优化流程**：整个优化过程（诊断、检索、计划、生成）不依赖运行时的迭代反馈，提高了效率和适用性。3) **多路径探索**：通过检索多组技能并组合成多个计划，系统性地探索多种合理的优化路线，避免了过早锁定单一方案而限制搜索空间。4) **技能的双层结构**：操作技能提供具体的转换“武器”，而元技能提供如何运用这些武器的“战术”，两者结合形成了一个完整、可复用的优化工具箱。

### Q4: 论文做了哪些实验？

论文在EffiBench-X基准上进行了全面的实验评估，主要涵盖四个研究问题。

**实验设置与数据集**：实验使用EffiBench-X基准的Python和C++子集，包含623个优化任务，输入为专家编写的规范解决方案。评估采用公开/私有测试划分（20%/80%），每个任务生成k=8个候选优化，使用私有测试计算OPT@k指标（即至少有一个top-k候选通过所有测试且运行时比输入程序减少至少10%的任务百分比）。实验使用GPT-5-mini和Qwen3-Coder-30B-A3B-Instruct作为LLM骨干，在相同硬件环境下执行。

**对比方法**：与四类基线对比：1) 提示方法（Instruction直接优化、CoT思维链）；2) 检索增强方法（RAG检索相似慢/快代码对、FasterPy检索优化摘要）；3) 进化搜索（SBLLM）；4) 微调方法（EffiCoder）。

**主要结果与关键指标**：
1. **整体有效性**：EffiSkill在所有模型和语言设置中均取得最佳OPT@1和OPT@8。例如，在GPT-5-mini上，Python的OPT@1为26.48%（比最佳基线FasterPy高5.29个百分点），OPT@8为37.40%；C++的OPT@8达66.77%（比最佳基线CoT高12.03个百分点）。在Qwen3-Coder上，Python的OPT@8为36.60%（比最佳基线FasterPy高8.35个百分点），C++的OPT@8为56.50%（比最佳基线SBLLM高12.52个百分点）。统计检验显示多数改进显著（p<0.05）。
2. **消融分析**：移除技能检索（w/o Retrieval）或使用随机技能（w/ Random Skills）导致性能大幅下降，如Qwen3-Coder上OPT@8从36.60%降至13.80%；移除多计划生成（w/o Multi Plans）使OPT@8从36.60%降至14.29%，表明各组件均贡献显著。
3. **跨语言一致性**：方法在Python和C++上均有效，且在C++上改进更显著（OPT@8提升达12.36个百分点）。
4. **技能分析**：学习的技能库包含29个操作符技能，分为五类：实现与常数因子优化（占比54.2%）、代数/闭式重写（19.7%）、动态规划/状态压缩（13.1%）、组合与数论（9.5%）、图/数据结构操作（3.5%），表明技能覆盖了从局部清理到算法优化的多层次知识。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的EffiSkill框架在无需执行反馈的情况下，通过构建可复用的技能库来优化代码效率，但仍存在一些局限性和值得探索的方向。首先，其技能挖掘依赖于大规模慢/快代码对，这限制了其在缺乏此类数据或涉及新颖优化模式场景下的泛化能力。未来可研究如何结合强化学习或自监督方法，使智能体能从更少的样本或单次优化尝试中自主发现和抽象技能。其次，当前框架主要针对已知的效率瓶颈模式，对于复杂、多步骤的跨模块优化，其“计划组合”能力可能不足。可探索引入分层规划或神经符号推理，使智能体能动态组合低级技能以解决更宏观的优化问题。此外，技能库目前是静态的，未来可设计持续学习机制，让智能体在应用过程中不断扩展和精炼技能库，形成自我演化的优化知识体系。最后，将此类技能库与具备代码执行和环境反馈的智能体相结合，形成“静态分析+动态验证”的闭环，可能进一步提升优化成功率与代码可靠性。

### Q6: 总结一下论文的主要内容

这篇论文提出了EffiSkill框架，旨在解决利用大语言模型（LLM）优化代码效率时，现有方法缺乏可复用知识、泛化能力有限的问题。其核心贡献是构建了一个基于Agent技能的、可移植的代码效率优化工具箱，将反复出现的“慢到快”代码转换模式提炼为可重用的Agent技能，这些技能既包含具体的转换机制，也包含更高层的优化策略。

方法上，EffiSkill采用两阶段设计：第一阶段（技能挖掘）从大规模的快/慢代码对中挖掘出“操作技能”和“元技能”，构建技能库；第二阶段（技能应用）对新程序进行无需执行的诊断、技能检索、计划组合和候选代码生成，整个过程不依赖运行时反馈。

主要结论是，在EffiBench-X基准上的实验表明，EffiSkill取得了更高的优化成功率，在不同模型和编程语言设置下，比最强基线提升了3.69到12.52个百分点。这证明了机制级技能重用为无需执行的代码优化提供了有效基础，所构建的技能库可作为可复用资源服务于更广泛的智能体工作流。
