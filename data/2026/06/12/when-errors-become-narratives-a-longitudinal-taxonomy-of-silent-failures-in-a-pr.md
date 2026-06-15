---
title: "When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime"
authors:
  - "Wei Wu"
date: "2026-06-12"
arxiv_id: "2606.14589"
arxiv_url: "https://arxiv.org/abs/2606.14589"
pdf_url: "https://arxiv.org/pdf/2606.14589v1"
github_url: "https://github.com/bisdom-cell/openclaw-model-bridge"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.DC"
tags:
  - "LLM Agent运行时"
  - "静默故障"
  - "故障分类体系"
  - "生产环境研究"
  - "智能体可靠性"
  - "长期实证研究"
  - "故障预防与回归测试"
relevance_score: 8.5
---

# When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime

## 原始摘要

LLM agent systems increasingly run as long-lived autonomous runtimes: scheduling jobs, calling tools, maintaining memory, and pushing results to humans. We present a longitudinal study of silent failures in one such system: a personal-assistant agent runtime in continuous production since March 2026, with roughly 40 scheduled jobs, 8 LLM providers, a tool-governance proxy, and a knowledge-base memory plane, defended by 4,286 unit tests and 827 governance checks. Over eight weeks we documented 22 incidents with full root-cause postmortems, in which one meta-pattern -- a failure whose error signal never reaches a human in actionable form -- manifested at least 28 times. We derive a five-class, mechanism-oriented taxonomy: (A) environment and platform quirks, (B) design-assumption mismatches, (C) error swallowing and dilution, (D) chained hallucination and fabrication, (E) operational omission and forensic blind spots. Class D is unique to LLM systems and the most dangerous: the system does not merely fail to report an error -- the LLM transforms it into fluent, plausible narrative delivered to the user. We term this fail-plausible: gray failure's differential observability escalated -- the observer is not just blind, it is convincingly lied to by the failure itself. Three findings: about 70% of silent failures were caught by human user-view observation, not tests or audits; a retrospective audit of 15 incidents found 0% ex-ante prevention but 87% regression blocking -- audits are regression engines, not prediction engines; incident latency (13 hours to 60 days) tracks failure mechanism, not code complexity -- the longest-lived failures lived in the seams between components, where no test runs. We describe the resulting defense framework and distill design principles for agent systems whose failures are loud, attributable, and boring. All postmortems and artifacts are public.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在大规模生产环境中，LLM智能体运行时系统长期存在的静默故障问题。研究背景是，随着LLM智能体系统越来越多地被部署为长期运行的自主动作运行时（如调度任务、调用工具、维护记忆等），其可靠性挑战日益凸显。现有方法主要关注系统崩溃等显性故障，但更隐蔽的“灰度故障”已通过差分可观测性机制导致系统受损而观测器却无所察觉。LLM系统在此基础上引入了一种全新的、更危险的故障模式：当上游错误泄漏到LLM上下文窗口时，系统并不会沉默，而是会生成流畅、看似可信的虚假输出（如虚构行业分析报告），作者将其命名为“fail-plausible”（可信故障）。这种故障不仅让检测器失明，还向用户输送了令人信服的谎言。本文的核心问题是：通过对一个自2026年3月起持续运行的个人助手智能体运行时（包含约40个定时任务、8个LLM供应商、工具治理代理和知识库内存平面，配备4286个单元测试和827个治理检查）进行为期八周的纵向研究，系统性地分类、量化和防御这类静默故障。研究基于22个完整根因分析的故障事件，提出了一个包含五类机制导向的分类法，并揭示了故障延迟（13小时至60天）、发现渠道（约70%依赖人工观察）等关键发现，最终提出防御框架和设计原则。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1. **系统故障分类研究**：Huang等人提出灰色故障（gray failure）概念，描述组件退化但检测器报告正常的现象；Gunawi等人的fail-slow研究收集了101-114个硬件性能故障报告，建立了生产环境故障分类方法。本文方法上继承这一传统，但聚焦于LLM agent运行时而非云基础设施，且所有案例均为静默故障。

2. **多Agent系统故障分类**：Cemri等人的MAST是首个多Agent LLM系统故障实证分类，识别了14种故障模式（规范问题、智能体间不匹配、任务验证问题），分析单元为基准任务轨迹。本文与MAST互补：MAST解释Agent集体为何无法完成任务，本文解释Agent系统为何在运行中未被察觉地失效。

3. **LLM推理服务故障研究**：近期有研究分析156个高严重性LLM推理事故，提出四类操作故障（基础设施、模型配置、推理引擎、操作故障）。该研究与本文共享生产事故基础，但覆盖Agent之下的推理服务层，故障表现为可用性和延迟违反——本质上是“响亮”的。

4. **Agent安全与异常处理**：Ezell等人提出Agent事故报告应包含的结构化信息；SHIELDA处理Agent工作流异常；AIR关注Agent安全事件响应；MCP生态有故障分类。这些工作均未聚焦静默/合理失败类别、延迟发现或防御框架演化。

5. **幻觉研究**：通常作为模型属性研究（无基础生成、事实性/忠实性分类、检测基准）。本文的D类将其重新定义为系统属性：4/4文档化编造案例中，模型行为完全符合训练（流畅完成上下文），故障在于系统传递了污染上下文（错误日志被命令替换捕获、过期告警消息遗留、跨日摘要无来源标记）。防御措施是系统层面的上下文卫生、来源标记和分层反编造防护。

### Q3: 论文如何解决这个问题？

该论文通过一项为期八周的生产系统纵向研究，提出了一种针对静默故障（silent failures）的因果导向五元分类法来解决这一问题。核心方法是对一个实际运行的LLM代理运行时系统进行持续的故障追踪和根因分析，该架构采用三平面设计：控制平面（含工具治理代理、声明式治理引擎含90个不变量和827项检查、SLO监控和断路器）、能力平面（跨8个提供商的适配器及自动回退链）和记忆平面（知识库RAG索引、对话收割与每日LLM合成任务）。系统底部是一个观测带，包含4286个单元测试和每日治理审计。研究团队记录了22起生产事故，并强制使用“异常分析章程”进行复盘，要求绘制完整的因果链图、识别三层根因（触发因素、放大因素、隐藏因素）和条件组合分析。关键创新是提出了五类机制导向的故障分类：（A）环境/平台怪癖，（B）设计假设不匹配，（C）错误吞噬与稀释，（D）链式幻觉与捏造（fail-plausible：系统不仅未报告错误，LLM还将其转化为流畅可信的叙述），（E）操作遗漏与取证盲点。其中D类是LLM系统独有的最危险类别，其防御重点在于系统侧上下文卫生（stderr纪律、警报剥离、来源标记和防污染提示守卫）。

### Q4: 论文做了哪些实验？

论文的核心实验是一项针对长期运行的生产级LLM Agent系统的纵向研究。该系统自2026年3月起持续运行，包含约40个定时任务、8个LLM提供商、一个工具治理代理及一个知识库内存平面，并受4286个单元测试和827项治理检查保护。在8周内，研究人员记录了22个完整根因分析的故障事件，识别出至少28次“静默失败”。

实验通过分析所有故障事件，衍生出一个五类机制导向的静默失败分类法：（A）环境与平台怪癖、（B）设计假设不匹配、（C）错误吞没与稀释、（D）链式幻觉与捏造、（E）操作遗漏与取证盲点。主要发现包括：约70%的静默失败是通过人类用户视角观察（每周检查实际输出）发现的，而非自动化测试或审计；对15个事件的回顾性审计显示，虽然未能实现任何事前预防（0%），但成功阻止了87%的回归问题，这表明审计是回归引擎而非预测引擎。故障潜伏期从13小时到60天不等，其长度与故障机制相关，而非代码复杂度，最持久的故障往往发生在组件间的“缝隙”中（无测试覆盖）。关键数据指标包括：22个故障事件、28次静默失败显现、70%的人类发现率、0%的事前审计预防率以及87%的回归阻止率。实验最终提出了一种防御框架和使系统失败“响亮、可归因且无聊”的设计原则。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于其分类框架基于单一生产系统（个人助手Agent运行时），结论的普适性需更广泛验证。未来可探索方向包括：（1）针对Class D“可信错误叙事”，设计对抗性测试框架，通过注入已知失败模式检测LLM是否会产生“叙事化”掩盖行为；（2）将纵向研究中发现的“用户视角检测（~70%）”转化为自动化检测信号，例如构建多模态异常监控系统，同时捕捉语言流畅性与工具调用结果不一致；（3）解决“审计作为回归引擎而非预测引擎”的困局，开发预测性失效模型，例如基于组件间交互频次与历史错误模式的图神经网络，提前识别组件“缝隙”中的长潜伏期故障。此外，可探究“失败信号稀释”在多层LLM管道中的级联效应，以及设计明确的“失败可观测性契约”来替代当前的被动防御架构。

### Q6: 总结一下论文的主要内容

本文针对LLM代理系统在生产环境中长期运行时的无声故障问题，进行了为期八周的纵向研究，记录了22个完全因果链故障事件。核心贡献包括：（1）提出一个五类机制导向的故障分类法，包含环境与平台异常、设计假设不匹配、错误吞噬与稀释、链式幻觉与捏造、操作遗漏与取证盲点；（2）发现并命名"可信失败"故障模式，即LLM将内部错误转化为流畅、合理但虚假的输出传递给用户；（3）量化发现约70%的无声故障由人类用户视角观察发现，而非测试或审计；审计仅为回归引擎而非预测引擎；故障延迟时间由机制决定，而非代码复杂度。研究表明，LLM代理系统的可靠性应优先减少组件间"缝隙"而非增加防御措施，并提出了相应的防御框架和"日落定律"设计原则。
