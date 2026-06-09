---
title: "What Should a Skill Remember? Quality-Cost Trade-offs in Cost-Aware Skill Rewriting for Language Model Agents"
authors:
  - "Qinghua Xing"
  - "Yinda Chen"
  - "Yaping Jin"
  - "Zhenhe Wu"
  - "Bohan Lin"
  - "Hang Zhou"
  - "Xinghao Chen"
  - "Hanting Chen"
  - "Zhiwei Xiong"
date: "2026-06-08"
arxiv_id: "2606.09421"
arxiv_url: "https://arxiv.org/abs/2606.09421"
pdf_url: "https://arxiv.org/pdf/2606.09421v1"
github_url: "https://github.com/1Reminding/Skill_EE"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Skill Rewriting"
  - "Cost-Aware Optimization"
  - "Prompt Compression"
  - "Agent Skills"
  - "Quality-Cost Trade-off"
relevance_score: 7.5
---

# What Should a Skill Remember? Quality-Cost Trade-offs in Cost-Aware Skill Rewriting for Language Model Agents

## 原始摘要

Large language model agents increasingly rely on skills: reusable procedural documents encoding workflows, tool use, implementation patterns, validation checks, and domain rules. Skill rewriting is often treated as prompt compression, but shorter skills can make agents more expensive by removing sparse operational anchors that prevent exploration, debugging, and recovery. We study skill rewriting through this economic lens. Our controlled framework profiles skill structure, rewrites skills using information-preservation strategies, and evaluates the rewrites under fixed task instructions, environments, and verifiers. Experiments on SkillsBench reveal distinct quality--cost trade-offs across strategies: API/code anchoring, workflow guarding, and rule/formula anchoring benefit different task families, with no universally dominant template. In the main held-out evaluation, the learned policy reduces total cost by 7.0\% and downstream agent-token cost by 6.0\%; in frozen cross-model transfer, the corresponding reductions average 14.7\% and 13.7\%, while verifier quality is preserved. These results position skill design as cost-aware operational knowledge engineering rather than prompt compression. Resources: \href{https://github.com/1Reminding/Skill_EE}{SkillEE}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体中技能（skill）重写时面临的质量与成本权衡问题。研究背景是，LLM智能体越来越依赖技能——即描述工作流、工具使用、代码模式、验证规则等可复用的程序性文档。现有方法通常将技能重写视为简单的提示压缩（prompt compression），通过缩短文本来降低成本。然而，论文指出这种做法存在不足：短技能可能移除关键的“操作锚点”（operational anchors），如API接口、验证阈值、恢复规则等，这些稀疏但关键的细节若被删除，会导致智能体在后续执行中增加探索、调试和恢复行为，反而使下游token成本升高（实验中固定工作流重写使下游成本升至原来的1.14倍）。因此，核心问题是：技能重写不应仅追求文本压缩，而应视为成本感知的知识保留（cost-aware knowledge preservation），需要决定哪些信息必须保留以平衡任务质量与总执行成本。论文的目标是系统性地研究不同重写策略（如保留API/代码细节、工作流守卫、规则公式）对不同任务类型的影响，并学习一个任务条件化的策略选择器，在维持验证质量的同时降低总成本。

### Q2: 有哪些相关研究？

相关工作主要分为三类：

1. **智能体、工具与程序性技能**：ReAct、Toolformer、API-Bank、ToolLLM等研究了智能体的推理-行动循环与工具使用能力。Voyager、SkillsBench等将技能视为可复用的程序性文档。本文不同于这些工作仅将技能视为给定内容，而是研究技能内部的重写结构：哪些“操作锚点”（如API、代码、规则）在重写中必须保留，及其对任务质量和成本的影响。

2. **提示压缩与优化**：LLMLingua、LongLLMLingua等通过剪枝或重新编码减少输入长度。提示优化方法（如文本反馈、演化搜索）则优化提示的语义保留或任务准确性。本文指出这些方法主要优化通用提示的输入长度或准确率，但忽略了技能文档中稀疏但执行关键的细节（如验证规则）在压缩中可能被牺牲，导致下游成本增加。

3. **成本感知的LLM与智能体系统**：现有工作通过提示适配、模型级联或路由优化质量-成本权衡。本文进一步发现技能重写不仅影响直接token成本，还会改变下游执行轨迹成本（如调试、恢复所需长度）。这是首个将技能设计定位为“成本感知的操作知识工程”而非简单提示压缩的工作。

### Q3: 论文如何解决这个问题？

论文通过一个成本感知的技能重写框架来解决大型语言模型智能体中技能的经济效用与质量权衡问题。核心方法是将技能重写视为信息保留问题，而非简单的提示压缩。整体框架包含四个模块：首先，计算每个任务-技能对的结构化特征φτ，包括技能数量、码-词比、API使用等，形成任务特征画像。其次，定义四种信息保留策略：源原生压缩保留原始结构、工作流守护保留顺序步骤和验证项、API/代码锚定保留调用细节、规则/公式锚定保留领域规则。每种策略在重写时通过轻量审计确保保留关键操作锚点，缺失时自动用源文档修复。第三，在固定任务指令、环境和验证器条件下，用每种策略重写技能并执行智能体，收集验证结果和令牌使用日志，转换为经济效用指标。最后，学习任务条件策略选择器：通过稀疏线性回归拟合效用预测模型Ûθ(φτ,a)=b_a+w_a⊤z(φτ)，在推理时选择预测效用最高的策略。关键技术包括：操作锚点的分类体系确保信息保留的可控性；轻量审计机制防止关键内容丢失；稀疏回归策略选择器学习特征-策略关联，避免在所有任务中使用统一模板。创新点在于将技能重写重新定义为成本感知的操作知识工程，通过策略选择实现质量与成本的帕累托最优，在保持验证质量的同时降低智能体部署成本。

### Q4: 论文做了哪些实验？

论文在SkillsBench基准上进行了全面的实验评估。实验设置包含88个任务，其中86个可执行任务被划分为28个模板校准任务、38个策略适应任务和20个保留评估任务。主要实验使用Gemini CLI与Gemini 3 Flash Preview，跨模型迁移测试额外使用Gemini 3 Pro、Codex与GPT-5.4、Claude Code与Opus 4.6三种配置。

对比方法包括原始手写技能基线（SkillsBench baseline）、三种固定重写策略（API/代码锚定、规则/公式锚定、工作流守卫）以及策略选择的技能重写。主要评估指标包括验证器质量保留率（QR）、直接技能令牌比（r_s）、下游智能体令牌比（r_a）和总成本比（ρ）。

在保留评估集上，策略选择方法实现了QR=1.01，总成本比ρ=0.93，分别降低总成本7.0%和下游令牌成本6.0%。在跨模型迁移测试中，平均总成本降低14.7%，下游令牌成本降低13.7%。消融实验表明，质量仅优化器虽获得略高验证分数（0.826）但成本未降低，而去除锚点修复导致最大质量下降（QR=0.95），验证了信息保留策略的重要性。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索方向主要集中在以下几个方面。首先，当前工作仅聚焦于静态、文本化的技能文档，未涵盖动态检索的知识或持续更新的部署时技能，未来可研究如何将在线学习与技能重写结合，使代理能根据运行经验自适应调整技能结构。其次，成本度量仅基于token数量，忽略了现实中的延迟、缓存、硬件成本等，可以构建更细粒度的成本模型（如考虑API调用频率与并行度）来指导重写。此外，当前策略在不同任务族间存在性能波动，可探索元学习或基于任务嵌入的自适应重写策略，例如为不同任务类型自动选择API锚定或规则保留等策略。另一个方向是技能的可解释性与鲁棒性：重写中如何平衡信息保留与泛化能力，防止因过度压缩导致代理在长尾场景下丢失关键修复模式。最后，可尝试将成本感知的技能重写与工具使用、记忆检索等模块联合优化，形成端到端的神经符号学习方法。

### Q6: 总结一下论文的主要内容

这篇论文研究了大型语言模型代理在技能重写过程中面临的质量与成本权衡问题。传统上，技能重写被视为提示压缩，但更短的技能可能因删除关键的操作锚点（如API调用、工作流规则等）而导致代理在探索、调试和恢复时产生更高成本。论文提出一个受控框架，通过分析技能结构、采用信息保留策略进行重写，并在固定任务指令、环境和验证器下评估重写效果。在SkillsBench上的实验表明，不同策略（如API/代码锚定、工作流保护、规则/公式锚定）在不同任务族中表现出互补的质量-成本权衡，不存在通用最优模板。主要结果表明，学习到的策略在保留验证质量的同时，将总成本降低7.0%，下游代理令牌成本降低6.0%；在跨模型迁移中，相应成本平均降低14.7%和13.7%。这一研究将技能设计从提示压缩重新定义为成本感知的操作知识工程，为构建高效、可靠的AI代理系统提供了新视角。
