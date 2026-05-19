---
title: "SaaSBench: Exploring the Boundaries of Coding Agents in Long-Horizon Enterprise SaaS Engineering"
authors:
  - "Qingnan Ren"
  - "Shun Zou"
  - "Shiting Huang"
  - "Ziao Zhang"
  - "Kou Shi"
  - "Zhen Fang"
  - "Yiming Zhao"
  - "Yu Zeng"
  - "Qisheng Su"
  - "Lin Chen"
  - "Yong Wang"
  - "Zehui Chen"
  - "Xiangxiang Chu"
  - "Feng Zhao"
date: "2026-05-17"
arxiv_id: "2605.17526"
arxiv_url: "https://arxiv.org/abs/2605.17526"
pdf_url: "https://arxiv.org/pdf/2605.17526v1"
github_url: "https://github.com/ShadeCloak/SaaSbench"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Coding Agent Benchmark"
  - "Enterprise SaaS"
  - "Long-Horizon Tasks"
  - "Multi-Component Integration"
  - "System-Level Complexity"
  - "Dependency-Aware Evaluation"
  - "Code Generation"
  - "Agent Evaluation"
relevance_score: 9.5
---

# SaaSBench: Exploring the Boundaries of Coding Agents in Long-Horizon Enterprise SaaS Engineering

## 原始摘要

As autonomous coding agents become capable of handling increasingly long-horizon tasks, they have gradually demonstrated the potential to complete end-to-end software development. Although existing benchmarks have recently evolved from localized code editing to from-scratch project generation, they remain confined to structurally simplified, single-stack applications. Consequently, they fail to capture the heterogeneous environments, full-stack orchestration, and system-level complexity of real enterprise Software as a Service (SaaS) systems, leaving a critical gap in assessing agents under realistic engineering constraints. To fill this gap, we introduce SaaSBench, the first benchmark designed to explore the boundaries of AI agents in enterprise SaaS engineering. Spanning 30 complex tasks across 6 SaaS domains with 5,370 validation nodes, it incorporates 8 programming languages, 6 databases, and 13 frameworks to meticulously mirror real-world software heterogeneity. Furthermore, we design a dependency-aware hybrid evaluation paradigm tailored for complex systems with long horizons and multi-component coupling, enabling fine-grained, reproducible assessment. Crucially, our extensive experiments reveal a striking insight: the primary bottleneck for state-of-the-art agents is not generating isolated code logic, but successfully configuring and integrating a multi-component system. Over 95\% of task failures occur before agents even reach deep business logic, with models often falling victim to overconfidence and prematurely halting during foundational system setup, or getting trapped in ineffective debugging loops. We hope SaaSBench serves as a practical and challenging testbed to drive the evolution of reliable, system-level coding agents. The code is available at \url{https://github.com/ShadeCloak/SaaSbench}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有 AI 编码智能体基准测试无法真实评估其在企业级软件即服务（SaaS）工程中表现的问题。研究背景是，随着自主编码智能体的能力提升，它们已能处理较长期任务，并展现出完成端到端软件开发的潜力。然而，现有的基准测试虽然从局部代码编辑发展到从零生成项目，但仍局限于结构简化、单一技术栈的应用。这导致它们无法捕捉真实企业 SaaS 系统的异构环境、全栈编排和系统级复杂性，从而在评估智能体面对现实工程约束时存在关键缺口。现有方法的主要不足包括：缺乏真实市场背景、系统复杂度有限（通常仅涉及单一语言或组件）、以及评价机制不足（多依赖扁平化的端到端信号，如单元测试通过率，无法表征复杂业务流程中的依赖关系）。本文要解决的核心问题是：如何构建一个能全面、真实评估编码智能体完成从零到一的长期企业 SaaS 工程任务能力的基准测试平台，并揭示当前最先进智能体在该场景下的主要瓶颈。为此，论文提出了 SaaSBench，这是一个首个系统化设计用于评估智能体在企业级 SaaS 开发中表现的基准，包含多领域复杂任务，并设计了依赖感知的混合评估范式。

### Q2: 有哪些相关研究？

相关研究可以分为三个类别。首先，在自主编码智能体方面，现有工作包括IDE集成助手（如Cursor、Claude Code、Codex）和面向自主性的框架（如OpenHands、Qwen-Agent、SWE-agent）。前者从代码补全演进到跨文件编辑，后者通过统一智能体循环支持长周期规划与调试。本文与这些工作均关注提升智能体的系统级工程能力，但SaaSBench侧重于评估而非方法设计，且聚焦于企业级SaaS场景的异构性与长周期耦合。其次，在代码中心基准测试方面，早期工作如HumanEval、MBPP、APPS等仅评测函数级代码生成。后续RepoBench、SWE-Bench扩展到真实代码仓库的编辑与问题修复。最新的NL2Repo-Bench、PRDBench、RepoGenesis和ProjDevBench要求从零构建完整项目。但这些基准仍局限于单栈应用或简单项目，缺乏企业SaaS的多语言、多数据库、多框架异构环境及交互式依赖验证。SaaSBench是首个针对企业SaaS工程的长周期、多组件耦合基准，并设计了依赖感知的混合评估范式，填补了这一空白。

### Q3: 论文如何解决这个问题？

SaaSBench通过构建一个覆盖真实企业级SaaS开发全流程的基准测试平台来解决现有评估方案的核心缺陷。整体框架由三部分组成：基于真实市场的任务集合、标准化运行时环境以及依赖感知的混合评估范式。

核心方法是从6个主流SaaS领域（如CRM、ERP等）精选30个复杂任务，每个任务包含平均4363行长上下文的产品需求文档（PRD）、歧义消解知识库、标准运行环境（覆盖8种编程语言、6种数据库和13种框架）。关键技术在于设计了基于有向无环图（DAG）的依赖感知混合评估机制：每个验证节点被编译成由可执行原语组成的线性检查链，通过前置依赖门控、失败传播控制和三级评分机制（二元/加权/LLM裁判）实现细粒度可复现评估。验证节点覆盖六大能力维度：部署可用性、数据建模、API契约一致性、业务逻辑正确性、访问控制和工程质量。

主要创新点包括：1）首次将市场真实性纳入基准设计，任务源自真实开源SaaS产品；2）系统性模拟企业级异构环境，包含5370个验证节点；3）提出支持长周期多组件耦合系统的DAG评估范式，解决了传统端到端信号无法刻画工作流依赖关系的问题。实验表明，95%以上的任务失败发生在系统配置与集成阶段而非深度业务逻辑生成，揭示了当前最先进编码智能体的核心瓶颈在于跨组件协同配置能力。

### Q4: 论文做了哪些实验？

论文在 SaaSBench 基准上进行了全面实验。实验设置了 30 个跨 6 个 SaaS 领域的复杂任务（包括客户增长、生产力协作、商业金融、数据基础设施、安全身份、领域工作流），包含 5370 个验证节点。采用两种代表性编码智能体框架：OpenHands 和 Claude Code，并评估了 8 个大模型后端（GPT-5.4、Gemini 3.1 Pro、Claude Opus 4.7 等）。主要指标为 Pass@1 和节点覆盖率。

主要结果：Claude Code + Claude Opus 4.7 取得最佳整体 Pass@1（20.68%），DeepSeek V4 Pro 和 GLM 5.1 在 OpenHands 下分别达 10.97% 和 10.23%。平均性能 Claude Code（11.64%）高于 OpenHands（9.26%）。按领域，模型在安全基础设施（SI）和数据基础设施（DCI）表现较好，在商业金融（CF）和生产力协作（PC）表现较弱。细粒度分析显示，质量维度得分最低（约2-3%），部署维度最高（约20%）。智能体平均执行步骤36-279步，消耗1.4M-24.4M tokens，耗时7分钟至2小时以上。关键发现：95.6%的任务失败发生在智能体触及深层业务逻辑之前，主要卡在系统配置和集成阶段。

### Q5: 有什么可以进一步探索的点？

虽然SaaSBench在评估企业级SaaS工程能力上迈出了重要一步，但其局限性同样值得关注。首先，当前30个任务虽覆盖6个领域，但样本量仍显不足，未来可扩展至更多行业场景（如金融、医疗）以验证泛化性。其次，基准测试聚焦于从头构建完整系统，但企业实际开发中常涉及遗留系统维护、API迁移等增量任务，这些场景未被涵盖。第三，评估指标主要基于功能正确性，而代码性能、安全性和可维护性等非功能属性尚未纳入，建议引入运行时资源消耗和漏洞扫描等维度。此外，论文揭示了95%的失败源于基础环境配置与集成，暗示现有智能体在系统级抽象理解上的短板。未来可探索：1）设计渐进式课程，从单服务配置逐步过渡到多服务编排；2）引入环境模拟器让智能体在失败后能回滚重试；3）结合人类反馈的强化学习，在配置阶段提供结构化提示而非自由文本。这些方向有望推动编码智能体从“代码生成器”进化为真正的“系统架构师”。

### Q6: 总结一下论文的主要内容

本文提出了SaaSBench，首个用于评估AI智能体在企业级SaaS工程中能力的基准。现有基准局限于单栈、结构化简单的应用，无法反映真实企业系统的异构性、全栈编排和系统级复杂性。针对此问题，SaaSBench设计了30个跨6个领域的复杂任务，包含5370个验证节点，涵盖8种编程语言、6种数据库和13种框架。主要方法包括依赖感知的混合评估范式，支持细粒度、可重复的评估。实验揭示核心瓶颈并非生成孤立代码逻辑，而是配置和集成多组件系统，超过95%的任务失败发生在触及深层业务逻辑之前，模型常因过度自信过早停止或陷入低效调试循环。该基准推动了面向系统级编码智能体的发展。
