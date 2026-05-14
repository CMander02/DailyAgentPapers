---
title: "No Attack Required: Semantic Fuzzing for Specification Violations in Agent Skills"
authors:
  - "Ying Li"
  - "Hongbo Wen"
  - "Yanju Chen"
  - "Hanzhi Liu"
  - "Yuan Tian"
  - "Yu Feng"
date: "2026-05-13"
arxiv_id: "2605.13044"
arxiv_url: "https://arxiv.org/abs/2605.13044"
pdf_url: "https://arxiv.org/pdf/2605.13044v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent Safety"
  - "Specification Violation"
  - "Semantic Fuzzing"
  - "Agent Skill Security"
  - "Benchmark"
relevance_score: 9.0
---

# No Attack Required: Semantic Fuzzing for Specification Violations in Agent Skills

## 原始摘要

LLM-powered agents can silently delete documents, leak credentials, or transfer funds on a routine user request, not because the agent was attacked, but because the skill it invoked broke its own declared safety rules. We call these specification violations: benign inputs cause a skill to breach the natural-language guardrails in its own specification, typically because the guardrail's semantics are undefined for autonomous execution, or because the implementation silently ignores the documented constraint. These violations are invisible to static analyzers, traditional fuzzers, and prompt-injection defenses alike, yet they undermine the very contract a user trusts when installing a skill.
  We present Sefz, a goal-directed semantic fuzzing framework that automatically discovers specification violations in agent skills. Sefz translates each guardrail into a reachability goal over an annotated execution trace, reducing violation checking to a deterministic graph query. An LLM-based mutator generates benign inputs whose traces progressively approach the violation patterns, guided by a multi-armed bandit that uses goal-proximity as its reward signal.
  On 402 real-world skills from the largest public agent-skill marketplace, Sefz finds specification violations in 120 (29.9%), including 26 previously unknown exploitable guardrail violations in deployed skills. Six recurring specification pitfalls explain the bulk of the failures, suggesting concrete principles for safer skill design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决由大语言模型驱动的智能体在执行技能时，因技能本身违反其声明的自然语言安全规则（即“规格违规”）而引发的安全问题。研究背景是：随着智能体技能生态系统的快速发展，技能通过自然语言指令和可选脚本定义其功能与安全约束（如“操作前需用户确认”）。现有方法的不足在于：静态分析无法捕捉自然语言规则与运行时行为之间的语义差距；传统的模糊测试和提示注入检测主要针对恶意输入，无法识别由良性用户输入触发的违规；而基于LLM的审计也难以系统性地发现此类隐蔽缺陷。核心问题是：当智能体遵守用户指令，但所调用的技能在执行时，其行为与自身声明的自然语言约束相矛盾（例如，本应要求确认的解锁操作直接执行），造成安全承诺的失效。这些违规行为在常规使用中即可发生，无需任何攻击，却可能引发数据删除、凭证泄露或资金转移等严重后果。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：

**方法类研究**：传统的静态分析工具（如程序验证器）和动态模糊测试工具（如AFL、LibFuzzer）无法检测这类规范违反，因为它们依赖形式化规约，无法处理自然语言语义的歧义性。本文提出的Sefz框架与这些方法不同，它通过将自然语言护栏转化为可达性目标，并利用LLM和MAB进行语义引导的模糊测试，专门针对技能规范中的语义漏洞。

**安全与防御类研究**：提示注入防御（如OpenAI的审核系统）关注对抗性输入造成的越狱攻击，但本文的规范违反是由良性用户输入触发，且根因在于技能设计本身（护栏语义未定义或实现忽略限制）。因此，现有防御无法覆盖此类漏洞，本文首次系统性地识别并检测这些“无需攻击”的漏洞。

**应用与评测类研究**：现有agent技能市场（如ClawHub）缺乏对规范合规性的自动化验证，开发者主要依赖人工审核。本文通过对402个真实技能的评测（发现29.9%含规范违反），揭示了六种典型的规格设计陷阱（如歧义护栏、规格-实现不匹配、工作流级权限升级），为更安全的技能设计提供了具体原则。

### Q3: 论文如何解决这个问题？

Sefz提出了一个目标驱动的语义模糊测试框架，能够自动发现Agent技能中的规范违反问题。其核心方法包含三个关键组件：首先，通过**守卫规则分解**模块，将自然语言编写的安全守卫规则转化为可验证的可达性目标。具体做法是引入一个中间表示——约束骨架，由LLM提取触发动作、角色、门控和参数四个槽位，再通过确定性匹配将其映射为三类达成目标（未经确认的操作、数据泄露、权限提升），从而弥合语义鸿沟。其次，**语义变异**模块基于LLM的变异算子对种子输入进行语义层面的扰动，产生新的良性用户请求。每个变异算子对应一种绕过手段，并用汤普森采样调度器根据目标接近度奖励信号动态选择最有效的变异策略。最后，**验证器**将Agent执行过程记录为带安全谓词注释的执行轨迹图，通过图查询判断轨迹是否匹配可达性目标。若匹配则报告为违反，同时计算接近度分数反馈给调度器，形成封闭的模糊测试循环。为保证结果鲁棒性，Sefz会在沙箱中多次执行同一输入并合并轨迹。这一框架的关键创新在于将规范违反检测转化为图上的可达性查询问题，而非依赖静态分析或提示注入防御，从而能发现因LLM对规则解释不一致或实现与规范不匹配导致的隐蔽违反。

### Q4: 论文做了哪些实验？

Sefz在最大公开智能体技能市场（PlugsHub）的402个真实技能上进行实验。设置包括：将每个技能的安全护栏转化为可达性目标，基于带注释的执行轨迹进行确定性图查询，使用LLM变异器生成良性输入，并由多臂老虎机以目标接近度为奖励信号引导变异方向。对比方法包括传统模糊测试（如随机输入生成）和提示注入防御，但论文主要聚焦于Sefz本身的特异性。主要结果：Sefz在120个技能（29.9%）中发现规范违反，其中26个是已部署技能中先前未知的可利用护栏违反。关键数据指标：发现6种重复出现的规范缺陷模式解释了大部分失败，例如护栏语义未定义或实现静默忽略文档化约束。实验表明，传统静态分析、模糊测试和提示注入防御对此类违规无效，而Sefz通过目标导向的语义变异能自动、高效地揭示深层安全隐患。

### Q5: 有什么可以进一步探索的点？

该工作的主要局限在于仅关注了单次技能执行中的语义违规，未考虑多技能组合或顺序调用时的复合违规场景。未来可探索：1）将语义模糊测试扩展到跨技能交互图，检测当多个技能链式执行时，各自安全的输入组合是否触发复合型违规；2）当前基于LLM的变异器依赖预定义引导策略，可引入对抗性训练或元学习，使变异器自主发现更隐蔽的、违反未明确定义约束的边界案例；3）仅检测自然语言护栏与实现间的语义偏差，未覆盖护栏本身的设计缺陷（如过度宽松或含糊的规则）。改进思路包括将形式化验证与模糊测试结合，利用符号执行枚举护栏的语义覆盖范围，或通过反事实推理生成违反人类直觉但技术合规的异常轨迹。此外，对158种未发现违规的技能进行反向分析，可能揭示其护栏设计的鲁棒性规律，为自动化生成防御性护栏提供基础。

### Q6: 总结一下论文的主要内容

论文提出了一种新的漏洞类型——“规约违反”（specification violations），即在没有恶意攻击的情况下，LLM智能体的技能在执行良性用户请求时，会违背其自身的自然语言安全约束（guardrails）。这类漏洞源于自然语言约束的语义歧义、规约与实现的不匹配，或组合操作产生的安全间隙，且静态分析、传统模糊测试和提示注入防御均无法检测。

本文提出Sefz，一种目标导向的语义模糊测试框架。其核心方法是：将每个安全约束翻译成带注释执行迹（annotated execution trace）上的可达性目标（reachability goals），从而将违规检测转化为确定性图查询；通过基于大语言模型的变异算子生成良性输入，并由多臂老虎机（multi-armed bandit）以目标接近度为奖励信号来引导探索，系统性地发现违规。

在402个真实世界技能上的评估表明，Sefz在29.9%的技能中发现了规约违反，其中包括26个已部署技能中的零日漏洞。研究还归纳出六种重复出现的规约缺陷模式，为设计更安全的智能体技能提供了具体指导原则。该工作首次系统性地定义并自动化检测了LLM智能体技能中的规约违反问题，对智能体生态系统的安全性具有重要意义。
