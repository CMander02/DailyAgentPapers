---
title: "SciVisAgentSkills: Design and Evaluation of Agent Skills for Scientific Data Analysis and Visualization"
authors:
  - "Kuangshi Ai"
  - "Haichao Miao"
  - "Kaiyuan Tang"
  - "Shusen Liu"
  - "Chaoli Wang"
date: "2026-06-04"
arxiv_id: "2606.05525"
arxiv_url: "https://arxiv.org/abs/2606.05525"
pdf_url: "https://arxiv.org/pdf/2606.05525v1"
github_url: "https://github.com/KuangshiAi/SciVisAgentSkills"
categories:
  - "cs.AI"
  - "cs.HC"
tags:
  - "科学计算可视化Agent"
  - "Agent技能库"
  - "工具使用"
  - "代码Agent"
  - "任务规划"
  - "SciVisAgentBench"
relevance_score: 7.5
---

# SciVisAgentSkills: Design and Evaluation of Agent Skills for Scientific Data Analysis and Visualization

## 原始摘要

Recent advances in agentic visualization have enabled the translation of natural language into executable scientific visualization (SciVis) workflows. While general-purpose coding agents show strong capabilities, they often lack the tool-specific expertise required for SciVis tasks. In this work, we present SciVisAgentSkills, a collection of reusable agent skills that augment coding agents for scientific data analysis and visualization by encoding environment assumptions, tool usage patterns, and domain heuristics across scientific tools such as ParaView, napari, VMD, and TTK. We evaluate these skills on Codex and Claude Code using SciVisAgentBench, a benchmark of 108 expert-designed multi-step tasks. Results show that agent skills improve mean task scores across the evaluated suites, with token-efficiency benefits that depend on the agent harness and tool setting. These findings highlight the importance of structured procedural knowledge for enabling reliable, long-horizon SciVis workflows, while also showing that skills should be studied alongside the execution harness that loads and applies them. The skills are available at https://github.com/KuangshiAi/SciVisAgentSkills.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何让通用编码代理具备科学数据分析和可视化（SciVis）领域专业知识的问题。研究背景是，随着多模态大语言模型和模型上下文协议的发展，基于自然语言的代理可视化系统成为可能，但科学可视化任务通常需要长序列、多步骤的工作流，涉及领域知识和专门工具（如ParaView、napari、VMD、TTK）的复杂交互。现有方法存在明显不足：一方面，通用编码代理虽然能力强大，但缺乏SciVis任务所需的工具特定专长；另一方面，为每个工具或任务构建专用代理效率低下，且当前社区中可复用的SciVis代理技能非常稀少，缺乏关于技能在不同工具、代理框架和任务类型间可移植性的实证证据。因此，本文的核心问题是：如何通过结构化的、可复用的代理技能来增强通用编码代理，使其能够可靠且高效地完成复杂的科学数据分析和可视化工作流。论文通过设计并评估SciVisAgentSkills技能集，探索了将环境约定、工具使用模式和领域启发式知识注入代理行为的有效性。

### Q2: 有哪些相关研究？

相关研究可分为三类。**方法类**包括通用智能体评测基准（如AgentBench、GAIA、τ-bench）和智能体技能研究（如SkillsBench），但它们未针对科学可视化（SciVis）工作流进行专门设计。本文与它们的区别在于提出了便携式技能模块（SciVisAgentSkills），通过编码环境假设和工具使用模式来增强通用编码智能体。**应用类**涵盖多种可视化智能体系统：对话式系统（VOICE、IntuiTF、CoDA）、工具中心型SciVis助手（AVA、ChatVis、ParaView-MCP）以及自主/多智能体工作流（VizGenie、NLI4VolVis等）。这些系统大多针对特定工具或界面定制，而本文聚焦于跨多工具（ParaView、napari等）的可复用技能。**评测类**包括VisEval、Drawing Pandas（侧重图表理解与代码生成）、LIDA（可视化度量）以及NL2SciVis（面向ParaView原子操作评测），SciVisAgentBench则扩展至多步长端到端SciVis工作流，本文正是在此基准上验证技能的有效性。

### Q3: 论文如何解决这个问题？

论文通过设计可复用的领域专家技能模块（SciVisAgentSkills）来增强通用编码智能体在科学数据分析和可视化任务中的表现。核心方法是将环境假设、工具使用模式和领域启发式知识编码为自包含、版本固定的过程性模块，覆盖ParaView、napari、VMD和TTK四种科学可视化工具。

整体框架由四个主要组件构成：一是YAML元数据前端，用于技能发现；二是Markdown格式的引导内容，包含使用规则、脚本模板、API摘要和故障排除笔记；三是代表性代码片段和函数使用模式，源自现有SciVis智能体；四是基于经验观察的约束条件（如强制无头渲染和视口输出捕获）。ParaView技能还额外包含独立的参考文件，因其API接口更为庞大。

关键技术包括：通过固定软件版本和指定执行环境来消除歧义和冗余探索；将官方文档提炼为结构化使用模式以引导智能体行为；融入来自ParaView-MCP、BioImage-Agent、GMX-VMD-MCP和TopoPilot等现有工作的可执行示例，减少试错成本。所有技能由可视化研究人员手动编写，并通过多轮观察智能体在代表性工作流上的表现进行迭代优化，专门针对工具使用失败模式（如错误的无头渲染和API误用）进行改进。为确保评估公正性，技能仅包含工具通用过程知识，不含基准测试特定解决方案或评估标准。

### Q4: 论文做了哪些实验？

论文在 SciVisAgentBench 基准上评估了 SciVisAgentSkills 技能库，该基准包含108个专家设计的多步骤任务，涵盖五个任务套件（生物图像、分子可视化、拓扑可视化、对象识别和ParaView）。实验设置是使用Codex和Claude Code两种通用编码智能体，分别在有技能和无技能条件下进行比较，每个配置进行三轮独立试验。评价采用标准化评估流水线，包括多模态LLM评判、基于图像的指标、代码验证器和规则检查。主要结果是：引入技能后，所有任务套件的总体得分均一致提升，其中Claude Code在拓扑可视化任务上提升最大（约60%），且较弱的基线获益更多。完成率不一定与分数趋势一致，例如Codex在对象识别上总体得分提高但完成率从92.59±9.80降至80.25±5.66。对于ParaView任务还报告了图像质量指标（PSNR、SSIM、LPIPS）。令牌效率分析显示，Claude Code输出令牌一致减少，而Codex趋势混合，令牌成本是技能内容、模型行为和环境上下文管理三者交互的结果，与性能无明确相关性。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向可归纳为以下几点：首先，技能与执行框架的交互机理尚不明确——不同模型（如Codex与Claude Code）对技能内容的检索与复用策略差异导致token效率变化，未来可设计自适应技能压缩与缓存机制；其次，技能增益高度依赖任务类型与工具成熟度，对已有良好文档的工具（如VMD）提升有限，需探索技能自动生成或从模型知识中动态提取；再者，当前未系统对比CLI与MCP等交互范式，可研究结构化工具体系如何影响技能设计；此外，技能知识仅覆盖单步模式，未支持长程工作流的状态保持与失败恢复，需耦合执行框架的持久化与回滚能力。未来可构建技能贡献生态，并开发元技能学习器，使其根据任务复杂度、模型基座与工具特性自适应组装技能模块。

### Q6: 总结一下论文的主要内容

该论文提出 SciVisAgentSkills，这是一套可重用的智能体技能集合，旨在增强通用编码智能体在科学数据分析和可视化（SciVis）中的能力。问题定义在于，通用编码智能体虽功能强大，但缺乏帕拉维尤（ParaView）、纳帕里（napari）等专业工具特有的领域知识。方法上，研究者通过编码环境假设、工具使用模式和领域启发式知识，构建了这些技能，并在包含108个专家设计的多步骤任务的 SciVisAgentBench 基准上，使用 Codex 和 Claude Code 进行评估。主要结论表明，技能提升了平均任务得分，但其令牌效率取决于智能体框架和工具设置。核心贡献在于证明了结构化程序知识对实现可靠、长周期 SciVis 工作流的重要性，并指出技能应与执行框架协同研究。该研究为低成本、可扩展地提升复杂科学场景下的智能体性能提供了新途径。
