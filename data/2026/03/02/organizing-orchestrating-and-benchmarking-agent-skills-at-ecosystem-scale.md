---
title: "Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale"
authors:
  - "Hao Li"
  - "Chunjiang Mu"
  - "Jianhao Chen"
  - "Siyue Ren"
  - "Zhiyao Cui"
date: "2026-03-02"
arxiv_id: "2603.02176"
arxiv_url: "https://arxiv.org/abs/2603.02176"
pdf_url: "https://arxiv.org/pdf/2603.02176v1"
github_url: "https://github.com/ynulihao/AgentSkillOS"
categories:
  - "cs.CL"
tags:
  - "Tool Use & API Interaction"
  - "Architecture & Frameworks"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "AgentSkillOS (tree-based skill organization, DAG-based orchestration)"
  primary_benchmark: "N/A"
---

# Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale

## 原始摘要

The rapid proliferation of Claude agent skills has raised the central question of how to effectively leverage, manage, and scale the agent skill ecosystem. In this paper, we propose AgentSkillOS, the first principled framework for skill selection, orchestration, and ecosystem-level management. AgentSkillOS comprises two stages: (i) Manage Skills, which organizes skills into a capability tree via node-level recursive categorization for efficient discovery; and (ii) Solve Tasks, which retrieves, orchestrates, and executes multiple skills through DAG-based pipelines. To evaluate the agent's ability to invoke skills, we construct a benchmark of 30 artifact-rich tasks across five categories: data computation, document creation, motion video, visual design, and web interaction. We assess the quality of task outputs using LLM-based pairwise evaluation, and the results are aggregated via a Bradley-Terry model to produce unified quality scores. Experiments across three skill ecosystem scales (200 to 200K skills) show that tree-based retrieval effectively approximates oracle skill selection, and that DAG-based orchestration substantially outperforms native flat invocation even when given the identical skill set. Our findings confirm that structured composition is the key to unlocking skill potential. Our GitHub repository is available at:https://github.com/ynulihao/AgentSkillOS.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决随着Claude等平台智能体技能生态系统的快速扩张和去中心化发展，所带来的技能有效利用、管理和规模化挑战。研究背景是，截至2026年初，公开可用的技能已超过28万个，且主要由第三方开发者贡献，形成了一个庞大而分散的生态系统。现有方法存在明显不足：从用户角度看，技能数量庞大且缺乏全局视图，导致难以发现、理解和选择适合特定任务的技能；从平台方角度看，缺乏有效的治理机制来保障技能质量和可靠性；更根本的是，现有技能调用方式往往是扁平、孤立的，缺乏系统的组合与协调机制，使得许多技能未被充分利用，无法通过协同多个技能来解决超越单个技能能力的复杂任务。

因此，本文要解决的核心问题是：如何构建一个系统化的框架，以实现对大规模、去中心化智能体技能生态的高效组织、编排和任务解决。具体而言，论文提出了AgentSkillOS框架，它通过两个核心阶段来应对上述挑战：首先，在“管理技能”阶段，通过构建能力树对技能进行层次化分类组织，以支持高效的技能发现；其次，在“解决任务”阶段，基于能力树进行任务驱动的技能检索，并利用有向无环图（DAG）对多个技能进行结构化编排与执行，从而将分散的技能组合起来解决复杂任务。最终目标是通过结构化的组合机制，充分释放技能生态系统的潜力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕智能体技能的管理、编排与评测展开，可分为以下几类：

**1. 技能管理与检索方法**：现有研究多关注基于语义嵌入的检索技术，如通过向量数据库匹配技能描述与任务需求。本文提出的能力树（capability tree）方法则通过递归分类构建层次化结构，不仅提升检索效率，还能发现功能相关但语义不直接匹配的技能，弥补了纯语义检索的不足。

**2. 多技能编排与执行框架**：传统智能体常以扁平、顺序方式调用技能，缺乏结构化组合机制。本文引入基于有向无环图（DAG）的编排管道，显式建模技能间的依赖与数据流，实现多技能协同。这与早期工作流式智能体（如AutoGPT）有相似之处，但更专注于技能生态系统的规模化协调。

**3. 智能体能力评测基准**：现有评测多集中于代码生成或问答任务，缺乏对多格式、端到端产出的评估。本文构建的基准包含30项跨领域任务（如数据计算、视觉设计），要求输出完整可交付成果，并通过基于LLM的成对比较与Bradley-Terry模型聚合评分，提供了更细粒度的质量评估方法。

**4. 生态系统治理与扩展**：针对第三方技能生态的治理挑战，本文首次提出系统级管理框架（Manage Skills阶段），通过能力树实现技能分类与容量控制，为平台方提供了可扩展的质量管理途径，区别于以往仅关注单技能调用的研究。

总体而言，本文在技能检索上创新性地结合层次化分类与语义检索，在编排上强调DAG驱动的结构化组合，在评测上注重真实场景下的多技能协作产出，系统性解决了大规模技能生态中的发现、协调与评估问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AgentSkillOS的两阶段框架来解决大规模Agent技能生态系统的有效利用、管理和扩展问题。

**核心方法与架构设计：**
AgentSkillOS的整体框架分为“管理技能”和“解决任务”两个核心阶段。
1.  **管理技能阶段**：其核心创新是构建一个**能力树**来组织大规模技能生态系统。该树通过节点级递归分类法离线构建和更新。具体过程是：从根节点（包含所有技能）开始，采用广度优先策略，利用LLM为每个节点执行“组发现”（生成类别）和“技能分配”（将技能分到类别）两个步骤来生成子节点，从而逐层构建树。每个叶节点对应一个具体技能。此结构支持从粗到细的层级定位，显著提升了大规模技能库中的检索效率。此外，系统通过一个**使用频率队列**来选择构建树的技能子集，以控制树的大小并优先纳入高质量技能，同时允许用户添加自定义或私有技能。
2.  **解决任务阶段**：其核心是基于**有向无环图（DAG）的技能编排管道**。该阶段包含三个子步骤：
    *   **任务驱动的技能检索**：利用上述能力树，引导LLM根据用户任务描述，自上而下遍历树结构，层层筛选相关类别节点，最终到达相关技能的叶节点，形成候选集。对于不在树中的技能，则通过向量相似性搜索进行补充。
    *   **基于DAG的技能编排**：将最终选定的技能集（V）组织成DAG。论文定义了三种编排策略（质量优先、效率优先、简洁优先），由LLM根据任务、技能集和指定策略，将任务分解为子任务，并确定子任务（对应技能节点）之间的依赖关系，从而生成不同结构的DAG。
    *   **多技能任务执行**：任务特定的Agent按照DAG的层级依赖关系顺序（同层可并行）执行节点。每个节点执行时，系统会构建详细的提示，说明子任务、上游产出和预期输出，执行后将产出保存为工件，并生成结构化摘要。

**关键技术及创新点：**
*   **结构化技能组织（能力树）**：这是实现高效技能发现与管理的基础创新。它通过递归分类将扁平技能库转化为层次化结构，解决了直接在海量技能中检索的效率和准确性问题。
*   **基于DAG的显式编排**：区别于简单的扁平化技能调用，该方法将任务解决过程明确建模为具有依赖关系的图结构。这允许复杂的多技能协作、并行执行，并支持根据不同目标（如质量、效率）灵活定制解决方案，是“结构化组合”思想的关键体现。
*   **动态更新与混合检索机制**：能力树支持新技能的增量插入和路径更新。同时，系统结合了树遍历（利用LLM推理发现互补技能）和向量检索（处理未入库技能）的混合检索方式，兼顾了覆盖面和创造性。
*   **编排复用机制**：系统会存储已生成的技能编排图（DAG），当遇到描述相似的新任务时，可直接复用已有编排计划，跳过检索和编排阶段，提升了运行效率。

### Q4: 论文做了哪些实验？

本论文的实验旨在评估AgentSkillOS框架在管理、检索和编排大规模技能生态系统的有效性。实验设置包括构建三个不同规模的技能生态系统（200、1K、200K个技能），技能来源于公共技能市场和GitHub仓库。评估基准是一个包含30个任务的测试集，涵盖数据计算、文档创建、动态视频、视觉设计和网页交互五大类别，要求生成PDF、PPTX、视频等多种终端用户可用的成品。主要对比方法分为四组：1）AgentSkillOS的三种变体（Quality-First、Efficiency-First、Simplicity-First），它们基于能力树进行技能检索，并使用有向无环图（DAG）进行编排；2）Oracle编排（Quality-First (Oracle)），使用基准指定的真实相关技能作为性能上限参考；3）Claude Code Agent SDK的三种消融配置（w/ Full Pool、w/ Retrieval、w/ Oracle Skills），提供技能但以扁平、非结构化方式调用；4）基线方法（Vanilla），即不提供任何技能的原生Claude Code Agent SDK。评估采用基于LLM的成对比较，并通过Bradley-Terry模型聚合结果生成统一的排名分数（BT分数，范围0-100）。

主要结果显示，在所有生态系统规模下，AgentSkillOS变体均显著优于其他方法。例如，在200技能规模中，Quality-First的BT分数为100（最佳），而w/ Full Pool为24.3，Vanilla为0。随着规模扩大至200K，Quality-First仍保持100分，w/ Full Pool降至17.2。这表明基于树的检索能有效近似真实技能选择（与Oracle相比差距较小），且DAG编排即使在使用相同技能集时也能大幅提升性能（如w/ Oracle Skills仍落后于Quality-First）。此外，实验还通过消融分析验证了检索和编排两个组件的贡献：移除任一组件的性能都会下降，其中DAG编排提供了显著的额外改进。关键数据指标包括各方法在五大类别上的胜/平/负计数（W/T/L）以及最终的BT分数，这些结果证实了结构化组合是释放技能潜力的关键。

### Q5: 有什么可以进一步探索的点？

该论文提出了一个系统性的技能管理框架，但在技能生态的深度组织与动态协同方面仍有进一步探索的空间。局限性在于：当前的能力树分类依赖于静态、预定义的递归划分，难以适应技能快速演化和跨领域融合的复杂场景；DAG编排虽优于扁平调用，但任务流程仍是预定义或有限检索生成的，缺乏在复杂、开放环境中实时动态重组与自适应优化的能力。

未来研究方向可包括：一、引入动态技能图谱与元学习机制，使技能表征能随使用反馈持续演化，支持更精准的情境化检索与组合推荐；二、探索基于强化学习或因果推理的编排策略，让系统能自主评估技能组合效果并优化执行路径，尤其在多步骤、多模态任务中实现更灵活的决策；三、扩展基准测试至更开放的真实世界场景，如跨平台协作、长期任务规划等，以评估系统在不确定性下的鲁棒性。此外，可研究技能间的知识迁移与共享机制，提升生态整体的学习效率与协同智能。

### Q6: 总结一下论文的主要内容

该论文针对Claude智能体技能生态快速扩张带来的管理挑战，提出了首个系统性框架AgentSkillOS，旨在实现技能的高效组织、编排与规模化应用。核心问题是如何在庞大的技能库中有效发现、选择并组合多个技能以完成复杂任务。

方法上，AgentSkillOS包含两个阶段：1) **管理技能**：通过节点级递归分类法将技能组织成能力树，实现高效检索与发现；2) **解决任务**：基于有向无环图（DAG）的流水线来检索、编排和执行多个技能。为评估框架效果，作者构建了一个包含30个任务的基准测试集，涵盖数据计算、文档创建、动态视频、视觉设计和网页交互五类，并采用基于LLM的成对评估与Bradley-Terry模型聚合输出质量。

主要结论显示，在从200到20万技能的不同规模生态中，基于树结构的检索能有效逼近理想技能选择效果，且DAG编排显著优于传统的扁平调用方式。实验证实结构化组合是释放技能潜力的关键，为大规模智能体技能生态的治理与性能提升提供了重要理论基础与实践方案。
