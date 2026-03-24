---
title: "Dynamic analysis enhances issue resolution"
authors:
  - "Mingwei Liu"
  - "Zihao Wang"
  - "Zhenxi Chen"
  - "Zheng Pei"
  - "Yanlin Wang"
  - "Zibin Zheng"
date: "2026-03-23"
arxiv_id: "2603.22048"
arxiv_url: "https://arxiv.org/abs/2603.22048"
pdf_url: "https://arxiv.org/pdf/2603.22048v1"
categories:
  - "cs.SE"
tags:
  - "Code Agent"
  - "Automated Debugging"
  - "Dynamic Analysis"
  - "Agent Architecture"
  - "Tool-Augmented Reasoning"
  - "SWE-bench"
relevance_score: 9.0
---

# Dynamic analysis enhances issue resolution

## 原始摘要

Translating natural language descriptions into viable code fixes remains a fundamental challenge in software engineering. While the proliferation of agentic large language models (LLMs) has vastly improved automated repository-level debugging, current frameworks hit a ceiling when dealing with sophisticated bugs like implicit type degradations and complex polymorphic control flows. Because these methods rely heavily on static analysis and superficial execution feedback, they lack visibility into intermediate runtime states. Consequently, agents are forced into costly, speculative trial-and-error loops, wasting computational tokens without successfully isolating the root cause.
  To bridge this gap, we propose DAIRA (Dynamic Analysis-enhanced Issue Resolution Agent), a pioneering automated repair framework that natively embeds dynamic analysis into the agent's reasoning cycle. Driven by a Test Tracing-Driven methodology, DAIRA utilizes lightweight monitors to extract critical runtime data -- such as variable mutations and call stacks -- and synthesizes them into structured semantic reports. This mechanism fundamentally shifts the agent's behavior from blind guesswork to evidence-based, deterministic deduction. When powered by Gemini 3 Flash Preview, DAIRA establishes a new state-of-the-art (SOTA) performance, achieving a 79.4% resolution rate on the SWE-bench Verified dataset. Compared to existing baselines, our framework not only conquers highly complex defects but also cuts overall inference expenses by roughly 10% and decreases input token consumption by approximately 25%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的自动化软件问题修复中，由于缺乏对程序运行时状态的观察而导致的瓶颈问题。研究背景是软件工程中，通过自然语言描述（如GitHub Issues）来自动定位和修复代码缺陷是一个极具价值但充满挑战的任务。当前的主流方法依赖于静态代码分析和简单的执行反馈来构建智能体的工作上下文，例如通过关键词匹配或语义相似性检索代码片段。

然而，现有方法存在显著不足。首先，它们缺乏对程序中间运行时状态（如变量值变化、调用栈、条件执行路径）的“细粒度可观测性”。这导致智能体在面对复杂的动态缺陷（如隐式类型转换、多态控制流）时，如同在“隧道”中盲目探索，只能进行大量推测性的试错，无法准确定位根本原因。其次，静态视角无法捕捉仅在运行时才显现的行为，使得修复过程效率低下、成本高昂且成功率受限。

因此，本文要解决的核心问题是：如何将动态分析深度集成到基于LLM的智能体决策循环中，以提供程序执行的因果和状态感知视图，从而将修复过程从“盲目猜测”转变为“基于证据的确定性推理”。为此，论文提出了名为DAIRA的动态分析增强型问题解决框架，通过轻量级追踪工具捕获运行时数据并生成结构化语义报告，旨在从根本上提升智能体对复杂缺陷的诊断与修复能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类（自动化修复框架）和应用类（基于LLM的代理）两大类，并与本文提出的DAIRA框架形成对比。

在方法类研究中，SWE-agent开创了代理-计算机接口（ACI）范式，通过标准化命令（如浏览、编辑、执行）优化了LLM与环境的交互，成为自动化问题修复的基准。后续研究在此基础上进行了扩展：例如，规划类方法（如SWE-Search、CodeTree）集成了蒙特卡洛树搜索（MCTS）来优化推理过程；而经验驱动或多代理方法（如Live-SWE-agent、SWE-Exp、SWE-Debate）则利用自我进化或竞争动态来提升决策质量。然而，这些方法主要依赖静态分析（如代码检索、语义相似性匹配）和浅层的执行反馈（如最终错误输出），缺乏对程序运行时中间状态（如变量突变、调用堆栈）的细粒度观测能力，导致代理在复杂缺陷（如隐式类型退化、多态控制流）修复中陷入低效的试错循环。

在应用类研究中，基于大语言模型（LLM）的代理（如SWE-agent、OpenHand）已成为解决GitHub问题的主流范式。它们通过静态分析构建代码上下文，但受限于LLM的上下文窗口，无法处理大型紧密耦合的代码库，且在动态依赖（如多态、运行时状态变化）场景中表现不佳。近期实证研究（如Liu等人的工作）表明，LLM在从静态代码推理转向真实项目中的硬问题时，性能显著下降，这凸显了静态推理的不足。

本文提出的DAIRA框架与上述工作的核心区别在于，它首次将动态分析深度集成到代理推理循环中。DAIRA采用测试追踪驱动范式，通过轻量级监控工具捕获关键运行时数据（如变量突变、调用堆栈），并将其合成为结构化的语义报告，为代理提供“全景式”程序执行视图。这使得代理能从基于猜测的探索转变为基于证据的确定性推断，从而在复杂缺陷修复上实现更高的成功率（在SWE-bench Verified上达到79.4%的修复率），同时降低了推理开销和令牌消耗。因此，DAIRA弥补了现有方法在运行时可观测性方面的根本缺陷，代表了一种新的自动化修复范式。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为DAIRA的动态分析增强型问题解决框架来解决传统方法在修复复杂软件缺陷时因依赖静态分析和浅层执行反馈而导致的低效问题。其核心方法是将动态分析原生嵌入智能体的推理循环，通过“测试追踪驱动”的工作流程，使智能体能够基于运行时证据进行精确推理，而非盲目试错。

整体框架采用三阶段工作流。第一阶段为执行追踪阶段，智能体首先生成错误复现脚本和边界案例脚本，随后调用动态分析工具在隔离沙箱中执行这些脚本，捕获变量突变、调用栈等原始追踪日志，并通过语义分析模块将其转化为结构化的执行追踪报告。第二阶段为故障诊断阶段，智能体利用追踪报告进行关键函数规范总结和根因分析，通过交叉验证不同输入场景的报告，推断关键函数的实际工作角色和设计意图，从而精准定位偏离预期行为的根本原因。第三阶段为迭代修复与验证阶段，智能体基于根因生成候选补丁，并立即使用第一阶段生成的脚本进行动态验证，形成闭环；在提交最终解决方案前，还会进行回归测试以确保修复不引入副作用。

主要模块包括动态分析工具和追踪日志语义分析模块。动态分析工具基于定制的Hunter引擎实现，采用轻量级“触发-收集”追踪策略，通过标准化CLI集成到智能体动作空间。其关键技术包括：原生执行（通过自动钩子，无需智能体手动注入调试代码，直接执行标准Python脚本）、时空追踪过滤（按需激活追踪、白名单过滤库噪声、仅捕获关键调用与返回事件）以及自适应粒度迭代（在日志超出上下文窗口时动态降低追踪深度，避免信息过载）。追踪日志语义分析模块则利用LLM对原始日志进行深度解析，生成包含分层逻辑重建（生成可视化的ASCII执行树）、关键函数分析（阐明各组件在工作流中的角色）和工作流程介绍（自然语言概述执行事件）的结构化报告，弥合原始日志与高层逻辑之间的语义鸿沟。

创新点在于：首次将动态分析作为可调用工具深度集成到智能体推理循环中，实现了从猜测到证据驱动推理的范式转变；设计了测试追踪驱动的三阶段工作流，系统性协调了从追踪、诊断到修复验证的全过程；并通过轻量级、自适应且语义增强的动态分析设计，有效克服了复杂环境兼容性、日志噪声和信息过载等挑战，从而在提升问题解决率的同时显著降低了计算开销。

### Q4: 论文做了哪些实验？

本文实验围绕提出的DAIRA框架，在软件问题自动修复任务上进行了系统性评估。实验设置基于广泛使用的SWE-agent框架，仅采用其基础的代码搜索和编辑工具，并确保方法具有框架无关性。资源约束遵循标准配置：每个问题实例最多250步，预算上限为1.00美元。

**数据集/基准测试**：使用权威的SWE-bench Verified数据集，该数据集包含从12个流行Python开源仓库（如scikit-learn、Flask）中收集的500个经过人工验证的问题实例，专门用于评估自动问题修复系统。

**对比方法**：选择了多个当前最先进的基线方法，包括SWE-agent、Live-SWE-agent、Mini-SWE-agent、OpenHands以及集成了蒙特卡洛树搜索的SWE-search。

**主要结果与关键指标**：
1.  **整体性能（RQ1）**：以Gemini 3 Flash为基座模型的DAIRA取得了79.4%的解决率，在SWE-bench Verified上创造了新的最优性能，超越了此前最佳基线OpenHands（Claude Opus 4.5，77.6%）。当使用DeepSeek-V3基座模型时，DAIRA达到74.2%的解决率，相比使用同模型的原始SWE-agent（65.4%）绝对提升了8.8%。
2.  **独特解决能力**：在性能前五的配置中，有324个简单实例被所有顶级智能体共同解决。DAIRA的独特优势在于，它额外解决了9个其他所有基线方法均未能处理的复杂实例，证明了其处理边缘案例的能力。
3.  **效率与成本**：根据摘要信息，与现有基线相比，DAIRA将总体推理开销降低了约10%，并将输入令牌消耗减少了约25%。
4.  **案例研究**：通过对不同难度代表性问题的解决轨迹分析，实验展示了动态分析如何在故障定位和补丁生成两个关键阶段优化调试工作流，使其从逐步调查转向直接定位根本原因。

### Q5: 有什么可以进一步探索的点？

该论文提出的动态分析增强方法虽显著提升了复杂缺陷的定位与修复能力，但仍存在若干局限和可拓展方向。首先，其动态监控依赖于预设的轻量级探针，可能无法覆盖所有潜在运行时状态（如并发场景下的竞态条件），未来可探索自适应或可编程的监控机制，根据代码变更动态调整观测点。其次，框架目前主要针对单次提交的缺陷，未来可研究跨版本或持续集成环境中的增量式修复，并引入更精细的因果推理来区分缺陷的根本原因与副作用。此外，动态分析可能引入性能开销，需进一步优化监控效率，例如通过采样或选择性插桩。从方法论看，当前依赖单一LLM（Gemini），可探索多智能体协作框架，让不同Agent分别负责静态分析、动态追踪和补丁生成，通过辩论机制提升决策可靠性。最后，可将动态语义报告与代码知识图谱结合，实现更长期的缺陷模式学习与预防。

### Q6: 总结一下论文的主要内容

该论文针对现有基于大语言模型的自动化软件修复方法在处理复杂缺陷时存在的局限性，提出了首个深度集成动态分析的自动化问题解决框架DAIRA。核心问题是现有方法主要依赖静态分析和浅层执行反馈，缺乏对程序运行时中间状态的可见性，导致代理陷入低效的试错循环，难以定位如隐式类型转换、复杂多态控制流等动态缺陷。

DAIRA的方法核心是“测试追踪驱动”范式，通过轻量级监控工具在沙箱环境中捕获运行时关键数据（如变量变化、调用栈），并将其合成为结构化的语义追踪报告，作为代理推理的直接证据。这使代理的行为从盲目猜测转变为基于证据的确定性推断。

实验表明，在SWE-bench Verified基准测试中，DAIRA实现了79.4%的修复率，达到新的最优性能，尤其在中等和高难度任务上优势显著。此外，该方法通过精准的故障定位，减少了不必要的代码检索和尝试，相比基线方法降低了约25%的输入令牌消耗和约10%的整体推理开销。论文的核心贡献在于首次系统地将动态分析融入代理决策循环，为解决深层逻辑缺陷提供了关键的可观测性，显著提升了自动化修复的效能与效率。
