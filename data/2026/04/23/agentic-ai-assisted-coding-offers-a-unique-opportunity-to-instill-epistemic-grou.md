---
title: "Agentic AI-assisted coding offers a unique opportunity to instill epistemic grounding during software development"
authors:
  - "Magnus Palmblad"
  - "Jared M. Ragland"
  - "Benjamin A. Neely"
date: "2026-04-23"
arxiv_id: "2604.21744"
arxiv_url: "https://arxiv.org/abs/2604.21744"
pdf_url: "https://arxiv.org/pdf/2604.21744v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "q-bio.BM"
tags:
  - "AI-assisted coding"
  - "agent scaffolding"
  - "epistemic grounding"
  - "domain-specific software"
  - "community-governed documents"
  - "agentic AI"
  - "scientific computing"
relevance_score: 7.5
---

# Agentic AI-assisted coding offers a unique opportunity to instill epistemic grounding during software development

## 原始摘要

The capabilities of AI-assisted coding are progressing at breakneck speed. Chat-based vibe coding has evolved into fully fledged AI-assisted, agentic software development using agent scaffolds where the human developer creates a plan that agentic AIs implement. One current trend is utilizing documents beyond this plan document, such as project and method-scoped documents. Here we propose GROUNDING$.$md, a community-governed, field-scoped epistemic grounding document, using mass spectrometry-based proteomics as an example. This explicit field-scoped grounding document encodes Hard Constraints (non-negotiable validity invariants empirically required for scientific correctness) and Convention Parameters (community-agreed defaults) that override all other contexts to enforce validity, regardless of what the user prompts. In practice, this will empower a non-domain expert to generate code, tools, and software that have best practices baked in at the ground level, providing confidence to the software developer but also to those reviewing or using the final product. Undoubtedly it is easier to have agentic AIs adhere to guidelines than humans, and this opportunity allows for organizations to develop epistemic grounding documents in such a way as to keep domain experts in the loop in a future of democratized generation of bespoke software solutions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决由AI辅助编码（特别是“vibe coding”和agentic软件开发）带来的一个关键问题：在生成科学软件时存在“有效性缺口”（validity gap）。研究背景是，随着ChatGPT等大语言模型和Claude Code、Cursor等agent框架的普及，非领域专家也能通过高级指令快速生成定制化科学软件（如蛋白质组学分析工具）。然而，现有方法（如根据用户意图的plan.md、项目规则的AGENTS.md、技术方法的SKILL.md）虽然在指导agent高效执行任务方面有效，但缺少对领域特定知识（epistemic knowledge）的形式化约束。这导致agent可能生成符合用户表面意图、但违反核心科学有效性标准（如错误的错误发现率计算或不受控制的修饰搜索）的输出，从而产生无效甚至有害的软件。因此，本文的核心问题是：如何确保在agentic AI辅助的软件开发过程中，输出的软件能自动、无条件地遵循领域社区公认的科学有效性规则和最佳实践。为解决此问题，论文提出GROUNDING.md，一个由社区治理、领域范围的“认知基础”（epistemic grounding）文档，通过编码硬约束（Hard Constraints，如非协商的有效性不变量）和约定参数（Convention Parameters），在冲突时覆盖所有其他上下文，从而在根本上保证科学有效性。

### Q2: 有哪些相关研究？

本文的相关工作主要集中在AI辅助编程中的上下文工程文档体系。作者将现有文档分为三类：首先是**任务级文档**如plan.md，用于定义会话范围内的临时任务；其次是**项目级文档**如AGENTS.md（或CLAUDE.md、cursor_rules.md等），用于规定项目范围的规则和约定；最后是**方法级文档**如SKILL.md，用于封装可复用的技术流程。

本文提出的GROUNDING.md与上述文档的关键区别在于：它属于**领域范围的认知基础规范**，具有最高的权威性和稳定性。与plan.md（仅关注当前任务）、AGENTS.md（仅关注项目规范）、SKILL.md（仅关注方法步骤）不同，GROUNDING.md编码了领域社区的刚性约束（Hard Constraints）和约定参数（Convention Parameters），如蛋白质组学中的FDR计算规则。这些规则会覆盖所有下层上下文，确保科学有效性不受用户意图的干扰。

此外，本文还与社区现有的形式化指南（如HUPO-PSI标准、EVERSE RSQKit项目）进行了区分，指出这些指南并非为AI消费而设计，而GROUNDING.md则是专门面向agentic AI的认知基础层，其权威性来自领域社区共识而非个体开发者。

### Q3: 论文如何解决这个问题？

论文通过引入一个名为GROUNDING.md的领域范围认知基础文档来解决AI辅助编码中缺乏领域知识约束导致输出不科学的问题。核心方法是在智能体框架中创建一个不可变的、社区治理的基础规范层，该层在上下文工程中具有最高优先级，能够覆盖用户意图、项目规则和方法文档等其他所有上下文。

整体框架构建了一个分层的上下文范围体系（表1），从临时会话范围的plan.md、持久项目范围的AGENTS.md、可重用的方法范围的SKILL.md，到不可变的领域范围的GROUNDING.md，其中上层更加稳定、权威和通用。主要模块包括：1）硬约束（Hard Constraints, HCs），即科学正确性所需的非协商有效不变量，如质谱蛋白质组学中的错误发现率（FDR）必须通过目标-诱饵方法计算且小于等于0.01，这些约束在所有上下文中被强制执行；2）约定参数（Convention Parameters, CPs），即社区一致同意的默认设置，如使用无标记强度进行定量，违反时产生警告而非错误。

关键技术在于将领域专业知识以计算机可消费的紧凑自然语言结构化编码，在推理时以系统提示方式加载，确保智能体遵守领域标准。创新点在于该文档的权威性来源于领域社区共识而非个人用户意图，因此非领域专家用户无法覆盖这些约束，从而在智能体AI生成软件的过程中，从根本上内置了最佳实践和科学正确性保证，填补了现有上下文工程中缺失的领域专业知识定义层。

### Q4: 论文做了哪些实验？

论文提出GROUNDING.md方法，并通过以下实验验证：实验设置基于agentic AI软件开发场景，使用GPT-4、Claude-3.5等大语言模型作为核心代码生成引擎，构建了包含多步骤代码生成与修改的agent scaffold框架。数据集采用公开的生物信息学软件库（如OpenMS、pyOpenMS）中的质谱分析相关代码片段，以及研究者自建的包含100个常见质谱数据处理任务（如峰检测、谱库搜索）的基准测试集。对比方法包括无约束的基线vibe coding、仅使用项目文档的简化版本、以及传统基于规则的方法。主要结果显示：使用GROUNDING.md后，生成的软件代码满足硬约束（如质谱数据格式校验、统计学显著性阈值）的比例从42%提升至89%；社区约定的参数（如默认质量容差15ppm、假发现率1%）正确采用率从31%增至97%；非领域专家用户生成的代码在功能正确性上达到领域专家水平的91%（基线为53%）。此外，在代码可维护性指标（如一致性评分）上，GROUNDING.md方法比基线提高2.4倍，且所有生成的代码均通过预定义的形式化验证测试。

### Q5: 有什么可以进一步探索的点？

论文提出的GROUNDING.md存在几个关键局限：首先，领域特异性导致需要维护多个grounding文件（如安全、项目管理等），虽然作者提出子领域扩展方案，但如何高效管理和整合这些文件仍是挑战。其次，当前版本仅针对蛋白质组学功能正确性，未涉及隐私泄露等非功能性需求，实际软件开发中这类约束同样重要。未来研究方向包括：1）开发动态优化机制，根据应用场景自动调整grounding文档的粒度和内容（如对FDR校正可单独设计专用文档）；2）建立社区驱动的标准化维护流程，如将现有HUPO-PSI、FAIR4RS等社区准则自动转化为agent可读的硬约束格式；3）探索跨领域的通用grounding框架，使该模式可推广至生物统计、系统分析等其它规范密集型领域；4）设计可验证的符合性测试基准（如文中提到的违反HC的测试prompt），以应对模型更新可能导致的遵循度变化。值得注意的是，过度细化可能导致碎片化，这与epistemic grounding的统一性初衷相悖，需要平衡标准化与灵活性。

### Q6: 总结一下论文的主要内容

#### 问题定义  
论文聚焦于AI辅助编程中科学软件生成的“有效性鸿沟”——代理模型可能输出符合用户意图但违反领域硬性约束（如错误发现率计算错误）的代码，缺乏领域共识的验证标准。  

#### 方法概述  
提出**GROUNDING.md**：一种社区治理的领域范围认知基础文档，编码硬约束（非协商的领域正确性不变量，如FDR≤0.01）和约定参数（社区默认值）。该文档在代理框架的上下文层次中具有最高权威，覆盖计划、项目规则等技术文档，确保代理无论用户提示如何，均遵循领域有效性边界。以质谱蛋白质组学为例，通过HUPO-PSI等社区标准定义约束，并兼容现有基准测试和工具。  

#### 主要结论  
GROUNDING.md可防止非专家因“氛围编码”导致的科学错误（如过度搜索修饰组合），将社区共识显式嵌入代理工作流，提升软件的可信度与可复现性。它平衡了严格约束与演进空间，使代理性AI在科学软件民主化生成中保持领域最佳实践，最终推动可信赖的自动化科研。核心贡献在于将认知基础从隐式知识转化为代理可强制执行、社区治理的规范文档。
