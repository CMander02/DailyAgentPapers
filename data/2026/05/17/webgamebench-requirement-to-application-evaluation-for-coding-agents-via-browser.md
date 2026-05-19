---
title: "WebGameBench: Requirement-to-Application Evaluation for Coding Agents via Browser-Native Games"
authors:
  - "Wenyu Zhang"
  - "Guoliang You"
  - "Tianlun"
  - "Haotian Zhao"
  - "Tianshu Zhu"
  - "Haoran Wang"
  - "Xiaoxuan Tang"
  - "Mingyang Dai"
  - "Jingnan Gu"
  - "Daxiang Dong"
  - "Jianmin Wu"
date: "2026-05-17"
arxiv_id: "2605.17637"
arxiv_url: "https://arxiv.org/abs/2605.17637"
pdf_url: "https://arxiv.org/pdf/2605.17637v1"
categories:
  - "cs.AI"
tags:
  - "coding agent"
  - "agent benchmark"
  - "requirement-to-application"
  - "code generation evaluation"
  - "web-based game"
relevance_score: 7.5
---

# WebGameBench: Requirement-to-Application Evaluation for Coding Agents via Browser-Native Games

## 原始摘要

Coding agents are increasingly used as application builders, yet many evaluations still focus on source code, repository-level tests, or intermediate traces rather than the delivered application. We introduce WebGameBench, a requirement-to-application benchmark that evaluates whether coding agents can turn a frozen Structured WebGame Specification into a browser-accessible game. Browser-native games provide a compact but behavior-dense testbed: even simple games require coordinated input handling, spatial mapping, rule execution, state transitions, terminal conditions, restart behavior, and visible feedback. In WebGameBench, each generated artifact is built, served, and exposed as a browser-accessible application under a unified deployment protocol. A runtime evaluator then interacts with the delivered game in a real browser and assigns a three-way label: EXCELLENT, USABLE, or UNUSABLE. On a human-reviewed subset, the runtime label is broadly aligned with human gameplay review under the Usable-rate criterion. Across 111 tasks, 12 coding agents, and 14 evaluation configurations, WebGameBench separates current systems: the best configuration reaches a 76.9% usable rate but only a 20.2% excellent rate. This gap shows that crossing the minimum playable-delivery threshold is still far from complete requirement satisfaction. To our knowledge, WebGameBench is the first requirement-to-application benchmark for browser-native game delivery that validates delivered-application runtime labels against independent human gameplay review under the Usable-rate criterion.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有编码智能体评估基准的局限性。当前主流评估（如HumanEval、SWE-bench、WebArena）主要聚焦于源代码正确性、仓库级补丁、终端输出或现有环境中的任务完成度，这些方法均未直接评估从需求到可交付交互式应用的完整流程。例如，一个项目可能成功安装、构建和渲染页面，但在输入处理、空间映射、规则执行、状态转换或视觉反馈等运行时行为上违背规范，而传统指标无法捕获此类缺陷。

针对这一问题，论文提出了 **WebGameBench**，首个面向浏览器原生游戏的“需求到应用”（requirement-to-application）基准。其核心创新在于：将评估单元从中间代码或部署成功性转变为**交付应用的实际运行时行为**。核心瓶颈在于开发一个可复现的评估框架，该框架需（1）减少对外部服务依赖，（2）支持统一轻量级部署，（3）通过真实浏览器交互实现自动化运行时验证。通过使用冻结的结构化游戏规范（Structure WebGame Specification）作为唯一任务契约，并设计三标签评估（EXCELLENT/USABLE/UNUSABLE），论文解决了“可构建性不等于可用性”的关键挑战，揭示了当前最强代理在达到最低可用阈值（76.9%）与完全满足需求（仅20.2%优秀率）之间的显著鸿沟。

### Q2: 有哪些相关研究？

论文的相关研究可归为三类：

1. **代码与软件工程基准**：如 HumanEval、MBPP、APPS、LiveCodeBench 等函数级基准，以及 SWE-bench、SWT-Bench、Terminal-Bench 等仓库级基准。WebGameBench 与这些工作的区别在于，它不关注源代码或仓库测试，而是评估最终交付的浏览器应用是否可玩，即“需求到应用”的完整流程。

2. **网页生成与计算机使用基准**：如 WebArena、VisualWebArena、WebVoyager 等评测模型生成网站或操作浏览器，以及 OSWorld、AndroidWorld 等环境。本文不同之处在于，WebGameBench 要求模型从结构化规范生成完整游戏，并通过真实浏览器交互评估应用质量，而非仅考察前端生成或环境操作。

3. **游戏交互基准**：如文本游戏、Minecraft 类环境、LLM/VLM 游戏套件等，通常评测智能体作为玩家的能力。WebGameBench 则转向“开发者”角色，评测模型生成可交付游戏的能力，并首次验证了运行时标签与人类游戏评审在“可用率”标准下的一致性。

总体而言，WebGameBench 填补了从需求到可交付浏览器游戏的自动化评估空白，强调端到端应用交付而非中间过程或玩家表现。

### Q3: 论文如何解决这个问题？

WebGameBench通过一个完整的“需求到应用”评估流水线解决编码智能体能否将结构化需求转化为可运行浏览器游戏的问题。整体框架包含三个明确分离的角色：任务定义、应用交付和运行时评判。

核心方法是：为每个任务生成一个冻结的结构化Web游戏规范（Structured WebGame Specification），编码智能体在统一环境中基于该规范生成浏览器原生应用源码，并通过统一部署协议将其暴露为可访问的URL。随后，一个基于Codex的运行时评估器通过Playwright控制真实浏览器，与该交付应用进行交互，依据规范判断其是否满足需求。评估器不检查代码或构建日志，而是通过用户级操作、页面状态读取和运行时证据，最终输出三档质量标签：EXCELLENT（完全稳定满足）、USABLE（存在非核心缺陷但可玩）或UNUSABLE（无法完成核心玩法循环）。

主要创新点包括：1）设计了包含行为、空间、状态三个复杂度维度的B-S-T/L4功能点标注体系，以及基于结构规模和逻辑深度的D1-D4难度标签，用于语料库构建和分析。2）评估过程在真实浏览器中动态交互，验证游戏入口、输入响应、规则执行、状态转换、分数变化、终止与重启等完整行为。3）通过人类游戏评论验证，证明运行时标签与人类判断在可用率标准上高度一致。实验表明，最佳配置下可用率仅76.9%，优秀率更低至20.2%，揭示了当前编码智能体在完整需求满足上的显著差距。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估。实验设置基于111个冻结的WebGameBench任务，使用统一的部署协议，将编码代理生成的浏览器原生游戏构建并暴露为可访问的URL，然后由运行时评估器在真实浏览器中交互评估，输出EXCELLENT、USABLE或UNUSABLE标签。共评估了12个编码代理（覆盖Anthropic Claude Opus/Sonnet、OpenAI GPT-5.5、Google Gemini 3.1 Pro、DeepSeek-V4系列、Kimi K2.6/K2.5、GLM-5/5.1、腾讯Hy3）在14种配置下的表现，包括DeepSeek-V4 Pro/Flash的思考与非思考推理设置。主要指标包括覆盖率、可用率R_use和优秀率R_exc。结果显示，最佳配置（opus-4-7）达到最高可用率76.9%和优秀率20.2%，而最低配置（kimi-k2.5）仅有38.3%可用率和8.4%优秀率。任务按复杂度D1-D4分层，D1/D2任务可用率约75%，D3降至52%，D4仅12.6%。此外，在43个样本的人工审查子集上验证了运行时评估器与人类判断的一致性，在可用率标准下最高达85%准确率；优秀率标准下一致性较低（50.0%），表明自动评估更适合聚合可用率统计。

### Q5: 有什么可以进一步探索的点？

首先，WebGameBench的runtime evaluator虽然在可用率评估上与人类评审有一定一致性，但在三档质量标签（EXCELLENT、USABLE、UNUSABLE）的精确标注上仍有显著局限，未来可探索更细粒度的自动评估机制，例如结合多模态大模型进行视觉与交互行为联合分析，以缩小与人工评审的差距。其次，当前基准依赖固定模板生成的规格说明，且候选前置条件构造无法覆盖长周期、随机或多会话行为，这限制了评估的复杂性。改进方向包括引入动态需求生成或强化学习环境，让智能体在开放式、演化性需求下迭代构建应用，从而测试其长期规划与适应能力。最后，WebGameBench仅覆盖浏览器原生游戏场景，其结论不能直接推广到通用软件工程能力。未来的研究可扩展至更多交互式应用领域（如数据可视化、教育工具），并探索跨领域迁移评估方法，以验证编码智能体在需求到应用交付范式下的普适性瓶颈。

### Q6: 总结一下论文的主要内容

WebGameBench是一个评估编程智能体能否将结构化需求转化为可运行浏览器游戏的基准测试。每个任务提供冻结的Structured WebGame Specification，智能体生成源代码后通过统一协议构建、部署为浏览器可访问的游戏，运行时评估器在真实浏览器中验证输入处理、空间映射、规则执行、状态转换、终止条件和重启行为，并给出EXCELLENT、USABLE或UNUSABLE三级标签。在111个任务、12个智能体和14种配置下，最佳配置的可用率达到76.9%，但优秀率仅20.2%，说明达到最低可玩阈值远非完全满足需求。该基准首次实现了对交付应用运行时的独立人工验证。其核心贡献在于提供了一个紧凑、行为密集的测试平台，能够有效区分不同编程智能体从需求到可运行、可交互、可诊断软件工件的交付能力。
