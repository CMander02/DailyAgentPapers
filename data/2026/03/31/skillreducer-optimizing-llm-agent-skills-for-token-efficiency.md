---
title: "SkillReducer: Optimizing LLM Agent Skills for Token Efficiency"
authors:
  - "Yudong Gao"
  - "Zongjie Li"
  - "Yuanyuanyuan"
  - "Zimo Ji"
  - "Pingchuan Ma"
  - "Shuai Wang"
date: "2026-03-31"
arxiv_id: "2603.29919"
arxiv_url: "https://arxiv.org/abs/2603.29919"
pdf_url: "https://arxiv.org/pdf/2603.29919v1"
categories:
  - "cs.SE"
tags:
  - "LLM Agent"
  - "Tool Use"
  - "Context Window Optimization"
  - "Skill Compression"
  - "Coding Agent"
  - "Empirical Study"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# SkillReducer: Optimizing LLM Agent Skills for Token Efficiency

## 原始摘要

LLM-based coding agents rely on \emph{skills}, pre-packaged instruction sets that extend agent capabilities, yet every token of skill content injected into the context window incurs both monetary cost and attention dilution. To understand the severity of this problem, we conduct a large-scale empirical study of 55,315 publicly available skills and find systemic inefficiencies: 26.4\% lack routing descriptions entirely, over 60\% of body content is non-actionable, and reference files can inject tens of thousands of tokens per invocation. Motivated by these findings, we present \textsc{SkillReducer}, a two-stage optimization framework. Stage~1 optimizes the routing layer by compressing verbose descriptions and generating missing ones via adversarial delta debugging. Stage~2 restructures skill bodies through taxonomy-driven classification and progressive disclosure, separating actionable core rules from supplementary content loaded on demand, validated by faithfulness checks and a self-correcting feedback loop. Evaluated on 600 skills and the SkillsBench benchmark, \textsc{SkillReducer} achieves 48\% description compression and 39\% body compression while improving functional quality by 2.8\%, revealing a \emph{less-is-more} effect where removing non-essential content reduces distraction in the context window. These benefits transfer across five models from four families with a mean retention of 0.965, and generalize to an independent agent framework.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的编程智能体（Agent）中，其核心功能扩展模块——“技能”（Skill）所导致的上下文窗口令牌（token）使用效率低下和成本高昂的问题。研究背景是，LLM编程智能体（如Claude Code）通过“技能”来封装可复用的领域特定指令和知识，以定制化其行为。这些技能在智能体被调用时，其内容会被注入到上下文窗口中，从而产生计算和金钱成本。

现有方法或现状的不足在于，通过对55,315个公开技能的大规模实证分析，论文发现当前技能生态系统存在严重的系统低效问题：1）路由层低效：26.4%的技能完全缺乏用于智能体路由选择的描述，导致路由机制失效；2）主体内容臃肿：超过60%的技能主体内容是非操作性的背景介绍或示例，而非核心行动指令；3）令牌成本失控：引用文件多的技能单次调用可能注入数万个令牌，造成巨大的不必要开销。这导致了“技能膨胀”（skill bloat）现象，即大量无关内容不仅没有提升智能体性能，反而稀释了其注意力并增加了成本。

因此，本文要解决的核心问题是：如何系统性地优化LLM智能体技能，在最大限度压缩其令牌使用量（从而降低成本）的同时，保持甚至提升其功能性质量。论文提出了名为SkillReducer的两阶段优化框架来应对这一挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：技能优化与压缩方法、上下文窗口管理技术，以及测试用例最小化算法。

在**技能优化与压缩方法**方面，相关工作主要关注如何减少输入到LLM中的内容。例如，LLMLingua等基于困惑度的token级剪枝方法会移除低重要性的token；Gisting等嵌入级方法将提示压缩为学习的软token；基于摘要的方法则直接使用LLM重写内容以缩短长度。本文提出的SkillReducer与这些方法的关键区别在于其**结构感知**的特性。现有方法通常对自由文本进行均匀压缩，而技能文档混合了可执行规则、示例和解释性背景，需要同时保持路由正确性和任务性能。SkillReducer通过分类和渐进披露来重构技能主体，将核心规则与补充内容分离，从而实现了更精细的压缩。

在**上下文窗口管理**方面，研究关注如何在固定上下文预算内高效组织信息。本文借鉴了**渐进披露**原则，即默认只加载核心指令，在需要时才通过工具调用获取补充模块。SkillReducer的第二阶段自动化了从单体架构到分层架构的转换，这与旨在优化上下文使用的代理设计思想一脉相承，但本文将其系统性地应用于技能内容的自动化重构。

在**算法基础**方面，本文创新性地将**Delta调试**算法应用于技能描述优化。该算法原用于软件测试中以最小化导致失败的输入。SkillReducer的第一阶段将其适配，将路由描述中的语义子句视为“变更”，将路由正确性作为“谓词”，从而找到在保持路由行为前提下的最小描述子集。这为技能描述的压缩提供了一个形式化且可验证的优化框架。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SkillReducer的两阶段优化框架来解决LLM智能体技能中存在的令牌效率低下问题。该框架的核心思想是借鉴软件“去膨胀”的理念，移除技能中非必要的自然语言内容，从而减少注入上下文窗口的令牌数量，同时保持甚至提升功能质量。

**整体框架与主要模块：**
SkillReducer包含两个顺序执行的阶段。
1.  **第一阶段：路由层优化**。针对技能描述（description）进行优化，解决其缺失、过短或冗长的问题。该阶段采用两阶段设计：
    *   **模拟预言驱动的Delta调试**：首先，利用LLM将技能描述分割为具有独立路由意义的“语义单元”。然后，应用Delta调试算法（ddmin），在一个由目标技能、相似技能和一个对抗性生成的“影子技能”构成的候选池中，迭代测试并移除那些对路由决策（即智能体正确选择该技能）非必要的语义单元，得到一个“1-最小”的子集。最后，对保留的单元进行精简重写。
    *   **真实环境验证与选择性恢复**：将压缩后的描述部署到真实的智能体运行环境（如Claude Code CLI）中进行验证。如果压缩导致某些查询无法触发技能，则从被删除的单元中贪婪地恢复最能改善触发率的单元，确保路由等效性。对于缺失或过短的描述，则直接从技能主体中提取关键路由信号（主要能力、触发条件、唯一标识符）来生成。

2.  **第二阶段：技能主体与引用文件优化**。核心是将原本整体加载的单一技能文档，重构为一个“核心规则”模块和多个“按需加载”的引用模块。具体流程包含五个步骤：
    *   **内容分类**：使用基于分类法的LLM分类器，将技能主体内容划分为五类：核心规则（必须遵循的可执行指令）、背景说明、示例、模板和冗余内容。
    *   **类型特异性压缩**：对分类后的内容进行针对性处理。核心规则被合并和精简；示例和模板按概念去重，只保留最具代表性的一个；背景内容被总结概括。
    *   **跨文件去重**：处理外部引用文件，移除其与技能主体内容重叠的部分，并对剩余内容进行压缩。
    *   **引用标注**：为每个引用模块生成“何时加载”的触发条件和关键词元数据，以支持任务相关的选择性加载。
    *   **质量门禁与反馈循环**：通过两个质量门禁进行验证。门禁1检查压缩后的核心模块是否忠实于原意。门禁2通过实际任务评估功能保留度。如果任务失败，则分析原因并将必要的内容从引用模块“提升”回核心模块，形成一个自我修正的反馈循环。

**关键技术：**
*   **基于语义单元的Delta调试**：将自然语言描述视为可分割的语义单元进行最小化测试，平衡了搜索效率与精度。
*   **对抗性候选池构建**：在路由测试中引入通过LLM生成的、主题相似但功能不同的“对抗性技能”，提高了压缩的鲁棒性。
*   **分类驱动的渐进式披露**：依据对技能内容构成的实证发现（仅38.5%为可执行核心），通过分类实现核心指令与辅助内容的分离，模仿了软件工程中的“按需加载”模式。
*   **任务感知的引用加载**：通过去重和元数据标注，使引用文件仅在智能体明确请求时才被加载，避免了无关内容的令牌开销。

**创新点：**
1.  **问题驱动的系统化方法**：框架的每个阶段都直接对应实证研究中发现的具体问题（描述低效、主体内容冗余、引用文件过载）。
2.  **两阶段混合验证**：结合了快速的模拟预言测试和耗时的真实环境验证，在效率与可靠性之间取得平衡。
3.  **“少即是多”的压缩哲学**：不仅压缩文本长度，更通过分离核心与辅助内容来减少智能体在上下文中的注意力分散，从而在降低令牌成本的同时，实现了功能质量的提升（2.8%）。

### Q4: 论文做了哪些实验？

论文的实验设置、数据集、对比方法和主要结果如下：

**实验设置与数据集**：实验在600个技能（87个来自SkillHub官方，464个来自社区，49个从GitHub采样）和外部基准SkillsBench（包含87个任务，涉及229个技能）上进行。评估采用三种条件：条件D（无技能，作为下限）、条件A（原始未压缩技能，作为基线）、条件C（仅提供压缩后的核心内容并按需加载引用，测试SkillReducer）。使用开源模型Qwen3.5进行任务生成、代理执行和评估，以防止信息泄漏。

**对比方法**：主要对比原始技能（条件A）与压缩后技能（条件C）的性能，同时以无技能条件（条件D）作为参考。此外，论文还进行了可扩展性验证，对从55,315个野生技能中采样的198个技能应用压缩，并测试了在五个不同模型家族和独立代理框架上的泛化能力。

**主要结果与关键指标**：
1. **压缩效果**：SkillReducer实现了48%的描述压缩率和39%的主体压缩率，平均每个技能节省约1000个token。在SkillsBench上，主体token从359K降至84K（平均每任务减少75%）。对野生技能的压缩率更高，平均核心减少77.5%（其中大型技能压缩率可达95.8%）。
2. **功能质量保留**：压缩后技能（条件C）的平均得分为0.742，高于原始技能（条件A）的0.722，功能质量提升2.8%。通过率（即压缩后得分不低于原始得分的技能比例）为86.0%，改进率（压缩后得分更高的技能比例）未明确给出但得分提升显著。
3. **泛化与经济效益**：压缩效果在四个模型家族的五个模型中平均保留率为0.965，并能泛化到独立代理框架。压缩600个技能的成本约为14-18美元，经济可行。端到端分析显示，最佳情况下平均输入节省26.8%，且代理输出未显著增加（平均+1.7%，中位数-0.3%）。

### Q5: 有什么可以进一步探索的点？

这篇论文提出了一个有效的技能压缩框架，但仍有多个方向值得深入探索。首先，其优化主要针对静态技能库，未能考虑技能在动态、多轮次交互中的演化。未来可研究在线学习机制，让技能描述能根据实际使用频率和成功率进行自适应精简。其次，当前方法侧重于文本压缩，而高级技能可能涉及代码、API调用或外部工具的组合，未来可探索跨模态（如结构化代码与自然语言指令）的联合优化方案。此外，论文验证集中于功能正确性，但未深入评估压缩后对复杂任务中推理链连贯性的长期影响，这需要更复杂的基准测试。最后，从系统层面看，SkillReducer 作为一个独立预处理工具，未来可尝试与LLM的注意力机制或推理过程更深度集成，例如开发能实时感知上下文负荷并动态加载技能片段的轻量级调度器，从而实现更精细的端到端效率优化。

### Q6: 总结一下论文的主要内容

这篇论文针对基于大语言模型的编码代理中“技能”组件导致的上下文窗口令牌效率低下问题进行了研究。论文首先通过大规模实证分析（涉及55,315个公开技能）揭示了现有技能存在的系统性低效：26.4%的技能完全缺乏路由描述，超过60%的技能主体内容是非操作性的，且引用文件会注入大量令牌。

为解决此问题，论文提出了SkillReducer这一两阶段优化框架。第一阶段优化路由层，通过压缩冗长描述并利用对抗性增量调试为缺失描述生成内容。第二阶段重构技能主体，采用基于分类法的分类和渐进式披露方法，将可操作的核心规则与按需加载的补充内容分离，并通过忠实度检查和自我纠正反馈循环进行验证。

实验评估表明，SkillReducer在600个技能和SkillsBench基准测试上实现了48%的描述压缩和39%的主体压缩，同时将功能质量提升了2.8%，揭示了“少即是多”的效应。其优化效益在来自四个家族的五个模型中平均保留了96.5%，并能推广到独立的代理框架，核心贡献在于显著提升了LLM代理的令牌效率与功能性。
