---
title: "SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents"
authors:
  - "Yipeng Ouyang"
  - "Yi Xiao"
  - "Yuhao Gu"
  - "Xianwei Zhang"
date: "2026-05-05"
arxiv_id: "2605.03353"
arxiv_url: "https://arxiv.org/abs/2605.03353"
pdf_url: "https://arxiv.org/pdf/2605.03353v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent技能编译"
  - "跨框架Agent部署"
  - "Agent安全"
  - "中间表示"
  - "Agent技能封装"
  - "编译器方法"
relevance_score: 9.5
---

# SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents

## 原始摘要

LLM-Agents have evolved into autonomous systems for complex task execution, with the SKILL.md specification emerging as a de facto standard for encapsulating agent capabilities. However, a critical bottleneck remains: different agent frameworks exhibit starkly different sensitivities to prompt formatting, causing up to 40% performance variation, yet nearly all skills exist as a single, format-agnostic Markdown version. Manual per-platform rewriting creates an unsustainable maintenance burden, while prior audits have found that over one third of community skills contain security vulnerabilities. To address this, we present SkCC, a compilation framework that introduces classical compiler design into agent skill development. At its core, SkIR - a strongly-typed intermediate representation - decouples skill semantics from platform-specific formatting, enabling portable deployment across heterogeneous agent frameworks. Around this IR, a compile-time Analyzer enforces security constraints via Anti-Skill Injection before deployment. Through a four-phase pipeline, SkCC reduces adaptation complexity from $O(m \times n)$ to $O(m + n)$. Experiments on SkillsBench demonstrate that compiled skills consistently outperform their original counterparts, improving pass rates from 21.1% to 33.3% on Claude Code and from 35.1% to 48.7% on Kimi CLI, while achieving sub-10ms compilation latency, a 94.8% proactive security trigger rate, and 10-46% runtime token savings across platforms.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决跨框架LLM agent系统中技能（skill）的“可移植性”和“安全性”两大核心问题。研究背景是：当前存在如Claude Code、OpenAI Codex等多种agent框架，但不同框架对技能提示的格式极其敏感，格式差异可导致高达40%的性能波动。然而，现有技能生态普遍采用单一的、与格式无关的Markdown版本（SKILL.md），手动为每个平台重写技能会产生难以持续的维护负担。同时，安全漏洞问题同样严峻，社区审计发现超过三分之一的技能存在安全漏洞。因此，论文要解决的核心问题是：如何设计一种机制，使得一个技能能高效、安全地部署到格式敏感性各异的异构agent框架上，在降低跨平台适配复杂度的同时，确保技能的安全性。

### Q2: 有哪些相关研究？

与本文相关的研究主要分为三类：**代理技能结构与检索**、**结构化提示与格式敏感性**、**代理与技能的编译技术**。

在**代理技能结构与检索**方面，Agent Skills标准提出了SKILL.md规范，EvoSkill通过自动发现和迭代优化扩展了技能范式。近期工作还探索了基于生成、增强、图谱和嵌入的技能检索方法，并系统评估了实际检索条件下的技能表现。但这些工作均假设技能格式无关，忽视了不同LLM对格式的强偏好。

**结构化提示与格式敏感性**领域，He等人发现格式变化可导致高达40%的性能差异，Liu等人提出了内容-格式联合优化方法(CFPO)。Anthropic证实XML标签能提升Claude 23%的准确率，而YAML在嵌套数据中解析准确率最高(51.9%)。安全方面，Snyk's ToxicSkills发现37%的社区技能存在漏洞。这些研究为SkCC的平台特定发射策略与编译时安全分析提供了依据。

**代理与技能的编译技术**中，Mikek等人展示了编译器-LLM协作可优化代理代码，Kim等人利用编译器编排实现高效并行函数调用。最相关的是SkVM，它将编译概念引入技能领域，提出类JVM架构，但聚焦于语义退化而非格式适配，且未集成安全加固。SkCC创新性地引入经典多阶段编译器架构，通过共享中间表示(IR)解耦技能语义与平台格式，并利用编译时分析实现安全约束检查，将适配复杂度从O(m×n)降至O(m+n)。

### Q3: 论文如何解决这个问题？

SkCC通过引入经典编译器设计解决了LLM-Agent技能开发中的跨框架适配和安全性两大挑战。其核心创新是SkIR（强类型中间表示），它将技能语义与平台特定格式解耦，使编译后的技能可跨异构框架移植。

整体架构是一个四阶段编译流水线：1）**前端阶段**对SKILL.md进行词法分析和解析，将YAML元数据反序列化为静态路由表，对Markdown主体进行抽象语法树（AST）降级，并计算SHA-256哈希确保可重复编译；2）**IR构建阶段**将原始AST转换为强类型、平台无关的SkIR，组织为六类信息（元数据、接口、安全控制、执行逻辑、编译器注入约束、AST优化标志），并支持四种执行模式，同时通过嵌套数据检测决定是否使用YAML优化；3）**分析器阶段**依次执行结构验证、依赖验证、权限审计、抗技能注入（Anti-Skill Injection）和安全分级，其中抗技能注入通过AST遍历自动扫描危险模式并注入约束，实现了94.8%的主动安全触发率；4）**后端阶段**通过多态发射器生成平台原生格式（XML语义分层、XML标记Markdown、Markdown+条件YAML、全Markdown保留）。

关键技术创新包括：通过共享IR将适配复杂度从O(m×n)降至O(m+n)；编译时安全强化避免了运行时依赖LLM判断不可靠的问题；渐进式路由清单仅暴露轻量元数据。实验显示编译后技能在Claude Code和Kimi CLI上通过率分别提升12.2%和13.6%，编译延迟小于10ms，跨平台节省10-46%运行时token。

### Q4: 论文做了哪些实验？

论文在 SkillsBench 基准上进行了系统性实验，包含89个真实编程和数据分析任务，使用Pass@1作为主要指标。实验对比了SkCC编译后技能（Compiled）与原始SKILL.md技能（Original）在四个主流智能体框架上的表现：Claude Code (claude-opus-4-6)、Kimi CLI (kimi-k2.5)、Codex CLI (gpt-5.3-codex)、Gemini CLI (gemini-2.5-pro)。主要结果：Claude Code上Compiled的通过率从21.1%提升至33.3%（+12.2pp）；Kimi CLI上从35.1%提升至48.7%（+13.5pp）；Codex CLI上从38.5%提升至42.3%（+3.8pp）；Gemini CLI上保持22.2%不变。消融实验证明编译收益是模型特定的：同一Kimi编译格式在kimi-k2.5上有显著提升（p=0.0063），但对glm-5.1和deepseek-v4-flash影响不显著。工程性能上，编译延迟低于10ms，安全规则触发率达94.8%，并在各平台上实现10-46%的运行时token节省。与Liu等人的检索式优化方法相比，SkCC在Claude和Kimi上分别取得+12.2pp和+13.5pp的绝对提升，远超对比方法的+8.1pp和+3.3pp。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可进一步探索的方向包括：1) **自动反模式发现**：当前安全审计依赖预定义规则，未来可从大规模漏洞语料库中自动学习攻击模式，提升对未知注入的检测能力。2) **语义级自适应**：现有编译优化主要针对格式敏感性，可结合运行时反馈（如模型输出质量）实现动态提示工程，例如根据执行历史调整指令顺序或采用示例学习风格。3) **生态系统集成**：通过WebAssembly绑定实现实时IDE验证，使开发者能在编写技能时即刻获得编译时安全警告。4) **跨框架泛化性**：当前实验限于四种框架，需验证SkIR对更异构的Agent框架（如AutoGPT、LangGraph）的适配能力。5) **编译时与运行时结合**：可探索将部分安全检查延迟到运行时，例如针对动态反射调用的注入检测，以平衡编译速度与防护完备性。

### Q6: 总结一下论文的主要内容

SkCC提出了一个针对跨框架LLM Agent的便携式安全技能编译框架。其核心问题在于不同Agent框架对提示格式的敏感性差异巨大，导致性能波动最高达40%，且社区技能中存在超三分之一的安全漏洞。方法上，SkCC引入经典编译器设计，通过强类型中间表示SkIR解耦语义与平台格式，实现可移植性；编译时分析器通过Anti-Skill Injection在部署前强制执行安全约束。核心贡献是将适应复杂度从O(m×n)降至O(m+n)。实验表明，编译后的技能在Claude Code上的通过率从21.1%提升至33.3%，在Kimi CLI上从35.1%提升至48.7%，编译延迟低于10毫秒，主动安全触发率达94.8%，并实现10-46%的运行token节省。该工作标志着从手动重写向编译器驱动的系统化适配的范式转变，对Agent生态的安全性、可移植性和工具链演进具有重要价值。
